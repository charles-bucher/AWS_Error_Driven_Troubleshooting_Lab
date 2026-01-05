# Runbook: S3 Public Bucket

## Summary
An S3 bucket is unintentionally public.

## Symptoms
- Public access warnings in console
- Objects accessible without authentication

## Likely Root Causes
- Public ACL
- Public bucket policy
- Block Public Access disabled

## Troubleshooting Steps
1. Check Block Public Access settings  
2. Review bucket policy  
3. Review object ACLs  
4. Use IAM Access Analyzer

## Fix
- Enable Block Public Access  
- Remove public statements from bucket policy  
- Remove public ACLs

## Prevention
- Use SCPs to block public buckets  
- Use S3 Access Analyzer

## Validation
Confirm bucket is private using: