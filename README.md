# PoE2 Research Atlas v0.7

Diese Version ist für GitHub Pages und Safari auf dem iPhone vorbereitet.

## Veröffentlichung über GitHub Pages

1. Auf github.com anmelden.
2. Ein neues öffentliches Repository namens `poe2-research-atlas` anlegen.
3. Im Repository `Add file` → `Upload files` öffnen.
4. Den INHALT dieses Ordners hochladen:
   - index.html
   - manifest.webmanifest
   - sw.js
5. `Commit changes` drücken.
6. `Settings` → `Pages` öffnen.
7. Unter `Build and deployment`:
   - Source: `Deploy from a branch`
   - Branch: `main`
   - Folder: `/ (root)`
8. Speichern. Nach kurzer Zeit erscheint die Website unter:
   `https://DEIN-GITHUB-NAME.github.io/poe2-research-atlas/`

## Erste Benutzung

1. Website in Safari öffnen.
2. Links oben das Menü öffnen.
3. `GGG-Baum laden` drücken.
4. Nach dem Laden wird der Datensatz im Browser gespeichert.
5. In Safari über Teilen → `Zum Home-Bildschirm` hinzufügen.

## Datenquelle

Die App lädt:
https://raw.githubusercontent.com/grindinggear/poe2-skilltree-export/main/data.json

Offizielles Repository:
https://github.com/grindinggear/poe2-skilltree-export

## Hinweise

- Die erste Datenladung benötigt Internet.
- Danach bleiben die Baumdaten im lokalen Browser-Cache.
- Markierte Passivpunkte werden auf diesem Gerät gespeichert.
- GitHub Pages benötigt ein öffentliches Repository, sofern kein kostenpflichtiger Plan für private Pages verwendet wird.


## Wichtig bei Update von v0.3

Safari kann die alte Datei im Cache behalten.

1. Die neuen v0.7-Dateien vollständig ins GitHub-Repository hochladen und bestehende Dateien ersetzen.
2. Danach die Website in Safari öffnen.
3. Falls weiterhin die alte Version erscheint:
   - Safari-Tab schließen,
   - Einstellungen → Apps → Safari → Erweitert → Websitedaten,
   - den Eintrag `github.io` beziehungsweise die Atlas-Seite löschen,
   - Seite erneut öffnen.
4. Oben im Atlas muss `v0.7` stehen.


## Fehlerkorrektur v0.7

In v0.4 enthielt der Drag-and-drop-Handler einen JavaScript-Syntaxfehler.
Dadurch startete die Anwendung überhaupt nicht und blieb bei
`Prüfe Offline-Cache …` stehen.

Nach dem Upload muss oben `v0.7` stehen. Falls weiterhin v0.4 erscheint,
die Seite mit Strg+F5 neu laden oder die Websitedaten der GitHub-Pages-Seite löschen.


## Layout-Korrektur v0.7

Der Renderer ermittelt die Gruppenzuordnung jetzt auf zwei Wegen:

- direkt über `node.group`
- über die in jeder Gruppe enthaltene Knotenliste

Knoten ohne belastbare Position werden nicht mehr bei 0/0 übereinander gezeichnet.
Die Diagnose zeigt nun `Darstellbar`, `Ohne Position` und `Gruppenzuordnungen`.

Nach dem Update:
1. Alte Dateien im Repository ersetzen.
2. Strg+F5 drücken.
3. Im Atlas `Baum-Cache löschen`.
4. `GGG-Baum laden` drücken, damit der Datensatz neu normalisiert wird.


## Verifizierte Layout-Korrektur v0.7

Die Korrektur wurde gegen den tatsächlich verwendeten Export getestet.

Erkannte Struktur:
- Knoten: 5151
- Knoten mit fertigen x/y-Koordinaten: 5150
- Gruppen: 1621
- Kanten: 6074
- Grenzen: x -22597 bis 21814, y -18720 bis 20053

Wesentliche Änderung:
- `node.x` und `node.y` werden direkt verwendet.
- Gruppenmittelpunkt und Orbit werden nicht erneut addiert.
- Verbindungen werden primär aus dem Top-Level-Feld `edges` gelesen.

Nach dem Upload:
1. Alle Dateien ersetzen.
2. Strg+F5.
3. Baum-Cache löschen.
4. GGG-Baum neu laden.
5. Oben muss v0.7 stehen.
