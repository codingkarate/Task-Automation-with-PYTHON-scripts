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

# Go through all files in Downloads
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)
    if os.path.isfile(file_path):
        file_ext = os.path.splitext(filename)[1].lower()

        # Find matching folder
        moved = False
        for folder, extensions in destination_map.items():
            if file_ext in extensions:
                shutil.move(file_path, os.path.expanduser(f"~/{folder}/{filename}"))
                moved = True
                break

        # Move to Misc if no match
        if not moved:
            shutil.move(file_path, os.path.expanduser(f"~/Misc/{filename}"))


print("*** Files organized successfully!")