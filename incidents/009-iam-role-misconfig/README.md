# 009 - IAM Role Misconfiguration Lab

**Category:** Entry-Level Cloud Lab  
**Skills Demonstrated:** IAM permissions troubleshooting, role policies, least-privilege access, CloudWatch logs  
**Project Type:** Hands-on cloud support simulation

---

## Overview

This lab simulates **misconfigured IAM roles and permissions** in AWS.  
You will practice **identifying, diagnosing, and resolving access issues** to enforce proper least-privilege security practices.

**Key Objectives:**  
- Detect and troubleshoot IAM role misconfigurations  
- Analyze permissions using policy simulation tools  
- Correct role policies to grant proper access  
- Verify changes with real-world scenarios  

---

## Lab Scenario

- A user or application cannot access an AWS service (e.g., S3, EC2, or RDS).  
- Potential causes:  
  - Missing IAM policies  
  - Incorrect role attachments  
  - Overly restrictive or conflicting policies  

---

## Steps to Reproduce

1. **Setup Environment**  
   - Create IAM users, groups, and roles  
   - Attach policies with intentional misconfigurations  
   - Assign roles to EC2 or Lambda services  

2. **Simulate Access Issue**  
   - Attempt access to restricted resources  
   - Observe permission denied errors  

3. **Troubleshooting Workflow**  
   - **Step 1:** Use IAM Policy Simulator  
     ```bash
     aws iam simulate-principal-policy --policy-source-arn arn:aws:iam::123456789012:user/CloudUser --action-names s3:ListBucket
     ```  
   - **Step 2:** Review attached policies and role permissions  
   - **Step 3:** Update policies to grant minimum required access  
     ```bash
     aws iam attach-user-policy --user-name CloudUser --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
     ```  
   - **Step 4:** Test access again to confirm fix  

---

## Validation

- User or service can access only the intended resources  
- No excessive permissions granted  
- CloudWatch logs show successful access after remediation  

---

## Folder Structure

009-iam-role-misconfig/
├─ screenshots/ # Screenshots of IAM policies and test results
├─ logs/ # CloudTrail or CloudWatch logs
├─ scripts/ # Optional automation scripts for policy fixes
└─ README.md # This file

yaml
Copy code

---

## Tech Stack

- AWS IAM Roles, Users, Groups, Policies  
- CloudTrail for access auditing  
- CloudWatch Logs  
- Python / Bash (optional automation)  

---

## Skills Gained

✅ Diagnosing IAM role misconfigurations  
✅ Applying least-privilege access principles  
✅ Using IAM Policy Simulator for troubleshooting  
✅ Validating permissions with CloudWatch and real-world tests
## Usage
Clone the repo and follow the scripts or Terraform configurations to deploy and test resources. Designed to simulate realistic AWS cloud incidents.

## What I Learned
Hands-on experience troubleshooting AWS incidents, applying automation, monitoring with CloudWatch, and ensuring cloud reliability.
