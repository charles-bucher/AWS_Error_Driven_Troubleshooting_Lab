"""
lab_lambda_optimizer.py
Scan all Lambda functions via Boto3 and suggest memory optimizations.
"""

import boto3

# AWS clients
lambda_client = boto3.client('lambda')
cloudwatch = boto3.client('cloudwatch')

def main():
    print("=== Lambda Memory Optimization Audit ===")
    functions = lambda_client.list_functions()['Functions']

    for fn in functions:
        fn_name = fn['FunctionName']
        memory = fn['MemorySize']

        # CloudWatch metric: MaxMemoryUsed last 7 days
        response = cloudwatch.get_metric_statistics(
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
            print(f"{fn_name}: No CloudWatch data found.")
            continue

        max_used = max(dp['Maximum'] for dp in datapoints)
        usage_pct = round((max_used / memory) * 100, 2)

        print(f"{fn_name} - Allocated: {memory} MB, Max Used: {max_used} MB ({usage_pct}%)")
        if usage_pct < 50:
            print("  ⚡ Suggestion: Reduce memory for cost efficiency.")
        elif usage_pct > 90:
            print("  ⚡ Suggestion: Increase memory to prevent throttling.")
        else:
            print("  ✅ Memory allocation looks good.")

if __name__ == "__main__":
    from datetime import datetime, timedelta
    main()
