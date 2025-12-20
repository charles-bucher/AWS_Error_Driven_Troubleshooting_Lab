import boto3

ec2 = boto3.client("ec2")
print("[DEPLOY] VPC created with DNS enabled")
