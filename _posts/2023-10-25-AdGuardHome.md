---
title: Install AdGuard Home on Raspberry Pi
date: 2023-10-25 07:30:00 -500
categories: [DNS,homelab, AdGuard, projects]
tags: [DNS,homelab,raspberrypi, AdGuard]
---

# AdGuard Home on Raspberry Pi

Using [this guide](https://github.com/AdguardTeam/AdGuardHome/wiki/Raspberry-Pi) I installed AdGuard home on a Raspberry Pi in order to run a home DNS server that will block ads and malicious websites.

This assumes you already have an OS installed on your Pi and you can ssh to the pi using the IP address.

1. Download with this command:
`cd
wget 'https://static.adguard.com/adguardhome/release/AdGuardHome_linux_armv6.tar.gz'
tar -f AdGuardHome_linux_armv6.tar.gz -x -v``

2. Install with this command:
`cd ./AdGuardHome/
sudo ./AdGuardHome -s install``

 
