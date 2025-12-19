import os

def create_incident(name):
    base = os.path.join("incidents", name)
    os.makedirs(os.path.join(base, "scripts"), exist_ok=True)
    os.makedirs(os.path.join(base, "evidence"), exist_ok=True)
    with open(os.path.join(base, "README.md"), "w") as f:
        f.write(f"# {name}\\n\\nIncident documentation placeholder.")

if __name__ == "__main__":
    incident_name = input("Enter incident folder name: ")
    create_incident(incident_name)
    print(f"Incident {incident_name} created.")
