---
title: "Juncture: One-Time Setup for Authors"
description: A guide for configuring the Juncture Preview Tool.  The tool uses a bookmarklet and GitHub token, enabling one-click live preview of any post directly from GitHub's file browser.
permalink: /admin/juncture-preview-setup
date: 2026-02-15
toc: true
order: 11
---

<style>
  .bookmarklet-wrap {
    max-width: 640px;
    margin: 2rem auto;
    font-family: inherit;
  }
  .bookmarklet-intro {
    margin-bottom: 2rem;
    line-height: 1.7;
  }
  .drag-zone {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1.5rem;
    padding: 2.5rem;
    border: 2px dashed var(--border-color, #444);
    border-radius: 12px;
    background: var(--card-bg, rgba(255,255,255,0.03));
    margin-bottom: 2rem;
  }
  .drag-zone p {
    margin: 0;
    opacity: 0.65;
    font-size: 0.9rem;
    text-align: center;
  }
  #bookmarklet-link {
    display: inline-flex;
    align-items: center;
    gap: 0.6em;
    padding: 0.75em 1.4em;
    background: var(--link-color, #4a9eff);
    color: #fff !important;
    border-radius: 8px;
    font-weight: 700;
    font-size: 1rem;
    text-decoration: none !important;
    cursor: grab;
    box-shadow: 0 4px 16px rgba(0,0,0,0.25);
    transition: transform 0.15s, box-shadow 0.15s;
    user-select: none;
  }
  #bookmarklet-link:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.35);
  }
  #bookmarklet-link:active { cursor: grabbing; }
  .bookmarklet-link-icon { font-size: 1.2em; }
  .steps {
    list-style: none;
    padding: 0;
    margin: 0;
    counter-reset: steps;
  }
  .steps li {
    counter-increment: steps;
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    margin-bottom: 1rem;
    line-height: 1.6;
  }
  .steps li::before {
    content: counter(steps);
    flex-shrink: 0;
    width: 1.8em;
    height: 1.8em;
    border-radius: 50%;
    background: var(--link-color, #4a9eff);
    color: #fff;
    font-weight: 700;
    font-size: 0.85rem;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 0.1em;
  }
  .tip {
    padding: 1rem 1.25rem;
    border-left: 3px solid var(--link-color, #4a9eff);
    background: var(--card-bg, rgba(255,255,255,0.03));
    border-radius: 0 8px 8px 0;
    font-size: 0.9rem;
    line-height: 1.6;
    margin-top: 1.5rem;
  }
  .tip code {
    font-size: 0.85em;
  }
</style>

## Step 1 — Add Bookmarklet to Browser

<div class="bookmarklet-wrap">

  <div class="bookmarklet-intro">
    <p>This bookmarklet lets you preview any markdown post from this site's GitHub repository — 
    rendered with full Chirpy layout — without waiting for a GitHub Pages build.</p>
  </div>

  <div class="drag-zone">
    <a id="bookmarklet-link" href="#" title="Drag me to your bookmarks bar">
      <span class="bookmarklet-link-icon">🔖</span>
      Preview on GitHub
    </a>
    <p>Drag the button above to your bookmarks bar</p>
  </div>

  <ol class="steps">
    <li>Make sure your <strong>bookmarks bar is visible</strong> 
        (Chrome: <kbd>⌘⇧B</kbd> / <kbd>Ctrl+Shift+B</kbd>)</li>
    <li>Drag the <strong>"Preview on GitHub"</strong> button above into your bookmarks bar</li>
    <li>Navigate to any <code>.md</code> file in your repo on GitHub 
        (e.g. <code>github.com/{{ site.github_username }}/{{ site.repository | split: "/" | last }}/blob/main/_posts/...md</code>)</li>
    <li>Click the bookmarklet — the preview opens in a new tab</li>
  </ol>

  <div class="tip">
    💡 The bookmarklet only works on GitHub <code>blob</code> URLs for <code>.md</code> files 
    in this repository. It will show an alert if clicked on any other page.
  </div>

</div>

## Step 2 — Add a GitHub Token (PAT)

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
---


<script>
(function() {
  const previewUrl = '{{ site.url }}{{ site.baseurl }}/preview';

  const code = `(function(){
  var m=location.href.match(/github\\.com\\/([^/]+)\\/([^/]+)\\/blob\\/([^/]+)\\/(.+\\.md)/);
  if(!m)return alert('Navigate to a .md file in GitHub first');
  var p=JSON.stringify({o:m[1],r:m[2],ref:m[3],p:m[4]});
  window.open('${previewUrl}#'+encodeURIComponent(p),'_blank');
})();`;

  const link = document.getElementById('bookmarklet-link');
  link.href = 'javascript:' + code;

  link.addEventListener('click', function(e) {
    e.preventDefault();
    alert('Drag this button to your bookmarks bar instead of clicking it.');
  });
})();
</script>