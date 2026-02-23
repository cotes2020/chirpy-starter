---
title: "Juncture: Image Viewer"
description: How to use the Juncture image viewer in your Markdown posts.
permalink: /admin/juncture-image-viewer
date: 2026-02-15
media_subpath: /assets/posts/juncture
# image: image.png
# show_header_image: false
order: 11
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

At first glance, the Juncture Image Viewer looks similar to the standard image support built into Jekyll and the Chirpy theme. It displays a clean, responsive image in the page, just like a normal Markdown image.

The difference becomes clear when the image is clicked.

When a reader clicks the page image, Juncture opens a larger viewer using the **highest-resolution version available**. This version supports smooth zooming and panning, allowing readers to explore fine detail. The image shown in the page itself is optimized for normal web viewing, so your page loads quickly and looks clean. The high-resolution version is only loaded when needed.

This makes the Juncture viewer ideal for:

- Maps  
- Archival photographs  
- Works of art  
- Scientific or historical illustrations  
- Any image where detail matters  

### First-Class Support for Wikimedia Commons

The Juncture viewer makes using Wikimedia Commons especially convenient.

You can reference a Commons image either by:

- Full Commons URL  
- The shorthand format: `wc:File_Name.jpg`

Juncture automatically:

- Retrieves the optimal image size for the page  
- Loads the highest-resolution version for exploration  
- Pulls caption and attribution information from the Commons API  
- Displays proper credit and licensing automatically  

This removes much of the friction normally involved in correctly using Commons images.

### Interactive Storytelling

Where Juncture goes beyond a traditional image viewer is in **interactivity**.

You can link text to viewer actions such as:

- `zoomto` — zoom to a specific region of the image  
- Display a label identifying the area of interest  

This allows your writing to guide the reader visually. Instead of saying “look in the upper right corner,” you can make the image respond directly when the reader clicks a link.

The result is a more immersive reading experience — one where the image becomes part of the narrative rather than just an illustration.

---

In short:

- Use the standard Chirpy image when you simply need to display a picture.
- Use the Juncture Image Viewer when the image is something readers should explore.

## Attributes

### Required Attributes

You must provide either a **src** or **manifest** attribute to the image tag.

---

#### src
{: .attribute }

The `src` attribute define the image to display.  You can use:

**A local image**

    src="/assets/posts/my-post/photo.jpg"

**A full web URL**

    src="https://example.org/image.jpg"

**A Wikimedia shortcut**

    src="wc:File_Name.jpg"

---

#### manifest
{: .attribute }

The for the image manifest attribute a full URL to an IIIF manifest must b provided.

    manifest="https://iiif.harvardartmuseums.org/manifests/object/299843"

---

### Optional Attributes

These improve presentation but are not required.

#### aspect
{: .attribute }

---

Controls the image shape.

    aspect="1200/630"
    aspect="1"

You usually don’t need to change this unless you want a taller or more square presentation.

---

#### caption
{: .attribute }

Text displayed below the image.

    caption="Monument Valley, UT"

Keep captions short and descriptive.

---

#### cover
{: .attribute }

Makes the image fill its space more dramatically, similar to a cover photo.

    cover="true"

This works well for wide landscape images.

---

#### region
{: .attribute }

Starts the viewer zoomed into a specific area.

    region="pct:10,20,30,40"

Most users won’t type this manually. You can use the viewer’s selection tool to generate region values.

---

#### rotate
{: .attribute }

Rotates the image.

    rotate="90"

---

#### seq
{: .attribute }

Selects image in a multi-image IIIF manifest.  By default, the first image in a manifest is displayed.  If multiple images are defined in a manifest others can be referenced using the `seq` attribute.  In this example the 2nd image in the manifest is displayed.

    seq="3"

---

## Examples

### The Simplest Example

This creates an image that when clicked will open a dialog with an image at full resolution with zoom and pan features enabled.

<div class="example">

<div markdown="1">
{% raw %}
```liquid
{% include embed/image.html
    src="wc:Monument_Valley,_Utah,_USA.jpg"
%}
```
{: .nolineno }
{% endraw %}

</div>

<div>
{% include embed/image.html
    src="wc:Monument_Valley,_Utah,_USA.jpg"
    cover="true"
%}
</div>

</div>

This uses a Wikimedia Commons image.  When using a Commons image the caption, attribution statement and license (if needed) are automatically added.

Click on the image to open the interactive pan and zoom viewer on a high-resolution version of the image.

---

### IIIF Example

In addition to displaying regular images, the image viewer can also display a IIIF image.  The IIIF image is referenced using a manifest URL.

<div class="example">
<div markdown="1">
{% raw %}
```liquid
{% include embed/image.html
    manifest="https://iiif.harvardartmuseums.org/manifests/object/299843"
%}
```
{: .nolineno }
{% endraw %}

</div>

<div>
{% include embed/image.html
    manifest="https://iiif.harvardartmuseums.org/manifests/object/299843"
%}
</div>
</div>


---

### Action Link Example

An action link is a standard Markdown link where the URL is formatted with information needed trigger an action on the referenced item when clicked.  To use an action link the image must include an `id` attribute so that it may be referenced in an action link.  In tbe example below that `zoomto` action is triggered on the image with the `img1` id.

<div class="example">
<div markdown="1">
{% raw %}
```liquid
{% include embed/image.html
    id="img1"
    src="wc:Monument_Valley,_Utah,_USA.jpg"
%}
```
{: .nolineno }
{% endraw %}

Note the addition of the `id` attribute with the value `img1`.

```markdown
[Merrick Butte](img1/zoomto/pct:67.68,34.23,23.22,27)
```
{: .nolineno }


</div>

<div>
{% include embed/image.html
    id="img1"
    src="wc:Monument_Valley,_Utah,_USA.jpg"
%}
</div>
</div>

in this action link the first segment of the URL contains the `id` of the image to target in the action.  The second segment (`zoomto`) is the action to perform.  The third segment is the action argument, in this case the image region to zoom into. 

Click this link to zoom in on [Merrick Butte](img1/zoomto/pct:67.68,34.23,23.22,27).

Note that the label for the zoomed region is taken from the action link text in this example.  The next example shows how to define a custom label.

### Action Link Example With Custom Label

When the action link is clicked, the image viewer will zoom into the area defined and display a label.  By default the text in the action link is used for the label.  While this is convenient you may use other text by appending an attribute block to the link with a *label* attribute defined.

<div class="example">
<div markdown="1">
{% raw %}
```liquid
{% include embed/image.html
    id="img2"
    src="wc:Monument_Valley,_Utah,_USA.jpg"
%}
```
{: .nolineno }
{% endraw %}

Note the addition of the `id` attribute with the value `img1`.

```markdown
[Merrick Butte](img2/zoomto/pct:67.68,34.23,23.22,27){: label="Custom Label"}
```
{: .nolineno }

</div>

<div>
{% include embed/image.html
    id="img2"
    src="wc:Monument_Valley,_Utah,_USA.jpg"
%}
</div>
</div>

In this action link the first segment of the URL contains the `id` of the image to target in the action.  The second segment (`zoomto`) is the action to perform.  The third segment is action argument, in this case the image region to zoom into.  Click the link below to trigger the action.

[zoomto action link with](img2/zoomto/pct:67.68,34.23,23.22,27){: label="Custom Label"}

Note that in this example the label for the zoomed region is taken from the custom attributes appended to the link.

---