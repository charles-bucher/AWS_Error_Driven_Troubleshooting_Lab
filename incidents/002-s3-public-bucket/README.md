002-s3-public-bucket

Description
This incident simulates a misconfigured S3 bucket that is publicly accessible, violating security best practices.

Objectives

Identify which bucket is misconfigured.

Collect evidence (bucket policies, ACLs, logs).

Remediate by restricting public access.

Validate that the bucket is secured.

Included Scripts

Script	Purpose
break.py	Opens the S3 bucket publicly for testing.
collect_evidence.py	Gathers bucket policies, ACLs, and access logs.
deploy.py	Deploys the S3 bucket scenario.
remediate.py	Fixes the bucket to enforce security best practices.
teardown.py	Deletes the test bucket.

Screenshots
Include screenshots of bucket policies, ACLs, and evidence of public access.

Commit Info

Name	Last Commit Message	Last Commit Date
002-s3-public-bucket	Clean repo: move scripts into incidents, add incident READMEs, remove…	2 minutes ago