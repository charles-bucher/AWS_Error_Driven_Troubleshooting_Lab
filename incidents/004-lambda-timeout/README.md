004-lambda-timeout

Description
This incident simulates another Lambda timeout scenario or similar runtime failure for advanced testing and automation.

Objectives

Identify root cause of runtime failure.

Collect logs, metrics, and evidence.

Remediate the function.

Validate correct execution.

Included Scripts

Script	Purpose
break.py	Triggers Lambda failure scenario.
collect_evidence.py	Gathers logs and execution metrics.
deploy.py	Deploys Lambda test environment.
remediate.py	Fixes Lambda runtime issues.
teardown.py	Cleans up all resources.

Screenshots
Include relevant screenshots of failures, logs, and remediation steps.

Commit Info

Name	Last Commit Message	Last Commit Date
004-lambda-timeout	Clean repo: move scripts into incidents, add incident READMEs, remove…	2 minutes ago

If you want, I can turn this into ready-to-drop READM