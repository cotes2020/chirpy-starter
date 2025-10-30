---
title: CTF Challenges
icon: fas fa-flag
order: 4
---

<!-- 
═══════════════════════════════════════════════════════════════════════════
INSTRUCTIONS FOR ADDING CTF/LAB WRITE-UPS:
═══════════════════════════════════════════════════════════════════════════

This page showcases your CTF and lab challenge solutions. To add a new write-up:

1. Copy the template below for each challenge
2. Fill in all the [BRACKETS] with your information
3. Add screenshots by:
   - Creating folder: /assets/img/ctf/
   - Placing images there
   - Referencing like: ![Alt text](/assets/img/ctf/challenge-name-screenshot.png)
4. Be careful not to spoil solutions - add spoiler warnings if needed
5. Remove these instruction comments when done

═══════════════════════════════════════════════════════════════════════════
-->

# CTF & Lab Challenges

This section documents my journey through various CTF competitions and lab challenges, showcasing problem-solving skills, technical knowledge, and hands-on security experience.

---

<!-- ========== CTF CHALLENGE TEMPLATE - COPY THIS FOR EACH CHALLENGE ========== -->

## 🚩 [Challenge Name]

**Platform**: Hack The Box 
**Machine**: SoulMate
**Difficulty**: Easy  
**Category**: Web / Forensics  
**Completion Date**: Sept 2025

### 📝 Challenge Description

- This challenge likely involved finding and exploiting a vulnerability in a web application.
    - CrushFTP bypass led to initial access
    - Password extraction from internal scripts
    - Erlang shell exploitation for privilege escalation
    - Root access


### 🎯 Learning Objectives

- The highlight has been “Enumeration is everything”, and that includes network and process enumeration, not just files.

---

### 🔍 Reconnaissance

**Initial Approach:**

**Reconnaissance Phase**

*Nmap Scan*

- Given an IP, first step is to carry out an *nmap* tool to scan to identify open ports and services on the target machine.
*Findings*:
    - Port 22 — OpenSSH (SSH service)
    - Port 80 — HTTP (Web server)
    -   http-title: Did not follow redirect to http://soulmate.htb/.

*Screenshot*

*Web directory enumeration*

- Next was to do further enumerations for hidden subdomains, directories and even virtual hosts. Virtual host scanning checks for websites hosted on the same IP but with different domain names. 
- This revealed ftp.soulmate.htb.Used  gobuster and a common wordlist. 
- Tool: Gobuster

*Screenshot*
### 🔓 Exploitation

edit the hosts file so the ftp server can be resolved and on the  browser we have a Crushftp login page. CrushFTP is a powerful file server supporting standard secure file transfer protocols.

*Screenshot of ftp login*

**Vulnerability Identified:**

-  **Vulnerability Research*
Likewise, The CrushFTP server running on ftp.soulmate.htb was analyzed to determine the exact version, version 11.This version was found to be vulnerable to CVE-2025-31161 - allows authentication bypass and takeover of the crushadmin account. Looked for public exploit for this particular vulnerability by Immersive labs
https://github.com/Immersive-Labs-Sec/CVE-2025-31161.


**Initial Exploitation** 
*Run Authentication Bypass* 
This critical flaw allows an attacker to register a new user with administrative privileges by leveraging existing admin accounts (like the default crushadmin user) without requiring their credentials.

*screenshot*

*Login*
- Using admin: admin123 login to the page and have full administrative access to the CrushFTP admin web interface and with admin privileges.
Looking around there’s a user management dashboard, there are different users and with a user ben, we reset ben's password to one we control and login as him. On ben’s dash we can upload a file, so we can create a web shell and upload it.

*Screenshot of userdash*

*Creating the Web Shell*

- Created a simple revshell.php with reverse shell code, upload to a web-accessible directory, webProd. The web server executes PHP files in this directory.
    Triggering Reverse Shell
        - Start a listener.
        - Access the shell:
            Browse to http://soulmate.htb/revshell.php
        - PHP file executes the reverse shell code
        - Connects back to our netcat listener on port 4444

*Shell Screenshot*

*Finding Ben's Home Directory and User Flag.*

- Find ben’s SSH credentials that I used to establish SSH connection as Ben home directory where a file, user.txt exists and contains the flag.

*Screenshot of ssh*
*sshh and flag*

**Privilege Escalation to Root and Root Flag**

- My thought went on to do a network enumeration and on analysis port 2222(Common alternative SSH port),was an interesting one. It is a non-standard port and locally bound, meaning the service only accessible from the machine itself (127.0.0.1), as root - a classic privilege escalation vector.

- Key Findings:
	- Service Type: Erlang-based SSH daemon
	- Authentication: Username "ben" with password "HouseH0ldings998"
- The Privilege Escalation Mechanism - The Erlang service process starts and runs with root privileges. Service Connection – ssh -p 2222 ben@localhost

*Normal SSH Authentication Flow*
*User → SSH Client → SSH Server (runs as root) → Command Execution (as authenticated user)*

*Erlang SSH Service Flow*
*User → SSH Client → Erlang Service (runs as root) → os:cmd() Function → Command Execution (as root)*

*Screenshot*

---

### 📚 Key Takeaways

**Mitigation and Lessons Learned**

*Security Issues Identified*
- Excessive Privileges: Service running as root unnecessarily
- Command Injection: Unrestricted system command execution
- Privilege Maintenance: Failure to drop privileges after authentication

*Recommended Fixes*
- Principle of Least Privilege: Run service under dedicated service account
- Privilege Separation: Drop privileges after authentication

*Detection*
- Network Scanning: Identify non-standard services
- Process Monitoring: Flag services running as root
- Configuration Auditing: Review service privilege settings

*Screenshot*

---

