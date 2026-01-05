# deploy.ps1 - Spin up entire AWS_Error_Driven_Troubleshooting_Lab in PowerShell
# Run this in PowerShell (Windows 10/11)
# Make sure AWS CLI is configured, Python 3 installed, and you have Lambda IAM roles

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

Write-Host "=== Starting full lab deployment ===`n"

# 1️⃣ Pull latest repo updates
Write-Host "[1/6] Updating local repo..."
git pull origin main

# 2️⃣ Install Python dependencies
Write-Host "[2/6] Installing Python dependencies..."
if (Test-Path "requirements.txt") {
    python -m pip install -r requirements.txt
}

# 3️⃣ Deploy Linux broken-systemd lab (simulate broken EC2 service)
Write-Host "[3/6] Deploying Linux lab scripts..."
if (Test-Path "linux/broken-systemd-service/setup.sh") {
    Write-Host "Note: Linux scripts require Bash; skipping on PowerShell"
}

# 4️⃣ Deploy AWS Lambda functions
Write-Host "[4/6] Deploying Lambda functions..."
if (Test-Path "lambdas") {
    Get-ChildItem -Path "lambdas" -Filter "*.zip" | ForEach-Object {
        $fname = $_.BaseName
        Write-Host "Deploying Lambda $fname..."
        try {
            aws lambda update-function-code --function-name $fname --zip-file ("fileb://{0}" -f $_.FullName)
        }
        catch {
            Write-Host "Updating failed; trying to create function..."
            aws lambda create-function --function-name $fname `
                --runtime python3.11 `
                --role "arn:aws:iam::YOUR_ACCOUNT_ID:role/YOUR_LAMBDA_ROLE" `
                --handler "$fname.handler" `
                --zip-file ("fileb://{0}" -f $_.FullName)
        }
    }
}

# 5️⃣ Run automation scripts
Write-Host "[5/6] Running automation scripts..."
if (Test-Path "scripts") {
    Get-ChildItem -Path "scripts" -Filter "*.ps1" | ForEach-Object {
        Write-Host "Running $($_.Name)..."
        & $_.FullName
    }
    # If you still have bash scripts, you can optionally call Git Bash to run them
    Get-ChildItem -Path "scripts" -Filter "*.sh" | ForEach-Object {
        Write-Host "Skipping bash script $($_.Name); run in Git Bash if needed"
    }
}

# 6️⃣ Deploy S3 buckets and sample files
Write-Host "[6/6] Creating S3 buckets and uploading test files..."
if (Test-Path "s3/buckets.txt") {
    Get-Content "s3/buckets.txt" | ForEach-Object {
        $bucket = $_.Trim()
        if ($bucket -ne "") {
            Write-Host "Creating bucket $bucket..."
            try {
                aws s3 mb "s3://$bucket"
            }
            catch {
                Write-Host "$bucket may already exist"
            }
            if (Test-Path "s3/files") {
                aws s3 cp "s3/files/" "s3://$bucket/" --recursive
            }
        }
    }
}

Write-Host "`n✅ Lab deployment complete! Check AWS console for resources."
