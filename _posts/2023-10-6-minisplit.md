---
title: Cooling My Homelab
date: 2023-10-06 10:13:00 -500
categories: [homelab,diy, cooling]
tags: [homelab,diy,minisplit,cooling]
---

# Cooling My Garage with a Mini-Split

The best place to build my homelab is in my detached garage. The problem is that there is no AC and the temps are way too hot in the summer.

My solution: install a mini-split air conditioner. This proved to be a challenging project but I'm happy with how it turned out.

I won't go into detail about the install process (there are tons of great tutorials on youtube).

![minisplit](https://github.com/PostOakLab/assets/blob/master/minisplit.JPG?raw=true)

This unit required a 220v disconnect, so I had to replace the garage's subpanel with a larger box to accomodate more breakers. Then I ran a wire from a 220v breaker to an AC disconnect which I installed on the outside.

These units are pre-charged with coolant so once I connected the high and low pressure lines I released the coolant and had cold air!

One issue: I learned the hard way that the PCBs in these units are sensitive to power surges. We had a thunderstorm which fried the PCB.

![pcb](https://github.com/PostOakLab/assets/blob/master/minisplitpcb.JPG?raw=true)

Fortunately the company sent me a replacement PCB. Once I swapped it out it started right up. To protect the PCB from future surges I also installed this surge protector to the disconnect.

![surgeprotector](https://github.com/PostOakLab/assets/blob/master/minisplitsurgeprotector.JPG?raw=true)
