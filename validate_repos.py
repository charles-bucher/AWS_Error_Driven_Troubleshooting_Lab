import os
import re
import time

# ==========================
# AWS Cloud & Repo Validator
# ==========================
# Scans all repos in the folder
# Validates code files, incident structure, screenshots, and naming
# Gives rough hireability score
# ==========================

class RepoValidator:
    def __init__(self, base_path):
        self.base_path = base_path
        self.issues = []
        self.total_checks = 0
        self.passed_checks = 0

    def validate_repo_structure(self):
        print("\n--- Checking repo structure ---")
        required_folders = ["incidents", "lambdas", "scripts"]
        for folder in required_folders:
            path = os.path.join(self.base_path, folder)
            if not os.path.exists(path):
                self.issues.append(f"Missing folder: {folder}")
            else:
                self.passed_checks += 1
            self.total_checks += 1

    def validate_incidents(self):
        incidents_path = os.path.join(self.base_path, "incidents")
        if not os.path.exists(incidents_path):
            return

        print("\n--- Checking incidents ---")
        for incident in os.listdir(incidents_path):
            incident_folder = os.path.join(incidents_path, incident)
            if not os.path.isdir(incident_folder):
                continue
            scripts_path = os.path.join(incident_folder, "scripts")
            evidence_path = os.path.join(incident_folder, "evidence")

            # Scripts folder
            if not os.path.exists(scripts_path):
                self.issues.append(f"{incident}: Missing scripts folder")
            else:
                # Must have core scripts
                for script in ["break.py", "collect_evidence.py", "deploy.py", "remediate.py", "teardown.py"]:
                    script_path = os.path.join(scripts_path, script)
                    if not os.path.exists(script_path):
                        self.issues.append(f"{incident}: Missing {script}")
                    else:
                        self.passed_checks += 1
                    self.total_checks += 1

            # Evidence folder
            if not os.path.exists(evidence_path):
                self.issues.append(f"{incident}: Missing evidence folder")
            else:
                self.passed_checks += 1
            self.total_checks += 1

    def validate_screenshot_naming(self):
        screenshots_path = os.path.join(self.base_path, "screenshots")
        if not os.path.exists(screenshots_path):
            self.issues.append("Missing screenshots folder")
            return

        print("\n--- Checking screenshot naming ---")
        for filename in os.listdir(screenshots_path):
            if not re.match(r"^\d{2}_.+\.png$", filename):
                self.issues.append(f"Bad screenshot name: {filename}")
            else:
                self.passed_checks += 1
            self.total_checks += 1

    def validate_code_files(self):
        print("\n--- Checking Python code files ---")
        for root, dirs, files in os.walk(self.base_path):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        if "Your descriptive commit message" in content:
                        self.passed_checks += 1
                        self.total_checks += 1

    def calculate_hireability(self):
        print("\n--- Calculating hireability ---")
        if self.total_checks == 0:
            return 0
        score = (self.passed_checks / self.total_checks) * 100
        print(f"Hireability score (based on repo quality): {score:.2f}%")
        return score

    def run_all_validations(self):
        start_time = time.time()
        print("="*80)
        print("AWS Repo Validator Running...")
        print("="*80)

        self.validate_repo_structure()
        self.validate_incidents()
        self.validate_screenshot_naming()
        self.validate_code_files()
        score = self.calculate_hireability()

        print("\n--- Issues Found ---")
        if self.issues:
            for issue in self.issues:
                print(f"❌ {issue}")
        else:
            print("✅ No major issues detected!")

        print("\nValidation completed in {:.2f}s".format(time.time() - start_time))
        return score

# ==========================
# Entry point
# ==========================
if __name__ == "__main__":
    base_path = os.getcwd()  # REPOS folder root
    validator = RepoValidator(base_path)
    validator.run_all_validations()
