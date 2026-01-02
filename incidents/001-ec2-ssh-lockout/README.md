🔐 EC2 SSH Lockout – Troubleshooting Lab
Overview

This lab simulates a common real-world AWS Cloud Support incident: loss of SSH access to an EC2 instance.
The goal is to diagnose, isolate, and remediate the issue using AWS-native tools and safe automation practices.

This scenario mirrors tickets frequently seen in Cloud Support, CloudOps, and SRE environments.

🎯 Scenario

A Linux EC2 instance becomes unreachable via SSH.
Possible causes include:

Incorrect security group rules

NACL misconfiguration

Broken SSH daemon

Corrupted authorized_keys

Disk full or filesystem errors

Accidental firewall changes

Access must be restored without destroying the instance.

🛠 Skills Demonstrated

EC2 troubleshooting under access loss

AWS Security Group & NACL analysis

Instance recovery using:

Stop/start lifecycle

Root volume detachment

Offline repair via helper instance

Safe scripting & validation practices

Writing testable, defensive cloud tooling

📂 Repository Structure
001-ec2-ssh-lockout/
├── README.md
├── scripts/
│   ├── check_ssh_config.py
│   ├── validate_security_groups.py
│   └── recover_authorized_keys.py
├── tests/
│   ├── test_security_groups.py
│   └── test_ssh_config.py
├── conftest_safe.py
└── notes/
    └── incident_analysis.md

🧪 Testing & Safety

Uses pytest for validation

conftest_safe.py prevents:

Destructive AWS calls

Accidental production access

Scripts are designed to be read-only by default

This mirrors real enterprise guardrails.

🚑 Recovery Workflow (High Level)

Confirm instance state and reachability

Verify security group and NACL rules

Attempt safe SSH config validation

Detach root volume if needed

Repair filesystem / SSH keys offline

Reattach and validate access

📌 Why This Lab Matters

SSH lockouts are:

One of the top EC2 support tickets

A strong signal of cloud troubleshooting maturity

A gateway skill for CloudOps and DevOps roles

This lab emphasizes diagnosis over brute force rebuilds.

🧠 Key Takeaways

Cloud failures are often configuration mistakes, not infrastructure failures

Safe automation beats panic actions

Recovery skills are more valuable than deployment skills early on

🚀 Next Improvements (Planned)

SSM Session Manager recovery path

CloudWatch log-based diagnostics

Automated NACL diffing

Incident-style runbook formatting
## Usage
Clone the repo and follow the scripts or Terraform configurations to deploy and test resources. Designed to simulate realistic AWS cloud incidents.

## What I Learned
Hands-on experience troubleshooting AWS incidents, applying automation, monitoring with CloudWatch, and ensuring cloud reliability.
