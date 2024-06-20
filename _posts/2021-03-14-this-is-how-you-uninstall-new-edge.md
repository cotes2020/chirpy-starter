---
layout: post
published: false
title: This is How You Uninstall New Edge
---
## A New Post

Enter text in [Markdown](http://daringfireball.net/projects/markdown/). Use the toolbar above, or click the **?** button for formatting help.

## Take Ownership of Registry Keys
1. Open Registry Editor
2. Navigate to `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Microsoft Edge`
3. Right click `Microsoft Edge` folder. Click `Permissions...`
4. Click `Advanced` >> `Change` 
5. Type your User name >> `Check Names` >> `OK`
6. Select `SYSTEM` principal


{: .box-warning} reg delete "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Microsoft Edge" /v NoRemove /f  



{: .box-warning} reg delete "HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Microsoft Edge" /v NoRemove /f  

