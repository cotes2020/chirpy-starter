---
title: DisplayPort Black Screen Fix
description: Fix black screen on boot with DisplayPort 1.3/1.4 and NVIDIA GPU
author: null
date: '2024-09-21 07:20:00 +0800'
categories:
  - Tips
tags:
  - PC
pin: false
math: false
mermaid: false
media_subpath: /azimstech.github.io/
image:
  path: displayport-art.png
  alt: 
---

## The Issue: 
Black screen during boot when using a DisplayPort 1.3/1.4 monitor with an NVIDIA GPU.  
**So, What Causing This?**  
Outdated GPU firmware can’t handle the DisplayPort standard until the OS loads.

## Symptoms:
- Screen stays black during boot but works after OS loads.
- System may hang on boot.
- Switching to HDMI temporarily fixes it.

## The Fix (Step-by-Step):

1. **Download NVIDIA’s Firmware Update Tool:**  ![alt text](https://cdn.statically.io/gh/AzimsTech/compress/master/azimstech.github.io/image-2.png){: width="972" height="589" .w-50 .right}  
[Get it here](https://www.nvidia.com/en-us/drivers/nv-uefi-update-x64/).

2. **Run the Tool:**  
It will check if your GPU firmware is outdated. Follow the prompts to update it.

3. **Restart:**  
Once updated, your black screen issue during boot should be resolved.

## Quick Tips:
- **Temporary Fix:** Use HDMI until you can update the firmware.
- **Keep Drivers Updated:** Regular updates help prevent future issues.

## Conclusion:  
Updating your firmware will fix the issue, making your DisplayPort connection work seamlessly from boot to desktop.


