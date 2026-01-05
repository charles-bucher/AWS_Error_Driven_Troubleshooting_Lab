<#
.SYNOPSIS
  Scan all AWS Lambda functions for memory usage and recommend adjustments.
.DESCRIPTION
  Uses AWS Tools for PowerShell (AWSPowerShell module) to get Lambda functions,
  compares allocated memory vs. recent usage, and outputs recommendations.
#>

# Ensure AWS PowerShell module is installed
# Install-Module -Name AWSPowerShell.NetCore -Force

Import-Module AWSPowerShell.NetCore

Write-Host "=== Lambda Memory Optimization Audit ==="

# Get all Lambda functions
$functions = Get-LMFunctionList

foreach ($fn in $functions.Functions) {
    $fnName = $fn.FunctionName
    $memory = $fn.MemorySize

    # Get CloudWatch metrics for memory usage (last 7 days)
    $metrics = Get-CWMetricStatistics `
        -Namespace "AWS/Lambda" `
        -MetricName "MaxMemoryUsed" `
        -Dimensions @{ Name = "FunctionName"; Value = $fnName } `
        -Statistics Maximum `
        -StartTime (Get-Date).AddDays(-7) `
        -EndTime (Get-Date) `
        -Period 86400

    if ($metrics.Datapoints.Count -eq 0) {
        Write-Warning "$fnName: No CloudWatch data found."
        continue
    }

    $maxUsed = ($metrics.Datapoints | Measure-Object -Property Maximum -Maximum).Maximum
    $usagePct = [math]::Round(($maxUsed / $memory) * 100, 2)

    Write-Host "$fnName - Allocated Memory: $memory MB, Max Used: $maxUsed MB ($usagePct%)"

    if ($usagePct -lt 50) {
        Write-Host "  ⚡ Suggestion: Consider reducing memory allocation for cost efficiency."
    } elseif ($usagePct -gt 90) {
        Write-Host "  ⚡ Suggestion: Increase memory allocation to prevent throttling."
    } else {
        Write-Host "  ✅ Memory allocation looks good."
    }
}
