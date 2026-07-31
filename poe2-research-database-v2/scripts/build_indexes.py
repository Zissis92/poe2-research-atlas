#!/usr/bin/env python3
"""Build compact lookup indexes for browser or analysis tools."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
skills = json.loads((ROOT / "database/normalized/skills.json").read_text(encoding="utf-8"))["records"]

by_tag = {}
by_weapon = {}
for skill in skills:
    for tag in skill.get("tags", []):
        by_tag.setdefault(tag, []).append(skill["id"])
    for weapon in skill.get("weapon_restrictions", []):
        by_weapon.setdefault(weapon, []).append(skill["id"])

index = {
    "skill_by_id": {s["id"]: s["name"] for s in skills},
    "skill_ids_by_tag": {k: sorted(v) for k, v in sorted(by_tag.items())},
    "skill_ids_by_weapon": {k: sorted(v) for k, v in sorted(by_weapon.items())}
}
target = ROOT / "database/normalized/indexes.json"
target.write_text(json.dumps(index, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Wrote {target}")
