# 008 - CloudWatch Alerts Lab

**Category:** Entry-Level Cloud Lab  
**Skills Demonstrated:** CloudWatch alarms, monitoring metrics, troubleshooting, automated notifications  
**Project Type:** Hands-on cloud support simulation

---

## Overview

This lab simulates **monitoring AWS resources using CloudWatch alarms**.  
You will practice **creating, testing, and troubleshooting alarms for EC2, RDS, and custom metrics** to ensure proactive incident response.

**Key Objectives:**  
- Create CloudWatch alarms for system and application metrics  
- Trigger notifications on threshold breaches  
- Analyze metrics and logs to verify alarm behavior  
- Troubleshoot and fine-tune alerts  

---

## Lab Scenario

- You are responsible for monitoring cloud resources.  
- Requirements:  
  - Detect high CPU utilization on EC2 instances  
  - Trigger alarms for RDS performance issues  
  - Create custom metrics for application health  
  - Receive notifications via SNS  

---

## Steps to Reproduce

1. **Setup Environment**  
   - Launch EC2 instances or RDS databases  
   - Install sample applications if needed  
   - Ensure IAM permissions allow CloudWatch monitoring  

2. **Create CloudWatch Alarms**  
   - **EC2 CPU Alarm:**  
     ```bash
     aws cloudwatch put-metric-alarm --alarm-name HighCPUAlarm --metric-name CPUUtilization --namespace AWS/EC2 --statistic Average --period 300 --threshold 70 --comparison-operator GreaterThanThreshold --dimensions Name=InstanceId,Value=i-xxxxxxxx --evaluation-periods 2 --alarm-actions arn:aws:sns:region:account-id:my-topic
     ```  
   - **Custom Metric Alarm:** Track application-specific metrics using the PutMetricData API  

3. **Test Alarm Triggers**  
   - Generate load on EC2 or RDS to exceed thresholds  
   - Confirm notifications via SNS  
   - Review CloudWatch logs and metrics  

4. **Troubleshooting Workflow**  
   - Check alarm state:  
     ```bash
     aws cloudwatch describe-alarms --alarm-names HighCPUAlarm
     ```  
   - Verify metrics and thresholds  
   - Adjust period, evaluation, or thresholds if needed  

---

## Validation

- Alarms trigger correctly when thresholds are breached  
- Notifications are received via SNS  
- Metrics and logs confirm correct monitoring  

---

## Folder Structure

008-cloudwatch-alerts/
├─ screenshots/ # Screenshots of alarms, notifications, and CloudWatch console
├─ logs/ # CloudWatch logs or metric data
├─ scripts/ # Optional automation scripts for alarm setup
└─ README.md # This file

yaml
Copy code

---

## Tech Stack

- AWS CloudWatch  
- EC2, RDS  
- SNS for notifications  
- IAM for permissions  
- Python / Bash (optional automation)  

---

## Skills Gained

✅ Creating and configuring CloudWatch alarms  
✅ Monitoring AWS resources and custom metrics  
✅ Troubleshooting alarm misconfigurations  
✅ Ensuring proactive incident detection and response

## Usage
Clone the repo and follow the scripts or Terraform configurations to deploy and test resources. Designed to simulate realistic AWS cloud incidents.

## What I Learned
Hands-on experience troubleshooting AWS incidents, applying automation, monitoring with CloudWatch, and ensuring cloud reliability.
