---
title: "SekaiCTF 2025 – My Flask App (Web)"
date: 2025-09-23 23:30:00 +0300
categories: [CTF, Web]
tags: [SekaiCTF, Flask, LFI, RCE, Writeup]
description: "1st Place – SekaiCTF 2025 Writeup Contest."
---

## TL;DR

The app had two critical issues: an arbitrary file-read (LFI) at `/view?filename=...` which allowed reading `/proc/mounts` and thus leaked the bind-mounted flag filename `/flag-<32chars>.txt`, and **Flask `debug=True`** exposed a Werkzeug PIN-gated debugger — by reconstructing the PIN you can unlock the interactive debugger and gain remote RCE.

---

**Challenge:** [My Flask App](https://2025.ctf.sekai.team/challenges/#My-Flask-App-12)<br>**Author:** [belugagemink](https://sekai.team/members/beluga)  

Greetings,

When I was playing **Sekai CTF 2025**, one challenge that stuck with me was called **My Flask App**. At first glance it looked like just another boring Flask file-read problem, but it turned out to have a neat twist. Here’s how I went from staring at the Dockerfile to pulling the flag out of nowhere.

---

## Opening the Box

The first thing I always do with web challenges is check the **Dockerfile**. That’s usually where the authors leave little hints.

This one looked straightforward — install Flask, copy in the app, start the server. Nothing surprising… until I noticed what it did with the flag:

```docker
FROM python:3.11-slim

RUN pip install --no-cache-dir flask==3.1.1

WORKDIR /app

COPY app .

RUN mv flag.txt /flag-$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1).txt && \
    chown -R nobody:nogroup /app

USER nobody

EXPOSE 5000

CMD ["python", "app.py"]
```

Aha. So the flag wasn’t at `/flag.txt`. Instead, every time the container spun up, it got renamed to something like `/flag-VenUXnNXjh9MJxOH6m8xHvAR2oG9cmmG.txt`

A 32-character random suffix. No way I was going to brute-force that. I knew the game now: the vulnerability would be trivial, but finding the *flag path* would be the real puzzle.

---

## Peeking Inside the Flask App

Next stop: `app.py`. And sure enough, the code was as barebones as it gets:

```python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/view')
def view():
    filename = request.args.get('filename')
    if not filename:
        return "Filename is required", 400
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content, 200
    except FileNotFoundError:
        return "File not found", 404
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

- `debug=True` → At the time, I brushed it off. “Probably just left in by the author for testing” I thought. It didn’t seem like something exploitable, because even with debug mode on, I’d still need the Werkzeug PIN to interact with anything useful. So, I kept moving and focused on other parts of the app.
- `/` → serve an index page.
- `/view` → takes a `filename`, opens it, and dumps the content.

No filters. No checks. Nothing.

I didn’t even need to think twice — this was **arbitrary file read** on a silver platter.

The exploit part was done. The mystery was still: *how do I find the randomized flag filename?*

---

## Chasing the Flag

At this point, I went through my mental checklist. With arbitrary file read, you basically have the whole container at your fingertips, so the question is **where to look**.

`/proc` is always an interesting target in Linux — it’s full of runtime metadata. I started poking around: `/proc/self/cmdline`, `/proc/self/environ`, and then I remembered: *mounts*.

I pulled up `/proc/mounts`:

```
/view?filename=/proc/mounts
```

And right there, staring back at me, was the jackpot:

```
/dev/nvme0n1p1 /flag-VenUXnNXjh9MJxOH6m8xHvAR2oG9cmmG.txt ext4 ro,...
```

The entire randomized flag path, exposed in plain text.

---

## Why Did That Work?

At first I was a little surprised. Why would the random flag filename show up in the mount table?

Then it clicked: the challenge wasn’t just *copying* the flag file into the container — it was **bind-mounting** it.

A bind mount in Linux is when you take an existing file or directory and mount it somewhere else in the filesystem. Unlike plugging in a new drive, it’s just a second reference to the same underlying data.

And since all mounts have to be tracked by the kernel, they all end up listed in `/proc/mounts`. Which means… the container basically snitched on itself.

> **Note:** We can also use `/proc/self/mountinfo` only difference is `/proc/mounts` is a simplified, legacy view of mounted filesystems, while `/proc/self/mountinfo` is the detailed, canonical kernel view with extra metadata like IDs and propagation flags.

---

## The Final Step

Armed with the path, it was just a matter of reading the file like any other:

```bash
curl "http://server/view?filename=/flag-VenUXnNXjh9MJxOH6m8xHvAR2oG9cmmG.txt"
```
Boom. Out came the flag:

```
SEKAI{!s-+h1s_3VEN_<all3d_a_cv3}
```

![CTF Victory](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3NzaWRoajVyc2ZxdXF5Mm44eXZiYXVjZG8yNXBmNDUwMWg5NmJqYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WMa7eMMZQ16uc/giphy.gif){: .text-center }

---

## The intended Solution

When I looked at the intended solution later, I was stunned. That single line, `debug=True`, was the gateway to the whole exploit.

Here’s how it unfolded:

1. **File Disclosure**
    
    The `/view?filename=...` endpoint gave us arbitrary file reads. Using it, I could grab sensitive system values like:
    
    - `/sys/class/net/eth0/address` → the MAC address
    - `/proc/sys/kernel/random/boot_id` → the boot ID
2. **Rebuilding the PIN**
    
    Flask’s debugger console isn’t wide open — it generates a secret PIN using a mix of “public bits” (username, module name, Flask app path) and “private bits” (the MAC + boot ID).
    
    By replicating Werkzeug’s `get_pin` function, I could calculate the exact PIN the server expected.
    
3. **Bypassing Host Checks**
    
    Normally, access to the debugger console is restricted. But by sending requests with `Host: 127.0.0.1`, I was able to trick the app into thinking I was local. This exposed the hidden `SECRET` value directly from `/console`.
    
4. **Authenticating to the Console**
    
    With the computed **PIN** and the leaked **SECRET**, I called `pinauth` and received a valid session cookie for the debugger console.
    
5. **Remote Code Execution**
    
    Once authenticated, the debugger console gave me full Python code execution.

The intended chain was: **LFI → PIN reconstruction → SECRET leak → debugger auth → RCE → flag**.

Official solve can be found [here](https://github.com/project-sekai-ctf/sekaictf-2025/blob/main/web/my-flask-app/solution/solve.py).

Looking back, I realize the real hint was sitting right there in the open — `debug=True` — I just underestimated it.

## Final Thoughts

What I really enjoyed about *My Flask App* was how it played on expectations. At first glance it screamed *“just another Flask LFI”*, but the randomized flag path flipped the script. Instead of brute force or guesswork, the challenge nudged you to think about **what Linux exposes by design**.

The beauty was in the duality of solutions:

- The **bind-mount leak** route — where `/proc/mounts` betrayed the randomized filename.
- The **debug=True route** — where replicating Werkzeug’s PIN logic unlocked the powerful Flask debugger for full RCE.

Both paths taught a valuable lesson: even the most trivial vulnerabilities (like arbitrary file read or a forgotten `debug=True`) can snowball into full compromise if you understand the environment well enough.

That’s what made this problem stick with me — it wasn’t about grinding through payloads, but about *observing carefully, connecting the dots, and leveraging the system against itself*.

Thanks for reading!