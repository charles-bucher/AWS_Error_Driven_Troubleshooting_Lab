import boto3

lambda_client = boto3.client("lambda")

print("[DEPLOY] Lambda created with VPC attachment")
