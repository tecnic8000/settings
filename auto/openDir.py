import os
import subprocess

# List of directories you want to open
directories = [
    r"C:\path\to\directory1",
    r"C:\path\to\directory2",
    r"C:\path\to\directory3"
]

# Loop through each directory and open it
for directory in directories:
    if os.path.exists(directory):
        subprocess.Popen(f'explorer "{directory}"')
    else:
        print(f"Directory not found: {directory}")