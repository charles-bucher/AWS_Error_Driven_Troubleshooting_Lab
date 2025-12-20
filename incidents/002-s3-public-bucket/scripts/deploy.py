import boto3, sys

s3 = boto3.client("s3")
bucket = sys.argv[1]

s3.create_bucket(Bucket=bucket)
print("[DEPLOYED] Bucket created")
