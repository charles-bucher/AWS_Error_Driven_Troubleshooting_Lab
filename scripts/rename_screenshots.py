import os

# Map of folder paths to their target screenshot names
incident_screenshots = {
    r"C:\Users\buche\docs\Desktop\REPOS\AWS_Error_Driven_Troubleshooting_Lab\incidents\001-ec2-ssh-lockout": [
        "001_01_vpc_creation.png",
        "001_02_subnets.png",
        "001_03_route_tables.png",
        "001_04_security_groups.png",
        "001_05_ec2_instances.png",
        "001_06_storage_gateway.png"
    ],
    r"C:\Users\buche\docs\Desktop\REPOS\AWS_Error_Driven_Troubleshooting_Lab\incidents\002-s3-public-bucket": [
        "002_01_deploy_s3_bucket.png",
        "002_02_bucket_misconfig.png",
        "002_03_collect_evidence.png",
        "002_04_full_workflow.png",
        "002_05_validate_public_access.png"
    ],
    r"C:\Users\buche\docs\Desktop\REPOS\AWS_Error_Driven_Troubleshooting_Lab\incidents\003-lambda-timeout": [
        "003_01_lambda_deploy.png",
        "003_02_invoke_timeout.png",
        "003_03_collect_logs.png",
        "003_04_fix_configuration.png",
        "003_05_validate_lambda.png"
    ],
    r"C:\Users\buche\docs\Desktop\REPOS\AWS_Error_Driven_Troubleshooting_Lab\incidents\004-lambda-timeout": [
        "004_01_lambda_deploy.png",
        "004_02_trigger_error.png",
        "004_03_collect_evidence.png",
        "004_04_remediate_issue.png",
        "004_05_validation.png"
    ]
}

for folder, new_names in incident_screenshots.items():
    # List all files in folder
    files = sorted(os.listdir(folder))  # sort to match intended order
    for i, file in enumerate(files):
        # Skip if we already renamed more files than in new_names
        if i >= len(new_names):
            break
        old_path = os.path.join(folder, file)
        # Ensure extension is .png and lowercase
        new_path = os.path.join(folder, new_names[i].lower())
        print(f"Renaming '{old_path}' -> '{new_path}'")
        os.rename(old_path, new_path)

print("Renaming complete!")
