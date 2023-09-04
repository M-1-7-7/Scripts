# Find all http and https ports
ip=$1

mkdir $ip/webEnum && cd $ip/webEnum

echo -e "\n===== Begining Feroxbuster for HTTP and HTTPS =====\n"
cat ../nmapScans/sVC_Port_Scan.txt | grep "/tcp\|/udp" | grep "http" | cut -d "/" -f 1 > httpPorts.txt
cat ../nmapScans/sVC_Port_Scan.txt | grep "/tcp\|/udp" | grep "https" | cut -d "/" -f 1 >> httpPorts.txt

cat httpPorts.txt | while read line; 
do
	feroxbuster -C 404,500,403 -d 3 -u http://$ip:$line/ -w "/usr/share/seclists/Discovery/Web-Content/combined_words.txt" -x html,pdf,php,asp,htaccess,json,docx,xml -o ferox_port_$line.txt
done;
