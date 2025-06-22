---
title: Fixing Component Store (WinSxS folder) in Windows 11 24H2
date: '2025-03-20 21:00:00 +0800'
categories:
  - How-to
  - Software
tags:
  - win11
media_subpath: /azimstech.github.io/
image:
  path: windows11-update-cover.png
---

## Problem

After the Windows 11 24H2 update, a bug prevents the cleanup tool from removing two WinSxS packages. Cleanup commands don’t work, and Microsoft hasn’t fixed it yet.

```console
PS C:\> Dism.exe /Online /Cleanup-Image /AnalyzeComponentStore

Deployment Image Servicing and Management tool
Version: 10.0.26100.1150

Image Version: 10.0.26100.3613

[==========================100.0%==========================]

Component Store (WinSxS) information:

Windows Explorer Reported Size of Component Store : 5.60 GB

Actual Size of Component Store : 5.52 GB

    Shared with Windows : 3.81 GB
    Backups and Disabled Features : 1.70 GB
    Cache and Temporary Data :  0 bytes

Date of Last Cleanup : 2025-03-20 18:21:30

Number of Reclaimable Packages : 2
Component Store Cleanup Recommended : Yes

The operation completed successfully.
```

## The Fix

Remove the problematic package by executing (replace the package name if it differs on your system):


```console
Dism.exe /online /remove-package /packagename:Package_for_RollupFix~31bf3856ad364e35~amd64~~26100.1742.1.10
```

```console
PS C:\> Dism.exe /online /Remove-Package /packagename:Package_for_RollupFix~31bf3856ad364e35~amd64~~26100.1742.1.10

Deployment Image Servicing and Management tool
Version: 10.0.26100.1150

Image Version: 10.0.26100.3613

Processing 1 of 1 - Removing package Package_for_RollupFix~31bf3856ad364e35~amd64~~26100.1742.1.10
[==========================100.0%==========================]
The operation completed successfully.
PS C:\> dism /online /cleanup-image /startcomponentcleanup

Deployment Image Servicing and Management tool
Version: 10.0.26100.1150

Image Version: 10.0.26100.3613

[==========================100.0%==========================]
The operation completed successfully.
```

After removal, run the cleanup command to finalize the process:

```console
Dism.exe /online /Cleanup-Image /StartComponentCleanup
```

```console
PS C:\> Dism.exe /online /Cleanup-Image /StartComponentCleanup

Deployment Image Servicing and Management tool
Version: 10.0.26100.1150

Image Version: 10.0.26100.3613

[==========================100.0%==========================]
The operation completed successfully.
```

## Result

Re-run the analyze command to ensure all reclaimable packages are cleared:

```console
Dism.exe /Online /Cleanup-Image /AnalyzeComponentStore
```

```console
PS C:\> Dism.exe /Online /Cleanup-Image /AnalyzeComponentStore

Deployment Image Servicing and Management tool
Version: 10.0.26100.1150

Image Version: 10.0.26100.3613

[==========================100.0%==========================]

Component Store (WinSxS) information:

Windows Explorer Reported Size of Component Store : 4.79 GB

Actual Size of Component Store : 4.75 GB

    Shared with Windows : 3.80 GB
    Backups and Disabled Features : 958.57 MB
    Cache and Temporary Data :  0 bytes

Date of Last Cleanup : 2025-03-20 18:26:39

Number of Reclaimable Packages : 0
Component Store Cleanup Recommended : No

The operation completed successfully
```

## Research
- [@Bree - ElevenForum.com](https://www.elevenforum.com/t/how-to-identify-reclaimable-packages-reported-as-count-by-dism-online-cleanup-image-analyzecomponentstore.30344/post-575823)
