# Datenmodell

## Grundsatz

Jeder Datensatz braucht eine eindeutige ID und Provenienz. Unsichere Zahlen werden nicht geschätzt.

## Trennung

- Fakten: `database/normalized`
- Originalquellen: `database/raw`
- Hypothesen und Bewertungen: `database/research`

## Skill-ID

IDs sind stabile, kleingeschriebene Slugs. Anzeigenamen dürfen sich ändern, IDs nur durch Migration.

## Provenienz

Jede manuelle Ergänzung enthält:

```json
{
  "confidence": "verified_manual",
  "sources": ["in_game_screenshot"],
  "verified_at": "YYYY-MM-DD"
}
```

## Null-Werte

`null` bedeutet unbekannt oder noch nicht normalisiert. Es bedeutet niemals automatisch null, 0 oder false im Spiel.
