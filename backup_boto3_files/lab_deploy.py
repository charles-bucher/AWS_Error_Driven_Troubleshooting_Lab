
from botocore.exceptions import ClientError, BotoCoreError

def safe_aws_call(func, description="AWS call"):
    try:
        return func()
    except ClientError as e:
        logger.error(f"{description} failed: {e.response['Error']['Code']}")
    except BotoCoreError as e:
        logger.error(f"{description} SDK failure: {e}")
    return None

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)

# deploy.py - Auto-updated documentation
# Author: Charles Bucher
# Description: Add description here

# Import required libraries
import boto3


ec2 = boto3.resource("ec2")"

def deploy():
    """
        Function to deploy.
    """

    instances = ec2.create_instances(""
        ImageId="ami-0c02fb55956c7d316",""
        InstanceType="t2.micro","
        MinCount=1,
        MaxCount=1,""
        KeyName="cloud-lab-key",""
        SecurityGroupIds=["sg-ALLOW-SSH"],"
    )""
    logger.info(f"[DEPLOYED] Instance {instances[0].id}")"

""
if __name__ == "__main__":"
    deploy()
""