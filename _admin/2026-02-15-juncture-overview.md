---
title: "Juncture: Overview"
description: An introduction to Juncture — a Markdown-first framework for adding interactive viewers and text-driven media interactions to a Jekyll + Chirpy site. This overview explains Juncture’s origins, how it fits into the existing architecture, and how it is enabled and configured for individual posts.
permalink: /admin/juncture-overview
date: 2026-02-15
order: 10
juncture:
    mode: flat
    toolbar: false
---


## What Is Juncture?

**Juncture** is a Markdown-based authoring extension for Jekyll that enables the creation of interactive, media-rich essays without requiring users to write HTML, CSS, or JavaScript.

At its core, Juncture allows authors to:

* Add interactive viewers (images, maps, and more) using simple, Markdown-friendly tags
* Trigger actions in those viewers directly from links in the text
* Compose visual narratives that combine media and prose in a coordinated way

Juncture is designed for content authors. If you can write basic Markdown and are comfortable editing a web page in a text editor, you can use Juncture.

---

## Where Juncture Came From

Juncture evolved from a 2018 digital humanities collaboration between **JSTOR Labs** and **Dumbarton Oaks**. The original goal was straightforward:

> Enable students and scholars to create interactive visual narratives using Markdown — without requiring coding skills.

The initial framework allowed authors to:

* Write essays in Markdown
* Insert interactive image and map viewers
* Coordinate text and media through simple action links

After the completion of that project, the underlying ideas were generalized into a framework named **Juncture**.

Over time, the implementation went through several iterations. The current architecture reflects a shift away from a heavily customized codebase toward a cleaner, more maintainable structure built directly on **Jekyll**.

---

## Juncture + Jekyll + Chirpy

Juncture does not replace Jekyll or the Chirpy theme. It extends and complements them.

* **Jekyll** provides the static site engine.
* **Chirpy** provides the theme, layout, typography, navigation, and core documentation model (see “Getting Started”  and “Writing a New Post” ).
* **Juncture** adds interactive media components and text-driven interactions on top of that foundation.

The result is:

* A standard Jekyll site structure
* A robust, well-maintained theme (Chirpy)
* A lightweight layer of interactive enhancements

Earlier versions of Juncture relied on substantial custom JavaScript and infrastructure. The current Jekyll-based architecture removes much of that complexity while preserving the core concepts:

* Markdown-first authoring
* Media viewers embedded through simple tags
* Text-triggered interaction with those viewers

This makes the system more robust, easier to maintain, and more extensible over time.

---

## What Juncture Adds

When enabled for a post, Juncture provides:

### 1. Viewer Components

You can insert interactive components such as:

* Image viewers
* Map viewers
* Other iframe-based components

These are added using Liquid include tags that are designed to feel natural within a Markdown workflow. Authors do not need to understand the underlying HTML or JavaScript implementation.

### 2. Action Links

One of Juncture’s distinguishing features is **text-driven interaction**.

Within your narrative, you can include action links that:

* Zoom to a specific region of an image
* Move a map to a defined location
* Trigger other component behaviors

This allows prose and media to work together — the text becomes part of the interface.

---

## Configuration Model

Juncture functionality is controlled in two places:

### Global Configuration

Site-wide settings are defined in `_config.yml`. This determines:

* Which Juncture features are available
* How components behave by default

If Juncture is not configured in `_config.yml`, its functionality is effectively inactive.

### Per-Post Enablement

Juncture is **not enabled by default**.

To use Juncture features in a post, you must explicitly enable it in that post’s Front Matter:

```yaml
---
title: Example Post
juncture: true
---
```

Only posts that include the `juncture` field in their Front Matter will activate the additional scripts and behaviors.

This design keeps the base site lightweight and ensures that standard posts behave exactly like normal Chirpy posts unless Juncture is intentionally enabled.

---

## Design Philosophy

Juncture is guided by a few core principles:

* **Markdown first** — Authors work in familiar, simple syntax.
* **No required coding** — HTML, CSS, and JavaScript are abstracted away.
* **Text and media integration** — Prose can directly control visual elements.
* **Incremental enhancement** — A post still works as a normal page even if interactive features are minimal.

In short, Juncture turns a standard Jekyll + Chirpy site into a platform for interactive visual essays — without compromising maintainability or forcing authors into a technical workflow.

---

## Attribute Blocks and Entity Information

### Kramdown Attribute Blocks

Jekyll (and therefore Chirpy) uses **kramdown** as its Markdown processor. One of kramdown’s most useful features is the *attribute block*. An attribute block lets you attach additional properties — such as classes or IDs — to a Markdown element without writing raw HTML.

A simple example looks like this:

```markdown
This is a paragraph.
{: .highlight }
```

The second line attaches the CSS class `highlight` to the paragraph above it.

In standard Jekyll/Chirpy usage, attribute blocks are commonly used to:

* Apply layout or formatting classes
* Add custom styling
* Control alignment or width
* Add IDs for linking

Juncture builds on this existing capability rather than introducing something entirely new. In Juncture-enabled posts, attribute blocks are also used to:

* Assign IDs to viewer components
* Attach action behaviors to links
* Provide custom labels or parameters for interactive elements

In other words, attribute blocks are a general Markdown feature — but Juncture uses them as a structured way to connect text and media behavior without exposing authors to JavaScript.

---

### Entity Information Popups (Wikidata)

Another key Juncture feature is the ability to create **Entity Information Boxes** by linking text to a Wikidata entity ID.

When an author links a term to a Wikidata identifier (for example, a person, place, or concept), Juncture can automatically generate a small information popup. This popup typically includes:

* A short description
* An image (when available)
* Basic structured facts

This allows authors to enrich their essays with contextual information without manually writing sidebars or summaries.

---

### What Is Wikidata?

For many users, Wikidata will be unfamiliar.

**Wikidata** is a free, collaboratively edited knowledge base maintained by the Wikimedia Foundation (the same organization behind Wikipedia). Instead of storing narrative articles, Wikidata stores *structured data* about entities:

* People
* Places
* Organizations
* Works of art
* Scientific concepts
* Historical events
* And more

Each entity in Wikidata has a unique identifier, such as:

```
Q42
```

These identifiers represent structured records containing names, descriptions, images, dates, relationships, and other properties.

Because Wikidata is structured and machine-readable, it can be used programmatically. Juncture leverages this structure to dynamically generate entity information popups directly within your content.

---

### Why This Matters

Together, attribute blocks and Wikidata-powered entity popups illustrate an important design principle of Juncture:

* Authors write simple Markdown.
* Structured enhancements are layered on top.
* Interactive and contextual features are added without requiring custom HTML or scripting.

The result is content that remains readable and maintainable, while still supporting rich interaction and contextual depth.
