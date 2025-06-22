---
published: true
subtitle: Step-by-step guide
media_subpath: /tmnet_unifi-openwrt-setup/
image:
  path: owrt.png
  alt:
tags:
  - OpenWrt
  - Networking
title: Configuring TMNet UniFi ISP through OpenWrt Web Interface
---
UniFi is a popular internet service provider in Malaysia, and OpenWrt is a free and open-source firmware for routers that allows for greater control and customization. This tutorial will guide you through the process of configuring UniFi on your OpenWrt router using the web interface.

## Step 1: Connect to your OpenWrt router

Connect your computer to the router via Ethernet cable or Wi-Fi, and access the router's web interface by typing the IP address into your web browser's address bar. The default IP address for OpenWrt is **192.168.1.1**.

## Step 2: Navigate to Network Interfaces

From the web interface, navigate to **Network » Interfaces**. Here, you can configure your router's network interfaces.

![status](status_network_interface.webp "Network>Interfaces")

## Step 3: Configure WAN interface

Under the WAN section, click on **Edit**.

![wan_edit](wan_edit.webp "Edit WAN Interface")

In the General settings tab, set the following:

Protocol: **PPPoE**  
Click on **Switch protocol**  

![wan_protocol](wan_protocol.webp "Interfaces » WAN, Protocol: PPPoE")

Under the **Device** section, you will need to manually type the device name **wan.500** & hit **Enter**.

![wan_device_vlan500](wan_device_vlan500.webp "Interfaces » WAN, Device: wan.500")

In the PAP/CHAP username field, enter your UniFi account login, for example, **adbdulwahub69@unifi**. In the PAP/CHAP password field, enter your UniFi account password.

Click on **Save** to save your settings.

![wan_pppoe_info](wan_pppoe_info.webp "Interfaces » WAN, PPPoE username & password")

## Step 4: Configure WAN6 interface

Under the WAN6 section, click on **Edit**. 

![wan6_edit](wan6_edit.webp "Edit WAN6 Interface")  

Under the **Device** section, select **Alias Interface: @wan**.

![wan6_device](wan6_device.webp "Interfaces » WAN6, Device: @wan")

Click on **Save** and then click on **Save & Apply** to apply the changes.

![save_apply](save_apply.webp "Save & Apply")

## Step 5: Verify connection

To verify that your UniFi connection is working, navigate to **Network » Diagnostics** and click on **IPv4 Ping**. If the ping is successful, then your UniFi connection is working properly.

Congratulations, you have successfully configured your UniFi connection on your OpenWrt router!

![network_diagnostics](network_diagnostics.webp "Network » Diagnostics")

## Research

* [[klseet.com] - OpenWRT 21.02.0-rc2 Vlans for TM-UniFi Home](https://klseet.com/networking/router-firmware/openwrt/openwrt-21-02-0-rc2-vlans)
* [[Telegram @gilagajet] - Guna router OpenWRT sebagai router Unifi
](https://telegra.ph/Guna-router-OpenWRT-sebagai-router-Unifi-01-04)
* [[Gao's Blog] - OpenWrt Installation and Configuration on D-LINK DIR-882-A1](https://vitaminac.github.io/D-LINK-DIR-882-A1-OpenWrt/)
