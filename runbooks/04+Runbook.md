# Runbook: RDS Connection Issue

## Summary
Application cannot connect to RDS database.

## Symptoms
- Connection timeout
- Authentication failure
- “Could not connect to host”

## Likely Root Causes
- Wrong security group rules  
- Wrong DB endpoint  
- DB stopped  
- Incorrect credentials  
- VPC routing issue

## Troubleshooting Steps
1. Check RDS instance status  
2. Validate endpoint  
3. Check SG inbound rules  
4. Check NACLs  
5. Test connectivity from EC2  
6. Validate credentials

## Fix
- Update SG rules  
- Restart RDS  
- Correct endpoint  
- Reset password

## Prevention
- Use parameter groups  
- Use Secrets Manager

## Validation
Connect successfully using: