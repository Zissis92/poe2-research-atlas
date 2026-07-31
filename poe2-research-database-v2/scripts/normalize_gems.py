#!/usr/bin/env python3
"""Best-effort normalizer for RePoE gem exports.

The upstream schema can change. Unknown fields are preserved in `source_payload`.
"""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]

def slug(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9]+", "_", value.strip().lower())
    return value.strip("_")

def records_from_payload(payload):
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for key in ("records", "data", "items"):
            if isinstance(payload.get(key), list):
                return payload[key]
        return [{"_source_key": k, **v} if isinstance(v, dict) else {"_source_key": k, "value": v}
                for k, v in payload.items()]
    return []

def pick_name(row):
    for key in ("Name", "name", "display_name", "DisplayName", "_source_key"):
        value = row.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return None

def normalize(source_name, output_name, kind):
    src = ROOT / "database/raw" / source_name
    if not src.exists():
        print(f"Skip: {src} not found. Run fetch_sources.py first.")
        return
    payload = json.loads(src.read_text(encoding="utf-8"))
    out = []
    for row in records_from_payload(payload):
        name = pick_name(row)
        if not name:
            continue
        out.append({
            "id": slug(name),
            "name": name,
            "kind": kind,
            "tags": row.get("tags", row.get("Tags", [])) if isinstance(row, dict) else [],
            "provenance": {
                "confidence": "extracted",
                "sources": [source_name],
                "verified_at": None
            },
            "source_payload": row
        })
    target = ROOT / "database/normalized" / output_name
    target.write_text(json.dumps({"records": out}, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {len(out)} records to {target}")

normalize("active_skill_gems.json", "skills.imported.json", "other")
normalize("support_skill_gems.json", "support_gems.imported.json", "support")
normalize("meta_skill_gems.json", "meta_gems.imported.json", "meta")
