# Runbook: CloudWatch Alerts Issue

## Summary
CloudWatch alarms not triggering or not notifying.

## Symptoms
- No SNS notifications  
- Alarm stuck in “INSUFFICIENT_DATA”

## Likely Root Causes
- Wrong metric  
- Wrong threshold  
- SNS misconfigured  
- IAM permissions missing

## Troubleshooting Steps
1. Check metric graph  
2. Validate threshold  
3. Test SNS topic  
4. Check IAM permissions  
5. Review alarm history

## Fix
- Correct metric  
- Fix SNS subscription  
- Adjust threshold

## Prevention
- Use metric math  
- Use composite alarms

## Validation
Trigger alarm manually.