# Variables
$stackName = "Incident002TempLab"
$templateFile = "C:\Users\buche\docs\Desktop\REPOS\AWS_Error_Driven_Troubleshooting_Lab\incident_002_temp.yaml"
$region = "us-east-1"

# Create CloudFormation stack
Write-Host "Creating Incident 002 temporary lab..."
aws cloudformation create-stack --stack-name $stackName --template-body file://$templateFile --region $region

# Wait for completion
Write-Host "Waiting for stack to complete..."
aws cloudformation wait stack-create-complete --stack-name $stackName --region $region
Write-Host "Stack created successfully! You can now test the environment and take screenshots."

# Instructions for tearing down
Write-Host "`nAfter taking screenshots, run the following to tear down:"
Write-Host "aws cloudformation delete-stack --stack-name $stackName --region $region"
Write-Host "aws cloudformation wait stack-delete-complete --stack-name $stackName --region $region"
