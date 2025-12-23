"""
Mock script to clean up resources for lab 004.
"""

import time

def teardown():
    resources = ["EC2 instance", "S3 bucket", "RDS database"]
    for resource in resources:
        print(f"[TEARDOWN] Removing {resource}...")
        time.sleep(1)
        print(f"[TEARDOWN] {resource} removed successfully")

if __name__ == "__main__":
    teardown()
