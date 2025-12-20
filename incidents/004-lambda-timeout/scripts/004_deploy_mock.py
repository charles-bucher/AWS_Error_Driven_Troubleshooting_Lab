"""
Mock script to simulate deploying resources for lab 004.
"""

import time

def simulate_deploy():
    resources = ["EC2 instance", "S3 bucket", "RDS database"]
    for resource in resources:
        print(f"[DEPLOY] Deploying {resource} for lab 004...")
        time.sleep(1)
        print(f"[DEPLOY] {resource} deployment successful!")

if __name__ == "__main__":
    simulate_deploy()
