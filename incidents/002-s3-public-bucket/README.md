🔓 S3 Public Bucket Exposure – Security Troubleshooting Lab
Overview

This lab simulates a high-risk AWS security incident: an S3 bucket is accidentally exposed to the public.
The objective is to identify how access was granted, assess risk, and lock the bucket down safely without breaking legitimate access.

This mirrors real Cloud Support and Security Operations tickets.

🎯 Scenario

An S3 bucket containing internal data is discovered to be publicly accessible.

Potential causes include:

Misconfigured bucket policy

Public ACLs on objects

Disabled S3 Block Public Access

Over-permissive IAM roles

Third-party tooling misconfiguration

The bucket must be secured without deleting data.

🛠 Skills Demonstrated

S3 permission model analysis (ACLs vs policies)

Block Public Access configuration

IAM principle of least privilege

Public exposure detection

Safe remediation and validation

Writing non-destructive security scripts

📂 Repository Structure
002-s3-public-bucket/
├── README.md
├── scripts/
│   ├── detect_public_access.py
│   ├── analyze_bucket_policy.py
│   ├── disable_public_access.py
│   └── validate_bucket_security.py
├── tests/
│   ├── test_bucket_policy.py
│   └── test_public_access.py
├── conftest_safe.py
└── notes/
    └── security_incident_review.md

🧪 Testing & Safety

Uses pytest for script validation

conftest_safe.py blocks:

Bucket deletion

Policy overwrite without confirmation

Account-wide permission changes

Scripts default to audit-only mode

Designed to reflect real enterprise guardrails.

🚨 Incident Response Workflow

Identify public exposure vector

Verify bucket ACLs and object ACLs

Inspect bucket policy statements

Review Block Public Access settings

Apply least-privilege remediation

Validate access is restricted

Document root cause

📌 Why This Lab Matters

Public S3 buckets are:

One of the most common AWS security misconfigurations

A frequent cause of data exposure incidents

A core responsibility for Cloud Support and Cloud Security roles

This lab emphasizes safe containment over panic remediation.

🧠 Key Takeaways

Public access is usually accidental, not malicious

S3 permissions are layered and easy to misunderstand

Fixing exposure requires precision, not blanket lockdowns

🚀 Next Improvements (Planned)

CloudTrail-based exposure detection

AWS Config rule simulation

Cross-account access analysis

Incident timeline reconstruction
## Usage
Clone the repo and follow the scripts or Terraform configurations to deploy and test resources. Designed to simulate realistic AWS cloud incidents.

## What I Learned
Hands-on experience troubleshooting AWS incidents, applying automation, monitoring with CloudWatch, and ensuring cloud reliability.
