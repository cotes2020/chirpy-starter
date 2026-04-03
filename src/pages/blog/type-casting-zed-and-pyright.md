---
layout: ../../layouts/BlogPostLayout.astro
title: How the Death of Pytype Pushed Me to Switch to Zed
date: 2026-01-15 10:30:00 +0900
categories: [Programming, Python]
tags: [type-checking, ide, python]
---

Since Google announced the slow but expected demise of [pytype](https://github.com/google/pytype/commit/762b86d07d336613b4dfcc9f15ce9c4b730dbc02), I've been thinking about what well-supported type checker my team and I should consider adopting longer term. For now, to keep momentum, we'll stick with Pyright in the near term, but I wanted to spend some time testing alternatives.

Silly me: I expected trying different type checkers to be relatively straightforward. Unbeknownst to me at the time, VS Code would end up giving me tons of grief just trying to change the default type checker in a way that didn't require fiddling with multiple JSON files. After an hour or two (even with AI help), I threw in the towel and decided to take a different approach. If I couldn't easily set up VS Code with my existing repos, I figured it was time to consider other options for running Python code and developing new processes.

![VSCode configuration files to me while testing:](/assets/img/memes/xibit_config.webp)

After some basic searching of blog posts, reviews, and a few AI queries, I eventually settled on giving Zed a try, which recently within the last half year released a Windows version (and is available on multiple platforms). I was pleasantly surprised: not only was the editor fast, it worked basically out of the box with none of the usual Python venv tinkering I've come to expect when setting up VS Code on a new PC.

That let me focus on testing type checkers in Python, including [pyright](https://nilch.org/results?q=pyright), [mypy](https://github.com/python/mypy), and Zed's default, [basedpyright](https://github.com/DetachHead/basedpyright). Of the three, I was quite happy with basedpyright, both its approach and how well it fit into Zed's focused minimalism. This led me to switching Zed to my main Python editor.

I haven't fully abandoned VS Code, though. There are still aspects I appreciate, especially Jupyter notebook support and the huge ecosystem of extensions.
