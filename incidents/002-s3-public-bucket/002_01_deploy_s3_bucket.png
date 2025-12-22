INCIDENT REPORT: incident_002_s3_permission
Incident Summary
Incident ID: INC-002-S3-PERM
Date: December 14, 2025
Severity: High
Status: Resolved
Resolution Time: 47 minutes
Customer reported inability to access critical data files in AWS S3 bucket prod-customer-uploads after deploying IAM policy updates. Production application returned 403 Forbidden errors causing service degradation affecting 250+ active users. Issue isolated to misconfigured S3 bucket policy blocking legitimate CloudFront distribution access.

Symptoms

Primary: Application throwing AccessDenied (403) errors when fetching objects from S3 bucket
Secondary: CloudFront distribution returning cached content only; new uploads inaccessible
User Impact: File upload feature completely unavailable; existing files loading intermittently
Monitoring Alerts: CloudWatch alarm triggered for elevated 4xx error rate (23% above baseline)
Affected Services: Web application frontend, mobile app API endpoints, customer file retrieval system


Triage Steps
Initial Assessment (5 minutes)

Verified incident scope via AWS CloudWatch metrics - isolated to S3 GET requests
Confirmed application logs showing Access Denied errors with S3 API calls
Checked AWS Service Health Dashboard - no regional S3 outages reported
Validated IAM user credentials still active - no expiration or deactivation

Diagnostic Actions (15 minutes)

Reviewed recent IAM policy changes deployed 52 minutes prior to incident
Tested direct S3 bucket access via AWS CLI - successfully authenticated
Examined S3 bucket policy JSON for permission conflicts
Identified CloudFront OAI (Origin Access Identity) missing from bucket policy AllowedPrincipals
Cross-referenced CloudFront distribution configuration against bucket policy whitelist

Verification Testing (8 minutes)

Created test object in affected bucket via console - upload successful
Attempted retrieval via CloudFront URL - 403 error confirmed
Checked S3 server access logs for request patterns and IAM principal identifiers


Evidence Collected
CloudWatch Logs (Timestamp: 14:23 UTC)
{
  "errorCode": "AccessDenied",
  "errorMessage": "Access Denied",
  "requestId": "7X9K2PM4FJ8W",
  "s3Bucket": "prod-customer-uploads",
  "sourceIPAddress": "52.84.xxx.xxx" (CloudFront)
}
IAM Policy Change Log:

Deployment timestamp: 13:31 UTC
Change: Updated bucket policy to restrict access to specific IAM roles
Oversight: CloudFront OAI EOAI32XX not included in updated Principal list

S3 Bucket Policy Issue:

Missing Statement allowing CloudFront Origin Access Identity
Explicit Deny rule taking precedence over IAM role permissions
No condition clause for CloudFront service principal


Root Cause
Primary Cause:
During routine IAM policy hardening, S3 bucket policy was updated to restrict access to specific IAM roles for enhanced security. The deployment script failed to preserve the existing CloudFront Origin Access Identity (OAI) in the allowed Principals list, effectively blocking all CloudFront-originated requests to the bucket.
Contributing Factors:

Deployment automation lacked validation check for CloudFront OAI preservation
No staging environment test of policy changes against production traffic patterns
Insufficient peer review of IAM policy changes before production deployment
CloudFront cache masking initial impact for 15-20 minutes until cache expiration


Resolution
Immediate Fix (12 minutes)

Added CloudFront OAI arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity EOAI32XX to S3 bucket policy Principal list
Deployed corrected bucket policy via AWS CLI for immediate effect
Verified policy propagation across all S3 availability zones (2-3 minute delay)
Invalidated CloudFront cache paths /* to clear error responses

Validation (7 minutes)

Tested file uploads through application interface - successful
Confirmed 403 error rate returned to baseline (<0.1%)
Monitored CloudWatch for 5 minutes - no recurring errors
Received user confirmation that file access restored

Resolution Timeline:

Detection to acknowledgment: 3 minutes
Acknowledgment to root cause: 20 minutes
Root cause to resolution: 12 minutes
Validation and monitoring: 12 minutes
Total incident duration: 47 minutes


Lessons Learned
What Went Well

Monitoring alerts detected issue within 3 minutes of user impact
CloudWatch logs provided clear error patterns for rapid diagnosis
Team followed incident response runbook systematically
Rollback plan available if resolution failed

What Needs Improvement

Pre-Deployment Validation: Implement automated policy validation checking for CloudFront OAI presence
Testing Gaps: Create staging environment with production-mirrored CloudFront configuration
Documentation: Update IAM policy change checklist to include CDN integration dependencies
Automation: Build Terraform/CloudFormation template with CloudFront OAI as mandatory parameter

Action Items
ActionOwnerPriorityDue DateCreate IAM policy validation script for OAI checkDevOps TeamHighDec 18, 2025Update deployment runbook with CDN validation stepsCloud SupportHighDec 16, 2025Implement staging environment for policy testingInfrastructureMediumJan 15, 2026Conduct team training on S3-CloudFront dependenciesTeam LeadMediumDec 30, 2025
Skills Demonstrated

AWS S3 bucket policy troubleshooting and IAM permission management
CloudFront CDN integration and Origin Access Identity configuration
CloudWatch monitoring and log analysis for incident detection
Systematic incident response following industry best practices
Root cause analysis and documentation for knowledge base


Report Prepared By: Cloud Support Engineer
Date: December 14, 2025
Keywords: AWS S3, CloudFront, IAM, permissions, Access Denied, 403 error, bucket policy, OAI, incident response, troubleshooting, cloud supportClaude is AI and can make mistakes. Please double-check responses. Sonnet 4.5Claude is AI and can ma