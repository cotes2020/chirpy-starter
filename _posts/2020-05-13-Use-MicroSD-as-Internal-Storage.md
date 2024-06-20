---
layout: post
published: true
title: Use SD Card as Internal Storage
subtitle: Here’s how to do it
date: '2021-07-07'
tags:
  - Android
  - Magisk
  - How-to
  
share-img: 'https://imgur.com/nJLFumY.png'

---
If your phone has a small amount of storage, you probably want to use an external microSD card as internal storage. So here’s how to do it:  

![enter image description here](https://imgur.com/nJLFumY.png)

## Requirements
- Android 10 <= 
- Magisk 
- A good quality microSD Card 
- Root file explorer (I use [MiXplorer](https://azimstech.github.io/posts/2019-04-02-this-is-why-i-stopped-using-the-google-drive-app/))

> Before doing anything, I highly recommend you to read the  documentation from GitHub repository.

## Steps
1. Download [fbind](https://github.com/VR-25/fbind/releases)  module from GitHub.  
2. Open `Magisk` app ➡️ 🧩 `Modules` ➡️ 📦 `Install from storage`
3. Wait install to finish.
4. Open `MiXplorer` ➡️ navigate to `/data/adb/vr25/fbind`
5. Create `config.txt` with a text editor.
6. Paste the following code: 
`int_extf .external_storage`
7. Hit `save` & `reboot`

# Other Configurations
For some reason you just want to move some specific folders to microSD and leave the rest to internal storage. Well, you can do that too.

1. Install the `module` from `magisk` ➡️ `reboot`.  
2. Edit `config.txt` along the path:  `/data/adb/vr25/fbind`
3. The  necessary folders are bind like this:  
`from_to <phone_folder> <sd-card folder>`

Example `config.txt` to give you an idea:  
~~~
from_to WhatsApp .WhatsApp  
from_to Viber .Viber  
from_to Download .Download  
from_to DCIM .DCIM  
from_to Pictures .Pictures
~~~

> Please note that if you don't put `period` infront of \<sd-card folder> the picture & video will appear twice in your `Gallery` app.

# Research
- [VR-25](https://github.com/VR-25)/**[fbind](https://github.com/VR-25/fbind)** 
- [XDA discussion thread](https://forum.xda-developers.com/t/magisk-system-2019-1-23-fbind.3621814/)

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyMTQxNDA4MTksODk4OTkzMzg5LDEzMT
k3MzE4MzYsLTcyMzk4MTg0LC0xMjk5NjU2ODA4LDE0NjYwNTgx
NCwyMDE0OTMyMzIsNzg3MDExMTI1LC0xODgyOTgxNjQ1LDE4MT
Y3NDc2ODEsNzQ2NjQyOTgyLDQ0MzM2OTUwMF19
-->