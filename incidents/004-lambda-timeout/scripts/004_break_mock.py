"""
Mock script to simulate breaking resources for lab 004.
"""

import random
import time

def simulate_break():
    resources = ["EC2 instance", "S3 bucket", "RDS database"]
    resource = random.choice(resources)
    print(f"[ALERT] Simulating break on {resource} for lab 004...")
    time.sleep(1)
    print(f"[ALERT] {resource} is now in a failed state!")

if __name__ == "__main__":
    simulate_break()
