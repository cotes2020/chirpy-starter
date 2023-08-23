---
title: Flaws.cloud walkthrough
date: 02023-08-23 15:36:23
catagories: [cybersecurity, Red Teaming, terminal]
tags: [terminal, cloud, cybersecurity]
---
## Flaws.cloud walkthrough

**DayCyberWox Walkthrough:** https://www.youtube.com/watch?v=fEjAryrzLSQ
**Write up:** https://daycyberwox.com/exploiting-aws-1-a-beginners-guide-flawscloud#heading-level1

```
Through a series of levels you'll learn about common mistakes and gotchas when using Amazon Web Services (AWS). There are no SQL injection, XSS, buffer overflows, or many of the other vulnerabilities you might have seen before. As much as possible, these are AWS specific issues.

A series of hints are provided that will teach you how to discover the info you'll need. If you don't want to actually run any commands, you can just keep following the hints which will give you the solution to the next level. At the start of each level you'll learn how to avoid the problem the previous level exhibited.

```

**Scope**: Everything is run out of a single AWS account, and all challenges are sub-domains of [flaws.cloud](http://flaws.cloud/).

**Contact**  
This was built by Scott Piper ([@0xdabbad00](https://twitter.com/0xdabbad00), [summitroute.com](https://summitroute.com/))

Feedback is welcome! For security issues, fan mail, hate mail, or whatever else, contact scott@summitroute.com  
If you manage to find a flaw that breaks the game for others or some other undesirable issue, please let me know.

**Greetz**  
Thank you for advice and ideas from Andres Riancho ([@w3af](https://twitter.com/w3af)), [@CornflakeSavage](https://twitter.com/CornflakeSavage), Ken Johnson ([@cktricky](https://twitter.com/cktricky)), and Nicolas Gregoire ([@Agarri_FR](https://twitter.com/Agarri_FR))

Now for the challenge!

# Level 1

This level is *buckets* of fun. See if you can find the first sub-domain.

Need a hint? Visit [Hint 1](http://flaws.cloud/hint1.html)

First we begin with  `nslookup` and point it to the domain `flaws.cloud`
### Syntax
```shell
nslookup flaws.cloud
```

### Result

```shell
Server: 172.31.144.1
Address: 172.31.144.1#53

Non-authoritative answer:
Name:   flaws.cloud
Address: 52.92.196.83
Name:   flaws.cloud
Address: 52.92.227.67
Name:   flaws.cloud
Address: 52.92.243.131
Name:   flaws.cloud
Address: 52.92.250.91
Name:   flaws.cloud
Address: 52.218.132.58
Name:   flaws.cloud
Address: 52.218.218.82
Name:   flaws.cloud
Address: 52.218.237.138
Name:   flaws.cloud
Address: 52.92.163.83
```
