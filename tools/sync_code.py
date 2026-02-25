#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import os
import sys
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional


# ----------------------------
# Config: source repo + branch
# ----------------------------
SRC_USER = "rsnyder"
SRC_REPO = "chirpy-juncture-starter"
SRC_BRANCH = "main"

# Optional: GitHub token (env var) to avoid rate limits / access private repos
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

# ----------------------------
# Files to sync (relative paths)
# ----------------------------
FILES_TO_SYNC = [
    "_admin/index.md",
    "_admin/2019-08-08-text-and-typography.md",
    "_admin/2019-08-08-write-a-new-post.md",
    "_admin/2019-08-09-getting-started.md",
    "_admin/2019-08-11-customize-the-favicon.md",
    "_admin/2026-02-15-juncture-overview.md",
    "_admin/2026-02-15-juncture-image-viewer.md",
    "_admin/2026-02-15-juncture-image-compare-viewer.md",
    "_admin/2026-02-15-juncture-map-viewer.md",
    "_admin/2026-02-15-juncture-youtube-viewer.md",
    "_admin/2026-02-15-juncture-authors-guide.md",
    "_admin/2026-02-15-juncture-preview-setup.md",
    "_admin/2026-02-15-juncture-entity-info-popups.md",
    "_includes/embed/iframe.html",
    "_includes/embed/image-compare.html",
    "_includes/embed/image.html",
    "_includes/embed/map.html",
    "_includes/embed/vis-network.html",
    "_includes/embed/youtube.html",
    "_includes/cite-this.html",
    "_includes/col2-toggle.html",
    "_includes/featured_posts.html",
    "_includes/pdf-download.html",
    "_includes/post_index_item.html",
    "_includes/refactor-content.html",
    "_includes/media-url.html",
    "_includes/sidebar.html",
    "_layouts/admin.html",
    "_layouts/juncture-home.html",
    "_layouts/post.html",
    "_plugins/md5_filter.rb",
    "_posts/.template.md",
    "assets/components/image-compare.html",
    "assets/components/image.html",
    "assets/components/map.html",
    "assets/components/vis-network.html",
    "assets/components/youtube.html",
    "assets/css/juncture.css",
    "assets/js/juncture.js",
    "assets/img/devices-mockup.png",
    "assets/img/devtools-dark.png",
    "assets/img/devtools-light.png",
    "assets/img/mockup.png",
    "assets/img/pages-source-dark.png",
    "assets/img/pages-source-light.png",
    "assets/posts/juncture/image.png",
    "assets/posts/juncture/map.png",
    "assets/posts/image-compare/Westgate_Towers_c1905.jpg",
    "assets/posts/image-compare/Westgate_Towers_2021.jpg",
    "preview/index.html",
    "tools/sync_code.py",
]


@dataclass
class Result:
    changed: List[str]
    unchanged: List[str]
    failed: List[str]


def sha256_bytes(data: bytes) -> str:
    h = hashlib.sha256()
    h.update(data)
    return h.hexdigest()


def raw_url(rel_path: str) -> str:
    # Proper URL encoding for path segments
    parts = rel_path.split("/")
    safe_parts = [urllib.parse.quote(p) for p in parts]
    safe_path = "/".join(safe_parts)
    return f"https://raw.githubusercontent.com/{SRC_USER}/{SRC_REPO}/{SRC_BRANCH}/{safe_path}"


def fetch(url: str, token: str = "") -> bytes:
    req = urllib.request.Request(url)
    if token:
        req.add_header("Authorization", f"token {token}")
    req.add_header("User-Agent", "sync-selected-files/1.0")

    with urllib.request.urlopen(req, timeout=30) as resp:
        if resp.status != 200:
            raise RuntimeError(f"HTTP {resp.status}")
        return resp.read()


def sync_files(repo_root: Path, rel_paths: List[str]) -> Result:
    changed: List[str] = []
    unchanged: List[str] = []
    failed: List[str] = []

    for rel in rel_paths:
        target = repo_root / rel
        url = raw_url(rel)

        try:
            remote_data = fetch(url, GITHUB_TOKEN)
        except Exception as e:
            failed.append(f"{rel} (download failed: {e})")
            continue

        target.parent.mkdir(parents=True, exist_ok=True)

        if target.exists() and target.is_file():
            try:
                local_data = target.read_bytes()
            except Exception as e:
                failed.append(f"{rel} (read local failed: {e})")
                continue

            if sha256_bytes(local_data) == sha256_bytes(remote_data):
                unchanged.append(rel)
                continue

            # Replace
            try:
                target.write_bytes(remote_data)
                changed.append(rel)
            except Exception as e:
                failed.append(f"{rel} (write failed: {e})")
        else:
            # New file
            try:
                target.write_bytes(remote_data)
                changed.append(f"{rel} (new)")
            except Exception as e:
                failed.append(f"{rel} (write new failed: {e})")

    return Result(changed=changed, unchanged=unchanged, failed=failed)


def main(argv: List[str]) -> int:
    repo_root = Path.cwd()

    # Allow running from subdir: find a .git folder up the tree (optional convenience)
    cur = repo_root
    while cur != cur.parent and not (cur / ".git").exists():
        cur = cur.parent
    if (cur / ".git").exists():
        repo_root = cur

    result = sync_files(repo_root, FILES_TO_SYNC)

    print(f"\nSource: {SRC_USER}/{SRC_REPO}@{SRC_BRANCH}\n")

    print(f"CHANGED ({len(result.changed)}):")
    for p in result.changed:
        print(f"  - {p}")
    print()

    print(f"UNCHANGED ({len(result.unchanged)}):")
    for p in result.unchanged:
        print(f"  - {p}")
    print()

    print(f"FAILED ({len(result.failed)}):")
    for p in result.failed:
        print(f"  - {p}")

    return 2 if result.failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))