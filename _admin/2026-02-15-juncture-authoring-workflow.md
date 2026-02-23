---
title: "Juncture: Authoring Workflow"
description: A step-by-step guide for writing and previewing Chirpy blog posts using GitHub's web editor and the live preview tool, covering one-time setup and the ongoing edit-commit-preview workflow.
permalink: /admin/juncture-authoring-workflow
date: 2026-02-15
order: 20
---

# Authoring Blog Posts with Live Preview

## Overview

## Overview

Writing and previewing blog posts through GitHub normally involves a frustrating wait: every time you commit a change, GitHub Pages must rebuild your entire site before you can see the result — a process that can take anywhere from one to five minutes depending on how many posts you have. This guide walks you through a faster workflow using GitHub's built-in web editor alongside a live preview tool that renders your post instantly in a second browser window, with full Chirpy and Juncture styling, eliminating that wait almost entirely. With a GitHub token added, the preview loads in seconds and you can iterate as quickly as you can type and commit.

## Part 1 — One-Time Setup

Do this once. After setup, you'll go straight to Part 3 for every post you write.

### Step 1 — Add the Preview Bookmarklet to Your Browser

1. Go to your site's **Preview Bookmarklet** page at:
   [{{ site.url }}{{ site.baseurl }}/admin/preview-bookmarklet]({{ site.url }}{{ site.baseurl }}/admin/preview-bookmarklet)
2. Make sure your browser's **bookmarks bar is visible**
   - Chrome / Edge: press **Ctrl+Shift+B** (Windows) or **⌘+Shift+B** (Mac)
   - Firefox: press **Ctrl+Shift+B** / **⌘+Shift+B**
3. Drag the **"Preview on GitHub"** button from the page up into your bookmarks bar
4. You should see it appear there as a new bookmark

> ✅ You only need to do this once, even across browser restarts.

---

### Step 2 — Add a GitHub Token (PAT)

Without a token, GitHub limits you to a handful of preview loads per hour. Adding a token raises this to 5,000 — effectively unlimited for normal use.

**Create the token:**

1. Go to [github.com/settings/tokens/new](https://github.com/settings/tokens/new) *(sign in if prompted)*
2. In the **Note** field type: `Jekyll Preview`
3. Under **Expiration** choose `No expiration`
4. Scroll down — **do not check any boxes**
5. Click **Generate token**
6. **Copy the token** that appears — it starts with `ghp_`

> ⚠️ You won't be able to see this token again after you leave the page. Copy it now.

**Save the token in the preview tool:**

1. Open your preview page at [{{ site.url }}{{ site.baseurl }}/preview]({{ site.url }}{{ site.baseurl }}/preview)
2. Click the **⚙ Config** button in the top bar
3. Enter `1` and press OK
4. Paste your token and press OK

> ✅ The token is saved in your browser. You won't need to enter it again unless you clear your browser data or switch to a different browser.

---

## Part 2 — Set Up Your Side-by-Side Workspace

Do this at the start of each writing session.

### Step 1 — Open Your Post in GitHub's Editor

1. Go to your repository on GitHub
2. Navigate to the `_posts` folder
3. Click your post file (e.g. `2026-01-10-my-post.md`)
4. Click the **pencil icon** (✏️) in the top right to open the editor

### Step 2 — Open the Preview Window

1. While on the GitHub editor page, click the **"Preview on GitHub"** bookmarklet in your bookmarks bar
2. A new tab opens showing the rendered preview of your post
3. Arrange your two windows side by side:
   - **Left window:** GitHub editor tab
   - **Right window:** Preview tab

> 💡 On Mac, you can use Mission Control or drag windows to opposite sides of the screen. On Windows, drag a window to the left or right edge to snap it to half the screen.

---

## Part 3 — The Edit → Commit → Preview Cycle

Repeat these steps as you write your post.

### Step 1 — Make Your Edits

In the **left window** (GitHub editor), write or update your content.

### Step 2 — Commit Your Changes

When you're ready to preview, scroll down below the editor to the **Commit changes** section:

1. Leave the commit message as-is, or type a short note like `draft update`
2. Make sure **"Commit directly to the `main` branch"** is selected
3. Click **Commit changes**

### Step 3 — Refresh the Preview

In the **right window** (preview tab):

1. Click the **⟳ Reload** button in the top bar

> 💡 You may need to wait 5–10 seconds after committing before clicking Reload. GitHub's servers need a moment to register the new file content.

The preview will reload and show your latest changes with full Chirpy styling.

---

## Tips and Troubleshooting

**The preview looks outdated even after reloading**
Wait a few seconds and reload again. GitHub caches file content for a short time after a commit. If it's still stale after 30 seconds, try reloading a second time.

**The preview bar shows "WARN: API rate limited"**
You've hit the 60 requests/hour limit. Check that your PAT was saved correctly: click **⚙ Config → 1** and re-enter your token. If you don't have a token yet, follow the steps in Part 1, Step 2.

**Images aren't showing**
Check that your post's front matter includes the correct `media_subpath`. For example:
```yaml
media_subpath: /assets/posts/my-post
```
And that your image files have been uploaded to that folder in your repository.

**A Juncture embed shows as a yellow placeholder box**
The include file (e.g. `_includes/embed/image.html`) may not be in your repository. Check that your repo has the Juncture include files in the `_includes/embed/` folder.

**The bookmarklet doesn't work on a page**
The bookmarklet only works when you're viewing a `.md` file on GitHub — specifically on a URL that looks like `github.com/owner/repo/blob/branch/path/file.md`. It won't work on folder listings, issue pages, or other GitHub pages.

**You switch computers or browsers**
You'll need to re-add the bookmarklet (drag it from the Preview Bookmarklet page again) and re-enter your PAT (⚙ Config → 1) on the new browser.
