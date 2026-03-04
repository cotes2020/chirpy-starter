#!/usr/bin/env python3
"""
Generate 2-sentence descriptions for Plant Humanities Lab essays
and write them back into each file's YAML front matter.

Uses the Anthropic Claude API to produce concise, engaging descriptions
suited to an audience of academics and botany enthusiasts.

Usage:
    pip install anthropic pyyaml
    export ANTHROPIC_API_KEY="your-api-key-here"
    python describe_essays.py /path/to/markdown/files

Options:
    --model MODEL    Claude model to use (default: claude-haiku-4-5-20251001)
    --output FILE    Write results to a JSON file in addition to stdout
    --limit N        Process only the first N files (useful for testing)
    --dry-run        Show descriptions without modifying files
"""

import os
import re
import sys
import json
import glob
import argparse
import yaml
from anthropic import Anthropic

SYSTEM_PROMPT = """\
You write descriptions for the Plant Humanities Lab, a site about the \
cultural histories of plants. Audience: academics and botany enthusiasts.

Given a Markdown essay, write a 2-sentence description. Strict rules:

- Maximum 25 words total across both sentences.
- Sentence 1: the plant and its key cultural or historical role.
- Sentence 2: one specific surprising fact from the essay.
- Every word must earn its place. Cut all modifiers that don't add meaning.
- Banned words: discover, delve, explore, journey, uncover, fascinating, \
  remarkable, reveals, unveils.
- No promotional phrasing. No preamble. Output only the two sentences.\
"""

# ---------------------------------------------------------------------------
# Front matter helpers
# ---------------------------------------------------------------------------

FRONT_MATTER_RE = re.compile(r"\A(---\s*\n)(.*?\n)(---\s*\n)", re.DOTALL)


def parse_file(text: str) -> tuple[dict | None, str]:
    """Split a Markdown file into (front_matter_dict, body).

    Returns (None, full_text) if no valid front matter is found.
    """
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return None, text
    fm_raw = m.group(2)
    body = text[m.end():]
    try:
        fm = yaml.safe_load(fm_raw)
    except yaml.YAMLError:
        return None, text
    return fm, body


def rebuild_file(fm: dict, body: str) -> str:
    """Serialize front matter + body back to a Markdown string.

    Uses block style for long string values (like description) so that
    the YAML stays readable and matches typical Jekyll conventions.
    """
    dumped = yaml.dump(
        fm,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
        width=80,
    )
    return f"---\n{dumped}---\n\n{body}"


# ---------------------------------------------------------------------------
# API call
# ---------------------------------------------------------------------------

def describe_essay(client: Anthropic, text: str, model: str) -> str:
    """Send a Markdown essay to Claude and get a 2-sentence description."""
    message = client.messages.create(
        model=model,
        max_tokens=150,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": text}
        ],
    )
    return message.content[0].text.strip()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Generate 2-sentence descriptions for Plant Humanities Lab essays."
    )
    parser.add_argument("directory", help="Directory containing .md files")
    parser.add_argument(
        "--model",
        default="claude-haiku-4-5-20251001",
        help="Claude model ID (default: claude-haiku-4-5-20251001)",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Optional path for JSON output file",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Max number of files to process (useful for testing)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show generated descriptions without modifying files",
    )
    args = parser.parse_args()

    md_files = sorted(glob.glob(os.path.join(args.directory, "*.md")))

    if not md_files:
        print(f"No .md files found in {args.directory}")
        sys.exit(1)

    if args.limit:
        md_files = md_files[: args.limit]

    # Uses ANTHROPIC_API_KEY env variable by default
    client = Anthropic()
    mode = "DRY RUN" if args.dry_run else "LIVE"

    print(f"[{mode}] Processing {len(md_files)} file(s) with {args.model}...\n")

    results = []

    for filepath in md_files:
        filename = os.path.basename(filepath)
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

        if not text.strip():
            print(f"  [{filename}]  (empty, skipped)\n")
            continue

        fm, body = parse_file(text)
        if fm is None:
            print(f"  [{filename}]  (no front matter, skipped)\n")
            continue

        old_desc = fm.get("description", "")

        try:
            new_desc = describe_essay(client, text, args.model)
            results.append({
                "file": filename,
                "old_description": old_desc,
                "new_description": new_desc,
            })
            print(f"  [{filename}]")
            print(f"    OLD: {old_desc}")
            print(f"    NEW: {new_desc}\n")

            if not args.dry_run:
                fm["description"] = new_desc
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(rebuild_file(fm, body))

        except Exception as e:
            results.append({"file": filename, "error": str(e)})
            print(f"  [{filename}]  Error: {e}\n")

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"Results written to {args.output}")


if __name__ == "__main__":
    main()