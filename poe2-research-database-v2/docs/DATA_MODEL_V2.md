# Core data model V2

V2 separates facts, relations, hypotheses and generated conclusions.

## Layers

1. `database/raw/` — untouched source snapshots and source manifests.
2. `database/normalized/` — canonical entities and confirmed/inferred interaction edges.
3. `database/research/` — experiments, hypotheses, overrides and rejected claims.
4. `database/generated/` — deterministic indexes produced by `build_graph.py`.

## Entity identity

Every entity has one stable lowercase ID. Names may change; IDs should not. IDs are globally unique across all normalized datasets.

## Evidence discipline

Unknown values stay `null` or absent. A hypothesis never becomes a normalized fact until evidence changes its status. Every record requiring a schema carries provenance.

## Interaction graph

Interactions are directed edges with `from_id`, `to_id`, `relation`, `status`, conditions and provenance. Patch bounds allow historical and current relationships to coexist.

## Support compatibility

Compatibility has three outputs: compatible, incompatible, unknown. The engine does not guess. It evaluates explicit inclusions/exclusions and complete tag rules only.

## Modifier model

Modifiers record operation, scope, calculation stage, conditions and stacking group. This supports later calculation engines without storing ambiguous prose as arithmetic.
