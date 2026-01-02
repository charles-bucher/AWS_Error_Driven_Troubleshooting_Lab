# AWS Triage Playbook

## Purpose
This playbook provides step-by-step guidance for triaging AWS incidents, identifying root causes, and applying immediate remediation.

---

## 1. Initial Assessment
1. **Identify the affected service** (EC2, S3, Lambda, DynamoDB, etc.)
2. **Check monitoring dashboards**
   - CloudWatch metrics
   - CloudTrail logs
   - Trusted Advisor alerts
3. **Determine impact**
   - Number of affected resources
   - Business-critical impact
4. **Set severity level**
   - Sev 1: Critical outage
   - Sev 2: Major degradation
   - Sev 3: Minor impact

---

## 2. Evidence Collection
- Gather logs from:
  - CloudWatch
  - Application logs
  - Security groups / IAM changes
- Record timestamps of error occurrence
- Note any recent deployments or changes

---

## 3. Containment
- Stop further damage:
  - Isolate affected resources
  - Apply temporary configuration rollback if safe
  - Disable suspicious IAM changes
- Notify relevant teams and stakeholders

---

## 4. Investigation & Root Cause Analysis
1. Check configuration drift:
   - VPC settings, security groups, subnets
2. Validate permissions:
   - IAM policies, S3 bucket policies
3. Review service-specific logs:
   - Lambda logs, EC2 system logs, RDS logs
4. Correlate changes with errors
   - Recent deploys
   - Scheduled jobs or scripts

---

## 5. Remediation
- Apply fixes in a controlled environment first
- Test impact on non-production resources
- Implement fix in production after validation
- Document steps taken

---

## 6. Post-Incident
- Conduct retrospective / root cause review
- Update playbook with lessons learned
- Automate guardrails to prevent recurrence

---

## 7. Useful Commands & References

### EC2
```bash
aws ec2 describe-instances
aws ec2 describe-security-groups
aws s3 ls
aws s3 ls
aws s3api get-bucket-policy --bucket <bucket-name>
## Overview
This project demonstrates practical Cloud Support & CloudOps skills by working with AWS services such as VPC, DynamoDB, CloudTrail, RDS, IAM, EC2, CloudWatch, S3, Lambda.

## Skills Demonstrated
Automation, monitoring, incident response, troubleshooting, and Infrastructure as Code using Terraform/CloudFormation.

## Usage
Clone the repo and follow the scripts or Terraform configurations to deploy and test resources. Designed to simulate realistic AWS cloud incidents.

## What I Learned
Hands-on experience troubleshooting AWS incidents, applying automation, monitoring with CloudWatch, and ensuring cloud reliability.
