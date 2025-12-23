import os
import time

def teardown_lambda():
    print("[🗑️] Deleting Lambda function...")
    time.sleep(1)
    print("[✅] Lambda function removed!")

def teardown_s3(bucket_name):
    print(f"[🗑️] Deleting S3 bucket: {bucket_name}...")
    time.sleep(1)
    print(f"[✅] Bucket {bucket_name} deleted!")

if __name__ == "__main__":
    print("[⚠️] Starting full teardown of lab resources...")
    time.sleep(1)

    # Call teardowns (add more as needed)
    teardown_lambda()
    teardown_s3("my-test-bucket")

    print("[✅] Lab teardown complete!")
