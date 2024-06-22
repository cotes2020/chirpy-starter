---
layout: post
published: true
title: What is Chocolatey?
subtitle: Want to save time? Do yourself a favor and install Chocolatey!
date: '2020-05-13'
image:
   'https://cdn.statically.io/gh/AzimsTech/compress/master/azimstech.github.io/fpdfcRV.png'
tags:
  - How-to
  - Software
  - Windows
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
clist googlechrome
~~~

### To  install a package:
~~~
cinst googlechrome
~~~ 

### To install multiple packages:
~~~
cinst googlechrome 7zip mpcbe
~~~

### To ignore dependencies during install
~~~
cinst paint.net -i
~~~

### To uninstall a package:
~~~
cuninst googlechrome
~~~

### To update all installed packages:
~~~
cup all
~~~
![upgrade-example](https://cdn.statically.io/gh/AzimsTech/compress/master/azimstech.github.io/cz4stS4.png)

### To list all installed packages:
~~~
clist -l
~~~
![list-example](https://cdn.statically.io/gh/AzimsTech/compress/master/azimstech.github.io/PhBS9mO.png)

## Research

- [Official Chocolatey installation guide](https://chocolatey.org/install)
- [Chocolatey github wiki - Commands reference](https://github.com/chocolatey/choco/wiki/CommandsReference)
- [Level1Techs - Chocolatey: A Windows Package Manager?](https://www.youtube.com/watch?v=p7AsofW8kUY)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg0MjkyNzcyMF19
-->