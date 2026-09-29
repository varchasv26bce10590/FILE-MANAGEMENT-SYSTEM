# 📄 Project Statement & System Analysis

**Project Name:** Python File Manager

**Student:** Varchasv Panwar

**Registration Number:** 26BCE10590

**Language & Tools:** Python 3.x, Standard Libraries (`os`, `json`, `datetime`)

## 1. Project Overview

The **Python File Manager** is a menu-driven command-line interface (CLI) application built using Python 3 and standard operating system modules. It simplifies daily file management and directory organization by combining basic file interactions, directory navigation, automated file categorization, metadata inspection, and settings storage into a single unified system.

## 2. Key Program Components

* **File Operations:**
  Supports creating, reading, editing (appending data), deleting, searching, and copying text files safely without overwriting existing data.

* **Folder & Directory Management:**
  Enables listing directory items, sorting files alphabetically, creating new folders, removing empty folders, navigating file paths, and displaying current working directory details.

* **Automated File Categorization:**
  Scans working directory contents and automatically moves files into dedicated subfolders (`Images`, `Videos`, `Music`, `Documents`, `Python`, `Others`) based on file extensions.

* **Analytics & Metadata:**
  Inspects detailed file properties (file name, extension, size in bytes, absolute location, creation time, modification time) and calculates directory summary statistics (total file count, total folder count, aggregate byte size).

* **Persistent Settings Storage:**
  Saves current working directory paths and activity timestamps into a `settings.json` file for persistence across sessions.

## 3. Robustness & Error Handling

The program uses dedicated `try-except` exception blocks across all functions to handle real-world file system errors gracefully:

* `FileExistsError`: Prevents overwriting existing files or folders during creation/movement.

* `FileNotFoundError`: Handles missing file or directory paths smoothly.

* `PermissionError`: Protects against operating system permission restrictions (e.g., system files like `ntuser.dat`).

* `Exception Fallback`: Catches unexpected system errors without interrupting the main application loop.