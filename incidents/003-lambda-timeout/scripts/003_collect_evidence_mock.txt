"""
Mock script to simulate collecting evidence for incident 003.
This does not touch real resources — generates fake logs and resource states.
"""

import json
import random
import time
from datetime import datetime

def generate_mock_resource_state():
    resources = ["EC2 instance", "S3 bucket", "RDS database", "Lambda function"]
    states = ["OK", "FAILED", "WARNING"]
    return {resource: random.choice(states) for resource in resources}

def generate_mock_logs(resource_states):
    logs = []
    timestamp = datetime.utcnow().isoformat() + "Z"
    for resource, state in resource_states.items():
        log_entry = {
            "timestamp": timestamp,
            "resource": resource,
            "status": state,
            "message": f"Mock event for {resource} in state {state}"
        }
        logs.append(log_entry)
    return logs

def collect_evidence():
    print("[INFO] Collecting mock evidence for incident 003...")
    time.sleep(1)
    resource_states = generate_mock_resource_state()
    logs = generate_mock_logs(resource_states)

    evidence = {
        "incident_id": "003",
        "collected_at": datetime.utcnow().isoformat() + "Z",
        "resource_states": resource_states,
        "logs": logs
    }

    # Save to JSON file
    filename = "incident_003_evidence_mock.json"
    with open(filename, "w") as f:
        json.dump(evidence, f, indent=4)

    print(f"[INFO] Mock evidence collected and saved to {filename}")

if __name__ == "__main__":
    collect_evidence()
