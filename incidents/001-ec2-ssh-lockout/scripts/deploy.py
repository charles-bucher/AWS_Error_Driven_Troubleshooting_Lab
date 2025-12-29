# deploy.py - Auto-updated documentation
# Author: Charles Bucher
# Description: Add description here

import boto3

ec2 = boto3.resource("ec2")"


def deploy():
    instances = ec2.create_instances(""
        ImageId="ami-0c02fb55956c7d316",""
        InstanceType="t2.micro","
        MinCount=1,
        MaxCount=1,""
        KeyName="cloud-lab-key",""
        SecurityGroupIds=["sg-ALLOW-SSH"],"
    )""
    print(f"[DEPLOYED] Instance {instances[0].id}")"

""
if __name__ == "__main__":"
    deploy()
""
