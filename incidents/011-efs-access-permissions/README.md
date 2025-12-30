# 011 - EFS Access Permissions Lab

**Category:** Entry-Level Cloud Lab  
**Skills Demonstrated:** EFS mounting, access permissions, security groups, NFS troubleshooting  
**Project Type:** Hands-on cloud support simulation

---

## Overview

This lab simulates **Amazon EFS access and mounting issues**.  
You will practice **troubleshooting permissions, security groups, and network connectivity** to ensure proper access to file systems.

**Key Objectives:**  
- Mount EFS file systems on EC2 instances  
- Identify and resolve permission and access issues  
- Analyze security group and NACL rules affecting NFS traffic  
- Validate access from multiple clients  

---

## Lab Scenario

- EC2 instances cannot mount or access an EFS file system.  
- Potential causes:  
  - Incorrect NFS permissions  
  - Security group or network ACL blocking NFS ports  
  - IAM role misconfigurations (if using access points)  
  - Mount target issues  

---

## Steps to Reproduce

1. **Setup Environment**  
   - Create an EFS file system with mount targets  
   - Launch EC2 instances in the same VPC  
   - Configure security groups and IAM roles  

2. **Simulate Access Issue**  
   - Remove NFS access from security group  
   - Set incorrect POSIX permissions on EFS  

3. **Troubleshooting Workflow**  
   - **Step 1:** Check mount command and error messages  
     ```bash
     sudo mount -t nfs4 -o nfsvers=4.1 fs-xxxxxxxx.efs.region.amazonaws.com:/ /mnt/efs
     ```  
   - **Step 2:** Inspect EC2 and EFS security groups  
     ```bash
     aws ec2 describe-security-groups --group-ids sg-xxxxxxxx
     ```  
   - **Step 3:** Verify POSIX permissions  
     ```bash
     ls -ld /mnt/efs
     ```  
   - **Step 4:** Check mount targets and network connectivity  
     ```bash
     ping fs-xxxxxxxx.efs.region.amazonaws.com
     ```  

4. **Remediation**  
   - Update security group rules to allow NFS (port 2049)  
   - Correct POSIX ownership and permissions  
   - Remount the EFS file system and verify access  

---

## Validation

- EC2 instances can successfully mount the EFS file system  
- Users can read/write files according to intended permissions  
- Security groups allow only necessary NFS traffic  

---

## Folder Structure

011-efs-access-permissions/
├─ screenshots/ # Screenshots of mount attempts, security groups, and permissions
├─ logs/ # Mount logs or diagnostic output
├─ scripts/ # Optional automation scripts
└─ README.md # This file

yaml
Copy code

---

## Tech Stack

- AWS EFS  
- EC2 Instances  
- Security Groups & NACLs  
- POSIX Permissions  
- IAM Roles (if using EFS Access Points)  
- Python / Bash (optional automation)  

---

## Skills Gained

✅ Troubleshooting EFS mount and access issues  
✅ Configuring security groups for NFS access  
✅ Managing POSIX file system permissions  
✅ Validating secure and functional file system access in AWS
