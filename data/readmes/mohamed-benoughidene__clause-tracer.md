<p align="center">
  <img src="assets/clause-tracer-readme-banner.jpg" alt="Clause Tracer: AI contract review you can check. Local-first, your own playbook, evidence for every label." width="100%">
</p>

<p align="center">
  Private AI contract review for freelancers, solo lawyers and small law firms, on Linux and Windows.
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-FSL--1.1--ALv2-blue" alt="License: FSL-1.1-ALv2"></a>
  <img src="https://img.shields.io/badge/status-design%20%26%20prototype-orange" alt="Status: design and prototype">
  <img src="https://img.shields.io/badge/platforms-Linux%20%7C%20Windows-lightgrey" alt="Platforms: Linux and Windows">
  <img src="https://img.shields.io/badge/telemetry-none-brightgreen" alt="Telemetry: none">
</p>

---

With **Clause Tracer**, you write a **playbook**, your rules for a good deal: "paid within 30 days", "liability capped at the fee", "no non-compete". Clause Tracer reads the contract, labels every clause your playbook covers, and links each label to the exact words that support it. You check each result in one click, then send the other side a clear reply.

It runs on your own computer, with your own [OpenRouter](https://openrouter.ai) key. Names and addresses are replaced before anything is sent to an AI model. There's no account, no server run by the project and no telemetry.

> **Status: in design.** The spec, design system and a clickable HTML prototype are done. The code skeleton is in place and coding has started, but the app isn't usable yet. [Try the prototype](#try-the-prototype) and [watch the repo](https://github.com/mohamed-benoughidene/clause-tracer) to follow along.

## Why Clause Tracer

AI contract review tools are quick, but they can be wrong, and they rarely show their working. Clause Tracer is built on one rule: **the AI can be wrong, so every result comes with evidence you can check.**

- **Your rules, not a generic checklist.** Compare the contract with your own playbook of contract positions, from payment terms to IP ownership. Start from the free starter playbook for freelancers, then make the limits yours.
- **Evidence for every label.** Each label opens to the quoted clause, with the exact words highlighted, plus a plain-words reason. Follow cross-references and defined terms through the contract, like a red thread.
- **Code decides, not the AI.** For number and yes/no rules, the AI only pulls out the value and its quote. Code checks that the quote is really in the contract, then picks the label. Labels judged from wording alone are marked "AI judgment".
- **Private by design.** A privacy check replaces personal data (names, companies, addresses, emails, phone and bank numbers) on your computer, using [Presidio](https://microsoft.github.io/presidio/). Private mode asks for zero-retention AI providers only. Everything saved is encrypted.
- **From review to reply.** Turn the walk-aways and open questions into a ready-to-send negotiation email, or save a PDF contract review report.

## How it works

1. **Load the contract.** Load a PDF, a Word file (.docx), a text or Markdown file, or paste the text.
2. **Pick a playbook and your side.** For example, you're the "service provider".
3. **Check the clauses.** See how the contract was split into clauses. Hidden text is found and shown.
4. **Check the privacy.** Personal data is highlighted and replaced with placeholders such as `Person 1` and `Company 1`. You see the estimated cost before you send.
5. **Read the review.** The contract appears as its own pages, with a label on every clause a position covers:

   | Label | Meaning |
   | --- | --- |
   | ✓ **Preferred** | Meets your best terms |
   | ≈ **Acceptable** | You can live with it |
   | ✕ **Walk-away** | Crosses a line you set |
   | ? **Unsure** | The wording is vague, or the quote couldn't be confirmed |

   A **Missing** list shows what the contract leaves out. A **Not covered** list summarises the parts your playbook doesn't cover.
6. **Check every position.** Confirm or change each label. A walk-away or unsure label needs a real decision, not just a tick.
7. **Reply.** Write a friendly or formal message asking for changes, rewrite a clause, or export a report.

Clause Tracer is a checking tool, **not legal advice**. It compares the contract with your business rules. It doesn't judge what the law allows.

## Who it's for

- **Freelancers and contractors** who aren't lawyers, checking a client contract, an NDA or a statement of work before they sign.
- **Solo lawyers and small law firms** who want a fast, consistent first pass against their own clause playbooks, without uploading client documents to someone else's cloud.

## Try the prototype

The [HTML prototype](prototype/) shows every screen and state in version 1. It needs only Python 3:

```bash
git clone https://github.com/mohamed-benoughidene/clause-tracer.git
cd clause-tracer
python3 -m http.server 8767 --bind 127.0.0.1 --directory prototype
```

Then open http://localhost:8767. Start at First launch, or go to `states.html` for a map of every flow. Open `review.html?sample` for a practice review with one wrong label planted for you to catch.

## Version 1 at a glance

| | |
| --- | --- |
| **Platforms** | Linux and Windows desktop. Mac comes later. |
| **Contracts** | English. PDF with real text, .docx, .txt, .md, or pasted text. |
| **AI** | Models on OpenRouter, using your own key (bring your own key). You pay OpenRouter directly, and the cost is shown before and during each review. |
| **Privacy** | Personal data is replaced on your computer. Private mode is on by default. Data is encrypted at rest. Reviews are deleted automatically after 7, 30 or 90 days. |
| **Security** | The AI has no tools and can't run code. Contract text is always shown as plain text, and links in the contract open only after a warning. |
| **Not in version 1** | Scanned PDFs, other languages (Arabic and French are planned next), legal opinions, and accounts or cloud sync. |

## Documentation

| Document | What it covers |
| --- | --- |
| [Spec](docs/spec.md) | What version 1 does: the user flow, labelling rules, AI pipeline, privacy and acceptance tests |
| [Design system](docs/design-system.md) | Tokens, components and accessibility |
| [UX copy](docs/ux-copy.md) | The voice and the words on every screen |
| [Decisions](docs/adr/) | Architecture decision records |
| [Brand](docs/clause-tracer-brand-philosophy.md) | Why a red thread and a butterfly |
| [All docs](docs/) | The index of everything in `docs/` |

## Contributing

Issues and ideas are welcome, especially from freelancers and lawyers who review contracts.

### Set up for development

You need Python 3.12 or later. Everything else installs inside the repo folder: the packages in `.venv/` and the download cache in `.cache/uv/`. Both are git-ignored, and nothing is installed system-wide. After you clone the repo, run:

```bash
python3 -m venv .venv && .venv/bin/pip install --no-cache-dir uv
```

```bash
.venv/bin/uv sync
```

Then check that everything works:

```bash
scripts/check.sh
```

This runs the linter, the formatter check, type checks, the import rules and the tests. Use `.venv/bin/uv add <package>` to add a dependency, and commit the updated `uv.lock` with it.

### Sending a change

Code contributions are accepted under the [Contributor License Agreement](CLA.md). Run `scripts/check.sh` before you send one: it must pass. Write commit messages and name branches as [GIT_CONVENTIONS.md](GIT_CONVENTIONS.md) says. Please read the [Constitution](Constitution.md), the rules for how the code is built, before you start. When your change affects what the app does or says, update the docs too: [WRITING_DOCS.md](WRITING_DOCS.md) says which files to change. To report a security problem, see [SECURITY.md](SECURITY.md).

## License

Clause Tracer is **source available** under the [Functional Source License 1.1](LICENSE) (FSL-1.1-ALv2).

- **Free** to use, change and share for any purpose except a competing product or service. That includes paid work for your own customers.
- **Paid** to host it as a service for others, or to sell something that offers the same features. See [COMMERCIAL_LICENSE.md](COMMERCIAL_LICENSE.md).
- **Each version becomes Apache 2.0** two years after its release.

<sub>Keywords: AI contract review · contract analysis · contract checker · clause review · contract playbook · contract risk · freelancer contracts · NDA review · legal tech · privacy-first · local-first · PII redaction · OpenRouter · LLM · desktop app</sub>
