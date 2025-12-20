# deploy_mock.py - Incident 002 S3 Public Bucket (Mock)
import time

print("[MOCK] Starting deployment for incident 002 - S3 public bucket...")

# Simulate creating a bucket
bucket_name = "my-test-bucket"
print(f"[MOCK] Creating bucket: {bucket_name} ...")
time.sleep(1)

# Simulate applying public access policy
print(f"[MOCK] Applying public access policy to {bucket_name} ...")
time.sleep(1)

# Simulate uploading test objects
print(f"[MOCK] Uploading sample objects to {bucket_name} ...")
time.sleep(1)

# Simulate finalizing deployment
print("[MOCK] Deployment complete for incident 002.")
