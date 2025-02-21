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
