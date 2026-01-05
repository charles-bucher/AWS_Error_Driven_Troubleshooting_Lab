Runbook Lambda Memory Optimization.md
# Lambda Memory Optimization Runbook

**Author:** Charles Bucher  
**Repo:** AWS_Error_Driven_Troubleshooting_Lab  
**Date:** 2026-01-05  
**Purpose:** Identify inefficient memory allocations for AWS Lambda functions and provide optimization recommendations.

---

## 1. Objective
Ensure all Lambda functions are allocated memory according to usage patterns to reduce costs and improve performance.

---

## 2. Prerequisites
- AWS account with access to Lambda and CloudWatch
- AWSPowerShell module installed (`Install-Module -Name AWSPowerShell.NetCore`)
- IAM permissions: `lambda:ListFunctions`, `cloudwatch:GetMetricStatistics`

---

## 3. Steps

### 3.1 Launch Script
Run the PowerShell script:

```powershell
.\lambda_memory_optimization.ps1

3.2 Review Output

The script will list each Lambda function:

Function Name	Allocated Memory (MB)	Max Used (MB)	Usage %	Recommendation
ExampleLambda	1024	400	39%	Reduce memory
3.3 Actions

Functions under 50% usage → consider reducing memory allocation

Functions over 90% usage → consider increasing memory to prevent throttling

Functions in the 50–90% range → no change needed

3.4 Documentation

Save output logs for auditing

Take a screenshot of high/low usage examples

4. References

AWS Lambda Memory Allocation

CloudWatch Metrics for Lambda

5. Notes

Run weekly for active Lambda functions

Adjust script filters to focus on critical functions only


---

## **2. `Runbook Lambda Error Logs.md`**
```markdown
# Lambda Error Logs Runbook

**Author:** Charles Bucher  
**Repo:** AWS_Error_Driven_Troubleshooting_Lab  
**Date:** 2026-01-05  
**Purpose:** Identify recent errors in AWS Lambda functions via CloudWatch logs.

---

## 1. Objective
Quickly find Lambda function errors for troubleshooting and incident documentation.

---

## 2. Prerequisites
- AWS account with access to Lambda and CloudWatch
- AWSPowerShell module installed
- IAM permissions: `lambda:ListFunctions`, `logs:GetLogEvents`, `logs:DescribeLogStreams`

---

## 3. Steps

### 3.1 Launch Script
Run the PowerShell script:

```powershell
.\lambda_error_logs.ps1

3.2 Review Output

The script displays error messages for the last 24 hours:

[FunctionName][LogStream] Timestamp: Error message


Errors highlighted in red

Includes timestamp, function name, and log stream

3.3 Actions

Investigate functions with repeated errors

Check for misconfigured memory, IAM permissions, or runtime errors

Document root cause and remediation steps

3.4 Documentation

Save logs for each incident

Take a screenshot of critical errors for portfolio or audit

4. References

AWS CloudWatch Logs

AWS Lambda Troubleshooting

5. Notes

Run daily for production functions

Can be automated via a scheduled PowerShell task


---