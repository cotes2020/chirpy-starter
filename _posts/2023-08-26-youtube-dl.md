---
title: Downloading YouTube Videos and Audio using youtube-dl
date: 2023-08-26 21:19:14
categories: [Blogging]
tags: [youtube, blog]
pin: true
image:
    path: /assets/images/youtube-dl.png
    alt: youtube-dl running on MacOS M1
---

> youtube-dl is a command-line program to download videos from YouTube.com and a few more sites. It requires the Python interpreter, version 2.6, 2.7, or 3.2+, and it is not platform specific. It should work on your Unix box, on Windows or on macOS. It is released to the public domain, which means you can modify it, redistribute it or use it however you like.
{: .prompt-info }

## Introduction

At one point going to sketchy Youtube downloader websites just became too much with all the ADs and overall suspicious pop ups you would get while trying to either download an mp3 or mp4 from YouTube. 

Gone are these days though, while this tool in particular has been around for awhile it has it's perks. 
 - One, you no longer have to use sketchy websites. 
 - Two, you can look like a hacker man running the basic syntax to download YouTube videos.

 So now the question you're probably asking is; How do I use it?

 Easy, if you are like me and just want to have a copy and paste-able way to do either YouTube MP3's or MP4's I have two commands which can assist with that.

> This assumes you have already installed youtube-dl from the command line on your computer and installed all dependencies. For documentation on installation go here: https://github.com/ytdl-org/youtube-dl#installation 
{: .prompt-warning}

 
## Downloading YouTube MP4
 
 So maybe you are a data hoarder and want to save a video from YouTube before it gets taken down OR you have a favorite music video you'd like to have a personal copy of. I got you, here is the basic syntax to run to download an MP4. 

 In the terminal you would run the following syntax. 

 ```shell
 youtube-dl --format mp4 <insert YouTube link here> 
 ```
An example of how this looks is the following screenshot of this running: 

![Desktop View](/assets/images/youtube-dl.png){: width="972" height="589" }
_Downloading a full defcon 31 conference talk_

## Downloading YouTube MP3
This can come in handy if you have a song that may not be found else where and can be only found on YouTube and you desperately need to download it for safe keeping. Totally understandable by the way. 

You would run this command: 

```shell
youtube-dl -x --audio-format mp3 --prefer-ffmpeg <insert YouTube link here> 
```

Example of this running for a looped intro of The Weeknd - Is There Someone Else:

![Desktop View](/assets/images/youtube-dl-2.png){: width="972" height="589" }
_Downloading a Is There Someone Else Looped Intro_

## Issues
One of the issues I've had recently with using this tool is when pasting my YouTube link into the end of the command, the link inserts with a couple of back slashes:

![Desktop View](/assets/images/youtube-dl-3.png){: width="972" height="589" }
_Pasted link formats link with additional back slashes upon paste_

> The following syntax is incorrect and is only shown here for demonstration.
{: .prompt-warning}

```shell
youtube-dl --format mp4 "https://www.youtube.com/watch\?v\=G0JKdFjWkLA\&list\=RDlbbDOdDYXWg\&index\=2"
```

Due to this, the command may not run correctly. To fix this, you would simply remove any of the `\` in the youtube link and try again. It would then look like this:

```shell
youtube-dl --format mp4 "https://www.youtube.com/watch?v=G0JKdFjWkLA&list=RDlbbDOdDYXWg&index=2"
```

By removing all `\` from the link, the video OR audio will be able to download just fine. :)

## Conclusion
While I am sure there are plenty of ways to craft you syntax to work for certain use cases. This guide should be for those who just want to get started with basic downloads of MP3 and MP4s. 

Thank you for reading and perhaps following along. See you in the next one! 

## GitHub Repo and Installation Guides

youtube-dl GitHub Repo: https://github.com/ytdl-org/youtube-dl#installation

Install youtube-dl on Windows: https://www.youtube.com/watch?v=XebaoWchKxI

Install youtube-dl on MacOS: https://techwiser.com/how-to-install-youtube-dl-on-mac/
