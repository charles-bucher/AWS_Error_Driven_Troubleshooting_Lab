# Runbook: VPC Network Troubleshoot

## Summary
Resources cannot communicate inside VPC.

## Symptoms
- Timeouts  
- No connectivity  
- DNS failures

## Likely Root Causes
- Wrong route tables  
- Wrong NACLs  
- Wrong SG rules  
- Missing IGW or NAT

## Troubleshooting Steps
1. Check route tables  
2. Check NACLs  
3. Check SG rules  
4. Test ping/curl  
5. Validate DNS settings

## Fix
- Correct routing  
- Fix NACLs  
- Update SG rules

## Prevention
- Use VPC Flow Logs  
- Use standardized network templates

## Validation
Connectivity restored.