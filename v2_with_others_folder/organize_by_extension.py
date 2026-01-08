"""
Script Name: organize_by_extension.py
Description: This script organizes files by their extension and handles files without extension.
Notes: It creates folders automatically, moves files safely, and sends files without extension to a dedicated folder.
Author: Marcos Filipe Batista de Almeida
Date: 2026-01-08
"""

import os
import shutil

# Folder where the files to be organized are located
target_folder = r"C:\path\to\your\folder"

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
    file_path = os.path.join(target_folder, file_name)

    # Ignore folders
    if os.path.isdir(file_path):
        continue

    name, ext = os.path.splitext(file_name)
    ext = ext[1:].lower()  # remove the dot

    moved = False

    # If file has extension, try to categorize
    if ext:
        for category, extensions in file_types.items():
            if ext in extensions:
                dest_folder = os.path.join(target_folder, category)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, file_name))
                moved = True
                break

    # If file was not moved (no extension or unknown extension)
    if not moved:
        others_folder = os.path.join(target_folder, "Others")
        os.makedirs(others_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(others_folder, file_name))
