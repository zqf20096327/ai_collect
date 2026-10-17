# 🇮🇹 Claude Code Spinner Verbs — Sicilian Edition 🌋

> *Mizzica chi travagghiu!* — Un set di **spinner verbs** in siciliano (per essere precisi Catanese) per Claude Code.

Trasforma i soliti `Thinking...`, `Working...`, `Pondering...` del terminale in qualcosa che sa di Etna, mandorle tostate e granita con brioche. Invece di vedere `Cerebrating...` mentre il tuo agente compila, ti godi un bel `Scattiannu...` o `Sbumicannu...`.

Questo repo contiene oltre **140 verbi e frasi siciliane** pronti all'uso, in un preset:

- **`spinner-verbs.json`** — il set completo (sostituisce tutti i default)
- **`examples/spinner-verbs-append.json`** — solo verbi puri, da mescolare ai default
- **`examples/spinner-verbs-espressivi.json`** — solo frasi folkloristiche teatrali

---

## 📋 Prerequisiti

- [Claude Code](https://claude.com/claude-code) versione **2.1.23 o successiva**
- Un minimo di sangue siciliano nelle vene (opzionale ma consigliato 🍋)

---

## 🚀 Installazione

Hai tre strade, dalla più semplice alla più pulita.

### Opzione A — Incollare direttamente in `settings.json` (quick & dirty)

Apri `~/.claude/settings.json` e incolla il contenuto di [`spinner-verbs.json`](./spinner-verbs.json) al livello top, scegliendo inoltre se fare `replace` o `append` dei verbi grazie alla chiave `mode`:

```json
{
  "spinnerVerbs": {
    "mode": "replace",
    "verbs": [
      "Addumannannu",
      "Scattiannu",
      "Sbumicannu",
      "..."
    ]
  }
}
```

Riavvia Claude Code. Fatto!

### Opzione B — File separato con flag `--settings` (consigliato)

Se vuoi tenere `settings.json` pulito e i verbs in un file dedicato:

1. Copia `spinner-verbs.json` in `~/.claude/spinner-verbs.json`:
   ```bash
   cp spinner-verbs.json ~/.claude/spinner-verbs.json
   ```

2. Aggiungi un alias nella tua shell (`~/.zshrc`, `~/.bashrc`, etc.):
   ```bash
   alias claude='claude --settings ~/.claude/spinner-verbs.json'
   ```

3. Ricarica la shell e lancia `claude`. I verbs siciliani si mescolano al resto della tua config.

### Opzione C — Via `settings.local.json` (per progetto singolo)

Se vuoi il dialetto solo su un progetto specifico:

```bash
cp spinner-verbs.json <progetto>/.claude/settings.local.json
```

Claude Code farà automaticamente merge con le altre config. `settings.local.json` è ignorato da git di default.

---

## Il preset

### `spinner-verbs.json` — Set completo (140+ voci)

Il cuore del progetto. Mix di verbi autentici e frasi idiomatiche, con `"mode": "replace"` per darti immersione totale in siciliano.

Esempi che vedrai scorrere:

```
Scattiannu...
Curennu curennu...
Sbumicannu...
Mizzica chi travagghiu...
Acchianannu l'Etna...
Sciugghiennu sta rugna...
```

---

## 📖 Glossario essenziale

Per chi non mastica siciliano, ecco il significato di alcuni dei verbi più ricorrenti:

| Verbo | Traduzione | Quando lo vedi |
|---|---|---|
| **Addumannannu** | Chiedendo, interrogando | Claude sta formulando una query |
| **Scattiannu** | Scoppiando, scattando | Elaborazione intensa |
| **Curennu curennu** | Correndo correndo (di fretta) | Task veloce |
| **Sbumicannu** | Strabordando, ribollendo | Molto output in arrivo |
| **Travagghiannu** | Lavorando | Claude sta lavorando (che sorpresa) |
| **Ragiunannu** | Ragionando | Reasoning pass |
| **Taliannu** | Guardando, osservando | Sta leggendo file/output |
| **Ciccannu** | Cercando | Search / grep |
| **Annacannu** | Cullando, dondolando | Loop pigro, attesa |
| **Cafuddannu** | Colpendo forte, pestando | Compilazione pesante |
| **Caminannu** | Muovendo, smuovendo | Refactor |
| **Cumminannu** | Combinando (anche "combinando guai") | Task complesso |
| **Incignannu** | Iniziando, inaugurando | Avvio nuova operazione |
| **Macinannu** | Macinando | Elaborazione dati |
| **Manijannu** | Maneggiando | Manipolazione file |
| **Mischiannu** | Mischiando | Merge, diff |
| **Pigghiannu** | Prendendo, afferrando | Fetch / read |
| **Pruvannu** | Provando | Test in esecuzione |
| **Sbummicannu** | Traboccando (variante di sbumicannu) | Output abbondante |
| **Sciddicannu** | Scivolando | Transizione veloce |
| **Scummigghiannu** | Scoprendo, svelando | Debug / inspect |
| **Sturiannu** | Studiando | Analisi codice |
| **Tastiannu** | Assaggiando, tastando | Dry run |
| **Truvannu** | Trovando | Match trovato |
| **Tuppuliannu** | Bussando | API call, richiesta |
| **Zappuliannu** | Zappettando | Lavoro di fino |

E poi le frasi idiomatiche — si commentano da sole:

- **Mizzica chi travagghiu** — "Caspita che lavoro"
- **Minchia chi camurria** — (tradurre rovinerebbe la poesia)
- **Bedda matri chi buddellu** — "Madre mia questa cosa"
- **Chi camurria stu bug** — "Che seccatura questo bug"
- **Cca ci vole bellu cafè** — "Qui ci vuole il caffè"
- **Acchianannu l'Etna** — "Salendo l'Etna"
- **Sciugghiennu stu ruppu** — "Sciogliendo questa matassa/rogna"

---

## 🛠️ Modificare i verbs

Vuoi aggiungere i tuoi? Apri il file JSON, aggiungi stringhe all'array `verbs`, salva, riavvia Claude Code.

Regole pratiche:

1. **Usa il gerundio** (forma `-ando / -endo` in italiano, `-annu / -ennu` in siciliano). Lo spinner funziona grammaticalmente se il verbo è un gerundio.
2. **Tienili corti** — il terminale è stretto. Sopra le 4-5 parole iniziano a sembrare scomodi.
3. **Pesca dalla tua vita** — è questo il bello!
4. **`mode: "replace"`** sostituisce completamente i default. **`mode: "append"`** li aggiunge.

---

## 🐛 Troubleshooting

**Non vedo i verbs nuovi.**
- Assicurati di avere Claude Code ≥ 2.1.23: `claude --version`
- Verifica la sintassi JSON: `cat ~/.claude/settings.json | jq .`
- Riavvia Claude Code (non basta ricaricare la shell).

**Vedo sia i miei verbs che i default.**
- Stai usando `"mode": "append"`. Cambia in `"replace"` se vuoi solo i tuoi.

**Il flag `--settings` non viene applicato.**
- Controlla il path assoluto nell'alias. `~` potrebbe non espandersi in alcuni contesti: usa `$HOME` o il path completo.

**Vedo caratteri strani al posto di `ï` o accenti.**
- Il tuo terminale non è in UTF-8. Su Linux: `export LANG=it_IT.UTF-8`. Su macOS dovrebbe andare di default.

---

## 📚 Riferimenti

- [Claude Code — documentazione ufficiale](https://docs.claude.com/en/docs/claude-code/overview)
- [Issue GitHub che traccia la feature `spinnerVerbs`](https://github.com/anthropics/claude-code/issues/21599) (al momento ancora non documentata ufficialmente)
- [Articolo originale di Daniel Miessler che ha lanciato la moda dei custom spinner verbs](https://danielmiessler.com/blog/customized-spinner-verbs-in-claude-code)

---

## 🤝 Contribuire

Pull request benvenute! Se conosci verbi siciliani che mancano, soprattutto della tua zona (Palermo, Messina, Siracusa, Ragusa, Trapani, Agrigento, Enna, Caltanissetta hanno tutte varianti), aprile una PR. Accetto anche contributi in varianti regionali — catanese, palermitano, ennese, ecc.

Linee guida:

- Un verbo/frase per riga nell'array
- Rispetta l'ordine alfabetico in `spinner-verbs.json` per i verbi puri (le frasi stanno in coda)
- Se un termine è molto locale, aggiungilo al glossario nel README con una nota tipo *(zona Catania)*
- No parolacce troppo pesanti — qualche `minchia` ci sta, è folklore, ma tenetevi nel bon ton

---

## 📜 Licenza

MIT. Fai quello che vuoi, basta che non togli il nome di chi ha contribuito.

---

## 🌋 Crediti

Creato a Catania, sotto l'Etna, da chi pensa che il terminale debba avere un'anima e mangiare granite!
