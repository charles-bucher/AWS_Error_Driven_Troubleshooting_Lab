# Runbook: EC2 SSH Lockout Response

**Runbook ID:** RB-INC-001  
**Last Updated:** 2024-12-15  
**Incident Type:** SSH Access Lost  
**Severity:** P2 (High)  
**Estimated Time:** 5-15 minutes  

---

## 📋 Overview

### Purpose
Step-by-step procedure to restore SSH access when locked out of EC2 instance due to security group misconfiguration.

### When to Use
- Cannot SSH to EC2 instance
- Connection times out (not refused)
- Recent security group changes
- Need immediate access to instance

### Prerequisites
- AWS CLI configured
- IAM permissions for EC2 and SSM
- Know instance ID and security group ID

---

## 🔍 Quick Diagnosis

### Symptom Check

**Try to connect:**
```bash
ssh -i ~/.ssh/your-key.pem ec2-user@INSTANCE_IP
```

**Possible outcomes:**
1. **Connection times out** → Likely security group issue (this runbook)
2. **Connection refused** → SSH service not running (different issue)
3. **Permission denied** → Key mismatch (different issue)
4. **Host key changed** → Instance replaced (different issue)

If **connection times out**, proceed with this runbook.

---

## 🚨 Step 1: Confirm Security Group Issue (2 min)

### Check Instance Status
```bash
# Get instance details
aws ec2 describe-instances \
    --instance-ids i-YOUR-INSTANCE-ID \
    --query 'Reservations[0].Instances[0].[State.Name,SecurityGroups[0].GroupId]' \
    --output text
```

**Expected output:** `running sg-XXXXXXXXX`

### Check Security Group Rules
```bash
# Get security group inbound rules
aws ec2 describe-security-groups \
    --group-ids sg-YOUR-GROUP-ID \
    --query 'SecurityGroups[0].IpPermissions[*].[IpProtocol,FromPort,ToPort,IpRanges[0].CidrIp]' \
    --output table
```

**Look for:** SSH rule (port 22) with your IP

**If missing → Security group issue confirmed**

---

## 🔧 Step 2: Choose Recovery Method

### Option A: Fix Security Group (Fastest - 2 min)
**Use when:** You have AWS CLI access and know your current IP

### Option B: Use Session Manager (5 min)
**Use when:** 
- Security group fix doesn't work
- Want to avoid touching security groups
- Session Manager already enabled

### Option C: Create New Security Group (10 min)
**Use when:**
- Cannot modify existing security group
- Original security group severely misconfigured
- Want clean slate

---

## 🔧 Option A: Fix Security Group (Recommended)

### Step 1: Get Your Current IP
```bash
# Get your public IP
MY_IP=$(curl -s ifconfig.me)
echo "My IP: $MY_IP"
```

### Step 2: Add SSH Rule
```bash
# Add SSH access for your IP
aws ec2 authorize-security-group-ingress \
    --group-id sg-YOUR-GROUP-ID \
    --protocol tcp \
    --port 22 \
    --cidr $MY_IP/32 \
    --description "SSH access from my current IP"
```

**Expected output:**
```json
{
    "Return": true,
    "SecurityGroupRules": [...]
}
```

### Step 3: Verify Rule Added
```bash
# Check rules again
aws ec2 describe-security-groups \
    --group-ids sg-YOUR-GROUP-ID \
    --query 'SecurityGroups[0].IpPermissions[?FromPort==`22`]'
```

### Step 4: Test SSH Connection
```bash
# Wait 10 seconds for rule to propagate
sleep 10

# Try SSH again
ssh -i ~/.ssh/your-key.pem ec2-user@INSTANCE_IP
```

**If successful:** ✅ Skip to Step 5: Verification

**If still failing:** Try Option B (Session Manager)

---

## 🔧 Option B: Use Session Manager

### Prerequisites Check
```bash
# Check if Session Manager is available
aws ssm describe-instance-information \
    --filters "Key=InstanceIds,Values=i-YOUR-INSTANCE-ID" \
    --query 'InstanceInformationList[0].PingStatus'
```

**Expected:** `"Online"`

**If Offline or not found:** Session Manager not configured. Use Option C.

### Connect via Session Manager
```bash
# Start session (opens interactive shell)
aws ssm start-session --target i-YOUR-INSTANCE-ID
```

**You're now connected to the instance!**

### Fix Security Group from Inside Instance
```bash
# From within Session Manager shell, get your IP
curl ifconfig.me

# Note your IP, then exit
exit
```

### Add SSH Rule (from your local terminal)
```bash
# Add rule with IP you just found
aws ec2 authorize-security-group-ingress \
    --group-id sg-YOUR-GROUP-ID \
    --protocol tcp \
    --port 22 \
    --cidr YOUR_IP/32
```

### Test SSH
```bash
ssh -i ~/.ssh/your-key.pem ec2-user@INSTANCE_IP
```

**If successful:** ✅ Skip to Step 5: Verification

---

## 🔧 Option C: Create New Security Group

### Step 1: Create Security Group
```bash
# Get VPC ID
VPC_ID=$(aws ec2 describe-instances \
    --instance-ids i-YOUR-INSTANCE-ID \
    --query 'Reservations[0].Instances[0].VpcId' \
    --output text)

# Create new security group
NEW_SG=$(aws ec2 create-security-group \
    --group-name "fixed-ssh-access-$(date +%Y%m%d)" \
    --description "Emergency SG with SSH access" \
    --vpc-id $VPC_ID \
    --query 'GroupId' \
    --output text)

echo "New SG: $NEW_SG"
```

### Step 2: Add SSH Rule
```bash
# Add SSH rule
MY_IP=$(curl -s ifconfig.me)
aws ec2 authorize-security-group-ingress \
    --group-id $NEW_SG \
    --protocol tcp \
    --port 22 \
    --cidr $MY_IP/32
```

### Step 3: Attach to Instance
```bash
# Stop instance (if required)
aws ec2 stop-instances --instance-ids i-YOUR-INSTANCE-ID
aws ec2 wait instance-stopped --instance-ids i-YOUR-INSTANCE-ID

# Change security group
aws ec2 modify-instance-attribute \
    --instance-id i-YOUR-INSTANCE-ID \
    --groups $NEW_SG

# Start instance
aws ec2 start-instances --instance-ids i-YOUR-INSTANCE-ID
aws ec2 wait instance-running --instance-ids i-YOUR-INSTANCE-ID
```

### Step 4: Get New IP and Test
```bash
# Get new public IP
NEW_IP=$(aws ec2 describe-instances \
    --instance-ids i-YOUR-INSTANCE-ID \
    --query 'Reservations[0].Instances[0].PublicIpAddress' \
    --output text)

echo "New IP: $NEW_IP"

# Test SSH
ssh -i ~/.ssh/your-key.pem ec2-user@$NEW_IP
```

---

## ✅ Step 5: Verification (2 min)

### Verify SSH Access
```bash
# Connect and run command
ssh -i ~/.ssh/your-key.pem ec2-user@INSTANCE_IP 'uptime'
```

**Expected:** Output showing system uptime

### Verify Security Group
```bash
# Confirm SSH rule exists
aws ec2 describe-security-groups \
    --group-ids sg-YOUR-GROUP-ID \
    --query 'SecurityGroups[0].IpPermissions[?FromPort==`22`]' \
    --output json
```

**Expected:** JSON showing SSH rule with your IP

### Document Access Details
```bash
# Save for reference
echo "Instance: i-YOUR-INSTANCE-ID" >> access_restored.txt
echo "Security Group: sg-YOUR-GROUP-ID" >> access_restored.txt
echo "SSH Rule Added: $(date)" >> access_restored.txt
echo "IP: $MY_IP" >> access_restored.txt
```

---

## 🛡️ Step 6: Prevention (5 min)

### Enable Session Manager (If Not Already)

**Install SSM Agent (if needed):**
```bash
# On Amazon Linux 2
sudo yum install -y amazon-ssm-agent
sudo systemctl enable amazon-ssm-agent
sudo systemctl start amazon-ssm-agent
```

**Attach IAM Role:**
```bash
# Create instance profile if needed
aws iam create-instance-profile --instance-profile-name SSM-Instance-Profile

# Attach managed policy
aws iam attach-role-policy \
    --role-name SSM-Instance-Role \
    --policy-arn arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
```

### Backup Security Group Config
```bash
# Save current configuration
aws ec2 describe-security-groups \
    --group-ids sg-YOUR-GROUP-ID \
    > sg-backup-$(date +%Y%m%d).json
```

### Create CloudWatch Alarm
```bash
# Alert on SSH connection failures
aws cloudwatch put-metric-alarm \
    --alarm-name "SSH-Access-Failed-i-YOUR-INSTANCE-ID" \
    --alarm-description "Alert when SSH connections fail" \
    --metric-name NetworkPacketsIn \
    --namespace AWS/EC2 \
    --statistic Sum \
    --period 300 \
    --threshold 10 \
    --comparison-operator LessThanThreshold \
    --evaluation-periods 2 \
    --dimensions Name=InstanceId,Value=i-YOUR-INSTANCE-ID
```

### Document Baseline
Create `security-group-baseline.md`:
```markdown
# Security Group: sg-YOUR-GROUP-ID

## Required Rules:
- SSH (22) from MY_IP/32
- HTTP (80) from 0.0.0.0/0 (if web server)
- HTTPS (443) from 0.0.0.0/0 (if web server)

## Change Process:
1. Review current rules
2. Take screenshot
3. Make changes
4. Test immediately
5. Document in Git

## Emergency Contact:
- AWS Account Owner: [email]
- Runbook: RB-INC-001
```

---

## 📊 Post-Incident Checklist

- [ ] SSH access restored and tested
- [ ] Security group configuration documented
- [ ] Session Manager verified working
- [ ] CloudWatch alarm created
- [ ] Incident report filed (see incident README)
- [ ] Prevention measures implemented
- [ ] Team notified (if team environment)
- [ ] Baseline configuration saved

---

## 🔍 Troubleshooting

### Issue: Security Group Rule Added But Still Can't Connect

**Check 1: Network ACLs**
```bash
# Get subnet NACLs
SUBNET_ID=$(aws ec2 describe-instances \
    --instance-ids i-YOUR-INSTANCE-ID \
    --query 'Reservations[0].Instances[0].SubnetId' \
    --output text)

aws ec2 describe-network-acls \
    --filters "Name=association.subnet-id,Values=$SUBNET_ID"
```

**Check 2: Route Table**
```bash
# Verify route to internet gateway
aws ec2 describe-route-tables \
    --filters "Name=association.subnet-id,Values=$SUBNET_ID"
```

**Check 3: Instance Has Public IP**
```bash
# Confirm public IP exists
aws ec2 describe-instances \
    --instance-ids i-YOUR-INSTANCE-ID \
    --query 'Reservations[0].Instances[0].PublicIpAddress'
```

### Issue: Your IP Changed

**Quick fix:**
```bash
# Remove old rule, add new one
OLD_IP="203.0.113.45"
NEW_IP=$(curl -s ifconfig.me)

aws ec2 revoke-security-group-ingress \
    --group-id sg-YOUR-GROUP-ID \
    --protocol tcp \
    --port 22 \
    --cidr $OLD_IP/32

aws ec2 authorize-security-group-ingress \
    --group-id sg-YOUR-GROUP-ID \
    --protocol tcp \
    --port 22 \
    --cidr $NEW_IP/32
```

### Issue: Multiple Security Groups Attached

```bash
# List all security groups on instance
aws ec2 describe-instances \
    --instance-ids i-YOUR-INSTANCE-ID \
    --query 'Reservations[0].Instances[0].SecurityGroups[*].[GroupId,GroupName]'

# Check each one for SSH rule
```

---

## 📚 Related Resources

### Incident Documentation
- [Incident 001 README](README.md) - Full incident report

### AWS Documentation
- [Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)
- [Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html)
- [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)

### Scripts
- `scripts/backup_security_groups.py`
- `scripts/restore_security_group.py`
- `scripts/verify_ssh_access.py`

---

## ⏱️ Time Estimates

| Step | Estimated Time |
|------|----------------|
| Diagnosis | 2 min |
| Option A (Fix SG) | 2 min |
| Option B (Session Manager) | 5 min |
| Option C (New SG) | 10 min |
| Verification | 2 min |
| Prevention | 5 min |
| **Total (Option A)** | **~10 min** |

---

## 💡 Pro Tips

1. **Always check your current IP** before adding rules:
   ```bash
   curl ifconfig.me
   ```

2. **Use /32 CIDR** for single IPs (not /24):
   ```
   ✅ 203.0.113.45/32  (single IP)
   ❌ 203.0.113.0/24   (256 IPs - too broad)
   ```

3. **Keep Session Manager enabled** as backup access

4. **Document your security groups** in Git

5. **Test changes immediately** after applying

---

**Runbook Owner:** Charles Bucher  
**Contact:** quietopscb@gmail.com  
**Review Frequency:** Quarterly or after each incident  
**Version:** 1.0