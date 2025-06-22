---
title: How to Change Intel CPU Microcode
description: By replacing the microcode update in the latest BIOS file
author: null
date: '2024-10-07 07:20:00 +0800'
categories:
  - Tips
tags:
  - PC
pin: false
math: false
mermaid: false
media_subpath: /azimstech.github.io/
image: https://img.youtube.com/vi/DUPY8S8B-04/maxresdefault.jpg
alt: 'Youtube thumbnail'
---

If you need to change the microcode but still want the latest BIOS features and fixes, you're in luck! I'll share how I managed to do this relatively easily.

# Why do You Want to Change the Microcode?
Depending on the generation of Intel CPUs, you might have different reasons for this:

- You may want to receive security enhancements, stability improvements, and performance optimizations from the latest microcode released by Intel, but your motherboard manufacturer has abandoned support or failed to keep the microcode up to date.
- In my case, downgrading the microcode helps regain 5-30% of the performance lost (depending on the workload) due to Spectre and Meltdown patches.


## Things you'll need
- Python - [Download](https://www.python.org/downloads/)
- UEFI BIOS Updater (UBU) - [UBU_v1_80_a17_fixed.zip](https://mega.nz/file/nAFAQILY#Ti5R-SSXKpsKgNVYcaKMef3MnAH0GyrsfDf6FM3CqFc)
- HWinfo64 - [Download](https://www.hwinfo.com/download/)
- Old & new BIOS file of your motherboard

## Preparations
1. Install **Python.**
2. Extract the old & new BIOS files in seperate folder.
3. Extract `UBU_v1_80_a17_fixed.zip`. 
4. Open **Hwinfo64** and take note CPU ID from there.

## How to do it (Step-by-Step)

{% include embed/youtube.html id='DUPY8S8B-04' %}

> Flashing modified BIOS may brick your motherboard.
{: .prompt-danger }

### Part 1: Extracting Old Microcode from the Old BIOS File

1. Delete `bios.bin` from the **UBU** folder if present.
2. Open `UBU.cmd` and select your old BIOS file (e.g., `E7B53IMS.110`).
3. Choose **Do not use MMTool** (press `0`).
4. Select **CPU Microcode** (press `5`).
5. Press `X` to extract all CPU microcodes, then close the window.
6. Go to `.\Extracted\Intel`, find the file matching your CPU ID (e.g., `cpu906EA_...`), and copy it.
7. Paste it into `.\Files\intel\mCode\USR_mCode`.
8. Run `GenUSRmC.bat` in `.\Files\intel\mCode`, then close it.
9. **Part 1 complete.**

### Part 2: Replacing the Microcode in the New BIOS File

1. Delete `bios.bin` from the **UBU** folder if present.
2. Open `UBU.cmd` and select your new BIOS file (e.g., `E7B53IMS.1D0`).
3. Choose **Do not use MMTool** (press `0`).
4. Select **CPU Microcode** (press `5`).
5. Press `U` to replace microcode using `USR_mCode.txt`.
6. Confirm the “Checksum correct” message.
7. Press `R` to start the replacement, then press any key.
8. Exit the tool, rename the new file if necessary (e.g., `mod_E7B53IMS.1D0`), and flash it.
9. **Part 2 complete.**

You can proceed to flash the BIOS that you have modified.

> Flashing modified BIOS may brick your motherboard.
{: .prompt-danger }

| Before | After |
| --- | ----- |
| ![MSI_SnapShot.jpg](MSI_SnapShot.jpg) | ![MSI_SnapShot_01.jpg](MSI_SnapShot_01.jpg) |

## Research  
- [Update Your CPU BIOS Microcode - More Performance - Less Consumption - BIOS Modding - Overclocking](https://www.youtube.com/watch?v=MzGGIkLFO8A)
- [Latest Overclocking Programs, System Info, Benchmarking, & Stability Tools
](https://www.tweaktownforum.com/forum/tech-support-from-vendors/gigabyte/30823-latest-overclocking-programs-system-info-benchmarking-stability-tools)
- [[Tool Guide+News] “UEFI BIOS Updater” (UBU)](https://winraid.level1techs.com/t/tool-guide-news-uefi-bios-updater-ubu/)

