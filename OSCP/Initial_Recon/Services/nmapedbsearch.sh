# Prompt the user for a hostname or IP address
echo -n "What is the hostname or IP address?  "
read host

# Run nmap with the following options:
# -oX tmp.xml: Output in XML format to a file named tmp.xml
# -A: Enable OS detection, version detection, script scanning, and traceroute
# -Pn: Treat all hosts as online (skip host discovery)
# -n: Never do DNS resolution
# -T4: Set timing template (higher is faster)
# --min-rate=6000: Send packets no slower than 6000 per second
# $host: The hostname or IP address provided by the user
# -p-: Scan all 65535 ports
sudo nmap -oX tmp.xml -A -Pn -n -T4 --min-rate=6000 $host -p-

# Parse the XML output to extract product names from service information
products=$(grep '<service' tmp.xml | awk -F'product="' '{print $2}' | awk -F'"' '{print $1}')

# Clean up product names by replacing spaces with newlines, removing "None", and removing "httpd"
cleanservices=$(echo $products | tr ' ' '\n' | grep -v "None" | sed 's/httpd//g')

# For each cleaned service name, run searchsploit to find potential exploits
for service in $cleanservices
do
    echo "\nSEARCHING FOR THE $service SERVICE\n"
    searchsploit $service
done

# Remove the temporary XML file
rm tmp.xml
