import os
import json
import csv
import re
from openai import OpenAI

client = OpenAI()

# ---- Controlled geographic vocabulary (edit as needed) ----
GEO_REGIONS = [
    # Continental / macro
    "Sub-Saharan Africa",
    "North Africa",
    "Mediterranean Basin",
    "Western Europe",
    "Eastern Europe",
    "South Asia",
    "Southeast Asia",
    "East Asia",
    "Central Asia",
    "Middle East",
    "Oceania",
    "North America",
    "Mesoamerica",
    "Caribbean",
    "South America",

    # Ecological / cultural / circulation regions
    "Amazon Basin",
    "Andean Highlands",
    "Himalayan Region",
    "Sahel",
    "Horn of Africa",
    "Tropical Africa",
    "Indian Ocean World",
    "Atlantic World",
    "Silk Road Region",
]

# ---- Core geo tag generation ----
def generate_geo_tags(text: str, max_chars: int = 12000) -> dict:
    """
    Returns a dict with keys:
      - origin_regions
      - circulation_regions
      - cultural_regions
    Each value is a list[str] of up to 5 regions selected from GEO_REGIONS.
    """
    clipped = text[:max_chars]

    prompt = f"""
You are a plant humanities scholar.

Task:
From the essay below, identify broad geographic regions that are central to:
1) the plant's origin / native range / early domestication (origin_regions)
2) historical circulation / trade / transfer / cultivation diffusion (circulation_regions)
3) cultural meaning / ritual / cuisine / symbolic or political significance (cultural_regions)

Rules:
- Select ONLY from this allowed list:
{GEO_REGIONS}
- Select at most 5 regions per category.
- Prioritize significance over completeness: pick the 3–5 strongest regions where possible.
- If a category is not supported by the essay, return an empty list for that category.
- Return STRICT JSON only, no prose.

Return JSON schema:
{{
  "origin_regions": ["Region", ...],
  "circulation_regions": ["Region", ...],
  "cultural_regions": ["Region", ...]
}}

Essay:
{clipped}
"""

    resp = client.responses.create(
        model="gpt-4.1",
        input=prompt,
        temperature=0.2,
    )

    raw = resp.output[0].content[0].text

    try:
        data = json.loads(raw)
    except Exception:
        print("JSON parse failure. Raw output:\n", raw)
        return {"origin_regions": [], "circulation_regions": [], "cultural_regions": []}

    # Defensive cleanup: enforce allowed list + max 5
    def clean(lst):
        if not isinstance(lst, list):
            return []
        seen = set()
        out = []
        for x in lst:
            if not isinstance(x, str):
                continue
            x = x.strip()
            if x in GEO_REGIONS and x not in seen:
                out.append(x)
                seen.add(x)
            if len(out) >= 5:
                break
        return out

    return {
        "origin_regions": clean(data.get("origin_regions", [])),
        "circulation_regions": clean(data.get("circulation_regions", [])),
        "cultural_regions": clean(data.get("cultural_regions", [])),
    }


def process_directory(input_dir: str = "./_posts", output_csv: str = "geo_tags.csv"):
    rows = []

    for filename in sorted(os.listdir(input_dir)):

        # ---- Skip hidden/system files ----
        if filename.startswith("."):
            continue

        if not filename.lower().endswith(".md"):
            continue

        # Remove extension
        base = os.path.splitext(filename)[0]

        # ---- Strip yyyy-mm-dd- prefix if present ----
        essay_id = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", base)

        filepath = os.path.join(input_dir, filename)

        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

        print(f"Processing: {essay_id}")

        tags = generate_geo_tags(text)

        rows.append({
            "essay_id": essay_id,
            "origin_regions": "; ".join(tags["origin_regions"]),
            "circulation_regions": "; ".join(tags["circulation_regions"]),
            "cultural_regions": "; ".join(tags["cultural_regions"]),
        })

    with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=["essay_id", "origin_regions", "circulation_regions", "cultural_regions"],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nDone. Output written to {output_csv}")


if __name__ == "__main__":
    process_directory()