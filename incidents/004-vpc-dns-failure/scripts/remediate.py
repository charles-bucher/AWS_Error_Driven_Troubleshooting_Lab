import boto3, sys

ec2 = boto3.client("ec2")
vpc_id = sys.argv[1]

ec2.modify_vpc_attribute(
    VpcId=vpc_id,
    EnableDnsSupport={"Value": True}
)

print("[FIXED] DNS restored")
