# Incident 001: EC2 Instance Unreachable - Security Group Misconfiguration

## Executive Summary
**Incident ID:** INC-001-EC2-UNREACHABLE  
**Severity:** High (Production Service Disruption)  
**Detection Time:** 2024-12-14 09:15 UTC  
**Resolution Time:** 2024-12-14 09:47 UTC  
**Total Downtime:** 32 minutes  
**Status:** RESOLVED

Production web application became completely unreachable due to misconfigured EC2 Security Group blocking all inbound HTTP/HTTPS traffic. Root cause identified as unauthorized security group rule removal during maintenance window. Service restored through security group rule reinstatement and verification of network connectivity.

**Business Impact:**
- 100% service unavailability for external users
- Estimated 1,200+ failed connection attempts
- Customer-facing API endpoints down
- Zero data loss or corruption

---

## Symptoms

### Initial Alert
```
CloudWatch Alarm: EC2-WebServer-HealthCheck-FAILED
Instance ID: i-0abc123def456789
Region: us-east-1
Alarm State: ALARM → INSUFFICIENT_DATA
Time: 09:15:33 UTC
```

### User-Reported Issues
- Web application returning "Connection Timeout" errors
- Unable to establish TCP connection on ports 80 and 443
- API endpoint health checks failing across all monitoring services
- Mobile app showing "Cannot connect to server" messages

### Observable Behaviors
1. **EC2 Instance Status:** Running (2/2 checks passed internally)
2. **Network Connectivity:** No response to external HTTP/HTTPS requests
3. **SSH Access:** Accessible via bastion host on port 22 (internal VPC only)
4. **Application Logs:** No new connection attempts logged (confirms traffic not reaching instance)
5. **Load Balancer:** Target marked as "unhealthy" due to failed health checks

---

## Triage Steps

### Step 1: Instance Health Verification (09:16 - 09:19 UTC)
```bash
# Checked EC2 instance status
aws ec2 describe-instance-status --instance-ids i-0abc123def456789

# Result: Both status checks passing - instance itself is healthy
# Status Check 1: Passed (AWS infrastructure)
# Status Check 2: Passed (Instance OS/network)
```

**Findings:** Instance hardware and OS-level networking confirmed operational.

### Step 2: Application Layer Testing (09:20 - 09:24 UTC)
```bash
# SSH into instance via bastion host
ssh -i keypair.pem ec2-user@10.0.1.45

# Verify web server running
sudo systemctl status nginx
# Status: active (running)

# Test local HTTP response
curl localhost:80
# Result: 200 OK - Application responding correctly on localhost

# Check listening ports
sudo netstat -tlnp | grep nginx
# Result: nginx listening on 0.0.0.0:80 and 0.0.0.0:443
```

**Findings:** Application confirmed healthy and listening on correct ports. Issue isolated to external connectivity.

### Step 3: Network Layer Investigation (09:25 - 09:31 UTC)
```bash
# Test external connectivity from instance
ping 8.8.8.8
# Result: Successful - outbound internet access working

# Review VPC route tables
aws ec2 describe-route-tables --filters "Name=association.subnet-id,Values=subnet-abc123"
# Result: Routes appear correct, internet gateway attached

# Examine Network ACLs
aws ec2 describe-network-acls --network-acl-ids acl-xyz789
# Result: Default allow rules present - no blocking at NACL level
```

**Findings:** VPC networking configuration validated. Routing and NACLs not the culprit.

### Step 4: Security Group Analysis (09:32 - 09:38 UTC)
```bash
# Retrieve instance security groups
aws ec2 describe-instances --instance-ids i-0abc123def456789 \
  --query 'Reservations[].Instances[].SecurityGroups'

# Output: Security Group ID: sg-webserver-prod-001

# Inspect security group rules
aws ec2 describe-security-groups --group-ids sg-webserver-prod-001 \
  --query 'SecurityGroups[].IpPermissions'
```

**CRITICAL FINDING:**
```json
{
  "IpPermissions": [
    {
      "IpProtocol": "tcp",
      "FromPort": 22,
      "ToPort": 22,
      "IpRanges": [{"CidrIp": "10.0.0.0/16"}]
    }
  ]
}
```

**Root Cause Identified:** Security group missing inbound rules for ports 80 (HTTP) and 443 (HTTPS). Only SSH access from internal VPC allowed.

### Step 5: Change History Audit (09:39 - 09:42 UTC)
```bash
# Query CloudTrail for recent security group modifications
aws cloudtrail lookup-events \
  --lookup-attributes AttributeKey=ResourceName,AttributeValue=sg-webserver-prod-001 \
  --max-results 10
```

**Audit Trail Discovery:**
- **Event:** RevokeSecurityGroupIngress
- **Time:** 2024-12-14 08:45 UTC (30 minutes before incident)
- **User:** maintenance-automation-role
- **Action:** Removed rules for ports 80 and 443
- **Reason:** Automated cleanup script misconfigured during scheduled maintenance

---

## Evidence Collected

### 1. CloudWatch Metrics
- **CPUUtilization:** Steady at 12% (normal baseline)
- **NetworkIn:** Dropped to near-zero at 09:15 UTC
- **HTTPCode_Target_5XX_Count:** Zero (no application errors)
- **TargetResponseTime:** N/A (no connections reaching target)

### 2. VPC Flow Logs Analysis
```
2024-12-14 09:16:23 eni-abc123 203.0.113.45 10.0.1.45 54123 80 6 1 52 REJECT OK
2024-12-14 09:16:24 eni-abc123 198.51.100.78 10.0.1.45 43891 443 6 1 52 REJECT OK
```
**Interpretation:** External IPs attempting connection on ports 80/443 rejected at security group level.

### 3. Security Group Configuration Backup
```json
// Correct configuration (from backup taken 2024-12-13):
{
  "IpPermissions": [
    {
      "IpProtocol": "tcp",
      "FromPort": 80,
      "ToPort": 80,
      "IpRanges": [{"CidrIp": "0.0.0.0/0"}]
    },
    {
      "IpProtocol": "tcp",
      "FromPort": 443,
      "ToPort": 443,
      "IpRanges": [{"CidrIp": "0.0.0.0/0"}]
    },
    {
      "IpProtocol": "tcp",
      "FromPort": 22,
      "ToPort": 22,
      "IpRanges": [{"CidrIp": "10.0.0.0/16"}]
    }
  ]
}
```

### 4. Application Logs
```
[2024-12-14 09:14:57] INFO: Request from 203.0.113.45 - 200 OK - /api/health
[2024-12-14 09:15:33] INFO: Last successful request
[2024-12-14 09:15:34 - 09:47:00] NO INCOMING CONNECTIONS
[2024-12-14 09:47:12] INFO: Request from 203.0.113.45 - 200 OK - /api/health
```

### 5. Screenshots & Diagrams
- Network topology diagram showing security group placement
- CloudWatch dashboard showing traffic drop
- CloudTrail event JSON for unauthorized change

---

## Root Cause

**Primary Cause:** Automated maintenance script incorrectly removed critical security group ingress rules.

**Contributing Factors:**
1. **Inadequate Script Validation:** Maintenance automation lacked dry-run mode or approval gate
2. **Missing Change Control:** Security group modifications not subject to change approval process
3. **Insufficient Monitoring:** No alerting configured for security group rule changes
4. **Lack of Testing:** Script not tested in non-production environment before production deployment

**Why Issue Occurred:**
The maintenance automation role was granted overly broad `ec2:RevokeSecurityGroupIngress` permissions. A Python script designed to clean up unused security group rules contained a logic error that evaluated the production web server security group as "unused" because it matched deprecated naming patterns. The script executed during the scheduled 08:30 UTC maintenance window without human review.

---

## Resolution

### Immediate Actions (09:43 - 09:47 UTC)

**Step 1: Restore Security Group Rules**
```bash
# Add HTTP ingress rule
aws ec2 authorize-security-group-ingress \
  --group-id sg-webserver-prod-001 \
  --protocol tcp \
  --port 80 \
  --cidr 0.0.0.0/0

# Add HTTPS ingress rule
aws ec2 authorize-security-group-ingress \
  --group-id sg-webserver-prod-001 \
  --protocol tcp \
  --port 443 \
  --cidr 0.0.0.0/0
```

**Step 2: Verify Connectivity**
```bash
# External connectivity test
curl -I https://webapp.example.com
# Result: HTTP/1.1 200 OK

# Load balancer health check
aws elbv2 describe-target-health --target-group-arn arn:aws:elasticloadbalancing:...
# Result: Target state = healthy
```

**Step 3: Confirm Service Restoration**
- CloudWatch alarms returned to OK state
- User reports of connectivity restored
- Application logs showing incoming connections resuming
- Service fully operational at 09:47 UTC

### Temporary Workarounds
None required - full service restoration achieved.

---

## Preventive Measures Implemented

### 1. IAM Policy Restrictions (Completed 2024-12-14)
```json
// Updated maintenance-automation-role policy
{
  "Effect": "Deny",
  "Action": [
    "ec2:RevokeSecurityGroupIngress",
    "ec2:RevokeSecurityGroupEgress"
  ],
  "Resource": "arn:aws:ec2:*:*:security-group/sg-*prod*"
}
```

### 2. AWS Config Rules (Deployed 2024-12-14)
- **Rule:** `required-security-group-rules`
- **Trigger:** On security group configuration change
- **Action:** Auto-remediate if HTTP/HTTPS rules removed from production security groups

### 3. EventBridge Monitoring (Configured 2024-12-14)
```json
{
  "source": ["aws.ec2"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventName": ["RevokeSecurityGroupIngress", "RevokeSecurityGroupEgress"],
    "requestParameters": {
      "groupId": [{"prefix": "sg-"}]
    }
  }
}
```
- **Action:** Immediate SNS alert to operations team + Slack notification

### 4. Infrastructure as Code Enforcement (In Progress)
- Migrating all security groups to Terraform management
- Security group changes require pull request review + approval
- Automated testing in staging environment before production deployment

### 5. Enhanced Documentation
- Created runbook: "EC2 Connectivity Troubleshooting Guide"
- Added security group baseline configurations to wiki
- Documented rollback procedures for network changes

---

## Lessons Learned

### What Went Well ✅
1. **Systematic Troubleshooting:** Methodical approach quickly isolated issue to network layer
2. **Rapid Response:** 32-minute resolution time met SLA targets
3. **Clear Communication:** Stakeholders kept informed throughout incident
4. **Audit Trail:** CloudTrail provided complete change history for root cause analysis
5. **Zero Data Loss:** Instance-level health meant no application data compromised

### What Could Be Improved 🔧
1. **Change Control Gaps:** Automated scripts bypassed approval processes
2. **Delayed Detection:** 15-minute gap between change and alarm could be shortened
3. **Documentation:** Security group baseline not version-controlled or easily accessible
4. **Monitoring Coverage:** No proactive alerts on security group modifications
5. **Testing Procedures:** Automation scripts lacked pre-production validation

### Action Items

| Item | Owner | Priority | Due Date | Status |
|------|-------|----------|----------|--------|
| Implement security group change alerts | CloudOps | P0 | 2024-12-15 | ✅ Complete |
| Deploy AWS Config auto-remediation | Security | P0 | 2024-12-16 | ✅ Complete |
| Migrate to Terraform for SGs | Infrastructure | P1 | 2024-12-30 | 🔄 In Progress |
| Audit all automation scripts | DevOps | P1 | 2024-12-22 | 🔄 In Progress |
| Create EC2 troubleshooting runbook | Documentation | P2 | 2024-12-28 | ⏳ Planned |
| Review IAM permissions org-wide | Security | P2 | 2025-01-15 | ⏳ Planned |

---

## Related Documentation
- [AWS Security Group Best Practices](./docs/security-groups.md)
- [Incident Response Playbook](./docs/incident-response.md)
- [EC2 Troubleshooting Runbook](./docs/ec2-troubleshooting.md)
- [Change Management Policy](./docs/change-management.md)

## Technical Skills Demonstrated
`AWS EC2` `VPC Networking` `Security Groups` `CloudWatch` `CloudTrail` `VPC Flow Logs` `AWS CLI` `Incident Response` `Root Cause Analysis` `Linux Systems Administration` `Network Troubleshooting` `IAM Policy Management` `Infrastructure as Code` `AWS Config` `EventBridge` `Load Balancing`

---

**Incident Owner:** Charles Bucher  
**Last Updated:** 2025-12-14  
**Review Date:** 2026-01-14