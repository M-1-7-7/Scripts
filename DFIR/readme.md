# Conducting IR Task
## Overview
These scripts can be used to automate the aquisistion proccesses of digital forensics and incident respone.  All scripts are aimed to be dinamic and modulare to easily mold to many incident responce tasks.

for specific artifact analysis refer too the `Artifact_Collection_Techniques.md`

`continue noting tools from book 2 page 35`

## Artifact Types `artifact name, location, description, book.page#, more`
- Prefetch data, `C:\Windows\Prefetch`, contains executable name/execution time(s)/number of times executed, 2.6
- shimcache, `SYSTEM\CurrentContolSet\Control\SessionManager\AppCompatCache\AppCompatCache`, available on windows 7 and later | AppCompatCache tracks the executable file's last modification date and file path | Advanced: Applications will be shimmed again (w/ additional entry) if the file content is updated or renamed. Good for proving application was moved, renamed, or timestamps were manipulated (If current File's Modified time # ShimCache Modified time), 2.14-16
- amcache, `C:\Windows\AppCompat\Programs\Amcache.hve`, tracks installed apps/loaded drives/and unasociated executables | Full path, file size, file modification time, compilation time, publisher metadata, 2.17
- 

## Flow
- book 4 page 25 shows proccess for identifying compromise with no sign of malware through different arifacts.


## Scripts
1. Volatility Automation Script (this will automate/semi-automate memory forensics)
2. Plaso Automation Script (Extraction of data like registries, web history, etc.)
3. Log2Timeline Filter Files
