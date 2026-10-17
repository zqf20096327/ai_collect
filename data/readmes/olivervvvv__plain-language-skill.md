# plain-language

**English** ｜ [繁體中文](README.zh-TW.md)

Turn AI prose that needs three reads into prose that needs one — without changing what it says.

**Before**

> Following an evaluation of the current implementation, it was determined that the introduction of a
> completeness validation gate at the import-to-persistence transition point is feasible; however, as the
> source system provides only a snapshot of the most recent period and does not retain historical
> sequences, retrospective verification of this layer cannot be performed, and forward-only observation
> must therefore be adopted.

**After**

> **Bottom line:** We can add the check, but we can only prove it works going forward — there's no history to test against.
>
> - It sits between import and the database write: incomplete data doesn't get written.
> - The source system only gives us the latest snapshot, with no history.
> - No history means no backtest. We'd have to accumulate results after it ships.
>
> **Detail:** source exposes latest period only (no historical sequence). Backtesting needs a different source.

Same facts, same constraints, same hedge. 78 words → 62, and the answer arrives in the first line.

---

An Agent Skill for rewriting convoluted, jargon-stacked AI output and technical documents into plain
language. It has **two separate rule sets** — one for Traditional Chinese, one for English — because the
two languages fail in different ways. They are not translations of each other.

Works with [Claude Code](https://claude.com/claude-code), [OpenClaw](https://docs.openclaw.ai), and any environment that supports Agent Skills.

## Why two rule sets

The two languages fail differently, so porting one language's rules onto the other doesn't work.

**Chinese** — the worst habit is the unbroken multi-idea sentence. Chinese has no clause markers and
tolerates comma chains, so one breath can carry thirty-plus characters and three separate ideas. It also
lets you drop the subject legally, so `已移除` ("removed") reads like a conclusion while never saying who
did it or where. Add `進行／加以／做出` nominalization and `的` chains, and you get prose where every
character is familiar and the paragraph still needs three reads.

**English** — the worst habit is hiding the actor. Agentless passive ("it was decided that", "the column
is dropped") plus noun stacking ("data quality validation gate configuration") makes the reader guess both
who acts and which noun modifies which. Then come the Latinate padding (utilize / facilitate / prior to),
the hedge stacks ("it may potentially be possible that"), and the LLM tics ("It's worth noting that",
"delve into", "robust", "not only… but also").

Each track maps its own failure modes to executable rewrite rules. What they share — the accuracy red line,
long-form structure, the pre-flight checklist — lives in `SKILL.md`.

## Core design

- **The red line comes first.** Readability must never cost accuracy. Numbers, units, constraints, risks, and stated uncertainty are preserved verbatim. Output that is easy to read but wrong is worse than output that is merely hard to read.
- **Action items must have a location.** Every "fix this" has to point at a file, sheet, column, or line number. If the source text never said, the rewrite labels it `原文沒說` ("the source doesn't say") instead of papering over the gap. Plain language may clarify; it may not invent facts.
- **Long answers get a skeleton.** A lead block carries the conclusion (a reader who stops there can still make the right decision), numbered sections walk through setup → cause → options → recommendation, and details plus open questions go into appendices.
- **Headings carry content.** Read the section headings alone and you have a summary — not empty labels like "Analysis" and "Conclusion".
- **It knows when to stay out of the way.** Specs, legal text, and expert-to-expert conversation are explicitly excluded: there, precision beats readability and plain language is just noise.

## Structure

```
SKILL.md               shared: red line, long-form skeleton, checklist, when not to apply
references/zh-TW.md    Traditional Chinese: diagnosis, rewrite rules, examples
references/en.md       English: diagnosis, rewrite rules, examples
always-on.md           the block the installer appends to your global CLAUDE.md
install.sh / .ps1      one-line global install
```

The agent reads `SKILL.md` first, then loads only the track matching its output language.

## Install

One line, global, always on:

```bash
git clone https://github.com/olivervvvv/plain-language-skill /tmp/pl && sh /tmp/pl/install.sh
```

Windows PowerShell:

```powershell
git clone https://github.com/olivervvvv/plain-language-skill $env:TEMP\pl; & "$env:TEMP\pl\install.ps1"
```

The installer clones the skill into every skills directory it finds (`~/.claude/skills`, `~/.openclaw/skills`)
and appends a short always-on block to your global `CLAUDE.md` / `AGENTS.md`.

### Always-on vs keyword-triggered

A skill on its own is **model-invoked**: it loads when the request looks like a match ("put this in plain
English", 「翻成人話」). That's the default Agent Skills mechanism, and it means dense output still ships
whenever nobody thought to ask.

Always-on mode fixes that by putting one small rule where the agent reads it every turn — your global
`CLAUDE.md` — so the agent classifies its own output before delivering it:

- **Written to a file, implemented verbatim, machine-read, or legal** → stays precise. Never simplified.
- **Explanation, status report, diagnosis, option comparison — anything a human just reads** → delivered plain.

The dividing line is deliberately mechanical: **written to disk → precise; spoken to a person → plain.**
No keyword needed, and specs don't get mangled.

Skill only, no always-on:

```bash
sh install.sh --skill-only     # or: .\install.ps1 -SkillOnly
```

To turn always-on off later, delete the block between the `plain-language:begin` / `plain-language:end`
markers in your `CLAUDE.md`. Re-running the installer never duplicates it.

## Provenance

Every rule in here came from a round of real feedback — someone reading the output and saying "still can't follow it." The rules accumulated in this order: split into sections → make headings carry content → number them → lead with the conclusion → give action items a subject and a file location → break ASCII tables into bullets. The examples have been rewritten as generic cases.

## License

MIT
