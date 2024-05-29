# Dirty Word Searcher

## Overview

The Dirty Word Searcher is a script designed to scan files on your computer for predefined "dirty" or inappropriate words. This can be useful for content moderation, filtering, or simply auditing text files for certain words.

## Features

- Scans multiple file types (e.g., .txt, .log, .csv).
- Generates a report of files containing dirty words.
- Easy-to-use interface and setup.

## Prerequisites

- Windows operating system
- Administrator privileges (for accessing protected files and directories)
- Python installed on your machine (if the script is written in Python)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/M-1-7-7/Scripts/edit/main/Dirty_Word_search
   cd dirty-word-searcher

# Overview
This is a word searcher that scans the file system and identifies specified words in documentation.

## File Types
- PDF
- PowerPoint (PPT, PPTX)
- Word Documents (DOC, DOCX)
- Excel Spreadsheets (XLS, XLSX)

## Todo List

1. export the python file to exe with pyinstaller. `C:\Users\ABB58612\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts\pyinstaller.exe --collect-all spire.doc --collect-all spire.doc.common --uac-admin --onefile .\Dirty_Word_Searcher.py`

3. add a shortcut to the task for the user to execute: 'runas /user:Administrator /savecred "cmd /k  C:\Path\To\dirty_word_searcher.exe"
