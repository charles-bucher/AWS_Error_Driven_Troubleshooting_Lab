import boto3, sys

ec2 = boto3.client("ec2")
ec2.delete_vpc(VpcId=sys.argv[1])
print("[CLEANUP] VPC deleted")
