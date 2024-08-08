
import os
import shutil
from tqdm import tqdm

def find_external_drive(drive_label):
    mount_point = f"/Volumes/{drive_label}"
    if os.path.exists(mount_point):
        return mount_point
    return None

def copy_folder_to_external_drive(source_folder, drive_label):
    try:
        # Find the external drive
        destination_folder = find_external_drive(drive_label)
        
        if not destination_folder:
            print(f"Could not find a drive with the label '{drive_label}'.")
            return
        
        destination_path = os.path.join(destination_folder, os.path.basename(source_folder))
        
        # Ensure the destination folder does not already exist
        if os.path.exists(destination_path):
            print(f"The destination folder '{destination_path}' already exists on the thumb drive.")
            return
        
        # Walk through the source folder
        total_files = sum([len(files) for _, _, files in os.walk(source_folder)])
        with tqdm(total=total_files, desc="Copying files", unit="file") as pbar:
            for root, dirs, files in os.walk(source_folder):
                relative_path = os.path.relpath(root, source_folder)
                destination_dir = os.path.join(destination_path, relative_path)
                os.makedirs(destination_dir, exist_ok=True)
                
                for file in files:
                    source_file = os.path.join(root, file)
                    destination_file = os.path.join(destination_dir, file)
                    shutil.copy2(source_file, destination_file)
                    pbar.update(1)
        
        print(f"Folder '{source_folder}' has been successfully copied to '{destination_path}'.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    source = "/Users/minhhoangtran/Library/Application Support/Blender/4.2"
    drive_label = "32GB-USB2"
    copy_folder_to_external_drive(source, drive_label)