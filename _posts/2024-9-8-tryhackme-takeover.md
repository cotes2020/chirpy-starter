---
title: 'TryHackMe: Takeover'
author: AmcaQt
categories: [TryHackMe]
tags: [web, enumeration, subdomain, subdomain takeover]
render_with_liquid: false
media_subpath: /images/thm_takeover/
image:
  path: room_card.png
---

![Tryhackme Room Link](room_image.PNG){: width="600" height="150" .shadow }
_<https://tryhackme.com/room/takeover>_

## Description

Hello there,

I am the CEO and one of the co-founders of futurevera.thm. In Futurevera, we believe that the future is in space. We do a lot of space research and write blogs about it. We used to help students with space questions, but we are rebuilding our support.

Recently blackhat hackers approached us saying they could takeover and are asking us for a big ransom. Please help us to find what they can takeover.

Our website is located at https://futurevera.thm

Hint: Don't forget to add the MACHINE_IP in /etc/hosts for futurevera.thm ; )

## Basic Scan

As usual we've been given a MACHINE_IP and need to put it on `/etc/hosts` with a named `futurevera.thm`. Lets run basic scan using Nmap

```Nmap Scan
┌──(amca㉿amcaqt)-[~]
└─$ nmap -A -T5 futurevera.thm 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-12-17 14:19 +08
Warning: 10.10.200.103 giving up on port because retransmission cap hit (2).
Nmap scan report for futurevera.thm (10.10.200.103)
Host is up (0.20s latency).
Not shown: 910 closed tcp ports (conn-refused), 87 filtered tcp ports (no-response)
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 dd:29:a7:0c:05:69:1f:f6:26:0a:d9:28:cd:40:f0:20 (RSA)
|   256 cb:2e:a8:6d:03:66:e9:70:eb:96:e1:f5:ba:25:cb:4e (ECDSA)
|_  256 50:d3:4b:a8:a2:4d:1d:79:e1:7d:ac:bb:ff:0b:24:13 (ED25519)
80/tcp  open  http     Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Did not follow redirect to https://futurevera.thm/
|_http-server-header: Apache/2.4.41 (Ubuntu)
443/tcp open  ssl/http Apache httpd 2.4.41
| ssl-cert: Subject: commonName=futurevera.thm/organizationName=Futurevera/stateOrProvinceName=Oregon/countryName=US
| Not valid before: 2022-03-13T10:05:19
|_Not valid after:  2023-03-13T10:05:19
|_http-title: FutureVera
|_http-server-header: Apache/2.4.41 (Ubuntu)
| tls-alpn: 
|_  http/1.1
|_ssl-date: TLS randomness does not represent time
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 44.43 seconds
```

We foundd that there's 3 open port which is :

`22` ssh
`80` http
`443` ssl/http

### Subdomain Enumaration

#### First Subdomain 

The Description mention `support`, which I assume they have `support` as their subdomain, so lets add that in `/etc/hosts` and looks what we can find on that subdomain. View the subdomain on firefox and shall find this : 

![First Subdomain](1st-subdo.PNG)

#### Second Subdomain

By clicking the `View Cerificate` you shall find info about the subdomain `support.futurevera.thm`. If you a little lower you'll find Subject Alternative Names with DNS Names `s******************2.support.futurevera.htm` and as usual add the DNS Names in `/etc/hosts`

![Second Subdomain](2nd-subdo.jpg)

### What's the value of the flag?

By viewing the DNS Names on the browser you'll obtain the flag and will be redirect to [AWS Web Server](https://www.geeksforgeeks.org/aws-cloud-architecture-for-web-hosting/). 

![Flag](flag.jpg)

### Conclusion

This room was fun and very interesting, it made me search and try to understand what is `Subdomain takeover`, and learned something new with this room.

If you want to learn more about `Subdomain Takeover`

- [Book.Hacktricks.xyz](https://book.hacktricks.xyz/pentesting-web/domain-subdomain-takeover)
- [HackerOne](https://www.hackerone.com/application-security/guide-subdomain-takeovers)
- [Developer.Mozilla](https://developer.mozilla.org/en-US/docs/Web/Security/Subdomain_takeovers)

## Happy Hacking

![](https://media1.tenor.com/m/aXVFqv8KInAAAAAC/anime-frieren.gif){: width="600" height="150" .shadow }