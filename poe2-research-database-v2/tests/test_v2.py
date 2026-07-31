import json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def test_manifest_v2():
 m=json.loads((ROOT/'manifest.json').read_text()); assert m['database_version']=='2.0.0'; assert m['data_policy']['no_invented_game_values'] is True
def test_required_datasets_exist():
 m=json.loads((ROOT/'manifest.json').read_text())
 for ds in m['datasets']: assert (ROOT/ds['path']).exists()
def test_graph_builder_runs():
 r=subprocess.run([sys.executable,str(ROOT/'scripts'/'build_graph.py')],cwd=ROOT,capture_output=True,text=True); assert r.returncode==0,r.stderr
 for f in ['entity_index.json','adjacency.json','tag_index.json','support_compatibility.json']: assert (ROOT/'database'/'generated'/f).exists()
