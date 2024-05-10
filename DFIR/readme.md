# Conducting IR Task

## Overview
These scripts can be used to automate the aquisistion proccesses of digital forensics and incident respone.  All scripts are aimed to be dinamic and modulare to easily mold to many incident responce tasks.

## Artifact Types

## Flow

### Examine shadow copies (Windows)
- KAPE (Triage Analysis) (book 5, page 12)
- Velociraptor (Triage Analysis) (book 5, page 12)
- Arsenal Image Mounter (Full-Volume Image) (book 5, page 12)
- F-Response (Full-Volume Image) (book 5, page 12)
- vshadowmount (Full-Volume Image) (book 5, page 12)
  
### Examine shadow copies (Linux)
- vshadowinfo (must be a raw image, lists all available shadow snapshots on disk) (book 5, page 13)
- vshadowmount (must be raw volume) (book 5, page 13)
- Log2timeline (for VSS volume shadow copies) (book 5, page 17)
  
## Scripts

1. Volatility Automation Script (this will automate/semi-automate memory forensics)
2. Plaso Automation Script (Extraction of data like registries, web history, etc.)
3. Log2Timeline Filter Files
