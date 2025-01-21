---
title: Disable Virtualization on Gigabyte Motherboard
description: Without Flashing Modded BIOS
author: null
date: '2024-10-22 13:20:00 +0800'
categories: [How-to, Software, Hardware]
tags:
  - Windows
pin: false
math: false
mermaid: false
image:
    path: https://cdn.statically.io/gh/AzimsTech/compress/master/azimstech.github.io/Giga-H410-H-V3-banner.jpg
alt:
---

I can't believe that Gigabyte doesn't let you turn off the virtualization in the BIOS, unlike other vendors, well at least for some of the Intel motherboards. There's a lot of reddit posts around asking for it, and I found an easy way to do it that nobody seems to be talking about.

This is the easiest way to do it. It is also quite safe. If something goes wrong, you can just delete the cmos and everything's back to normal.

## Note
> This was tested on Gigabyte H410M H V3 (rev. 1.0)  
> BIOS version: F9 (Dec 20, 2023)

## Preparation
- The [modGRUBShell.efi](https://github.com/datasone/grub-mod-setup_var/releases) file
- A USB stick

## Here's the way I do it:
1. Format the USB stick to `FAT32`
2. Place the file `modGRUBShell.efi` on the USB stick in this directory, so it looks like this `X:\EFI\BOOT\modGRUBShell.efi`.
3. Disable `Secure Boot` and then enable `CSM` in the BIOS.
4. Press `F12` to boot from the USB stick. Select the one with `UEFI:` at the beginning.
5. Now type this command:  
   
   To **disable** virtualization:  
   ```
   setup_var_cv CpuSetup 0xB9 0x1 0x0
   ```
   To **enable** virtualization:  
   ```
   setup_var_cv CpuSetup 0xB9 0x1 0x1
   ```
 6. Type `reboot` when you're done


## Where do I get these commands?
I followd this guide: https://github.com/BoringBoredom/UEFI-Editor

![image](https://gist.github.com/user-attachments/assets/8fae0846-326d-4b14-80fb-ec11b6a73bc2)