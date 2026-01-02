# 005 - S3 Lifecycle Policy Lab

**Category:** Entry-Level Cloud Lab  
**Skills Demonstrated:** S3 lifecycle policies, object expiration, versioning, permissions  
**Project Type:** Hands-on cloud support simulation

---

## Overview

This lab demonstrates **managing S3 buckets with lifecycle policies**.  
You will practice **configuring, testing, and verifying object expiration, versioning, and permissions** in a real AWS environment.

**Key Objectives:**  
- Implement lifecycle rules for S3 buckets  
- Test object expiration and transition to storage classes  
- Enable and manage versioning  
- Analyze bucket policies and permissions  

---

## Lab Scenario

- You have an S3 bucket storing logs and backups.  
- Requirements:  
  - Automatically transition old objects to Glacier  
  - Delete expired objects after a set period  
  - Maintain versioning for backups  
  - Ensure proper IAM permissions  

---

## Steps to Reproduce

1. **Setup Environment**  
   - Create an S3 bucket  
   - Upload sample files and folders  
   - Enable versioning  

2. **Apply Lifecycle Policy**  
   - Create rules for:  
     - Transition to Glacier after X days  
     - Expire objects after Y days  
   - Apply rules via AWS Management Console or Terraform  

3. **Verify Rules**  
   - Check object storage class transitions  
   - Confirm expired objects are deleted  
   - Test versioning by uploading and deleting objects  

4. **Troubleshooting Workflow**  
   - **Step 1:** Inspect bucket lifecycle configuration  
     ```bash
     aws s3api get-bucket-lifecycle-configuration --bucket my-bucket
     ```  
   - **Step 2:** Verify IAM permissions  
     ```bash
     aws s3 ls s3://my-bucket
     ```  
   - **Step 3:** Monitor CloudWatch for lifecycle events (optional)  

---

## Validation

- Old objects are moved to Glacier or deleted according to policy  
- Versioned objects are preserved and accessible  
- Permissions prevent unauthorized access  

---

## Folder Structure

005-s3-lifecycle-policy/
├─ screenshots/ # Screenshots of lifecycle rules and outputs
├─ logs/ # Optional logs of bucket activity
├─ scripts/ # Optional automation scripts
└─ README.md # This file

yaml
Copy code

---

## Tech Stack

- AWS S3  
- IAM Policies & Roles  
- Lifecycle Management  
- CloudWatch Logs (optional)  
- Python / Bash (optional automation)  

---

## Skills Gained

✅ Implementing S3 lifecycle policies  
✅ Managing object expiration and storage classes  
✅ Configuring bucket versioning and permissions  
✅ Analyzing and troubleshooting S3 lifecycle behavior
## Usage
Clone the repo and follow the scripts or Terraform configurations to deploy and test resources. Designed to simulate realistic AWS cloud incidents.

## What I Learned
Hands-on experience troubleshooting AWS incidents, applying automation, monitoring with CloudWatch, and ensuring cloud reliability.
