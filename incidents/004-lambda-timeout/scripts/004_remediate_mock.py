"""
Mock script to simulate remediation for lab 004.
"""

import time

def remediate():
    resources = ["EC2 instance", "S3 bucket", "RDS database"]
    for resource in resources:
        print(f"[REMEDIATE] Fixing {resource}...")
        time.sleep(1)
        print(f"[REMEDIATE] {resource} is now healthy")

if __name__ == "__main__":
    remediate()
