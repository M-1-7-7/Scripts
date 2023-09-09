# Checklist - Linux Privilege Escalation

Use LinPEAS for best results

1. [System Information](https://book.hacktricks.xyz/linux-hardening/privilege-escalation#system-information)
   - [ ] Get OS information
   - [ ] Check the [PATH](https://book.hacktricks.xyz/linux-hardening/privilege-escalation#path) for any writable folder
   - [ ] check the [env variable](https://book.hacktricks.xyz/linux-hardening/privilege-escalation#env-info) for any sensitive detail
   - [ ] Search for any [kernal exploits](https://book.hacktricks.xyz/linux-hardening/privilege-escalation#kernel-exploits) using scripts
   - [ ] check if the [sudo version is vulnerble](https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-version)
   - [ ] [Dmesage signature cerification failed](https://book.hacktricks.xyz/linux-hardening/privilege-escalation#dmesg-signature-verification-failed)
   - [ ] [other system info](https://book.hacktricks.xyz/linux-hardening/privilege-escalation#more-system-enumeration)
       - [ ] Date
       - [ ] System Status
       - [ ] CPU Info
       - [ ] Printers
       - [ ] etc
   - [ ] [enum more defences](https://book.hacktricks.xyz/linux-hardening/privilege-escalation#enumerate-possible-defenses)

2. [Drivers](https://book.hacktricks.xyz/linux-hardening/privilege-escalation#enumerate-possible-defenses)
   - [ ] List mounted drivers
   - [ ] list Unmounted drivers
   - [ ] any creds in fstab

3. [Installed Software](https://book.hacktricks.xyz/linux-hardening/privilege-escalation#installed-software)
   - [ ] check for [useful software](https://book.hacktricks.xyz/linux-hardening/privilege-escalation#useful-software) that is installed
   - [ ] check for [vulnerble software](https://book.hacktricks.xyz/linux-hardening/privilege-escalation#vulnerable-software-installed) that is installed
  
4. [Processes](https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes)
   - [ ] any unknown software running
   - [ ] software running with more privilage then required
   - [ ] exploits for services running
   - [ ] proccesses we can modify the binary
   - [ ] monitor proccesses and see if they run frequently
   - [ ] can we read come interesting process memory (where passwords may be stored)

6. [Scheduled/Cron jobs](https://book.hacktricks.xyz/linux-hardening/privilege-escalation#scheduled-jobs)
   - [ ] is the [PATH](https://book.hacktricks.xyz/linux-hardening/privilege-escalation#cron-path) being modified by a cron and can we write in it
   - [ ] Any [Wildcards](https://book.hacktricks.xyz/linux-hardening/privilege-escalation#cron-using-a-script-with-a-wildcard-wildcard-injection) in the cron job
   - [ ] is a [modifiable script](https://book.hacktricks.xyz/linux-hardening/privilege-escalation#cron-script-overwriting-and-symlink) being executed or in a modifiable folder
   - [ ] Is there some script may be [executing frequently](https://book.hacktricks.xyz/linux-hardening/privilege-escalation#frequent-cron-jobs) (every 1,2, or 5 min)
  
7. 
