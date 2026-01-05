# list_scripts.ps1
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

Write-Output "=== Scripts in Repo ==="
Get-ChildItem -Path . -Include *.ps1,*.sh -Recurse | Select-Object FullName
