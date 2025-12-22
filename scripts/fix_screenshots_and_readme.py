import os
import re

# -------------------------------
# Configuration
# -------------------------------
base_path = r"C:\Users\buche\docs\Desktop\REPOS\AWS_Error_Driven_Troubleshooting_Lab\incidents"

incident_folders = {
    "001-ec2-ssh-lockout": [
        "001_01_vpc_creation.png",
        "001_02_subnets.png",
        "001_03_route_tables.png",
        "001_04_security_groups.png",
        "001_05_ec2_instances.png",
        "001_06_storage_gateway.png"
    ],
    "002-s3-public-bucket": [
        "002_01_deploy_s3_bucket.png",
        "002_02_bucket_misconfig.png",
        "002_03_collect_evidence.png",
        "002_04_full_workflow.png",
        "002_05_validate_public_access.png"
    ],
    "003-lambda-timeout": [
        "003_01_lambda_deploy.png",
        "003_02_invoke_timeout.png",
        "003_03_collect_logs.png",
        "003_04_fix_configuration.png",
        "003_05_validate_lambda.png"
    ],
    "004-lambda-timeout": [
        "004_01_lambda_deploy.png",
        "004_02_trigger_error.png",
        "004_03_collect_evidence.png",
        "004_04_remediate_issue.png",
        "004_05_validation.png"
    ]
}

# -------------------------------
# Rename screenshots
# -------------------------------
for incident, new_names in incident_folders.items():
    folder_path = os.path.join(base_path, incident)
    files_to_rename = []

    # Flatten nested screenshots folders if present
    for root, dirs, files in os.walk(folder_path):
        for f in files:
            if f.lower().endswith((".png", ".jpg")):
                files_to_rename.append(os.path.join(root, f))

    # Sort files to maintain intended order
    files_to_rename.sort()

    for i, old_path in enumerate(files_to_rename):
        if i >= len(new_names):
            break
        new_path = os.path.join(folder_path, new_names[i])
        os.rename(old_path, new_path)
        print(f"Renamed: {old_path} -> {new_path}")

# -------------------------------
# Update README.md links
# -------------------------------
for incident, new_names in incident_folders.items():
    readme_path = os.path.join(base_path, incident, "README.md")
    if not os.path.exists(readme_path):
        continue

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace old image filenames that start with incident number with new names
    for new_name in new_names:
        pattern = re.compile(rf"{new_name[:7]}.*?\.png", re.IGNORECASE)
        content = pattern.sub(new_name, content)

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Updated README links in {incident}")

print("All screenshots renamed and README links updated!")
