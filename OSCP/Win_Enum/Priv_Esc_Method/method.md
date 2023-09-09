# Checklist - Local Windorws privilage Escalation

**Run Linpeas for best results**

1. System Info:
   - [ ] Obtain System Info
   - [ ] Search for [**Kernal exploits**](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#version-exploits)
   - [ ] Use **Google** to search for **Kernal** exploitsUse Google to search for kernel exploits
   - [ ] Use **searchsploit** to search for **kernel** exploits
   - [ ] Interesting Info in [**env vars**](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#environment)
   - [ ] Passwords in [**Powershell History**](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#powershell-history)
   - [ ] Interesting info in [**Internet settings**](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#internet-settings)
   - [ ] [Drivers](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#drives)
   - [ ] [**WSUS exploit**](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#wsus)
   - [ ] [**AllwaysIOnstallElevated** Vulnerbility](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#alwaysinstallelevated)

2. Logging/AV enumeration:
   - [ ] Check [Audit](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#audit-settings) and [WEF](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#wef) settings
   - [ ] Check [LAPS](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#laps)
   - [ ] Check if [**WDigest**](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#wdigest) is active
   - [ ] [LSA Protection](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#lsa-protection)
   - [ ] [Credentials Guard](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#credentials-guard)
   - [ ] [Cached Credentials](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#cached-credentials)
   - [ ] [Check for [**AV**](https://github.com/carlospolop/hacktricks/blob/master/windows-hardening/windows-av-bypass/README.md)
   - [ ] [**Applocker** Policy](https://github.com/carlospolop/hacktricks/blob/master/windows-hardening/authentication-credentials-uac-and-efs/README.md#applocker-policy)
   - [ ] [**UAC**](https://github.com/carlospolop/hacktricks/blob/master/windows-hardening/authentication-credentials-uac-and-efs/uac-user-account-control/README.md)
   - [ ] [**User Priv**](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#users-and-groups)
      - [ ] Current User Privilages
      - [ ] Current group privilages
      - [ ] User Sessions
      - [ ] users homes (access)
      - [ ] Password Policy
      - [ ] what is in the clipboard

3. Network:
   - [ ] Check current [**network information**](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#network)
   - [ ] check **hidden local services** hidden to the outside
   - [ ] Enumerate the network (shares, interfaces, routes, neighbours, ...)
   - [ ] Take a special look at network services listening on localhost (127.0.0.1)

4. Running Processes:
   - [ ] Processes Binaries [files and folder permisions](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#file-and-folder-permissions)
   - [ ] [**Memory Password mining**](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#memory-password-mining)
   - [ ] [Insecure GUI apps](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#insecure-gui-apps)

5. Services:
   - [ ] can you [modify services](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#permissions)
   - [ ] can you modify the [binary that is executed by any service](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#modify-service-binary-path)
   - [ ] Can you [modify the registry of any service](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#services-registry-modify-permissions)
   - [ ] can you take advantage of [unqoted service path](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#unquoted-service-paths)

6. Applications:
   - [ ] any [**Write** permisions on installed applications](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#write-permissions)
   - [ ] [**Startup Applications**](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#run-at-startup)
   - [ ] [**Vulnerble Drivers**](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#drivers)

7. DLL Hijacking:
   - [ ] Can you write in any folder inside PATH?
   - [ ] Is there any known service binary that tries to load any non-existant DLL?
   - [ ] Can you write in any binaries folder?
  
8. Windows Credentials 
