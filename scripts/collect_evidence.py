import os
from datetime import datetime

INCIDENT_DIR = "evidence"
os.makedirs(INCIDENT_DIR, exist_ok=True)

# Simple zero-cost evidence simulation
with open(os.path.join(INCIDENT_DIR, "incident_summary.txt"), "w") as f:
    f.write(f"Incident simulated at {datetime.now()}\n")
    f.write("SSH access removed from EC2 Security Group to simulate outage.\n")

print(f"[EVIDENCE] Incident evidence saved in {INCIDENT_DIR}/")
