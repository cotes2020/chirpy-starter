---
title: "Juncture: Image Compare Viewer"
description: How to use the Juncture Image Compare viewer in your Markdown posts.
permalink: /admin/juncture-image-compare-viewer
date: 2026-02-22
media_subpath: /assets/posts/image-compare
toc: true
order: 23
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

The Juncture Image Compare Viewer places two images side by side in an interactive slider that lets readers reveal one image beneath the other by dragging a divider. It is designed for comparing before/after photographs, historical images against modern views, or any pair of images that share the same subject.

When a reader clicks the viewer, Juncture opens a **larger, expanded viewer** using the full available screen width. This gives a much better experience for detailed comparison without forcing a large element into the article layout itself.

### Preview Mode and Expanded Mode

The viewer operates in two modes:

**Preview mode** (default) renders a compact, interactive slider in the page. The drag handle is visible but clicking anywhere on the viewer opens the expanded version. This keeps the article layout clean while still making the comparison immediately visible.

**Expanded mode** opens automatically when the reader clicks the preview. The viewer loads in a large dialog at full width, where the drag handle is fully interactive and the alignment adjustment tool becomes available.

### Alignment Adjustment

Where the Image Compare viewer goes beyond a simple image slider is in its built-in **alignment tool**.

Real-world before/after photographs are rarely taken from exactly the same position or at exactly the same scale. The alignment tool lets you correct for these differences by independently offsetting and scaling each image until the subjects line up precisely. Your corrections are encoded directly in the tag so the alignment is preserved for every reader.

---

In short:

- Use a standard `<img>` pair when you simply need two images displayed together.
- Use the Juncture Image Compare viewer when you want an interactive slider, a clean layout, or precise alignment between the two images.

---

## Attributes

### Required Attributes

You must provide both a **before** and an **after** attribute.

---

#### before
{: .attribute }

The filename of the bottom image — the one revealed as the divider is dragged left. For relative paths only the filename is required; absolute URLs are also accepted.

    before="Canterbury_1920.jpg"
    before="https://example.com/images/Canterbury_1920.jpg"

Alignment corrections for the before image are appended directly to this value as query parameters. You do not need to add them by hand — the adjustment tool generates the correct value for you.

---

#### after
{: .attribute }

The filename of the top image — the one visible when the divider is fully to the right. Accepts the same formats as `before`.

    after="Canterbury_today.jpg"
    after="https://example.com/images/Canterbury_today.jpg"

As with `before`, alignment corrections are appended to this value automatically by the adjustment tool.

---

### Optional Attributes

---

#### caption
{: .attribute }

Text displayed below the viewer. If omitted, no caption is shown.

    caption="Canterbury High Street — 1920 vs today"

---

#### aspect
{: .attribute }

The width-to-height ratio used to size the expanded dialog. Expressed as a decimal.

    aspect="1.5"

A value of `1.5` produces a dialog that is one and a half times wider than it is tall, which suits most landscape photographs. A value of `0.75` suits portrait images. If omitted, the dialog uses its own default sizing.

---

#### position
{: .attribute }

The initial position of the divider, expressed as a percentage of the viewer width from the left edge. Defaults to `50`.

    position="40"

Use a value other than `50` when one image is more recognisable and you want it to dominate the initial view.

---

## Alignment Query Parameters

These parameters are appended to the `before` or `after` attribute values by the adjustment tool. You will not normally write them by hand, but they are documented here for completeness.

| Parameter | Applies to | Default | Description |
|---|---|---|---|
| `bx` | before | `0` | Horizontal offset of the before image, in percent |
| `by` | before | `0` | Vertical offset of the before image, in percent |
| `bs` | before | `1` | Scale (zoom) of the before image |
| `ax` | after | `0` | Horizontal offset of the after image, in percent |
| `ay` | after | `0` | Vertical offset of the after image, in percent |
| `as` | after | `1` | Scale (zoom) of the after image |

A `before` value with alignment corrections looks like this:

    before="Canterbury_1920.jpg&bx=-4&by=-2&bs=1.17"

Positive offset values shift the image right (X) or down (Y). Negative values shift it left or up. Scale values greater than `1` zoom in; values less than `1` zoom out.

---

## Examples

### The Simplest Example

<div class="example">

<div markdown="1">
{% raw %}
```liquid
{% include embed/image-compare.html
    before="Westgate_Towers_c1905.jpg&bx=-8&by=-6&bs=1.31"
    after="Westgate_Towers_2021.jpg&ax=-4&ay=-2&as=1.17"
    caption="Westgate Towers — c.1905 vs 2021"
    aspect="1.5"
    position="50"
%}
```
{: .nolineno }
{% endraw %}
</div>

<div>
{% include embed/image-compare.html
    before="Westgate_Towers_c1905.jpg&bx=-8&by=-6&bs=1.31"
    after="Westgate_Towers_2021.jpg&ax=-4&ay=-2&as=1.17"
    caption="Westgate Towers — c.1905 vs 2021"
    aspect="1.5"
    position="50"
%}
</div>

</div>

The divider starts at the centre. Click the viewer to open the expanded version. Drag the divider left or right to reveal each image.

---

### Custom Caption and Initial Position

<div class="example">

<div markdown="1">
{% raw %}
```liquid
{% include embed/image-compare.html
    before="Westgate_Towers_c1905.jpg"
    after="Westgate_Towers_2021.jpg"
    caption="Westgate Towers — c.1905 vs 2021"
    aspect="1.5"
    position="35"
%}
```
{: .nolineno }
{% endraw %}
</div>

<div>
{% include embed/image-compare.html
    before="Westgate_Towers_c1905.jpg"
    after="Westgate_Towers_2021.jpg"
    caption="Westgate Towers — c.1905 vs 2021"
    aspect="1.5"
    position="35"
%}
</div>

</div>

Setting `position="35"` opens the viewer with the divider shifted left so the modern image dominates the initial view. The caption provides context visible without opening the expanded viewer.

---

### With Alignment Corrections

When images were photographed at different distances or angles, the alignment tool generates corrected values like these:

<div class="example">

<div markdown="1">
{% raw %}
```liquid
{% include embed/image-compare.html
    before="Westgate_Towers_c1905.jpg&bx=-8&by=-6&bs=1.31"
    after="Westgate_Towers_2021.jpg&ax=-4&ay=-2&as=1.17"
    caption="Westgate Towers — c.1905 vs 2021"
    aspect="1.5"
    position="50"
%}
```
{: .nolineno }
{% endraw %}
</div>

<div>
{% include embed/image-compare.html
    before="Westgate_Towers_c1905.jpg&bx=-8&by=-6&bs=1.31"
    after="Westgate_Towers_2021.jpg&ax=-4&ay=-2&as=1.17"
    caption="Westgate Towers — c.1905 vs 2021"
    aspect="1.5"
    position="50"
%}
</div>

</div>

The `after` image has been shifted left by 4%, up by 2%, and zoomed in by 17% to align the tower with its historical counterpart. These values were generated automatically by the adjustment tool described below.

---

## The Alignment Adjustment Tool

The adjustment tool is available in the expanded viewer. It lets you nudge and scale each image independently until the subjects line up, then copies a ready-to-use Liquid tag to your clipboard.

### Opening the Tool

1. Click the viewer in your article to open the expanded version.
2. **Double-click** anywhere on the image comparison. The alignment panel slides open below the viewer.
3. Double-click again, or click the **×** button in the panel header, to close it.

When the alignment panel is open, the top (after) image becomes slightly transparent so the bottom (before) image shows through. This ghosting effect makes misalignment immediately visible as a double-image, and disappears when the panel is closed.

### Using the Controls

The panel has two tabs — **Before** and **After** — one for each image. Each tab contains three sliders:

| Control | Range | Effect |
|---|---|---|
| X | −50% to +50% | Shifts the image left (negative) or right (positive) |
| Y | −50% to +50% | Shifts the image up (negative) or down (positive) |
| Zoom | 0.5× to 3× | Scales the image in or out from its centre |

Adjust the sliders on whichever image needs moving. In most cases only one image needs correction — use the After tab to align a newer photograph to a fixed historical reference.

**Tip:** Start with Zoom to match the scale of the two images, then use X and Y to bring the subjects into register.

### Copying the Tag

Once aligned, click **Copy tag** at the bottom right of the panel. The tag is copied to your clipboard in this format:

{% raw %}
```liquid
{% include embed/image-compare.html
    before="Westgate_Towers_c1905.jpg&bx=-8&by=-6&bs=1.31"
    after="Westgate_Towers_2021.jpg&ax=-4&ay=-2&as=1.17"
    caption="Westgate Towers — c.1905 vs 2021"
    aspect="1.5"
    position="50"
%}
```
{: .nolineno }
{% endraw %}

Alignment corrections that differ from the defaults are appended as query parameters on the relevant `before` or `after` value. Parameters at their default values are omitted to keep the tag clean.

Paste the tag directly into your Markdown. No further editing is required.

### Resetting

Click **Reset all** to return all six sliders to their defaults (zero offset, 1× scale on both images). This is useful if you want to start the alignment process over.