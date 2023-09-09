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
      - [ ] [Current User Privilages](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#users-and-groups)
      - [ ] Current group privilages
      - [ ] User Sessions
      - [ ] users homes (access)
      - [ ] Password Policy
      - [ ] what is in the clipboard
   
