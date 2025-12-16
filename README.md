# AWS Error Driven Troubleshooting Lab

![GitHub last commit](https://img.shields.io/github/last-commit/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab)
![GitHub repo size](https://img.shields.io/github/repo-size/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab)
![GitHub issues](https://img.shields.io/github/issues/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab)
![GitHub license](https://img.shields.io/github/license/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab)
![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?logo=python)
![Terraform](https://img.shields.io/badge/Terraform-623CE4?logo=terraform&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?logo=amazon-aws&logoColor=FF9900)

## 📊 Architecture

![AWS Error Driven Lab Architecture](./aws-error-driven-lab-architecture.png)

## 🚀 Overview

The **AWS Error Driven Troubleshooting Lab** is a hands-on simulation environment designed to teach real-world incident response and troubleshooting skills in AWS. This lab focuses on:

- Identifying and diagnosing cloud infrastructure issues
- Analyzing logs, metrics, and alerts
- Implementing remediation and preventive measures
- Learning AWS best practices for fault-tolerant systems

This lab is perfect for aspiring **AWS Cloud Support Engineers, CloudOps, and Site Reliability Engineers**.

---

## 🧰 Tech Stack

| Technology | Purpose |
|------------|---------|
| AWS EC2 | Compute instances for simulations |
| AWS S3 | Storage and logging |
| AWS Lambda | Automation & remediation scripts |
| AWS CloudWatch | Monitoring, metrics, and alerts |
| Python 🐍 | Scripting and automation |
| Terraform | Infrastructure as code setup |

---

## 🎯 Key Features

- **Pre-Broken Environment:** Every lab environment is intentionally misconfigured to simulate real-world errors.  
- **Step-by-Step Error Analysis:** Learn root cause analysis using logs, alerts, and metrics.  
- **Automated Remediation:** Practice writing scripts to automatically remediate common AWS issues.  
- **Preventive Strategies:** Implement best practices to prevent future failures.  

---

## 📂 Repository Structure

```
AWS_Error_Driven_Troubleshooting_Lab/
│
├── README.md                         # This documentation
├── aws-error-driven-lab-architecture.png  # Architecture diagram
├── incidents/                        # Individual incident scenarios
│   ├── incident_001_ec2_unreachable/
│   │   ├── scripts/         # deploy.py, break.py, collect_evidence.py, teardown.py
│   │   ├── evidence/        # Logs and screenshots
│   │   └── README.md        # Incident-specific documentation
│   ├── incident_002_s3_permission/
│   └── incident_003_lambda_failure/
├── scripts/                          # Global automation scripts
├── templates/                        # Reusable templates
├── docs/                             # Detailed guides and notes
├── create_lab_structure.py   # Lab setup automation
├── spin_incidents.py         # Incident deployment script
└── terminate_all_aws.ps1     # Cleanup script
```

---

## 🎬 Incident Scenarios

| Incident ID | Summary | Status |
|-------------|---------|--------|
| [incident_001_ec2_unreachable](./incidents/incident_001_ec2_unreachable/) | EC2 instance cannot be reached over SSH | ✅ Complete |
| [incident_002_s3_permission](./incidents/incident_002_s3_permission/) | Misconfigured S3 bucket policy blocking access | ⚠️ In Progress |
| [incident_003_lambda_failure](./incidents/incident_003_lambda_failure/) | Lambda function throwing runtime errors | ⚠️ In Progress |
| incident_004_custom | Custom incident for testing your own failures | 🛠 Placeholder |

---

## 🖼️ Evidence Examples

Each incident folder contains an `evidence/` directory with:
- **Screenshots:** Console captures, error states, configuration proofs
- **Logs:** CloudWatch exports, system logs, error traces
- **Metrics:** CPU/memory graphs, network traffic data

**Example evidence structure:**
```
incident_001_ec2_unreachable/evidence/
├── screenshots/
│   ├── screenshot_001_instances_info.png
│   ├── screenshot_002_security_groups.png
│   └── screenshot_003_vpc_creation.png
└── logs/
    ├── cloudwatch_logs.txt
    └── system_logs.txt
```

To reference screenshots in your incident README:
```markdown
![EC2 Instance Info](./evidence/screenshots/screenshot_001_instances_info.png)
```

---

## 📖 How to Use

### 1. Clone the repository
```bash
git clone https://github.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab.git
cd AWS_Error_Driven_Troubleshooting_Lab
```

### 2. Set up AWS credentials
```bash
aws configure
# Enter your AWS Access Key ID, Secret Access Key, and region
```

### 3. Create lab structure (first time only)
```bash
python create_lab_structure.py
```

### 4. Deploy an incident scenario
```bash
python spin_incidents.py
```
⚠️ **Warning:** This creates live AWS resources. Charges may apply.

### 5. Troubleshoot the incident
- Navigate to the incident folder (e.g., `incidents/incident_001_ec2_unreachable/`)
- Review the incident README
- Use AWS Console and CLI to investigate
- Run `scripts/collect_evidence.py` to gather logs and metrics
- Document your findings in the incident README

### 6. Remediate the issue
- Apply fixes manually or run remediation scripts
- Verify the issue is resolved
- Document root cause and resolution steps

### 7. Clean up resources
```powershell
# PowerShell
.\terminate_all_aws.ps1
```
or
```bash
# Bash
cd incidents/incident_001_ec2_unreachable/scripts/
python teardown.py
```

---

## 💡 Learning Outcomes

By completing this lab, you will be able to:

✅ Diagnose AWS service failures and misconfigurations  
✅ Write automation scripts for remediation  
✅ Implement monitoring and alerting best practices  
✅ Understand fault tolerance and resilience in cloud systems  
✅ Build professional incident documentation with evidence  

---

## 🎯 Workflow Summary

```
1. DEPLOY    → Spin up AWS infrastructure with deploy.py
2. BREAK     → Intentionally inject failures with break.py
3. DIAGNOSE  → Investigate using AWS Console, CLI, logs
4. COLLECT   → Gather evidence with collect_evidence.py
5. REMEDIATE → Fix issues and document root cause
6. TEARDOWN  → Clean up resources with teardown.py
```

---

## 📚 Learning Resources

- [AWS Documentation](https://docs.aws.amazon.com/)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
- [AWS Troubleshooting Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-troubleshoot.html)
- [Terraform AWS Provider Docs](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [Python Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

---

## 🔧 Requirements

- Python 3.14+
- boto3 (install via `pip install boto3 --break-system-packages`)
- AWS CLI configured
- PowerShell (for teardown scripts on Windows)
- Basic AWS knowledge: EC2, VPC, Subnets, IGW, Security Groups, S3, Lambda

---

## ⭐ Contributing

Contributions are welcome! Please submit pull requests for:

- Additional broken scenarios
- New remediation scripts
- Updated diagrams or screenshots
- Documentation improvements

**Guidelines:**
- Keep incidents consistent in structure
- Include README.md and evidence/screenshots for each incident
- Never commit AWS credentials or private keys

---

## 📝 Lessons Learned

💡 AWS breaks in unpredictable ways; hands-on practice accelerates learning  
💡 Always tear down resources to avoid unexpected bills  
💡 IAM & permissions mistakes are your first lesson  
💡 Documentation + screenshots matter—they are proof of skill, not decoration  

---

## 👤 Author

**Charles Bucher** – Cloud Support / DevOps Self-Taught  
- GitHub: [@charles-bucher](https://github.com/charles-bucher)
- Portfolio: [charles-bucher.github.io](https://charles-bucher.github.io/)
- Email: quietopscb@gmail.com
- LinkedIn: [charles-bucher-cloud](https://www.linkedin.com/in/charles-bucher-cloud)

---

## ⚡ License

MIT License © Charles Bucher

---

## ⚠️ Disclaimer

This lab is for learning purposes only. Running scripts can create billable AWS resources. Always clean up resources after use to avoid unexpected charges.