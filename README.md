# 📁 Python File Manager

A simple, feature-rich command-line interface (CLI) File Manager application written in Python. This tool allows users to perform basic file operations, organize files automatically by type, view directory statistics, and manage settings using JSON.

## 🚀 Features

### 📄 File Operations

* **Create File**: Create a new empty file safely without overwriting existing files.
* **Read File**: Display the contents of a text file in the terminal.
* **Edit File**: Append new text/data to an existing file.
* **Delete File**: Remove a specified file from the directory.
* **Copy File**: Copy content from a source file into a destination file.
* **Search File**: Search for a specific file within the current directory.
* **File Information**: Display details such as file name, extension, size, absolute path, creation time, and last modified time.

### 📁 Directory & Folder Management

* **View All Items**: List all files and subdirectories.
* **List Files Only**: Filter and list only files (excluding folders).
* **Sort Files**: Alphabetically list all files in the current directory.
* **Create Folder**: Create a new directory.
* **Delete Folder**: Remove an empty folder.
* **Change Directory**: Navigate to a different path or directory.
* **Current Directory**: View the absolute path of the current working directory.
* **Directory Statistics**: View summary data including total file count, total folder count, and total size in bytes.

### 🧹 Advanced & Utility Features

* **Organize Files**: Automatically categorizes files into subfolders based on extension (`Images`, `Videos`, `Music`, `Documents`, `Python`, `Others`).
* **Save Settings**: Exports the last active directory and timestamp to a `settings.json` file.

---

## 🛠️ Prerequisites

* **Python 3.x** installed on your system.
* Standard Python libraries used (no additional `pip` dependencies required):
* `os`
* `json`
* `datetime`



---

## 📥 Installation & Running

1. **Clone or Download** the script file (e.g., `file_manager.py`).
2. Open your command prompt / terminal and navigate to the project directory:
```bash
cd path/to/project

```


3. Run the script:
```bash
python file_manager.py

```



---

## 🎮 How to Use

When you run the application, an interactive main menu will appear:

```text
========== FILE MANAGER ==========
1. Create File
2. View All Items
3. Delete File
4. Read File
5. Copy File
6. Search File
7. File Information
8. Sort Files
9. List Files Only
10. Organize Files
11. Edit Files
12. Create Folder
13. Delete Folder
14. Change Directory
15. Current Directory
16. Directory Statistics
17. Save Settings
18. Exit

Enter your choice: 

```

1. Select a menu option by entering the corresponding number (1-18).
2. Follow the on-screen prompts (e.g., entering filenames or directory paths).

---

## 🗂️ File Organization Logic

When option `10` (**Organize Files**) is selected, the application scans the directory and organizes files into folders:

| Folder | Extensions Supported |
| --- | --- |
| **Images** | `.jpg`, `.jpeg`, `.png`, `.gif` |
| **Videos** | `.mp4`, `.mkv`, `.avi` |
| **Music** | `.mp3`, `.wav` |
| **Documents** | `.txt`, `.pdf`, `.docx` |
| **Python** | `.py` |
| **Others** | Any other unlisted extension |

---

## 📝 Error Handling

The application handles common file system exceptions gracefully:

* `FileNotFoundError`: Triggers when trying to access or manipulate non-existent files/directories.
* `FileExistsError`: Prevents accidental overwriting when creating new files or folders.
* `PermissionError`: Catches permission restrictions during file access or directory changes.


