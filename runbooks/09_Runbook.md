# Runbook: IAM Role Misconfiguration

## Summary
IAM role cannot be assumed or used.

## Symptoms
- AccessDenied  
- “Not authorized to perform sts:AssumeRole”

## Likely Root Causes
- Wrong trust policy  
- Missing permissions  
- Wrong principal

## Troubleshooting Steps
1. Check trust policy  
2. Check permissions policy  
3. Validate principal  
4. Test AssumeRole with CLI

## Fix
- Correct trust policy  
- Add required permissions

## Prevention
- Use IAM Access Analyzer

## Validation
Assume role successfully.