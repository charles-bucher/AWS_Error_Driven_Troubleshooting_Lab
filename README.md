 AWS_Error_Driven_Troubleshooting_Lab

[![Python](https://img.shields.io/badge/Python-3.14-blue)](https://www.python.org/)
[![Boto3](https://img.shields.io/badge/Boto3-AWS%20SDK-orange)](https://boto3.amazonaws.com/)
[![Lab Status](https://img.shields.io/badge/Lab-In%20Progress-yellow)](#)

---

## Overview

This repository is a **hands-on AWS Error-Driven Troubleshooting Lab**.  
It’s designed to simulate real-world AWS incidents so you can **diagnose, remediate, and document failures safely**.

⚠️ Warning: These labs are intentionally destructive. You **will** spin up resources, break them, and tear them down. AWS charges **can apply** if you leave resources running.

---

## Incident Scenarios

| Incident | Summary | Status |
|----------|--------|--------|
| `incident_001_ec2_unreachable` | EC2 instance cannot be reached over SSH | ✅ Complete |
| `incident_002_s3_permission` | Misconfigured S3 bucket policy blocking access | ⚠️ In Progress |
| `incident_003_lambda_failure` | Lambda function throwing runtime errors | ⚠️ In Progress |
| `incident_004_custom` | Custom incident for testing your own failures | 🛠 Placeholder |

---

## Lab Structure

AWS_Error_Driven_Troubleshooting_Lab/
├─ incidents/
│ ├─ incident_001_ec2_unreachable/
│ │ ├─ scripts/
│ │ │ ├─ deploy.py
│ │ │ ├─ break.py
│ │ │ ├─ collect_evidence.py
│ │ │ └─ teardown.py
│ │ ├─ evidence/
│ │ ├─ screenshots/
│ │ └─ README.md
├─ docs/
├─ templates/
├─ scripts/
├─ config/
└─ create_lab_structure.py

yaml
Copy code

- **Scripts**: deploy, break, collect evidence, teardown.  
- **Evidence folder**: logs, screenshots, CloudWatch exports.  
- **Screenshots**: visual proof of your work.  
- **README.md per incident**: summarize problem, triage, root cause, resolution, lessons learned.

---

## How to Run

1. Clone repo:

```bash
git clone https://github.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab.git
cd AWS_Error_Driven_Troubleshooting_Lab
Create lab structure:

bash
Copy code
python create_lab_structure.py
Spin up incidents:

bash
Copy code
python spin_incidents.py
⚠️ Caution: This will create live AWS resources. You may incur charges.

Tear down all resources:

powershell
Copy code
# PowerShell
.\terminate_all_aws.ps1
Evidence Tracking
Use screenshots and logs to prove your work.

Badge completion example:

less
Copy code
![Incident 1](https://img.shields.io/badge/incident_001-Complete-green)
![Incident 2](https://img.shields.io/badge/incident_002-InProgress-yellow)
![Incident 3](https://img.shields.io/badge/incident_003-InProgress-yellow)
Keep updating as you collect evidence for each incident.

Lessons Learned (Honest)
AWS breaks in unpredictable ways; you will learn fast.

Always tear down resources to avoid unexpected bills.

IAM & permissions mistakes are your first lesson—messing up can make everything fail.

Documentation + screenshots matter. This is proof of skill, not decoration.

Requirements
Python 3.14+

boto3 (pip install boto3)

AWS CLI configured

PowerShell (for teardown scripts)

Basic AWS knowledge: EC2, VPC, Subnets, IGW, SG, S3, Lambda

Contributing
Keep incidents consistent in structure.

Include README.md, evidence/screenshots.

Never commit AWS credentials or private keys.

Author
Charles Bucher – Cloud Support / DevOps self-taught – GitHub

Disclaimer: This lab is for learning only. Running scripts can create billable AWS resources. Always clean up.

