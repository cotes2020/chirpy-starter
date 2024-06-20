---
published: true
layout: post
tags:
  - Windows
  - How-to
subtitle: on Windows 10/11
title: How to Setup Network File Sharing?
share-img: 'https://i.imgur.com/k02TwQS.png'
---
Here's how to share files & folders in Windows:


## Open Computer Management

First, you will need to open   Computer Management
<kbd>Win</kbd> + <kbd>X</kbd> ➡ `Computer Management`  

![computer management](https://i.imgur.com/FqQauc5.png)

## Create a New User

Just in case you need a password protection, You'll need a new account.

1. `Local Users and Groups` ➡ `Users` ➡ <kbd>Right Click</kbd> ➡ `New User...`  

![New user](https://i.imgur.com/0BpBpqJ.png)
2. Fill down your new `User name` & `password`
3. Uncheck `User must change password at next logon`  

![username password](https://i.imgur.com/zKQUo5G.png)

## Choose a Folder to Share

Now it's time to choose a folder you wanted to share.  

1. `Shared Folders` ➡ `Shares` ➡ <kbd>Right Click</kbd> ➡ `New Share...`    

![New shared folder](https://i.imgur.com/VSiSdqR.png)
2. On `Create A Shared Folder Wizard` window: `Next` ➡ `Browse...` ➡ select a folder ➡ `OK`  

![Browse](https://i.imgur.com/wo4rtZh.png)
3. `Customize permissions` (recommended) ➡ Check `Full Control` ➡ `Ok` ➡ `Finish`  

![Cusmotize permissons](https://i.imgur.com/f2sLUkz.png)

## Give Permission to a User

1. Select shared folder you just created & `<kbd>Right Click</kbd>` ➡ `Properties`  

![Shared Folder Properties](https://i.imgur.com/NlIE6Tr.png)
2. `Security` tab ➡ `Edit` ➡ `Add..` ➡ Fill user name inside `Enter the object names to select` ➡ `OK`  

![Add Username](https://i.imgur.com/PTh8DSZ.png)
3. Under `Permissions for home network` window: Click your `user name` ➡ Check `Allow` on `Full Control` ➡ `OK`  

![Give Full Control Permission](https://i.imgur.com/YwDnJjF.png)

## Troubleshooting

### Check the Advanced Sharing Settings

Make sure the settings has been setup correctly.  
<kbd>Win</kbd> + <kbd>X</kbd> ➡ `Network Connections` ➡ `Network and Sharing Centre` ➡ `Change advanced sharing settings`  

Follow these settings:  

![1](https://i.imgur.com/Zx1l2hv.png)  

![2](https://i.imgur.com/Jv8NwlE.png)  

![3](https://i.imgur.com/L3eLRfG.png)
