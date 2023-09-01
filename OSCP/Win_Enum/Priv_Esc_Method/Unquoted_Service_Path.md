# Unquoted Service Path Attack

### Identify a writable directory where the target file is located

- If the target file is located in `C:\Program Files\cater\cater_term.exe` we should see if the following a writable:

1. `C:\`, if this is writable we would name the payload `Program.exe`
2. `C:\Program\`, if this is writable we would name the payload `Files.exe`
3. `C:\Program Files\`, if this is writable we would name the payload `carter.exe`
4. `C:\Program Files\carter\`, if this is writable we would name the payload `carter_term.exe` and delete/rename the original `carter_term.exe`


