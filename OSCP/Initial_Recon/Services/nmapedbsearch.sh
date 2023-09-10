#!/bin/bash

echo -n "What is the hostname or IP address?  "
read host


# Run nmap and save output to a temporary file
sudo nmap -oX tmp.xml -A -Pn -n -T4 --min-rate=6000 $host -p-

# Parse XML output for product names
products=$(grep '<service' tmp.xml | awk -F'product="' '{print $2}' | awk -F'"' '{print $1}')

# Clean up product names
cleanservices=$(echo $products | tr ' ' '\n' | grep -v "None" | sed 's/httpd//g')

# Run searchsploit for each service
for service in $cleanservices
do
    echo "\nSEARCHING FOR THE $service SERVICE\n"
    searchsploit $service
done

# Remove temporary file
rm tmp.xml
