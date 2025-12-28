# AWS Error-Driven Troubleshooting Lab

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![AWS](https://img.shields.io/badge/AWS-Cloud-orange.svg)](https://aws.amazon.com/)
[![Terraform](https://img.shields.io/badge/Terraform-IaC-purple.svg)](https://www.terraform.io/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Learning](https://img.shields.io/badge/Type-Hands--on%20Labs-brightgreen.svg)]()

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

## 📊 Project Stats

- **4 Production-Grade Labs** covering EC2, S3, Lambda, VPC
- **12+ AWS Services** hands-on experience
- **20+ Real Error Scenarios** you'll debug
- **100% Infrastructure as Code** using Terraform
- **Automated Tests** to validate your fixes

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

### Lab 001: EC2 SSH Connection Timeout
**Error:** `ssh: connect to host X.X.X.X port 22: Operation timed out`

**Root Cause:** Security group misconfiguration blocking SSH access

**Skills:** VPC networking, security groups, route tables, VPC Flow Logs, EC2 connectivity debugging

**AWS Services:** EC2, VPC, Security Groups, NACLs, CloudWatch

![Security Group Misconfiguration](incidents/001-ec2-ssh-lockout/001_screenshots/001_sg_before.png)

**What You'll Fix:**
- Diagnose network connectivity issues
- Analyze security group rules
- Understand VPC Flow Logs
- Configure proper SSH access

[📖 **Full Lab Guide →**](incidents/001-ec2-ssh-lockout/README.md)

---

### Lab 002: S3 Bucket Accidentally Public
**Error:** `S3 bucket exposed to internet - potential security breach`

**Root Cause:** Misconfigured bucket policy allowing public read access

**Skills:** S3 security, IAM policies, CloudTrail forensics, incident response, security compliance

**AWS Services:** S3, IAM, CloudTrail, GuardDuty, AWS Config

![S3 Public Access Investigation](incidents/002-s3-public-bucket/002_screenshots/002_investigation.png)

**What You'll Fix:**
- Investigate security incidents using CloudTrail
- Remediate public S3 buckets
- Implement Block Public Access
- Understand IAM vs bucket policies

[📖 **Full Lab Guide →**](incidents/002-s3-public-bucket/README.md)

---

### Lab 003: Lambda Function Timeout
**Error:** `Task timed out after 3.00 seconds`

**Root Cause:** Insufficient memory allocation causing timeout under load

**Skills:** Serverless troubleshooting, Lambda configuration, CloudWatch Logs analysis, performance optimization

**AWS Services:** Lambda, CloudWatch Logs, CloudWatch Metrics, X-Ray

![Lambda Timeout Investigation](incidents/003-lambda-timeout/003_screenshots/003_cloudwatch_logs.png)

**What You'll Fix:**
- Analyze CloudWatch Logs for Lambda errors
- Optimize Lambda memory and timeout settings
- Understand cold starts vs warm starts
- Debug serverless performance issues

[📖 **Full Lab Guide →**](incidents/003-lambda-timeout/README.md)

---

### Lab 004: Lambda Timeout (Advanced Multi-Factor)
**Error:** Multiple cascading timeout issues

**Root Cause:** Complex combination of memory limits, dependency conflicts, and concurrent execution throttling

**Skills:** Advanced troubleshooting, multi-hypothesis testing, production debugging, complex error diagnosis

**AWS Services:** Lambda, CloudWatch, X-Ray, VPC, IAM

**What You'll Fix:**
- Diagnose multiple simultaneous issues
- Test and eliminate hypotheses systematically
- Apply advanced Lambda optimization
- Handle production-grade scenarios

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

### Installation
```bash
# Clone repository
git clone https://github.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab.git
cd AWS_Error_Driven_Troubleshooting_Lab

# Install Python dependencies
pip install -r requirements.txt

# Start with Lab 001
cd incidents/001-ec2-ssh-lockout
```

### Run Your First Lab
```bash
# 1. Read the lab guide
cat README.md

# 2. Deploy infrastructure
cd terraform
terraform init
terraform apply -auto-approve

# 3. Follow the lab steps:
#    → Break the configuration
#    → Investigate the error
#    → Fix the issue
#    → Validate your solution

# 4. Clean up resources
terraform destroy -auto-approve
```

---

## 💼 Skills Demonstrated

### Cloud Engineering
- ✅ AWS service troubleshooting (EC2, Lambda, S3, VPC)
- ✅ Root cause analysis methodology
- ✅ CloudWatch Logs and Metrics interpretation
- ✅ Infrastructure as Code with Terraform
- ✅ Security incident response

### Technical Competencies
- ✅ VPC networking and security groups
- ✅ Serverless architecture debugging
- ✅ IAM policy analysis
- ✅ Performance optimization
- ✅ Bash and Python scripting

### Professional Skills
- ✅ Systematic problem-solving
- ✅ Documentation and communication
- ✅ Hypothesis-driven debugging
- ✅ Solution validation and testing

---

## 📂 Repository Structure

```
AWS_Error_Driven_Troubleshooting_Lab/
├── incidents/
│   ├── 001-ec2-ssh-lockout/      # Lab 1: VPC networking
│   │   ├── terraform/            # Infrastructure code
│   │   ├── scripts/              # Automation scripts
│   │   ├── 001_screenshots/      # Visual documentation
│   │   └── README.md             # Lab guide
│   ├── 002-s3-public-bucket/     # Lab 2: S3 security
│   ├── 003-lambda-timeout/       # Lab 3: Lambda performance
│   └── 004-lambda-timeout/       # Lab 4: Advanced debugging
├── lambdas/                      # Lambda function code
├── tests/                        # Automated validation
├── diagrams/                     # Architecture diagrams
└── docs/                         # Additional documentation
```

---

## 🎓 Learning Path

**Beginner Track** (Start here if new to AWS)
1. Lab 001: EC2 SSH Lockout → Learn VPC networking fundamentals
2. Lab 002: S3 Public Bucket → Understand security and IAM

**Intermediate Track** (Comfortable with AWS basics)
3. Lab 003: Lambda Timeout → Master serverless troubleshooting

**Advanced Track** (Preparing for cloud engineering roles)
4. Lab 004: Complex Lambda Issues → Handle production scenarios

**Estimated Time:** 8-10 hours to complete all labs with notes

---

## 🎯 Use Cases

### For Job Seekers
✓ **Portfolio Project** - Demonstrate hands-on AWS troubleshooting experience  
✓ **Interview Prep** - Reference specific errors you've debugged  
✓ **Resume Skills** - List concrete AWS services and tools used  
✓ **GitHub Activity** - Show active learning and technical growth  

### For Certification Study
✓ **AWS Solutions Architect Associate** - Practice VPC, EC2, S3, Lambda scenarios  
✓ **AWS SysOps Administrator** - Focus on CloudWatch, troubleshooting, operations  
✓ **AWS DevOps Engineer** - Infrastructure as Code and CI/CD concepts  

### For Career Changers
✓ **Practical Experience** - Build real troubleshooting skills without a job  
✓ **Confidence Building** - Work through errors in safe learning environment  
✓ **Technical Communication** - Practice explaining your debugging process  

---

## 🛠️ Technologies Used

| Category | Technologies |
|----------|-------------|
| **Cloud Platform** | AWS (EC2, Lambda, S3, VPC, IAM) |
| **Infrastructure** | Terraform, CloudFormation |
| **Monitoring** | CloudWatch Logs, CloudWatch Metrics, CloudTrail |
| **Languages** | Python 3.9+, Bash, HCL |
| **Security** | IAM, Security Groups, S3 Bucket Policies |
| **Testing** | pytest, boto3 |

---

## 📈 What Makes This Different

| Traditional Labs | This Project |
|-----------------|--------------|
| Perfect deployments that always work | Intentionally break things to learn |
| Skip over error messages | Experience real AWS errors |
| No investigation phase | Practice log analysis and debugging |
| No troubleshooting skills | Build systematic problem-solving |
| Theory-focused | Hands-on practical experience |

---

## ✅ Lab Methodology

Every lab follows this proven 7-step process:

1. **Deploy** - Set up infrastructure with Terraform
2. **Break** - Introduce realistic misconfiguration
3. **Observe** - See the actual error message
4. **Investigate** - Use CloudWatch, CloudTrail, AWS Console
5. **Remediate** - Fix following AWS best practices
6. **Validate** - Confirm resolution with tests
7. **Document** - Record learnings in lab notes

This mirrors real cloud engineering workflows used in production support roles.

---

## 💡 Key Learnings

After completing these labs, you'll be able to:

- Navigate CloudWatch Logs efficiently to find error root causes
- Interpret common AWS error messages (timeouts, permission denied, connection refused)
- Use CloudTrail to investigate security incidents
- Debug VPC networking issues systematically
- Optimize Lambda function performance
- Secure S3 buckets properly
- Write Infrastructure as Code with Terraform
- Document troubleshooting processes clearly

---

## 🔒 Cost & Security

**AWS Costs:** < $5 total if you:
- Use AWS Free Tier eligible services
- Run labs in us-east-1 region
- Destroy resources immediately after completing each lab

**Security Note:** These labs intentionally create misconfigurations for learning.

⚠️ **ALWAYS:**
- Use a dedicated learning AWS account (not production)
- Run `terraform destroy` after completing each lab
- Never commit AWS credentials to Git
- Set up billing alerts before starting

---

## 📞 Connect

**Charles Bucher** | Cloud Engineer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://linkedin.com/in/charles-bucher-cloud)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/charles-bucher)

---

## 🌟 Related Projects

- [AWS Cloud Support Simulator](https://github.com/charles-bucher) - 7 production incident scenarios
- [AWS CloudOps Suite](https://github.com/charles-bucher) - Cloud operations automation

---

## 🤝 Contributing

Contributions welcome! Ways to help:

- 🐛 Report bugs or issues with labs
- 💡 Suggest new error scenarios
- 📝 Improve documentation
- ✨ Add troubleshooting techniques
- 🧪 Contribute test cases

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📜 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## ⭐ Support This Project

If this lab helped you learn AWS troubleshooting or land a cloud role:

1. ⭐ Star this repository
2. 📢 Share with others learning AWS
3. 💼 Mention it in your job interviews
4. 🤝 Connect with me on LinkedIn

---

## 🎯 Learning Outcomes

**After completing all 4 labs, you'll have:**

✅ Portfolio-ready GitHub project demonstrating AWS troubleshooting  
✅ Experience debugging 20+ real AWS error scenarios  
✅ Hands-on practice with 12+ AWS services  
✅ Systematic troubleshooting methodology  
✅ CloudWatch Logs analysis skills  
✅ Infrastructure as Code experience  
✅ Security incident response practice  
✅ Interview-ready technical stories  

---

<div align="center">

**Learn by breaking things. Build confidence through debugging.**

Made with 🔧 for cloud engineers by cloud engineers

**[⬆ Back to Top](#aws-error-driven-troubleshooting-lab)**

</div>

---

## 📋 Keywords for Search

AWS troubleshooting, cloud engineer portfolio, AWS labs, Terraform tutorial, Lambda debugging, EC2 networking, S3 security, CloudWatch Logs, AWS hands-on practice, Infrastructure as Code, cloud support engineer, DevOps projects, AWS certification prep, entry-level cloud engineer, junior cloud engineer projects, AWS Solutions Architect, troubleshooting methodology, root cause analysis, production debugging, serverless debugging