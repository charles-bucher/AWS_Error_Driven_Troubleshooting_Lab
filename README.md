 AWS Error-Driven Troubleshooting Lab

![Python](https://img.shields.io/badge/python-3.14+-blue)
![Boto3](https://img.shields.io/badge/boto3-installed-brightgreen)

## Overview
This repository is a hands-on **AWS Error-Driven Troubleshooting Lab**.  
It simulates real-world AWS incidents so you can **diagnose, remediate, and document failures safely**.  

⚠️ **Warning:** These labs are intentionally destructive. Resources will be created, broken, and torn down. **AWS charges may apply** if resources are left running.

---

## Incident Scenarios

| Incident ID | Summary | Status |
|------------|---------|-------|
| `incident_001_ec2_unreachable` | EC2 instance cannot be reached over SSH | ✅ Complete |
| `incident_002_s3_permission` | Misconfigured S3 bucket policy blocking access | ⚠️ In Progress |
| `incident_003_lambda_failure` | Lambda function throwing runtime errors | ⚠️ In Progress |
| `incident_004_custom` | Custom incident for testing your own failures | 🛠 Placeholder |

---

## Lab Structure

AWS_Error_Driven_Troubleshooting_Lab/
├─ incidents/
│ ├─ incident_001_ec2_unreachable/
│ │ ├─ scripts/ # deploy, break, collect_evidence, teardown
│ │ ├─ evidence/
│ │ │ └─ screenshots/ # visual proof
│ │ └─ README.md # incident summary
├─ docs/
├─ templates/
├─ scripts/
├─ config/
└─ create_lab_structure.py

yaml
Copy code

**Notes:**
- Scripts: `deploy.py`, `break.py`, `collect_evidence.py`, `teardown.py`.  
- Evidence folder: logs, CloudWatch exports, screenshots.  
- README per incident: summarize problem, triage, root cause, resolution, lessons learned.

---

## How to Run

1. **Clone the repo**
```bash
git clone https://github.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab.git
cd AWS_Error_Driven_Troubleshooting_Lab
Create lab structure

bash
Copy code
python create_lab_structure.py
Spin up incidents

bash
Copy code
python spin_incidents.py
⚠️ Caution: This creates live AWS resources. Charges may apply.

Tear down all resources

powershell
Copy code
# PowerShell
.\terminate_all_aws.ps1
Evidence Tracking
Use screenshots and logs as proof of work.
Example badges:





Screenshots naming convention:

python-repl
Copy code
screenshot_001_instances_info.png
screenshot_002_security_groups.png
screenshot_003_vpc_creation.png
...
Reference them in README for visual proof:

markdown
Copy code
![EC2 Instance Info](incidents/incident_001_ec2_unreachable/evidence/screenshots/screenshot_001_instances_info.png)
Lessons Learned
AWS breaks in unpredictable ways; hands-on practice accelerates learning.

Always tear down resources to avoid unexpected bills.

IAM & permissions mistakes are your first lesson.

Documentation + screenshots matter—they are proof of skill, not decoration.

Requirements
Python 3.14+

boto3 (install via pip install boto3)

AWS CLI configured

PowerShell (for teardown scripts)

Basic AWS knowledge: EC2, VPC, Subnets, IGW, SG, S3, Lambda

Contributing
Keep incidents consistent in structure.

Include README.md and evidence/screenshots.

Never commit AWS credentials or private keys.

Author
Charles Bucher – Cloud Support / DevOps self-taught – GitHub

Disclaimer
This lab is for learning only. Running scripts can create billable AWS resources. Always clean up.

About
Intentionally broken AWS scenarios for hands-on troubleshooting using real cloud support workflows. Focus on logs, metrics, root cause analysis, remediation, and prevention, not tutorials.

Topics
aws cloud aws-lambda aws-s3 aws-ec2 aws-dynamodb aws-cloud cloud-support aws-automation cloud-ops error-driven-learning
---

