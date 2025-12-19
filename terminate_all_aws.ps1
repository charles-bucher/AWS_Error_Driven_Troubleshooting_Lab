# terminate_all_aws.ps1
# Loops through incidents and runs teardown.py

\ = Join-Path \ "incidents"
\ = Get-ChildItem -Path \ -Directory

foreach (\ in \) {
    \ = Join-Path \.FullName "scripts"
    \ = Join-Path \ "teardown.py"
    if (Test-Path \) {
        Write-Host "Tearing down \..."
        python \ \.Name terraform
    }
}
