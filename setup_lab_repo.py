from pathlib import Path
import subprocess

# ---- 1️⃣ Terraform placeholders ----
terraform_files = {
    "provider.tf": """# Terraform provider placeholder
provider "aws" {
  region = "us-east-1"
}""",
    "versions.tf": """# Terraform versions placeholder
terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}"""
}

tf_dir = Path("terraform")
tf_dir.mkdir(exist_ok=True)
for filename, content in terraform_files.items():
    file_path = tf_dir / filename
    file_path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"Created {file_path}")

# ---- 2️⃣ Scripts placeholders ----
scripts_files = {
    "error_simulation.py": "# Placeholder for error simulation logic\n",
    "remediation.py": "# Placeholder for remediation scripts\n",
    "monitoring.py": "# Placeholder for monitoring scripts\n"
}

scripts_dir = Path("scripts")
scripts_dir.mkdir(exist_ok=True)
for filename, content in scripts_files.items():
    file_path = scripts_dir / filename
    file_path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"Created {file_path}")

# ---- 3️⃣ Lambda placeholder ----
lambda_dir = Path("lambdas")
lambda_dir.mkdir(exist_ok=True)
lambda_file = lambda_dir / "index.py"
lambda_content = """def handler(event, context):
    \"""
    Minimal AWS Lambda handler placeholder.
    \"""
    return {
        "statusCode": 200,
        "body": "Lambda placeholder executed successfully"
    }
"""
lambda_file.write_text(lambda_content.strip() + "\n", encoding="utf-8")
print(f"Created {lambda_file}")

# ---- 4️⃣ Docs skeletons ----
docs = {
    "architecture.md": "# Architecture Documentation\n\n- High-level architecture diagram placeholder\n- Components description\n- AWS services used\n",
    "deployment.md": "# Deployment Guide\n\n- Prerequisites\n- Deployment steps\n- Verification steps\n",
    "troubleshooting.md": "# Troubleshooting Guide\n\n- Common errors\n- How to reproduce\n- How to resolve\n",
    "setup.md": "# Setup Guide\n\n- Clone repo\n- Install dependencies\n- Configure environment\n- Run validator\n"
}

docs_dir = Path("docs")
docs_dir.mkdir(exist_ok=True)
for filename, content in docs.items():
    file_path = docs_dir / filename
    file_path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"Created {file_path}")

# ---- 5️⃣ Update .gitignore ----
gitignore = Path(".gitignore")
if gitignore.exists():
    current = gitignore.read_text()
else:
    current = ""

if "__pycache__/" not in current:
    with gitignore.open("a", encoding="utf-8") as f:
        f.write("\n__pycache__/\n")
    print("Updated .gitignore to ignore __pycache__/")

# ---- 6️⃣ Git add + commit ----
subprocess.run(["git", "add", "."], check=False)
subprocess.run(["git", "commit", "-m", "Add lab placeholders: Terraform, scripts, Lambda, docs"], check=False)
print("Committed all placeholders to git")

# ---- 7️⃣ Optional: run validator ----
# subprocess.run(["python", "aws_lab_validator.py"])
