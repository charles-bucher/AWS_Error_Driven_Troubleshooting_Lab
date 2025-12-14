import boto3

# Configuration
REGION = "us-east-1"
VPC_CIDR = "10.0.0.0/16"
VPC_NAME = "Lab-VPC"

ec2 = boto3.client("ec2", region_name=REGION)

# Create VPC
response = ec2.create_vpc(CidrBlock=VPC_CIDR)
vpc_id = response["Vpc"]["VpcId"]

# Add Name tag
ec2.create_tags(Resources=[vpc_id], Tags=[{"Key": "Name", "Value": VPC_NAME}])

# Enable DNS support
ec2.modify_vpc_attribute(VpcId=vpc_id, EnableDnsSupport={"Value": True})
ec2.modify_vpc_attribute(VpcId=vpc_id, EnableDnsHostnames={"Value": True})

print(f"[VPC] Created VPC {VPC_NAME} ({vpc_id}) in {REGION}")
