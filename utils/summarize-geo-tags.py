import csv
from collections import defaultdict

INPUT_CSV = "geo_tags.csv"
OUTPUT_CSV = "geo_tags_category_tag_summary.csv"

CATEGORIES = [
    ("origin", "origin_regions"),
    ("circulation", "circulation_regions"),
    ("cultural", "cultural_regions"),
]

def split_regions(cell: str):
    if not cell:
        return []
    return [r.strip() for r in cell.split(";") if r.strip()]

def main(input_csv=INPUT_CSV, output_csv=OUTPUT_CSV):
    # key: "category:Region" -> set(essay_id)
    combo_to_essays = defaultdict(set)

    with open(input_csv, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=1):
            essay_id = (row.get("essay_id") or "").strip() or f"row_{i}"

            for cat, col in CATEGORIES:
                regions = set(split_regions(row.get(col, "")))  # dedupe within essay/category
                for region in regions:
                    key = f"{cat}:{region}"
                    combo_to_essays[key].add(essay_id)

    rows = []
    for key, essays in combo_to_essays.items():
        cat, region = key.split(":", 1)
        rows.append({
            "category_tag": key,          # e.g., origin:North America
            "category": cat,              # e.g., origin
            "tag": region,                # e.g., North America
            "count": len(essays),
            "essay_ids": "; ".join(sorted(essays)),
        })

    # Sort: category, then count desc, then tag
    cat_order = {c[0]: idx for idx, c in enumerate(CATEGORIES)}
    rows.sort(key=lambda r: (cat_order.get(r["category"], 999), -r["count"], r["tag"].lower()))

    with open(output_csv, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["category_tag", "category", "tag", "count", "essay_ids"],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {output_csv}")

if __name__ == "__main__":
    main()