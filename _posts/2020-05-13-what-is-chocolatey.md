---
layout: post
published: true
title: What is Chocolatey?
description: Want to save time? Do yourself a favor and install Chocolatey!
date: '2020-05-13'
categories: [How-to, Software, Windows]
media_subpath: /azimstech.github.io/
image:
  path: fpdfcRV.png
  alt:
tags: [chocolatey cheat sheet]
---

**Chocolatey** is command line package manager for Windows just like Google Play Store in your phone but it does not come with graphical user interface. However, there's optional user interface available for those who needed. 

## Why Chocolatey is useful.

Having a package manager, makes installs of my most used software, that much easier. It is a great way to keep track of the software you have and which version of that software you are on. So installing Chocolatey is going to be what I do when set up windows for the first time.

## Installing Chocolatey from Powershell

1\. Run Powershell as Administrator.  
2\. Copy & paste the following command into Powershell:  

{: .box-note}
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

3\. Wait for the command to complete.  
4\. You don't see any errors, you can start using chocolatey.

## Using Chocolatey

Before you start using chocolatey, I usualy start by disabling confirmation feature by running this command:
~~~
choco feature enable -n allowGlobalConfirmation
~~~

### To find a package in command line use:
~~~
choco search googlechrome
~~~

### To  install a package:
~~~
choco install googlechrome
~~~ 

### To install multiple packages:
~~~
choco install googlechrome 7zip mpcbe
~~~

### Pin a package to suppress upgrades:
~~~
choco pin add --name paint.net
~~~

### To unpin a package:
~~~
choco pin remove --name paint.net
~~~

### To uninstall a package:
~~~
choco uninstall googlechrome
~~~

### To update all installed packages:
~~~
choco upgrade all
~~~
![upgrade-example](cz4stS4.png)

### To list all installed packages:
~~~
choco list
~~~
![list-example](PhBS9mO.png)

## Research

- [Official Chocolatey installation guide](https://chocolatey.org/install)
- [Chocolatey github wiki - Commands reference](https://github.com/chocolatey/choco/wiki/CommandsReference)
- [Level1Techs - Chocolatey: A Windows Package Manager?](https://www.youtube.com/watch?v=p7AsofW8kUY)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg0MjkyNzcyMF19
-->
