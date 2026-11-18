# reflexion-skill

Ein Claude-Skill für die Nachbesprechung nach jeder Aufgabe. Du tippst `/reflexion`, und der Agent schaut auf die Sitzung zurück, die gerade zu Ende ging: Was war geplant, was ist passiert, warum gab es eine Lücke, und was ändert sich beim nächsten Mal. Daraus entstehen Lektionen, die so konkret sind, dass die nächste Sitzung sie befolgen kann. Wo eine Lektion allein nicht reicht, schlägt der Agent eine Änderung an `CLAUDE.md`, `AGENTS.md`, einer Cursor-Regel oder einer `SKILL.md` vor und setzt sie nach deinem Ja um.

Jede Lektion landet in `LESSONS.md`. Bevor eine neue dazukommt, prüft das Werkzeug, ob es dieselbe Lektion in anderen Worten schon gibt.

## Die Methode

Das After Action Review stammt aus der Nachbesprechung militärischer Übungen und wird seit Jahrzehnten so gehalten: Plan und Ergebnis vergleichen, den Grund für die Lücke finden, niemanden beschuldigen. Dieselbe Idee hat in der KI-Forschung einen Namen: [Reflexion](https://arxiv.org/abs/2303.11366) (Shinn et al., 2023). Agenten, die nach einem Fehlversuch festhalten, was schiefging, und diese Notiz beim nächsten Versuch mitnehmen, sind besser als Agenten ohne Gedächtnis.

Die vier Fragen:

1. Was war geplant?
2. Was ist tatsächlich passiert?
3. Warum weicht das eine vom anderen ab?
4. Was behalten wir bei, und was machen wir anders?

## Installation

Füg das in Claude ein:

```
https://github.com/Ultra-Smashed/reflexion-skill

installiere den Skill
```

Oder als Plugin in Claude Code:

```
/plugin marketplace add Ultra-Smashed/reflexion-skill
/plugin install reflexion-skill@reflexion-skill
```

Oder den Ordner direkt kopieren, dann heißt der Befehl kurz `/reflexion`:

```bash
git clone https://github.com/Ultra-Smashed/reflexion-skill.git
cp -r reflexion-skill/skills/reflexion ~/.claude/skills/
```

Als Plugin heißt der Befehl `/reflexion-skill:reflexion`. Das Werkzeug braucht Python 3.8 oder neuer und keine Pakete.

## Benutzung

Nach einer Aufgabe:

```
/reflexion
```

oder in normalen Worten: „Lass uns eine Nachbesprechung machen“, „Was haben wir gelernt?“. Sollen vorgeschlagene Änderungen ohne Rückfrage umgesetzt werden, sag es gleich mit: „/reflexion anwenden“ oder „Reflexion, und wende den Fix an“.

So sieht eine Antwort aus:

```
REFLEXION · Release 1.4 taggen

1. Was war geplant?
   Version hochzählen, Changelog schreiben, Tag v1.4.0 setzen und pushen.

2. Was ist tatsächlich passiert?
   Tag und Push liefen durch, aber der Tag zeigte auf den Commit vor dem
   Changelog. Der Nutzer hat es im Release auf GitHub bemerkt.

3. Warum weicht das eine vom anderen ab?
   Der Changelog lag noch ungesichert im Arbeitsverzeichnis. git tag nimmt
   den letzten Commit, nicht den Stand der Dateien.

4. Was behalten wir bei, und was machen wir anders?
   Vor jedem Tag git status prüfen und bei ungesicherten Änderungen abbrechen.
   Beibehalten: Version und Changelog im selben Commit.

LEKTIONEN
- Vor git tag immer git status prüfen; bei ungesicherten Änderungen erst
  committen, dann taggen. (angewendet)

FIX-PLAN
1. Ziel: skills/release/SKILL.md, nach Schritt 4
   Änderung: „Vor dem Tag git status ausführen. Sind Dateien geändert,
   abbrechen und zuerst committen.“ (angewendet)

Logbuch: ./LESSONS.md
```

## Das Werkzeug

```bash
cd skills/reflexion
python3 lessons.py aehnlich "Vor git tag immer git status prüfen"   # Dubletten suchen
python3 lessons.py hinzufuegen --lektion "..." --geplant "..." --passiert "..." \
  --ursache "..." --fix "..." --status angewendet --tags "git,release"
python3 lessons.py liste                     # alle Lektionen
python3 lessons.py liste --tag git           # nach Tag
python3 lessons.py liste --status offen      # vorgeschlagene, nie umgesetzte Fixes
```

Mit `--global` schreibt und liest das Werkzeug `~/.claude/LESSONS.md` statt der Datei im Projekt.

**Dublettenprüfung.** Das Werkzeug vergleicht die Kernwörter einer neuen Lektion mit allen vorhandenen. Füllwörter fallen weg, Wortendungen werden gekürzt, und zusammengesetzte Wörter wie „Batch-Upload“ zählen auch in ihren Teilen. Ab 40 Prozent Ähnlichkeit zeigt es die Treffer, ab 70 Prozent schreibt es nicht und verlangt, die vorhandene Lektion zu ergänzen. Mit `--trotzdem` wird dennoch geschrieben.

**Status.** Jede Lektion ist `notiert` (nur Wissen), `vorgeschlagen` (Fix-Plan steht, noch nicht freigegeben) oder `angewendet`. So sieht man später, welche Ursachen behoben sind und welche nur aufgeschrieben.

## Damit es wirkt

Drei Dinge müssen zusammenkommen. Die Lektion nennt eine Datei, einen Befehl, eine Zahl oder eine Bedingung. Der Fix nennt eine Zieldatei und den wörtlichen Text. Und die nächste Sitzung liest das Ergebnis: Dafür steht in `CLAUDE.md` oder `AGENTS.md` die Zeile „Lies LESSONS.md, bevor du mit einer Aufgabe beginnst.“ Fehlt sie, schlägt der Skill sie beim ersten Lauf vor.

Der Skill trainiert kein Modell. Er schreibt Text in Dateien, die der Agent beim nächsten Start liest. Die Wirkung beginnt mit der nächsten Sitzung, nicht in der laufenden.

## Lizenz

MIT, siehe [LICENSE](LICENSE). Von [Christopher Thanisch](https://thanisch.co).
