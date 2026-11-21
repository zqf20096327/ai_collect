<!--
PaiBot – Startseite des Projekts: was PaiBot ist, Status, Schnellstart und Lizenz.

Autor:     Oliver Hees
Website:   https://paibot.de
Copyright: 2026 Oliver Hees. Alle Urheberrechte liegen beim Autor.
Lizenz:    PaiBot Fair-Code-Lizenz 1.1 – siehe Datei LICENSE im Projektstamm
Seit:      2026-11-07
-->

<p align="center">
  <img src="docs/assets/banner.png" alt="PaiBot – dein persönliches KI-Team" width="100%">
</p>

<p align="center">
  <a href="https://github.com/oliverhees/paibot/actions/workflows/ci.yml"><img src="https://github.com/oliverhees/paibot/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <img src="https://img.shields.io/badge/Lizenz-Fair--Code%20(eine%20Person)-ff6b1a" alt="Lizenz: Fair-Code, für eine Person">
  <img src="https://img.shields.io/badge/Status-Build%20in%20Public-2b2d31" alt="Status: Build in Public">
  <img src="https://img.shields.io/badge/Made%20in-EU%20%F0%9F%87%AA%F0%9F%87%BA-003399" alt="Made in EU">
  <img src="https://img.shields.io/badge/Sprache-Deutsch%20%7C%20English-555" alt="Deutsch und Englisch">
</p>

<p align="center">
  <b>Dein persönliches KI-Team – auf deinem Server oder Rechner, mit dem Anbieter deiner Wahl und zuschaltbarer Datenschleuse.</b><br>
  Der Code ist öffentlich. Und du entscheidest mit, was als Nächstes kommt.
</p>

<p align="center">
  <b>Entwickelt von <a href="https://hr-codelabs.de">HR CodeLabs</a></b><br>
  Du willst so etwas für dein Unternehmen? <a href="https://hr-codelabs.de">HR CodeLabs</a> baut Projekte im Auftrag: KI-Integration für Selbstständige und KMU.
</p>

---

## So sieht PaiBot aus

<p align="center">
  <img src="docs/assets/screenshots/chat-beleg.png" alt="PaiBot am Rechner: links die Navigation mit dem Bot Pai und seinen Unterhaltungen, in der Mitte eine Antwort mit dem Entwurf einer Absage, rechts die Arbeitsfläche mit dem Beleg zu dieser Antwort" width="76%">
  <img src="docs/assets/screenshots/chat-handy-beleg.png" alt="PaiBot auf dem Handy: eine Unterhaltung, von unten ist der Beleg zur Antwort als Blatt geöffnet" width="21%">
</p>

<p align="center">
  <sub><b>Vorschau, im Bau:</b> aufgenommen aus der laufenden App mit Beispiel-Daten (Bot „Pai“, erfundene Unterhaltungen, Test-Anbieter). Eine veröffentlichte Version gibt es noch nicht (siehe <a href="#stand">Stand</a>).</sub>
</p>

<p align="center">
  <img src="docs/assets/screenshots/belege-kette-geprueft.png" alt="Die Seite „Belege“: ganze Kette im Browser geprüft, „Vertrauenswürdig“, darunter die Liste der Belege mit Zeit, Kennung, Aktion, Ergebnis und Prüfung" width="49%">
  <img src="docs/assets/screenshots/datenschleuse-letzte-anfrage.png" alt="Die Seite „Datenschleuse“: Zustand „bereit“, die letzte Anfrage ging maskiert an das Modell, und ein Beispiel mit erfundenen Daten" width="49%">
</p>

<p align="center">
  <sub><b>Vorschau, im Bau:</b> Belege prüfen und die Datenschleuse (in der Doku-Umgebung mit einer Attrappe der Datenschleuse aufgenommen). Alle Schritte mit Bildern stehen in der <a href="docs/README.md">Doku</a>.</sub>
</p>

<details>
<summary><b>Weitere Bilder: helles Design und Einrichtung</b></summary>

<p align="center">
  <img src="docs/assets/screenshots/app-hell.png" alt="PaiBot am Rechner im hellen Design mit einer Beispiel-Unterhaltung" width="76%">
  <img src="docs/assets/screenshots/app-handy-hell.png" alt="PaiBot auf dem Handy im hellen Design" width="21%">
</p>

<p align="center">
  <img src="docs/assets/screenshots/einrichtung-code.png" alt="Die Einrichtung von PaiBot: Pai begrüßt dich, rechts das Feld für den Einrichtungs-Code aus dem Log" width="76%">
  <img src="docs/assets/screenshots/einrichtung-code-handy.png" alt="Die Einrichtung auf dem Handy" width="21%">
</p>

</details>

Alle Bilder entstehen per Skript aus der App, nicht von Hand (`pnpm doku:app -- pnpm doku:screenshots`, siehe [Doku](docs/README.md#screenshots)).

## Inhalt

- [So sieht PaiBot aus](#so-sieht-paibot-aus)
- [Was ist PaiBot?](#was-ist-paibot)
- [Warum PaiBot?](#warum-paibot)
- [Funktionen](#funktionen)
- [So funktioniert es](#so-funktioniert-es)
- [Stand](#stand)
- [Bevor du echte Daten einträgst](#bevor-du-echte-daten-einträgst)
- [Roadmap](#roadmap)
- [Schnellstart](#schnellstart)
- [Projektaufbau](#projektaufbau)
- [Lizenz: Fair-Code, für eine Person](#lizenz-fair-code-für-eine-person)
- [FAQ](#faq)
- [Mitmachen und Community](#mitmachen-und-community)
- [Wer steckt dahinter](#wer-steckt-dahinter)

## Was ist PaiBot?

**PaiBot** (Personal AI Bot) ist ein persönlicher KI-Agent für eine Person. Heute chattest du mit deinem Bot, und jede seiner Aktionen läuft durch ein Tor mit festen Regeln und bekommt einen Beleg. Das Ziel ist mehr als ein einzelner Chatbot: ein ganzes Team aus Bots mit eigenen Rollen, die miteinander reden, sich Aufgaben übergeben, selbst im Browser surfen und für dich in deinen Apps arbeiten (geplant, siehe [Roadmap](#roadmap)).

PaiBot läuft **bei dir** auf deinem eigenen Server (mit Docker Compose, auch auf dem eigenen Rechner), verbindet sich mit dem **Anbieter deiner Wahl** (Mistral AI über dessen EU-Endpunkt, EUrouter mit deinen Routing-Regeln oder ein eigener bzw. lokaler Dienst) und zeigt an jeder Antwort, wer laut Anbieter geantwortet hat; dazu eine zuschaltbare **Datenschleuse** ersetzt persönliche Daten durch Platzhalter, bevor sie eine KI erreichen.

<p align="center">
  <img src="docs/assets/idee.jpg" alt="Die Idee: Problem, Lösung, Bauplan" width="90%">
</p>

## Warum PaiBot?

Die neuesten KI-Agenten kommen oft gar nicht oder nur eingeschränkt nach Europa, laufen in fremden Clouds oder bekommen weitreichende Rechte auf deinem System. PaiBot geht einen anderen Weg:

|                  | PaiBot                                                                                                                                                                                                            |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Wo läuft es?** | auf deinem eigenen Server oder lokal auf deinem Rechner                                                                                                                                                           |
| **Welche KI?**   | Mistral AI (EU-Endpunkt laut Mistral), EUrouter mit deinen Routing-Regeln oder ein eigener, OpenAI-kompatibler Anbieter (auch auf dem eigenen Rechner); an jeder Antwort steht, wer laut Anbieter geantwortet hat |
| **Deine Daten**  | zuschaltbare Datenschleuse: Namen, E-Mails, IBANs werden vor dem Modell maskiert und in der Antwort zurückgetauscht                                                                                               |
| **Rechte**       | jede Aktion läuft durch ein Tor mit festen Regeln ohne KI und bekommt einen Beleg; Werkzeuge mit eigenen Rechten je Bot sind geplant                                                                              |
| **Kontrolle**    | Belege zu jeder Aktion, im Browser prüfbar; eine Freigabe vor Aktionen, die etwas nach außen schicken, ist geplant                                                                                                |
| **Transparenz**  | Code öffentlich einsehbar, jede Folge als nachbaubarer Stand                                                                                                                                                      |

## Funktionen

|     | Funktion                                                       | Status                                                                                                                        |
| --- | -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| 🖥️  | Läuft auf eigenem Server (Docker Compose, Coolify)             | vorhanden, siehe [`docs/installation.md`](docs/installation.md); ein veröffentlichtes Image gibt es noch nicht                |
| 💬  | Chat mit deinem Bot, Antwort Stück für Stück, Stopp            | vorhanden ([Chat](docs/funktion-chat.md)); Anhänge, Spracheingabe, Merken und Web-Zugriff geplant                             |
| 🧾  | Tor und Belege: feste Regeln ohne KI, Beleg zu jeder Aktion    | vorhanden ([Belege](docs/funktion-belege.md), [Das Tor](docs/funktion-tor.md))                                                |
| 🛡️  | Datenschleuse für persönliche Daten, zuschaltbar               | vorhanden als zuschaltbarer Dienst, Schalter je Unterhaltung ([Datenschleuse](docs/funktion-datenschleuse.md)); Standard: aus |
| 🤖  | Dein Bot mit Name, Anweisung und Aussehen                      | vorhanden ([Bot](docs/funktion-bot.md)); weitere Bots mit Rollen und Gedächtnis: geplant                                      |
| 🔌  | Apps per MCP verbinden, Freigabe vor jeder schreibenden Aktion | geplant                                                                                                                       |
| 🌐  | Browser-Agent: der Bot surft selbst, du schaust live zu        | geplant                                                                                                                       |
| 🤝  | Bots im Team: Delegieren, Übergeben, Chief of Staff            | geplant                                                                                                                       |
| ⏰  | Routinen, die im Hintergrund laufen                            | geplant                                                                                                                       |
| 📱  | App fürs Handy (PWA) mit Push, Deutsch und Englisch            | Oberfläche fürs Handy und „Als Web-App installieren“ vorhanden; Push und Englisch geplant                                     |
| 💻  | PaiBot lokal auf deinem Rechner mit lokalem Modell             | geplant                                                                                                                       |

## So funktioniert es

```mermaid
flowchart LR
    U["📱 Du – PWA im Browser oder auf dem Handy"] --> W["PaiBot<br/>Next.js + Agenten"]
    W --> DB[("Postgres")]
    W --> J["Hintergrund-Jobs"]
    W -.->|"geplant"| B["Browser-Dienst"]
    W -->|"Schleuse an"| S["🛡️ Datenschleuse<br/>maskiert persönliche Daten"]
    W -.->|"Schleuse aus"| M
    S --> M["🇪🇺 KI-Modelle<br/>EUrouter oder eigener Anbieter"]
```

Mit eingeschalteter Datenschleuse sieht das Modell zum Beispiel nur `<PERSON_0>` statt „Max Mustermann“. Die Antwort enthält trotzdem wieder den echten Namen.

## Stand

> 🚧 **PaiBot ist im Bau.** Die Basisversion lässt sich schon einrichten und benutzen: Einrichtung und Anmeldung, Chat mit deinem Bot, Belege und Regeln, Modell und Anbieter, Datenschleuse, Bot sowie Einstellungen und Info. Eine veröffentlichte Version (Release mit fertigem Image) gibt es noch nicht; installiert wird aus dem Quellcode.
>
> **Die erste Version ist zum Ausprobieren gedacht.** Bevor du ihr echte Daten anvertraust, fehlen noch ein Notfall-Zugang, die erneute Bestätigung heikler Aktionen und ein zweiter Faktor beim Anmelden.

| Was                                                                                                                                                             | Stand                  |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| Server-Grundlage mit Docker Compose und Datenbank ([Installation](docs/installation.md))                                                                        | ✅ fertig und getestet |
| Getrennte Datenbank-Rollen und gehärtetes Docker Compose                                                                                                        | ✅ fertig und getestet |
| [Einrichtung und Anmeldung](docs/funktion-einrichtung-und-zugang.md) mit Schutz vor zu vielen Versuchen                                                         | ✅ fertig und getestet |
| [Chat](docs/funktion-chat.md): Antwort live, Stopp, neu erzeugen, Suche, als Datei sichern, Belege                                                              | ✅ fertig und getestet |
| Das [Tor](docs/funktion-tor.md): jede Aktion läuft durch feste Regeln ohne KI                                                                                   | ✅ fertig und getestet |
| [Belege](docs/funktion-belege.md): Protokoll mit Prüfer im Browser und mit `pnpm belege:pruefen`                                                                | ✅ fertig und getestet |
| [Modell und Anbieter](docs/funktion-anbieter-und-modelle.md) mit Ausgangs-Liste                                                                                 | ✅ fertig und getestet |
| [Bot](docs/funktion-bot.md): Name, Anweisung, Aussehen                                                                                                          | ✅ fertig und getestet |
| [Datenschleuse](docs/funktion-datenschleuse.md) als zuschaltbarer Dienst (Standard: aus)                                                                        | ✅ fertig und getestet |
| [Einstellungen und Info](docs/funktion-einstellungen.md): Passwort, Sitzungen, Grenzen                                                                          | ✅ fertig und getestet |
| Verschlüsselung der gespeicherten Schlüssel ([Sicherheit](docs/sicherheit.md))                                                                                  | ✅ fertig und getestet |
| [Sicherung und Wiederherstellung](docs/sicherung.md): ein Befehl je Richtung, mit Prüfung danach                                                                | ✅ fertig und getestet |
| Doku mit Bildern aus der laufenden App ([Doku](docs/README.md))                                                                                                 | ✅ fertig              |
| Release zum Installieren (fertiges Image)                                                                                                                       | 🔨 im Bau              |
| [Eigener Anbieter](docs/funktion-anbieter-und-modelle.md) in der Oberfläche, auch auf deinem Rechner                                                            | ✅ fertig und getestet |
| [Not-Aus als Schalter](docs/funktion-tor.md#not-aus-alle-bots-anhalten): alle Bots anhalten, mit Passwort fortsetzen                                            | ✅ fertig und getestet |
| [Selbsttest](docs/funktion-selbsttest.md): Ist meine Installation richtig eingestellt?                                                                          | ✅ fertig und getestet |
| [Bekannte Geräte](docs/funktion-einstellungen.md) und Hinweis bei Anmeldung von einem neuen Gerät                                                               | ✅ fertig und getestet |
| [Startbereich](docs/funktion-chat.md#so-benutzt-du-es) einer leeren Unterhaltung in drei Fassungen, wählbar unter [Darstellung](docs/funktion-einstellungen.md) | ✅ fertig und getestet |
| Lebendiger Avatar im Chat: zeigt mit dem Gesicht, ob dein Bot zuhört, nachdenkt, schreibt oder angehalten ist ([Chat](docs/funktion-chat.md))                   | ✅ fertig und getestet |
| „Zugang abriegeln“ (alle Geräte auf einen Schlag sperren)                                                                                                       | 🗓️ geplant             |
| Zweiter Faktor beim Anmelden                                                                                                                                    | 🗓️ geplant             |
| Notfall-Zugang                                                                                                                                                  | 🗓️ geplant             |
| Erneute Bestätigung heikler Aktionen                                                                                                                            | 🗓️ geplant             |
| Apps anbinden per MCP                                                                                                                                           | 🗓️ geplant danach      |
| Bots im Team                                                                                                                                                    | 🗓️ geplant danach      |

- 🛠️ **Was gerade gebaut wird:** jede Aufgabe ist ein Issue, sortiert nach [Meilensteinen](https://github.com/oliverhees/paibot/milestones).
- 📖 **Wie es funktioniert:** die [Doku](docs/README.md) beschreibt jede fertige Funktion Schritt für Schritt mit Bildern.

## Bevor du echte Daten einträgst

Diese Version ist zum Ausprobieren gedacht. Nutze sie mit Beispiel-Daten und einem Anbieter-Schlüssel mit niedrigem Ausgabe-Limit, noch nicht für vertrauliche Unterhaltungen oder wichtige Schlüssel.

- **Anmeldung:** Ein zweiter Faktor, ein Notfall-Zugang ohne Passwort und eine erneute Bestätigung für heikle Einstellungen fehlen noch; sie sind für die nächste Version geplant. Bis dahin schützt dich vor allem ein langes, zufälliges Passwort aus einem Passwort-Manager.
- **Erreichbarkeit:** Betreibe PaiBot nur hinter einem Proxy mit HTTPS (zum Beispiel Coolify) und gib den Port der App nicht direkt frei. Am besten erreichst du PaiBot nur über dein eigenes Netz oder einen Tunnel.
- **Geräte:** Melde dich nur auf deinen eigenen Geräten an. Unter Einstellungen → Zugang siehst du alle Geräte und kannst jedes einzeln entfernen.
- **Sicherungen:** Spiel nur Sicherungen zurück, die du selbst angelegt hast. Sicherungen sind nicht verschlüsselt und enthalten deine Unterhaltungen lesbar ([Sicherung](docs/sicherung.md)).
- **Coolify:** Lass die Geheimnisse (`PAIBOT_SECRET`, die Passwörter der Datenbank, die Schlüssel der Datenschleuse) nicht zur Bauzeit zu; wie du das prüfst, steht in [PaiBot mit Coolify betreiben](docs/deploy-coolify.md#geheimnisse-nicht-im-image-so-prüfst-du-es). Sobald es ein fertiges Image von PaiBot gibt, nimm das statt des Baus auf dem Server.
- **Mehr dazu:** Was PaiBot schützt und was nicht, steht in [Sicherheit](docs/sicherheit.md). Sicherheitslücken bitte nicht öffentlich melden, sondern wie in [SECURITY.md](SECURITY.md) beschrieben.

## Roadmap

Gebaut wird zwischen den Folgen der YouTube-Serie, in Coding-Sessions der Community auf [aiianer.de](https://aiianer.de) und im Livestream. Die Folgen zeigen, wie man PaiBot installiert, benutzt und ausbaut. Jede Folge bekommt einen eigenen Git-Tag (`folge-00`, `folge-01`, …), so kannst du jeden Stand nachbauen. Die Reihenfolge kann sich ändern, und die Community stimmt ab, welche Funktion als Nächstes kommt.

- 🗺️ [Bauplan](https://paibot.de/bauplan): der aktuelle Stand
- 🗳️ [Mitentscheiden](https://paibot.de/mitentscheiden): welche Funktion kommt als Nächstes?
- 📖 [Doku](https://paibot.de/doku): installieren und benutzen

- [x] **Folge 0** – Gerüst, Lizenz, CI
- [ ] **Folge 1** – Die Idee
- [ ] **Folge 2** – Der Server: PaiBot geht online
- [ ] **Folge 3** – Die Datenschleuse
- [ ] PaiBot auf deinem Rechner mit lokaler KI
- [ ] Der erste Bot
- [ ] Apps anbinden per MCP
- [ ] Der Browser-Agent
- [ ] Bots im Team
- [ ] Routinen
- [ ] Die App fürs Handy
- [ ] … und was die Community sich wünscht

## Schnellstart

> PaiBot ist im Bau. Zum Ausprobieren mit Datenbank, Einrichtung und Chat: [Installation mit Docker Compose](docs/installation.md). Der Schnellstart unten ist für die Entwicklung.

**Voraussetzungen:** Node.js 22 und pnpm 10

```bash
git clone https://github.com/oliverhees/paibot.git
cd paibot
pnpm install
pnpm dev          # startet PaiBot auf http://localhost:3000
```

| Befehl                | Zweck                              |
| --------------------- | ---------------------------------- |
| `pnpm dev`            | PaiBot lokal starten               |
| `pnpm build`          | alles bauen                        |
| `pnpm test`           | Tests ausführen                    |
| `pnpm lint`           | Lint und Format prüfen (Biome)     |
| `pnpm typecheck`      | Typen prüfen                       |
| `pnpm licenses:check` | Lizenzen der Abhängigkeiten prüfen |

## Projektaufbau

```
apps/web/          PaiBot-App (Next.js: Oberfläche, API)
packages/shared/   gemeinsame Typen, Texte und Konstanten
packages/db/       Datenbank: Schema, Migrationen, Zugriff
packages/gate/     das Tor: feste Regelprüfung für jede Aktion
packages/receipts/ Beleg-Protokoll: verketten, signieren, prüfen, exportieren
packages/crypto/   Verschlüsselung, Passwörter, Tokens, Signaturen
packages/llm/      Anbieter und Modelle, Ausgangs-Liste, Anbindung der Datenschleuse
packages/agents/   KI-Laufzeit (Motor) für die Bots
packages/jobs/     Warteschlange für Läufe im Hintergrund
packages/ui/       Design und Bausteine der Oberfläche
packages/mcp/      App-Anbindungen per MCP (geplant)
services/browser/  Browser-Dienst (Python)
deploy/            Docker Compose und Coolify
docs/              Dokumentation
```

## Lizenz: Fair-Code, für eine Person

PaiBot ist **Fair-Code** („Source Available“), nicht Open Source. Es gilt die PaiBot Fair-Code-Lizenz, Version 1.1. Kurz gesagt:

**Du darfst**

- PaiBot für dich herunterladen, installieren und nutzen: privat **und für deine eigene Arbeit**, auch als Selbstständiger oder Freiberufler
- als Angestellter für deine eigenen Aufgaben nutzen, solange nicht dein Arbeitgeber PaiBot bereitstellt oder vorgibt
- den Code für dich anpassen und erweitern
- ihn kostenlos weitergeben, z. B. als Fork, solange die Lizenz dabei bleibt, der Fork kostenlos bleibt, einen eigenen Namen trägt und „Powered by PaiBot“ mit Verweis auf [paibot.de](https://paibot.de) zeigt
- Kurse, Bücher, Videos und Beratung dazu machen, die zeigen, wie man PaiBot selbst nutzt

**Du darfst nicht**

- PaiBot mit mehreren Personen nutzen – nicht im Team, nicht in einer Firma, auch nicht intern
- PaiBot oder eine angepasste Fassung verkaufen oder vermieten
- ihn als gehosteten Dienst für andere anbieten oder gegen Entgelt für andere einrichten, betreiben oder supporten
- eine angepasste Fassung unter dem Namen „PaiBot“ oder ohne Herkunftshinweis als eigenes Produkt ausgeben
- Lizenz- und Markenhinweise oder „Powered by PaiBot“ entfernen

> **PaiBot ist für eine Person: für dich und deine eigene Arbeit.** Sobald mehrere Personen damit arbeiten sollen, im Team oder im Unternehmen, brauchst du **PaiBot Enterprise** mit Support (in Vorbereitung). Mehr dazu: [paibot.de/enterprise](https://paibot.de/enterprise).

Rechtlich gilt nur der Text in [`LICENSE`](LICENSE). Wer einen Beitrag einreichen will, findet die [Beitragsvereinbarung](docs/BEITRAGSVEREINBARUNG.md). Bausteine Dritter behalten ihre eigenen Lizenzen, siehe [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

## FAQ

<details>
<summary><b>Ist PaiBot Open Source?</b></summary>

Nein. Der Code ist öffentlich einsehbar und für eine Person kostenlos („Fair-Code“), aber die Nutzung mit mehreren Personen, Verkauf sowie bezahlter Betrieb oder Support für andere sind nicht erlaubt.
</details>

<details>
<summary><b>Darf ich PaiBot für meine Arbeit nutzen?</b></summary>

Ja, wenn du es allein nutzt: als Selbstständiger, als Freiberufler oder für deine eigenen Aufgaben. Nicht erlaubt ist, dass mehrere Personen damit arbeiten oder dass eine Firma PaiBot für ihre Mitarbeiter bereitstellt. Dafür ist PaiBot Enterprise mit Support gedacht (in Vorbereitung): [paibot.de/enterprise](https://paibot.de/enterprise).
</details>

<details>
<summary><b>Was unterscheidet PaiBot?</b></summary>

PaiBot setzt diese Schwerpunkte: Anbieter mit Sitz oder Endpunkt in Europa zur Auswahl und eine ehrliche Angabe, wer eine Antwort geliefert hat (nur, was der Anbieter selbst meldet), eine Datenschleuse, die persönliche Daten vor dem Modell maskiert, ein Tor mit festen Regeln und ein Beleg für jede Aktion, und jeder Schritt wird auf Deutsch erklärt, damit du verstehst, was dein Agent tut. Geplant sind lokale Modelle in der Oberfläche und eine eigene Anbindung von Apps per MCP.
</details>

<details>
<summary><b>Brauche ich einen eigenen Server?</b></summary>

Heute läuft PaiBot mit Docker Compose auf einem Server (z. B. mit Coolify) oder auf deinem eigenen Rechner. Ein Modell auf deinem eigenen Rechner anzubinden, kann PaiBot technisch schon; die Oberfläche dafür ist geplant.
</details>

<details>
<summary><b>Ist PaiBot damit DSGVO-konform?</b></summary>

PaiBot und die Datenschleuse sind technische Schutzmaßnahmen, keine Rechtsberatung und keine Garantie. Für die rechtliche Bewertung deines Einsatzes bist du selbst verantwortlich.
</details>

<details>
<summary><b>Wie oft kommen neue Folgen?</b></summary>

Regelmäßig, mehrmals pro Woche. Abonniere den Kanal und gib dem Repo einen Stern ⭐, dann siehst du sofort, wenn es weitergeht.
</details>

## Mitmachen und Community

- ⭐ **Gib dem Repo einen Stern**, wenn dir das Projekt gefällt – das hilft enorm.
- 🗳️ **Entscheide mit:** auf [paibot.de/mitentscheiden](https://paibot.de/mitentscheiden) stimmst du ab, was als Nächstes kommt. Den Stand siehst du im [Bauplan](https://paibot.de/bauplan), die Anleitungen in der [Doku](https://paibot.de/doku).
- 💬 **Community auf [aiianer.de](https://aiianer.de):** Deep Dives zu jeder Folge, gemeinsame Coding-Sessions zum Mitbauen und Hilfe, wenn es hakt.
- 🐛 **Fehler oder Ideen?** Eröffne ein [Issue](https://github.com/oliverhees/paibot/issues/new/choose).
- 🛠️ **Selbst beitragen?** Lies zuerst [`CONTRIBUTING.md`](CONTRIBUTING.md) (Beitragsvereinbarung nötig).
- 🔒 **Sicherheitslücke gefunden?** Bitte nicht öffentlich melden, sondern wie in [`SECURITY.md`](SECURITY.md) beschrieben.

## Wer steckt dahinter

PaiBot wird von [HR CodeLabs](https://hr-codelabs.de) entwickelt. Die Agentur bietet KI-Integration für Selbstständige und KMU und setzt Projekte im Auftrag um.

PaiBot selbst ist für eine Person gedacht. Für Teams gibt es [PaiBot Enterprise](https://paibot.de/enterprise) (in Vorbereitung). Für ein eigenes Projekt: [Projekt anfragen](https://hr-codelabs.de).

---

<p align="center">
  Gebaut in Deutschland von <a href="https://github.com/oliverhees">Oliver Hees</a> · „PaiBot“, Logo und Maskottchen sind Kennzeichen von Oliver Hees.<br>
  Entwickelt von <a href="https://hr-codelabs.de">HR CodeLabs</a> · Projekte im Auftrag: <a href="https://hr-codelabs.de">hr-codelabs.de</a><br>
  Für Teams und Firmen: <a href="https://paibot.de/enterprise">PaiBot Enterprise</a> · Community: <a href="https://aiianer.de">aiianer.de</a>
</p>
