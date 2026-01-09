# AWS Error-Driven Troubleshooting Lab

![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PowerShell](https://img.shields.io/badge/PowerShell-%235391FE.svg?style=for-the-badge&logo=powershell&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge)
![Status](https://img.shields.io/badge/status-active-success.svg?style=for-the-badge)

![CloudWatch](https://img.shields.io/badge/CloudWatch-FF4F8B?style=flat-square&logo=amazon-cloudwatch&logoColor=white)
![Lambda](https://img.shields.io/badge/Lambda-FF9900?style=flat-square&logo=aws-lambda&logoColor=white)
![S3](https://img.shields.io/badge/S3-569A31?style=flat-square&logo=amazon-s3&logoColor=white)
![EC2](https://img.shields.io/badge/EC2-FF9900?style=flat-square&logo=amazon-ec2&logoColor=white)
![IAM](https://img.shields.io/badge/IAM-DD344C?style=flat-square&logo=amazon-aws&logoColor=white)
![VPC](https://img.shields.io/badge/VPC-232F3E?style=flat-square&logo=amazon-aws&logoColor=white)

![GitHub last commit](https://img.shields.io/github/last-commit/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab?style=flat-square&color=blue)
![Maintenance](https://img.shields.io/maintenance/yes/2025?style=flat-square)
![Scenarios](https://img.shields.io/badge/Scenarios-4+-success?style=flat-square)
![Scripts](https://img.shields.io/badge/Scripts-15+-blue?style=flat-square)
![Runbooks](https://img.shields.io/badge/Runbooks-10+-orange?style=flat-square)
![AWS Cost](https://img.shields.io/badge/AWS_Cost-~$15%2Fmo-orange?style=flat-square&logo=amazon-aws)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/charles-bucher-cloud)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/charles-bucher)
[![Portfolio](https://img.shields.io/badge/Portfolio-255E63?style=for-the-badge&logo=About.me&logoColor=white)](https://github.com/charles-bucher)
[![Open to Work](https://img.shields.io/badge/Open%20to%20Work-2ea44f?style=for-the-badge)](https://linkedin.com/in/charles-bucher-cloud)

> **Real-world AWS incident response and troubleshooting scenarios**

---

## 🎯 TL;DR

**Who I Am:** 40-year-old delivery driver teaching myself cloud engineering to provide for my family (wife + 3 kids)

**What This Is:** Portfolio of intentionally broken AWS environments that I fix, document, and automate—proving I can do cloud support work, not just talk about it

**Why It Matters:** 
- ✅ **4+ real incidents** investigated with full RCA (not tutorials)
- ✅ **15+ Python/boto3 scripts** automating AWS troubleshooting
- ✅ **10+ production-standard runbooks** documenting fixes
- ✅ **All from my AWS account** (722631436033) - real work, real screenshots

**What I'm Looking For:** Entry-level cloud support/SysOps roles ($50k-$65k) where I can start immediately and prove myself through results

**Investment:** 50+ hours building this after 10-hour delivery shifts, $15/month from my paycheck running real AWS infrastructure

**Bottom Line:** I can't fake experience, so I'm building proof instead.

---

## 📑 Table of Contents

- [🎯 TL;DR](#-tldr)
- [🎯 Project Purpose](#-project-purpose)
- [🛠️ Technical Skills Demonstrated](#️-technical-skills-demonstrated)
- [📁 Repository Structure](#-repository-structure)
- [🚀 Quick Start](#-quick-start)
- [📸 Lab Screenshots](#-lab-screenshots)
- [📋 Available Scenarios](#-available-scenarios)
- [🔍 Learning Approach](#-learning-approach)
- [📚 Runbook Examples](#-runbook-examples)
- [🎓 Why This Approach Works](#-why-this-approach-works)
- [🏗️ Built With](#️-built-with)
- [📊 Lab Metrics](#-lab-metrics)
- [🙋‍♂️ About Me](#️-about-me)
- [📧 Contact](#-contact)

---

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

### AWS Services:
- **EC2** (instances, security groups, networking)
- **Lambda** (functions, triggers, permissions)
- **S3** (buckets, policies, versioning)
- **IAM** (roles, policies, least privilege)
- **VPC** (subnets, route tables, NACLs)
- **CloudWatch** (logs, metrics, alarms)

### Tools & Languages:
- **Python** (boto3, AWS automation)
- **PowerShell** (Windows-based AWS management)
- **Bash scripting** (Linux troubleshooting)
- **AWS CLI** (resource inspection and remediation)
- **Git/GitHub** (version control, CI/CD basics)

### Cloud Support Methodology:
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
├── lambdas/             # Lambda function code for scenarios
├── tests/               # Validation scripts to verify fixes
├── diagrams/            # Architecture diagrams and visual aids
├── screenshots/         # Evidence of troubleshooting process
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

Example workflow:
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

## 📸 Lab Screenshots

### Deployment & Setup:

**AWS CLI Identity Check**  
![AWS CLI configured and ready - verifying account access](screenshots/aws-cli-identity-check.png)

> AWS CLI configured and ready - verifying account access

**S3 Buckets Created**  
![S3 buckets deployed for troubleshooting scenarios](screenshots/s3-buckets-created.png)

> S3 buckets deployed for troubleshooting scenarios

**Lambda Functions**  
![Lambda functions deployed - intentionally misconfigured for practice](screenshots/lambda-functions-deployed.png)

> Lambda functions deployed - intentionally misconfigured for practice

### Troubleshooting in Action:

**Lab Fix Execution**  
![PowerShell script executing remediation steps](screenshots/powershell-fix-execution.png)

> PowerShell script executing remediation steps

**Deploy Output**  
![Initial deployment showing expected errors](screenshots/deploy-output-errors.png)

> Initial deployment showing expected errors

---

**Note:** All screenshots are from my actual AWS account (Account ID: 722631436033, Region: us-east-1). No stock images or tutorial screenshots - just real troubleshooting work.

## 📋 Available Scenarios

Each scenario is production-realistic and requires systematic troubleshooting:

| Scenario | AWS Services | Skills Practiced | Difficulty | Folder |
|----------|--------------|------------------|------------|--------|
| Lambda Permission Denied | Lambda, S3, IAM | IAM policy debugging, CloudWatch log analysis | ⭐⭐ Beginner | [📁](incidents/01_lambda_s3_permission_denied/) |
| EC2 Connection Timeout | EC2, VPC, Security Groups | Network troubleshooting, security group rules | ⭐⭐ Beginner | [📁](incidents/02_ec2_connection_timeout/) |
| S3 Access Denied | S3, IAM, Bucket Policies | S3 permissions, bucket policy debugging | ⭐⭐⭐ Intermediate | [📁](incidents/03_s3_access_denied/) |
| Lambda Timeout | Lambda, VPC, CloudWatch | Performance troubleshooting, timeout investigation | ⭐⭐⭐ Intermediate | [📁](incidents/04_lambda_timeout/) |

### Coming Soon:
- EC2 Instance Store Data Loss
- RDS Connection Pool Exhaustion
- API Gateway 502 Bad Gateway
- CloudFront Cache Invalidation Issues

> 💡 **Tip:** Start with the "Beginner" scenarios if you're new to AWS troubleshooting. Each incident includes a `scenario.md` file explaining the problem and an `expected_errors.txt` showing what you should see.

## 🔍 Learning Approach

This lab follows an **error-driven learning model**:

1. **Deploy** - Run a script to create a broken AWS environment
2. **Observe** - Encounter real error messages and failures
3. **Investigate** - Use AWS tools to gather diagnostic information
4. **Diagnose** - Apply root cause analysis techniques
5. **Remediate** - Fix the issue using AWS CLI or console
6. **Document** - Write up your findings and prevention steps
7. **Validate** - Run tests to confirm the fix works

This mirrors actual cloud support work where you receive a ticket, investigate logs, identify root cause, implement a fix, and document the incident.

### 💡 Example Workflow:

```bash
# 1. Navigate to a scenario
cd incidents/01_lambda_s3_permission_denied/

# 2. Read the scenario description
cat scenario.md

# 3. Deploy the broken environment
python deploy.py
# Output: Resources deployed. Lambda will fail with permission errors.

# 4. Investigate using AWS CLI
aws lambda get-function --function-name troubleshooting-lambda
aws logs tail /aws/lambda/troubleshooting-lambda --follow

# 5. Identify the root cause
# (IAM role missing S3 permissions)

# 6. Implement the fix
aws iam attach-role-policy \
  --role-name lambda-execution-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess

# 7. Validate the fix
python test_fix.py
# Output: ✅ Lambda executed successfully

# 8. Document your findings
# Compare with: cat ../../runbooks/01_lambda_s3_troubleshooting.md

# 9. Clean up resources
python cleanup.py
```

### 💰 Lab Costs

Estimated AWS costs per scenario:

| Resource | Cost | Notes |
|----------|------|-------|
| Lambda executions | ~$0.01 | First 1M requests free |
| S3 storage | ~$0.05 | Minimal test data |
| EC2 instances (t3.micro) | ~$0.10/hr | Stop when not using |
| CloudWatch Logs | ~$0.02 | 5GB free tier |
| **Total per scenario** | **~$0.20-$0.50** | If cleaned up after |

**Monthly estimate:** ~$10-15 if actively learning (2-3 scenarios/week)

#### 💡 Cost Saving Tips:
- Always run `cleanup.py` after each scenario
- Use AWS Budgets to set $15/month alert
- Stop EC2 instances when not troubleshooting
- Free Tier covers most Lambda/S3 usage

## 📚 Runbook Examples

Each runbook follows a standard incident response format:

1. **Incident Description** - What's broken and what symptoms appear
2. **Initial Triage** - First checks to perform
3. **Diagnostic Commands** - AWS CLI commands to gather data
4. **Root Cause Analysis** - Step-by-step investigation
5. **Remediation Steps** - How to fix the issue
6. **Validation** - Confirming the fix works
7. **Prevention** - How to avoid this in the future

These demonstrate the ability to create clear, actionable documentation—a critical skill for cloud support roles.

### 📚 Sample Runbooks:
- [RB-001: Lambda S3 Permission Troubleshooting](runbooks/01_lambda_s3_troubleshooting.md)
- [RB-002: EC2 Connection Timeout Debugging](runbooks/02_ec2_connection_timeout.md)
- [RB-003: S3 Access Denied Investigation](runbooks/03_s3_access_denied.md)
- [View All Runbooks →](runbooks/)

### 🔍 Sample Incidents:
- [INC-001: Lambda Permission Denied Error](incidents/01_lambda_s3_permission_denied/)
- [INC-002: EC2 Security Group Misconfiguration](incidents/02_ec2_connection_timeout/)
- [INC-003: S3 Bucket Policy Conflict](incidents/03_s3_access_denied/)
- [View All Incidents →](incidents/)

## 🎓 Why This Approach Works

Traditional labs show you how to build things correctly. This lab shows you how to **fix things when they break**—which is 80% of cloud operations work.

### Skills employers look for:

✅ **Troubleshooting mindset** (don't panic, investigate systematically)  
✅ **Log analysis** (CloudWatch, application logs, error messages)  
✅ **AWS service knowledge** (not just how to deploy, but how to debug)  
✅ **Documentation skills** (runbooks, incident reports)  
✅ **Automation** (scripts to detect, diagnose, and remediate issues)

### 💼 What Hiring Managers See Here:

| Instead of... | You see... |
|---------------|------------|
| "I passed the AWS SAA exam" | "Here are 4+ real incidents I investigated, diagnosed, and fixed" |
| "I know Python and boto3" | "Here are 15+ scripts I wrote to automate AWS troubleshooting" |
| "I can work independently" | "I built this entire lab on my own while working full-time" |
| "I document my work" | "Here are 10+ runbooks written to production standards" |

### 🎯 This Lab Proves I Can:

| Cloud Support Skill | Evidence in This Repo |
|---------------------|----------------------|
| Read AWS logs | Every scenario requires CloudWatch log analysis |
| Debug IAM permissions | Multiple IAM-related incidents documented |
| Troubleshoot systematically | Runbooks show step-by-step investigation |
| Use AWS CLI | All remediation uses CLI commands |
| Write documentation | 10+ runbooks in production format |
| Automate with Python | 15+ boto3 scripts for deployment/testing |
| Work independently | Self-taught, self-directed learning |
| Handle incidents | Full incident response workflow demonstrated |

**For staffing agencies:** This is exactly what your clients need for entry-level cloud support contracts—someone who can investigate tickets, read logs, and fix issues without extensive hand-holding.

## 🏗️ Built With

- **Python 3.9** - Primary scripting language for AWS automation
- **boto3** - AWS SDK for Python
- **AWS CLI** - Command-line interface for AWS services
- **PowerShell 7** - Windows-based AWS management scripts
- **GitHub Actions** - CI/CD for automated testing

### 📚 Learning Resources Used

**Free Resources I Used to Build This:**
- [AWS Documentation](https://docs.aws.amazon.com/) - Official service documentation
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) - Best practices
- [boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - Python AWS SDK
- [AWS CLI Reference](https://docs.aws.amazon.com/cli/latest/reference/) - Command-line tools
- [AWS re:Post](https://repost.aws/) - Community troubleshooting forums
- [Stack Overflow](https://stackoverflow.com/) - Specific error resolution

**Paid Resources:** $0 - Everything is free except AWS usage (~$15/month)

> No paid courses, no bootcamps, no hand-holding. Just documentation, practice, and determination.

## 🎯 Why This Lab Is Different

### Most "Learning Projects":
❌ Follow step-by-step tutorials that always work  
❌ Copy/paste code without understanding  
❌ Never encounter real errors  
❌ Skip documentation entirely  
❌ Focus on deployment, not troubleshooting

### This Lab:
✅ Intentionally breaks things to learn troubleshooting  
✅ Requires investigation - no solutions provided upfront  
✅ Mirrors real incidents - same errors you'd see in production  
✅ Documents everything - runbooks, incidents, RCAs  
✅ Focuses on fixing - 80% of cloud ops is troubleshooting

> **"Anyone can follow a tutorial. This lab proves you can figure things out when the tutorial is wrong."**  
> — The hiring manager mindset

## 📊 Lab Metrics

```yaml
name: Charles Bucher
role: Self-Taught Cloud Engineer
location: Largo, Florida
status: Open to Work

lab_stats:
  scenarios_created: 4+
  aws_services_used: 6
  python_scripts: 15+
  runbooks_documented: 10+
  average_troubleshooting_time: 15-30 minutes
  lab_hours: 50+
  monthly_aws_cost: ~$15

technical_skills:
  - AWS (Lambda, S3, EC2, IAM, VPC, CloudWatch)
  - Python (boto3, automation)
  - PowerShell (Windows management)
  - Bash (Linux troubleshooting)
  - Git/GitHub (version control)

currently_studying:
  - AWS Solutions Architect Associate
  - Advanced CloudWatch log analysis
  - IAM policy troubleshooting

ideal_roles:
  - AWS Cloud Support Associate
  - Junior Cloud Operations Engineer
  - Entry-level SysOps Administrator
  - Cloud Support Technician

motivation: "Building proof of skills, not just collecting certs"
```

### 🚀 Recent Updates
- **2025-01-05:** Added comprehensive README with badges and screenshots
- **2025-01-04:** Organized scripts and runbooks into proper folder structure
- **2024-12-20:** Initial commit with all incidents, scripts, and documentation

[View Full Changelog](https://github.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab/commits/) | [All Incidents](incidents/) | [All Runbooks](runbooks/)

---

> 💡 **For Hiring Managers:** This project demonstrates practical cloud troubleshooting skills beyond certifications. Each scenario requires the same systematic approach used in production support: investigating logs, analyzing errors, identifying root causes, implementing fixes, and documenting solutions. These are day-one skills for cloud support engineers, SREs, and DevOps roles.

## 🙋‍♂️ About Me

### Charles Bucher
**Self-Taught Cloud Engineer | Career Transition**

I'm 40 years old, married with three kids (ages 12, 11, and 2). I work part-time delivery while teaching myself cloud engineering to provide better for my family.

### Why This Lab Exists:
Instead of just watching videos and reading docs, I'm:

✅ Breaking AWS services intentionally to learn troubleshooting  
✅ Documenting everything like production systems  
✅ Building automation scripts to solve real problems  
✅ Creating runbooks that show my thought process

### What I'm NOT:
❌ A senior engineer pretending to be entry-level  
❌ Someone who just copied tutorials  
❌ A cert collector with no hands-on experience

### What I AM:
✅ Self-taught and learning every day  
✅ Honest about being entry-level  
✅ Willing to start small and prove myself  
✅ Ready to outwork anyone for this opportunity

### Current Status:
- **Studying for:** AWS Solutions Architect Associate
- **Looking for:** Entry-level Cloud Support / SysOps / Cloud Operations roles
- **Location:** Largo, Florida (remote preferred)
- **Salary expectations:** $50k-$65k (realistic for entry-level)

### What I'm Open To:
- Full-time W2 positions
- Contract work through staffing agencies
- Remote opportunities
- Hybrid roles in Tampa Bay area

**I Can Start:** Immediately - I'm ready to go

---

## 💪 What Makes This Portfolio Work:

### 1. Proof Over Promises
- I don't ask you to believe I can do the job
- I show you the actual work

### 2. Honest About Experience Level
- I'm not pretending to be senior
- I'm proving I can handle entry-level work

### 3. Real Investment
- I'm spending my own money ($15/month)
- I'm spending my own time (50+ hours)
- This isn't a weekend project

### 4. Remote-Ready Skills
- All troubleshooting done via CLI/console
- Documentation shows communication ability
- Self-directed learning proves independence

### 5. Growth Trajectory
- Started with basic scenarios
- Building complexity over time
- Continuously adding new incidents

---

## 🏆 For Employers Who Value Skills Over Background:

This portfolio demonstrates:

✅ **Work ethic** - Building this while working full-time delivery  
✅ **Determination** - Teaching myself without bootcamps or courses  
✅ **Accountability** - Documenting every step professionally  
✅ **Results** - Real AWS work, not just theory  
✅ **Growth mindset** - Learning from intentional failures

**I'm not looking for sympathy. I'm looking for opportunity to prove what I can do.**

Companies like Amazon, Accenture, IBM, and many staffing agencies actively hire entry-level cloud support roles and value skills-based portfolios like this. If you're one of them, let's talk.

---

## 📧 Contact

### Charles Bucher

- **GitHub:** [@charles-bucher](https://github.com/charles-bucher)
- **LinkedIn:** [charles-bucher-cloud](https://linkedin.com/in/charles-bucher-cloud)
- **Email:** Available on LinkedIn profile
- **Location:** Largo, Florida (Tampa Bay Area)

### Portfolio Projects:
- [AWS Error-Driven Troubleshooting Lab](https://github.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab) - This repository
- [CloudOpsLab](https://github.com/charles-bucher/CloudOpsLab) - Monitoring & automation

---

## 🤝 Contributing

This is a personal learning project demonstrating cloud troubleshooting skills, but suggestions for additional scenarios are welcome!

### Ways to help:
- 🐛 Report issues or suggest improvements
- 💡 Suggest realistic troubleshooting scenarios
- 📝 Improve documentation
- ⭐ Star this repo if it helped you learn

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

### Inspiration:
- My wife and three kids depending on this career change
- Need to prove skills through actual work, not just certs
- The self-taught developer community

### Tools:
- AWS Free Tier (made this possible)
- Python & boto3 (automation power)
- VS Code (development environment)
- Git/GitHub (version control & portfolio hosting)

---

## ⭐ If This Helped You

If this repo helped you learn AWS troubleshooting or gave you ideas for your own portfolio, please give it a star! It helps others find it.

---

<div align="center">

**Built with ☕, Python, and determination**

**Charles Bucher | Self-Taught Cloud Engineer**

*"I can't fake experience, so I'm building proof instead"*

![Profile Views](https://komarev.com/ghpvc/?username=charles-bucher&color=brightgreen)

---

### AWS Error-Driven Troubleshooting Lab
*Learning cloud support through real incidents, not tutorials*

**Status:** 🟢 Active | 💼 Open to Work | 📍 Florida

[⬆ Back to Top](#aws-error-driven-troubleshooting-lab)

---

**Questions?** [Open an Issue](https://github.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab/issues) or [Connect on LinkedIn](https://linkedin.com/in/charles-bucher-cloud)

</div>

---

## About

Intentionally broken AWS scenarios for hands-on troubleshooting using real cloud support workflows. Focused on logs, metrics, root cause analysis, remediation, and prevention — not tutorials or guided labs.

### Topics

`python` `linux` `bash` `aws` `portfolio` `automation` `monitoring` `aws-lambda` `aws-s3` `logging` `incident-response` `vpc` `aws-ec2` `troubleshooting` `remediation` `cloud-support` `root-cause-analysis` `hands-on-labs` `error-driven-learning`

---

**© 2025 Charles Bucher | MIT License**