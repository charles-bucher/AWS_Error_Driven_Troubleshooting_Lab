# cleanup_lab.ps1
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

Write-Output "=== Cleaning up Lab Resources ==="

# Delete S3 buckets
$bucketsFile = ".\s3\buckets.txt"
if (Test-Path $bucketsFile) {
    Get-Content $bucketsFile | ForEach-Object {
        $bucket = $_.Trim()
        if ($bucket -ne "") {
            Write-Output "Deleting bucket $bucket..."
            aws s3 rb "s3://$bucket" --force
        }
    }
}

Write-Output "=== Lab Cleanup Complete ==="
