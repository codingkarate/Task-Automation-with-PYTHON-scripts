import os
import shutil

# Change this to your actual Downloads path
source_folder = os.path.expanduser("~/Downloads")

# Destination folders
destination_map = {
    'Documents/PDFs': ['.pdf'],
    'Pictures/Images': ['.jpg', '.jpeg', '.png'],
    'Archives': ['.zip', '.rar'],
    'Misc': []  # Anything else
}


# Create destination folders if not exist
for folder in destination_map:
    dest_path = os.path.expanduser(f"~/{folder}")
    os.makedirs(dest_path, exist_ok=True)