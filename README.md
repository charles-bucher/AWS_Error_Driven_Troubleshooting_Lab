# AWS Error-Driven Troubleshooting Lab 🔧

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-1.0+-7B42BC?logo=terraform&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-Cloud-FF9900?logo=amazon-aws&logoColor=white)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Learning](https://img.shields.io/badge/Learning-Error--Driven-red.svg)

> **Learn AWS troubleshooting by breaking things, investigating errors, and fixing them**

Hands-on error-driven learning lab featuring **4 real-world AWS incidents**. Each lab intentionally introduces errors, then guides you through investigation, root cause analysis, and remediation—teaching practical cloud troubleshooting skills through experience.

---

## 🎯 What is Error-Driven Learning?

**Traditional Learning:** Read documentation → Deploy perfectly → Never see real errors

**Error-Driven Learning:** Deploy → Break something → Investigate logs → Fix it → Learn deeply

This approach mirrors real cloud engineering work where you:
1. Encounter unexpected errors
2. Read logs and metrics
3. Form hypotheses
4. Test solutions
5. Document what you learned

**Perfect for:** Entry-level cloud engineers learning practical troubleshooting skills

---

## 🔬 The 4 Error Labs

Each lab follows the same proven methodology:

### Lab Structure
1. **Deploy** - Set up AWS infrastructure with Terraform
2. **Break** - Intentionally introduce a realistic misconfiguration
3. **Investigate** - Use CloudWatch, CloudTrail, and AWS Console to find the issue
4. **Fix** - Remediate the problem following best practices
5. **Validate** - Confirm the fix works
6. **Document** - Record what you learned

---

## 🚨 Lab 001: EC2 SSH Lockout

**The Error:** Can't SSH into EC2 instance - connection times out

**What You'll Learn:**
- VPC networking fundamentals
- Security group configuration
- Route table troubleshooting
- Network ACLs vs Security Groups
- VPC Flow Logs analysis

### Visual Walkthrough

![Security Groups](incidents/001-ec2-ssh-lockout/001_screenshots/001_04_security_group.png)
*Security group misconfiguration blocking SSH access*

![EC2 Instances](incidents/001-ec2-ssh-lockout/001_screenshots/001_05_ec2_instances.png)
*EC2 instances deployed but unreachable due to network issues*

**Skills Practiced:**
- EC2 instance troubleshooting
- VPC networking
- Security group rules
- SSH connectivity debugging

[📖 Full Lab Guide](incidents/001-ec2-ssh-lockout/README.md)

---

## 🚨 Lab 002: S3 Bucket Accidentally Public

**The Error:** S3 bucket exposed to internet - potential data breach

**What You'll Learn:**
- S3 bucket policy analysis
- IAM permissions debugging
- CloudTrail forensics
- Security incident response
- Block Public Access settings

### Visual Walkthrough

![S3 Workflow](incidents/002-s3-public-bucket/002_screenshots/002_04_full_workflow.png)
*Complete workflow from deployment through investigation to remediation*

![Bucket Misconfiguration](incidents/002-s3-public-bucket/002_screenshots/002_02_bucket_misconfig.png)
*S3 bucket policy misconfigured allowing public access*

![Evidence Collection](incidents/002-s3-public-bucket/002_screenshots/002_03_collect_evidence.png)
*Using CloudTrail to investigate who made the configuration change*

**Skills Practiced:**
- S3 security configuration
- Bucket policies
- IAM troubleshooting
- CloudTrail forensics
- Security compliance

[📖 Full Lab Guide](incidents/002-s3-public-bucket/README.md)

---

## 🚨 Lab 003: Lambda Function Timeout

**The Error:** Lambda function fails with timeout errors under load

**What You'll Learn:**
- Lambda performance tuning
- CloudWatch Logs investigation
- Memory vs timeout configuration
- Error handling best practices
- Performance optimization

### Visual Walkthrough

![Lambda Deployment](incidents/003-lambda-timeout/003_screenshots/003_01_lambda_deploy.png)
*Lambda function deployed with insufficient resources*

![CloudWatch Logs](incidents/003-lambda-timeout/003_screenshots/003_03_collect_logs.png)
*Investigating timeout errors in CloudWatch Logs*

![Break and Fix](incidents/003-lambda-timeout/003_screenshots/003_break_mock.png)
*Intentionally introducing timeout by reducing memory allocation*

**Skills Practiced:**
- Serverless troubleshooting
- Lambda configuration
- CloudWatch Logs analysis
- Performance debugging
- Resource optimization

[📖 Full Lab Guide](incidents/003-lambda-timeout/README.md)

---

## 🚨 Lab 004: Lambda Timeout (Advanced)

**The Error:** Complex Lambda timeout with multiple root causes

**What You'll Learn:**
- Multi-factor troubleshooting
- Dependency conflicts
- Cold start optimization
- Concurrent execution issues
- Advanced Lambda debugging

**Skills Practiced:**
- Complex error diagnosis
- Multiple hypothesis testing
- Advanced serverless patterns
- Production debugging techniques

[📖 Full Lab Guide](incidents/004-lambda-timeout/README.md)

---

## 🚀 Quick Start

### Prerequisites

- **AWS Account** (free tier works for most labs)
- **AWS CLI** configured with credentials
- **Terraform** 1.0+ installed
- **Python** 3.9+ installed
- Basic command line familiarity

### Run Your First Lab

```bash
# 1. Clone the repository
git clone https://github.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab.git
cd AWS_Error_Driven_Troubleshooting_Lab

# 2. Start with Lab 001
cd incidents/001-ec2-ssh-lockout

# 3. Read the lab guide
cat README.md

# 4. Deploy infrastructure
cd terraform
terraform init
terraform apply

# 5. Follow the lab instructions to:
#    - Break the configuration
#    - Investigate the error
#    - Fix the issue
#    - Validate your solution
```

---

## 📂 Project Structure

```
AWS_Error_Driven_Troubleshooting_Lab/
├── .github/workflows/      # CI/CD automation
├── diagrams/               # Architecture diagrams
├── docs/                   # Documentation
├── incidents/              # The 4 error labs
│   ├── 001-ec2-ssh-lockout/
│   │   ├── 001_screenshots/
│   │   ├── scripts/
│   │   ├── terraform/
│   │   └── README.md       # Lab 001 guide
│   ├── 002-s3-public-bucket/
│   │   ├── 002_screenshots/
│   │   ├── scripts/
│   │   ├── terraform/
│   │   └── README.md       # Lab 002 guide
│   ├── 003-lambda-timeout/
│   │   ├── 003_screenshots/
│   │   ├── scripts/
│   │   ├── terraform/
│   │   └── README.md       # Lab 003 guide
│   └── 004-lambda-timeout/
│       ├── scripts/
│       ├── terraform/
│       └── README.md       # Lab 004 guide
├── lambdas/                # Lambda function code
├── src/                    # Helper scripts
├── tests/                  # Validation tests
└── README.md              # This file
```

---

## 🎓 Learning Path

### Beginner (Start Here)
**Lab 001: EC2 SSH Lockout**
- Fundamental AWS networking
- Security group basics
- Simple troubleshooting

### Intermediate
**Lab 002: S3 Security Issue**
- IAM and permissions
- Security investigation
- CloudTrail forensics

**Lab 003: Lambda Timeout**
- Serverless concepts
- Performance tuning
- Log analysis

### Advanced
**Lab 004: Complex Lambda Issues**
- Multi-factor debugging
- Production scenarios
- Advanced troubleshooting

---

## 💡 Skills You'll Gain

### 🔍 Troubleshooting Methodology
- Systematic error investigation
- Root cause analysis
- Hypothesis testing
- Solution validation

### ☁️ AWS Services
- **Compute:** EC2, Lambda
- **Storage:** S3
- **Networking:** VPC, Security Groups, NACLs
- **Monitoring:** CloudWatch, CloudTrail
- **Security:** IAM, GuardDuty

### 🛠️ Tools & Technologies
- AWS Console navigation
- CloudWatch Logs interpretation
- Terraform infrastructure management
- AWS CLI commands
- Python scripting

### 📊 Observability
- Reading CloudWatch metrics
- Analyzing CloudWatch Logs
- Using CloudTrail for forensics
- VPC Flow Logs analysis
- Performance monitoring

### 🔒 Security
- IAM policy debugging
- Security group configuration
- S3 bucket security
- Incident response
- Compliance validation

---

## 🔧 What Makes This Different

### Traditional Labs
❌ Perfect deployments that always work  
❌ No exposure to real errors  
❌ Skip the investigation phase  
❌ Don't teach debugging skills  

### Error-Driven Labs
✅ Intentionally break things  
✅ Experience real error messages  
✅ Practice log investigation  
✅ Learn troubleshooting methodology  
✅ Build debugging confidence  

---

## 🎯 Use Cases

### For Learning
- Build troubleshooting muscle memory
- See real error messages before interviews
- Practice systematic debugging
- Gain confidence in AWS Console

### For Portfolios
- Demonstrate practical troubleshooting skills
- Show ability to work with logs
- Prove infrastructure knowledge
- Document problem-solving approach

### For Interviews
- Reference real scenarios you've debugged
- Discuss your troubleshooting methodology
- Show hands-on AWS experience
- Explain specific error patterns you've seen

---

## 📝 Lab Methodology

Each lab follows this proven structure:

### 1. Deploy Infrastructure
Use Terraform to create AWS resources in a known-good state

### 2. Break Something
Introduce a realistic misconfiguration that mirrors production issues

### 3. Observe the Error
See the actual error message, just like you would in production

### 4. Investigate
- Check CloudWatch Logs
- Review CloudTrail events
- Examine resource configurations
- Form hypotheses about root cause

### 5. Remediate
Apply the fix following AWS best practices

### 6. Validate
Confirm the issue is resolved and service is restored

### 7. Document
Record what you learned for future reference

---

## 🤝 Contributing

Contributions welcome! This is an active learning project.

**How to contribute:**
- 🐛 Report bugs or issues with labs
- 💡 Suggest new error scenarios
- 📝 Improve lab documentation
- ✨ Add new troubleshooting techniques

---

## 📜 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

---

## 🔒 Security

**Note:** These labs intentionally create misconfigurations for learning purposes. Always:
- Use a dedicated learning AWS account
- Never run these labs in production
- Destroy resources after completing labs (use `terraform destroy`)
- Review AWS costs before deploying

---

## 📞 Connect With Me

**Charles Bucher** - Cloud Engineer | AWS Enthusiast

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Charles__Bucher-0A66C2?logo=linkedin&logoColor=white)](https://linkedin.com/in/charles-bucher-cloud)
[![GitHub](https://img.shields.io/badge/GitHub-charles--bucher-181717?logo=github&logoColor=white)](https://github.com/charles-bucher)
[![Portfolio](https://img.shields.io/badge/Portfolio-View-success?logo=github&logoColor=white)](https://charles-bucher.github.io)

---

## 🌟 Related Projects

- [AWS Cloud Support Simulator](https://github.com/charles-bucher/AWS_Cloud_Support_Sim) - 7 production incident scenarios
- [AWS CloudOps Suite](https://github.com/charles-bucher/AWS_Cloudops_Suite) - Cloud operations automation toolkit

---

## 💬 Testimonials

> "Error-driven learning helped me understand AWS errors I'd never seen in tutorials. When I got a similar error at work, I knew exactly how to debug it." - Student feedback

> "These labs prepared me for real cloud engineering interviews better than any course. I could speak confidently about actual troubleshooting experience." - Career changer

---

<div align="center">

**⭐ If this lab helped you learn AWS troubleshooting, please star it! ⭐**

**Learn by breaking things. Build confidence through debugging.**

Made with 🔧 by [Charles Bucher](https://github.com/charles-bucher)

</div>