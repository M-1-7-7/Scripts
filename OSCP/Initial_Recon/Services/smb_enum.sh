#!/bin/bash

#Argument Supplied Check
display_usage() { 
	echo -e "\nUsage: $0 <IP Address>\n" 
	} 
# if less than X arguments supplied, display usage 
if [  $# -le 0 ] 
then 
	display_usage
	exit 1
fi 
 
# check whether user had supplied -h or --help . If yes display usage 
if [[ ( $@ == "--help") ||  $@ == "-h" ]] 
then 
	display_usage
	exit 0
fi 

# Variable Assignment

# SMB enum scan

ip=$1
cd $ip
 
mkdir SMB_Enum && cd SMB_Enum
#run nmap smb enum scan
nmap $ip --script=smb-enum* -p 445 -vvv -o smb_enum.out

#run nmap smb vuln scan
nmap $ip --script=smb-vuln* -p 445 -vvv -o smb_enum.out

#run nmap if creds are known 
#nmap $ip --script=smb-enum* --script-args smbusername=<name>,smbpass=<pass> -p 445 -vvv -o smb_credentialed_enum.out







