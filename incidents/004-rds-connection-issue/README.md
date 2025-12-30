# 004 - RDS Connection Issue

**Category:** Entry-Level Cloud Lab  
**Skills Demonstrated:** RDS troubleshooting, IAM permissions, VPC security groups, logs & metrics analysis  
**Project Type:** Hands-on cloud support simulation

---

## Overview

This lab simulates a **broken Amazon RDS instance connectivity scenario**.  
You will practice **diagnosing, resolving, and documenting** real-world AWS cloud support issues.

**Key Objectives:**  
- Diagnose RDS connectivity failures  
- Investigate IAM permissions and security group misconfigurations  
- Analyze CloudWatch logs and VPC Flow Logs  
- Apply remediation and verify resolution

---

## Lab Scenario

- An application cannot connect to the RDS database.  
- Potential causes:  
  - Misconfigured VPC/subnets  
  - Incorrect security group inbound rules  
  - IAM role missing database access  
  - RDS parameter or network ACL issues

---

## Steps to Reproduce

1. **Setup Environment** (Terraform or manual)  
   - Launch an RDS instance in a VPC  
   - Configure subnets and security groups  
   - Assign IAM roles and database credentials  

2. **Simulate Issue**  
   - Block the security group inbound rule for the RDS port  
   - Remove IAM policy access temporarily  

3. **Troubleshooting Workflow**  
   - **Step 1:** Check RDS status and endpoints  
     ```bash
     aws rds describe-db-instances --db-instance-identifier my-db
     ```
   - **Step 2:** Verify security groups  
     ```bash
     aws ec2 describe-security-groups --group-ids sg-xxxxxxxx
     ```
   - **Step 3:** Check IAM permissions  
     ```bash
     aws iam simulate-principal-policy --policy-source-arn arn:aws:iam::123456789012:user/CloudUser --action-names rds:Connect
     ```
   - **Step 4:** Review logs  
     - CloudWatch logs for database connectivity errors  
     - VPC Flow Logs for blocked traffic  

4. **Remediation**  
   - Correct security group inbound rules  
   - Reassign IAM policy to allow RDS connection  
   - Verify connectivity using a client or CLI

---

## Validation

- RDS instance is reachable from the client  
- IAM user/role can connect successfully  
- Logs confirm no connection errors

---

## Folder Structure

004-rds-connection-issue/
├─ screenshots/ # Screenshots of issue & fix
├─ logs/ # CloudWatch or diagnostic logs
├─ scripts/ # Automation or remediation scripts
└─ README.md # This file

yaml
Copy code

---

## Tech Stack

- AWS RDS  
- VPC, Subnets, Security Groups  
- IAM & Roles  
- CloudWatch Logs, VPC Flow Logs  
- Python / Bash (optional automation)

---

## Skills Gained

✅ Troubleshooting connectivity issues  
✅ Analyzing IAM permissions and security group rules  
✅ Reading and interpreting CloudWatch logs  
✅ Applying remediations and verifying fixes
