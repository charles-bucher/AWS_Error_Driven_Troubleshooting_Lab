import boto3, sys

ec2 = boto3.client("ec2")
vpc_id = sys.argv[1]

attrs = ec2.describe_vpc_attribute(
    VpcId=vpc_id,
    Attribute="enableDnsSupport"
)

print(attrs)
