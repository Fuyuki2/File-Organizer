import os
import shutil
import tkinter as tk
from tkinter import messagebox

file_type = {
    "image": ["jpg", "png", "jpeg"],
    "video": ["mp4", "mov", "avi"],
    "document": ["pdf", "docx", "txt"],
    "executable": ["exe", "msi"],
    "compressed": ["zip", "rar", "7z"],
    "code": ["py", "java", "cpp", "html", "css", "js"],
    "other": []
}

directory_path = os.getcwd()  # current folder where .exe is located

for file in os.listdir(directory_path):
    source_path = os.path.join(directory_path, file)

    if os.path.isdir(source_path) or file.startswith('.'):
        continue

    file_extension = os.path.splitext(file)[1][1:].lower()
    moved = False

    for category, extensions in file_type.items():
        if file_extension in extensions:
            directory_name = category.upper()
            os.makedirs(os.path.join(directory_path, directory_name),
                        exist_ok=True)
            shutil.move(source_path,
                        os.path.join(directory_path, directory_name, file))
            moved = True
            break

    if not moved:
        directory_name = "OTHER"
        os.makedirs(os.path.join(directory_path, directory_name),
                    exist_ok=True)
        shutil.move(source_path,
                    os.path.join(directory_path, directory_name, file))

# Show popup after all files are organized
root = tk.Tk()
root.withdraw()  # hide main window
messagebox.showinfo("Done", "All files have been organized!")
