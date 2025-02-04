---
title:  HTB - GreenHorn
date: 2024-02-02 12:17:34 -0400
categories: [hackthebox , GreenHorn]
tags: [HackTheBox, CMS pluck, RCE, User-Agent]
image:
  path: /assets/img/post/greenhorn/greenhorn-card.png
  lqip: data:image/webp;base64,UklGRpoAAABXRUJQVlA4WAoAAAAQAAAADwAABwAAQUxQSDIAAAARL0AmbZurmr57yyIiqE8oiG0bejIYEQTgqiDA9vqnsUSI6H+oAERp2HZ65qP/VIAWAFZQOCBCAAAA8AEAnQEqEAAIAAVAfCWkAALp8sF8rgRgAP7o9FDvMCkMde9PK7euH5M1m6VWoDXf2FkP3BqV0ZYbO6NA/VFIAAAA
  alt: Hack the Box - GreenHorn.
---

## Box Info

| Name                  | GreenHorn        | 
| :-------------------- | ---------------: |
| Release Date          | 20 Jul, 2024     |
| OS                    | Linux            |
| Rated Difficulty      | Easy             |

## **Enumeration**

### Information Gathering

#### Scan with nmap:

![Image](/assets/img/post/greenhorn/image.png)

Add the dns to /etc/hosts:

```java
echo "10.10.11.25 greenhorn.htb" | sudo tee -a /etc/hosts
```

```bash
whatweb greenhorn.htb or wappalyzer from web.
```

we have  in the bottom a web for `admin` with the `CMS` called '`pluck'`

![Image](/assets/img/post/greenhorn/image-1.png)

## CMS pluck 4.7.18

We found in the web admin the version for the CMS 'pluck' 4.7.18 which have a `RCE vulnerability` but we need a password for login in the pluck CMS so i look at the port 3000 because we have a http with status 200 so investigate i found a web similar to github. After searching, I found credentials I assumed use it to pluck CMS.

![Image](/assets/img/post/greenhorn/image-2.png)

## Gitea

![Image](/assets/img/post/greenhorn/image-3.png)

`iloveyou1`

![Image](/assets/img/post/greenhorn/image-4.png)

## Explotation

I login into pluck CMS and we are inside as administrator in the web and see the version of the pluck cms

![Image](/assets/img/post/greenhorn/image-5.png)

I found a [RCE](https://www.exploit-db.com/exploits/51592) for that version CMS pluck and we go use it

![Image](/assets/img/post/greenhorn/image-6.png)

looked the "upload_url" that tell me the web have a section in "module" of pluck CMS called "installmodule" so we go to investigate and used it

![Image](/assets/img/post/greenhorn/image-7.png)

To perform the RCE we need to make a reverse shell with pentestmonkey in php because the server is mount over apache so i use the pentestmonkey reverse shell for compressed and upload .

![Image](/assets/img/post/greenhorn/image-8.png)

## Privilege Escalation

when upload the zip we need to reload the web http://greenhorn.htb/data/modules/shell/revshell.php and listening with `nc -lvnp 9001` Once reload the web we got the reverse shell as www-data but we go to re-use the password iloveyou1 for login as junior and see the user.txt file.

![Image](/assets/img/post/greenhorn/image-9.png)

Well for scalation priveligies we download the file 'Using OpenVAS.pdf'

![Image](/assets/img/post/greenhorn/image-10.png)

Well, after hours of searching, i need download 2 tools 
`pdfimages` from poppler-utils
`depix.py` from  https://github.com/spipm/Depix

`pdfimages ./PDF OUTPUT`  

![Image](/assets/img/post/greenhorn/image-11.png)

## Pixelized Screenshots

```zsh
python3 depix.py -p /path/of/openvas image -s /images/searchimages/debruinseq_notepad_windows10_CloseAndSpace.png -o out1.png
```

![Image](/assets/img/post/greenhorn/image-12.png)

And we got the password for root:
sidefromsidetheothersidesidefromsidetheotherside

![Image](/assets/img/post/greenhorn/image-13.png)

and login as root

![Image](/assets/img/post/greenhorn/image-14.png)