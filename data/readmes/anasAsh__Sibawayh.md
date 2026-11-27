<div align="center">

```text
 ____   _  _                                      _
/ ___| (_)| |__    __ _ __      __   __ _  _   _ | |__
\___ \ | || '_ \  / _` |\ \ /\ / /  / _` || | | || '_ \
 ___) || || |_) || (_| | \ V  V /  | (_| || |_| || | | |
|____/ |_||_.__/  \__,_|  \_/\_/    \__,_| \__, ||_| |_|
                                           |___/
```

# سيبويه · Sibawayh: Arabic writing skill and grammar checker for AI agents

**Your AI writes Arabic. Sibawayh makes it _correct_ Arabic.**

A source-available Agent Skill (`SKILL.md`) and Arabic spelling, grammar and punctuation checker. It makes Claude Code, Codex, Cursor, GitHub Copilot and other AI coding agents write correct, natural Modern Standard Arabic (MSA, فصحى), and check it before they answer.

<p dir="rtl"><b>سيبويه</b> مهارة مفتوحة المصدر جزئيًا (Source-available) لوكلاء الذكاء الاصطناعي (Agent Skill)، ومدقّق إملائي ونحوي للغة العربية. تجعل Claude Code وCodex وCursor وGitHub Copilot وغيرها تكتب العربية الفصحى سليمةً وطبيعية، ثم تراجعها قبل الإجابة: الهمزات والإملاء وعلامات الترقيم والنحو والأسلوب واتجاه النص من اليمين إلى اليسار.</p>

[![License: MIT + Commons Clause](https://img.shields.io/badge/license-MIT%20%2B%20Commons%20Clause-orange)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-3776ab?logo=python&logoColor=white)](#-run-the-checker-yourself)
[![Dependencies: none](https://img.shields.io/badge/dependencies-none-brightgreen)](#-run-the-checker-yourself)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-SKILL.md-d97757)](skills/sibawayeh/SKILL.md)
[![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-d97757)](#-install)
[![AI-judged: −97% errors](https://img.shields.io/badge/AI--judged-%E2%88%9297%25%20errors-2ea44f)](https://anasash.github.io/Sibawayh/)

<img src="docs/assets/social-preview.png" alt="Sibawayh Arabic grammar checker: typical AI-generated Arabic with errors next to corrected Arabic" width="820">

[Install](#-install) · [How it works](#-how-it-works) · [What it catches](#-what-it-catches) · [Checker](#-run-the-checker-yourself) · [Evaluation](#-evaluation) · [How it is tested](https://anasash.github.io/Sibawayh/) · [بالعربية](https://anasash.github.io/Sibawayh/ar/) · [FAQ](#-faq) · [Contribute](#-contribute)

</div>

---

## 🤔 Why AI-generated Arabic needs checking

Ask ChatGPT, Claude or any other AI model for Arabic and you get text that is *understandable*, but that a native reader spots in a second:

| What goes wrong | Looks like |
|---|---|
| English grammar in Arabic words | تم إنشاء الملف من قبل المستخدم |
| Broken agreement | الملفات الذين تم رفعهم موجودين |
| Wrong number–noun gender | ثلاث مهندسين |
| Wrong hamza | إستخدام، الى |
| English punctuation | نعم, ولكن? |
| Scrambled RTL | lines starting with an English word flip direction |
| Dialect slipping into formal text | عشان، بدي، هيك |

Sibawayh is named after **سيبويه**, the 8th-century scholar whose *al-Kitāb* is the foundational book of Arabic grammar. It gives the agent the rules, a checker and a review checklist, so that its Arabic reads as if a careful native writer wrote it.

## ✨ Before and after: AI Arabic with and without Sibawayh

<div align="center">
<img src="docs/assets/demo.gif" alt="Demo: Claude Code writes an Arabic LinkedIn post without Sibawayh, then with Sibawayh" width="720">
<br><sub>Real Claude Code outputs for the same prompt, with and without the skill.</sub>
</div>

<table>
<tr><th>✗ Typical AI output</th><th>✓ With Sibawayh</th></tr>
<tr>
<td dir="rtl">

تم إستخدام الأداة من قبل الفريق, وهاذا ساعدنا كثيرا.<br>
لدينا 3 ملفات و٤ مجلدات.<br>
الملفات الذين تم رفعهم موجودين هنا

</td>
<td dir="rtl">

استخدم الفريق الأداة، وهذا ساعدنا كثيرًا.<br>
لدينا 3 ملفات و4 مجلدات.<br>
الملفات التي رُفعت موجودة هنا

</td>
</tr>
</table>

<details>
<summary><b>See what the checker reported on the left-hand text</b></summary>

```
1:1   INFO   translationese-density  Translationese density 15.8 per 100 words (تم/يتم: 2, من قبل: 1) …
1:4   ERROR  hamza-wasl    Hamzat al-wasl: write a bare alif, not إ (form X masdar)  → استخدام
1:32  FIX    punct-latin   Latin punctuation between Arabic words  → ،
1:34  ERROR  misspelling   Misspelling (no alif after ها)  → وهذا
2:16  WARN   digit-mix     Mixed digit systems; this text uses Western (0-9) digits  → 4
```

The script finds nothing on line 3: a regex can't reliably catch agreement with non-human plurals. That line gets fixed in the model's checklist review. This is exactly the split Sibawayh is designed around.

</details>

## ⚙️ How it works

```mermaid
flowchart LR
    A["✍️ Write<br/>with SKILL.md rules"] --> B["🔍 Check<br/>check_arabic.py --fix"]
    B --> C["📋 Review<br/>7-point checklist"]
    C --> D["✅ Answer<br/>clean Arabic only"]
```

1. **Write.** The skill loads whenever the agent is about to produce Arabic: answers, docs, emails, posts, translations, summaries, UI strings and commit messages. While writing, the agent follows the rules in `SKILL.md`: verb-first active sentences, correct agreement and numbers, Arabic punctuation, one digit system, and RTL-safe lines.
2. **Check.** It runs a tiny Python script with no dependencies. The script auto-fixes what is certain and flags the rest.
3. **Review.** It works through a prioritized checklist: agreement, numbers, case endings, إنّ/أنّ, translationese, register, formatting. It changes only what is wrong.
4. **Answer.** The user gets clean Arabic, with no checker noise.

> **🛡️ Golden rule: never over-correct.**
> Forms that purists reject but the Cairo Arabic Language Academy approved are never flagged. Examples: يعتبر، ساهم في، أكد على، في نفس الوقت، أبحاث. Contested forms are left alone, and auto-fixes run only where they can't be wrong.

## 🎯 What it catches

| | Area | Examples | Handled by |
|---|---|---|---|
| ✏️ | Punctuation | `,` `?` `;` → ، ؟ ؛, spacing | 🤖 checker (auto-fix) |
| 🔤 | Unicode | Persian ک/ی, presentation forms, tatweel | 🤖 checker |
| 📝 | Spelling | إستخدام, هاذا, الى, الاطفال, المدرسه, المصرى, و الكتاب, لايوجد, مساءًا | 🤖 checker (word lists + frequency lexicons) |
| 🔢 | Digits and RTL | mixed 3 / ٣, lines that flip direction | 🤖 checker |
| 🗣️ | Dialect leakage | عشان, بدي, هيك in formal text | 🤖 checker |
| ⚖️ | Verb endings | لم يكونون, لن يذهبون, سوف لن | 🤖 checker + 🧠 checklist |
| 🧮 | Agreement and numbers | non-human plurals, العدد والمعدود (ثلاث ملفات → ثلاثة ملفات, خمسة عشرة → خمس عشرة) | 🤖 checker (numbers 3–10 and 13–19) + 🧠 checklist + 📚 tables |
| 🌐 | Translationese | تم + masdar, قام بـ, من قبل, كـ "as a"; idioms translated word for word (يصنع الفرق) | 🤖 density and idiom list + 🧠 checklist |
| 💻 | Tech terms | واجهة برمجة التطبيقات (API) | 📚 glossary (450+ terms) |

## 📦 Install

### Claude Code

```
/plugin marketplace add anasAsh/Sibawayh
/plugin install sibawayeh@sibawayh
```

That's it. The skill now loads by itself whenever Claude writes Arabic.

Upgrading from an older release? The plugin and skill were called `arabic-writing`, then `sibawayh`. Run `/plugin uninstall sibawayh@sibawayh` (or `/plugin uninstall arabic-writing@sibawayh` if you're coming from 0.2.x), then the install command above.

<details>
<summary>Prefer a manual install?</summary>

```bash
git clone https://github.com/anasAsh/Sibawayh.git
cd Sibawayh
ln -s "$PWD/skills/sibawayeh" ~/.claude/skills/sibawayeh
# or: cp -r skills/sibawayeh ~/.claude/skills/
```

From a shell, the plugin commands are `claude plugin marketplace add anasAsh/Sibawayh` and `claude plugin install sibawayeh@sibawayh`.

</details>

### Codex, Cursor, GitHub Copilot and most other agents

The skill is a standard [`SKILL.md`](https://agentskills.io/specification) folder, and most agents read skills from one shared place: `~/.agents/skills/` for all your projects, or `.agents/skills/` inside one project.

```bash
git clone https://github.com/anasAsh/Sibawayh.git
mkdir -p ~/.agents/skills
cp -r Sibawayh/skills/sibawayeh ~/.agents/skills/
```

According to their documentation, that folder is read by OpenAI Codex, Cursor, GitHub Copilot (CLI and VS Code), Gemini CLI, OpenCode, Amp, Goose, Roo Code, Zed, JetBrains Junie and Windsurf (Devin Local). A few agents use their own folder; copy the same `sibawayeh` folder there instead:

| Agent | Folder for your user | Folder inside a project |
|---|---|---|
| Claude Code | plugin (above), or `~/.claude/skills/` | `.claude/skills/` |
| Cline | `~/.cline/skills/` | `.cline/skills/` |
| Kiro | `~/.kiro/skills/` | `.kiro/skills/` |
| Google Antigravity | `~/.gemini/config/skills/` | `.agents/skills/` |

If you use Node, [`npx skills add anasAsh/Sibawayh`](https://github.com/vercel-labs/skills) installs the skill into the agents you pick. It is a third-party tool that we have not tested.

### Claude Desktop and claude.ai

1. Download [`sibawayeh.zip`](https://github.com/anasAsh/Sibawayh/releases/latest/download/sibawayeh.zip) from the latest release. To build it yourself: `cd Sibawayh/skills && zip -r sibawayeh.zip sibawayeh -x '*__pycache__*'`
2. In Claude, open **Customize → Skills**, choose **Create skill → Upload a skill**, and upload the zip.
3. Turn on **Code execution and file creation** in **Settings → Capabilities**, so that Claude can run the checker.

We have not tested the upload yet; if Claude rejects it, please open an issue.

The Code tab of Claude Desktop reads `~/.claude/skills/` and Claude Code plugins, so the Claude Code install covers it.

### What has been tested

| Agent | Status |
|---|---|
| Claude Code | Full evaluation: 100 requests, see [Evaluation](#-evaluation) |
| OpenAI Codex CLI | Smoke-tested 2026-11-24: loads the skill from `.agents/skills/` and runs the checker |
| OpenCode | Smoke-tested 2026-11-24: loads the skill from `.agents/skills/` and runs the checker |
| All others | Install paths taken from each agent's documentation on 2026-11-24; not run by us yet |

A smoke test is one Arabic request, checked to see that the agent read `SKILL.md` and ran `check_arabic.py`. It does not measure quality. If an agent has no shell, the skill falls back to its checklist alone. Reports from other agents are welcome in the [issues](https://github.com/anasAsh/Sibawayh/issues).

## 🔍 Run the checker yourself

It needs Python 3.8 or later and nothing else.

```bash
python3 skills/sibawayeh/scripts/check_arabic.py file.md          # report findings
python3 skills/sibawayeh/scripts/check_arabic.py --fix file.md    # print text with safe fixes applied
python3 skills/sibawayeh/scripts/check_arabic.py --json -         # JSON findings from stdin
```

| Severity | Meaning |
|---|---|
| `fix` | certain; applied by `--fix` |
| `error` | almost always wrong |
| `warn` | probably wrong; check the context |
| `info` | style or consistency note |

<details>
<summary>More options</summary>

- `--digits western|arabic|auto` sets the expected digit system. The default, `auto`, follows the majority in the text.
- Exit code: `1` when findings above `info` remain, otherwise `0`.
- Never touched: code blocks, inline code, URLs, file paths, emails, YAML front matter, Qur'an quotes in ﴿…﴾, and anything between `<!-- arabic-check: off -->` and `<!-- arabic-check: on -->`.

</details>

## 🗂️ What's inside

```
skills/sibawayeh/
├── SKILL.md                  writing rules, workflow, checklist
├── references/
│   ├── grammar.md            agreement, numbers, case endings
│   ├── orthography.md        hamza, ة/ه, ى/ي, punctuation, digits, RTL
│   ├── style.md              translationese → natural Arabic
│   ├── common-errors.md      قل ولا تقل
│   ├── approved-forms.md     never "fix" these
│   ├── classical.md          classical register, only on request
│   ├── glossary.md           450+ tech terms, English → Arabic
│   ├── legal.md              contracts, notices: terms and document shape
│   ├── banking.md            bank/loan text: terms and document shape
│   └── commercial.md         business letters, quotations: terms and shape
└── scripts/
    ├── check_arabic.py       the checker (stdlib only)
    ├── archeck/              rules
    └── data/                 word lists
evals/                        before/after evaluation harness, results and raw answers
docs/                         the "How Sibawayh is tested" pages (English and Arabic)
tests/                        unit tests
research/                     the research the rules are built on
```

## 📊 Evaluation

The harness in [`evals/`](evals/README.md) answers 100 realistic prompts with and without the skill, and a judge scores both versions blind, without knowing which is which. So far the judge is an AI model from a different family; a native-speaker round is planned. The success bar is **zero over-corrections** and **about 50% fewer errors per 100 words**, with no category getting worse. **Triggering** (does the skill load when it should?): **20/20** (18/20 in the first run).
- All 14 requests in Arabic, or for Arabic output, loaded the skill. That includes summarise, rewrite and proofread.
- All 4 English-only requests correctly left it unloaded.
- The 2 dialect requests load it too, for the formatting checks only. In the first run they did not.

**Full evaluation** (100 prompts, judged blind by an AI model from a different family; see [`evals/full_eval.md`](evals/full_eval.md)):
- Errors per 100 words went from **2.26 to 0.07 (−97%)**, averaged over three blind judgings (−98%, −97% and −96%) of release 0.4.0. Register errors fell by 99% and translationese by 87%. On the 50 prompts the skill was not tuned on, the result is −95%.
- The Sibawayh version was preferred in **92–93** of the 100 pairs, the baseline in 3–4.
- **0** over-corrections. The success bar (≤50% of the baseline's errors, no category worse, no over-corrections) is met in all three judgings. The previous run (2026-11-23, release 0.3.0) was −96%, and the first run (2026-11-20, 50 prompts, one judging) was −88%. Answers vary from run to run, so the step from −96% to −97% is not evidence of an improvement.

An AI judge is not a native reader, so a human-scored round is still to come. [How Sibawayh is tested](https://anasash.github.io/Sibawayh/) describes every test in plain language ([بالعربية](https://anasash.github.io/Sibawayh/ar/)). All 100 requests, both answers to each and the judge's counts are on the [full results page](https://anasash.github.io/Sibawayh/results/) ([بالعربية](https://anasash.github.io/Sibawayh/ar/results/)); the raw files are in [`evals/results/`](evals/results/).

**Classical register** (new in 0.4.0, lightly tested; see [`evals/classical.md`](evals/classical.md)): on 20 requests for classical or elevated literary Arabic, the judge preferred the skill's answer to the no-skill answer in 17–19 of 20 pairs, and to release 0.3.0's answer in 12 of 20. It found no classical wording leaking into everyday answers. This is a small trial judged by an AI model, and it is separate from the −96% figure above.

**The checker against human corrections** ([`evals/benchmarks.md`](evals/benchmarks.md)): on two public corpora that people corrected word by word, it catches **52%** of all errors in student essays (ZAEBUC) and **41%** in native-speaker comments (QALB), up from 23% and 20% in release 0.1.2. For hamza it catches 68% and 59%; for و written apart from its word, 98% and 86%. Every flag on a word the annotators left unchanged was a real error they missed, or (in ZAEBUC) a Latin comma they chose to keep.

**Over-correction check** ([`evals/corpus_check.md`](evals/corpus_check.md)): on Arabic Wikipedia featured articles, every error-level flag was a real error, including in a held-out set used for no tuning.

## ❓ FAQ

**How do I make Claude or another AI agent write better Arabic?**
Install Sibawayh (see [Install](#-install)). The skill loads by itself whenever the agent writes Arabic. It gives the agent the writing rules, runs the checker, and reviews the text against a checklist before answering.

**Is it an Arabic spell checker?**
Partly. The checker catches Arabic spelling (hamza, ة/ه, ى/ي, tanween), punctuation, digit and RTL errors, some grammar (verb endings, number–noun gender, compound numbers), and English idioms translated word for word. A script can't reliably catch agreement and case endings, so the model's checklist review handles those.

**Can I use the checker without an AI agent?**
Yes. `check_arabic.py` is a standalone Python script with no dependencies. Run it on any Markdown or text file to proofread Arabic, or use `--json` in CI. See [Run the checker yourself](#-run-the-checker-yourself).

**Does it change correct Arabic?**
No, that is the golden rule. It never flags forms approved by the Cairo Arabic Language Academy, or contested forms. Its false flags are measured on Arabic Wikipedia featured articles.

**Does it work with Arabic dialects?**
Yes. When you ask for Egyptian, Gulf, Levantine or another dialect, the agent writes in that dialect. The skill then fixes only formatting (punctuation, digits, RTL lines), never the dialect itself.

**Can it write classical Arabic (فصحى التراث)?**
Yes, when you ask for it. Ask for classical or elevated literary style (فصحى التراث، أسلوب تراثي، "classical Arabic") or for a genre that is classical by nature, such as a Friday sermon, a maqama or a literary debate, and the agent switches register: weightier words, balanced sentences, sparing rhyme, and no invented quotations. Everyday requests stay in plain Modern Standard Arabic. This mode is new in 0.4.0 and has had only a small trial.

**Does it know legal, banking or business-correspondence Arabic?**
Yes. When the text is a contract, terms of service, legal notice, bank letter, loan/financing text, business letter, quotation or similar, the agent picks up the matching terminology and document shape (preamble and article numbering for a contract, the customer-notice phrasing for a bank letter, the opening/closing formulas for a business letter) on its own — no need to name the domain. This is new and has not had an evaluation trial yet.

**Which agents does it work with?**
Any agent that supports the `SKILL.md` Agent Skills format: Claude Code (as a plugin), Claude Desktop, Codex, Cursor, GitHub Copilot, OpenCode and others. See [Install](#-install) for each one's folder and for which agents we have tested. Agents without a shell use the checklist alone.

## 🤝 Contribute

Native-speaker review is the most valuable contribution. Ways to help:

- 🧑‍⚖️ **Score the answers.** The evaluation was judged by an AI model. If you read Arabic natively, score a set of the blind answer pairs in [`evals/results/`](evals/results/) and [open an issue](https://github.com/anasAsh/Sibawayh/issues) with what you find. The [test page](https://anasash.github.io/Sibawayh/ar/) explains the method.
- 🤖 **Try another agent.** Most agents in [Install](#-install) are documented but not yet tested by us. Tell us whether the skill loads and the checker runs in yours.
- 💻 **Glossary.** Suggest better or more standard terms in [`glossary.md`](skills/sibawayeh/references/glossary.md). Some terms, such as epoch, tokenization and pipeline, still have no settled Arabic equivalent.
- 📝 **Word lists.** Add misspellings to `scripts/data/*.tsv`. The rule is strict: an entry must be wrong in *every* context, and each entry needs a test.
- 🚩 **False flags.** If the checker flags correct Arabic, [open an issue](https://github.com/anasAsh/Sibawayh/issues) with the sentence.

Run the tests before opening a pull request:

```bash
python3 -m unittest discover -s tests -t .
```

## 📄 License

Source-available: MIT with the [Commons Clause](https://commonsclause.com/) condition, see [`LICENSE`](LICENSE). Free to use, modify, self-host and embed, including at a company, for any purpose — the only thing withheld is the right to **sell** the software itself or resell it as a hosted/managed service. If you want to offer Sibawayh (or a product substantially built on it) as a paid product or service, contact the author for a commercial license. The project contains no GPL code. Any entries adapted from LanguageTool (LGPL) would live only in `skills/sibawayeh/scripts/data/third_party/`, with their own licence notice. The frequency lexicons (`scripts/data/lexicon_*`) are word counts derived from [Arabic Wikipedia](https://ar.wikipedia.org/) featured articles, whose text is licensed CC BY-SA 4.0.

<div align="center">
<br>
<sub>Built for Arabic speakers who are tired of AI that writes <i>almost</i> right. 🌙</sub>
</div>
