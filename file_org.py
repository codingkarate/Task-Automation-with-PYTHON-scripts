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