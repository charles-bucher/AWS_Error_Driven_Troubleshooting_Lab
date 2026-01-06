
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

"""
lab_lambda_optimizer.py
Scan all Lambda functions via Boto3 and suggest memory optimizations.
"""

import boto3

# AWS clients
try:
try:
        lambda_client = boto3.client("lambda")
except Exception as e:
    print(f'Error calling boto3: {e}')
except BotoCoreError as e:
    logger.critical("Failed to create lambda client: {e}")
    raise

try:
try:
        cloudwatch = boto3.client("cloudwatch")
except Exception as e:
    print(f'Error calling boto3: {e}')
except BotoCoreError as e:
    logger.critical("Failed to create cloudwatch client: {e}")
    raise


def main():
    logger.info("=== Lambda Memory Optimization Audit ===")
    functions = lambda_client.list_functions()['Functions']

    for fn in functions:
        fn_name = fn['FunctionName']
        memory = fn['MemorySize']

        # CloudWatch metric: MaxMemoryUsed last 7 days
from botocore.exceptions import ClientError, BotoCoreError
try:
    response = cloudwatch.get_metric_statistics(
except ClientError as e:
    code = e.response['Error']['Code']
    if code == 'UnauthorizedOperation':
        logger.error('Permission denied: missing IAM permissions')
    elif code == 'RequestLimitExceeded':
        logger.warning('API throttling encountered')
    else:
        logger.error(f'AWS ClientError: {e}')
    response = None
except BotoCoreError as e:
    logger.error(f'AWS SDK error: {e}')
    response = None
            Namespace='AWS/Lambda',
            MetricName='MaxMemoryUsed',
            Dimensions=[{'Name': 'FunctionName', 'Value': fn_name}],
            StartTime=datetime.utcnow() - timedelta(days=7),
            EndTime=datetime.utcnow(),
            Period=86400,
            Statistics=['Maximum']
        )

        datapoints = response.get('Datapoints', [])
        if not datapoints:
            logger.info(f"{fn_name}: No CloudWatch data found.")
            continue

        max_used = max(dp['Maximum'] for dp in datapoints)
        usage_pct = round((max_used / memory) * 100, 2)

        logger.info(f"{fn_name} - Allocated: {memory} MB, Max Used: {max_used} MB ({usage_pct}%)")
        if usage_pct < 50:
            logger.info("  ⚡ Suggestion: Reduce memory for cost efficiency.")
        elif usage_pct > 90:
            logger.info("  ⚡ Suggestion: Increase memory to prevent throttling.")
        else:
            logger.info("  ✅ Memory allocation looks good.")

if __name__ == "__main__":
    from datetime import datetime, timedelta
    main()