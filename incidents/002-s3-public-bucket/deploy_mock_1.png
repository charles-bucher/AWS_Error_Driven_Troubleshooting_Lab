# deploy_mock.py
import sys
import time

print("[INFO] (MOCK) Starting deployment for incident 002: S3 Public Bucket")

buckets = ["my-test-bucket"]

for bucket in buckets:
    print(f"[INFO] (MOCK) Creating S3 bucket: {bucket}...")
    time.sleep(1)
    print(f"[SUCCESS] (MOCK) Bucket '{bucket}' deployed successfully")

print("[INFO] (MOCK) Applying bucket policies...")
time.sleep(1)
print("[SUCCESS] (MOCK) Bucket policies applied: PublicRead for testing")

print("[INFO] (MOCK) Deployment completed for incident 002")
