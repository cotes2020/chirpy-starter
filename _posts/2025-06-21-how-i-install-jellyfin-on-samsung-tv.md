---
title: How I Install Jellyfin on Samsung TV
description: Running TizenOS 6.0
date: 2025-06-21 15:00:00 +0800
categories: How-to, Tizen]
tags: [jellyfin]     # TAG names should always be lowercase
media_subpath: /azimstech.github.io/
image:
  path: jellfin-plus-tizen.png
---

There's many other ways of installing it but I found this is the easiest way that nobody talked about.

## Tools & Downloads

- Samsung Smart TV (in my case AU7002 4K TV) connected on the same network as your PC. 
- Latest **TizenBrew Device Manager** for your operating system:  
  Download from the [TizenBrew Device Manager releases page](https://github.com/reisxd/tizenbrew-device-manager/releases/latest).
- Latest **Jellyfin.wgt** widget package:  
  Download from the [jeppevinkel/jellyfin-tizen-builds releases page](https://github.com/jeppevinkel/jellyfin-tizen-builds/releases/latest).

---

## Simple Step-by-Step Instructions

1. **Set Host PC IP Address**  
   - Change the Host PC IP address in your Developer settings to your PC’s IP address. [Follow this guide](https://developer.samsung.com/smarttv/develop/getting-started/using-sdk/tv-device.html#Connecting-the-TV-and-SDK).  
   - Install & Launch the TizenBrew Device Manager application on your PC. Look up in Task Manager, mine is `192.168.0.176`
   - Navigate to the **Connect Device** page and connect to your Samsung TV. Enter your TV's IP address eg: `192.168.0.158`

3. **Install Jellyfin Widget**  
   - After connecting, go to the **Apps** page in the Device Manager.  
   - Click the **Install App** button.  
   - Select the downloaded Jellyfin.wgt widget package and click **Install**.  
   - Wait for the installation logs to confirm the app has been installed successfully.

4. **Reset Host PC IP Address**  
   - Change the Host PC IP address back to `127.0.0.1` in your SDK settings following the same official guide.

5. **Launch Jellyfin on TV**  
   - On your Samsung Smart TV, locate and launch the newly installed TizenBrew app.

---

> Tested on Samsung UHD 4K AU7002 TV (Tizen 6.0) as of June 2025.  
> For detailed information about Jellyfin widget, refer to [eppevinkel/jellyfin-tizen-builds](https://github.com/jeppevinkel/jellyfin-tizen-builds?tab=readme-ov-file#jellyfin-tizen-builds)
{: .prompt-info }