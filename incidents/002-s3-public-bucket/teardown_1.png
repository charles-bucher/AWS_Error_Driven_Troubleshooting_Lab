import boto3, sys

s3 = boto3.resource("s3")
bucket = s3.Bucket(sys.argv[1])
bucket.objects.all().delete()
bucket.delete()
print("[CLEANUP] Bucket removed")
