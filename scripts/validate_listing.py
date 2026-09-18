#!/usr/bin/env python3
"""Validate counts and prohibited words in a structured Amazon Listing JSON."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


DEFAULT_PROHIBITED = [
    "kid", "kids", "child", "children", "toy", "toys",
    "set", "sets", "kit", "kits", "pack", "packs", "bundle", "bundles",
    "suite", "suites", "combination", "combinations",
    "best", "bestseller", "premium",
]

DEFAULT_INTERNAL_MARKERS = [
    "待确认", "未确认", "确认后", "需补充", "资料未提供", "以图片为准",
    "后再填写", "后再补充", "Produktdaten", "Produktabbildungen",
    "Formulierung", "Suchform", "erst ergänzt", "richtet sich nach",
]


def count_chars(value: str) -> int:
    return len(value)


def count_bytes(value: str) -> int:
    return len(value.encode("utf-8"))


def find_terms(value: str, terms: list[str]) -> list[str]:
    found = []
    for term in terms:
        if re.search(rf"(?<!\w){re.escape(term)}(?!\w)", value, flags=re.I):
            found.append(term)
    return found


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("json_file", type=Path)
    parser.add_argument("--title-min", type=int, default=65)
    parser.add_argument("--title-max", type=int, default=70)
    parser.add_argument("--highlight-min", type=int, default=120)
    parser.add_argument("--highlight-max", type=int, default=125)
    parser.add_argument("--bullet-min", type=int, default=300)
    parser.add_argument("--bullet-max", type=int, default=350)
    parser.add_argument("--search-min", type=int, default=240)
    parser.add_argument("--search-max", type=int, default=249)
    args = parser.parse_args()

    data = json.loads(args.json_file.read_text(encoding="utf-8"))
    title = str(data.get("title", ""))
    highlights = str(data.get("item_highlights", ""))
    bullets = [str(x) for x in data.get("bullets", [])]
    description = str(data.get("description", ""))
    search_terms = str(data.get("search_terms", ""))
    prohibited = [str(x) for x in data.get("prohibited_terms", DEFAULT_PROHIBITED)]
    internal_markers = [str(x) for x in data.get("internal_markers", DEFAULT_INTERNAL_MARKERS)]
    title_cn = str(data.get("title_cn", ""))
    highlights_cn = str(data.get("item_highlights_cn", ""))
    bullets_cn = [str(x) for x in data.get("bullets_cn", [])]
    description_cn = str(data.get("description_cn", ""))
    keyword_placements = data.get("keyword_placements", [])
    bullet_topics = data.get("bullet_topics", [])

    report = {
        "title_chars": count_chars(title),
        "item_highlights_chars": count_chars(highlights),
        "bullet_chars": [count_chars(x) for x in bullets],
        "description_chars": count_chars(re.sub(r"<[^>]+>", "", description)),
        "search_term_bytes": count_bytes(search_terms),
        "prohibited_hits": {},
        "internal_review_hits": {},
        "embedded_keyword_count": 0,
        "errors": [],
    }

    if len(bullets) != 5:
        report["errors"].append(f"bullet count must be exactly 5: got {len(bullets)}")

    profile_id = str(data.get("profile_id", ""))
    if profile_id != "KAIHA-LISTING-2026-V10":
        report["errors"].append("missing or incorrect profile_id: expected KAIHA-LISTING-2026-V10")

    if not isinstance(bullet_topics, list) or len(bullet_topics) != 5:
        report["errors"].append("bullet_topics must contain exactly 5 product-specific topics")
    else:
        normalized_topics = {" ".join(str(value).strip().lower().split()) for value in bullet_topics if str(value).strip()}
        if len(normalized_topics) != 5:
            report["errors"].append("bullet_topics must contain 5 distinct nonempty topics")

    if not isinstance(keyword_placements, list):
        report["errors"].append("keyword_placements must be a list")
        keyword_placements = []

    embedded_keywords = set()
    for index, item in enumerate(keyword_placements, start=1):
        if not isinstance(item, dict):
            report["errors"].append(f"keyword_placements[{index}] must be an object")
            continue
        keyword = " ".join(str(item.get("keyword", "")).strip().lower().split())
        approved = item.get("approved") is True
        placements = item.get("placements", [])
        if approved and keyword and isinstance(placements, list) and any(str(value).strip() for value in placements):
            embedded_keywords.add(keyword)

    report["embedded_keyword_count"] = len(embedded_keywords)
    if report["embedded_keyword_count"] < 25:
        report["errors"].append(
            f"fewer than 25 unique approved embedded keywords: {report['embedded_keyword_count']} < 25"
        )

    if "|" not in highlights:
        report["errors"].append("item_highlights must contain vertical-bar separators")

    for i, bullet in enumerate(bullets):
        if not re.match(r"^【[^】]{2,80}】\s+", bullet):
            report["errors"].append(f"bullet_{i+1} must start with 【Title Phrase】 followed by a space")

    fields = {"title": title, "item_highlights": highlights, "description": description, "search_terms": search_terms}
    fields.update({f"bullet_{i+1}": value for i, value in enumerate(bullets)})
    fields.update({"title_cn": title_cn, "item_highlights_cn": highlights_cn, "description_cn": description_cn})
    fields.update({f"bullet_{i+1}_cn": value for i, value in enumerate(bullets_cn)})
    for name, value in fields.items():
        hits = find_terms(value, prohibited)
        if hits:
            report["prohibited_hits"][name] = hits
        internal_hits = [marker for marker in internal_markers if marker.lower() in value.lower()]
        if internal_hits:
            report["internal_review_hits"][name] = internal_hits

    def check_range(label: str, value: int, low: int | None, high: int | None) -> None:
        if low is not None and value < low:
            report["errors"].append(f"{label} below minimum: {value} < {low}")
        if high is not None and value > high:
            report["errors"].append(f"{label} above maximum: {value} > {high}")

    check_range("title", report["title_chars"], args.title_min, args.title_max)
    check_range("item_highlights", report["item_highlights_chars"], args.highlight_min, args.highlight_max)
    for i, value in enumerate(report["bullet_chars"]):
        check_range(f"bullet_{i+1}", value, args.bullet_min, args.bullet_max)
    check_range("search_terms", report["search_term_bytes"], args.search_min, args.search_max)
    if report["prohibited_hits"]:
        report["errors"].append("prohibited terms found")
    if report["internal_review_hits"]:
        report["errors"].append("internal review language found in customer-facing copy")

    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
