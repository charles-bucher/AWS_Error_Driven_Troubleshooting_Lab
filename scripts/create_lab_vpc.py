import boto3

# Config
REGION = "us-east-1"
VPC_CIDR = "10.0.0.0/16"
SUBNET_CIDR = "10.0.1.0/24"
VPC_NAME = "Lab-VPC"
SUBNET_NAME = "Lab-Subnet"
IGW_NAME = "Lab-IGW"
ROUTE_TABLE_NAME = "Lab-RouteTable"

ec2 = boto3.client("ec2", region_name=REGION)
resource = boto3.resource("ec2", region_name=REGION)

# 1️⃣ Create VPC
vpc_resp = ec2.create_vpc(CidrBlock=VPC_CIDR)
vpc_id = vpc_resp["Vpc"]["VpcId"]
print(f"[VPC] Created VPC {VPC_NAME} ({vpc_id})")

# Enable DNS
ec2.modify_vpc_attribute(VpcId=vpc_id, EnableDnsSupport={"Value": True})
ec2.modify_vpc_attribute(VpcId=vpc_id, EnableDnsHostnames={"Value": True})

# Add Name tag to VPC
ec2.create_tags(Resources=[vpc_id], Tags=[{"Key": "Name", "Value": VPC_NAME}])

# 2️⃣ Create Subnet
subnet_resp = ec2.create_subnet(VpcId=vpc_id, CidrBlock=SUBNET_CIDR)
subnet_id = subnet_resp["Subnet"]["SubnetId"]
ec2.create_tags(Resources=[subnet_id], Tags=[{"Key": "Name", "Value": SUBNET_NAME}])
print(f"[SUBNET] Created Subnet {SUBNET_NAME} ({subnet_id})")

# 3️⃣ Create Internet Gateway
igw_resp = ec2.create_internet_gateway()
igw_id = igw_resp["InternetGateway"]["InternetGatewayId"]
ec2.attach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id)
ec2.create_tags(Resources=[igw_id], Tags=[{"Key": "Name", "Value": IGW_NAME}])
print(f"[IGW] Created and attached Internet Gateway {IGW_NAME} ({igw_id})")

# 4️⃣ Create Route Table and route to IGW
rt_resp = ec2.create_route_table(VpcId=vpc_id)
rt_id = rt_resp["RouteTable"]["RouteTableId"]
ec2.create_tags(Resources=[rt_id], Tags=[{"Key": "Name", "Value": ROUTE_TABLE_NAME}])

# Create default route to IGW
ec2.create_route(RouteTableId=rt_id, DestinationCidrBlock="0.0.0.0/0", GatewayId=igw_id)

# Associate route table with subnet
ec2.associate_route_table(SubnetId=subnet_id, RouteTableId=rt_id)
print(f"[ROUTE] Route Table {ROUTE_TABLE_NAME} associated with {SUBNET_NAME}")

print("\n✅ Lab VPC setup complete!")
print(f"VPC ID: {vpc_id}, Subnet ID: {subnet_id}, IGW ID: {igw_id}, Route Table ID: {rt_id}")
