#!/bin/bash

#usage:
# ./initialNMAP.sh <ip address>

ip=$1

#nmap scan to identify all open port
nmap -p- -Pn --min-rate 2000 $ip -o nmapPortScan.txt

#formating port numbers so we can perform service scans
cat nmapPortScan.txt | grep open | cut -d "/" -f 1 > ports.txt
awk '{print $1}' ports.txt | paste -s -d, - > portList.txt

#scan for services on the open ports
nmap -p $(cat portList.txt) -sVC -Pn $1 -o sVC_Port_Scan.txt
