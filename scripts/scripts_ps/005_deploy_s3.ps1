# deploy_s3.ps1
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

Write-Output "=== Deploying S3 Buckets ==="

$bucketsFile = ".\s3\buckets.txt"
$filesPath = ".\s3\files"

if (-Not (Test-Path $bucketsFile)) {
    Write-Warning "Buckets file not found. Exiting..."
    return
}

Get-Content $bucketsFile | ForEach-Object {
    $bucket = $_.Trim()
    if ($bucket -eq "") { return }

    Write-Output "Creating bucket $bucket..."
    try {
        aws s3 mb "s3://$bucket" | Out-Null
    } catch {
        Write-Warning "$bucket may already exist or failed to create."
    }

    if (Test-Path $filesPath) {
        Write-Output "Uploading files to $bucket..."
        aws s3 cp "$filesPath\" "s3://$bucket/" --recursive | Out-Null
    }
}

Write-Output "=== S3 Deployment Completed ==="
