#!/usr/bin/env python3
"""Validate JSON syntax, IDs and optional JSON schemas."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

for path in ROOT.rglob("*.json"):
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")

for path in (ROOT / "database/normalized").glob("*.json"):
    payload = json.loads(path.read_text(encoding="utf-8"))
    records = payload.get("records", [])
    ids = [r.get("id") for r in records if isinstance(r, dict) and "id" in r]
    duplicate_ids = sorted({x for x in ids if ids.count(x) > 1})
    if duplicate_ids:
        errors.append(f"{path.name}: duplicate IDs: {duplicate_ids}")

try:
    import jsonschema
    skill_schema = json.loads((ROOT / "schemas/skill.schema.json").read_text())
    skills = json.loads((ROOT / "database/normalized/skills.json").read_text())["records"]
    for record in skills:
        jsonschema.validate(record, skill_schema)
except ModuleNotFoundError:
    print("Note: install jsonschema for schema validation: pip install jsonschema")
except Exception as exc:
    errors.append(f"Schema validation: {exc}")

if errors:
    print("\n".join(f"ERROR: {e}" for e in errors))
    sys.exit(1)
print("Validation passed.")
