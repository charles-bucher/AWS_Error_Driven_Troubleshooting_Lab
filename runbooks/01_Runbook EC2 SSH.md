# Runbook: EC2 SSH Lockout

## Summary
User cannot SSH into an EC2 instance.

## Symptoms
- SSH timeout
- “Connection refused”
- No response on port 22

## Likely Root Causes
- Security group missing port 22
- NACL blocking inbound/outbound
- Instance has no public IP
- Key pair mismatch
- Broken SSH daemon on instance

## Troubleshooting Steps
1. Check instance state  
2. Verify public IP or Elastic IP  
3. Check security group inbound rules  
4. Check NACL rules  
5. Use EC2 Reachability Analyzer  
6. Use EC2 Serial Console to inspect SSH service  
7. Validate correct key pair

## Fix
- Add SG rule for port 22  
- Correct NACL rules  
- Restart SSH service  
- Reassign public IP  
- Replace key pair if needed

## Prevention
- Use SSM Session Manager  
- Enforce baseline SG templates  
- Use IMDSv2 and hardened AMIs

## Validation
SSH into the instance successfully.