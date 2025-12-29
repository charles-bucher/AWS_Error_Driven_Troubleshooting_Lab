# AWS Error-Driven Troubleshooting Lab

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![AWS](https://img.shields.io/badge/AWS-Cloud-orange.svg)](https://aws.amazon.com/)
[![Terraform](https://img.shields.io/badge/Terraform-IaC-purple.svg)](https://www.terraform.io/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Learning](https://img.shields.io/badge/Type-Hands--on%20Labs-brightgreen.svg)]()
[![CloudWatch](https://img.shields.io/badge/AWS-CloudWatch-FF9900.svg)]()
[![Lambda](https://img.shields.io/badge/AWS-Lambda-FF9900.svg)]()
[![VPC](https://img.shields.io/badge/AWS-VPC-FF9900.svg)]()

> **Break things. Fix them. Learn AWS troubleshooting the way real cloud engineers do.**

---

## 🎯 TL;DR

**What:** 4 hands-on AWS labs where you intentionally break cloud infrastructure, then investigate and fix real errors using CloudWatch, CloudTrail, and AWS best practices.

**Why:** Most tutorials show perfect deployments. This teaches **troubleshooting skills** employers actually need—reading logs, diagnosing errors, and fixing production issues.

**Skills:** EC2 networking • Lambda performance tuning • S3 security • IAM debugging • CloudWatch Logs • Infrastructure as Code • Root cause analysis

**Time Investment:** 2-4 hours per lab • Complete all 4 labs in a weekend

**Cost:** AWS Free Tier (under $5 total if you clean up resources)

**Best For:** Entry-level cloud engineers, AWS certification prep, portfolio projects, interview prep

---

## 📊 Project Overview

```
┌─────────────────────────────────────────────────────────────┐
│                   Error-Driven Learning                     │
│                                                             │
│  Deploy → Break → Investigate → Fix → Validate → Document  │
│                                                             │
│    4 Labs × 20+ Real Errors = Production-Ready Skills      │
└─────────────────────────────────────────────────────────────┘
```

| Metric | Value |
|--------|-------|
| **Labs** | 4 Production-Grade Scenarios |
| **AWS Services** | 12+ Hands-on |
| **Error Scenarios** | 20+ Real-World |
| **Infrastructure** | 100% Terraform |
| **Tests** | Automated Validation |

---

## 🔍 Why Error-Driven Learning?

### Traditional AWS Tutorials
```
1. Read documentation
2. Deploy perfect infrastructure
3. Everything works
4. Never see real errors ❌
```

### This Lab Approach
```
1. Deploy infrastructure
2. Intentionally break something
3. See real error messages
4. Investigate using CloudWatch/CloudTrail
5. Form hypotheses
6. Fix the issue
7. Validate solution ✅
```

**Result:** You gain troubleshooting confidence and practical debugging experience that translates directly to cloud support and DevOps roles.

---

## 🚨 The 4 Labs

### 🔴 Lab 001: EC2 SSH Connection Timeout

**Error Message:**
```bash
ssh: connect to host X.X.X.X port 22: Operation timed out
```

**What You'll Debug:**
- ✅ VPC networking fundamentals
- ✅ Security group configuration
- ✅ Route table troubleshooting
- ✅ VPC Flow Logs analysis
- ✅ Network ACLs vs Security Groups

**AWS Services:** EC2, VPC, Security Groups, NACLs, CloudWatch

**The Scenario:** EC2 instance deployed successfully but SSH connections time out. You'll investigate security groups, route tables, and VPC Flow Logs to identify the network misconfiguration blocking access.

[📖 **Full Lab Guide →**](incidents/001-ec2-ssh-lockout/README.md)

---

### 🟠 Lab 002: S3 Bucket Accidentally Public

**Error Message:**
```
S3 bucket exposed to internet - potential security breach detected
```

**What You'll Debug:**
- ✅ S3 bucket policy analysis
- ✅ IAM permissions debugging
- ✅ CloudTrail forensics
- ✅ Security incident response
- ✅ Block Public Access settings

**AWS Services:** S3, IAM, CloudTrail, GuardDuty, AWS Config

**The Scenario:** A misconfigured S3 bucket policy has exposed sensitive data to the public internet. You'll use CloudTrail to investigate who made the change, understand bucket policies vs IAM permissions, and properly secure the bucket.

[📖 **Full Lab Guide →**](incidents/002-s3-public-bucket/README.md)

---

### 🟡 Lab 003: Lambda Function Timeout

**Error Message:**
```
Task timed out after 3.00 seconds
```

**What You'll Debug:**
- ✅ Lambda performance tuning
- ✅ CloudWatch Logs investigation
- ✅ Memory vs timeout configuration
- ✅ Error handling best practices
- ✅ Cold start optimization

**AWS Services:** Lambda, CloudWatch Logs, CloudWatch Metrics, X-Ray

**The Scenario:** Lambda function works fine in testing but fails with timeout errors under load. You'll analyze CloudWatch Logs, optimize memory allocation, and understand the relationship between memory and CPU in Lambda.

[📖 **Full Lab Guide →**](incidents/003-lambda-timeout/README.md)

---

### 🔵 Lab 004: Lambda Timeout (Advanced Multi-Factor)

**Error Message:**
```
Multiple cascading timeout and throttling errors
```

**What You'll Debug:**
- ✅ Multi-factor troubleshooting
- ✅ Dependency conflicts
- ✅ Concurrent execution issues
- ✅ Complex error diagnosis
- ✅ Production debugging techniques

**AWS Services:** Lambda, CloudWatch, X-Ray, VPC, IAM

**The Scenario:** Complex Lambda timeout with multiple simultaneous root causes: memory limits, dependency conflicts, and concurrent execution throttling. You'll use systematic hypothesis testing to isolate and fix each issue.

[📖 **Full Lab Guide →**](incidents/004-lambda-timeout/README.md)

---

## 🚀 Quick Start

### Prerequisites
```bash
✓ AWS Account (Free Tier sufficient)
✓ AWS CLI configured
✓ Terraform 1.0+
✓ Python 3.9+
✓ 30 minutes per lab
```

### Installation & First Lab
```bash
# Clone repository
git clone https://github.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab.git
cd AWS_Error_Driven_Troubleshooting_Lab

# Install Python dependencies
pip install -r requirements.txt

# Start with Lab 001
cd incidents/001-ec2-ssh-lockout

# Read the lab guide
cat README.md

# Deploy infrastructure
cd terraform
terraform init
terraform apply -auto-approve

# Follow the lab steps to break, investigate, and fix
# Then clean up
terraform destroy -auto-approve
```

---

## 💼 Skills Demonstrated

### ☁️ Cloud Engineering
| Skill | Details |
|-------|---------|
| **AWS Services** | EC2, Lambda, S3, VPC, IAM, CloudWatch, CloudTrail |
| **Troubleshooting** | Root cause analysis, log investigation, systematic debugging |
| **Infrastructure** | Terraform, Infrastructure as Code, automated testing |
| **Security** | IAM policies, security groups, incident response |
| **Monitoring** | CloudWatch Logs, Metrics, CloudTrail forensics |

### 🛠️ Technical Competencies
- ✅ VPC networking and security groups
- ✅ Serverless architecture debugging
- ✅ IAM policy analysis
- ✅ Performance optimization
- ✅ Bash and Python scripting
- ✅ CI/CD concepts

### 💡 Professional Skills
- ✅ Systematic problem-solving
- ✅ Documentation and communication
- ✅ Hypothesis-driven debugging
- ✅ Solution validation and testing

---

## 📂 Repository Structure

```
AWS_Error_Driven_Troubleshooting_Lab/
├── incidents/                     # The 4 error labs
│   ├── 001-ec2-ssh-lockout/      # Lab 1: VPC networking
│   │   ├── terraform/            # Infrastructure code
│   │   ├── scripts/              # Automation scripts
│   │   ├── 001_screenshots/      # Lab documentation
│   │   └── README.md             # Step-by-step guide
│   ├── 002-s3-public-bucket/     # Lab 2: S3 security
│   │   ├── terraform/
│   │   ├── scripts/
│   │   ├── 002_screenshots/
│   │   └── README.md
│   ├── 003-lambda-timeout/       # Lab 3: Lambda performance
│   │   ├── terraform/
│   │   ├── scripts/
│   │   ├── 003_screenshots/
│   │   └── README.md
│   └── 004-lambda-timeout/       # Lab 4: Advanced debugging
│       ├── terraform/
│       ├── scripts/
│       └── README.md
├── lambdas/                      # Lambda function code
├── tests/                        # Automated validation
├── diagrams/                     # Architecture diagrams
├── docs/                         # Additional documentation
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

---

## 🎓 Learning Path

### 🟢 Beginner Track (Start here if new to AWS)

**Lab 001: EC2 SSH Lockout** (2-3 hours)
- Learn VPC networking fundamentals
- Understand security groups
- Practice basic troubleshooting

**Lab 002: S3 Public Bucket** (2-3 hours)
- Master S3 security concepts
- Learn IAM policies
- Practice CloudTrail forensics

### 🟡 Intermediate Track (Comfortable with AWS basics)

**Lab 003: Lambda Timeout** (3-4 hours)
- Dive into serverless troubleshooting
- Master CloudWatch Logs
- Learn performance optimization

### 🔴 Advanced Track (Preparing for cloud engineering roles)

**Lab 004: Complex Lambda Issues** (4-5 hours)
- Handle production-grade scenarios
- Practice multi-hypothesis debugging
- Master systematic troubleshooting

**Total Time:** 10-15 hours to complete all labs with documentation

---

## 🎯 Use Cases

### 📋 For Job Seekers
```
✓ Portfolio Project      → Demonstrate hands-on AWS troubleshooting
✓ Interview Prep        → Reference specific errors you've debugged
✓ Resume Skills         → List concrete AWS services and tools
✓ GitHub Activity       → Show active learning and growth
✓ Technical Stories     → Have real scenarios to discuss
```

### 📜 For Certification Study
```
✓ AWS Solutions Architect Associate  → VPC, EC2, S3, Lambda scenarios
✓ AWS SysOps Administrator          → CloudWatch, troubleshooting, ops
✓ AWS DevOps Engineer               → IaC, CI/CD, automation
```

### 🚀 For Career Changers
```
✓ Practical Experience  → Build troubleshooting skills without a job
✓ Confidence Building   → Work through errors in safe environment
✓ Communication         → Practice explaining debugging process
✓ Portfolio Building    → Create tangible proof of capabilities
```

---

## 🛠️ Technologies Used

| Category | Technologies |
|----------|-------------|
| **Cloud Platform** | AWS (EC2, Lambda, S3, VPC, IAM, CloudWatch, CloudTrail) |
| **Infrastructure** | Terraform, Infrastructure as Code |
| **Monitoring** | CloudWatch Logs, CloudWatch Metrics, X-Ray |
| **Languages** | Python 3.9+, Bash, HCL (Terraform) |
| **Security** | IAM, Security Groups, S3 Bucket Policies, GuardDuty |
| **Testing** | pytest, boto3, automated validation |
| **Version Control** | Git, GitHub, CI/CD workflows |

---

## 📈 What Makes This Different

| Traditional Labs | This Project |
|-----------------|--------------|
| ❌ Perfect deployments | ✅ Intentionally break things |
| ❌ Skip error messages | ✅ Experience real AWS errors |
| ❌ No investigation phase | ✅ Practice log analysis |
| ❌ No troubleshooting | ✅ Build systematic debugging |
| ❌ Theory-focused | ✅ Hands-on practical experience |
| ❌ Always works | ✅ Learn from failures |

---

## ✅ Lab Methodology

Every lab follows this proven 7-step process:

```
1. DEPLOY      → Set up infrastructure with Terraform
                 ↓
2. BREAK       → Introduce realistic misconfiguration
                 ↓
3. OBSERVE     → See the actual error message
                 ↓
4. INVESTIGATE → Use CloudWatch, CloudTrail, AWS Console
                 ↓
5. REMEDIATE   → Fix following AWS best practices
                 ↓
6. VALIDATE    → Confirm resolution with tests
                 ↓
7. DOCUMENT    → Record learnings in lab notes
```

This mirrors real cloud engineering workflows used in production support roles.

---

## 💡 Key Learnings

After completing these labs, you'll be able to:

**Troubleshooting Skills:**
- ✅ Navigate CloudWatch Logs efficiently to find error root causes
- ✅ Interpret common AWS error messages (timeouts, permission denied, connection refused)
- ✅ Use CloudTrail to investigate security incidents
- ✅ Form and test hypotheses systematically

**Technical Knowledge:**
- ✅ Debug VPC networking issues (security groups, NACLs, route tables)
- ✅ Optimize Lambda function performance (memory, timeout, cold starts)
- ✅ Secure S3 buckets properly (bucket policies, IAM, Block Public Access)
- ✅ Write Infrastructure as Code with Terraform

**Professional Skills:**
- ✅ Document troubleshooting processes clearly
- ✅ Communicate technical issues effectively
- ✅ Think critically about cloud architecture
- ✅ Follow AWS Well-Architected Framework principles

---

## 🔒 Cost & Security

### AWS Costs
**Total Cost:** < $5 if you:
- ✅ Use AWS Free Tier eligible services
- ✅ Run labs in us-east-1 region
- ✅ Destroy resources immediately after completing each lab
- ✅ Set up billing alerts before starting

### Security Best Practices
⚠️ **IMPORTANT:** These labs intentionally create misconfigurations for learning.

**ALWAYS:**
- Use a dedicated learning AWS account (not production)
- Run `terraform destroy` after completing each lab
- Never commit AWS credentials to Git
- Set up billing alerts ($5, $10, $20 thresholds)
- Review resources in AWS Console before and after labs

**NEVER:**
- Run these labs in production environments
- Leave resources running overnight
- Share AWS credentials in code
- Skip the cleanup steps

---

## 📞 Connect

**Charles Bucher** | Cloud Engineer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/charles-bucher-cloud)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)](https://github.com/charles-bucher)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-FF6B6B?style=for-the-badge)](https://charles-bucher.github.io)

---

## 🌟 Related Projects

Explore more hands-on AWS learning projects:

- **[AWS Cloud Support Simulator](https://github.com/charles-bucher)** - 7 production incident scenarios
- **[AWS CloudOps Suite](https://github.com/charles-bucher)** - Cloud operations automation toolkit

---

## 🤝 Contributing

Contributions welcome! Ways to help:

| Type | How to Help |
|------|-------------|
| 🐛 **Bugs** | Report issues with labs or infrastructure |
| 💡 **Ideas** | Suggest new error scenarios or labs |
| 📝 **Docs** | Improve documentation and guides |
| ✨ **Features** | Add troubleshooting techniques |
| 🧪 **Tests** | Contribute test cases and validation |

**To contribute:**
1. Fork this repository
2. Create a feature branch (`git checkout -b feature/new-lab`)
3. Commit your changes (`git commit -m 'Add new Lambda error scenario'`)
4. Push to the branch (`git push origin feature/new-lab`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📜 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

Free to use for personal learning, portfolio projects, and educational purposes.

---

## 🎯 Learning Outcomes

**After completing all 4 labs, you'll have:**

| Outcome | Description |
|---------|-------------|
| 📂 **Portfolio Project** | GitHub repository demonstrating AWS troubleshooting skills |
| 🔍 **Error Experience** | Debugged 20+ real AWS error scenarios |
| ☁️ **Service Knowledge** | Hands-on practice with 12+ AWS services |
| 🎓 **Methodology** | Systematic troubleshooting approach |
| 📊 **Monitoring Skills** | CloudWatch Logs and Metrics analysis |
| 🏗️ **IaC Experience** | Infrastructure as Code with Terraform |
| 🔒 **Security Practice** | Security incident response and remediation |
| 💼 **Interview Stories** | Real technical scenarios to discuss |

---

## ⭐ Support This Project

**If this lab helped you:**

1. ⭐ **Star this repository** - Help others discover it
2. 📢 **Share with others** - Learning AWS or cloud engineering
3. 💼 **Mention in interviews** - Demonstrate practical experience
4. 🤝 **Connect with me** - Share your success stories

**Success Stories:**

> "Error-driven learning helped me understand AWS errors I'd never seen in tutorials. When I got a similar error at work, I knew exactly how to debug it."

> "These labs prepared me for real cloud engineering interviews better than any course. I could speak confidently about actual troubleshooting experience."

---

## 🏆 Achievements

Track your progress:

- [ ] 🟢 Completed Lab 001 - EC2 Networking
- [ ] 🟠 Completed Lab 002 - S3 Security
- [ ] 🟡 Completed Lab 003 - Lambda Performance
- [ ] 🔵 Completed Lab 004 - Advanced Debugging
- [ ] 📝 Documented all learnings
- [ ] ⭐ Added to resume/LinkedIn
- [ ] 🎯 Used in job interview
- [ ] 💼 Landed cloud role

---

<div align="center">

**Learn by breaking things. Build confidence through debugging.**

Made with 🔧 for cloud engineers by cloud engineers

**[⬆ Back to Top](#aws-error-driven-troubleshooting-lab)**

</div>

---

## 📋 Keywords for ATS/Search

AWS troubleshooting, cloud engineer portfolio, AWS labs, Terraform tutorial, Lambda debugging, EC2 networking, S3 security, CloudWatch Logs, AWS hands-on practice, Infrastructure as Code, cloud support engineer, DevOps projects, AWS certification prep, entry-level cloud engineer, junior cloud engineer projects, AWS Solutions Architect, troubleshooting methodology, root cause analysis, production debugging, serverless debugging, VPC networking, IAM policies, CloudTrail forensics, AWS Well-Architected Framework, site reliability engineering, cloud operations, AWS monitoring, error handling, incident response, AWS CLI, boto3, Python AWS, Terraform AWS, cloud infrastructure, AWS Free Tier, learn AWS, AWS career change
## Deployment
Content to be added.

## Tech Stack
Content to be added.

## Incident Scenarios
Example incidents and how this project addresses them.

## Setup Instructions
1. Clone the repo
2. Install dependencies (`pip install -r requirements.txt` or as needed)
3. Configure environment variables if required
4. Run scripts or tests

## Usage Examples
```bash
python script_name.py --example-arg value
```
Replace with actual usage commands for this repo.

## Screenshots
Include screenshots of outputs, dashboards, or any UI here. Example:
![Example](path_to_screenshot.png)

## Contact
Reach me at your-email@example.com or GitHub: https://github.com/Charles-Bucher


## Overview
_TODO: Describe this section._


## Features
_TODO: Describe this section._


## Skills Demonstrated
_TODO: Describe this section._


## License
_TODO: Describe this section._
