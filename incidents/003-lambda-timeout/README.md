# Incident 003: Lambda Function Timeout

**Incident ID:** INC-003  
**Date:** 2024-12-20  
**Severity:** P3 (Medium)  
**Status:** ✅ Resolved  
**Duration:** 25 minutes  

---

## 📋 Summary

Lambda function `ec2-scheduler` repeatedly timed out after 30 seconds while attempting to stop multiple EC2 instances. Function was processing 15 instances but couldn't complete within default 30-second timeout.

**Impact:** Cost-saving automation delayed by ~25 minutes. Instances continued running during failure window, resulting in ~$2 additional cost.

---

## ⏱️ Timeline

| Time (EST) | Event |
|------------|-------|
| 18:00 | Scheduled Lambda execution (stop instances for night) |
| 18:00:30 | Lambda timed out after 30 seconds |
| 18:05 | Second retry attempt - timeout again |
| 18:10 | CloudWatch alarm fired for Lambda errors |
| 18:12 | Acknowledged alert, began investigation |
| 18:15 | Reviewed CloudWatch Logs, identified timeout issue |
| 18:18 | Analyzed function code - found inefficient loop |
| 18:20 | Increased timeout to 60 seconds (temporary fix) |
| 18:20 | Re-ran function manually - successful |
| 18:22 | Optimized code to use batch operations |
| 18:25 | Tested optimized function - completes in 12 seconds |
| 18:30 | Deployed optimized version |

**Total Duration:** 25 minutes from first failure to permanent fix

---

## 🔍 Root Cause Analysis

### What Happened:

Lambda function stopped each EC2 instance sequentially in a loop:

**Original Code (Inefficient):**
```python
def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    instances = ['i-123', 'i-456', 'i-789', ...]  # 15 instances
    
    for instance_id in instances:
        # Stop each instance one at a time
        ec2.stop_instances(InstanceIds=[instance_id])
        
        # Wait for each to stop before continuing
        waiter = ec2.get_waiter('instance_stopped')
        waiter.wait(InstanceIds=[instance_id])  # This takes ~5 seconds per instance
    
    return {'statusCode': 200}
```

**Problem:** 15 instances × 5 seconds each = 75 seconds (exceeds 30s timeout)

### Why It Happened:

1. **Sequential Processing:** Stopping instances one by one instead of in batch
2. **Synchronous Waiting:** Waiting for each instance to stop before moving to next
3. **Default Timeout:** 30 seconds is too short for this workload
4. **No Optimization:** Code worked fine with 5 instances, didn't scale to 15

### Contributing Factors:

- Added more instances without testing function performance
- Didn't monitor Lambda duration metrics
- No load testing before deploying
- Default timeout wasn't adjusted when workload increased

---

## 🔧 Resolution Steps

### 1. Immediate Fix (Increased Timeout)

```bash
# Temporarily increase timeout to 60 seconds
aws lambda update-function-configuration \
    --function-name ec2-scheduler \
    --timeout 60
```

**Result:** Function now completes (but takes ~45 seconds)

### 2. Optimized Code (Permanent Fix)

**Optimized Code:**
```python
def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    instances = ['i-123', 'i-456', 'i-789', ...]  # 15 instances
    
    # Stop ALL instances in single API call
    ec2.stop_instances(InstanceIds=instances)
    
    # Don't wait - let them stop asynchronously
    # Next scheduled run will verify they stopped
    
    return {
        'statusCode': 200,
        'body': f'Initiated stop for {len(instances)} instances'
    }
```

**Improvements:**
- ✅ Single API call instead of 15
- ✅ No waiting for instances to stop
- ✅ Completes in ~2 seconds (was 45 seconds)
- ✅ Uses 95% less execution time = lower cost

### 3. Deployed and Tested

```bash
# Deploy optimized version
aws lambda update-function-code \
    --function-name ec2-scheduler \
    --zip-file fileb://function.zip

# Test manually
aws lambda invoke \
    --function-name ec2-scheduler \
    --payload '{}' \
    response.json

# Check duration
cat response.json
# Duration: 2143ms (was 45000ms)
```

---

## 📸 Evidence

### CloudWatch Logs - Timeout Error:
```
START RequestId: abc-123-def
[INFO] Stopping instance i-123...
[INFO] Stopping instance i-456...
[INFO] Stopping instance i-789...
... (continues) ...
END RequestId: abc-123-def
REPORT RequestId: abc-123-def
Duration: 30000.00 ms
Billed Duration: 30000 ms
Memory Size: 128 MB
Max Memory Used: 58 MB
Status: Task timed out after 30.00 seconds
```

### Duration Before/After:
![Lambda Duration Metrics](../docs/screenshots/incidents/003-lambda-duration-improvement.png)
*Duration dropped from 45s to 2s after optimization*

### Cost Impact:
```
Before: 45 seconds × $0.0000166667 per GB-second × 0.128 GB = $0.00009600/execution
After:   2 seconds × $0.0000166667 per GB-second × 0.128 GB = $0.00000427/execution

Savings: 95.5% per execution
Monthly savings (2 runs/day × 30 days): $0.058
```

---

## 🛡️ Prevention Strategies

### Implemented:

#### 1. Added Duration Monitoring
```bash
# CloudWatch alarm for duration approaching timeout
aws cloudwatch put-metric-alarm \
    --alarm-name "Lambda-Duration-Warning-ec2-scheduler" \
    --metric-name Duration \
    --namespace AWS/Lambda \
    --statistic Maximum \
    --period 300 \
    --threshold 50000 \
    --comparison-operator GreaterThanThreshold \
    --evaluation-periods 1 \
    --dimensions Name=FunctionName,Value=ec2-scheduler
```

#### 2. Implemented Batch Operations Pattern
All future Lambda functions follow this pattern:
- Use batch API calls when available
- Avoid synchronous waiting
- Process asynchronously when possible

#### 3. Load Testing Before Deploy
```bash
# Test with maximum expected load
for i in {1..10}; do
    aws lambda invoke --function-name ec2-scheduler response.json
    cat response.json | jq .Duration
done
```

#### 4. Added Timeout Buffer
```
Function timeout = Expected duration × 3
Example: 10 second function → 30 second timeout
```

---

## 📚 Lessons Learned

### What Went Well:
✅ CloudWatch alarm detected issue quickly  
✅ Logs clearly showed the problem  
✅ Had immediate fix (increase timeout)  
✅ Found permanent optimization  
✅ Reduced cost and improved reliability  

### What Could Be Better:
❌ Should have load tested with 15 instances  
❌ Didn't monitor duration metrics proactively  
❌ Code wasn't optimized from the start  
❌ Timeout wasn't configured appropriately  

### Key Takeaways:

1. **Batch operations are critical** for Lambda performance
2. **Monitor duration metrics** before timeouts happen
3. **Test at scale** even for simple functions
4. **Async > Sync** - don't wait if you don't have to
5. **Set appropriate timeouts** based on actual workload

---

## 🔗 Related Resources

### Runbook:
- [RUNBOOK: Lambda Timeout Troubleshooting](RUNBOOK.md)

### Code:
- `scripts/ec2_scheduler.py` - Optimized version
- `tests/test_ec2_scheduler.py` - Load tests

### AWS Documentation:
- [Lambda Limits](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html)
- [Lambda Best Practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
- [Boto3 Batch Operations](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-example-managing-instances.html)

---

## 📊 Incident Metrics

| Metric | Value |
|--------|-------|
| Time to Detect | 10 minutes |
| Time to Temporary Fix | 20 minutes |
| Time to Permanent Fix | 25 minutes |
| Duration Improvement | 95% (45s → 2s) |
| Cost Savings | 95.5% per execution |
| Additional Cost (incident) | ~$2 |
| Recurrence | None |

---

## ✅ Follow-up Actions

- [x] Increase timeout temporarily (Completed: 2024-12-20 18:20)
- [x] Optimize code for batch operations (Completed: 2024-12-20 18:22)
- [x] Deploy optimized version (Completed: 2024-12-20 18:30)
- [x] Add duration monitoring (Completed: 2024-12-20 19:00)
- [x] Create load testing script (Completed: 2024-12-21)
- [x] Document optimization patterns (Completed: 2024-12-21)
- [x] Review other Lambda functions for similar issues (Completed: 2024-12-22)
- [ ] Implement automated performance testing in CI/CD (Planned: Q1 2025)

---

## 👤 Incident Owner

**Name:** Charles Bucher  
**Role:** CloudOps Lab Owner  
**Contact:** quietopscb@gmail.com

---

## 📝 Additional Notes

### Code Optimization Patterns Learned:

**Pattern 1: Batch API Calls**
```python
# Bad
for item in items:
    api_call(item)

# Good
api_call(items)  # Single call for all items
```

**Pattern 2: Avoid Synchronous Waiting**
```python
# Bad
trigger_action()
wait_for_completion()  # Blocks

# Good
trigger_action()
# Let it complete asynchronously
# Check status in next invocation if needed
```

**Pattern 3: Connection Reuse**
```python
# Bad
def lambda_handler(event, context):
    client = boto3.client('ec2')  # New connection every time
    
# Good
client = boto3.client('ec2')  # Reused across invocations
def lambda_handler(event, context):
    # Use existing client
```

This incident taught me that Lambda optimization isn't just about cost—it's about reliability. A function that takes 2 seconds is much less likely to timeout than one that takes 45 seconds.

---

**Document Version:** 1.0  
**Last Updated:** 2024-12-20  
**Next Review:** Quarterly or after Lambda changes