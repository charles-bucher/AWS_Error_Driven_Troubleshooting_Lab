import os
import sys
import time

def remediate_lambda_timeout():
    print("[✅] Remediating Lambda timeout issue...")
    time.sleep(1)
    print("[🔧] Reset Lambda function timeout to 15 seconds")
    time.sleep(0.5)
    print("[✅] Lambda remediation complete!")

def remediate_s3_public_bucket(bucket_name):
    print(f"[✅] Remediating public S3 bucket: {bucket_name}")
    time.sleep(1)
    print(f"[🔒] Removing public access policies from {bucket_name}")
    time.sleep(0.5)
    print(f"[✅] Bucket {bucket_name} is now private")

if __name__ == "__main__":
    # Example CLI usage: python remediate_mock.py lambda
    if len(sys.argv) < 2:
        print("Usage: python remediate_mock.py <resource> [bucket_name]")
        sys.exit(1)

    resource = sys.argv[1]

    if resource == "lambda":
        remediate_lambda_timeout()
    elif resource == "s3":
        if len(sys.argv) < 3:
            print("Please provide a bucket name for S3 remediation.")
            sys.exit(1)
        bucket_name = sys.argv[2]
        remediate_s3_public_bucket(bucket_name)
    else:
        print(f"[❌] Unknown resource: {resource}")
