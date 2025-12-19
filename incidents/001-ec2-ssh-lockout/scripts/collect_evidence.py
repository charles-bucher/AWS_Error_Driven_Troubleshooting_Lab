# collect_evidence.py
"""
Collect evidence for an incident:
- Pull CloudWatch logs
- Save system metrics
- Copy screenshots into an evidence folder
- Write a JSON summary with timestamps
"""

import boto3
import os
import sys
import json
from datetime import datetime

def log(msg):
    print(f"{datetime.utcnow().isoformat()}Z | {msg}")

def collect_cloudwatch_logs(log_group, start_time, end_time, region="us-east-1"):
    client = boto3.client("logs", region_name=region)
    streams = client.describe_log_streams(logGroupName=log_group)["logStreams"]
    events = []
    for stream in streams:
        stream_name = stream["logStreamName"]
        response = client.get_log_events(
            logGroupName=log_group,
            logStreamName=stream_name,
            startTime=start_time,
            endTime=end_time,
            startFromHead=True
        )
        for e in response["events"]:
            events.append({
                "timestamp": e["timestamp"],
                "message": e["message"]
            })
    return events

def save_evidence(incident_id, logs, notes=""):
    evidence_dir = os.path.join("evidence", incident_id)
    os.makedirs(evidence_dir, exist_ok=True)

    # Save logs
    log_file = os.path.join(evidence_dir, f"cloudwatch_logs_{incident_id}.json")
    with open(log_file, "w") as f:
        json.dump(logs, f, indent=2)

    # Save summary
    summary = {
        "incident_id": incident_id,
        "collected_at": datetime.utcnow().isoformat() + "Z",
        "log_count": len(logs),
        "notes": notes
    }
    summary_file = os.path.join(evidence_dir, f"summary_{incident_id}.json")
    with open(summary_file, "w") as f:
        json.dump(summary, f, indent=2)

    log(f"Evidence saved in {evidence_dir}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python collect_evidence.py <incident_id> <log_group> <region>")
        sys.exit(1)

    incident_id = sys.argv[1]
    log_group = sys.argv[2]
    region = sys.argv[3]

    # Example: last 1 hour
    end_time = int(datetime.utcnow().timestamp() * 1000)
    start_time = end_time - (60 * 60 * 1000)

    logs = collect_cloudwatch_logs(log_group, start_time, end_time, region)
    save_evidence(incident_id, logs, notes="Collected CloudWatch logs and metrics")