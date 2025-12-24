# AWS Error-Driven Troubleshooting Lab

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![AWS](https://img.shields.io/badge/AWS-Free_Tier-FF9900?logo=amazon-aws&logoColor=white)](https://aws.amazon.com/free/)
[![Python 3.14+](https://img.shields.io/badge/python-3.14+-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Boto3](https://img.shields.io/badge/boto3-SDK-orange)](https://boto3.amazonaws.com/)
[![EC2](https://img.shields.io/badge/AWS-EC2-FF9900)](https://aws.amazon.com/ec2/)
[![S3](https://img.shields.io/badge/AWS-S3-569A31)](https://aws.amazon.com/s3/)
[![Lambda](https://img.shields.io/badge/AWS-Lambda-FF9900)](https://aws.amazon.com/lambda/)
[![CloudWatch](https://img.shields.io/badge/CloudWatch-Monitoring-FF4F8B)](https://aws.amazon.com/cloudwatch/)
[![VPC](https://img.shields.io/badge/AWS-VPC-FF9900)](https://aws.amazon.com/vpc/)
[![IAM](https://img.shields.io/badge/AWS-IAM-FF9900)](https://aws.amazon.com/iam/)
[![Incidents Complete](https://img.shields.io/badge/Incidents-3%2F5%20Complete-success)](https://github.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab)
[![Documentation](https://img.shields.io/badge/Docs-Comprehensive-blue)](https://github.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab/tree/main/docs)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)](https://github.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab)
[![Remote Friendly](https://img.shields.io/badge/Remote-Friendly-success)](https://github.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab)

---

## 🎯 TL;DR

**Real-world AWS troubleshooting portfolio** built by a self-taught developer targeting remote Cloud Support Engineer roles. This lab demonstrates hands-on skills by intentionally breaking AWS environments and then documenting the complete investigation, root cause analysis, and remediation process—just like you'd do on the job.

**What's Inside:**
- ✅ **3 Complete Incidents**: EC2 SSH lockouts, S3 security exposures, Lambda timeouts
- 📸 **Visual Documentation**: 15+ screenshots showing every troubleshooting step
- 📊 **KPI Tracking**: MTTD, MTTI, MTTR metrics for each incident
- 🐍 **Python Automation**: Boto3 scripts for deployment, breaking, evidence collection, and cleanup
- 📝 **Professional RCAs**: Industry-standard Root Cause Analysis documentation
- 💰 **Free Tier Friendly**: All labs run on AWS Free Tier (< $1/month)

**Key Skills Demonstrated:** EC2 • S3 • Lambda • VPC • CloudWatch • IAM • Python • Boto3 • Incident Response • Log Analysis • Security Troubleshooting

> **Perfect for:** Entry-level cloud support roles, remote positions, felon-friendly tech companies

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab.git
cd AWS_Error_Driven_Troubleshooting_Lab

# Install dependencies
pip install -r requirements.txt

# Configure AWS CLI (requires AWS account)
aws configure

# Run your first incident
cd incidents/001-ec2-ssh-lockout/scripts
python deploy.py
python break.py
python collect_evidence.py
python teardown.py
```

**Cost:** All labs are designed to run within AWS Free Tier limits (< $1/month typical usage)

---

## 📋 Incident Scenarios

| ID | Incident Name | AWS Services | Difficulty | Status | Avg Resolution Time |
|----|---------------|--------------|------------|--------|---------------------|
| 001 | EC2 SSH Lockout | EC2, VPC, Security Groups | 🟢 Entry | ✅ Complete | ~15 min |
| 002 | S3 Public Bucket Exposure | S3, IAM, CloudTrail | 🟢 Entry | ✅ Complete | ~20 min |
| 003 | Lambda Function Timeout | Lambda, VPC, CloudWatch | 🟡 Intermediate | ✅ Complete | ~30 min |
| 004 | Lambda Cold Start Issues | Lambda, API Gateway | 🟡 Intermediate | 🛠 Planned | TBD |
| 005 | VPC Network Connectivity | VPC, Route Tables, NACLs | 🟡 Intermediate | 🛠 Planned | TBD |

---

## 📸 Example: Incident 002 - S3 Public Bucket Exposure

### Step 1: S3 Bucket Deployment
![S3 Bucket Creation](incidents/002-s3-public-bucket/002_screenshots/002_01_deploy_s3_bucket.png)
*Deploying S3 bucket with intentional misconfiguration for security analysis*

### Step 2: Bucket Misconfiguration Analysis
![Bucket Misconfiguration](incidents/002-s3-public-bucket/002_screenshots/002_02_bucket_misconfig.png)
*Identifying public access settings and policy vulnerabilities - ROOT CAUSE*

### Step 3: Evidence Collection
![Evidence Collection](incidents/002-s3-public-bucket/002_screenshots/002_03_collect_evidence.png)
*Gathering CloudTrail logs, bucket policies, and access patterns*

### Step 4: Complete Workflow
![Full Workflow](incidents/002-s3-public-bucket/002_screenshots/002_04_full_workflow.png)
*End-to-end demonstration of detection, investigation, and remediation process*

### Step 5: Public Access Validation
![Public Access Validation](incidents/002-s3-public-bucket/002_screenshots/002_05_validate_public_access.png)
*Verifying bucket security settings and confirming remediation success*

---

## 📸 Example: Incident 003 - Lambda Function Timeout

### Step 1: Lambda Function Deployment
![Lambda Deploy](incidents/003-lambda-timeout/003_screenshots/003_01_lambda_deploy.png)
*Deploying Lambda function with VPC configuration and timeout settings*

### Step 2: Break Scenario
![Break Scenario](incidents/003-lambda-timeout/003_screenshots/003_break_mock.png)
*Introducing timeout condition through VPC network restrictions*

### Step 3: Log Collection & Analysis
![CloudWatch Logs](incidents/003-lambda-timeout/003_screenshots/003_03_collect_logs.png)
*Analyzing CloudWatch logs to identify timeout patterns and root cause*

### Step 4: Remediation Implementation
![Remediation](incidents/003-lambda-timeout/003_screenshots/003_remediate_mock.png)
*Applying fixes: VPC endpoint configuration, timeout adjustments, retry logic*

### Step 5: Teardown & Cleanup
![Teardown](incidents/003-lambda-timeout/003_screenshots/003_teardown.png)
*Proper resource cleanup to prevent cost leakage and maintain clean environment*

---

## 📸 Example: Incident 001 - EC2 SSH Lockout Resolution

### Step 1: VPC Infrastructure Setup
![VPC Creation](incidents/001-ec2-ssh-lockout/001_screenshots/001_01_vpc_creation.png)
*Creating isolated VPC environment for the troubleshooting scenario*

### Step 2: Subnet Configuration
![Subnet Configuration](incidents/001-ec2-ssh-lockout/001_screenshots/001_02_subnets.png)
*Configuring public and private subnets with proper CIDR blocks*

### Step 3: Route Table Analysis
![Route Tables](incidents/001-ec2-ssh-lockout/001_screenshots/001_03_route_tables.png)
*Investigating route table configurations and internet gateway associations*

### Step 4: Security Group Investigation
![Security Group Rules](incidents/001-ec2-ssh-lockout/001_screenshots/001_04_security_group.png)
*Identifying misconfigured inbound rules preventing SSH access - ROOT CAUSE*

### Step 5: EC2 Instance Details
![EC2 Instances](incidents/001-ec2-ssh-lockout/001_screenshots/001_05_ec2_instances.png)
*Verifying instance state, networking, and security group attachments*

### Step 6: Storage & System Configuration
![Storage Gateway](incidents/001-ec2-ssh-lockout/001_screenshots/001_06_storage_gateway.png)
*Confirming storage and system-level configurations during troubleshooting*

---

## 🔍 What's Included in Each Incident

```text
incidents/001-ec2-ssh-lockout/
├── README.md                    # Full incident documentation
├── scripts/
│   ├── deploy.py               # Creates the broken environment
│   ├── break.py                # Introduces the specific error
│   ├── collect_evidence.py     # Gathers logs, metrics, screenshots
│   ├── fix.py                  # Automated remediation
│   └── teardown.py             # Cleanup resources
├── 001_screenshots/
│   ├── 001_01_vpc_creation.png
│   ├── 001_02_subnets.png
│   ├── 001_03_route_tables.png
│   ├── 001_04_security_group.png
│   ├── 001_05_ec2_instances.png
│   └── 001_06_storage_gateway.png
├── logs/
│   ├── cloudwatch-logs.json
│   ├── system-logs.txt
│   └── error-traces.log
├── metrics/
│   ├── performance-data.json
│   └── resolution-timeline.csv
└── docs/
    ├── RCA-report.md           # Root Cause Analysis
    ├── remediation-steps.md
    └── prevention-plan.md
```

---

## 📊 Key Performance Indicators (KPIs)

Each incident tracks industry-standard metrics:

- **MTTD** (Mean Time To Detect): How quickly the issue was identified
- **MTTI** (Mean Time To Investigate): Time spent analyzing the root cause
- **MTTR** (Mean Time To Resolve): Total time from detection to resolution
- **Cost Impact**: AWS service costs incurred during the incident
- **Documentation Time**: Time invested in creating thorough documentation

### Example Metrics (Incident 001)

| Metric | Value |
|--------|-------|
| MTTD | 2 minutes |
| MTTI | 8 minutes |
| MTTR | 15 minutes |
| Cost | $0.12 |
| Documentation | 45 minutes |

---

## 🛠 Technical Skills Demonstrated

### AWS Services
- **EC2**: Instance management, security groups, key pairs, system logs
- **S3**: Bucket policies, encryption, access logging, versioning
- **Lambda**: Function configuration, VPC integration, timeout troubleshooting
- **VPC**: Network architecture, route tables, NACLs, security groups
- **CloudWatch**: Logs analysis, metrics monitoring, alarms, dashboards
- **IAM**: Policy troubleshooting, role permissions, access analysis

### Cloud Support Skills
- Incident response and triage
- Root cause analysis (RCA) documentation
- Log analysis and correlation
- Performance metrics interpretation
- Cost optimization awareness
- Customer-facing documentation

### Automation & Scripting
- **Python**: Boto3 SDK, error handling, automation scripts
- **Bash/PowerShell**: System administration, log parsing
- **Infrastructure as Code**: Terraform (planned)
- **CI/CD Concepts**: Automated testing and validation

---

## 🎓 Learning Methodology

This project follows an **error-driven learning** approach:

1. **Break It**: Intentionally misconfigure AWS resources
2. **Detect It**: Use monitoring tools to identify the issue
3. **Investigate It**: Gather evidence and analyze logs
4. **Fix It**: Implement the correct solution
5. **Document It**: Create comprehensive RCA reports
6. **Prevent It**: Design safeguards against recurrence

This mirrors real cloud support workflows where you must troubleshoot unfamiliar issues under time pressure.

---

## 📦 Installation & Requirements

### Prerequisites
- AWS Account (Free Tier eligible)
- Python 3.14 or higher
- AWS CLI configured with appropriate credentials
- Basic understanding of AWS services

### Setup
```bash
# Clone repository
git clone https://github.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab.git
cd AWS_Error_Driven_Troubleshooting_Lab

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Verify AWS CLI configuration
aws sts get-caller-identity
```

---

## 🔐 Security & Best Practices

- All scenarios use least-privilege IAM policies
- Sensitive data is never committed to the repository
- Automated teardown scripts prevent resource leakage
- Security group rules are scoped to necessary access only
- All credentials are managed through AWS CLI/SDK

---

## 📈 Roadmap

- [x] EC2 SSH connectivity troubleshooting (Incident 001)
- [x] S3 bucket security and access issues (Incident 002)
- [x] Lambda timeout and VPC integration (Incident 003)
- [ ] Lambda cold start optimization (Incident 004)
- [ ] VPC network connectivity problems (Incident 005)
- [ ] CloudWatch alarm configuration
- [ ] IAM permission troubleshooting
- [ ] Cost optimization scenarios
- [ ] Multi-region failover testing
- [ ] Add Terraform infrastructure definitions
- [ ] Create video walkthroughs

---

## 🤝 Contributing

While this is a personal portfolio project, I welcome feedback and suggestions:

1. Open an issue to discuss proposed changes
2. Fork the repository
3. Create a feature branch
4. Submit a pull request with clear documentation

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

**Charles Bucher**\
GitHub: [@charles-bucher](https://github.com/charles-bucher)\
Portfolio: [View Live Projects](https://github.com/charles-bucher)

*Self-taught developer focusing on cloud infrastructure and remote opportunities*

---

## 🔗 Resources & References

- [AWS Documentation](https://docs.aws.amazon.com/)
- [AWS Free Tier](https://aws.amazon.com/free/)
- [Python Boto3 SDK](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [AWS Cloud Support Knowledge Base](https://aws.amazon.com/premiumsupport/knowledge-center/)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)

---

## 📊 Project Statistics

![Repository Stats](https://github-readme-stats.vercel.app/api?username=charles-bucher&repo=AWS_Error_Driven_Troubleshooting_Lab&show_icons=true&theme=default)

---

**⭐ If you find this project helpful, please consider giving it a star!**