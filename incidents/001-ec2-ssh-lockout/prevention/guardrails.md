# GUARDRAILS.md

## Purpose
This document defines the guardrails for running **AWS_Error_Driven_Troubleshooting_Lab**.  
The goal is to intentionally break cloud resources for learning, while keeping costs low, environments safe, and cleanup automatic.

---

## Cost Guardrails
- **Instance Types:** Use only `t3.micro` or smaller for EC2 labs.
- **Run Time:** Destroy all resources immediately after testing. Never leave labs running overnight.
- **Tagging:** Every resource must include tags:
  - `Name = IncidentLab`
  - `Owner = YourName`
  - `Purpose = BreakTest`
- **Automation:** Run `scripts/cost_guardrails.py` daily to stop idle instances and prevent runaway costs.

---

## Security Guardrails
- **IAM:** Use least-privilege roles. Never test with admin/root credentials.
- **S3:** Public access is allowed only when intentionally breaking. Always remediate with block-public-access scripts.
- **Keys:** Never commit AWS access keys or secrets to GitHub. Use environment variables or AWS CLI profiles.
- **Isolation:** Labs run in a dedicated VPC. Do not use production accounts.

---

## Operational Guardrails
- **Logging:** Every incident must produce an audit log (`scripts/audit_log.py`) with timestamps and actions.
- **Screenshots:** Save console errors, CloudWatch alarms, and fixes in `/screenshots/` for recruiter visibility.
- **Documentation:** Each incident folder must include `incident.md` with:
  - Symptoms
  - Root Cause
  - Remediation
  - Prevention
- **CI/CD:** Terraform code must pass `terraform validate` via GitHub Actions before deployment.

---

## Cleanup Guardrails
- **Terraform Destroy:** Always run `terraform destroy` after each incident.
- **Scripts:** Include cleanup scripts (`cleanup.sh` or `cleanup.ps1`) in each incident folder.
- **Verification:** Confirm no active resources remain with `aws resourcegroupstaggingapi get-resources`.

---

## Learning Guardrails
- **Break Intentionally:** Only break resources defined in the lab. Never disrupt shared or production environments.
- **Document Everything:** Treat each incident like a case study. Recruiters want to see your troubleshooting process.
- **Iterate:** Update incidents with lessons learned, screenshots, and improved guardrails.

---

## License
This repo uses the MIT License. All labs are for **educational purposes only**.