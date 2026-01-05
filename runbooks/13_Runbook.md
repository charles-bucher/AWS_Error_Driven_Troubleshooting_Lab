# Runbook: Cost Optimization Lab

## Summary
Environment has unnecessary or expensive resources.

## Symptoms
- High monthly bill  
- Idle resources  
- Unused storage

## Likely Root Causes
- Overprovisioned EC2  
- Unused EBS volumes  
- Idle RDS  
- S3 storage class mismatch

## Troubleshooting Steps
1. Review Cost Explorer  
2. Identify idle EC2  
3. Identify unused EBS  
4. Review RDS usage  
5. Review S3 storage classes

## Fix
- Right-size EC2  
- Delete unused EBS  
- Stop or downsize RDS  
- Move S3 to cheaper storage

## Prevention
- Use budgets  
- Use Trusted Advisor  
- Use lifecycle policies

## Validation
Cost Explorer shows reduced spend.