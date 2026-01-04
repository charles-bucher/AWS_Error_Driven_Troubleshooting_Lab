# Incident 002: S3 Public Bucket Exposure

**Incident ID:** INC-002  
**Date:** 2024-12-18  
**Severity:** P1 (Critical - Security)  
**Status:** ✅ Resolved  
**Duration:** 8 minutes  

---

## 📋 Summary

S3 bucket `charlesb-lab-data` was accidentally configured with public read access during testing, potentially exposing non-sensitive test data. Detected by automated security audit script, remediated immediately.

**Impact:** Test data (non-sensitive) was publicly accessible for approximately 15 minutes. No actual sensitive data exposed. No confirmed unauthorized access detected.

---

## ⏱️ Timeline

| Time (EST) | Event |
|------------|-------|
| 10:15 | Modified S3 bucket ACL while testing access controls |
| 10:18 | Bucket became publicly accessible |
| 10:30 | Weekly security audit script ran |
| 10:30 | Script detected public bucket, sent alert |
| 10:31 | Acknowledged alert, began investigation |
| 10:33 | Confirmed bucket was public |
| 10:34 | Ran automated remediation script |
| 10:36 | Verified bucket now private |
| 10:38 | Checked CloudTrail for any unauthorized access |
| 10:40 | No unauthorized access found |
| 10:45 | Documented incident and implemented prevention |

**Total Public Exposure:** ~15 minutes  
**Time to Remediation:** 8 minutes (from detection to fix)

---

## 🔍 Root Cause Analysis

### What Happened:

While testing S3 access control scenarios for my lab, I modified the bucket ACL using:

```bash
aws s3api put-bucket-acl --bucket charlesb-lab-data --acl public-read
```

I intended to test this on a **test** bucket, but ran the command on my main lab data bucket instead.

**Before (Correct):**
```json
{
    "Owner": {...},
    "Grants": [{
        "Grantee": {
            "Type": "CanonicalUser",
            "ID": "..."
        },
        "Permission": "FULL_CONTROL"
    }]
}
```

**After (Broken):**
```json
{
    "Owner": {...},
    "Grants": [{
        "Grantee": {
            "Type": "Group",
            "URI": "http://acs.amazonaws.com/groups/global/AllUsers"
        },
        "Permission": "READ"
    }]
}
```

**Result:** Anyone on the internet could list and download objects from the bucket.

### Why It Happened:

1. **Human Error:** Ran command on wrong bucket (tab-completion error)
2. **No Confirmation:** AWS CLI doesn't ask "Are you sure?" for dangerous operations
3. **No Public Access Block:** Bucket didn't have S3 Block Public Access enabled
4. **Testing in Production:** Should have used dedicated test bucket

### Contributing Factors:

- Late night testing (fatigue)
- Similar bucket names (`charlesb-lab-data` vs `charlesb-lab-test-data`)
- No pre-command verification habit
- Public access block not enabled account-wide

---

## 🔧 Resolution Steps

### 1. Confirmed Public Access
```bash
# Check bucket ACL
aws s3api get-bucket-acl --bucket charlesb-lab-data

# Check bucket policy
aws s3api get-bucket-policy --bucket charlesb-lab-data 2>/dev/null || echo "No policy"

# Check public access block
aws s3api get-public-access-block --bucket charlesb-lab-data 2>/dev/null || echo "Not configured"
```

**Result:** Public-read ACL confirmed, no bucket policy, no public access block

### 2. Ran Automated Remediation
```bash
# Used my remediation script
python scripts/s3_public_remediate.py --bucket charlesb-lab-data --block-all
```

Script performed:
1. ✅ Set bucket ACL to private
2. ✅ Enabled public access block (all 4 settings)
3. ✅ Logged action to CloudWatch

### 3. Verified Bucket is Private
```bash
# Test anonymous access (should fail)
curl -I https://charlesb-lab-data.s3.amazonaws.com/

# Expected: 403 Forbidden (got it!)
```

### 4. Checked for Unauthorized Access
```bash
# Query CloudTrail for GetObject events
aws cloudtrail lookup-events \
    --lookup-attributes AttributeKey=ResourceName,AttributeValue=charlesb-lab-data \
    --start-time 2024-12-18T10:15:00 \
    --end-time 2024-12-18T10:35:00 \
    --query 'Events[?EventName==`GetObject`]'
```

**Result:** Only my own access (from security audit script). No unauthorized access detected.

---

## 📸 Evidence

### Security Audit Detection:
![Security Audit Alert](../docs/screenshots/incidents/002-security-audit-alert.png)
*Security audit script detecting public bucket*

### Bucket ACL Before Fix:
```bash
$ aws s3api get-bucket-acl --bucket charlesb-lab-data

{
    "Grants": [
        {
            "Grantee": {
                "Type": "Group",
                "URI": "http://acs.amazonaws.com/groups/global/AllUsers"
            },
            "Permission": "READ"
        }
    ]
}
```

### Public Access Block After Fix:
![Public Access Block](../docs/screenshots/incidents/002-public-access-block.png)
*All 4 public access block settings enabled*

### CloudTrail Analysis:
```bash
$ aws cloudtrail lookup-events --lookup-attributes \
    AttributeKey=ResourceName,AttributeValue=charlesb-lab-data

# Only my IP addresses in results - no unauthorized access
```

---

## 📊 Data Exposure Assessment

### What Was in the Bucket:
```
Total Objects: 47
Total Size: 2.3 MB

Content breakdown:
- CloudWatch logs (test data): 35 files
- Terraform state backups: 8 files
- Sample CSV files: 4 files
```

### Sensitivity Classification:
- ❌ No customer data
- ❌ No credentials or secrets
- ❌ No PII (Personal Identifiable Information)
- ✅ Only: Test logs and sample data

### Risk Assessment:
**Overall Risk:** LOW
- No sensitive data exposed
- No confirmed unauthorized access
- Quick remediation (8 minutes)
- No regulatory notification required

---

## 🛡️ Prevention Strategies

### Implemented Immediately:

#### 1. Enabled Public Access Block Account-Wide
```bash
# Block all public access for ALL buckets in account
aws s3control put-public-access-block \
    --account-id $(aws sts get-caller-identity --query Account --output text) \
    --public-access-block-configuration \
        BlockPublicAcls=true,\
        IgnorePublicAcls=true,\
        BlockPublicPolicy=true,\
        RestrictPublicBuckets=true
```

**Result:** Now it's **impossible** to make buckets public (even accidentally)

#### 2. Updated Security Audit Script
```python
# Now runs every 6 hours (was daily)
# Added immediate SNS alert for public buckets
# Added automatic remediation option
```

#### 3. Created Pre-Command Checklist
Before running S3 commands:
- [ ] Verify bucket name (echo first)
- [ ] Check if command affects public access
- [ ] Run in dry-run mode if available
- [ ] Have remediation script ready

#### 4. Separated Test/Prod Buckets
```bash
# Test buckets clearly marked
charlesb-test-*     # For testing access controls
charlesb-lab-*      # For actual lab data
```

#### 5. Implemented Tagging
```bash
# Tag buckets by purpose
aws s3api put-bucket-tagging \
    --bucket charlesb-lab-data \
    --tagging 'TagSet=[{Key=Environment,Value=Lab},{Key=Sensitivity,Value=Low}]'
```

### Planned Improvements:

- [ ] Create AWS Config rule to auto-remediate public buckets
- [ ] Set up S3 access logging for audit trail
- [ ] Enable versioning on all buckets (ransomware protection)
- [ ] Implement encryption by default
- [ ] Create bucket policy templates

---

## 📚 Lessons Learned

### What Went Well:
✅ Automated detection (security audit script)  
✅ Fast remediation (8 minutes)  
✅ No sensitive data exposed  
✅ No unauthorized access  
✅ Good CloudTrail logging for investigation  

### What Could Be Better:
❌ Should have had public access block enabled from day 1  
❌ Bucket names too similar (confusion risk)  
❌ Didn't verify bucket name before running command  
❌ Testing dangerous operations late at night  

### Key Takeaways:

1. **Defense in Depth Works** - Public access block would have prevented this
2. **Automation Saves Time** - Security script detected it before I did
3. **Naming Conventions Matter** - Clear bucket names prevent confusion
4. **Documentation is Critical** - This incident report helps future me
5. **Test in Test, Not Prod** - Separate environments for testing

---

## 🔗 Related Resources

### Runbook:
- [RUNBOOK: S3 Public Bucket Remediation](RUNBOOK.md)

### Scripts:
- `scripts/s3_public_check.py` - Scans for public buckets
- `scripts/s3_public_remediate.py` - Auto-fixes public buckets
- `monitoring/security_audit.py` - Weekly security scan

### Documentation:
- `docs/s3-security-baseline.md` - S3 security requirements
- `docs/incident-response-plan.md` - Incident response procedures

### AWS Resources:
- [S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)
- [S3 Security Best Practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html)

---

## 📊 Incident Metrics

| Metric | Value |
|--------|-------|
| Time to Detect | 15 minutes (via automated scan) |
| Time to Acknowledge | 1 minute |
| Time to Remediate | 8 minutes |
| Total Public Exposure | 15 minutes |
| Data Accessed (Unauthorized) | 0 bytes |
| Sensitive Data Exposed | None |
| Compliance Impact | None |
| Cost Impact | $0 |
| Recurrence | None (prevention in place) |

---

## ✅ Follow-up Actions

- [x] Remediate public bucket (Completed: 2024-12-18 10:36)
- [x] Enable account-wide public access block (Completed: 2024-12-18 10:45)
- [x] Check CloudTrail for unauthorized access (Completed: 2024-12-18 10:40)
- [x] Document incident (Completed: 2024-12-18 11:00)
- [x] Update security audit frequency (Completed: 2024-12-18)
- [x] Separate test/prod buckets (Completed: 2024-12-19)
- [ ] Implement AWS Config rules (Planned: Week of 2024-12-23)
- [ ] Enable S3 access logging (Planned: Week of 2024-12-23)
- [ ] Team training on S3 security (N/A - solo lab)

---

## 🔔 Notifications Sent

- [x] Email alert from security audit script
- [x] Logged to incident tracking system
- [x] Updated portfolio documentation

*Note: No customer/user notifications required as this is a personal lab with no external users*

---

## 👤 Incident Owner

**Name:** Charles Bucher  
**Role:** CloudOps Lab Owner  
**Contact:** quietopscb@gmail.com  

---

## 📝 Additional Notes

### Compliance Considerations:
- **GDPR:** N/A (no EU data)
- **HIPAA:** N/A (no healthcare data)
- **PCI-DSS:** N/A (no payment card data)
- **SOC 2:** N/A (personal lab)

### Breach Notification:
Not required - no sensitive data, no unauthorized access, personal lab environment.

### Portfolio Value:
This incident demonstrates:
1. Automated security monitoring
2. Rapid incident response
3. Proper investigation methodology
4. Prevention-focused mindset
5. Professional documentation

Even though I caused this (learning exercise), the response process shows real operational skills that translate to production environments.

---

**Document Version:** 1.0  
**Last Updated:** 2024-12-18  
**Next Review:** After next security audit or Q1 2025  
**Incident Classification:** Security - Unauthorized Data Exposure (Potential)