---
title: Disable Virtualization on Gigabyte Motherboard
description: Without Flashing Modded BIOS
author: null
date: '2025-01-22 1:20:00 +0800'
categories: [How-to, Software, Hardware]
tags:
  - Windows
pin: false
math: false
mermaid: false
media_subpath: /azimstech.github.io/
image:
  path: Giga-H410-H-V3-banner.jpg
alt:
---

I can't believe Gigabyte doesn't let you disable virtualization in the BIOS for some Intel motherboards. Many Reddit posts ask about this, and I found an easy way to do it that isn't widely discussed.

This is the easiest way to do it. It is also quite safe. If something goes wrong, you can just clear the cmos and everything's back to normal.

## Note

This guide is only for MSI H410M H3 (rev. 1.0). For other motherboards, [see here.](#where-do-i-get-these-commands-from)

> This was tested on Gigabyte H410M H V3 (rev. 1.0)  
> BIOS version: F9 (Dec 20, 2023)
{: .prompt-info }

## Preparation

- [modGRUBShell.efi](https://github.com/datasone/grub-mod-setup_var/releases)
- A USB stick

## Here's the way I do it:

1. Format the USB stick to `FAT32`
2. Download the file `modGRUBShell.efi` and rename it to `BOOTX64.EFI`. Then put it on the USB stick so it looks like this `X:\EFI\BOOT\BOOTX64.EFI`. (X: is the USB drive letter)
3. Disable `Secure Boot` and then enable `CSM` in the BIOS.
4. Press `F12` to boot the EFI shell from the USB stick. Select the one with `UEFI:` at the beginning.
5. In EFI shell mode, type this command:  

   To **disable** virtualization:  

   ```bash
   setup_var_cv CpuSetup 0xB9 0x1 0x0
   ```

   To **enable** virtualization:  

   ```bash
   setup_var_cv CpuSetup 0xB9 0x1 0x1
   ```

6. Type `reboot` when you're done/
7. Now its virtualization is disabled:

   ![result](vm-disabled-result.png)

## Where do I get these commands from?

Just follow this guide: [https://github.com/BoringBoredom/UEFI-Editor](https://github.com/BoringBoredom/UEFI-Editor)

![image](https://gist.github.com/user-attachments/assets/8fae0846-326d-4b14-80fb-ec11b6a73bc2)