# Runbook: EFS Access Permissions

## Summary
EC2 instance cannot mount EFS.

## Symptoms
- Permission denied  
- Mount command fails

## Likely Root Causes
- Wrong security group  
- Wrong EFS access point  
- IAM policy missing  
- NFS port blocked

## Troubleshooting Steps
1. Check SG inbound/outbound  
2. Check EFS access point  
3. Validate IAM permissions  
4. Test NFS port 2049

## Fix
- Update SG  
- Correct access point  
- Add IAM permissions

## Prevention
- Use EFS mount helper  
- Use access points consistently

## Validation
Mount EFS successfully.