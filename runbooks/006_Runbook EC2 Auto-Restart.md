# Runbook: EC2 Auto-Restart Issue

## Summary
EC2 instance restarts unexpectedly.

## Symptoms
- Unexpected reboot events
- CloudWatch logs show system failures

## Likely Root Causes
- Health check failures  
- Auto Recovery enabled  
- Kernel panic  
- Hardware issues

## Troubleshooting Steps
1. Check EC2 system logs  
2. Review CloudWatch metrics  
3. Check Auto Recovery settings  
4. Inspect OS logs  
5. Validate instance type stability

## Fix
- Disable Auto Recovery  
- Patch OS  
- Change instance type

## Prevention
- Use stable AMIs  
- Monitor CPU credits

## Validation
Instance remains stable for 24 hours.