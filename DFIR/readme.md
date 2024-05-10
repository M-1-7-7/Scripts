# Conducting IR Task
## Overview
These scripts can be used to automate the aquisistion proccesses of digital forensics and incident respone.  All scripts are aimed to be dinamic and modulare to easily mold to many incident responce tasks.
`continue noting tools from book 2 page 35`
## Artifact Types `artifact name, location, description, book.page#, more`
- Prefetch data, `C:\Windows\Prefetch`, contains executable name/execution time(s)/number of times executed, 2.6
- shimcache, `SYSTEM\CurrentContolSet\Control\SessionManager\AppCompatCache\AppCompatCache`, available on windows 7 and later | AppCompatCache tracks the executable file's last modification date and file path | Advanced: Applications will be shimmed again (w/ additional entry) if the file content is updated or renamed. Good for proving application was moved, renamed, or timestamps were manipulated (If current File's Modified time # ShimCache Modified time), 2.14-16
- amcache, `C:\Windows\AppCompat\Programs\Amcache.hve`, tracks installed apps/loaded drives/and unasociated executables | Full path, file size, file modification time, compilation time, publisher metadata, 2.17
- 

## Flow
- book 4 page 25 shows proccess for identifying compromise with no sign of malware through different arifacts.

## Artifact Collection Techniqes `exe(Description, OS, book.page#, more)`

<details>
 <summary><b>1. Prefetch Data Analysis</b> (Ref. Artiact Types for overview^^) </summary>
 <ul>
  <li><b>PECmd.exe</b> (can parse a single or multiple prefetch files, Windows, 2.9-13)</li>
 </ul>
</details>

<details>
 <summary><b>2. Shimcache Data Extraction</b> (Ref. Artiact Types for overview^^) </summary>
 <ul>
  <li><b>appcompatparser.exe</b> (powershell tool that extracts amcache data for data in the SYSTEM hive, Windows, 2.16)</li>
  <li><b>appcompatprocessor.py</b> (powershell tool that automates the hunt for shimcache and amcache artifacts, Windows, 2.28-33)</li>
 </ul>
</details>

<details>
 <summary><b>3. amcache Data Extraction </b> (Ref. Artiact Types for overview^^) </summary>
 <ul>
  <li><b>amcacheparser.exe</b> (powershell tool that extracts shimcache data for data in the hive, Windows, 2.16)</li>
  <li><b>appcompatprocessor.py</b> (powershell tool that automates the hunt for shimcache and amcache artifacts, Windows, 2.28-33)</li>
 </ul>
</details>

<details>
 <summary><b>1. Malware Discovery </b></summary>
 <ul>
  <li><b>sigcheck.exe</b> (check for code signing of executables, Windows, 4.6, can be ouput as csv and loaded into timeline_analyser)</li>
  <li><b>entropy.exe</b> (checks file entropy to identify anomelies in data, Windows, 4.7)</li>
  <li><b>yarra rule</b> (identifies malware based on a number of properties, any, 4.8-11)</li>
  <li><b>maldump</b> (idenetifies and extracts quarentiened filed from antivirus software, XXX, 4.12-13)</li>
  <li><b>capa</b> (triage an executable and display its properties, XXX, 14-16)</li>
 </ul>
</details>

<details>
 <summary><b>2. Timeline Anlysis</b></summary>
 <ul>
  <li><b>MFTEcmd.exe</b> (uses windows artifacts to generate filesystem timeline, Windows, 4.43-44)</li>
  <li><b>fls</b> (can run againes live or dead file systems and generates comprehensive file system timelines, Any, 4.45)</li>
 </ul>
</details>

<details>
 <summary><b>3. Examine shadow copies</b></summary>
 <ul>
  <li><b>KAPE</b> (Triage Analysis, Windows, 5.12)</li>
  <li><b>Velociraptor</b> (Triage Analysis, Windows, 5.12)</li>
  <li><b>Arsenal Image Mounter</b> (Full-Volume Image, Windows, 5.12)</li>
  <li><b>F-Response</b> (Full-Volume Image, Windows, 5.12)</li>
  <li><b>vshadowmount</b> (Full-Volume Image, Windows, 5.12)</li>
  <li><b>vshadowinfo</b> (must be a raw image and lists all available shadow snapshots on disk, Linux, 5.13)</li>
  <li><b>vshadowmount</b> (must be raw volume, Linux, 5.13)</li>
  <li><b>Log2timeline</b> (for VSS volume shadow copies, Linux, 5.17)</li>
 </ul>
</details>


## Scripts
1. Volatility Automation Script (this will automate/semi-automate memory forensics)
2. Plaso Automation Script (Extraction of data like registries, web history, etc.)
3. Log2Timeline Filter Files
