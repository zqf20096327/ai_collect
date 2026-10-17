# PAIONE Starter · Dein eigener Vault in 30 Minuten

> Alles in Markdown. Alles in Git. Alles unter deiner Kontrolle.

**Ein [PAIONE](https://paione.de)-Produkt · Gelehrt auf [Aiianer](https://aiianer.de)**

Build-in-Public-Serie & Workshops: [youtube.com/@aiianer](https://youtube.com/@aiianer) · [skool.com/aiianer](https://skool.com/aiianer)

---

## Was ist PAIONE?

PAIONE ist ein self-hosted AI-Betriebssystem für Solopreneure und kleine Teams. Statt deine Arbeit auf fünf SaaS-Tools zu verteilen (Notion für Notes, Linear für Tasks, Obsidian für Wissen, ClickUp für Projekte, proprietäre Agent-Plattformen), lebt alles in **einem Git-Repo als Markdown** — mit einer wachsenden Sammlung von Modulen darauf: Projekt-Management, Second Brain, Agent-Orchestrierung, Client-Portal.

Dieses Repo ist der **Starter** — die Basis-Vault-Struktur, auf der alle PAIONE-Module aufbauen. Es ist gleichzeitig der Einstiegspunkt ins Ökosystem: installier den Starter, lern die Architektur, und wenn du bereit bist, kommen die Module obendrauf.

## Warum PAIONE?

- **DSGVO ohne Workarounds** — läuft auf deinem Server, deine Daten gehören dir
- **Kein Vendor-Lock-in** — Markdown in Git ist in 20 Jahren noch lesbar
- **AI-native** — Agents wie Claude, Hermes, Mission Control verstehen Markdown nativ
- **Modular** — Second Brain, Client-Portal, Agent-Memory greifen auf denselben Vault zu, keine Silos
- **Audit-Trail by default** — jede Änderung ist ein Commit, `git log` ist dein Protokoll

## Was du am Ende hast

Ein Repo mit:

- **10 Top-Level-Ordner** nach durchdachtem Schema
- **SPEC.md** als Grundgesetz deines Vaults
- **JSON-Schemas** die Frontmatter-Fehler automatisch verhindern
- **Templates** für neue Tasks, Notizen, Projekte
- **Pre-commit Hook** der Schema-Konsistenz durchsetzt
- **5 Beispiel-Dateien** damit das System vom ersten Tag an lebt

## Voraussetzungen

| Was | Wie prüfen |
|---|---|
| Git | `git --version` |
| Git-Host | Forgejo empfohlen, GitHub/Gitea geht auch |
| Terminal | Bash/Zsh auf Linux/macOS, Windows: WSL2 |

Du brauchst **nicht**: Docker, Node.js, eine Datenbank. Nur Git, Python, Texteditor.

## Los geht's

### Weg A — Automatisch (5 Min)

```bash
git clone https://forgejo.hr-applab.de/paione/paione-starter.git mein-vault
cd mein-vault
./scripts/setup.sh
```

### Weg B — Schritt für Schritt (30 Min)

Öffne [`docs/SETUP.md`](docs/SETUP.md) — jeder Schritt mit **Warum, Was, Wie**. Empfohlener Weg beim ersten Mal.

### Weg C — Video mitmachen

Schau die [Aiianer YouTube-Serie](https://youtube.com/@aiianer) und mach live mit.

## Repo-Struktur

```
paione-starter/
├── README.md                         ← du bist hier
├── LICENSE                           ← MIT
├── BRAND.md                          ← Attribution-Guidelines
├── .gitignore                        ← blockiert Binärdateien
├── .githooks/
│   └── pre-commit                    ← Bash-Hook, validiert Frontmatter
├── 00_meta/
│   ├── SPEC.md                       ← das Grundgesetz (Specification)
│   ├── mcp-scopes.yaml               ← Agent-Berechtigungen
│   ├── schemas/                      ← JSON-Schemas (7 Stück)
│   └── templates/                    ← Vorlagen für neue Files (5 Stück)
├── 10_projects/                      ← Aktive Projekte + Tasks
├── 20_notes/
│   ├── daily/                        ← Tages-Journal
│   ├── topics/                       ← Dauerhaftes Wissen
│   └── fleeting/                     ← Inbox / unsortiert
├── 30_captures/
│   ├── urls/                         ← gescrapte Webseiten
│   ├── youtube/                      ← Video-Transkripte
│   ├── voice/                        ← Sprach-Transkripte
│   └── pdfs/                         ← PDF-Extrakte
├── 40_customers/                     ← B2B-Kunden (Phase 5)
├── 50_decisions/                     ← Architektur-Entscheidungen
├── 60_meetings/                      ← Meeting-Notes
├── 70_pai/
│   ├── context/                      ← Agent-Kontext
│   ├── workflows/                    ← Agent-Abläufe
│   ├── memory/                       ← Cognee Sync-State
│   └── interventions/                ← Agent-Vorschläge
├── 80_brand/
│   ├── youtube/                      ← Video-Scripts
│   ├── newsletter/                   ← Newsletter-Entwürfe
│   └── social/                       ← Social-Media-Posts
├── 99_archive/                       ← Erledigtes (read-only)
├── docs/
│   ├── SETUP.md                      ← Schritt-für-Schritt-Anleitung
│   ├── WARUM.md                      ← Design-Entscheidungen erklärt
│   └── FAQ.md                        ← Häufige Stolpersteine
├── scripts/
│   ├── setup.sh                      ← Ein-Klick-Setup
│   └── new-file.sh                   ← Helper für neue Files
└── examples/                         ← 5 Beispiel-Dateien
```

## Das PAIONE-Ökosystem

Dieser Starter ist das Fundament. Weitere Module, die darauf aufsetzen (kommen Schritt für Schritt in der Aiianer-Serie):

- **PAIONE PM** — Next.js PWA für Kanban, Calendar, File-View
- **PAIONE Brain** — Capture-Pipeline (URL/YouTube/Voice/PDF → Markdown) + Cognee als RAG-Layer
- **PAIONE Agent** — Hermes-Integration mit MCP-Anbindung an den Vault
- **PAIONE Client** — Git-native Client-Portale

Jedes Modul ist ein eigenständiges Repo, greift aber auf denselben Vault-Standard zu, den dieser Starter etabliert.

## Nächste Schritte nach dem Setup

1. **Erstes Projekt anlegen** — `./scripts/new-file.sh project mein-projekt`
2. **Erste Notiz** — in `20_notes/topics/` oder via Helper-Script
3. **Push zu deinem eigenen Git-Host**
4. **Aiianer-Community joinen** um beim nächsten Modul dabei zu sein

## Lizenz

MIT — nutze es, forke es, bau drauf auf. Details in [`LICENSE`](LICENSE).

Wenn du nett sein willst: ein Link zu PAIONE oder Aiianer macht uns happy. Details in [`BRAND.md`](BRAND.md).

## Die Brands dahinter

| | PAIONE | Aiianer |
|---|---|---|
| **Was** | Produkt-Ökosystem | Content & Community |
| **Inhalt** | Repos, Agents, Module, Infrastruktur | YouTube, Workshops, Kurse, Skool |
| **Du findest uns** | [paione.de](https://paione.de) | [aiianer.de](https://aiianer.de) |
| **Kontakt** | [hi@paione.de](mailto:hi@paione.de) | [hi@aiianer.de](mailto:hi@aiianer.de) |

**Beide Marken, ein Mensch:** Oliver Hees · [HR Code Labs](https://hr-codelabs.de) · Hamburg.

## Support

1. **FAQ lesen** — [`docs/FAQ.md`](docs/FAQ.md) deckt die häufigsten Stolpersteine ab
2. **Issue öffnen** — in diesem Repo
3. **In der Community fragen** — [skool.com/aiianer](https://skool.com/aiianer)

Los geht's.

— Oliver · [@aiianer](https://youtube.com/@aiianer)
