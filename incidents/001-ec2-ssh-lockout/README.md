# Incident 001: EC2 SSH Lockout

**Incident ID:** INC-001  
**Date:** 2024-12-15  
**Severity:** P2 (High)  
**Status:** ✅ Resolved  
**Duration:** 12 minutes  

---

## 📋 Summary

Locked myself out of EC2 instance after accidentally modifying security group inbound rules, removing SSH access (port 22). Unable to connect via SSH to perform routine maintenance.

**Impact:** Loss of SSH access to production-like lab instance. No other services affected.

---

## ⏱️ Timeline

| Time (EST) | Event |
|------------|-------|
| 14:32 | Modified security group while testing new rules |
| 14:34 | SSH connection attempt failed |
| 14:35 | Realized security group modification removed SSH access |
| 14:36 | Began investigation using AWS Console |
| 14:38 | Identified missing SSH inbound rule |
| 14:40 | Added SSH rule back with restricted IP |
| 14:42 | Verified SSH access restored |
| 14:44 | Documented incident and prevention steps |

**Total Duration:** 12 minutes from detection to resolution

---

## 🔍 Root Cause Analysis

### What Happened:
While testing security group modifications in AWS Console, I accidentally replaced all inbound rules instead of adding to them. The security group went from:

**Before:**
```
Inbound Rules:
- SSH (22) from MY_IP/32
- HTTP (80) from 0.0.0.0/0
```

**After (Broken):**
```
Inbound Rules:
- HTTP (80) from 0.0.0.0/0
```

**Result:** SSH rule was completely removed.

### Why It Happened:
- Used "Edit inbound rules" and inadvertently deleted the SSH rule
- Did not verify rules before saving
- No confirmation step in AWS Console for rule deletion

### Contributing Factors:
- Lack of systematic change process
- No pre-change checklist
- No backup access method (should have used Session Manager)

---

## 🔧 Resolution Steps

### 1. Confirmed the Problem
```bash
# SSH connection attempt
ssh -i ~/.ssh/my-key.pem ec2-user@54.123.45.67

# Result: Connection timeout (not refused, indicating firewall/SG issue)
```

### 2. Checked Security Group in Console
- Navigated to EC2 → Security Groups
- Found security group sg-0123abc
- Confirmed SSH (port 22) rule was missing

**Screenshot:** Security group showing only HTTP rule

### 3. Added SSH Rule Back
```bash
# Using AWS CLI to restore access
aws ec2 authorize-security-group-ingress \
    --group-id sg-0123abc \
    --protocol tcp \
    --port 22 \
    --cidr 203.0.113.45/32 \
    --description "SSH access from my IP"
```

### 4. Verified Connection
```bash
# SSH now works
ssh -i ~/.ssh/my-key.pem ec2-user@54.123.45.67
```

**Result:** ✅ SSH access restored

---

## 📸 Evidence

### Before Fix:
![Security Group - Broken](../docs/screenshots/incidents/001-sg-before-fix.png)
*Security group missing SSH rule*

### After Fix:
![Security Group - Fixed](../docs/screenshots/incidents/001-sg-after-fix.png)
*SSH rule restored with proper IP restriction*

### CloudWatch Logs:
![Connection Timeouts](../docs/screenshots/incidents/001-connection-attempts.png)
*Failed SSH connection attempts in VPC Flow Logs*

---

## 🛡️ Prevention Strategies

### Implemented:

1. **Created Backup Access Method**
   - Enabled AWS Systems Manager Session Manager
   - Can now access instance even without SSH
   ```bash
   aws ssm start-session --target i-0123456789abcdef
   ```

2. **Documented Security Group Baseline**
   - Created `docs/security-group-baseline.md`
   - Lists required rules for each instance type

3. **Created Pre-Change Checklist**
   - Review current rules before editing
   - Take screenshot of current state
   - Verify changes before applying
   - Test access immediately after change

4. **Automated Security Group Backup**
   ```python
   # scripts/backup_security_groups.py
   # Runs daily, saves SG configurations to S3
   ```

5. **Added CloudWatch Alarm**
   - Alerts if SSH connection attempts fail repeatedly
   - Helps detect lockouts faster

### Future Improvements:

- [ ] Implement Infrastructure as Code (Terraform/CloudFormation) for security groups
- [ ] Add approval process for security group changes
- [ ] Create automated testing of critical ports after changes
- [ ] Set up secondary SSH key on instance

---

## 📚 Lessons Learned

### What Went Well:
✅ Quickly identified the issue (security group)  
✅ Had AWS CLI access to fix remotely  
✅ Documented the entire process  
✅ Implemented multiple prevention measures  

### What Could Be Better:
❌ Should have verified rules before saving changes  
❌ Didn't have backup access method initially  
❌ No pre-change checklist in place  
❌ Security group changes not version controlled  

### Key Takeaways:
1. **Always verify** before applying security group changes
2. **Multiple access methods** are critical (SSH + Session Manager)
3. **Document everything** - this incident documentation helped me improve
4. **Automation prevents human error** - considering IaC for SGs

---

## 🔗 Related Resources

### Runbook:
- [RB-001: EC2 SSH Lockout Response](../../docs/runbooks/RB-001-EC2-SSH-Lockout.md)

### Scripts:
- `scripts/backup_security_groups.py` - Backup SG configurations
- `scripts/restore_security_group.py` - Restore from backup
- `scripts/verify_security_groups.py` - Audit current SGs

### Documentation:
- `docs/security-group-baseline.md` - Required SG rules
- `docs/change-management.md` - Change process checklist

### AWS Documentation:
- [Security Groups for EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)
- [Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html)

---

## 📊 Incident Metrics

| Metric | Value |
|--------|-------|
| Time to Detect | 2 minutes |
| Time to Identify Root Cause | 4 minutes |
| Time to Resolution | 12 minutes |
| Services Affected | 1 (EC2) |
| Users Affected | 1 (me) |
| Data Loss | None |
| Cost Impact | $0 |
| Recurrence | None since prevention implemented |

---

## ✅ Follow-up Actions

- [x] Restore SSH access (Completed: 2024-12-15)
- [x] Document incident (Completed: 2024-12-15)
- [x] Enable Session Manager (Completed: 2024-12-15)
- [x] Create security group backup script (Completed: 2024-12-16)
- [x] Add CloudWatch alarm for SSH failures (Completed: 2024-12-16)
- [x] Create runbook for future incidents (Completed: 2024-12-16)
- [ ] Migrate security groups to Terraform (Planned: Q1 2025)
- [ ] Implement change approval workflow (Planned: Q1 2025)

---

## 👤 Incident Owner

**Name:** Charles Bucher  
**Role:** CloudOps Lab Owner  
**Contact:** quietopscb@gmail.com  

---

## 📝 Additional Notes

This was my first "real" incident in the lab. Even though I caused it intentionally as a learning exercise initially, I did actually lock myself out accidentally once while testing. The recovery process taught me:

1. **Always have a backup** - Session Manager saved me
2. **Document everything** - This template helps for future incidents
3. **Prevention > Cure** - The prevention measures have stopped this from happening again
4. **Learn from mistakes** - This incident made me a better engineer

This incident documentation follows AWS Well-Architected Framework operational excellence principles and is part of my portfolio demonstrating incident response skills.

---

**Document Version:** 1.0  
**Last Updated:** 2024-12-15  
**Next Review:** Quarterly or after recurrence