 010 - VPC Network Troubleshooting Lab

**Category:** Entry-Level Cloud Lab  
**Skills Demonstrated:** VPC, subnets, route tables, NACLs, network misconfigurations, troubleshooting  
**Project Type:** Hands-on cloud support simulation

---

## Overview

This lab simulates **network connectivity issues within an AWS VPC**.  
You will practice **diagnosing subnet, routing, and network ACL issues**, applying real-world troubleshooting skills.

**Key Objectives:**  
- Identify and resolve VPC network misconfigurations  
- Troubleshoot subnet and route table issues  
- Analyze NACLs and security group conflicts  
- Validate connectivity and remediation steps  

---

## Lab Scenario

- Instances in a VPC cannot communicate with each other or the internet.  
- Potential causes:  
  - Misconfigured subnets or route tables  
  - Incorrect NACLs or security group rules  
  - Overlapping CIDR blocks  
  - Missing Internet Gateway attachment  

---

## Steps to Reproduce

1. **Setup Environment**  
   - Create a VPC with multiple subnets  
   - Launch EC2 instances in each subnet  
   - Assign security groups and NACLs  

2. **Simulate Network Issues**  
   - Remove routes in the route table  
   - Block traffic with NACL rules  
   - Misconfigure security group rules  

3. **Troubleshooting Workflow**  
   - **Step 1:** Verify VPC and subnet configurations  
     ```bash
     aws ec2 describe-vpcs
     aws ec2 describe-subnets
     ```  
   - **Step 2:** Check route tables and gateways  
     ```bash
     aws ec2 describe-route-tables
     ```  
   - **Step 3:** Inspect NACL and security group rules  
     ```bash
     aws ec2 describe-network-acls
     aws ec2 describe-security-groups
     ```  
   - **Step 4:** Test connectivity using ping, traceroute, or VPC reachability analyzer  

4. **Remediation**  
   - Correct subnet routes and associate route tables  
   - Update NACLs and security group rules  
   - Verify connectivity between instances and to the internet  

---

## Validation

- Instances communicate correctly within the VPC  
- Traffic flows as intended through subnets and routes  
- Security group and NACL rules allow expected connections without exposing unnecessary access  

---

## Folder Structure

010-vpc-network-troubleshoot/
├─ screenshots/ # Screenshots of route tables, NACLs, and security groups
├─ logs/ # VPC flow logs or diagnostic output
├─ scripts/ # Optional automation scripts
└─ README.md # This file

yaml
Copy code

---

## Tech Stack

- AWS VPC, Subnets, Route Tables, Internet Gateway  
- Security Groups & NACLs  
- EC2 Instances for testing  
- VPC Flow Logs  
- Python / Bash (optional automation)  

---

## Skills Gained

✅ Diagnosing VPC connectivity issues  
✅ Troubleshooting route tables, subnets, and NACLs  
✅ Verifying network configurations with logs and reachability tools  
✅ Implementing secure and functional network setups in AWS

## Usage
Clone the repo and follow the scripts or Terraform configurations to deploy and test resources. Designed to simulate realistic AWS cloud incidents.

## What I Learned
Hands-on experience troubleshooting AWS incidents, applying automation, monitoring with CloudWatch, and ensuring cloud reliability.
