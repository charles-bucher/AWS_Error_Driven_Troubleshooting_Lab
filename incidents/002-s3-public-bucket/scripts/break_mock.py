#!/usr/bin/env python3
"""
break_mock.py
Mock break script for incident 002 - S3 public bucket
"""

import sys

# Check for bucket name argument
if len(sys.argv) < 2:
    print("[ERROR] Please provide the bucket name as an argument.")
    print("Usage: python break_mock.py <bucket-name>")
    sys.exit(1)

bucket = sys.argv[1]

# Mock breaking steps
print(f"[INFO] (MOCK) Starting to break S3 bucket: {bucket}")

# Example simulated break actions
print(f"[INFO] (MOCK) Removing bucket policy for {bucket}")
print(f"[INFO] (MOCK) Making bucket publicly readable")
print(f"[INFO] (MOCK) Disabling Public Access Block for {bucket}")

# Success
print(f"[SUCCESS] (MOCK) Incident 002 environment broken for bucket: {bucket}")
