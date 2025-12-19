# deploy.py
"""
Deploy infrastructure for an incident lab using Terraform.
This script:
- Runs 'terraform init' and 'terraform apply'
- Logs the deployment with timestamp
- Stores outputs for later use (e.g., SG ID, instance ID)
"""

import subprocess
import sys
import os
import json
from datetime import datetime

def log(msg):
    print(f"{datetime.utcnow().isoformat()}Z | {msg}")

def run_terraform(path):
    # Ensure path exists
    if not os.path.isdir(path):
        log(f"Terraform path not found: {path}")
        sys.exit(1)

    # Initialize Terraform
    log("Running terraform init...")
    subprocess.run(["terraform", "init"], cwd=path, check=True)

    # Apply Terraform
    log("Running terraform apply...")
    subprocess.run(["terraform", "apply", "-auto-approve"], cwd=path, check=True)

    # Capture outputs
    log("Capturing terraform outputs...")
    result = subprocess.run(
        ["terraform", "output", "-json"],
        cwd=path,
        capture_output=True,
        text=True,
        check=True
    )
    outputs = json.loads(result.stdout)

    return outputs

def save_outputs(incident_id, outputs):
    evidence_dir = os.path.join("evidence", incident_id)
    os.makedirs(evidence_dir, exist_ok=True)
    out_file = os.path.join(evidence_dir, f"deploy_outputs_{incident_id}.json")
    with open(out_file, "w") as f:
        json.dump(outputs, f, indent=2)
    log(f"Outputs saved to {out_file}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python deploy.py <incident_id> <terraform_path>")
        sys.exit(1)

    incident_id = sys.argv[1]
    tf_path = sys.argv[2]

    log(f"Starting deployment for incident {incident_id}")
    outputs = run_terraform(tf_path)
    save_outputs(incident_id, outputs)
    log("Deployment complete.")