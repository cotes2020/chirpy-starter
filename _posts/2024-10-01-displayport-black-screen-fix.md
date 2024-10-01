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
---
### Background:

Let me tell you about my first experience using DisplayPort on my Nvidia GPU! I’ve never had the luxury of owning a high-res or ultrawide monitor, so DisplayPort was totally new to me. 

I finally got a brand new monitor, but to my surprise, the screen stayed blank during the first few seconds of boot! Turns out, it wouldn’t show anything in the BIOS. After a quick Google search, I found the fix, and here's how:

**The Issue:**  
Black screen during boot when using a DisplayPort 1.3/1.4 monitor with an NVIDIA GPU.  
**So, What Causing This?**  
Outdated GPU firmware can’t handle the DisplayPort standard until the OS loads.

### Symptoms:
- Screen stays black during boot but works after OS loads.
- System may hang on boot.
- Switching to HDMI temporarily fixes it.

### The Fix (Step-by-Step):

**1. Download NVIDIA’s Firmware Update Tool:**  
[Get it here](https://www.nvidia.com/en-us/drivers/nv-uefi-update-x64/).

**2. Run the Tool:**  
It will check if your GPU firmware is outdated. Follow the prompts to update it.

**3. Restart:**  
Once updated, your black screen issue during boot should be resolved.

### Quick Tips:
- **Temporary Fix:** Use HDMI until you can update the firmware.
- **Keep Drivers Updated:** Regular updates help prevent future issues.

### Conclusion:  
Updating your firmware will fix the issue, making your DisplayPort connection work seamlessly from boot to desktop.


