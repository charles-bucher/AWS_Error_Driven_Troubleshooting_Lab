# deploy_lambda.ps1
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

Write-Output "=== Deploying Lambda Functions ==="

$lambdaFolder = ".\lambdas"
$accountID = "722631436033"  # Replace with your AWS account
$lambdaRole = "YOUR_LAMBDA_ROLE"  # Replace with actual IAM role ARN or name

if (-Not (Test-Path $lambdaFolder)) {
    Write-Warning "Lambda folder not found. Exiting..."
    return
}

$zips = Get-ChildItem "$lambdaFolder\*.zip"
foreach ($zip in $zips) {
    $fname = $zip.BaseName
    Write-Output "Deploying Lambda $fname..."
    try {
        aws lambda update-function-code --function-name $fname --zip-file "fileb://$($zip.FullName)" | Out-Null
        Write-Output "[+] Updated Lambda $fname"
    } catch {
        Write-Output "[+] Creating Lambda $fname"
        aws lambda create-function `
            --function-name $fname `
            --runtime python3.11 `
            --role "arn:aws:iam::$accountID:role/$lambdaRole" `
            --handler "$fname.handler" `
            --zip-file "fileb://$($zip.FullName)" | Out-Null
    }
}

Write-Output "=== Lambda Deployment Completed ==="
