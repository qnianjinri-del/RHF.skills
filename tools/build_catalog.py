#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "skills.json"
OUTPUT = ROOT / "docs" / "CATALOG.md"


def load_registry() -> dict:
    with REGISTRY.open("r", encoding="utf-8") as f:
        return json.load(f)


def build() -> str:
    data = load_registry()
    entries = data.get("entries", [])
    grouped: dict[str, list[dict]] = defaultdict(list)
    for entry in entries:
        grouped[entry.get("theme", "unknown")].append(entry)

    lines: list[str] = []
    lines.append("# Catalog")
    lines.append("")
    lines.append(f"Total entries: **{len(entries)}**")
    lines.append("")

    for theme in sorted(grouped):
        items = sorted(grouped[theme], key=lambda x: x.get("repo_full_name", ""))
        lines.append(f"## {theme}")
        lines.append("")
        lines.append("| Title | Repo | Object | Status | Strategy | Notes |")
        lines.append("|---|---|---|---|---|---|")
        for item in items:
            title = item.get("title", "")
            repo = item.get("repo_full_name", "")
            url = item.get("repo_url", "")
            obj = item.get("object_type", "")
            status = item.get("inspection_status", "")
            strategy = item.get("integration_strategy", "")
            notes = "；".join(item.get("notes", [])[:2])
            lines.append(f"| {title} | [{repo}]({url}) | {obj} | {status} | {strategy} | {notes} |")
        lines.append("")

    lines.append("## Status Legend")
    lines.append("")
    lines.append("- `inspected`: 已人工检查过 README / SKILL.md 或核心结构")
    lines.append("- `candidate_unverified`: 只按仓库名或弱信号命中，未完成核验")
    lines.append("- `rejected`: 明确不纳入")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    OUTPUT.write_text(build(), encoding="utf-8")
    print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
