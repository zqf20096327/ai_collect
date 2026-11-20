# Agentic Data Room

An investor data room is, by default, a shared folder on Drive. You sign an NDA with the investor, you send them a link, and an associate from the fund spends a week reading it before sending you a list of thirty questions. Then you answer them. The next fund sends a list that overlaps with the first one by about two thirds. This goes on for weeks, and most of the answers were in the folder the whole time.

This repository puts a chat on top of the folder. Investors ask questions in plain English and the bot answers from the documents you chose, with a citation to the file behind every number. Contracts are quoted rather than summarized. Questions that would need the financial model re-run, or a document that is not in the room, get a fixed refusal sentence instead of a guess. Every question lands in a log the founder can read the next morning.

![Walkthrough: ask a question, open a cited file, get a refusal on a what-if, browse the library](docs/media/walkthrough.gif)

We built this at Gaia Family during our last fundraising and gave it to every investor who was interested. 43 investors signed in and asked 372 questions. Every one was answered with a citation to a file in the room, or refused with a fixed sentence, and every one landed in a log we read the next morning. A few people have since asked for the approach and the implementation details, so the code is here, with a fictional company's data room inside so you can run it in about ten minutes. The longer story is in [the blog post](https://medium.com/gaia-family).

## Why build your own

The honest starting point is that your deck and docs are already in someone's AI. Associates paste the PDF into whatever they use and ask it questions. You have no say in which version of your docs they pasted, whether the churn figure it produced was real, or what ended up in the screenshot in their internal presentation. You cannot stop that. What you can do is offer a version that has the current documents, cites a file for every number, refuses questions that need the live model, and keeps a log. It has to be at least as convenient as the paste, or nobody will use it.

## Two decisions we were skeptical about at first and would make again

**No retrieval, everything in context.** A curated data room is 30 to 40 thousand tokens and the model's context window is 200 thousand, so the whole corpus goes into every request as a prompt-cached system block. Cached reads cost about a tenth of the normal input price. There is nothing to chunk, nothing to embed, and no retrieval step that can return the wrong passage. We would use retrieval if the room did not fit. It fit.

**Curate instead of ingest.** We did not point the bot at the Drive folder. We chose the documents by hand, had an agent rewrite each one into plain markdown, and kept a note on what was left out and why. The reason is mundane: if two documents give two prices, the bot picks one, and it is not always the current one. Deleting an old pricing sheet took five minutes and removed a whole class of wrong answers. Curation only works if the investor can check the source, so citations became the interface. The model may only cite `[doc:slug]`. One JSON file maps slugs to real files, and the UI turns a slug into a chip that opens the PDF or downloads the spreadsheet. That file was the whole contract between the AI side and the UI side, which is why the app could be built while the corpus was still being edited.

A curated corpus answers the narrative questions. Investors also ask about specific cells and specific clauses, so two small routers attach what the corpus cannot hold: up to four tabs of the financial model as CSV, with a rule that the cell wins over the prose, and the relevant contract PDF, which the bot then quotes. Both routers are a table of regular expressions with a small model as the fallback. [ARCHITECTURE.md](ARCHITECTURE.md) has the details.

## Ten minutes

Python 3.10+, Node 20+, an Anthropic API key.

```bash
git clone https://github.com/gaia-family/agentic-data-room.git && cd agentic-data-room
make demo
```

It installs, builds the index and the sample library, and opens http://localhost:3000. Two things on the way: paste your `ANTHROPIC_API_KEY` into `.env`, put your email in `ADMIN_EMAILS` in `web/.env.local`. Sign in with that email. No Resend key, the one-time code prints in the terminal. No Redis, no Google Drive, no accounts. Sessions live in memory, files come from `corpus/library`.

The sample company is Probably Covered Inc., which sells embedded insurance. Ask "What does the Growth plan cost?" Then ask "What would 2028 revenue be if the attach rate doubled?" and watch it refuse the second one.

## The eval is the spec

```bash
make eval          # corpus only
make upload        # once: push spreadsheet tabs and contracts to the Files API
make eval-files    # with sheets and contracts attached
```

Fifteen questions. Easy lookups, financial figures, three kinds of refusal, synthesis across documents, cell lookups. The sample passes 15 of 15 in both modes. In the real deployment the set grew from 10 to 23 questions in two weeks and every bug became a test: the bot that invented a theory for a multiplier, the cap table that answered in the wrong currency, the pricing sheet nobody deleted. Grading is crude on purpose. Read [docs/eval.md](docs/eval.md).

## Your own data room

1. One markdown file per document under `corpus/<section>/`, with `slug`, `title`, `note` in the frontmatter. [docs/curation.md](docs/curation.md) has the rules, including the three-layer extraction that makes a many-tab spreadsheet readable.
2. Register every slug in `corpus/manifest.json` (copy the example): title, filename, and a Drive id or a `local_path` under `corpus/library/`.
3. Drop the model at `corpus/finance/financial_model.xlsx`, point `SHEET_SLUG_MAP` in `build_index.py` and the two sheet routers at your tab names.
4. Contracts go in `corpus/legal/`, slugs and keywords in the two legal routers.
5. `make index`, `make upload`, rewrite `playground/eval_questions.json` for your numbers, run `make eval-files` until it is green.
6. Edit `PROMPT.md`. The refusal sentences are checked as exact substrings, so change them in both places or not at all.

Production: `GOOGLE_SERVICE_ACCOUNT_KEY` and `DRIVE_ROOT_FOLDER_ID` for Drive, `REDIS_URL` for a shared store, `RESEND_API_KEY` for login emails, and a dedicated Anthropic workspace with zero retention. [SECURITY.md](SECURITY.md) has the rest.

## If you are raising

Treat the room as a product with a login and a log, not as a folder. Let investors ask instead of scroll. Delete documents that are out of date rather than adding a note next to them. Make the bot refuse what it cannot know; "not covered in the data room" earns more trust than a confident guess. Read the log every morning, because it is the most direct feedback you will get during a raise. If the first version takes more than a day, the scope is wrong.

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

It was built by one person in four agent sessions on the same day. The sessions did not share context; they passed files.

Built with [Vaidik Kapoor](https://github.com/vaidik), who shipped the UI, the auth, and the deploy while the corpus was still being written.

MIT. See [LICENSE](LICENSE).
