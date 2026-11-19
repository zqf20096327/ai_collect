# Agentic Data Room

Your investor data room is a folder. With an NDA on the door. The associate reads it for a week and sends you 30 questions. You answer the same 30 questions for every fund. For months.

This repo replaces the folder with a chat. Investors ask in plain English. The bot answers from your documents, cites the file behind every number, quotes contracts instead of paraphrasing them, and refuses what it cannot know. You read the chat log every morning. Best investor feedback you will ever get, and it is free.

![Walkthrough: ask a question, open a cited file, get a refusal on a what-if, browse the library](docs/media/walkthrough.gif)

Built at Gaia Family during our fundraising. V1 shipped the same day it was pitched. The round closed. Folks at a MIPT (Phystech) reunion asked me for the code, so here it is, with a fictional company's data room inside so you can run it in ten minutes.

## The associate already has ChatGPT

Your deck is already in someone's chatbot. The only question is whose.

Theirs: the FINAL_v7 from an email, not v29 from the room. Hallucinated churn. No citations. A screenshot in the partner meeting that you will never see.

Yours: one version, every number cited to a file, what-ifs refused, nothing stored, nothing trained on, and a log of every question asked.

Build the governed one first.

## Three decisions, no regrets

**1. No RAG.** A curated data room is 30 to 40 thousand tokens. The context window is 200 thousand. Retrieval is for things that do not fit. Ours fit. So the whole corpus goes into every request as a prompt-cached system block. Cache reads cost a tenth. Nothing to chunk, nothing to index, nothing for retrieval to get wrong. Reflexive RAG is the new reflexive microservices.

**2. Curate, do not ingest.** Do not point the bot at the Drive folder. Pick the documents by hand, rewrite each one into clean markdown, write down what you threw out and why. Two documents with two prices means the bot picks one. The agent does the typing. You do the editing. The editing is the job.

**3. Citations are a contract.** The model may only cite `[doc:slug]`. One JSON file maps slugs to real files. The UI turns the slug into a chip that opens the PDF or downloads the xlsx. That file was the entire integration between the AI side and the UI side. Best API I ever shipped.

Then two things a curated corpus cannot do on its own. Investors ask about cells, not stories, so a router attaches up to four tabs of the financial model as CSV at question time, with a rule that the cell wins over the prose. Investors ask about clause 7.2, so a second router attaches the contract and the bot quotes it word for word. Both routers are a regex table with a small model as fallback. Details in [ARCHITECTURE.md](ARCHITECTURE.md).

## Ten minutes

Python 3.10+, Node 20+, an Anthropic API key.

```bash
git clone https://github.com/d-sigal/agentic-data-room.git && cd agentic-data-room
make demo
```

It installs, builds the index and the sample library, and opens http://localhost:3000. Two things on the way: paste your `ANTHROPIC_API_KEY` into `.env`, put your email in `ADMIN_EMAILS` in `web/.env.local`. Sign in with that email. No Resend key, the one-time code prints in the terminal. No Redis, no Google Drive, no accounts. Sessions live in memory, files come from `corpus/library`.

The sample company is Probably Covered Inc., embedded insurance for things you forgot to insure. Ask "What does the Growth plan cost?" Then ask "What would 2028 revenue be if the attach rate doubled?" and watch it refuse. That refusal is the feature.

## The eval is the spec

```bash
make eval          # corpus only
make upload        # once: push spreadsheet tabs and contracts to the Files API
make eval-files    # with sheets and contracts attached
```

Fifteen questions. Easy lookups, financial figures, three kinds of refusal, synthesis across documents, cell lookups. The sample passes 15 of 15 in both modes. In the real deployment the set grew from 10 to 23 questions in two weeks and every bug became a test: the bot that invented a theory for a multiplier, the cap table that answered in pounds, the pricing sheet nobody deleted. Grading is crude on purpose. Read [docs/eval.md](docs/eval.md).

## Your own data room

1. One markdown file per document under `corpus/<section>/`, with `slug`, `title`, `note` in the frontmatter. [docs/curation.md](docs/curation.md) has the rules, including the three-layer extraction that makes a 19-tab spreadsheet readable.
2. Register every slug in `corpus/manifest.json` (copy the example): title, filename, and a Drive id or a `local_path` under `corpus/library/`.
3. Drop the model at `corpus/finance/financial_model.xlsx`, point `SHEET_SLUG_MAP` in `build_index.py` and the two sheet routers at your tab names.
4. Contracts go in `corpus/legal/`, slugs and keywords in the two legal routers.
5. `make index`, `make upload`, rewrite `playground/eval_questions.json` for your numbers, run `make eval-files` until it is green.
6. Edit `PROMPT.md`. The refusal sentences are checked as exact substrings, so change them in both places or not at all.

Production: `GOOGLE_SERVICE_ACCOUNT_KEY` and `DRIVE_ROOT_FOLDER_ID` for Drive, `REDIS_URL` for a shared store, `RESEND_API_KEY` for login emails, and a dedicated Anthropic workspace with zero retention. [SECURITY.md](SECURITY.md) has the rest.

## Playbook, steal it

1. The data room is a product. Login, welcome screen, log. Not a folder.
2. Bot instead of deck. The investor asks, not scrolls.
3. Delete more than you add.
4. Refusal is a feature. "Not here" earns more trust than a guess.
5. Every number has a source, or the number does not exist.
6. Read the chat log every morning.
7. V1 in a day. If it needs a week, you are building the wrong thing.

## What is inside

```
agentic-data-room/
├── PROMPT.md                 # the rules. Edit this, not the code
├── Makefile                  # setup, index, library, upload, eval, dev, demo, check
├── corpus/
│   ├── overview/ acquisition/ product/ finance/   # one markdown per document
│   ├── finance/financial_model.xlsx                # tabs become CSVs for cell questions
│   ├── legal/*.pdf                                 # attached when the question is about a contract
│   ├── library/                                    # what the app serves in local mode
│   ├── manifest.example.json                       # the citation contract
│   ├── build_index.py                              # writes _index.md and _slug_to_asset.json
│   ├── sheet_router.py  legal_doc_router.py        # what to attach, per question
│   └── make_sample_library.py                      # renders the sample docs to PDF
├── playground/               # Streamlit chat for prompt work, eval runner
├── eval/questions.md         # the eval, human-readable
└── web/                      # Next.js: OTP login, chat, citations, library, admin
```

Next.js 15. Claude Sonnet answers through a forced tool call: TLDR, typed blocks, sources. Claude Haiku routes when the regex does not. Email OTP, allowlist, two access groups, admin invites, and a read-only browser of every investor conversation. Optional: Redis, Drive, Resend, Sentry, Hotjar, LangSmith.

One person, four agent sessions, same day. The agents never talked to each other. They passed files.

Built with [Vaidik Kapoor](https://github.com/vaidik), who shipped the UI, the auth, and the deploy while the corpus was still being written.

MIT. See [LICENSE](LICENSE).
