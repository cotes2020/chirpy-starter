---
title: Upgrade from Windows 10 to Windows 11 on an Unsupported Computer
description: Without using a third-party program
author: null
date: '2024-10-10 07:20:00 +0800'
categories: [How-to, Software, Windows]
tags:
  - Windows
pin: false
math: false
mermaid: false
image:
    path: https://cdn.statically.io/gh/AzimsTech/compress/master/azimstech.github.io/unsupportedw11.png
alt:
---

Here's how:
1. Mount the Windows 11 `.iso` file
2. Open the **Command Prompt** as an administrator
3. Enter the following command: `G:\setup.exe /product server`
4. Proceed with the Windows 11 upgrade process as usual

> `G:` being the drive letter assigned to your mounted ISO
{: .prompt-info }