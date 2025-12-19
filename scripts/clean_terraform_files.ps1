# Get all directories (your repos) in the current folder
$repos = Get-ChildItem -Directory

foreach ($repo in $repos) {
    Write-Host "`n--- Processing repo: $($repo.Name) ---`n"

    # Change to repo folder
    Set-Location $repo.FullName

    # Remove .terraform directories if they exist
    $terraformDirs = Get-ChildItem -Directory -Recurse -Force -Filter ".terraform" -ErrorAction SilentlyContinue
    foreach ($dir in $terraformDirs) {
        Remove-Item -Recurse -Force $dir.FullName
        Write-Host "Removed $($dir.FullName)"
    }

    # Remove terraform.tfstate files if they exist
    $tfstateFiles = Get-ChildItem -File -Recurse -Force -Filter "terraform.tfstate" -ErrorAction SilentlyContinue
    foreach ($file in $tfstateFiles) {
        Remove-Item -Force $file.FullName
        Write-Host "Removed $($file.FullName)"
    }

    # Go back to parent folder
    Set-Location ..
}

Write-Host "`n✅ All repos cleaned safely."
