#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import os
import json
import re
import shutil
from datetime import datetime

image_metadata = None

# Matches {% include embed/image.html key="value" ... %}
IMAGE_TAG_RE = re.compile(
    r'\{%-?\s*include\s+embed/image\.html\s+(.*?)\s*-?%\}',
    re.DOTALL
)

# Matches individual key="value" pairs inside a tag
ATTR_RE = re.compile(r'(\w+)="([^"]*)"')


def load_metadata():
    global image_metadata
    image_metadata = {}
    for item in json.load(open('metadata.json', 'r', encoding='utf-8')):
        fname = item['file_name']
        url = item.get('image_url')
        if url:
            image_fname = os.path.basename(url).split('.')[0]
            if image_fname in image_metadata:
                pass # print(f'Warning: Duplicate image filename {image_fname} for URL {url}')
            else:
                image_metadata[image_fname] = item
        else:
            image_metadata[fname] = item


def get_image_attrs(attrs_str):
    """Parse all key="value" pairs from a tag's attribute string into an ordered dict."""
    return dict(ATTR_RE.findall(attrs_str))


def build_image_tag(attrs):
    """Reconstruct a Liquid include tag from an attribute dict."""
    pairs = ' '.join(f'{k}="{v}"' for k, v in attrs.items())
    return '{{% include embed/image.html {} %}}'.format(pairs)


def enrich_tag_from_metadata(src):
    """
    Look up an image by its src filename stem in the loaded metadata.
    Returns (caption, attribution) strings, either of which may be None
    if not found in the metadata record.

    Adjust the field names below to match your actual metadata.json schema.
    """
    stem = os.path.splitext(os.path.basename(src))[0]
    meta = image_metadata.get(stem)
    if not meta:
        return None, None

    # Try common field names for caption — adjust as needed
    caption = (
        meta.get('caption') or
        meta.get('label') or
        meta.get('title')
    )

    # Try common field names for attribution — adjust as needed
    attribution = (
        meta.get('attribution') or
        meta.get('credit') or
        meta.get('source')
    )

    return caption or None, attribution or None


def update_essay_captions(md):
    """
    Find all embed/image.html tags in the markdown string.
    For any tag missing a 'caption' attribute, attempt to populate
    'caption' (and optionally 'attribution') from image metadata.
    Returns the (possibly modified) markdown string and a count of tags changed.
    """
    if image_metadata is None:
        load_metadata()

    changes = 0

    def replace_tag(match):
        nonlocal changes
        original_tag = match.group(0)
        attrs = get_image_attrs(match.group(1))

        if 'caption' in attrs:
            return original_tag   # already has a caption — leave it alone

        src = attrs.get('src', '')
        if not src:
            return original_tag   # no src to look up
        if src.startswith('wc:'):
            return original_tag   # Wikimedia Commons ref — skip

        caption, attribution = enrich_tag_from_metadata(src)

        if caption is None:
            print(f'  [no metadata] {src}')
            return original_tag   # nothing to add

        attrs['caption'] = caption
        if attribution:
            attrs['attribution'] = attribution

        changes += 1
        updated_tag = build_image_tag(attrs)
        print(f'  [updated] {src}')
        print(f'    caption:     {caption}')
        if attribution:
            print(f'    attribution: {attribution}')
        return updated_tag

    updated_md = IMAGE_TAG_RE.sub(replace_tag, md)
    return updated_md, changes


def update_captions(src, write=False, max=None):
    ctr = 0
    total_changes = 0

    for root, dirs, files in os.walk(src):
        for filename in sorted(files):
            if not filename.endswith('.md') or filename == '.template.md':
                continue

            ctr += 1
            file_path = os.path.join(root, filename)
            print(f'\nProcessing: {file_path}')

            with open(file_path, 'r', encoding='utf-8') as f:
                original = f.read()

            updated, changes = update_essay_captions(original)
            total_changes += changes

            if changes and write:
                # Back up the original before overwriting
                '''
                backup_path = file_path + '.bak'
                shutil.copy2(file_path, backup_path)
                '''
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated)
                # print(f'  Wrote {changes} change(s) — backup at {backup_path}')
            elif changes:
                print(f'  {changes} change(s) pending (re-run with --write to apply)')

            if max and ctr >= max:
                break
        else:
            continue
        break  # respect --max across subdirectories

    print(f'\nDone. {ctr} file(s) scanned, {total_changes} tag(s) updated.')


# ============================================================================
# CLI Entry Point
# ============================================================================

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Update essay captions and attribution.'
    )
    parser.add_argument(
        '--src',
        default='/Users/ron/projects/plant-humanities/plant-humanities-lab/_posts',
        help='Path to source directory'
    )
    parser.add_argument(
        '--write',
        action='store_true',
        default=False,
        help='Write changes back to the source files (default: dry run)'
    )
    parser.add_argument(
        '--max',
        type=int,
        default=None,
        help='Maximum number of files to process (for testing)'
    )

    args = vars(parser.parse_args())
    update_captions(**args)