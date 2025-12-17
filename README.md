# GommeHD IP List Generator

Dieses Projekt erzeugt automatisch eine `gommehd-ips.txt`, die IP‑Adressen sammelt,
die über öffentliche Minecraft-Servertracker für `gommehd.net` gefunden werden.

Die Datei kann direkt in OPNsense als **URL Table Alias** genutzt werden.

Beispiel:
https://raw.githubusercontent.com/proofy/gommehd-iplist-gen/main/gommehd-ips.txt


## Funktionsweise

1. GitHub Action läuft täglich um 03:00 UTC.  
2. Ruft folgende Quellen ab:
   - https://mclist.co/server/gommehd.net
   - https://crafty.gg/servers/gommehd.net
   - https://minecraft-statistic.net
3. Extrahiert IPv4-Adressen.
4. Entfernt Duplikate.
5. Speichert die Liste als `gommehd-ips.txt`.
6. Commit nur bei echten Änderungen.

## Repository Struktur

/
├── .github/workflows/update.yml
├── scripts/build_list.py
└── gommehd-ips.txt


## Verwendung in OPNsense

Firewall → Aliases → URL Table:

https://raw.githubusercontent.com/proofy/gommehd-iplist-gen/main/gommehd-ips.txt


Update-Intervall: z. B. 1 Stunde.

## Hinweis

Die IPs stammen aus öffentlichen Trackern, nicht aus offiziellen GommeHD‑Quellen.

## Lizenz

MIT

