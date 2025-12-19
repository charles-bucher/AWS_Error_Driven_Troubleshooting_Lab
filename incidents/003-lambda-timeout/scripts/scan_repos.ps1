# scan_repos.ps1
# Scans all folders and files under the REPOS directory
# Reports missing critical files and empty folders

$basePath = "C:\Users\buche\docs\Desktop\REPOS"

# Define critical files expected in repo root
$requiredRoot = @("README.md", "GUARDRAILS.md")

# Define critical files for incident folders
$requiredIncidentRootFiles = @("incident.md", "deploy.py", "teardown.py", "collect_evidence.py")
$requiredIncidentStructure = @{
    "terraform"   = @("main.tf", "variables.tf", "outputs.tf")
    "break"       = @("break.py", "app.py")
    "detect"      = @("detect.tf")
    "remediate"   = @("remediate.py")
    "verify"      = @("verify.py")
}

# Define critical files for scripts folder
$requiredScripts = @("audit_log.py", "fix_all_repos.ps1")

Write-Host "=== Scanning $basePath ==="

# Check root-level files
foreach ($file in $requiredRoot) {
    $path = Join-Path $basePath $file
    if (!(Test-Path $path)) {
        Write-Host "Missing root file: $file"
    }
}

# Scan all subfolders
$subfolders = Get-ChildItem -Path $basePath -Directory
foreach ($folder in $subfolders) {
    Write-Host "=== Checking $($folder.Name) ==="

    $missingItems = @()

    switch ($folder.Name) {
        "incidents" {
            $incidentFolders = Get-ChildItem -Path $folder.FullName -Directory
            foreach ($incident in $incidentFolders) {
                Write-Host " -> Incident: $($incident.Name)"
                $incidentMissing = @()

                foreach ($file in $requiredIncidentRootFiles) {
                    $path = Join-Path $incident.FullName $file
                    if (!(Test-Path $path)) {
                        $incidentMissing += "Missing root file: $file"
                    }
                }

                foreach ($sub in $requiredIncidentStructure.Keys) {
                    $subPath = Join-Path $incident.FullName $sub
                    if (!(Test-Path $subPath)) {
                        $incidentMissing += "Missing folder: $sub"
                    } else {
                        foreach ($file in $requiredIncidentStructure[$sub]) {
                            $filePath = Join-Path $subPath $file
                            if (!(Test-Path $filePath)) {
                                $incidentMissing += "Missing in $sub/: $file"
                            }
                        }
                    }
                }

                if ($incidentMissing.Count -eq 0) {
                    Write-Host "    All critical files present ✅"
                } else {
                    $incidentMissing | ForEach-Object { Write-Host "    - $_" }
                }
            }
        }
        "scripts" {
            foreach ($file in $requiredScripts) {
                $path = Join-Path $folder.FullName $file
                if (!(Test-Path $path)) {
                    $missingItems += "Missing script: $file"
                }
            }
        }
        default {
            # For other folders, just check if empty
            if ((Get-ChildItem -Path $folder.FullName).Count -eq 0) {
                $missingItems += "Folder is empty"
            }
        }
    }

    if ($missingItems.Count -eq 0) {
        Write-Host "All critical files present ✅"
    } else {
        $missingItems | ForEach-Object { Write-Host " - $_" }
    }
    Write-Host ""
}