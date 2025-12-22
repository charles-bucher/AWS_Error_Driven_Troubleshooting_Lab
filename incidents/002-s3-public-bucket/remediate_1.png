import boto3, sys

s3 = boto3.client("s3")
bucket = sys.argv[1]

s3.delete_bucket_policy(Bucket=bucket)
s3.put_public_access_block(
    Bucket=bucket,
    PublicAccessBlockConfiguration={
        "BlockPublicAcls": True,
        "IgnorePublicAcls": True,
        "BlockPublicPolicy": True,
        "RestrictPublicBuckets": True,
    },
)

print("[FIXED] Bucket secured")
