---
layout: post
published: true
title: How to delete a service in Windows?
share-img: 'https://i.imgur.com/Gpknkm7.png'
tags:
  - Windows
  - How-to
subtitle: Via Command Prompt
---
If for some reason you have a few services that you want to get rid of completely. Here I can show you how to do this step by step.


Open Command Prompt As Administrator
=====================================

First, you will need to open the command prompt as an administrator.

![Imgur](https://i.imgur.com/IiVOKuI.png)

Find Services You Want to Delete
====================================

Open Services same as opening command prompt by hitting the Start menu and start searching "services" and click on it.

In my case, I want to delete a couple of Adobe services. So I need to find its "short service name" by doing this.

![Imgur](https://i.imgur.com/Gpknkm7.png)

Start Typing These Command 
====================================

Now you need to start typing these two commands:

~~~
SC STOP shortservicename
SC DELETE shortservicename
~~~

Remember to replace "shortsercivename" to your desired service name that you have copied last time. 

Im my case:
~~~
SC STOP AGMService
SC DELETE AGMService
~~~

![example](https://i.imgur.com/Oi7tZZM.png)

Bonus Tips
====================================

If you need to find the short service name of a service, use the following command to generate a text file containing a list of services and their statuses:

~~~
SC QUERY state= all >"C:\Service List.txt"
~~~

Resources
==================================

- [Stackoverflow](https://stackoverflow.com/questions/76074/how-can-i-delete-a-service-in-windows)

