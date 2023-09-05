# Remote Service Access 

### SMB

1. `impacket-smbclient [[domain/]username[:password]@]<targetName or address> `
- hashes are also accepted `-hashes`

### RPC / WinRM

1. `evil-winrm -i IP -u USER`
- hashes are also accepted `-H`

### RDP (remote desktop)

1. `xfreerdp /u:<user> /p:<pass> /v:<server>`
- can set hight of screen with `/h:<pixels>`

3. `Rdesktop <target IP>`
   
### SSH (setting up keys)


### psexec

1. if SMB share is writable and RPC are open then psexec could be the method of authentication 
- `impacket-psexec [[domain/]username[:password]@]<targetName or address>`
