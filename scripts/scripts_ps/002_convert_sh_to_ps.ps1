# lab_fix.ps1 - PowerShell native version

# Variables
$OLD_PATH = "/old/path"               # Original (incorrect) path
$NEW_PATH = "/new/path"               # Correct path
$UNIT_FILE = "some-unit-file.service" # The file to fix

Write-Output "=== Running lab_fix.ps1 ==="

# Check if the unit file exists
if (-Not (Test-Path $UNIT_FILE)) {
    Write-Warning "Unit file '$UNIT_FILE' not found. Skipping..."
    return
}

# Read the file contents
$unitContent = Get-Content $UNIT_FILE

# Check for incorrect ExecStart and fix it
if ($unitContent -match [regex]::Escape($OLD_PATH)) {
    Write-Output "[+] Incorrect ExecStart found. Fixing..."
    
    $unitContent = $unitContent -replace [regex]::Escape($OLD_PATH), $NEW_PATH
    
    $unitContent | Set-Content $UNIT_FILE
    Write-Output "[+] ExecStart path updated to '$NEW_PATH'"
} else {
    Write-Output "[+] ExecStart path already correct. Nothing to do."
}

Write-Output "=== lab_fix.ps1 completed ==="
