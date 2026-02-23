---
title: "Juncture: Map Viewer"
description: How to use the Juncture map viewer in your Markdown posts.
permalink: /admin/juncture-map-viewer
date: 2026-02-15
media_subpath: /assets/posts/juncture
# image: map.png
# show_header_image: false
order: 12
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

Juncture lets you add **interactive maps** to your Markdown posts using a simple include. You do not need to write HTML, CSS, or JavaScript.

---

# The Simplest Example

This creates a map centered on Monument Valley in Utah.

<div class="example">

<div markdown="1">
{% raw %}
```liquid
{% include embed/map.html
    center="37.01056, -110.2425"
%}
```
{: .nolineno }
{% endraw %}

This example creates a map centered on the coordinates 37.01056, -110.2425, which correspond to the location of Monument Valley in Utah.  The map is displayed at the default zoom level. 

</div>

<div>
{% include embed/map.html
    center="37.01056, -110.2425"
%}
</div>

</div>

---

# Example with a Custom Caption and Location Marker

In this example a custom caption is defined

<div class="example">

<div markdown="1">
{% raw %}
```liquid
{% include embed/map.html
    center="37.01056, -110.2425"
    caption="Monument Valley, UT USA"
    markers="37.01056, -110.2425~Monument Valley"
%}
```
{: .nolineno }
{% endraw %}

In this example a caption and map marker are displayed. 

</div>

<div>
{% include embed/map.html
    center="37.01056, -110.2425"
    caption="Monument Valley, UT USA"
    markers="37.01056,-110.2425~Monument Valley"
%}
</div>

</div>

---

# Component Attribute

## Required Attributes

You must provide a **center** attribute to the map tag.  This defines the map location.  The **zoom** attribute is typically provided to control the level of detail displayed on the map when initially displayed.  This can be changed by viewer.  If not specified in an attribute, the initial zoom level is `8`.

### center
{: .attribute }

The for the map center attribute.

You can use:

**Geo Coordinates**

    center="37.01056, -110.2425"

**A Wikidata ID**

    center="Q852197"

For example, 

<div class="example">
<div markdown="1">
{% raw %}
```liquid
{% include embed/map.html
    center="32.783333, -79.931944"
%}
```
{: .nolineno }
{% endraw %}

</div>

<div>
{% include embed/map.html
    center="32.783333, -79.931944"
%}
</div>
</div>

---

# Optional Attributes

These improve presentation but are not required.

---

## allmaps
{: .attribute }

Defines an Allmaps ID referencing an IIIF image to use as a map layer.  This is often used to create a historical map overlay.

## basemap
{: .attribute }

Defines a basemap to add to the map.

## caption
{: .attribute }

Defines a caption to add to the map viewer.

## geojson
{: .attribute }

Defines a URL to a GeoJSON file to apply as a map layer.

## markers
{: .attribute }

Defines markers to add to the map.  Multiple markers are delimited with the pipe ('|') character.  A marker can be defined using a Wikidata ID or lat/lon position coordinates.  When using coordinates a label and image can also be provided using a tilde ('~') delimited values for the marker.

## zoom
{: .attribute }

Defines initial zoom level.  This is a number between 1 and 20, where the higher number reveals more detail.

    zoom="10"

---
