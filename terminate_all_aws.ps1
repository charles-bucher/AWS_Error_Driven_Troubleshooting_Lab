# terminate_all_aws.ps1
Import-Module AWSPowerShell.NetCore

# Optional: Set your default region
$Region = "us-east-1"

Write-Host "Starting AWS cleanup in region $Region..."

# Terminate all EC2 instances
$instances = Get-EC2Instance -Region $Region
foreach ($i in $instances.Instances) {
    Write-Host "Terminating instance $($i.InstanceId)..."
    Remove-EC2Instance -InstanceId $i.InstanceId -Force -Region $Region
}

# Delete key pairs
$keyPairs = Get-EC2KeyPair -Region $Region
foreach ($k in $keyPairs) {
    Write-Host "Deleting key pair $($k.KeyName)..."
    Remove-EC2KeyPair -KeyName $k.KeyName -Region $Region
}

# Delete security groups (except default)
$sgs = Get-EC2SecurityGroup -Region $Region | Where-Object { $_.GroupName -ne "default" }
foreach ($sg in $sgs) {
    Write-Host "Deleting security group $($sg.GroupName)..."
    Remove-EC2SecurityGroup -GroupId $sg.GroupId -Region $Region
}

# Detach and delete Internet Gateways
$vpcs = Get-EC2Vpc -Region $Region
foreach ($vpc in $vpcs) {
    $igws = Get-EC2InternetGateway -Region $Region | Where-Object { $_.Attachments.VpcId -eq $vpc.VpcId }
    foreach ($igw in $igws) {
        Write-Host "Detaching and deleting IGW $($igw.InternetGatewayId)..."
        Remove-EC2InternetGateway -InternetGatewayId $igw.InternetGatewayId -VpcId $vpc.VpcId -Region $Region
    }
}

# Delete subnets
foreach ($vpc in $vpcs) {
    $subnets = Get-EC2Subnet -Filter @{ Name="vpc-id"; Values=$vpc.VpcId } -Region $Region
    foreach ($subnet in $subnets) {
        Write-Host "Deleting subnet $($subnet.SubnetId)..."
        Remove-EC2Subnet -SubnetId $subnet.SubnetId -Region $Region
    }
}

# Delete VPCs
foreach ($vpc in $vpcs) {
    Write-Host "Deleting VPC $($vpc.VpcId)..."
    Remove-EC2Vpc -VpcId $vpc.VpcId -Force -Region $Region
}

Write-Host "AWS cleanup complete."
