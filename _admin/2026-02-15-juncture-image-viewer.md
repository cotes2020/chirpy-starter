---
title: Adding Zoomable Images with Juncture
description: How to use the Juncture image viewer in your Markdown posts.
permalink: /docs/juncture-image-viewer
date: 2026-02-15
order: 4
juncture:
    mode: 2col
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

Juncture lets you add **zoomable, interactive images** to your Markdown posts using a simple include. You do not need to write HTML, CSS, or JavaScript.

---

# The Simplest Example

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

Click on the image to open the dialog.

</div>

<div>
{% include embed/image.html
    src="wc:Monument_Valley,_Utah,_USA.jpg"
    cover="true"
%}
</div>

</div>

---

# Example with a Custom Caption

In this example a custom caption is defined

<div class="example">

<div markdown="1">
{% raw %}
```liquid
{% include embed/image.html
    src="wc:Monument_Valley,_Utah,_USA.jpg"
    caption="A Custom Caption"
%}
```
{: .nolineno }
{% endraw %}

</div>

<div>
{% include embed/image.html
    src="wc:Monument_Valley,_Utah,_USA.jpg"
    caption="A Custom Caption"
%}
</div>

Note that when using Wikimedia Commons images, a generated attribution statement is applied to custom captions when needed.

</div>

---

# IIIF Examples

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


By default, the first image in a manifest is displayed.  If multiple images are defined in a manifest others can be referenced using the `seq` attribute.  In this example the 2nd image in the manifest is displayed.

<div class="example">
<div markdown="1">
{% raw %}
```liquid
{% include embed/image.html
    manifest="https://iiif.harvardartmuseums.org/manifests/object/299843"
    seq="2"
%}
```
{: .nolineno }
{% endraw %}

</div>

<div>
{% include embed/image.html
    manifest="https://iiif.harvardartmuseums.org/manifests/object/299843"
    seq="2"
%}
</div>
</div>

---

# Action Link Example

When an image includes an `id` attribute it may be referenced in an action link.  An action link is a standard Markdown link where the URL is formatted with information needed trigger an action on the referenced item when clicked.  In tbe example below that `zoomto` action is triggered on the image with the `image` id.

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
[zoomto example](img1/zoomto/pct:45.45,39.44,13.25,18.56)
```
{: .nolineno }

in this action link the first segment of the URL contains the `id` of the image to target in the action.  The second segment (`zoomto`) is the action to perform.  The third segment is action argument, in this case the image region to zoom into.  Click the link below to trigger the action.


[zoomto example](img1/zoomto/pct:45.45,39.44,13.25,18.56)

Note that in this example the label for the zoomed region is taken from the link text.

</div>

<div>
{% include embed/image.html
    id="img1"
    src="wc:Monument_Valley,_Utah,_USA.jpg"
%}
</div>
</div>

# Action Link Example With Custom Label

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
[zoomto example](img2/zoomto/pct:45.45,39.44,13.25,18.56){: label="Custom Label"}
```
{: .nolineno }

in this action link the first segment of the URL contains the `id` of the image to target in the action.  The second segment (`zoomto`) is the action to perform.  The third segment is action argument, in this case the image region to zoom into.  Click the link below to trigger the action.

[zoomto example](img2/zoomto/pct:45.45,39.44,13.25,18.56){: label="Custom Label"}

Note that in this example the label for the zoomed region is taken from the custom attributes appended to the link.

</div>

<div>
{% include embed/image.html
    id="img2"
    src="wc:Monument_Valley,_Utah,_USA.jpg"
%}
</div>
</div>

---

# Required Attribute

You must provide either a **src** or **manifest** attribute to the image tag.

## src
{: .attribute }

The for the image src attribute.

You can use:

**A local image**

    src="/assets/posts/my-post/photo.jpg"

**A full web URL**

    src="https://example.org/image.jpg"

**A Wikimedia shortcut**

    src="wc:File_Name.jpg"

## manifest
{: .attribute }

The for the image manifest attribute a full URL to an IIIF manifest must b provided.

For example, 

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

# Optional Attributes

These improve presentation but are not required.

---

## caption
{: .attribute }

Text displayed below the image.

    caption="Monument Valley, UT"

Keep captions short and descriptive.

---

## `cover="true"`
{: .attribute }

Makes the image fill its space more dramatically, similar to a cover photo.

    cover="true"

This works well for wide landscape images.

---

## `aspect`

Controls the image shape.

    aspect="1200/630"

You usually don’t need to change this unless you want a taller or more square presentation.

---

## `region`

Starts the viewer zoomed into a specific area.

    region="pct:10,20,30,40"

Most users won’t type this manually. You can use the viewer’s selection tool to generate region values.

---

## `rotate`

Rotates the image.

    rotate="90"

---

# Linking to a Specific Part of an Image

To create interactive zoom links, your image must have an `id`.

Example image:

    {% include embed/image.html
      id="valley"
      src="/assets/posts/monument-valley/Monument_Valley.jpg"
      caption="Monument Valley"
    %}

Then in your text:

    Notice the dramatic formations like 
    [West Mitten Butte](image/zoomto/pct:10,20,30,40).

When a reader clicks that link:

- The image zooms to that region  
- The selected area is highlighted  

This allows you to guide the reader’s attention while telling a visual story.

---

# Complete Example

    {% include embed/image.html
      id="valley"
      src="/assets/posts/monument-valley/Monument_Valley.jpg"
      caption="Monument Valley"
      cover="true"
    %}

If you are not using zoom links, you can remove the `id` entirely.

---

# Tips for Visual Essays

- Use zoomable images when detail matters.
- Place images near the text that discusses them.
- Add an `id` only when you plan to use interactive links.
- Use zoom links sparingly to guide attention.
- Keep captions concise.

---

# When to Use This Viewer

Use the Juncture image viewer when:

- The image contains fine detail  
- You want readers to explore  
- You want to direct attention to specific areas  
- You’re creating an interactive visual essay  

For simple decorative images, a standard Markdown image may be sufficient.
