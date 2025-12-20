import sys
import time

# Check for a bucket argument
if len(sys.argv) < 2:
    print("Usage: python collect_evidence_mock.py <bucket_name>")
    sys.exit(1)

bucket = sys.argv[1]

print(f"[INFO] Starting evidence collection for bucket: {bucket}")

# Mock steps
steps = [
    "Checking bucket policies...",
    "Listing objects in the bucket...",
    "Checking public access settings...",
    "Capturing mock screenshots...",
    "Generating report..."
]

for step in steps:
    print(f"[MOCK] {step}")
    time.sleep(0.5)  # simulate some delay

print(f"[SUCCESS] Evidence collection complete for bucket: {bucket}")
print("[MOCK] Screenshots saved to /mock_screenshots folder")
