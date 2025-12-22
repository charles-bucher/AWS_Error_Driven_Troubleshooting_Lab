001-ec2-ssh-lockout

Description
This incident simulates an EC2 SSH lockout scenario where users cannot access the server due to misconfigured security groups or key issues.

Objectives

Identify the root cause of the SSH lockout.

Collect necessary evidence (logs, instance configuration).

Remediate the issue by fixing security groups or keys.

Validate that SSH access is restored.

Included Scripts

Script	Purpose
break.py	Simulates the EC2 SSH lockout.
collect_evidence.py	Gathers logs, configs, or metrics for troubleshooting.
deploy.py	Deploys the EC2 instance and network setup for testing.
remediate.py	Fixes the misconfiguration to restore SSH access.
teardown.py	Cleans up EC2 and related resources.

Screenshots
Include screenshots of SSH errors, security group configs, and evidence collected.

Commit Info

Name	Last Commit Message	Last Commit Date
001-ec2-ssh-lockout	Clean repo: move scripts into incidents, add incident READMEs, remove…	2 minutes ago