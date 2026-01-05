# Runbook: Lambda Memory Optimization

## Summary
Lambda function runs slowly due to low memory.

## Symptoms
- High duration  
- Low memory allocation  
- Throttling

## Likely Root Causes
- Insufficient memory  
- Inefficient code  
- Large dependencies

## Troubleshooting Steps
1. Check CloudWatch metrics  
2. Increase memory  
3. Test performance  
4. Optimize code  
5. Reduce package size

## Fix
- Increase memory  
- Optimize logic  
- Use layers

## Prevention
- Use Lambda Power Tuning

## Validation
Duration decreases after memory increase.