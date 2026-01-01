"""
Script Name: organize_by_extension.py
Description: This script organizes files by their extension.
Notes: It creates folders automatically and does not delete files.
Author: Marcos Filipe Batista de Almeida
Date: 2026-01-01
"""

import os
import shutil

# Folder where the files to be organized are located
target_folder = r"C:\Users\alexa\Downloads\programming\test_folder"

# Dictionary defining categories and corresponding extensions
file_types = {
    "Documents": ["pdf", "docx", "txt", "xlsx", "pptx"],
    "Images": ["jpg", "png"],
    "Audio": ["mp3", "wav"],
    "Video": ["mp4", "avi"],
    "Archives": ["zip", "rar"],
    "Scripts": ["py"]
}

# Loop through every item in the target folder
for file_name in os.listdir(target_folder):
    file_path = os.path.join(target_folder, file_name)   # Full path to the file

    if os.path.isdir(file_path):
        continue   # Ignore folders, only process files

    name, ext = os.path.splitext(file_name)
    ext = ext[1:].lower()  # Remove the dot and convert to lowercase

    print(name) # Debug: print file name
    print(ext)  # Debug: print file extension

    # Loop through categories to find the right one
    for category, extensions in file_types.items():
        if ext in extensions:
            dest_folder = os.path.join(target_folder, category)  # Destination folder
            os.makedirs(dest_folder, exist_ok=True)  # Create folder if it doesn't exist
            shutil.move(file_path, os.path.join(dest_folder, file_name))  # Move file
            break  # Stop checking categories once matched