import sys

# Check if bucket name argument is provided
if len(sys.argv) < 2:
    print("[ERROR] Please provide a bucket name as an argument.")
    print("Usage: python collect_evidence_mock.py <bucket_name>")
    sys.exit(1)

bucket = sys.argv[1]

# Mock evidence collection
print(f"[INFO] Starting evidence collection for bucket: {bucket}")

# Mock bucket policy
mock_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": f"arn:aws:s3:::{bucket}/*"
        }
    ]
}

# Mock public access block
mock_public_access_block = {
    "BlockPublicAcls": False,
    "IgnorePublicAcls": False,
    "BlockPublicPolicy": False,
    "RestrictPublicBuckets": False
}

print("[INFO] Collected bucket policy (mock):")
print(mock_policy)

print("[INFO] Collected public access block settings (mock):")
print(mock_public_access_block)

print(f"[SUCCESS] Evidence collection completed for bucket: {bucket}")
