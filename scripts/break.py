import boto3

REGION = "us-east-1"
KEY_NAME = "AEDT"
SECURITY_GROUP_NAME = "EC2-Incident-Test-SG"

ec2_client = boto3.client("ec2", region_name=REGION)

# Find the Security Group
response = ec2_client.describe_security_groups(
    GroupNames=[SECURITY_GROUP_NAME]
)
sg_id = response['SecurityGroups'][0]['GroupId']

# Remove SSH inbound rule to simulate outage
ec2_client.revoke_security_group_ingress(
    GroupId=sg_id,
    IpPermissions=[
        {
            'IpProtocol': 'tcp',
            'FromPort': 22,
            'ToPort': 22,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        }
    ]
)

print(f"[BREAK] SSH removed from {SECURITY_GROUP_NAME} ({sg_id})")
