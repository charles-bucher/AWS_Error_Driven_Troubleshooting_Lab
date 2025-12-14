import os

# Base lab folder
base_dir = "AWS_Error_Driven_Troubleshooting_Lab"

# Incident names
incidents = [
    "incident_001_ec2_unreachable",
    "incident_002_s3_permission",
    "incident_003_lambda_failure"
]

# Scripts for each incident
script_files = ["deploy.py", "break.py", "collect_evidence.py", "teardown.py"]

# Create main folders
os.makedirs(base_dir, exist_ok=True)
os.makedirs(os.path.join(base_dir, "templates"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "docs"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "config"), exist_ok=True)

for incident in incidents:
    incident_path = os.path.join(base_dir, "incidents", incident)
    scripts_path = os.path.join(incident_path, "scripts")
    evidence_path = os.path.join(incident_path, "evidence")
    screenshots_path = os.path.join(incident_path, "screenshots")
    
    os.makedirs(scripts_path, exist_ok=True)
    os.makedirs(evidence_path, exist_ok=True)
    os.makedirs(screenshots_path, exist_ok=True)
    
    # Create empty stub scripts
    for script in script_files:
        script_file_path = os.path.join(scripts_path, script)
        if not os.path.exists(script_file_path):
            with open(script_file_path, "w") as f:
                f.write(f"# {script} for {incident}\n# TODO: implement\n\n")
    
    # Create README.md
    readme_path = os.path.join(incident_path, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, "w") as f:
            f.write(f"# {incident}\n\n")
            f.write("## Incident Summary\n- TODO\n\n")
            f.write("## Symptoms\n- TODO\n\n")
            f.write("## Triage Steps\n- TODO\n\n")
            f.write("## Evidence Collected\n- TODO\n\n")
            f.write("## Root Cause\n- TODO\n\n")
            f.write("## Resolution\n- TODO\n\n")
            f.write("## Lessons Learned\n- TODO\n")


