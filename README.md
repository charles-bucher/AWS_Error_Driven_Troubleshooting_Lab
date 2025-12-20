# AWS_Error_Driven_Troubleshooting_Lab

![GitHub last commit](https://img.shields.io/github/last-commit/Charles-Bucher/AWS_Error_Driven_Troubleshooting_Lab?style=flat-square)
![GitHub repo size](https://img.shields.io/github/repo-size/Charles-Bucher/AWS_Error_Driven_Troubleshooting_Lab?style=flat-square)
![GitHub language count](https://img.shields.io/github/languages/count/Charles-Bucher/AWS_Error_Driven_Troubleshooting_Lab?style=flat-square)
![GitHub top language](https://img.shields.io/github/languages/top/Charles-Bucher/AWS_Error_Driven_Troubleshooting_Lab?style=flat-square)

**Entry-Level Cloud Support Engineer Portfolio** | AWS Troubleshooting | Remote-Ready

Hands-on AWS incident labs simulating real support tickets. Each scenario follows production workflows: intake → diagnosis → resolution → documentation.

## 🎯 Core Support Skills

✅ AWS Service Troubleshooting (EC2, Lambda, S3, DynamoDB, IAM)  
✅ CloudWatch Log Analysis & Metric Correlation  
✅ Root Cause Analysis via AWS Console/CLI  
✅ Ticket Management & Technical Documentation  
✅ Python/PowerShell Automation Scripts  

## 🛠️ Tech Stack

**AWS:** EC2 · Lambda · S3 · DynamoDB · CloudWatch · IAM  
**Languages:** Python · PowerShell · Bash · Terraform (HCL)  
**Tools:** AWS CLI · AWS Console · Git

## 📁 Lab Structure

```
├── incidents/       # Customer ticket scenarios (broken infrastructure)
├── errors/docs/     # Troubleshooting runbooks and playbooks
├── evidence/        # CloudWatch logs, metrics, diagnostic outputs
├── scripts/         # Remediation scripts (Python/PowerShell)
├── terraform/       # Infrastructure as Code (lab setup)
└── lambdas/         # Serverless diagnostic utilities
```

## 💼 Support Workflow

Each lab mirrors real AWS support tickets:

**1. Intake** → Review error logs and customer environment  
**2. Diagnosis** → Analyze CloudWatch logs, trace root cause  
**3. Resolution** → Fix via console/CLI/script  
**4. Documentation** → Write playbook for team knowledge base

## 🔧 Sample Incidents

**Lab 001:** EC2 instance connectivity failure (security group misconfiguration)  
**Lab 002:** Lambda timeout errors (memory/execution limits)  
**Lab 003:** S3 access denied (IAM policy troubleshooting)  
**Lab 004:** DynamoDB throttling (capacity planning)

Each includes: customer scenario, error logs, troubleshooting steps, resolution, and prevention strategies.

<details>
<summary>📸 <b>Lab Screenshots</b> (Click to expand)</summary>

### Lab 001: EC2 SSH Lockout
![EC2 SSH Lockout](./incidents/001-ec2-ssh-lockout/screenshots/security-group-issue.png)
*Security group misconfiguration blocking SSH access*

### Lab 002: S3 Public Bucket Exposure
![S3 Bucket Policy](./incidents/002-s3-public-bucket/screenshots/bucket-policy-error.png)
*Troubleshooting public access block settings*

### Lab 003: Lambda Timeout
![Lambda Timeout](./incidents/003-lambda-timeout/screenshots/cloudwatch-timeout.png)
*CloudWatch logs showing function execution timeout*

### Lab 004: VPC DNS Failure
![VPC DNS](./incidents/004-vpc-dns-failure/screenshots/dns-resolution-error.png)
*VPC DNS resolution troubleshooting*

</details>

<details>
<summary>📊 <b>Architecture Diagrams</b> (Click to expand)</summary>

### Lab Infrastructure Overview
![Architecture](./diagrams/lab-architecture.png)
*Terraform-managed AWS environment for incident simulation*

### Troubleshooting Workflow
![Workflow](./diagrams/support-workflow.png)
*Visual representation of 4-step incident resolution process*

</details>

## 🚀 Quick Start

```bash
# Validate lab environment
python aws_lab_validator.py

# Generate incident scenarios
python spin_incidents.py

# Run repository audit
powershell -ExecutionPolicy Bypass -File audit_error_repo.ps1
```

## 📫 Contact

**Charles Bucher** | Entry-Level Cloud Support Engineer  
📍 Pinellas Park, FL | 🌐 Remote (US-based)  
💼 GitHub: [@Charles-Bucher](https://github.com/Charles-Bucher)

**Seeking:** AWS Cloud Support Engineer · Technical Support Associate · Cloud Operations

Self-taught through hands-on AWS troubleshooting. Available for immediate start.

---

**ATS Keywords:** AWS · Cloud Support Engineer · Technical Support · Troubleshooting · CloudWatch · EC2 · Lambda · S3 · DynamoDB · IAM · Python · PowerShell · AWS CLI · Log Analysis · Root Cause Analysis · Customer Service · Remote · Entry Level · Cloud Operations · Infrastructure · Ticketing · Documentation