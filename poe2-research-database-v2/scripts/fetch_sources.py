#!/usr/bin/env python3
"""Download configured PoE2 source data without modifying normalized records."""
from pathlib import Path
import json
import urllib.request
import hashlib
import datetime

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "database/raw/source_manifest.json").read_text(encoding="utf-8"))

for source in manifest["sources"]:
    target = ROOT / source["target"]
    target.parent.mkdir(parents=True, exist_ok=True)
    print(f"Fetching {source['id']} ...")
    try:
        with urllib.request.urlopen(source["url"], timeout=90) as response:
            data = response.read()
        target.write_bytes(data)
        checksum = hashlib.sha256(data).hexdigest()
        meta = {
            "source_id": source["id"],
            "url": source["url"],
            "fetched_at_utc": datetime.datetime.now(datetime.UTC).isoformat(),
            "sha256": checksum,
            "bytes": len(data)
        }
        target.with_suffix(target.suffix + ".meta.json").write_text(
            json.dumps(meta, indent=2), encoding="utf-8"
        )
        print(f"  saved {len(data):,} bytes")
    except Exception as exc:
        print(f"  ERROR: {exc}")
