import boto3, sys

ec2 = boto3.client("ec2")
ec2.terminate_instances(InstanceIds=[sys.argv[1]])
print("[CLEANUP] Instance terminated")
