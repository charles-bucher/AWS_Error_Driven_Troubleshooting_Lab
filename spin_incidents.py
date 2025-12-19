import os, subprocess

INCIDENTS_DIR = "incidents"

def deploy_all():
    for incident in os.listdir(INCIDENTS_DIR):
        scripts = os.path.join(INCIDENTS_DIR, incident, "scripts")
        deploy = os.path.join(scripts, "deploy.py")
        if os.path.exists(deploy):
            print(f"Deploying {incident}...")
            subprocess.run(["python", deploy, incident, "terraform"], check=False)

if __name__ == "__main__":
    deploy_all()
