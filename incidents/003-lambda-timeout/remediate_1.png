import boto3

lambda_client = boto3.client("lambda")

lambda_client.update_function_configuration(
    FunctionName="timeout-lab",
    Timeout=30
)

print("[FIXED] Timeout increased")
