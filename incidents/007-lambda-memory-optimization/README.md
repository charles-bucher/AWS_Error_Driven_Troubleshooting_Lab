# 007 - Lambda Memory Optimization Lab

**Category:** Entry-Level Cloud Lab  
**Skills Demonstrated:** AWS Lambda troubleshooting, memory/timeouts, CloudWatch logs, performance tuning  
**Project Type:** Hands-on cloud support simulation

---

## Overview

This lab simulates **AWS Lambda function memory and timeout issues**.  
You will practice **diagnosing performance problems, adjusting memory settings, and analyzing logs** to optimize function execution.

**Key Objectives:**  
- Diagnose Lambda timeouts or performance bottlenecks  
- Adjust memory and timeout configuration  
- Analyze CloudWatch logs for root cause  
- Validate optimized function performance  

---

## Lab Scenario

- A Lambda function is failing due to timeouts or excessive memory consumption.  
- Potential causes:  
  - Insufficient memory allocation  
  - Inefficient code or resource-intensive tasks  
  - Timeout configuration too low  
  - External service delays  

---

## Steps to Reproduce

1. **Setup Environment**  
   - Deploy a Lambda function (Python/Node.js)  
   - Configure IAM role with necessary permissions  
   - Trigger function with sample events  

2. **Simulate Performance Issue**  
   - Configure memory too low or timeout too short  
   - Run function repeatedly to observe failures  

3. **Troubleshooting Workflow**  
   - **Step 1:** Check CloudWatch logs  
     ```bash
     aws logs tail /aws/lambda/my-function --follow
     ```  
   - **Step 2:** Analyze metrics  
     ```bash
     aws cloudwatch get-metric-statistics --metric-name Duration --namespace AWS/Lambda --dimensions Name=FunctionName,Value=my-function
     ```  
   - **Step 3:** Adjust function configuration  
     ```bash
     aws lambda update-function-configuration --function-name my-function --memory-size 512 --timeout 30
     ```  
   - **Step 4:** Retest function and confirm performance  

---

## Validation

- Lambda function executes within memory and timeout limits  
- CloudWatch logs show no errors or throttling  
- Metrics confirm optimized execution duration  

---

## Folder Structure

007-lambda-memory-optimization/
├─ screenshots/ # Screenshots of logs, metrics, and updated config
├─ logs/ # CloudWatch logs or diagnostic logs
├─ scripts/ # Optional helper scripts or automation
└─ README.md # This file

yaml
Copy code

---

## Tech Stack

- AWS Lambda  
- IAM Roles & Policies  
- CloudWatch Logs & Metrics  
- Python / Node.js for Lambda functions  

---

## Skills Gained

✅ Diagnosing Lambda memory and timeout issues  
✅ Adjusting configuration for performance optimization  
✅ Reading and interpreting CloudWatch logs and metrics  
✅ Ensuring reliable and optimized serverless functions