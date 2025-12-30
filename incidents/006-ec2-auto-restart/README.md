# 006 - EC2 Auto-Restart Lab

**Category:** Entry-Level Cloud Lab  
**Skills Demonstrated:** EC2 instance failures, CloudWatch alarms, auto-recovery, troubleshooting  
**Project Type:** Hands-on cloud support simulation

---

## Overview

This lab simulates **EC2 instance failures and automatic recovery**.  
You will practice **setting up CloudWatch alarms, monitoring, and auto-recovery**, mimicking real-world cloud support scenarios.

**Key Objectives:**  
- Detect EC2 instance failures  
- Configure CloudWatch alarms and auto-recovery actions  
- Verify automatic instance restart  
- Analyze metrics and logs for troubleshooting  

---

## Lab Scenario

- An EC2 instance stops unexpectedly.  
- Requirements:  
  - Automatically detect the failure  
  - Trigger auto-recovery  
  - Ensure minimal downtime and service continuity  

---

## Steps to Reproduce

1. **Setup Environment**  
   - Launch an EC2 instance in a VPC  
   - Install sample applications if needed  
   - Configure IAM roles for monitoring  

2. **Simulate Failure**  
   - Stop or terminate the instance manually  
   - Observe how CloudWatch detects the failure  

3. **Configure CloudWatch Alarm & Auto-Recovery**  
   - Create a CloudWatch alarm on **StatusCheckFailed_System** metric  
   - Configure **Auto-Recovery** action  
   - Verify alarm triggers and instance is restarted automatically  

4. **Troubleshooting Workflow**  
   - **Step 1:** Check CloudWatch metrics  
     ```bash
     aws cloudwatch get-metric-statistics --metric-name StatusCheckFailed_System --namespace AWS/EC2 --dimensions Name=InstanceId,Value=i-xxxxxxxx
     ```  
   - **Step 2:** Inspect system logs for errors  
   - **Step 3:** Review alarm configuration and recovery actions  

---

## Validation

- EC2 instance automatically recovers after failure  
- CloudWatch alarm triggers correctly  
- Logs show proper system and recovery events  

---

## Folder Structure

006-ec2-auto-restart/
├─ screenshots/ # Screenshots of alarms and instance status
├─ logs/ # System or CloudWatch logs
├─ scripts/ # Optional automation scripts
└─ README.md # This file

yaml
Copy code

---

## Tech Stack

- AWS EC2  
- VPC, Security Groups  
- CloudWatch Alarms & Metrics  
- IAM Roles  
- Python / Bash (optional automation)  

---

## Skills Gained

✅ Detecting and troubleshooting EC2 failures  
✅ Configuring CloudWatch alarms and auto-recovery  
✅ Analyzing system and CloudWatch logs  
✅ Implementing automated recovery processes
