#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "skills.json"

REQUIRED_FIELDS = {
    "id",
    "title",
    "repo_full_name",
    "repo_url",
    "theme",
    "object_type",
    "entry_file",
    "commands",
    "runtime_targets",
    "generated_output_dir",
    "license_signal",
    "inspection_status",
    "integration_strategy",
    "notes",
    "evidence",
}

ALLOWED_STATUS = {"inspected", "candidate_unverified", "rejected"}
ALLOWED_STRATEGY = {"reference_only", "submodule_candidate", "vendor_candidate", "rejected"}


def main() -> int:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    entries = data.get("entries", [])

    seen_ids: set[str] = set()
    errors: list[str] = []

    for idx, entry in enumerate(entries):
        prefix = f"entry[{idx}]"
        missing = REQUIRED_FIELDS - set(entry)
        if missing:
            errors.append(f"{prefix}: missing fields: {sorted(missing)}")

        entry_id = entry.get("id")
        if entry_id in seen_ids:
            errors.append(f"{prefix}: duplicate id: {entry_id}")
        elif entry_id:
            seen_ids.add(entry_id)

        status = entry.get("inspection_status")
        if status not in ALLOWED_STATUS:
            errors.append(f"{prefix}: invalid inspection_status: {status}")

        strategy = entry.get("integration_strategy")
        if strategy not in ALLOWED_STRATEGY:
            errors.append(f"{prefix}: invalid integration_strategy: {strategy}")

        if not isinstance(entry.get("notes", []), list):
            errors.append(f"{prefix}: notes must be a list")

        if not isinstance(entry.get("evidence", []), list):
            errors.append(f"{prefix}: evidence must be a list")

    if errors:
        print("registry validation failed:\n")
        for err in errors:
            print(f"- {err}")
        return 1

    print(f"registry validation passed: {len(entries)} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
