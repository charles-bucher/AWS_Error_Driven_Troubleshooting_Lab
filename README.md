# AWS Error-Driven Troubleshooting Lab

**TL;DR:** Hands-on portfolio for entry-level Cloud Support Engineers, demonstrating EC2, S3, Lambda, VPC, CloudWatch, IAM troubleshooting with full RCA documentation, evidence collection, and metrics tracking.

## Quick Start
...


Clone the repo:

git clone https://github.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab.git
cd AWS_Error_Driven_Troubleshooting_Lab


Install Python dependencies:

pip install -r requirements.txt


Configure AWS CLI:

aws configure


Run your first incident:

cd incidents/001-ec2-ssh-lockout/scripts
python deploy.py
python break.py
python collect_evidence.py
python teardown.py


All labs are Free Tier compatible and tested on Python 3.14+.

Installation

Follow the Quick Start above. Make sure Python 3.14+ and AWS CLI are installed.

Usage

Validate README:

python validate_readme.py "README.md"


Run individual incidents:

cd incidents/<incident-id>/scripts
python deploy.py
python break.py
python collect_evidence.py
python teardown.py

Incident Scenarios
ID	Incident	Services	Difficulty	Status	Resolution Time
001	EC2 SSH Lockout	EC2, VPC, Security Groups	🟢 Entry	✅ Complete	~15 min
002	S3 Public Bucket	S3, IAM	🟢 Entry	⚠️ In Progress	TBD
003	Lambda Timeout	Lambda, VPC, CloudWatch	🟡 Intermediate	⚠️ In Progress	TBD
004	Lambda Cold Start	Lambda, VPC, CloudWatch	🟡 Intermediate	🛠 Planned	TBD
Evidence

Each incident contains:

screenshots/ – Step-by-step images from error → investigation → resolution

logs/ – CloudWatch logs, system logs

metrics/ – Performance metrics, response times

Metrics

Tracked KPIs per incident:

MTTD – Mean Time To Detect

MTTI – Mean Time To Investigate

MTTR – Mean Time To Resolve

Cost per Incident

Documentation Time

Skills Mapped

Technical Skills: EC2, S3, Lambda, VPC, CloudWatch, IAM, network troubleshooting, cost optimization, root cause analysis
Professional Skills: Incident response, RCA documentation, time-to-resolution metrics, post-incident review
Automation & DevOps: Python (Boto3), Bash, PowerShell, Infrastructure-as-Code, CI/CD concepts

License

This project is licensed under the MIT License. See LICENSE
.

Keywords

EC2, S3, Lambda, VPC, CloudWatch, IAM, troubleshoot, root cause

References

AWS Documentation

Python Boto3

AWS Free Tier

