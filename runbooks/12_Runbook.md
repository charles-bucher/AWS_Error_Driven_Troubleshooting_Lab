# Runbook: CloudTrail Audit

## Summary
CloudTrail logs missing or incomplete.

## Symptoms
- No events recorded  
- Gaps in logs  
- S3 bucket empty

## Likely Root Causes
- CloudTrail disabled  
- Wrong S3 bucket  
- Permissions issue  
- Region mismatch

## Troubleshooting Steps
1. Check CloudTrail status  
2. Validate S3 bucket  
3. Check IAM permissions  
4. Check multi-region settings

## Fix
- Enable CloudTrail  
- Correct S3 bucket  
- Fix IAM permissions

## Prevention
- Use organization trails  
- Enable log file validation

## Validation
Events appear in CloudTrail console.