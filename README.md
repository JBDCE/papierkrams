# Papierkrams

Repository um Steuererklärungsunterlagen aus meiner Paperless Instanz zu laden und in ein Format für die Steuererklärung zu überführen

## Initiale Anforderungen
 - Paperless API anbindung mit Konfiguration über config datei
 - Auslesen aller Rechnugsdokumente
 - Ausgabe als CSV Datei mit den Spalten: Empfänger, Eingangsdatum, Betrag

## Benutzung

### Windows
 - Ordner in der Powershell öffnen
 - Virtualenv Initialisieren: `python3 -m venv venv`
 - Virtualenv aktivieren: `.\venv\bin\activate.ps1`
 - Abhängigkeiten installieren `pip install -r requirements.txt`
 - Evtl. Konfiguration anpassen
 - Main Skript ausführen `python3 -m main`


## Lessons Learned
Das Skript mit Testdaten zu füttern war eine gute Idee.
Generell mehr Testdaten zu haben ist hilfreich.
TODO Beim nächsten mal vlt. direkt mit Tox tests bauen anstelle main Funktionen zu benutzen?

Den kompletten Prozess vorher getestet zu haben
und Testdaten die nah an den Echten Daten sind war hilfreich.

Dass jede Rechnug einzeln eingescannt werden mussten war anstrengend.
Da ich die einzelnen Rechnungen aber als einzelne Dokumente haben wollte führte kein Weg daran vorbei.
TODO fürs nächste mal. Einen PDF Editor finden der die Dateien zerstückeln kann.

Der Bottleneck war nicht das Bearbeiten der Dateien in Paperless sondern das Einscannen der Dateien.

TODO Richte endlich die verdammte Email verarbeitung ein damit du diesen scheiß nicht nochmal ausdrucken und dann wieder einscannen must du opfer.