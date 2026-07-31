#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
commands = [
    [sys.executable, str(ROOT / "scripts/validate.py")],
    [sys.executable, str(ROOT / "scripts/build_indexes.py")]
]
for command in commands:
    subprocess.run(command, check=True)
print("PoE2 Research Database V1 initialized.")
