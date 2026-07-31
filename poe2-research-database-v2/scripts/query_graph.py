#!/usr/bin/env python3
"""Minimal graph query CLI."""
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(p): return json.loads((ROOT/p).read_text(encoding='utf-8'))
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--entity'); ap.add_argument('--tag'); ap.add_argument('--compatible-supports'); a=ap.parse_args()
 idx=load('database/generated/entity_index.json')
 if a.entity: print(json.dumps(idx.get(a.entity),indent=2,ensure_ascii=False))
 elif a.tag: print(json.dumps(load('database/generated/tag_index.json').get(a.tag,[]),indent=2,ensure_ascii=False))
 elif a.compatible_supports:
  rows=load('database/generated/support_compatibility.json').get(a.compatible_supports,{})
  print(json.dumps({k:v for k,v in rows.items() if v['status']=='compatible'},indent=2,ensure_ascii=False))
 else: ap.print_help()
if __name__=='__main__': main()
