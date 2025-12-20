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

### CloudWatch Log Analysis
![CloudWatch Logs](./evidence/cloudwatch-logs-sample.png)
*Example: Parsing Lambda error logs to identify timeout root cause*

### AWS Console Troubleshooting
![AWS Console](./evidence/ec2-troubleshooting-sample.png)
*Example: Debugging EC2 instance connectivity via security group rules*

### Incident Documentation
![Documentation](./evidence/playbook-sample.png)
*Example: Structured runbook for S3 access denied errors*

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