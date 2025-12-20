# collect_evidence_mock.py
import sys

bucket = sys.argv[1]
print(f"[MOCK] Collecting evidence for bucket: {bucket}")

# Simulate bucket policy
print("[MOCK] No bucket policy")

# Simulate public access block
print("[MOCK] Public access block: None")

# Simulate objects
print("[MOCK] Objects in bucket: ['file1.txt', 'file2.txt']")
