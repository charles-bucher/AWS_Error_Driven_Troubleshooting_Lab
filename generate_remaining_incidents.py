import os

# Define incidents and folder structure
incidents = {
    "002_s3_permission": ["break.py", "collect_evidence.py", "deploy.py", "teardown.py"],
    "003_lambda_failure": ["break.py", "collect_evidence.py", "deploy.py", "teardown.py"],
    "004_dynamodb_failure": ["break.py", "collect_evidence.py", "deploy.py", "teardown.py"]
}

base_path = os.path.join(os.getcwd(), "incidents")

# Template content for scripts
script_template = """\"\"\"
{script_name} for {incident_name}
\"\"\"

def main():
    print("This is a placeholder for {script_name} in {incident_name}")

if __name__ == "__main__":
    main()
"""

# Template for Markdown files
md_template = "# {file_name}\n\nThis is a placeholder for {file_name} in {incident_name}."

# Generate folders and files
for incident, scripts in incidents.items():
    incident_path = os.path.join(base_path, incident)
    
    # Create main incident folder
    os.makedirs(incident_path, exist_ok=True)
    
    # Create scripts folder
    scripts_path = os.path.join(incident_path, "scripts")
    os.makedirs(scripts_path, exist_ok=True)
    
    # Create evidence/screenshots folders
    evidence_path = os.path.join(incident_path, "evidence", "screenshots")
    os.makedirs(evidence_path, exist_ok=True)
    
    # Create prevention and remediation folders
    prevention_path = os.path.join(incident_path, "prevention")
    os.makedirs(prevention_path, exist_ok=True)
    remediation_path = os.path.join(incident_path, "remediation")
    os.makedirs(remediation_path, exist_ok=True)
    
    # Create scripts
    for script in scripts:
        script_file_path = os.path.join(scripts_path, script)
        with open(script_file_path, "w") as f:
            f.write(script_template.format(script_name=script, incident_name=incident))
    
    # Create README.md
    with open(os.path.join(incident_path, "README.md"), "w") as f:
        f.write(md_template.format(file_name="README.md", incident_name=incident))
    
    # Create guardrails.md
    with open(os.path.join(prevention_path, "guardrails.md"), "w") as f:
        f.write(md_template.format(file_name="guardrails.md", incident_name=incident))
    
    # Create fix.md
    with open(os.path.join(remediation_path, "fix.md"), "w") as f:
        f.write(md_template.format(file_name="fix.md", incident_name=incident))

print("All incidents 2, 3, and 4 folders and scripts have been generated!")
