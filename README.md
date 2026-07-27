# PoE2 Research Atlas v0.6

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

1. Die neuen v0.6-Dateien vollständig ins GitHub-Repository hochladen und bestehende Dateien ersetzen.
2. Danach die Website in Safari öffnen.
3. Falls weiterhin die alte Version erscheint:
   - Safari-Tab schließen,
   - Einstellungen → Apps → Safari → Erweitert → Websitedaten,
   - den Eintrag `github.io` beziehungsweise die Atlas-Seite löschen,
   - Seite erneut öffnen.
4. Oben im Atlas muss `v0.6` stehen.


## Fehlerkorrektur v0.6

In v0.4 enthielt der Drag-and-drop-Handler einen JavaScript-Syntaxfehler.
Dadurch startete die Anwendung überhaupt nicht und blieb bei
`Prüfe Offline-Cache …` stehen.

Nach dem Upload muss oben `v0.6` stehen. Falls weiterhin v0.4 erscheint,
die Seite mit Strg+F5 neu laden oder die Websitedaten der GitHub-Pages-Seite löschen.


## Layout-Korrektur v0.6

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
