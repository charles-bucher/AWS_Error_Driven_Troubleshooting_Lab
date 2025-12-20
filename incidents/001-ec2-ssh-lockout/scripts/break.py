import boto3, sys

ec2 = boto3.client("ec2")

INSTANCE_ID = sys.argv[1]

ec2.revoke_security_group_ingress(
    GroupId="sg-ALLOW-SSH",
    IpPermissions=[{
        "IpProtocol": "tcp",
        "FromPort": 22,
        "ToPort": 22,
        "IpRanges": [{"CidrIp": "0.0.0.0/0"}]
    }]
)

print("[INCIDENT] SSH access removed")
