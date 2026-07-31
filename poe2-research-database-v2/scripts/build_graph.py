#!/usr/bin/env python3
"""Build deterministic graph indexes and infer support compatibility.

No game facts are invented. Compatibility is emitted only where explicit IDs or
complete tag rules permit a deterministic decision. Unknown cases remain unknown.
"""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[1]
N=ROOT/'database'/'normalized'; G=ROOT/'database'/'generated'; R=ROOT/'database'/'research'

def load(name:str)->list[dict[str,Any]]:
 p=N/f'{name}.json'
 data=json.loads(p.read_text(encoding='utf-8'))
 if not isinstance(data,list): raise TypeError(f'{p} must contain an array')
 return data

def dump(name:str,data:Any)->None:
 G.mkdir(parents=True,exist_ok=True)
 (G/name).write_text(json.dumps(data,indent=2,ensure_ascii=False,sort_keys=True)+'\n',encoding='utf-8')

def decision(skill:dict[str,Any],support:dict[str,Any])->dict[str,Any]:
 c=support.get('compatibility') or {}; mode=c.get('mode','unknown'); sid=skill['id']; tags=set(skill.get('tags',[]))
 if sid in c.get('excluded_skill_ids',[]): return {'status':'incompatible','reason':'explicit exclusion'}
 if sid in c.get('explicit_skill_ids',[]): return {'status':'compatible','reason':'explicit inclusion'}
 if mode not in {'tag_rules','hybrid'}: return {'status':'unknown','reason':'no deterministic rule'}
 req=set(c.get('required_tags',[])); any_=set(c.get('any_tags',[])); exc=set(c.get('excluded_tags',[]))
 if exc & tags: return {'status':'incompatible','reason':'excluded tag: '+', '.join(sorted(exc & tags))}
 if not req.issubset(tags): return {'status':'incompatible','reason':'missing required tag: '+', '.join(sorted(req-tags))}
 if any_ and not any_ & tags: return {'status':'incompatible','reason':'none of any_tags present'}
 return {'status':'compatible','reason':'tag rules satisfied'}

def main()->None:
 names=['skills','support_gems','spirit_gems','ascendancies','passives','uniques','item_bases','modifiers','mechanics','tags','monsters','bosses','interactions','patches']
 sets={n:load(n) for n in names}; idx={}; tag_idx={}; adjacency={}
 for n,rows in sets.items():
  for row in rows:
   eid=row['id']
   if eid in idx: raise ValueError(f'duplicate id: {eid}')
   idx[eid]={'dataset':n,'name':row.get('name')}
   for tag in row.get('tags',[]): tag_idx.setdefault(tag,[]).append(eid)
 for edge in sets['interactions']:
  adjacency.setdefault(edge['from_id'],[]).append({'to':edge['to_id'],'relation':edge['relation'],'status':edge['status'],'id':edge['id']})
 compat={}
 for skill in sets['skills']:
  compat[skill['id']]={support['id']:decision(skill,support) for support in sets['support_gems']}
 dump('entity_index.json',idx); dump('tag_index.json',{k:sorted(v) for k,v in tag_idx.items()}); dump('adjacency.json',adjacency); dump('support_compatibility.json',compat)
 print(f'Indexed {len(idx)} entities, {len(sets["interactions"])} edges, {len(sets["skills"])*len(sets["support_gems"])} compatibility pairs.')
if __name__=='__main__': main()
