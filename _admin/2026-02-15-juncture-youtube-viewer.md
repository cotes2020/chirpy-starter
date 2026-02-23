---
title: "Juncture: YouTube Viewer"
description: How to use the Juncture YouTube viewer in your Markdown posts.
permalink: /admin/juncture-youtube-viewer
date: 2026-02-22
media_subpath: /assets/posts/juncture
order: 12
juncture:
    mode: flat
    toolbar: false
---
<style>
    @media (min-width: 1650px) {
        #main-wrapper>.container {
            max-width: 1600px;
            padding-left: 1.75rem !important;
            padding-right: 1.75rem !important;
        }
    }
    .example {
        display: grid;
        gap: 1rem;
    }
    @media (min-width: 640px) {
        .example {
            grid-template-columns: 1fr 1fr;
        }
    }
    iframe {
        width: 100%;
    }
    pre .s2,
    pre .sx {
        white-space: pre-wrap;
        word-break: break-word;
    }
    .attribute {
        color: red;
        font-weight: bold;
    }
</style>

## Overview

The Juncture YouTube Viewer embeds a YouTube video in your page as a clean, responsive preview. It looks similar to a standard embedded video, but behaves differently when clicked.

When a reader clicks the preview, Juncture opens a **larger, expanded viewer** using the full available screen width. This gives the reader a much better viewing experience without forcing a large player on the page itself.

This two-mode design keeps your article layout clean and readable while still making video a first-class part of the content.

### Preview Mode and Expanded Mode

The viewer operates in two modes:

**Preview mode** (default) renders a compact, non-playing embed in the page. The player is intentionally inactive — clicking anywhere on it opens the expanded viewer. No video loads or plays until the reader chooses to watch.

**Expanded mode** opens automatically when the reader clicks the preview. The video loads in a large dialog at full width and, if configured, begins playing immediately at a specified time.

### Interactive Storytelling

Where the YouTube viewer goes beyond a simple embed is in **interactivity**.

You can link text in your article to viewer actions, such as:

- `playat` — open the expanded viewer and begin playing at a specific timestamp

This allows your writing to direct the reader to the right moment in a video. Instead of saying "see the scene at 2:30," the reader can click a link and the video opens and plays from exactly that point.

---

In short:

- Use a standard YouTube embed when you simply need a video in the page.
- Use the Juncture YouTube Viewer when timing, interactivity, or a clean layout matters.

## Attributes

### Required Attributes

You must provide a **vid** attribute.

---

#### vid
{: .attribute }

The YouTube video ID. This is the short code found in the video's URL after `?v=`.

    vid="dQw4w9WgXcQ"

For the URL `https://www.youtube.com/watch?v=dQw4w9WgXcQ`, the ID is `dQw4w9WgXcQ`.

---

### Optional Attributes

These improve presentation and control playback but are not required.

---

#### caption
{: .attribute }

Text displayed below the video in the caption bar. If omitted, the video's title is fetched automatically from YouTube.

    caption="Apollo 11 Moon Landing, July 1969"

Use a caption when you want to provide context that differs from the YouTube title, or to avoid a network request on page load.

---

#### autoplay
{: .attribute }

When present, the video begins playing automatically when the expanded viewer opens.

    autoplay="true"

Autoplay only applies in expanded mode. The preview in the page is always inactive regardless of this setting.

> **Note:** Autoplay with sound requires the viewer to be served from a page that passes `allow="autoplay"` on its iframe. This is handled automatically by Juncture.

---

#### start
{: .attribute }

The time at which playback begins. Accepts either seconds or `h:mm:ss` format. Defaults to `0` if omitted.

    start="90"
    start="1:30"
    start="1:02:30"

When used with `autoplay`, the video opens and immediately begins playing from this position.

---

#### end
{: .attribute }

The time at which playback stops. Accepts either seconds or `h:mm:ss` format. If omitted, the video plays to its natural end.

    end="150"
    end="2:30"

The player pauses precisely at this time. Use `start` and `end` together to highlight a specific clip within a longer video.

---

#### id
{: .attribute }

An identifier for the viewer, required when using action links.

    id="vid1"

The `id` is used by action links in the article text to target this specific viewer. See the [Action Link Example](#action-link-example) below.

---

## Examples

### The Simplest Example

This creates a video preview that when clicked will open the expanded viewer.

<div class="example">

<div markdown="1">
{% raw %}
```liquid
{% include embed/youtube.html
    vid="dQw4w9WgXcQ"
%}
```
{: .nolineno }
{% endraw %}
</div>

<div>
{% include embed/youtube.html
    vid="dQw4w9WgXcQ"
%}
</div>

</div>

The video title is fetched automatically from YouTube and displayed in the caption bar. Click the preview to open the expanded viewer.

---

### Autoplay with Start and End Times

This example opens the expanded viewer and immediately plays a specific segment of the video.

<div class="example">

<div markdown="1">
{% raw %}
```liquid
{% include embed/youtube.html
    vid="dQw4w9WgXcQ"
    autoplay="true"
    start="42"
    end="1:15"
    caption="The famous chorus"
%}
```
{: .nolineno }
{% endraw %}
</div>

<div>
{% include embed/youtube.html
    vid="dQw4w9WgXcQ"
    autoplay="true"
    start="42"
    end="1:15"
    caption="The famous chorus"
%}
</div>

</div>

When the preview is clicked, the expanded viewer opens, seeks immediately to 0:42, plays until 1:15, then pauses. The custom caption overrides the YouTube title.

---

### Action Link Example

An action link is a standard Markdown link where the URL is formatted to trigger an action on a referenced viewer when clicked. To use an action link the viewer must include an `id` attribute.

<div class="example">

<div markdown="1">
{% raw %}
```liquid
{% include embed/youtube.html
    id="vid1"
    vid="dQw4w9WgXcQ"
%}
```
{: .nolineno }
{% endraw %}

Note the addition of the `id` attribute with the value `vid1`.

```markdown
[Watch the chorus](vid1/playat/42,75)
```
{: .nolineno }

</div>

<div>
{% include embed/youtube.html
    id="vid1"
    vid="dQw4w9WgXcQ"
%}
</div>

</div>

In this action link the first segment of the URL is the `id` of the viewer to target. The second segment (`playat`) is the action to perform. The third segment is the argument — a comma-separated start time and optional end time in seconds or `h:mm:ss` format.

Click this link to jump to the chorus: [Watch the chorus](vid1/playat/42,75)

The expanded viewer will open and begin playing from 0:42, stopping at 1:15.

---

### Action Link Example with Only a Start Time

If you only want to open the viewer at a specific point and let it play through, omit the end time.

<div class="example">

<div markdown="1">
{% raw %}
```liquid
{% include embed/youtube.html
    id="vid2"
    vid="dQw4w9WgXcQ"
%}
```
{: .nolineno }
{% endraw %}

```markdown
[Watch from here](vid2/playat/1:30)
```
{: .nolineno }

</div>

<div>
{% include embed/youtube.html
    id="vid2"
    vid="dQw4w9WgXcQ"
%}
</div>

</div>

Click this link to open the viewer at 1:30: [Watch from here](vid2/playat/1:30)

The expanded viewer opens and plays from 1:30 to the end of the video.

---

## Action Link Reference

Action links follow this URL format:

```
{viewer-id}/{action}/{args}
```

| Segment | Description |
|---|---|
| `viewer-id` | The `id` attribute of the target viewer |
| `action` | The action to perform (see table below) |
| `args` | Action-specific argument string |

### Supported Actions

| Action | Argument format | Description |
|---|---|---|
| `playat` | `start` or `start,end` | Opens the expanded viewer and plays from `start`, optionally stopping at `end`. Times may be in seconds or `h:mm:ss`. |

### Argument Format Examples

| Argument | Meaning |
|---|---|
| `90` | Start at 1:30, play to end |
| `1:30` | Start at 1:30, play to end |
| `90,150` | Start at 1:30, stop at 2:30 |
| `1:30,2:30` | Start at 1:30, stop at 2:30 |
| `1:02:30,1:05:00` | Start at 1h 2m 30s, stop at 1h 5m |