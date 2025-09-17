# File Organizer

A lightweight Python tool that automatically sorts files into categorized folders (Images, Videos, Documents, etc.).  

Two versions are available:
- **CLI Version** – prompts you for a target directory.
- **Silent Version** – organizes files in the current directory without any input.

---

## Features
- Automatically detects file types and moves them into corresponding folders.
- Supports images, videos, documents, executables, compressed files, code files, and more.
- Creates folders only when needed.
- Available in **CLI** (interactive) or **Silent** (drop-and-run) modes.---
## Installation
Clone this repository:
```bash
git clone https://github.com/Fuyuki2/File-Organizer.git
cd File-Organizer
````

## Usage

CLI Version

Run and enter the target directory path:
```bash
python file_organizer_cli.py
```

Silent Version

Place the .exe (or script) inside the folder you want to organize and run it:
```bash
python file_organizer_silent.py
```
(or just double-click the .exe)

---
## Outcome

**Before**
```html
project/
 ├── report.docx
 ├── movie.mp4
 ├── script.py
 └── photo.jpg

```
**After**

```html
project/
 ├── DOCUMENT/
 │   └── report.docx
 ├── VIDEO/
 │   └── movie.mp4
 ├── CODE/
 │   └── script.py
 └── IMAGE/
     └── photo.jpg
```
