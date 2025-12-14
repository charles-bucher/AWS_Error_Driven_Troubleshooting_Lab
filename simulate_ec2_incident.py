import boto3
import os
from datetime import datetime

# ---------------- CONFIG ----------------
REGION = 'us-east-1'
AMI_ID = 'ami-0c02fb55956c7d316'  # Example Amazon Linux 2 AMI
INSTANCE_TYPE = 't2.micro'
KEY_NAME = 'AEDT'  # Use your key pair
SECURITY_GROUP_NAME = 'EC2-Incident-Test-SG'
INCIDENT_DIR = r"C:\Users\buche\docs\Desktop\REPOS\AWS_Error_Driven_Troubleshooting_Lab\incidents\001-ec2-unreachable-security-group"
EVIDENCE_DIR = os.path.join(INCIDENT_DIR, "evidence")

# ---------------- SETUP ----------------
os.makedirs(EVIDENCE_DIR + r"\screenshots", exist_ok=True)
os.makedirs(EVIDENCE_DIR + r"\logs", exist_ok=True)
os.makedirs(os.path.join(INCIDENT_DIR, "remediation"), exist_ok=True)
os.makedirs(os.path.join(INCIDENT_DIR, "prevention"), exist_ok=True)

ec2 = boto3.resource('ec2', region_name=REGION)
ec2_client = boto3.client('ec2', region_name=REGION)

# ---------------- SECURITY GROUP ----------------
response = ec2_client.describe_security_groups(
    GroupNames=[SECURITY_GROUP_NAME]
)
if response['SecurityGroups']:
    sg_id = response['SecurityGroups'][0]['GroupId']
    print(f"Using existing Security Group {SECURITY_GROUP_NAME} with ID {sg_id}")
else:
    sg = ec2_client.create_security_group(
        GroupName=SECURITY_GROUP_NAME,
        Description="Temporary SG for EC2 incident lab",
        VpcId=None  # default VPC
    )
    sg_id = sg['GroupId']
    print(f"Created Security Group {SECURITY_GROUP_NAME} with ID {sg_id}")

# Allow SSH temporarily
ec2_client.authorize_security_group_ingress(
    GroupId=sg_id,
    IpPermissions=[{'IpProtocol':'tcp','FromPort':22,'ToPort':22,'IpRanges':[{'CidrIp':'0.0.0.0/0'}]}]
)

# ---------------- LAUNCH EC2 ----------------
print("Launching EC2 instance...")
instance = ec2.create_instances(
    ImageId=AMI_ID,
    InstanceType=INSTANCE_TYPE,
    KeyName=KEY_NAME,
    MinCount=1,
    MaxCount=1,
    SecurityGroupIds=[sg_id]
)[0]

instance.wait_until_running()
instance.reload()
print(f"EC2 Instance launched: {instance.id}, Public IP: {instance.public_ip_address}")

# ---------------- COLLECT INITIAL EVIDENCE ----------------
with open(os.path.join(EVIDENCE_DIR, "instance_info.txt"), "w") as f:
    f.write(f"Instance ID: {instance.id}\n")
    f.write(f"Public IP: {instance.public_ip_address}\n")
    f.write(f"Security Group ID: {sg_id}\n")
    f.write(f"Region: {REGION}\n")

# ---------------- BREAK SSH ACCESS ----------------
print("Simulating SSH outage by removing inbound SSH rule...")
ec2_client.revoke_security_group_ingress(
    GroupId=sg_id,
    IpPermissions=[{'IpProtocol':'tcp','FromPort':22,'ToPort':22,'IpRanges':[{'CidrIp':'0.0.0.0/0'}]}]
)

# Save post-break evidence
with open(os.path.join(EVIDENCE_DIR, "ssh_revoked.txt"), "w") as f:
    f.write(f"SSH access removed to simulate incident.\n")
    f.write(f"Check instance {instance.id} at IP {instance.public_ip_address} for SSH timeout.\n")

# ---------------- POPULATE INCIDENT MD ----------------
incident_md = os.path.join(INCIDENT_DIR, "incident.md")
with open(incident_md, "w") as f:
    f.write(f"# Incident 001 – EC2 Unreachable After Security Group Change\n\n")
    f.write("## Incident Summary\n")
    f.write("An EC2 instance became unreachable via SSH following a security group modification.\n\n")
    f.write("- **Service Impacted:** EC2\n")
    f.write("- **Severity:** Medium\n")
    f.write(f"- **Region:** {REGION}\n\n")
    f.write("## Symptoms\n")
    f.write("- SSH connection timeout\n")
    f.write("- Instance state: running\n")
    f.write("- No CPU or memory anomalies\n\n")
    f.write("## Initial Triage\n")
    f.write("1. Verified EC2 instance status checks\n")
    f.write("2. Reviewed recent configuration changes\n")
    f.write("3. Checked Security Group inbound rules\n")
    f.write("4. Evaluated NACL and route table configuration\n\n")
    f.write("## Evidence Collected\n")
    f.write("- Security Group inbound rules screenshot\n")
    f.write("- CloudWatch metrics (CPU, NetworkIn/Out)\n")
    f.write("- VPC Flow Logs (if enabled)\n\n")
    f.write("## Root Cause\n")
    f.write("Inbound SSH (port 22) access was removed from the attached Security Group during a configuration change.\n\n")
    f.write("## Resolution\n")
    f.write("Inbound SSH rule was restored, and access was confirmed from a trusted IP.\n\n")
    f.write("## Validation\n")
    f.write("- Successful SSH connection established\n")
    f.write("- No further connectivity issues observed\n\n")
    f.write("## Lessons Learned\n")
    f.write("Security Group changes require validation checks to prevent accidental service disruption.\n")

print("✅ EC2 incident simulated. Evidence collected in 'evidence' folder and incident.md updated.")
