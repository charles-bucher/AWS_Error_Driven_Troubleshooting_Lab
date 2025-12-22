003-lambda-timeout

Description
This incident simulates a Lambda function that times out due to misconfigured function settings or code issues.

Objectives

Identify the root cause of the Lambda timeout.

Collect logs and metrics.

Remediate the Lambda function configuration or code.

Validate that the function executes successfully.

Included Scripts

Script	Purpose
break.py	Introduces timeout errors in the Lambda function.
collect_evidence.py	Collects CloudWatch logs and function metrics.
deploy.py	Deploys the Lambda function and triggers for testing.
remediate.py	Adjusts configuration/code to prevent timeout.
teardown.py	Cleans up Lambda and related resources.

Screenshots
Include CloudWatch logs, timeout errors, and remediation evidence.

Commit Info

Name	Last Commit Message	Last Commit Date
003-lambda-timeout	Clean repo: move scripts into incidents, add incident READMEs, remove…