# Local Coach

**A personal coach-psychologist-mentor with a body double mode that learns from your Obsidian notes (or any Markdown).** It runs entirely on your own machine through [Ollama]. Nothing is sent to the cloud.

> 🌍 English is the default language of the interface, the prompts and the generated memory; Russian is available too (`LOCAL_COACH_LANG=ru`). Pick one language per working folder. The English translation was produced with a language model and has not been reviewed by a native speaker; corrections are welcome. The full guide is in Russian: [README.ru.md](README.ru.md).

## What it does

- **It reads your vault and remembers you.** Notes are split by headings. A local model extracts facts with a verbatim quote for each one, and the code checks every quote against the note. Facts that say the same thing are merged, so you can tell what is stable and what was mentioned only once.
- **It separates past from present.** Notes cover years, and without checks a profile describes who you were ten years ago as who you are now. Every statement is marked *current*, *past*, *event* or *unverified*. These marks come from:
  - your own answers (`calibrate`);
  - a timeline built from an imported biography spreadsheet and diary notes organised by year;
  - simple rules.
- **It builds a profile.** The model writes a review of each area of life and then a reference profile. An audit checks every point of the profile against the quotes. A plain version without sources is written for reading.
- **It talks with you.** The chat uses hybrid retrieval: vectors plus full-text search, merged with RRF. It also keeps session summaries and the agreements you made, and checks in on those agreements later. Things you say can be saved to memory after you review them.
- **It shows your life by year, exactly.** `bio 1988-2026` (or `/bio` in chat, or just "show everything from the database by year") prints a timeline straight from the database, without the model, so nothing is invented. The rows of an imported biography table are the backbone: one row is one event with its period. Notes and conversations add only events and decisions. Notes in project and idea folders (`Projects`, `Ideas`, also with a suffix like `Projects 2024`) are left out of the timeline and of the check of what is still true today, because years there are usually plans and specs, not life events; the coach still knows them in conversation. Anything the biography already covers is left out too. A number is not taken for a year when it has a unit or sits in a range (`2000 rpm`, `1500–2000`, `2000s`). The output ends with how many facts were hidden and why; `--all` prints everything as stored.
- **Body double.** Say «побудь рядом» or type `/focus <task>`. The coach then sends a short line every minute or two, unprompted, and reports the elapsed time. It stays quiet while you type. Optionally tie the session to a Life Reset item and a time plan: `/focus LR-12 on 50 minutes draft`; focus time per active direction then shows up in `reset`.
- **Life Reset.** A program for sorting out what has piled up in your notes. `inventory build` collects goals, projects, ideas and open loops into a registry; `triage` walks through it and records one decision per item (active, incubating, someday, waiting, done, let go) with a reason; `audit` is a short check of twelve areas of life; `hypotheses` shows careful guesses about recurring patterns, always with quotes and other possible explanations, and only you decide what is confirmed. `reset` shows where you are and what to do next. Results go to a `Life Reset/` folder in the vault (sensitive items by number only). Nothing is archived without your answer. The web interface has the same review as a window (one item per screen, items with the same title merged automatically, the area of an item changeable from a dropdown).
- **Web interface.** `python3 coach.py serve` opens the same coach in a browser, with a cat that thinks, talks and dozes next to you in body double mode. Set `LOCAL_COACH_WEB_PIN` to expose it beyond localhost (`--host 0.0.0.0`): it is a temporary PIN, and the page asks you to choose your own on first login (stored hashed). Without a PIN it listens on localhost only. Chat, `/think`, body double, `/bio`, `/sources`, `/new` work there; the commands that ask line by line (`/review`, `/calibrate`, `/people`, `/import`…) stay in the terminal. Meant to run as a service (systemd, `Restart=always`).
  - **Background sounds** for focus: a mixer in the browser with noise (white, pink, brown), waterfall, stream, leaves, wind, rain, rain on puddles and a cat's purr. Layers have their own switches and volumes and can be mixed. Noise and most layers are synthesised in the page. To use real recordings instead, put `<layer>.wav` (or `.mp3`, `.ogg`) into `localcoach/web/audio/` (layer names: `stream`, `leaves`, `puddles`, and so on). The repository ships no recordings, so you can pick ones whose licence suits you.
  - **Petting.** Buttons to stroke the cat, scratch behind the ear and hug it. The cat reacts and purrs or meows (sounds can be switched off). This changes nothing in the coach itself.
- **Also:**
  - people mentioned in your notes;
  - quick check-ins;
  - a small evaluation loop (`eval`) that tracks quality across versions;
  - import of `.xlsx`, `.csv`, `.docx`, `.txt` and `.md` files without changing your vault.

## Privacy by design

- **Your notes are only read, never changed.** A note that looks like a password store, or that contains a token, key or card number, is never sent to the model.
- **Requests go only to the Ollama address you configure, and it must be local:** localhost, a private LAN or Tailscale. Cloud Ollama models (`…:cloud`) are refused.
- **There is no telemetry.** There are no third-party APIs and no dependencies beyond the Python standard library.

## Requirements

- **Python** 3.10 or newer. `numpy` is optional and only speeds up vector operations.
- **Ollama** with two models:
  - [`qwen3.5:9b`] for chat and analysis;
  - [`embeddinggemma`] for vectors.
- **Other models.** The coach talks to Ollama only and needs structured JSON output from the model (Ollama's `format` parameter, which any recent model supports). Any chat model that Ollama serves should work: set `LOCAL_COACH_MODEL` (chat and quick calls), `LOCAL_COACH_HEAVY_MODEL` (extraction, registry, hypotheses; optional) and `LOCAL_COACH_EMBED_MODEL` (vectors). It has been tested only with Qwen 3.5 (9B and 27B) and `embeddinggemma`; other models are untested. Small models invent more, but every fact still needs a verbatim quote that the code checks. Changing the embedding model rebuilds all vectors, and the similarity thresholds were tuned on `embeddinggemma`. Not supported: OpenAI-compatible servers and cloud APIs. This is by design: your notes never leave your network.
- **A GPU with 8 GB of VRAM or more** (GTX 1070/1080, RTX 2060 Super, 3060 Ti, 4060 and up). Together the two models take about 7 GB: 6.3 GB for `qwen3.5:9b-q4_K_M` at the default 16k context, plus 0.65 GB for `embeddinggemma`. A 6 GB card won't hold the whole model, so part of it runs on the CPU, which is noticeably slower. 12 GB leaves room for a 32k context. To check, run `ollama ps` while the model is loaded: it should say `100% GPU`.
- Without a GPU the coach still works, but slowly. The first pass over a vault of a few hundred notes takes hours even on a GPU. After that, only new and changed notes are processed.

## Quick start

```bash
ollama pull qwen3.5:9b-q4_K_M
ollama pull embeddinggemma

git clone https://github.com/Jutqe/local-coach.git && cd local-coach
python3 coach.py --vault ~/Obsidian/MyVault plan      # how much work, no model calls
python3 coach.py --vault ~/Obsidian/MyVault update    # build the memory (can be interrupted and resumed)
python3 coach.py import ~/biography.xlsx              # optional: a timeline of your life
python3 coach.py bio                                  # your timeline by year, no model calls
python3 coach.py calibrate                            # answer what is still true today
python3 coach.py chat
```

Instead of `--vault` you can set `LOCAL_COACH_VAULT` once (the Russian guide does this). All data goes to `~/.local-coach/`: the SQLite database, the generated memory files and imported files. To change this, use `--workspace` or `LOCAL_COACH_WORKSPACE`.

Configuration is done through environment variables, for example `LOCAL_COACH_VAULT`, `LOCAL_COACH_OLLAMA`, `LOCAL_COACH_MODEL` and `LOCAL_COACH_LANG` (`en` or `ru`; the language is chosen at startup, and after changing it for an existing working folder run `python3 coach.py reextract` so the memory is rebuilt in the new language). See [README.ru.md](README.ru.md#настройки-переменные-окружения) for the full list.

## Tuning the coach

The coach is **not fine-tuned**: the weights of the model are never changed, and nothing you say retrains it. Its behaviour comes from four things, and you can change all of them:

- **Memory.** Tell it in chat: `/remember ...` (or "remember that ..."), "correct that ..." to change a remembered fact, `/forget ...` to remove one. `/review`, `/calibrate`, `/checkin` and `/people` let you confirm or correct what it learned from your notes. What it remembers shapes its answers.
- **Depth and reasoning.** `/depth 1|2|3` (practical, analytical, deep reflection) and `/think` (reasoning on or off for the conversation).
- **Your own rules.** `/rule answer shorter` adds a rule that the coach follows in conversation, `/rules` lists them, `/rule delete 2` removes one. They live in `rules.md` in the working folder (one line each, you can edit the file by hand), work in the terminal chat and the web chat, and are added to the coach instructions with a note that they never override the safety rules. Up to 20 rules of 300 characters.
- **Instructions.** All instructions to the model are plain text in the repository: `localcoach/prompts_en.py` (English) and `localcoach/prompts.py` (Russian). The coach persona is `COACH_SYSTEM`; fact extraction, the profile, the registry and the other tasks have their own prompts. Edit them, restart the coach, and after changing an extraction prompt run `python3 coach.py reextract`. The prompts also carry the safety rules (no diagnoses, no invented facts, careful hypotheses), so keep those when you edit. The built-in instructions are not editable from the chat, only your own rules are.
- **Models and language.** `LOCAL_COACH_MODEL`, `LOCAL_COACH_HEAVY_MODEL`, `LOCAL_COACH_EMBED_MODEL`, `LOCAL_COACH_LANG` (and the language switch in the web settings). Any model that Ollama serves with structured output should work (see "Other models" above).

## Tests

```bash
python3 -m unittest discover -s tests
```

End-to-end tests run on a small invented vault against a fake Ollama. They need no model and no network, and take about two seconds. They check that the code rejects unverifiable output: invented quotes, references to clusters that don't exist, verdicts with no supporting timeline line, and secrets.

## Limitations

- A 9B model makes mistakes. It can misplace a fact in the wrong area of life, generalise from a single note, or pull in memory that doesn't fit. The code catches what can be verified, and you correct the rest with `review` and `/forget`.
- This is a tool for reflection, not therapy or medical advice.

## License

[MIT](LICENSE) © Jutqe

[Ollama]: https://ollama.com
[`qwen3.5:9b`]: https://ollama.com/library/qwen3.5
[`embeddinggemma`]: https://ollama.com/library/embeddinggemma
