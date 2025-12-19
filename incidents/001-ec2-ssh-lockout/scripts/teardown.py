# teardown.py
"""
Tear down infrastructure for an incident lab using Terraform.
This script:
- Runs 'terraform destroy' in the incident's terraform folder
- Logs the teardown with timestamp
- Saves a summary JSON in evidence/<incident_id>/
"""

import subprocess
import sys
import os
import json
from datetime import datetime

def log(msg):
    print(f"{datetime.utcnow().isoformat()}Z | {msg}")

def run_terraform_destroy(path):
    if not os.path.isdir(path):
        log(f"Terraform path not found: {path}")
        sys.exit(1)

    log("Running terraform destroy...")
    subprocess.run(["terraform", "destroy", "-auto-approve"], cwd=path, check=True)
    log("Terraform destroy complete.")

def save_summary(incident_id):
    evidence_dir = os.path.join("evidence", incident_id)
    os.makedirs(evidence_dir, exist_ok=True)

    summary = {
        "incident_id": incident_id,
        "teardown_at": datetime.utcnow().isoformat() + "Z",
        "status": "destroyed"
    }
    summary_file = os.path.join(evidence_dir, f"teardown_{incident_id}.json")
    with open(summary_file, "w") as f:
        json.dump(summary, f, indent=2)

    log(f"Teardown summary saved to {summary_file}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python teardown.py <incident_id> <terraform_path>")
        sys.exit(1)

    incident_id = sys.argv[1]
    tf_path = sys.argv[2]

    log(f"Starting teardown for incident {incident_id}")
    run_terraform_destroy(tf_path)
    save_summary(incident_id)
    log("Teardown complete.")