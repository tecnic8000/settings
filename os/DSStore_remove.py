import os
import glob

def remove_ds_store_files(directory):
    # Use glob to find all .DS_Store files recursively
    ds_store_files = glob.glob(os.path.join(directory, '**', '.DS_Store'), recursive=True)
    
    # Remove each .DS_Store file found
    for file_path in ds_store_files:
        try:
            os.remove(file_path)
            print(f"Removed: {file_path}")
        except Exception as e:
            print(f"Error removing {file_path}: {e}")

# Specify the directory you want to clean
directory_path = '/path/to/your/directory'

remove_ds_store_files(directory_path)