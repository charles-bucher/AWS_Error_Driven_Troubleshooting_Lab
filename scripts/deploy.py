# scripts/deploy.py
# Deploy EC2 instance with existing key AEDT

import boto3

KEY_NAME = "AEDT"
INSTANCE_TYPE = "t2.micro"
AMI_ID = "ami-0c94855ba95c71c99"  # Amazon Linux 2 US East 1
REGION = "us-east-1"

ec2 = boto3.resource("ec2", region_name=REGION)

print(f"[DEPLOY] Would create EC2 instance in {REGION} with key {KEY_NAME}")

# Uncomment the below to actually deploy (free tier eligible)
# instance = ec2.create_instances(
#     ImageId=AMI_ID,
#     InstanceType=INSTANCE_TYPE,
#     KeyName=KEY_NAME,
#     MinCount=1,
#     MaxCount=1
# )[0]
# print(f"[DEPLOY] Created EC2 Instance ID: {instance.id}")
