# 012 - CloudTrail Audit Lab

**Category:** Entry-Level Cloud Lab  
**Skills Demonstrated:** CloudTrail monitoring, unauthorized access simulation, auditing, remediation  
**Project Type:** Hands-on cloud support simulation

---

## Overview

This lab simulates **unauthorized access events and auditing using AWS CloudTrail**.  
You will practice **detecting, analyzing, and remediating security incidents** while gaining hands-on experience with AWS logging and monitoring.

**Key Objectives:**  
- Monitor AWS account activity with CloudTrail  
- Detect unauthorized access or misconfigurations  
- Analyze logs to determine root cause  
- Apply remediation steps to prevent recurrence  

---

## Lab Scenario

- An IAM user attempts actions they are not authorized for, or suspicious API calls occur.  
- Potential causes:  
  - Misconfigured IAM policies  
  - Compromised credentials  
  - Unauthorized API calls  

---

## Steps to Reproduce

1. **Setup Environment**  
   - Enable CloudTrail in your AWS account  
   - Configure S3 bucket to store logs  
   - Enable logging for all regions  

2. **Simulate Unauthorized Access**  
   - Attempt API actions with a user lacking permissions  
   - Trigger failed login attempts or unauthorized API calls  

3. **Troubleshooting Workflow**  
   - **Step 1:** Review CloudTrail logs  
     ```bash
     aws cloudtrail lookup-events --lookup-attributes AttributeKey=Username,AttributeValue=TestUser
     ```  
   - **Step 2:** Identify suspicious events (failed API calls, unusual IP addresses)  
   - **Step 3:** Correlate events with IAM roles and policies  

4. **Remediation**  
   - Correct IAM policies and enforce least-privilege access  
   - Rotate credentials if compromised  
   - Enable CloudWatch alerts for suspicious activities  

---

## Validation

- Unauthorized access attempts are logged in CloudTrail  
- Remediation steps prevent repeat incidents  
- Alerts or notifications trigger on suspicious activity  

---

## Folder Structure

012-cloudtrail-audit/
├─ screenshots/ # Screenshots of CloudTrail console, events, and remediation steps
├─ logs/ # CloudTrail logs or exported events
├─ scripts/ # Optional automation scripts for analysis
└─ README.md # This file

yaml
Copy code

---

## Tech Stack

- AWS CloudTrail  
- S3 for log storage  
- CloudWatch Logs and Metrics  
- IAM Roles & Policies  
- Python / Bash (optional automation)  

---

## Skills Gained

✅ Monitoring AWS account activity using CloudTrail  
✅ Detecting unauthorized access and misconfigurations  
✅ Analyzing logs to identify root causes  
✅ Applying remediation and preventive security measures

## Usage
Clone the repo and follow the scripts or Terraform configurations to deploy and test resources. Designed to simulate realistic AWS cloud incidents.

## What I Learned
Hands-on experience troubleshooting AWS incidents, applying automation, monitoring with CloudWatch, and ensuring cloud reliability.
