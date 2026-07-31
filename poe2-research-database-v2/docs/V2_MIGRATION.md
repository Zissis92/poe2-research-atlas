# V1 to V2 migration

V2 is a drop-in replacement for the V1 database folder. Existing non-empty normalized datasets are retained. New empty datasets and schemas introduce no invented game facts.

After upload run:

```bash
python -m pip install -r requirements.txt
python scripts/validate_v2.py
python scripts/build_graph.py
python scripts/query_graph.py --entity <id>
```
