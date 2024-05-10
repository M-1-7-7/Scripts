# Conducting IR Task

## Overview
These scripts can be used to automate the aquisistion proccesses of digital forensics and incident respone.  All scripts are aimed to be dinamic and modulare to easily mold to many incident responce tasks.

## Artifact Types `artifact name, location, description, book.page#, more`
- Prefetch data, `C:\Windows\Prefetch`, contains executable name/execution time(s)/number of times executed, 2.6
- 
## Flow
- book 4 page 25 shows proccess for identifying compromise with no sign of malware through different arifacts.

## Artifact Collection Techniqes `exe(Description, OS, book.page#, more)`
### 1. Prefetch Data Analysis (Ref. Artiact Types for overview^^)
- PECmd.exe (can parse a single or multiple prefetch files, Windows, 2.9-13)

### 1. Malware Discovery 
- sigcheck.exe (check for code signing of executables, Windows, 4.6, can be ouput as csv and loaded into timeline_analyser)
- entropy.exe (checks file entropy to identify anomelies in data, Windows, 4.7)
- yarra rule (identifies malware based on a number of properties, any, 4.8-11)
- maldump (idenetifies and extracts quarentiened filed from antivirus software, XXX, 4.12-13)
- capa (triage an executable and display its properties, XXX, 14-16)

### 2. Timeline Anlysis
- MFTEcmd.exe (uses windows artifacts to generate filesystem timeline, Windows, 4.43-44)
- fls (can run againes live or dead file systems and generates comprehensive file system timelines, Any, 4.45)

### 3. Examine shadow copies
- KAPE (Triage Analysis, Windows, 5.12)
- Velociraptor (Triage Analysis, Windows, 5.12)
- Arsenal Image Mounter (Full-Volume Image, Windows, 5.12)
- F-Response (Full-Volume Image, Windows, 5.12)
- vshadowmount (Full-Volume Image, Windows, 5.12)
- vshadowinfo (must be a raw image and lists all available shadow snapshots on disk, Linux, 5.13)
- vshadowmount (must be raw volume, Linux, 5.13)
- Log2timeline (for VSS volume shadow copies, Linux, 5.17)
  
## Scripts
1. Volatility Automation Script (this will automate/semi-automate memory forensics)
2. Plaso Automation Script (Extraction of data like registries, web history, etc.)
3. Log2Timeline Filter Files
