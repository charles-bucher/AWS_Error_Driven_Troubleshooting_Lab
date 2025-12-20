# AWS Error Driven Troubleshooting Lab

![Python](https://img.shields.io/badge/python-3.14%2B-blue?logo=python&style=for-the-badge)
![Terraform](https://img.shields.io/badge/Terraform-%3E%3D1.0-blue?logo=terraform&style=for-the-badge)
![GitHub Repo Size](https://img.shields.io/github/repo-size/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![GitHub Last Commit](https://img.shields.io/github/last-commit/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab?style=for-the-badge)
![GitHub Stars](https://img.shields.io/github/stars/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab?style=for-the-badge)
![GitHub Forks](https://img.shields.io/github/forks/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab?style=for-the-badge)

---

## 📊 Architecture
AWS Error Driven Lab Architecture

---

## 🚀 Overview
This lab is a hands-on AWS simulation environment designed to **teach real-world incident response and troubleshooting skills**.  

You will learn to:

- Identify and diagnose AWS infrastructure issues  
- Analyze logs, metrics, and alerts  
- Apply remediation and preventive measures  
- Follow AWS best practices for fault-tolerant systems  

Perfect for **Cloud Support Engineers, CloudOps, and SREs**.

---

## 🧰 Tech Stack

| Technology | Purpose |
|------------|--------|
| AWS EC2 | Compute for simulations |
| AWS S3 | Storage & logging |
| AWS Lambda | Automation & remediation scripts |
| AWS CloudWatch | Monitoring, metrics, alerts |
| Python 🐍 | Scripting and automation |
| Terraform | Infrastructure as code setup |

---

## 🎯 Key Features

- Pre-Broken Environment: Intentional misconfigurations for realistic troubleshooting  
- Step-by-Step Error Analysis: Learn root cause analysis with logs & metrics  
- Automated Remediation: Write scripts to fix AWS issues automatically  
- Preventive Strategies: Implement best practices to prevent future failures  

---

## 📂 Repository Structure
AWS_Error_Driven_Troubleshooting_Lab/
│
├── README.md
├── diagrams/ # Architecture diagrams
├── incidents/ # Incident scenarios
├── scripts/ # Global automation scripts
├── templates/ # Reusable templates
├── docs/ # Detailed guides and notes
├── create_lab_structure.py # Lab setup
├── spin_incidents.py # Deploy incidents
└── terminate_all_aws.ps1 # Cleanup script

yaml
Copy code

---

## 🎬 Incident Scenarios

| Incident ID | Summary | Status |
|-------------|---------|--------|
| 001-ec2-ssh-lockout | EC2 instance unreachable via SSH | ✅ Complete |
| 002-s3-public-bucket | Misconfigured S3 bucket blocking access | ⚠️ In Progress |
| 003-lambda-timeout | Lambda function runtime errors | ⚠️ In Progress |
| 004-vpc-dns-failure | Custom DNS failure incident | 🛠 Placeholder |

---

## 🖼️ Evidence & Screenshots

<details>
<summary>Incident 001: EC2 SSH Lockout Screenshots</summary>

- ![Instances Info](./incidents/001-ec2-ssh-lockout/evidence/screenshots/01_instances_info.png)  
- ![Security Group Rules](./incidents/001-ec2-ssh-lockout/evidence/screenshots/02_security_group_rules.png)  
- ![VPC Creation](./incidents/001-ec2-ssh-lockout/evidence/screenshots/03_vpc_creation.png)  
- ![Subnets](./incidents/001-ec2-ssh-lockout/evidence/screenshots/04_subnets.png)  
- ![Route Tables](./incidents/001-ec2-ssh-lockout/evidence/screenshots/05_route_tables.png)  
- ![Storage Gateway Connect](./incidents/001-ec2-ssh-lockout/evidence/screenshots/12_storage_gateway_connect.png)  

</details>

<details>
<summary>Other incidents screenshots</summary>
*(Add collapsible sections for each additional incident folder similarly)*
</details>

---

## 📖 How to Use

1. Clone the repo:

```bash
git clone https://github.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab.git
cd AWS_Error_Driven_Troubleshooting_Lab
Set up AWS credentials:

bash
Copy code
aws configure
# Enter your AWS Access Key ID, Secret Key, and default region
Create lab structure (first time only):

bash
Copy code
python create_lab_structure.py
Deploy an incident scenario:

bash
Copy code
python spin_incidents.py
⚠️ Warning: This creates live AWS resources. Charges may apply.

Troubleshoot the incident:

Navigate to the incident folder (e.g., incidents/001-ec2-ssh-lockout/)

Review README

Investigate with AWS Console and CLI

Run scripts/collect_evidence.py to gather logs and metrics

Document findings in incident README

Remediate the issue:

Apply fixes manually or via remediation scripts

Verify issue resolution

Document root cause and resolution steps

Clean up resources:

powershell
Copy code
.\terminate_all_aws.ps1   # Windows
bash
Copy code
cd incidents/001-ec2-ssh-lockout/scripts/
python teardown.py        # Linux/Mac
💡 Learning Outcomes
Diagnose AWS failures & misconfigurations ✅

Write automation scripts for remediation ✅

Implement monitoring & alerting best practices ✅

Understand fault tolerance & resilience ✅

Build professional incident documentation with evidence ✅

👤 Author
Charles Bucher – Cloud Support / DevOps Self-Taught
GitHub: @charles-bucher
Email: quietopscb@gmail.com
LinkedIn: charles-bucher-cloud

⚡ License
MIT License © Charles Bucher

⚠️ Disclaimer
This lab is for learning purposes only. Running scripts can create billable AWS resources. Always clean up resources after use.

