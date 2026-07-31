# PoE2 Research Database v2.0.0

A provenance-first graph database foundation for Path of Exile 2 build discovery.

## What V2 adds

- globally unique entities and canonical tags
- normalized modifiers with calculation stages
- directed interaction graph with evidence status and patch bounds
- deterministic support-compatibility engine with an explicit `unknown` state
- experiment and hypothesis registries
- patch history model
- generated entity, tag and adjacency indexes
- strict JSON Schema validation and cross-reference validation

## Quick start

```bash
python -m pip install -r requirements.txt
python scripts/validate_v2.py
python scripts/build_graph.py
```

No unknown game value is fabricated. Empty datasets are intentional until a verified importer or manual evidence fills them.

See `docs/DATA_MODEL_V2.md`, `docs/IMPORT_CONTRACT.md` and `docs/EXPERIMENT_PROTOCOL.md`.
