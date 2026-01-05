# Runbook: S3 Lifecycle Policy Issue

## Summary
Lifecycle rules not transitioning or expiring objects.

## Symptoms
- Objects not moving to Glacier  
- Objects not expiring

## Likely Root Causes
- Prefix mismatch  
- Rule disabled  
- Incomplete transition days  
- Object versioning mismatch

## Troubleshooting Steps
1. Review lifecycle rules  
2. Check prefix filters  
3. Check versioning  
4. Validate transition days  
5. Use S3 Storage Lens

## Fix
- Correct prefix  
- Enable rule  
- Adjust transition days

## Prevention
- Use standardized lifecycle templates

## Validation
Check lifecycle status in S3 console.