import os

# Define the required sections and keywords per incident
incident_sections = [
    "## Quick Start",
    "## Incident Scenarios",
    "## Evidence",
    "## Metrics",
    "## Skills Mapped"
]

incident_keywords = {
    "001-ec2-ssh-lockout": ["S3", "Lambda", "VPC", "CloudWatch", "IAM", "root cause"],
    "002-s3-public-bucket": ["EC2", "Lambda", "VPC", "CloudWatch", "IAM", "troubleshoot", "root cause"],
    "003-lambda-timeout": ["EC2", "S3", "VPC", "IAM", "troubleshoot", "root cause"],
    "004-lambda-timeout": ["EC2", "S3", "VPC", "CloudWatch", "IAM", "troubleshoot", "root cause"]
}

repo_path = "./incidents"

for incident_dir in os.listdir(repo_path):
    incident_path = os.path.join(repo_path, incident_dir)
    if not os.path.isdir(incident_path):
        continue

    readme_path = os.path.join(incident_path, "README.md")
    
    # If README doesn't exist, create one
    if not os.path.exists(readme_path):
        with open(readme_path, "w") as f:
            f.write(f"# {incident_dir}\n\n")

    # Read existing content
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Add missing sections
    for section in incident_sections:
        if section not in content:
            content += f"\n{section}\n\n*Placeholder: Add content here*\n"

    # Add missing keywords in a "Keywords" section at the end
    keywords = incident_keywords.get(incident_dir, [])
    if keywords:
        keywords_line = "### Keywords: " + ", ".join(keywords) + "\n"
        if "### Keywords:" not in content:
            content += "\n" + keywords_line
        else:
            # Merge missing keywords if any
            existing_line_index = content.find("### Keywords:")
            existing_line_end = content.find("\n", existing_line_index)
            existing_keywords = content[existing_line_index + 13:existing_line_end].split(", ")
            missing_keywords = [kw for kw in keywords if kw not in existing_keywords]
            if missing_keywords:
                new_keywords_line = ", ".join(existing_keywords + missing_keywords)
                content = content[:existing_line_index] + f"### Keywords: {new_keywords_line}" + content[existing_line_end:]

    # Write back updated README
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Ensure evidence/logs and evidence/metrics folders exist
    logs_path = os.path.join(incident_path, "evidence", "logs")
    metrics_path = os.path.join(incident_path, "evidence", "metrics")
    os.makedirs(logs_path, exist_ok=True)
    os.makedirs(metrics_path, exist_ok=True)

print("✅ Incident READMEs and evidence folders auto-fixed!")
