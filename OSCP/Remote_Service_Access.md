# Remote Service Access 

### SMB

1. `impacket-smbclient [[domain/]username[:password]@]<targetName or address> `
2. hashes are also accepted `-hashes`

### RPC / WinRM

1. `evil-winrm -i IP -u USER`
2. hashes are also accepted `-H`

### RDP (remote desktop)

1. `xfreerdp /u:<user> /p:<pass> /v:<server>`
2. can set hight of screen with `/h:<pixels>`

3. `Rdesktop <target IP>`
   
### SSH (setting up keys)


