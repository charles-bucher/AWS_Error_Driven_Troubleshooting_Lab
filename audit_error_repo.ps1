# audit_error_repo.ps1
# Checks AWS_Error_Driven_Troubleshooting_Lab for all critical files/folders

$basePath = "C:\Users\buche\docs\Desktop\REPOS\AWS_Error_Driven_Troubleshooting_Lab"

Write-Host "=== Auditing $basePath ==="

# Critical root-level files/folders
$requiredRoot = @(
    "README.md",
    "LICENSE",
    "diagrams",
    "incidents",
    "scripts",
    "templates",
    "docs",
    "create_lab_structure.py",
    "spin_incidents.py",
    "terminate_all_aws.ps1"
)

# Critical files inside each incident folder
$requiredIncidentScripts = @("deploy.py", "break.py", "collect_evidence.py", "teardown.py")
$requiredIncidentDocs = @("README.md")

# Check root-level
foreach ($item in $requiredRoot) {
    $path = Join-Path $basePath $item
    if (!(Test-Path $path)) {
        Write-Host "Missing root item: $item"
    }
}

# Check incidents
$incidentsPath = Join-Path $basePath "incidents"
if (Test-Path $incidentsPath) {
    $incidentFolders = Get-ChildItem -Path $incidentsPath -Directory
    foreach ($incident in $incidentFolders) {
        Write-Host " -> Checking incident: $($incident.Name)"
        $missingItems = @()

        # Check scripts folder
        $scriptsPath = Join-Path $incident.FullName "scripts"
        if (!(Test-Path $scriptsPath)) {
            $missingItems += "Missing folder: scripts"
        } else {
            foreach ($file in $requiredIncidentScripts) {
                $filePath = Join-Path $scriptsPath $file
                if (!(Test-Path $filePath)) {
                    $missingItems += "Missing in scripts/: $file"
                }
            }
        }

        # Check evidence folder
        $evidencePath = Join-Path $incident.FullName "evidence"
        if (!(Test-Path $evidencePath)) {
            $missingItems += "Missing folder: evidence"
        }

        # Check incident README
        foreach ($doc in $requiredIncidentDocs) {
            $docPath = Join-Path $incident.FullName $doc
            if (!(Test-Path $docPath)) {
                $missingItems += "Missing incident doc: $doc"
            }
        }

        if ($missingItems.Count -eq 0) {
            Write-Host "    All critical files present ✅"
        } else {
            $missingItems | ForEach-Object { Write-Host "    - $_" }
        }
    }
} else {
    Write-Host "Missing folder: incidents"
}