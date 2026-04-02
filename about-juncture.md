---
layout: page
banner: /assets/img/PH-Banner_WithText.jpg
title: Juncture
permalink: /about-juncture
description: The evolution of Juncture, the framework behind the Plant Humanities Lab.
---

## The Evolution of Juncture

[Juncture](https://labs.jstor.org/projects/juncture/) started with a straightforward but ambitious idea: give scholars, students, and researchers the tools to tell rich, visually engaging stories on the web without needing to know how to write code. From the beginning, the goal was to make sophisticated digital storytelling feel accessible rather than intimidating.

### How It Began

Juncture grew out of a collaboration between JSTOR Labs and Dumbarton Oaks as part of the Plant Humanities Initiative. The project was designed to help researchers build complex narratives about plants and their cultural histories using modern web technologies, and to do it in a way that didn't require a software engineering background.

The core idea was elegant in its simplicity. Authors write their essays in Markdown and publish them on GitHub, and Juncture handles all the interactive complexity behind the scenes. Even in its earliest form, that meant support for zoomable high-resolution images using the IIIF framework, interactive maps, historical timelines, and network visualizations, all without authors needing to write a single line of custom code. Two projects in particular showed what was possible: the Plant Humanities Lab, the flagship platform for plant-focused visual essays, and Kent Maps Online, which used Juncture to publish interactive historical narratives tied to place.

### Growing Pains and Hard-Won Lessons

As Juncture moved from experiment to real-world platform, some architectural cracks began to show. The original system depended on a collection of custom backend services, including hosted image servers, specialized runtime scripts, and bespoke infrastructure, that worked well but created real sustainability headaches. The more an institution or individual relied on those services, the harder it became to maintain their own Juncture site independently over time. Power and complexity had come bundled together in ways that weren't ideal for the long run.

### A Simpler, More Sustainable Architecture

Those lessons shaped a significant rethinking of how Juncture works under the hood. The current generation is built around Jekyll, a widely used static site generator that powers GitHub Pages. The result is a much leaner system: the entire site is generated as static HTML, interactive features are implemented as lightweight web components and JavaScript modules, and Markdown remains the primary authoring format. Custom Jekyll extensions make it easy to embed interactive elements without ever leaving the writing environment.

This shift didn't mean giving anything up. Authors can still enrich their narratives with zoomable images, interactive maps, image comparison sliders, media viewers, and a range of other visual tools. What changed is that all of this now runs on open standards and widely adopted platforms, making sites genuinely easier to deploy, maintain, and extend over time.

### Where Juncture Stands Today

The architecture looks quite different than it did in the early days, but the core purpose hasn't changed. Juncture still exists to put sophisticated digital storytelling tools in the hands of people who have important things to say, whether researchers, educators, or students, without asking them to become software developers first.

That purpose now finds its fullest expression in [StoryKit](https://github.com/rsnyder/storykit-starter), the current manifestation of the Juncture ideal. StoryKit carries the same vision forward but represents a fundamental enough change in implementation that a new name felt warranted. Where earlier versions of Juncture leaned on custom backend services and specialized infrastructure, StoryKit relies on none of that. It depends on no external services, favors standard and widely adopted packages throughout, and is built to be robust, extensible, and sustainable in ways that earlier architectures couldn't quite achieve. The goal, making rich visual storytelling genuinely accessible to anyone with something worth saying, remains exactly what it always was.