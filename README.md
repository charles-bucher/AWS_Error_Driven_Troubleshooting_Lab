# AWS Error-Driven Troubleshooting Lab

**Real-world AWS incident response and troubleshooting scenarios**

This repository demonstrates hands-on cloud support skills through intentionally broken AWS environments. Each scenario simulates actual production issues requiring log analysis, metrics interpretation, root cause identification, and remediation—mirroring the daily work of cloud support engineers and SREs.

## 🎯 Project Purpose

Unlike guided tutorials that walk you through perfect deployments, this lab focuses on **what happens when things break**. Every scenario is designed to develop real troubleshooting muscle memory:

- Reading CloudWatch logs to identify failures
- Analyzing IAM permission errors
- Debugging Lambda function issues
- Investigating S3 bucket policy problems
- Troubleshooting VPC networking and security groups
- Documenting incidents and writing runbooks

**For hiring managers:** This project showcases practical cloud support capabilities—problem diagnosis, systematic troubleshooting, documentation, and automation—skills needed on day one of any cloud operations role.

## 🛠️ Technical Skills Demonstrated

**AWS Services:**
- EC2 (instances, security groups, networking)
- Lambda (functions, triggers, permissions)
- S3 (buckets, policies, versioning)
- IAM (roles, policies, least privilege)
- VPC (subnets, route tables, NACLs)
- CloudWatch (logs, metrics, alarms)

**Tools & Languages:**
- Python (boto3, AWS automation)
- PowerShell (Windows-based AWS management)
- Bash scripting (Linux troubleshooting)
- AWS CLI (resource inspection and remediation)
- Git/GitHub (version control, CI/CD basics)

**Cloud Support Methodology:**
- Incident response workflows
- Root cause analysis (5 Whys, fishbone)
- Runbook documentation
- Post-incident reviews
- Preventive controls

## 📁 Repository Structure

```
AWS_Error_Driven_Troubleshooting_Lab/
├── incidents/           # Real-world incident scenarios with full context
├── errors/              # Error messages, logs, and diagnostic data
├── runbooks/            # Step-by-step troubleshooting procedures
├── scripts/             # Python automation and remediation scripts
├── scripts_ps/          # PowerShell scripts for Windows-based management
├── tests/               # Validation scripts to verify fixes
├── diagrams/            # Architecture diagrams and visual aids
├── docs/screenshots/    # Evidence of troubleshooting process
└── .github/workflows/   # CI/CD automation for testing scenarios
```

## 🚀 Quick Start

### Prerequisites

- AWS Account (Free Tier eligible)
- AWS CLI configured with credentials
- Python 3.8+ with boto3
- Basic familiarity with AWS console

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab.git
   cd AWS_Error_Driven_Troubleshooting_Lab
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure AWS credentials**
   ```bash
   aws configure
   # Enter your AWS Access Key ID, Secret Access Key, and preferred region
   ```

4. **Verify AWS access**
   ```bash
   aws sts get-caller-identity
   ```

### Running a Scenario

Each incident folder contains:
- `scenario.md` - The problem description and symptoms
- `deploy.py` or `deploy.sh` - Script to create the broken environment
- `expected_errors.txt` - What you should see when things fail
- `solution.md` - Root cause and remediation (check after troubleshooting!)

**Example workflow:**
```bash
# Deploy a broken scenario
cd incidents/01_lambda_s3_permission_denied
python deploy.py

# Investigate the issue using AWS CLI, console, and CloudWatch logs
# Document your findings

# Compare your solution with the provided runbook
cat ../../runbooks/01_lambda_s3_troubleshooting.md

# Clean up resources
python cleanup.py
```

## 📋 Available Scenarios

Each scenario is production-realistic and requires systematic troubleshooting:

| Scenario | AWS Services | Skills Practiced |
|----------|-------------|------------------|
| Lambda Permission Denied | Lambda, S3, IAM | IAM policy debugging, CloudWatch log analysis |
| EC2 Connection Timeout | EC2, VPC, Security Groups | Network troubleshooting, security group rules |
| S3 Access Denied | S3, IAM, Bucket Policies | S3 permissions, bucket policy debugging |
| Lambda Timeout | Lambda, VPC, CloudWatch | Performance troubleshooting, timeout investigation |
| *More scenarios in development* | | |

## 🔍 Learning Approach

This lab follows an **error-driven learning** model:

1. **Deploy** - Run a script to create a broken AWS environment
2. **Observe** - Encounter real error messages and failures
3. **Investigate** - Use AWS tools to gather diagnostic information
4. **Diagnose** - Apply root cause analysis techniques
5. **Remediate** - Fix the issue using AWS CLI or console
6. **Document** - Write up your findings and prevention steps
7. **Validate** - Run tests to confirm the fix works

This mirrors actual cloud support work where you receive a ticket, investigate logs, identify root cause, implement a fix, and document the incident.

## 📚 Runbook Examples

Each runbook follows a standard incident response format:

- **Incident Description** - What's broken and what symptoms appear
- **Initial Triage** - First checks to perform
- **Diagnostic Commands** - AWS CLI commands to gather data
- **Root Cause Analysis** - Step-by-step investigation
- **Remediation Steps** - How to fix the issue
- **Validation** - Confirming the fix works
- **Prevention** - How to avoid this in the future

These demonstrate the ability to create clear, actionable documentation—a critical skill for cloud support roles.

## 🎓 Why This Approach Works

Traditional labs show you how to build things correctly. This lab shows you how to **fix things when they break**—which is 80% of cloud operations work.

**Skills employers look for:**
- ✅ Troubleshooting mindset (don't panic, investigate systematically)
- ✅ Log analysis (CloudWatch, application logs, error messages)
- ✅ AWS service knowledge (not just how to deploy, but how to debug)
- ✅ Documentation skills (runbooks, incident reports)
- ✅ Automation (scripts to detect, diagnose, and remediate issues)

## 🏗️ Built With

- **Python 3.9** - Primary scripting language for AWS automation
- **boto3** - AWS SDK for Python
- **AWS CLI** - Command-line interface for AWS services
- **PowerShell 7** - Windows-based AWS management scripts
- **GitHub Actions** - CI/CD for automated testing

## 🤝 Contributing

This is a portfolio project demonstrating cloud support skills, but suggestions for additional scenarios are welcome! If you have ideas for realistic troubleshooting scenarios, feel free to open an issue.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

**Charles Bucher**
- GitHub: [@charles-bucher](https://github.com/charles-bucher)
- LinkedIn: [charles-bucher-cloud](https://linkedin.com/in/charles-bucher-cloud)

*This repository is part of my transition into cloud computing, demonstrating hands-on AWS troubleshooting capabilities for entry-level cloud support, cloud operations, or junior DevOps roles.*

---

**💡 For Hiring Managers:** This project demonstrates practical cloud troubleshooting skills beyond certifications. Each scenario requires the same systematic approach used in production support: investigating logs, analyzing errors, identifying root causes, implementing fixes, and documenting solutions. These are day-one skills for cloud support engineers, SREs, and DevOps roles.