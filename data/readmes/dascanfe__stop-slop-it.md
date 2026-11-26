# stop-slop-it

**La skill che toglie l'odore di AI dai testi in italiano.**

Versione italiana di [stop-slop](https://github.com/hardikpandya/stop-slop). Funziona con Claude e con gli altri assistenti compatibili con lo standard [Agent Skills](https://agentskills.io), come Cursor, GitHub Copilot e ChatGPT.

[![Licenza: MIT](https://img.shields.io/badge/licenza-MIT-green.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatibile-blue.svg)](https://agentskills.io)

---

## Cos'è lo slop

"In un mondo in continua evoluzione, il design non è solo estetica: è strategia."

La riconosci al primo sguardo: una frase corretta che non dice niente. In inglese questo tipo di testo si chiama *slop*. Lo producono i modelli linguistici quando scrivono senza indicazioni, e lo producono anche le persone che hanno letto troppi testi scritti così.

Questa skill insegna all'assistente a riconoscerlo e a toglierlo.

## Perché una versione italiana

stop-slop è scritta per l'inglese, e molte regole non si traducono parola per parola. Gli avverbi inglesi finiscono in "-ly", quelli italiani in "-mente". L'inglese apre con "Here's the thing", l'italiano con "Ecco il punto" e "Diciamocelo".

E l'italiano ha tic che l'inglese non ha:

- **il "si" impersonale**, che nasconde chi agisce: "si è deciso di";
- **la nominalizzazione**, che trasforma un verbo in una pratica burocratica: "effettuare una verifica" invece di "verificare";
- **i calchi dall'inglese**: "impattare su", "fare la differenza", "mettere a terra".

stop-slop-it parte dalle regole originali e le riscrive per chi scrive in italiano.

Le regole di stop-slop, il punteggio, la tabella dei tic italiani e quando conviene lasciare la skill da parte sono raccontati per esteso nell'articolo [Stop Slop: la skill di Claude che toglie ai testi l'odore di AI](https://www.dascanfe.com/it/blog/stop-slop-claude-skill.html).

## Prima e dopo

| Prima | Dopo |
|-------|------|
| Ops! Sembra che qualcosa sia andato storto. Ma non preoccuparti: siamo qui per aiutarti! | Non siamo riusciti a salvare la nota. Riprova tra un minuto. |
| Si è deciso di procedere all'implementazione della nuova procedura, che andrà a impattare positivamente sull'operatività di tutti i reparti. | Da lunedì gli ordini si registrano nel gestionale e non più sul foglio condiviso. |
| Non sono semplicemente un designer. Sono un problem solver appassionato che trasforma le idee in esperienze memorabili. | Progetto app per la logistica da sei anni. L'ultima ha dimezzato gli errori di consegna. |

Altri esempi in [references/esempi.md](references/esempi.md).

## Cosa controlla

Nove regole, in breve:

1. Togli le frasi di riempimento e gli avverbi che non cambiano il significato.
2. Rompi le strutture a formula, come "non è X, è Y".
3. Dai un soggetto alle frasi: niente passivi e "si" impersonali che nascondono chi agisce.
4. Usa i verbi, non i nomi: "verificare", non "effettuare una verifica".
5. Sii specifico: niente affermazioni vaghe ed estremi pigri.
6. Parla a chi legge, con esempi concreti.
7. Varia il ritmo, e niente trattini lunghi.
8. Fidati di chi legge: niente giri di parole per ammorbidire.
9. Taglia le frasi da citazione.

Ogni testo riceve anche un punteggio da 1 a 10 su cinque dimensioni (direzione, ritmo, fiducia, autenticità, densità). Sotto 35 su 50, va riscritto.

## Installazione

### Con un comando

Funziona con Claude Code, Cursor, GitHub Copilot, Codex, Gemini CLI e gli altri assistenti compatibili con Agent Skills:

```bash
npx skills add dascanfe/stop-slop-it
```

Serve Node.js. Il comando chiede in quali assistenti installarla e se tenerla in un solo progetto o renderla disponibile ovunque (globale).

### Claude Code, senza Node.js

Clona il repository tra le tue skill personali:

```bash
git clone https://github.com/dascanfe/stop-slop-it.git ~/.claude/skills/stop-slop-it
```

Per usarla in un solo progetto e condividerla con il team, clonala in `.claude/skills/stop-slop-it` dentro il progetto.

### Claude.ai e app desktop

1. Scarica `stop-slop-it.zip` dall'[ultima release](https://github.com/dascanfe/stop-slop-it/releases/latest).
2. In Claude vai su **Customize, Skills**, premi "+", poi "Create skill" e "Upload a skill".
3. Carica il file ZIP.

Serve l'esecuzione del codice attiva nelle impostazioni. Sui piani Enterprise le skill devono essere abilitate da un amministratore.

### Altri assistenti

Se il tuo assistente non compare nell'elenco del comando, segui la sua documentazione per importare la cartella. In alternativa, copia le regole di [SKILL.md](SKILL.md) nelle istruzioni personalizzate di qualunque assistente.

## Come si usa

La skill si attiva da sola quando chiedi di scrivere, correggere o rivedere un testo in italiano. Puoi anche richiamarla esplicitamente:

> Rivedi questo testo con stop-slop-it e dammi il punteggio.

In Claude Code puoi usare `/stop-slop-it`.

## Struttura

```
stop-slop-it/
├── SKILL.md              le regole principali, i controlli rapidi, il punteggio
└── references/
    ├── frasi.md          le espressioni da togliere, divise per famiglia
    ├── strutture.md      gli schemi di frase da evitare, con l'alternativa
    └── esempi.md         sei esempi prima e dopo
```

I file in `references/` vengono letti solo quando servono, quindi la skill resta leggera.

## Quando non usarla

- Sul tono voluto di un marchio: se un prodotto usa esclamazioni o ripetizioni per scelta, la skill le segnala invece di toglierle.
- Sui testi legali e sulle istruzioni di sicurezza, dove la forma impersonale serve a essere precisi.
- Come pilota automatico: le regole sono un controllo, la decisione resta a chi scrive.

## Contribuire

Hai trovato un tic che manca, un esempio migliore o una regola che non funziona in italiano? Apri una [issue](https://github.com/dascanfe/stop-slop-it/issues) o una pull request.

Tre regole per i contributi:

- gli esempi devono essere inventati, mai testi o dati di persone reali;
- ogni frase da togliere va accompagnata da cosa scrivere al suo posto, dove serve;
- niente trattini lunghi, nemmeno nei file di questo repository.

## Crediti

Basata su [stop-slop](https://github.com/hardikpandya/stop-slop) di Hardik Pandya, pubblicata con licenza MIT. Le regole originali, il sistema di punteggio e la struttura dei file vengono da lì; l'adattamento all'italiano, le regole su impersonale, nominalizzazione e calchi, le liste di espressioni e gli esempi sono nuovi.

## Licenza

[MIT](LICENSE)

---

## English

**stop-slop-it** is the Italian version of [stop-slop](https://github.com/hardikpandya/stop-slop), a skill that removes AI writing patterns from prose. The original rules target English; this version rewrites them for Italian and adds patterns specific to the language, such as the impersonal "si", nominalization ("effettuare una verifica" instead of "verificare") and English calques. It works with Claude and with any assistant that supports the [Agent Skills](https://agentskills.io) standard. MIT licensed.

Install it with `npx skills add dascanfe/stop-slop-it`.

More on the rules, the scoring and how to adapt the skill to other languages: [Stop Slop: the Claude skill that removes AI writing tells](https://www.dascanfe.com/blog/stop-slop-claude-skill.html).
