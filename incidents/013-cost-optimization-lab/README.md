# 013 - Cost Optimization Lab

**Category:** Entry-Level Cloud Lab  
**Skills Demonstrated:** AWS cost analysis, right-sizing resources, monitoring, reporting, automation  
**Project Type:** Hands-on cloud support simulation

---

## Overview

This lab demonstrates **analyzing AWS resource usage and implementing cost optimization strategies**.  
You will practice **identifying idle or underutilized resources, generating reports, and applying best practices to reduce costs**.

**Key Objectives:**  
- Analyze EC2, S3, and other AWS service usage  
- Identify idle or underutilized resources  
- Implement right-sizing recommendations  
- Automate cost reporting and tracking  

---

## Lab Scenario

- Your AWS environment has multiple resources running, some of which are underutilized or idle.  
- Requirements:  
  - Detect idle EC2 instances and unattached EBS volumes  
  - Identify stale snapshots and unused S3 objects  
  - Generate automated cost reports  
  - Implement recommendations to reduce monthly costs  

---

## Steps to Reproduce

1. **Setup Environment**  
   - Access your AWS account and review EC2, EBS, and S3 resources  
   - Ensure IAM permissions allow cost explorer and resource inspection  

2. **Analyze Resource Usage**  
   - Use AWS Cost Explorer or CLI to identify idle resources:  
     ```bash
     aws ce get-cost-and-usage --time-period Start=2025-12-01,End=2025-12-31 --granularity MONTHLY --metrics "BlendedCost"
     ```  
   - List unattached EBS volumes:  
     ```bash
     aws ec2 describe-volumes --filters Name=status,Values=available
     ```  
   - Check for unused S3 objects and old snapshots  

3. **Implement Optimization Recommendations**  
   - Terminate or stop idle EC2 instances  
   - Delete unattached EBS volumes and old snapshots  
   - Apply S3 lifecycle policies for infrequent-access or archival  

4. **Automate Reporting**  
   - Generate automated cost reports via Python or PowerShell scripts  
   - Track savings over time  

---

## Validation

- Idle or underutilized resources are identified and remediated  
- Monthly cost reports reflect reduction opportunities  
- Alerts or dashboards monitor ongoing costs  

---

## Folder Structure

013-cost-optimization-lab/
├─ screenshots/ # Screenshots of cost reports, dashboards, and recommendations
├─ logs/ # Cost Explorer logs or automation outputs
├─ scripts/ # Python/PowerShell scripts for reporting and optimization
└─ README.md # This file

yaml
Copy code

---

## Tech Stack

- AWS Cost Explorer  
- EC2, EBS, S3  
- CloudWatch (optional monitoring)  
- Python / PowerShell automation  
- IAM Roles & Policies  

---

## Skills Gained

✅ Analyzing AWS resource utilization  
✅ Identifying and remediating idle or underutilized resources  
✅ Implementing cost-saving strategies (right-sizing, lifecycle policies)  
✅ Automating cost monitoring and reporting

## What I Learned
Hands-on experience troubleshooting AWS incidents, applying automation, monitoring with CloudWatch, and ensuring cloud reliability.
