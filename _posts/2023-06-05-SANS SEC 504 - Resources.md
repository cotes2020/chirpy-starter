---
title: SANS SEC 504 - Resources
date: 2023-08-23 15:35:56
catagories: [cybersecurity, malware, red team tools]
tags: [SANS, SEC504, GCIH, cybersecurity]
---

> Here are some valuable resouces that were recommended when taking the SANS SEC504 course. 
{: .prompt-info }

## Malware stuff
https://digitalcommons.lsu.edu/cgi/viewcontent.cgi?article=6527&context=gradschool_theses

https://github.com/volatilityfoundation/volatility/wiki/Mac

## Volatility
A few volatility resources:  

- [https://github.com/volatilityfoundation/volatility/wiki](https://github.com/volatilityfoundation/volatility/wiki)
- [https://forwarddefense.com/media/attachments/2021/05/15/memory-analysis-with-volatlity-analyst-reference-20200131.pdf](https://forwarddefense.com/media/attachments/2021/05/15/memory-analysis-with-volatlity-analyst-reference-20200131.pdf)
- [https://andreafortuna.org/2019/04/03/how-to-analyze-a-vmware-memory-image-with-volatility/](https://andreafortuna.org/2019/04/03/how-to-analyze-a-vmware-memory-image-with-volatility/)

(edited)

Andrea Fortuna

[How to analyze a VMware memory image with Volatility](https://andreafortuna.org/2019/04/03/how-to-analyze-a-vmware-memory-image-with-volatility/)

A very brief post, just a reminder about a very useful volatility feature. The process on a VMware machine is more simple than VirtualBox, just 4 simple steps: Suspend the virtual machine Navigate to the virtual machine's directory and identify the `*.vmem` file Copy the vmem image to you analysis workstation  Finally use the following Volatility command to convert the memory image to a dump ready for analysis: `$ volatility -f memory_image.vmem -O raw_image --profile=Win8SP0x86 raw2dmp` Now the memory dump can be analyzed with the usual methods. 

## Berkley Packet Filters

Berkeley packet filters

Berkeley Packet Filters (BPF) provide a powerful tool for intrusion detection analysis. Use BPF filtering to quickly reduce large packet captures to a reduced set of results by filtering based on a specific type of traffic. Both admin and non-admin users can create BPF filters.

Review the following sections to learn more about creating BPF filters:

-   [Primitives](https://www.ibm.com/docs/en/qsip/7.5?topic=queries-berkeley-packet-filters#c_forensics_bpf__primitives)
-   [Protocols and operators](https://www.ibm.com/docs/en/qsip/7.5?topic=queries-berkeley-packet-filters#c_forensics_bpf__prot_operators)
-   [BPF filter examples](https://www.ibm.com/docs/en/qsip/7.5?topic=queries-berkeley-packet-filters#c_forensics_bpf__bpf_examples)

### Primitives

Primitives are references to fields in a network protocol header, such as host, port, or TCP port. The BPF syntax consists of one or more primitives, which usually consist of an ID, typically a name or number, which is preceded by one or more qualifiers.

**Type qualifiers**

Type qualifiers identify the kind of information that the ID name or number refers to. For example, the type might refer to `host`, `net`, `port`, or `portrange`. When no type qualifier exists, `host` is assumed.

**Dir qualifiers**

`Dir` qualifiers specify the transfer direction in relation to the ID. For example, the dir qualifier might be `src`, `dst`, or `src` or `dst`.

**Proto qualifiers**

The `proto` qualifier restricts the match to a particular protocol. Possible protocols are `ether`, `fddi`, `tr`, `wlan`, `ip`, `ip6`, `arp`, `rarp`, `decnet`, `TCP`, or `UDP`.


#### References: 

https://www.ibm.com/docs/en/qsip/7.4?topic=queries-berkeley-packet-filters

https://github.com/sbabicz/tcpdump-bpf-cheatsheet

## Grouped Managed Service Accounts Overview

https://learn.microsoft.com/en-us/windows-server/security/group-managed-service-accounts/group-managed-service-accounts-overview





## How much does a DDoS cost?

As per the Dark Web Price Index 2022, a 24-hour DDoS attack with 20-50k requests per second can cost the attacker as little as $200 USD. This low cost of entry means that even small-time attackers can launch devastating DDoS attacks that can cripple businesses and cause significant financial losses. Mar 10, 2023

https://sans-live-training.slack.com/archives/C059WKMLLDB/p1686064393422589

[https://www.linkedin.com/pulse/true-cost-ddos-attack-protect-your-business-proactive-ali-el-tom/](https://www.linkedin.com/pulse/true-cost-ddos-attack-protect-your-business-proactive-ali-el-tom/)

![linkedin.com](https://slack-imgs.com/?c=1&o1=wi32.he32.si&url=https%3A%2F%2Fstatic.licdn.com%2Faero-v1%2Fsc%2Fh%2Fal2o9zrvru7aqj8e1x2rzsrca)linkedin.com

[The True Cost of a DDoS Attack: Protect Your Business with Proactive Measures](https://www.linkedin.com/pulse/true-cost-ddos-attack-protect-your-business-proactive-ali-el-tom/)

Launching a DDoS attack can be relatively inexpensive for the attacker. As per the Dark Web Price Index 2022, a 24-hour DDoS attack with 20-50k requests per second can cost the attacker as little as $200 USD.

#### MITRE ATT&CK

- CWE (Common Weakness Enumeration)

#### Background Reports 

Our disclaimer on Background Reports:  
DISCLOSURE/DISCLAIMERThe information in this report is based on public, non-public, private, and proprietary databases. Search results may not be complete or accurate. Not all states or counties report or make available all records in electronic format. Online databases could contain incomplete information, duplication, inaccuracies, or false matches based on common names.Certified copies can be obtained and in-person/on-site verification of research results can be performed but will require        additional investigative time and expenses that must be authorized.The general format of this report and parts of this report are produced from xxxxxxx. Information obtained from xxxxxx, and other public and private databases, does not constitute a "consumer report" as that term is defined in the federal Fair Credit Reporting Act, 15 USC 1681 et seq.(FCRA).As data from xxxxxxxx and other data sources is not specifically segregated, this report may not be used in whole or in part as a factor in determining eligibility for credit, insurance, employment, or another permissible purpose under the FCRA.Any questions, comments or concerns related to the information contained in this report should be directed to:  
Keith Olive Enterprises, LLC  
PO Box 26  
Mountain Home, Texas 78058  
Texas Private Security Bureau License #A19867

> OSINT on employees without permission will bite you big time if they ever bring up a LABOR board issue or lawsuit.
{: .prompt-tip }

## Cheat sheets

https://packetlife.net/library/cheat-sheets/


## What 2 Log

https://what2log.com/

