provider "aws" {
  region = var.region
}

resource "aws_iam_role" "lambda_role" {
  name = "lambda-broken-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action = "sts:AssumeRole",
      Effect = "Allow",
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
  # Intentionally missing CloudWatch Logs permissions
}

resource "aws_lambda_function" "slow_fn" {
  function_name = "lab-lambda-timeout"
  role          = aws_iam_role.lambda_role.arn
  runtime       = "python3.11"
  handler       = "app.handler"
  timeout       = 1 # Intentionally too low
  filename      = "function.zip"
}

output "lambda_name" { value = aws_lambda_function.slow_fn.function_name }
output "lambda_role" { value = aws_iam_role.lambda_role.name }