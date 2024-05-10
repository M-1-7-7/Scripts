# Conducting IR Task

## Overview
These scripts can be used to automate the aquisistion proccesses of digital forensics and incident respone.  All scripts are aimed to be dinamic and modulare to easily mold to many incident responce tasks.

## Artifact Types

## Flow

## Artifact Collection Techniqes

### 1. Malware Discovery exe(Description, OS, book.page#, more)
- sigcheck.exe (check for code signing of executables, Windows, 4.6, can be ouput as csv and loaded into timeline_analyser)
- entropy.exe (checks file entropy to identify anomelies in data, Windows, 4.7)
- yarra rule (identifies malware based on a number of properties, any, 4.8-11)
- maldump (idenetifies and extracts quarentiened filed from antivirus software, 4.12-13)
- capa (triage an executable and display its properties, 14-16)
  
### 2. Examine shadow copies (Windows)
- KAPE (Triage Analysis) (book 5, page 12)
- Velociraptor (Triage Analysis) (book 5, page 12)
- Arsenal Image Mounter (Full-Volume Image) (book 5, page 12)
- F-Response (Full-Volume Image) (book 5, page 12)
- vshadowmount (Full-Volume Image) (book 5, page 12)
  
### 3. Examine shadow copies (Linux)
- vshadowinfo (must be a raw image, lists all available shadow snapshots on disk) (book 5, page 13)
- vshadowmount (must be raw volume) (book 5, page 13)
- Log2timeline (for VSS volume shadow copies) (book 5, page 17)
  
## Scripts
1. Volatility Automation Script (this will automate/semi-automate memory forensics)
2. Plaso Automation Script (Extraction of data like registries, web history, etc.)
3. Log2Timeline Filter Files
