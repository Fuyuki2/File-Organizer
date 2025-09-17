import sys
import os
import shutil

file_type = {
    "image": ["jpg", "png", "jpeg"],
    "video": ["mp4", "mov", "avi"],
    "document": ["pdf", "docx", "txt"],
    "executable": ["exe", "msi"],
    "compressed": ["zip", "rar", "7z"],
    "code": ["py", "java", "cpp", "html", "css", "js"],
    "other": []
}

# Ask user for path, default to current folder if they press Enter
while True:
    directory_path = input("Enter the directory path (or 'q' to quit): ")
    if directory_path.lower() == 'q':
        sys.exit()
    if not directory_path:
        directory_path = os.getcwd()  # current folder where the .exe runs

    if os.path.isdir(directory_path):
        for file in os.listdir(directory_path):
            # 1. skip directories
            if os.path.isdir(os.path.join(directory_path, file)):
                continue

            # 2. Skip hidden/system files
            if file.startswith('.'):
                continue

            # 3. normalize extension
            file_extension = os.path.splitext(file)[1][1:].lower()
            moved = False
            # also could be root, extension = os.path.splitext(file) instead of extension os.path.splitext(file)[1]
            # this would give both the root and the extension

            for category, extensions in file_type.items():
                if file_extension in extensions:
                    directory_name = category.upper()
                    os.makedirs(os.path.join(directory_path, directory_name),
                                exist_ok=True)
                    shutil.move(
                        os.path.join(directory_path, file),
                        os.path.join(directory_path, directory_name, file))
                    moved = True
                    break
                    # stop once file is moved

            # 5. Move to "OTHER" if no match
            if not moved:
                directory_name = "OTHER"
                os.makedirs(os.path.join(directory_path, directory_name),
                            exist_ok=True)
                shutil.move(os.path.join(directory_path, file),
                            os.path.join(directory_path, directory_name, file))
        print("\nAll files have been organized!")
        input("Press Enter to exit...")
        break  # done organizing, exit loop
    else:
        print("Invalid directory path. Please enter a valid directory path.")
        continue
