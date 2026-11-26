# Viva Recall

**Flashcards you answer in your own words, marked by a decision model you can argue with.**

Viva Recall is a desktop app for open-ended recall. You write a question and the answer you expect. An LLM turns your answer into small yes/no checks. When you study, a **decision model** ([Jev](https://docs.typesafe.ai) by TypeSafe) answers each check with a calibrated probability, and plain code turns those probabilities into a verdict. [FSRS](https://github.com/open-spaced-repetition/ts-fsrs) schedules the next review. If you disagree with a mark, an appeal agent talks it through with you and can fix the checks, but only if your previously settled answers still pass.

![Demo: searching the Library, filtering across decks, fixing a flagged card with the assistant, managing decks, creating a deck while writing, and studying across decks](docs/demo/viva-recall-demo.gif)

## Why a decision model, not an LLM grader

Asking an LLM "is this answer correct?" on every review is slow, costly, hard to reproduce, and easy to argue with. Viva Recall splits the job three ways:

| Who | Does what | When |
|---|---|---|
| **LLM** (any provider) | Writes the yes/no checks from your answer, and handles appeals | Once per card, and on disputes |
| **Decision model** (Jev) | Answers each check: *"Does the answer say borrowing gets more expensive?"* → `p = 0.93` | Every review, in one request |
| **Code** | Bands each probability (yes / no / unsure) and applies the card's rule to reach a verdict | Every review, deterministically |

The judgment ("does this sentence say X?") is what decision models are good at: fast, cheap, and calibrated. The decision ("so is the answer correct?") stays in code, where it can be inspected and unit-tested as a truth table. The LLM is kept for the work that needs it: writing good checks, and reasoning with you when they're wrong.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/diagrams/readme/overview-dark.svg">
  <img alt="How Viva Recall works: write a card, an LLM writes checks, Jev marks answers, code decides, FSRS schedules, disputes go to the appeal agent" src="docs/diagrams/readme/overview-light.svg">
</picture>

## How an answer is marked

Each card's checks are versioned data. One marker request per answer sends only the question and your answer as state, plus every check:

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/diagrams/readme/marking-sequence-dark.svg">
  <img alt="Sequence: your answer goes to the main process, which sends one request to Jev and turns the probabilities into a verdict and an FSRS rating" src="docs/diagrams/readme/marking-sequence-light.svg">
</picture>

The verdict order, in code (`src/main/domain/decide.ts`):

1. The answer may contain instructions to the marker → **unsure**, always
2. Not a real attempt → **wrong**
3. A misconception check fires → **wrong**, with feedback on why
4. The rule is met (all groups, or "any N of M"; groups are any-of alternatives) → **correct**
5. Some key points passed → **wrong · incomplete**, listing what's missing
6. An off-target check fires → **wrong · answers a different question**

When a check lands between 0.3 and 0.7, the app works out the verdict with that check as both yes and no. If both give the same verdict, it stands. Only when the doubt could change the outcome is the answer **unsure**, and then you rate yourself or ask the appeal agent.

## Thresholds: fixed for Jev, fitted for Laya

- **Jev** needs no calibration. Its probabilities are already calibrated, so every Jev model version uses TypeSafe's recommended thresholds (0.7 / 0.3) and marks as soon as it's configured. On a bundled set of 60 labelled answers (correct paraphrases, misconceptions, incomplete, off-target, blank, and attempts to instruct the marker), Jev at 0.7 / 0.3 credited 10 of 10 correct paraphrases and never marked a wrong answer correct.
- **Laya** (open source, run locally, **experimental**) is calibrated: the 60 answers are run through it once and a threshold search picks the pair with the best *balanced* agreement, because its base checkpoints are uncalibrated. On the same set, zero-shot Laya credited at most 3 of 10 correct paraphrases:

  | Laya checkpoint | Correct credited | Wrong caught |
  |---|---|---|
  | english | 10% | 98% |
  | multilingual | 0% | 82% |
  | typed-decisions | 30% | 98% |

  Plain overall agreement hid this (70–87%), because most fixtures expect "wrong". That's why calibration scores per verdict.

## Fixing cards and disputing marks

**Fix with assistant.** A generated card must pass its own markability test before it can be studied. If it doesn't, or the generator suspects *your answer* is factually wrong (e.g. "Is Pluto a planet? → Yes"), the card gets a `!` and stays out of study. The assistant opens beside the card, explains the problem in plain words and offers one-click fixes:

- correct the answer
- rewrite the question
- edit the checks
- keep my answer
- regenerate
- mark it myself

Nothing changes until you click. Once a fix is applied you're taken back to the Library, where the card's status updates as its checks regenerate.

**Appeals.** Dispute any mark and the appeal agent treats your card's answer as the authority, not how persuasive you are. Every appeal ends in exactly one outcome:

| Outcome | What changes |
|---|---|
| `learner_wrong` | Nothing; the agent explains why (the expected common case) |
| `marker_misjudged` | This mark is overridden |
| `paraphrase_rejected` | A check's criterion is broadened by principle, not by pasting your words |
| `unanticipated_answer` | An alternative check is added to an any-of group |
| `confusing_check` | A check is split or rewritten |
| `ambiguous_question` | The question is rewritten; earlier marks are flagged suspect |
| `answer_key_wrong` | Your answer is updated and the checks regenerated |

Any check edit must keep every **regression bank** answer at its settled verdict. That covers the generator's test answers and every previously disputed answer, so the checks can't quietly drift looser. When an appeal overturns a mark, the review log entry is superseded and the card's FSRS schedule is **replayed** from the start as if you'd been marked right at the time.

## Decks and the Library

- **One deck picker everywhere.** Search decks by name, pick several at once (Library and Study), or type a new name to create a deck on the spot.
- **Deck names are unique,** ignoring case. Decks can be renamed, and deleting one asks whether to move its cards to another deck (keeping their history and schedules) or delete them with it.
- **Search the Library** by keywords across questions and answers, filter to cards that need attention, and keep your filters while you move between screens.
- **Import from Anki or a spreadsheet.** In the Library, choose **Import** and pick a CSV (comma, semicolon or tab; header row optional) or an Anki export from *File › Export › Notes in Plain Text*. The preview shows which columns are the question, answer and deck (change them if the guess is wrong), how many cards will be imported, and what's skipped: cloze notes, rows with an empty question or answer, and questions already in the target deck, so importing the same file twice adds nothing. Anki formatting becomes plain text; sounds and images are dropped. Anki sub-decks keep their full name, like `Biology::Cells`. Then either:
  - **Import as manual**: ready to study straight away, and you rate yourself. A good fit for short Anki answers like "Mitochondria", which the preview counts for you. Turn manual marking off on a card later to generate its checks.
  - **Import & generate checks**: each card is queued for check generation, like a card you wrote. That's one generator request per card.

  Nothing is written until you choose, and an import that fails partway imports nothing.
- **Export** saves the cards the Library is showing (after deck, search and attention filters) as a CSV with `deck,question,answer` columns. Checks and review history aren't included. The file imports back into Viva Recall.

## Study: workload, progress and studying ahead

The Study screen answers two questions before you start: *how long will today take?* and *am I improving?* Every figure follows the decks you've picked.

- **Time estimate.** "12 due · ~9 min" uses the median time of your last 50 answers, measured from the question appearing to the result appearing (marking included). Until 20 answers have been timed, it assumes 45 seconds per card and says so.
- **Retention.** The share of reviews of review-state cards (not new or still learning) that you recalled in the last 30 days, with how many of those the marker marked rather than you. A 7-day rolling line shows the trend. Easy upgrades and appeals count once, at their final rating.
- **Mature cards.** Cards whose FSRS stability is at least 21 days, and how that count moved over the month.
- **Forecast calendar.** How many cards fall due on each day, in your local time zone, with overdue cards on today. Use the arrow keys to move between days, and Enter to see a day's decks and estimate.
- **Study ahead.** From a future day, start a session with everything due by the end of that day, due-now cards first. These are real reviews: FSRS schedules each card from when you answer it, so an early review gains a little less than an on-time one.
- **Session summary.** Recalled and missed, the marker's verdicts with why answers were wrong, disputes and whether they changed the outcome, the questions you missed (each opens its card), and what's due next.

There are no streaks.

## Data model

SQLite, local. Check sets are immutable versions, the review log is append-only, and every mark records the check version and marker profile it used. An [interactive ERD](docs/diagrams/schema-erd.html) is in `docs/diagrams/`; the core:

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/diagrams/readme/data-model-dark.svg">
  <img alt="Entity-relationship diagram of the core SQLite tables" src="docs/diagrams/readme/data-model-light.svg">
</picture>

## Architecture

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/diagrams/readme/architecture-dark.svg">
  <img alt="Architecture: React renderer talks over typed IPC to the Electron main process, which owns keys, the queue, marking, FSRS and SQLite" src="docs/diagrams/readme/architecture-light.svg">
</picture>

- **Keys never reach the renderer.** Every network call happens in the main process, and API keys are encrypted with the OS keychain (`safeStorage`).
- **Bring your own models.** Any OpenAI-compatible endpoint (OpenAI, Gemini's free tier, OpenRouter, Ollama…) or Anthropic, configured separately for the generator and the appeal agent.
- **Spec-driven.** Requirements live in [`openspec/specs/`](openspec/specs) (13 capabilities, 113 requirements with testable scenarios). The design decisions, including the ones changed by testing, are in the [archived changes](openspec/changes/archive/): the [initial build](openspec/changes/archive/2026-11-22-build-flashcard-marking-app/design.md) and [deck and library improvements](openspec/changes/archive/2026-11-22-deck-and-library-qol/design.md).

![Setup wizard](docs/screenshots/setup-wizard.png)

## Getting started

Requirements: Node 20+, macOS (tested on Apple Silicon), a [TypeSafe](https://typesafe.ai) API key for Jev, and an LLM API key (OpenAI, Gemini, Anthropic, …).

```bash
npm install        # also rebuilds better-sqlite3 for Electron
npm run dev        # the setup wizard walks you through keys and a connection test
```

Other commands:

```bash
npm test           # 102 unit tests, run under Electron's Node
npm run typecheck
npm run dist:mac   # unpacked macOS build in dist/

# opt-in live checks against real services
TYPESAFE_API_KEY=… npm test -- jev.live
# behind a proxy that injects the key (e.g. a cloud sandbox), pass a placeholder:
TYPESAFE_API_KEY=proxy-injected npm test -- jev.live
LAYA_LIVE_URL=http://127.0.0.1:8000 npm test -- laya.live
```

To try Laya (experimental), run it yourself, e.g. on Apple Silicon: `pip install "laya-mlx[serve]"`, then `LAYA_HOST=127.0.0.1 laya-mlx-serve`.

## Project layout

```
src/shared/      check-set schema (zod), domain types, IPC channel schemas
src/main/
  domain/        decide() verdict logic, FSRS scheduler with replay, marker wording
  marker/        Jev and Laya clients (POST /v1/systemone, Noul questions)
  llm/           OpenAI-compatible and Anthropic chat clients
  prompts/       generator, appeal and repair prompts (versioned)
  services/      generation queue, marking + regression gate, calibration, cards, study, appeals, repair
  db/            migrations and repository
src/preload/     contextBridge allow-list
src/renderer/    React UI
resources/fixtures/fixtures.json   60 labelled calibration answers
openspec/        specs and the archived design change
docs/            interactive diagrams and screenshots
```

---

Viva Recall is an independent project. It uses TypeSafe's public Jev API and is not affiliated with TypeSafe.

Licensed under the [MIT License](LICENSE). Third-party licences for everything that ships in the app are in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md); after changing dependencies, run `npm run licenses` (or `npm run licenses:check` to verify).
