---
layout: post
published: true
title: Configuring OpenWrt via Command Line
subtitle: A Step-by-Step Guide for TMNet UniFi Users
media_subpath: /azimstech.github.io/
image:
  path: openwrt-cli.png
  alt:
tags:
  - OpenWrt
  - Networking
permalink: /2023-02-22-tmnet-unifi-with-openwrt-22.03.x-dsa/
date: '2023-02-22'
---
I'll be sharing my personal experience on how to configure OpenWrt via command line for TMnet ISP. With just a few simple commands, you can easily set up your router to work with your ISP and get your network up and running in no time.

When configuring OpenWrt via command line for TMnet ISP, I prefer to use Windows PowerShell (**Win** + **X** >> **Windows Powershell**). Here are the steps I follow:

## SSH into OpenWrt Router

```bash
rm -r  "~\.ssh"
ssh root@192.168.1.1
```

{: .box-note} 
Next time I can simply use `ssh root@192.168.1.1`

## How to tell: DSA vs Swconfig

To determine if my router uses DSA or Swconfig, I use the following commands:

**DSA** (eg: Mi Router 4A, D-Link DIR-882, Linksys E8450)
```bash
swconfig list
-ash: swconfig: not found
```
**Swconfig** (eg: Tp-Link Archer C7, D-Link DIR-842)

```bash
swconfig list
Found: switch0 - mdio.0
```

{: .box-error} 
If my router uses Swconfig, I follow [this guide](https://gist.github.com/AzimsTech/0404429cc82f8b7c8e7373bde4db1bef) instead.

## Set up UniFi PPPoE Username & Password  

To set up my UniFi PPPoE username and password, I use the following commands:

```bash
PPPOE_USERNAME=xxxx@unifi
PPPOE_PASSWORD=xxxxxxxxxxxxxx
DNS_1=1.1.1.1
DNS_2=8.8.8.8
DNS6_1=2606:4700:4700::1111
DNS6_2=2001:4860:4860::8888
uci set network.wan.proto='pppoe'
uci set network.wan.username=$PPPOE_USERNAME
uci set network.wan.password=$PPPOE_PASSWORD
uci set network.wan.device='wan.500'
uci set network.wan.ipv6='1'
uci set network.wan.peerdns='0'
uci set network.wan.dns="$DNS_1 $DNS_2"
uci set network.wan6.proto='dhcpv6'
uci set network.wan6.device='@wan'
uci set network.wan6.peerdns='0'
uci set network.wan6.dns="$DNS6_1 $DNS6_2"
uci commit network
ifup wan
echo 'Waiting for link to initialize'
sleep 20
```

## Extras

### Set Router Passsword

To set a new root password for my router, I use the following command:

```bash
echo 'Updating root password'
NEWPASSWD=123
passwd <<EOF
$NEWPASSWD
$NEWPASSWD
EOF
```

### Set Correct Timezone 

To set the correct timezone, I use the following commands:

```bash
TIMEZONE='<+08>-8'
ZONENAME='Asia/Kuala Lumpur'
echo 'Setting timezone to' $TIMEZONE
uci set system.@system[0].timezone="$TIMEZONE"
echo 'Setting zone name to' $ZONENAME 
uci set system.@system[0].zonename="$ZONENAME"
uci commit system
/etc/init.d/system reload
```

### Set Router Hostname

To set the router hostname, I use the following commands:

```bash
HOSTNAME="LiNKSYS"
uci set system.@system[0].hostname=$HOSTNAME
uci set network.lan.hostname="`uci get system.@system[0].hostname`"
uci commit system
/etc/init.d/system reload
```

### Install Optional Packages

```bash
opkg update                # retrieve updated packages
opkg install luci-app-sqm  # install the SQM modules to get fq_codel etc
opkg remove wpad-basic-wolfssl  # remove the non-mesh version of wpad
opkg install wpad-mesh-wolfssl  # Install the mesh supporting version
opkg intall luci-app-attendedsysupgrade # Install Attended Sysupgrade for keeping firmware up-to-date
```

With these commands, you can easily set up your router and get your network up and running. And the best part? You did it all from the command line, which can be a powerful tool for networking professionals. I hope this guide has been helpful to you. If you have any questions or feedback, feel free to leave a comment below.

## Research

- [SSH access for newcomers
](https://openwrt.org/docs/guide-quick-start/sshadministration)
- [richb-hanover
/
OpenWrtScripts](https://github.com/richb-hanover/OpenWrtScripts#opkgscriptsh)
- [How to tell whether device has network switch ports (DSA vs swconfig)?](https://forum.openwrt.org/t/how-to-tell-whether-device-has-network-switch-ports-dsa-vs-swconfig/128721/11)
