import os
import shutil

IMAGE_EXTENSIONS = ['.png', '.jpg', '.jpeg', '.gif']

def process_incidents(base_path):
    for root, dirs, files in os.walk(base_path):
        for file in files:
            file_path = os.path.join(root, file)
            name, ext = os.path.splitext(file_path)
            
            # Only normalize images
            if ext.lower() in IMAGE_EXTENSIONS:
                new_path = os.path.join(root, file.lower())
                if file_path != new_path:
                    os.rename(file_path, new_path)
                    print(f"Normalized image extension: {file_path} -> {new_path}")
            
            # Flattening: move everything up to the incident folder
            incident_folder = os.path.dirname(root) if root != base_path else root
            if os.path.dirname(file_path) != incident_folder:
                new_file_path = os.path.join(incident_folder, file)
                counter = 1
                while os.path.exists(new_file_path):
                    name_only, ext_only = os.path.splitext(file)
                    new_file_path = os.path.join(incident_folder, f"{name_only}_{counter}{ext_only}")
                    counter += 1
                shutil.move(file_path, new_file_path)
                print(f"Flattened: {file_path} -> {new_file_path}")
