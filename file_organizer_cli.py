import sys
import os
import shutil

file_type = {
    "images": ["jpg", "png", "jpeg", "webp"],
    "videos": ["mp4", "mov", "avi"],
    "documents": ["pdf", "docx", "txt", "xlsx", "pptx", "md"],
    "executables": ["exe", "msi"],
    "compressed": ["zip", "rar", "7z"],
    "code": ["py", "java", "cpp", "html", "css", "js", "json", "xml", "sql"],
    "other": []
}

# Ask user for path, default to current folder if they press Enter
while True:
    try:
        directory_path = input("\nEnter the directory path (or 'q' to quit): ")
    # The program exits gracefully when the user presses Ctrl+C (KeyboardInterrupt) or Ctrl+D (EOFError).
    except (KeyboardInterrupt, EOFError):
        print("\nThank you for using File Organizer!")
        sys.exit()

    if directory_path.lower() == 'q':
        sys.exit()

    if not directory_path:
        directory_path = os.getcwd()  # current folder where the .exe runs

    if os.path.isdir(directory_path):
        for file in os.listdir(directory_path):
            # 1. Skip directories.
            if os.path.isdir(os.path.join(directory_path, file)):
                continue

            # 2. Skip hidden/system files.
            if file.startswith('.'):
                continue

            # 3. Normalize extension.
            file_extension = os.path.splitext(file)[1][1:].lower()
            moved = False
            # Also could be root, extension = os.path.splitext(file) instead of extension os.path.splitext(file)[1]
            # This would give both the root and the extension.

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
                    # Stop once file is moved.

            # 5. Move to "OTHER" if no match.
            if not moved:
                directory_name = "OTHER"
                os.makedirs(os.path.join(directory_path, directory_name),
                            exist_ok=True)
                shutil.move(os.path.join(directory_path, file),
                            os.path.join(directory_path, directory_name, file))
        print("\nAll files have been organized!")

        try:
            input("Press Enter to exit...")
        except (KeyboardInterrupt, EOFError):
            print("\nThank you for using File Organizer!")

        break  # Done organizing, exit loop.
    else:
        print("\nInvalid directory path. Please enter a valid directory path.")
        continue
