# Runbook: S3 Public Bucket Immediate Remediation

**Runbook ID:** RB-INC-002  
**Last Updated:** 2024-12-18  
**Incident Type:** S3 Public Bucket Exposure  
**Severity:** P1 (Critical - Security)  
**Estimated Time:** 3-10 minutes  

---

## 📋 Overview

### Purpose
Immediate response procedure for S3 buckets accidentally or maliciously made public. This runbook prioritizes **speed** to minimize data exposure window.

### When to Use
- Security audit detects public S3 bucket
- GuardDuty alert: "S3 bucket has suspicious access"
- AWS Config compliance violation
- Manual discovery of public bucket
- **ANY** notification of public S3 bucket

### Critical Window
Every minute matters. Public buckets can be scanned and data exfiltrated within minutes of becoming public.

---

## 🚨 Step 1: Immediate Block (1 minute)

**DO THIS FIRST. Ask questions later.**

###  Option A: Automated Script (Fastest - 30 seconds)
```bash
# Run remediation script
python scripts/s3_public_remediate.py --bucket BUCKET_NAME --block-all
```

### Option B: AWS CLI (1 minute)
```bash
# Set bucket to private
aws s3api put-bucket-acl --bucket BUCKET_NAME --acl private

# Enable public access block (all 4 settings)
aws s3api put-public-access-block \
    --bucket BUCKET_NAME \
    --public-access-block-configuration \
        BlockPublicAcls=true,\
        IgnorePublicAcls=true,\
        BlockPublicPolicy=true,\
        RestrictPublicBuckets=true
```

### Option C: AWS Console (2 minutes)
1. Open S3 Console → Buckets
2. Click bucket name
3. Click "Permissions" tab
4. Click "Block public access"
5. Click "Edit"
6. Check ALL 4 boxes
7. Click "Save changes"
8. Type "confirm"

**Don't wait for investigation. Block first, investigate second.**

---

## ✅ Step 2: Verify Access Blocked (30 seconds)

### Test Anonymous Access
```bash
# Try to access bucket anonymously (should fail)
curl -I https://BUCKET_NAME.s3.amazonaws.com/

# Expected: 403 Forbidden or 404 Not Found
```

### Verify Public Access Block
```bash
# Check block settings
aws s3api get-public-access-block --bucket BUCKET_NAME
```

**Expected output:**
```json
{
    "PublicAccessBlockConfiguration": {
        "BlockPublicAcls": true,
        "IgnorePublicAcls": true,
        "BlockPublicPolicy": true,
        "RestrictPublicBuckets": true
    }
}
```

### Verify ACL is Private
```bash
# Check ACL
aws s3api get-bucket-acl --bucket BUCKET_NAME
```

**Should NOT contain:**
```json
"URI": "http://acs.amazonaws.com/groups/global/AllUsers"
```

**If still public:** Repeat Step 1 and check for bucket policy.

---

## 🔍 Step 3: Assess Exposure (2-3 minutes)

### A. Determine When Bucket Became Public
```bash
# Query CloudTrail for ACL/policy changes
aws cloudtrail lookup-events \
    --lookup-attributes AttributeKey=ResourceName,AttributeValue=BUCKET_NAME \
    --max-results 50 \
    --query 'Events[?EventName==`PutBucketAcl` || EventName==`PutBucketPolicy`].[EventTime,EventName,Username]' \
    --output table
```

**Note the timestamp when bucket became public.**

### B. Calculate Exposure Window
```
Public from: [timestamp from CloudTrail]
Blocked at: [current time]
Duration: [calculate difference]
```

### C. Check What Was Exposed
```bash
# List all objects
aws s3 ls s3://BUCKET_NAME --recursive | wc -l

# Check for sensitive files
aws s3 ls s3://BUCKET_NAME --recursive | grep -iE '\.(key|pem|p12|pfx|env|sql|csv|xls)'
```

---

## 🔍 Step 4: Investigate Unauthorized Access (3-5 minutes)

### A. Check S3 Server Access Logs (If Enabled)
```bash
# Check if logging enabled
aws s3api get-bucket-logging --bucket BUCKET_NAME

# If enabled, download recent logs
aws s3 sync s3://LOG_BUCKET/BUCKET_NAME/$(date +%Y-%m-%d)/ ./investigation/
```

### B. Query CloudTrail for Access
```bash
# Get all GetObject events during exposure window
aws cloudtrail lookup-events \
    --lookup-attributes AttributeKey=ResourceName,AttributeValue=BUCKET_NAME \
    --start-time 2024-12-18T10:15:00 \
    --end-time 2024-12-18T10:35:00 \
    --query 'Events[?EventName==`GetObject`].[EventTime,SourceIPAddress,UserAgent]' \
    --output table
```

### C. Analyze IP Addresses
```bash
# Extract unique IPs
aws cloudtrail lookup-events \
    --lookup-attributes AttributeKey=ResourceName,AttributeValue=BUCKET_NAME \
    --start-time START_TIME \
    --end-time END_TIME \
    | jq -r '.Events[].CloudTrailEvent' \
    | jq -r 'select(.eventName=="GetObject") | .sourceIPAddress' \
    | sort -u

# Check if IPs are yours
# Your known IPs: [list your IPs]
```

**Look for:**
- Unknown IP addresses
- High volume of requests from single IP
- Requests from unexpected countries
- Scanner user-agents (e.g., "aws-cli/", "curl/", "python-requests/")

---

## 📊 Step 5: Classify Data Sensitivity (2 minutes)

### A. Determine Data Classification
```bash
# Check bucket tags
aws s3api get-bucket-tagging --bucket BUCKET_NAME

# Check object types
aws s3 ls s3://BUCKET_NAME --recursive | awk -F'.' '{print $NF}' | sort | uniq -c
```

### B. Sensitivity Checklist

**High Sensitivity (Immediate escalation):**
- [ ] Customer PII (names, emails, addresses, SSN)
- [ ] Payment card data
- [ ] Healthcare records (PHI)
- [ ] Authentication credentials (passwords, keys)
- [ ] Proprietary source code
- [ ] Financial records

**Medium Sensitivity:**
- [ ] Internal documents
- [ ] Employee data (non-PII)
- [ ] Business plans
- [ ] Contracts

**Low Sensitivity:**
- [ ] Test data
- [ ] Logs (sanitized)
- [ ] Public marketing materials

### C. Determine Impact

| Sensitivity | Unauthorized Access | Action Required |
|-------------|---------------------|-----------------|
| High | Confirmed | Escalate immediately, breach notification may be required |
| High | Possible | Escalate, start investigation |
| Medium | Confirmed | Document, inform management |
| Medium | Possible | Continue investigation |
| Low | Any | Document for records |

---

## 🚨 Step 6: Escalation (If Needed)

### When to Escalate:

**Escalate Immediately If:**
- ✅ Confirmed unauthorized access to HIGH sensitivity data
- ✅ Customer data exposed
- ✅ Credentials/keys exposed
- ✅ Compliance data exposed (HIPAA, PCI, GDPR)

### Escalation Procedure:

**1. Notify Management:**
```
Subject: [URGENT] S3 Bucket Security Incident - BUCKET_NAME

Summary:
- Bucket: BUCKET_NAME
- Exposure Duration: X minutes
- Data Sensitivity: [High/Medium/Low]
- Unauthorized Access: [Confirmed/Possible/None]
- Current Status: Bucket secured

Action Required:
- [List specific actions needed]

Incident Report: [link to incident README]
```

**2. Contact AWS Support (If Needed):**
- Open support case
- Select "Security" category
- Include incident details
- Request assistance with forensics

**3. Legal/Compliance (If Needed):**
- Notify legal team
- Determine breach notification requirements
- GDPR: 72 hours to notify
- State laws: varies by jurisdiction

---

## 🛡️ Step 7: Prevention Measures (5 minutes)

### A. Enable Account-Wide Public Access Block

```bash
# Block public access for ALL buckets in account
aws s3control put-public-access-block \
    --account-id $(aws sts get-caller-identity --query Account --output text) \
    --public-access-block-configuration \
        BlockPublicAcls=true,\
        IgnorePublicAcls=true,\
        BlockPublicPolicy=true,\
        RestrictPublicBuckets=true
```

**This prevents ANY bucket from being made public accidentally.**

### B. Enable S3 Access Logging

```bash
# Create logging bucket if needed
aws s3 mb s3://my-s3-access-logs

# Enable logging on target bucket
aws s3api put-bucket-logging \
    --bucket BUCKET_NAME \
    --bucket-logging-status '{
        "LoggingEnabled": {
            "TargetBucket": "my-s3-access-logs",
            "TargetPrefix": "'"BUCKET_NAME"'/"
        }
    }'
```

### C. Enable Versioning (Ransomware Protection)

```bash
# Enable versioning
aws s3api put-bucket-versioning \
    --bucket BUCKET_NAME \
    --versioning-configuration Status=Enabled
```

### D. Enable Encryption

```bash
# Enable default encryption (AES-256)
aws s3api put-bucket-encryption \
    --bucket BUCKET_NAME \
    --server-side-encryption-configuration '{
        "Rules": [{
            "ApplyServerSideEncryptionByDefault": {
                "SSEAlgorithm": "AES256"
            }
        }]
    }'
```

### E. Set Up Monitoring

```bash
# Create Config rule to detect public buckets
aws configservice put-config-rule \
    --config-rule '{
        "ConfigRuleName": "s3-bucket-public-read-prohibited",
        "Source": {
            "Owner": "AWS",
            "SourceIdentifier": "S3_BUCKET_PUBLIC_READ_PROHIBITED"
        }
    }'

# Create CloudWatch alarm
aws cloudwatch put-metric-alarm \
    --alarm-name S3-Public-Bucket-Detected \
    --alarm-description "Alert on public S3 bucket" \
    --namespace AWS/Config \
    --metric-name ComplianceStatus \
    --statistic Maximum \
    --period 300 \
    --threshold 1 \
    --comparison-operator GreaterThanThreshold
```

---

## 📝 Step 8: Documentation (5 minutes)

### A. Create Incident Report

Use [Incident README Template](README.md) and document:
- Timeline of events
- Root cause
- Data exposed
- Unauthorized access (if any)
- Resolution steps taken
- Prevention measures implemented

### B. Update Runbook (If Needed)

If you learned something new:
- Add to troubleshooting section
- Update time estimates
- Add new prevention measures
- Share lessons learned

---

## 🔍 Troubleshooting

### Issue: Bucket Still Shows as Public After Fix

**Check 1: Bucket Policy Exists**
```bash
# Check for bucket policy (separate from ACL)
aws s3api get-bucket-policy --bucket BUCKET_NAME

# If policy allows public access, delete it
aws s3api delete-bucket-policy --bucket BUCKET_NAME
```

**Check 2: Multiple Grants in ACL**
```bash
# Get full ACL
aws s3api get-bucket-acl --bucket BUCKET_NAME

# Look for multiple grants, remove public ones
```

**Check 3: Object-Level ACLs**
```bash
# Check if individual objects are public
aws s3api list-objects --bucket BUCKET_NAME --query 'Contents[*].Key' --output text | \
while read key; do
    aws s3api get-object-acl --bucket BUCKET_NAME --key "$key" | \
    grep -q "AllUsers" && echo "Public: $key"
done
```

### Issue: Cannot Enable Public Access Block

**Error:** `AccessDenied` or `Conflict`

**Solution:**
```bash
# Check if there's an account-level block preventing bucket-level config
aws s3control get-public-access-block \
    --account-id $(aws sts get-caller-identity --query Account --output text)

# May need to disable account-level block first, or use account-level only
```

### Issue: Need to Verify No Data Exfiltration

**Without S3 Access Logs:**
```bash
# Use CloudTrail (limited to last 90 days)
aws cloudtrail lookup-events \
    --lookup-attributes AttributeKey=EventName,AttributeValue=GetObject \
    --max-results 1000 \
    | jq -r '.Events[] | select(.Resources[0].ResourceName | contains("BUCKET_NAME"))'
```

**With VPC Flow Logs (if bucket accessed via VPC endpoint):**
```bash
# Query flow logs for S3 traffic
aws logs filter-log-events \
    --log-group-name /aws/vpc/flowlogs \
    --filter-pattern "[version, account, eni, source, destination, srcport, destport=443, protocol=6, packets, bytes, start, end, action=ACCEPT, status]" \
    --start-time $(date -d '1 day ago' +%s)000
```

---

## 📚 Related Resources

### Incident Documentation
- [Incident 002 README](README.md) - Full incident report

### AWS Documentation
- [S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)
- [S3 Security Best Practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html)
- [Data Breach Response](https://aws.amazon.com/premiumsupport/knowledge-center/potential-account-compromise/)

### Scripts
- `scripts/s3_public_check.py` - Scan for public buckets
- `scripts/s3_public_remediate.py` - Auto-remediate
- `monitoring/security_audit.py` - Regular security scan

### Compliance
- [GDPR Breach Notification](https://gdpr.eu/data-breach-notification/)
- [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/)

---

## ⏱️ Time Estimates by Scenario

| Scenario | Time to Remediate |
|----------|-------------------|
| Simple ACL issue, no access | 3 minutes |
| ACL + bucket policy | 5 minutes |
| With investigation (no access) | 10 minutes |
| With confirmed unauthorized access | 15-30 minutes |
| With sensitive data + access | Hours (escalation required) |

---

## 💡 Pro Tips

1. **Speed over perfection** - Block first, investigate later

2. **Account-wide block** prevents this entirely:
   ```bash
   aws s3control put-public-access-block --account-id <account> \
       --public-access-block-configuration BlockPublicAcls=true,...
   ```

3. **Monitor continuously** - Don't rely on weekly scans:
   - AWS Config rules (real-time)
   - GuardDuty (threat detection)
   - Automated hourly scans

4. **Test your incident response** - Practice this runbook

5. **Know your data** - Tag buckets by sensitivity level

---

## ✅ Post-Incident Checklist

- [ ] Bucket access blocked and verified
- [ ] Exposure window calculated
- [ ] Data sensitivity assessed
- [ ] CloudTrail reviewed for unauthorized access
- [ ] Escalated if necessary
- [ ] Prevention measures implemented
- [ ] Incident documented
- [ ] Runbook updated with learnings
- [ ] Team training conducted (if team environment)

---

**Runbook Owner:** Charles Bucher  
**Contact:** quietopscb@gmail.com  
**Version:** 1.0  
**Last Tested:** 2024-12-18  
**Next Review:** Quarterly or after each incident