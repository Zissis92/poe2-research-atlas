import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_manifest_version_and_policy():
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["database_version"] == "2.0.0"
    assert manifest["data_policy"]["no_invented_game_values"] is True


def test_core_directories_exist():
    for rel in ["database/normalized", "database/research", "database/generated", "schemas", "scripts", "docs"]:
        assert (ROOT / rel).exists()
