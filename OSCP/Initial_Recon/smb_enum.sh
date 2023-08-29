#!/bin/bash

# SMB enum scan

ip=$1

#run nmap smb enum scan
nmap $ip --script=smb-enum* -p 445 -vvv -o smb_enum.out

#run nmap smb vuln scan
nmap $ip --script=smb-vuln* -p 445 -vvv -o smb_enum.out

#run nmap if creds are known 
#nmap $ip --script=smb-enum* --script-args smbusername=<name>,smbpass=<pass> -p 445 -vvv -o smb_credentialed_enum.out







