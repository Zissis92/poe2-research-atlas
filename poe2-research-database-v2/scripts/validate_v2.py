#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
try:
 import jsonschema
except ImportError:
 print('Missing dependency: pip install jsonschema',file=sys.stderr); raise SystemExit(2)

def main()->int:
 manifest=json.loads((ROOT/'manifest.json').read_text(encoding='utf-8')); ids={}; errors=[]
 datasets={}
 for ds in manifest['datasets']:
  path=ROOT/ds['path']; data=json.loads(path.read_text(encoding='utf-8')); datasets[ds['id']]=data
  if not isinstance(data,list): errors.append(f'{ds["id"]}: root must be an array'); continue
  if 'schema' in ds:
   sch=json.loads((ROOT/ds['schema']).read_text(encoding='utf-8')); validator=jsonschema.Draft202012Validator(sch)
   for i,row in enumerate(data):
    for e in validator.iter_errors(row): errors.append(f'{ds["id"]}[{i}] {e.json_path}: {e.message}')
  for i,row in enumerate(data):
   if isinstance(row,dict) and 'id' in row:
    if row['id'] in ids: errors.append(f'duplicate id {row["id"]}: {ids[row["id"]]} and {ds["id"]}[{i}]')
    ids[row['id']]=f'{ds["id"]}[{i}]'
 for i,e in enumerate(datasets.get('interactions',[])):
  for field in ('from_id','to_id'):
   if e.get(field) not in ids: errors.append(f'interactions[{i}].{field}: unknown entity {e.get(field)!r}')
 if errors:
  print('VALIDATION FAILED'); print('\n'.join('- '+x for x in errors)); return 1
 print(f'VALIDATION OK: {len(ids)} unique entities across {len(manifest["datasets"])} datasets'); return 0
if __name__=='__main__': raise SystemExit(main())
