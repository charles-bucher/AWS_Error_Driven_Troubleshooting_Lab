AWS Error-Driven Troubleshooting Lab










TL;DR

This repo demonstrates real-world AWS troubleshooting:

4+ scenarios, 15+ automation scripts, 10+ production-style runbooks

AWS skills: EC2, Lambda, S3, IAM, VPC, CloudWatch

Focused on entry-level Cloud Support readiness

Beginner scenarios highlight skills an entry-level cloud support engineer should have on day one.

🎯 Project Purpose

Instead of perfect tutorials, this lab breaks AWS services intentionally to teach real troubleshooting:

Read CloudWatch logs to identify failures

Debug IAM and S3 permission errors

Investigate Lambda function issues

Troubleshoot VPC networking and security groups

Document incidents and create production-style runbooks

This mirrors daily work of cloud support engineers and SREs.

🛠️ Skills Demonstrated
AWS Services

EC2 (instances, networking, security groups)

Lambda (functions, triggers, permissions)

S3 (buckets, policies, versioning)

IAM (roles, policies, least privilege)

VPC (subnets, route tables, NACLs)

CloudWatch (logs, metrics, alarms)

Tools & Languages

Python 3.9 + boto3 (automation, remediation scripts)

PowerShell 7 (Windows-based AWS management)

Bash (Linux troubleshooting)

AWS CLI (resource inspection and remediation)

Git/GitHub (version control, CI/CD basics)

Cloud Support Workflow

Incident response & triage

Root cause analysis (5 Whys, fishbone)

Runbook documentation

Post-incident reviews & preventive controls

📁 Repository Structure
AWS_Error_Driven_Troubleshooting_Lab/
├── incidents/           # Real-world incident scenarios
├── errors/              # Logs and diagnostic data
├── runbooks/            # Step-by-step troubleshooting procedures
├── scripts/             # Python automation & remediation
├── scripts_ps/          # PowerShell scripts
├── tests/               # Verification scripts
├── diagrams/            # Architecture diagrams & visual aids
├── docs/screenshots/    # Evidence of troubleshooting
└── .github/workflows/   # CI/CD automation

🚀 Quick Start

Prerequisites

AWS Account (Free Tier eligible)

AWS CLI configured with credentials

Python 3.8+ with boto3

Basic familiarity with AWS console

Setup

git clone https://github.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab.git
cd AWS_Error_Driven_Troubleshooting_Lab
pip install -r requirements.txt
aws configure   # Enter Access Key, Secret, Region
aws sts get-caller-identity  # Verify AWS access


Run a Scenario

cd incidents/01_lambda_s3_permission_denied
python deploy.py       # Deploy broken environment
# Investigate using AWS CLI, CloudWatch, console
cat ../../runbooks/01_lambda_s3_troubleshooting.md  # Compare with solution
python cleanup.py      # Clean up resources

📋 Available Scenarios
Scenario	AWS Services	Skills Practiced	Difficulty
Lambda Permission Denied	Lambda, S3, IAM	IAM policy debugging, CloudWatch logs	⭐⭐ Beginner
EC2 Connection Timeout	EC2, VPC, Security Groups	Network troubleshooting	⭐⭐ Beginner
S3 Access Denied	S3, IAM, Bucket Policies	Permissions, bucket policy debugging	⭐⭐⭐ Intermediate
Lambda Timeout	Lambda, VPC, CloudWatch	Performance troubleshooting, timeout investigation	⭐⭐⭐ Intermediate

Coming Soon: EC2 Instance Store Data Loss, RDS Connection Pool Exhaustion, API Gateway 502, CloudFront Cache Issues

🔍 Learning Approach

Error-driven model: Deploy → Observe → Investigate → Diagnose → Remediate → Document → Validate

Average troubleshooting time per scenario: 15–30 minutes

Remediation success rate: 100% (verified with test scripts)

AWS cost per scenario: ~$0.20–0.50, monthly ~$10–15

📚 Sample Runbooks

RB-001: Lambda S3 Permission Troubleshooting

RB-002: EC2 Connection Timeout Debugging

RB-003: S3 Access Denied Investigation

All runbooks are production-style, demonstrating documentation and systematic troubleshooting.

🎓 Why This Lab Works

Focuses on fixing broken systems, not just deployment

Mirrors real cloud support workflows

Shows hands-on skills over certifications

Demonstrates independence, documentation, and automation

💼 For Hiring Managers

Instead of claiming skills:

Skill	Evidence in This Repo
Read AWS logs	All scenarios use CloudWatch logs
Debug IAM permissions	Multiple IAM-related incidents
Troubleshoot systematically	Runbooks show step-by-step investigation
Use AWS CLI	All remediation uses CLI commands
Automate with Python	15+ boto3 scripts
Document work	10+ runbooks
🏗️ Built With

Python 3.9 & boto3

AWS CLI & PowerShell 7

GitHub Actions (CI/CD)

VS Code

📄 License

This project is licensed under the MIT License – see LICENSE
 for details.

🙋‍♂️ About Me

Charles Bucher | Self-Taught Cloud Engineer | Largo, Florida

Entry-level cloud support, career transition

Building proof of skills, not just collecting certs

Open to remote/full-time or contract W2 roles