import boto3
import time
import os

# INCIDENT CONFIG
incidents = [
    "incident_001_ec2_unreachable",
    "incident_002_s3_permission",
    "incident_003_lambda_failure"
]

REGION = "us-east-1"
AMI_ID = "ami-0c94855ba95c71c99"  # Amazon Linux 2
INSTANCE_TYPE = "t2.micro"
KEY_NAME = "AEDT"

# Create boto3 clients
ec2_client = boto3.client("ec2", region_name=REGION)
ec2_resource = boto3.resource("ec2", region_name=REGION)

# Loop over incidents
for incident in incidents:
    print(f"[{incident}] Creating resources...")

    # 1️⃣ Create VPC
    vpc = ec2_resource.create_vpc(CidrBlock="10.0.0.0/16")
    vpc.create_tags(Tags=[{"Key": "Name", "Value": f"{incident}-vpc"}])
    vpc.wait_until_available()
    print(f"[{incident}] VPC created: {vpc.id}")

    # 2️⃣ Enable DNS hostnames
    vpc.modify_attribute(EnableDnsHostnames={"Value": True})

    # 3️⃣ Create subnet
    subnet = ec2_resource.create_subnet(
        CidrBlock="10.0.1.0/24",
        VpcId=vpc.id,
        AvailabilityZone=f"{REGION}a"
    )
    print(f"[{incident}] Subnet created: {subnet.id}")

    # 4️⃣ Internet Gateway + attach
    igw = ec2_resource.create_internet_gateway()
    vpc.attach_internet_gateway(InternetGatewayId=igw.id)
    print(f"[{incident}] Internet Gateway attached: {igw.id}")

    # 5️⃣ Route Table
    route_table = list(vpc.route_tables.all())[0]
    route_table.create_route(
        DestinationCidrBlock="0.0.0.0/0",
        GatewayId=igw.id
    )
    print(f"[{incident}] Route Table updated for IGW")

    # 6️⃣ Security Group
    sg = ec2_resource.create_security_group(
        GroupName=f"{incident}-sg",
        Description=f"Security group for {incident}",
        VpcId=vpc.id
    )
    sg.authorize_ingress(
        IpPermissions=[
            {
                "IpProtocol": "tcp",
                "FromPort": 22,
                "ToPort": 22,
                "IpRanges": [{"CidrIp": "0.0.0.0/0"}]
            }
        ]
    )
    print(f"[{incident}] Security Group created: {sg.id}")

    # 7️⃣ Launch EC2
    instance = ec2_resource.create_instances(
        ImageId=AMI_ID,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        MaxCount=1,
        MinCount=1,
        NetworkInterfaces=[{
            "SubnetId": subnet.id,
            "DeviceIndex": 0,
            "AssociatePublicIpAddress": True,
            "Groups": [sg.id]
        }],
        TagSpecifications=[{
            "ResourceType": "instance",
            "Tags": [{"Key": "Name", "Value": f"{incident}-ec2"}]
        }]
    )[0]

    print(f"[{incident}] EC2 instance launching: {instance.id}")
    instance.wait_until_running()
    instance.reload()
    print(f"[{incident}] EC2 instance running: {instance.public_ip_address}")

    # 8️⃣ Screenshot placeholder path
    screenshots_dir = os.path.join("AWS_Error_Driven_Troubleshooting_Lab", "incidents", incident, "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)
    print(f"[{incident}] Take screenshots and save in: {screenshots_dir}")

    print(f"[{incident}] Resources ready!\n")

print("All incidents spun up. Remember to take screenshots!")
