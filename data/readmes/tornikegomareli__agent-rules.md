# agent-rules 

Fix your agents communication style, make it simple to read, easy to reason about, and remove AI slop from generated output.

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" />
  <img src="https://img.shields.io/badge/Shell-POSIX%20sh-89e051.svg" />
  <img src="https://img.shields.io/badge/Dependencies-none-brightgreen.svg" />
  <img src="https://img.shields.io/badge/Agents-Claude%20Code%20%7C%20Codex%20%7C%20Pi%20%7C%20Amp%20%7C%20Gemini%20%7C%20OpenCode-orange.svg" />
</p>

<p align="center">
  <img src="media/agent-rules-hero.png"
       alt="Unit tests versus integration tests, explained with and without the rules" width="100%" />
</p>

One behavior ruleset for every coding agent on your machine. It removes noise from responses so they’re easier to read, follow the same rules, and don’t drain your focus with AI slop.

`install.sh` writes it into each agent's global memory file, so it applies in
every project with no per-project setup. Behavior only, no coding conventions.

- [Install](#install)
- [Use it as a skill](#use-it-as-a-skill)
- [Showcase](#showcase)
- [What the rules cover](#what-the-rules-cover)
- [Install options](#install-options)
- [Does it actually work](#does-it-actually-work)
- [Make it yours](#make-it-yours)
- [Limits](#limits)

## Install

```bash
git clone https://github.com/tornikegomareli/agent-rules.git ~/.agent-rules
cd ~/.agent-rules
./install.sh
```

The installer finds your agents, appends the rules to each global memory file,
and leaves anything already there untouched. Start a new session to pick them up.

| Agent | File |
| --- | --- |
| Claude Code | `~/.claude/CLAUDE.md` |
| Codex CLI | `~/.codex/AGENTS.md` |
| Pi | `~/.pi/agent/AGENTS.md` |
| Amp | `~/.config/amp/AGENTS.md` |
| Gemini CLI | `~/.gemini/GEMINI.md` |
| OpenCode | `~/.config/opencode/AGENTS.md` |

Not in the list? `./install.sh --path ~/.youragent/AGENTS.md` takes any file.

Undo with `./install.sh --uninstall`. Other modes in
[Install options](#install-options).

## Use it as a skill

The install above is always on. It changes how your agents write, in every
session, whether or not you think about it.

Sometimes you want the opposite: a ruleset you point at one piece of text on
purpose. A README you already wrote. A release note a teammate drafted. A wall of
prose an agent handed you. For that there is a skill.

```bash
npx skills add https://github.com/tornikegomareli/agent-rules --skill agent-rules
```

It lands in `~/.agents/skills/` and reaches every agent it can find. On a machine
with the usual set installed, that is a symlink for Claude Code, Pi and OpenClaw,
plus universal copies for Codex, Cursor, Gemini CLI, OpenCode, Zed and others.
Add `--global` for user-level, `--agent <name>` to pick specific agents, or
`--list` to see what is in the repo without installing.

The installer asks whether you want it globally or in one project, and which
agents on your machine should get it. Requires Node.

Inside Claude Code you can install the whole repo as a plugin instead:

```
/plugin add https://github.com/tornikegomareli/agent-rules
```

Then invoke it directly:

```
/agent-rules clean up this release note
/agent-rules check README.md
```

Edit is the default. Check reports violations and changes nothing. Both run
`scripts/score.py` first, so you get line numbers and a score rather than an
opinion:

```
draft.md: 80 words, avg sentence 10, 20% over 20 words, Flesch 56
  12 violation(s), 15.00 per 100 words:
    banned word          line 3    …our comprehensive new REST API…
    banned word          line 4    …will empower your team to leverage seamless…
    em dash              line 3    …new REST API — a paradigm shift that…
    preamble opener      line 1    …Great question! We're thrilled to…
    binary contrast      line 5    …It's not just an API, but a powerful platform…
    copula avoidance     line 5    …platform that serves as the foundation…
    summary-recap ending line 9    …In conclusion, this marks a pivotal moment…
    closing pleasantry   line 12   …Let me know if you have any questions!…
```

Run the skill in edit mode on that same file and it comes back at 34 words with
zero violations. The 80-word original is in the test above; both numbers come
from the checker, not from an opinion.

Use both. They cover different jobs.

| | Global install | Skill |
|---|---|---|
| When it applies | Every turn, automatically | When you invoke it |
| What it governs | How the agent writes | Text that already exists |
| Works on your own writing | No | Yes |
| Cost when idle | Tokens in every session | Nothing |

The skill carries its own copy of the ruleset, so it works when installed on its
own. `./sync-skill.sh --check` fails if that copy drifts from `RULES.md`.

## Showcase

Same prompt, same model. The only difference is whether `RULES.md` was loaded.
Red marks every rule the plain answer broke. All pairs are reproducible from
[`bench/`](bench/).

### Writing a PR description

![PR description, with and without the rules](media/agent-rules-pr.png)

268 words about a diff it never saw, `[fill in based on infra]` shipped as the
deliverable, and an admission that the whole thing is a template in the last
line.

### Writing a commit message

![Commit message, with and without the rules](media/agent-rules-commit.png)

It invents the cause, invents the fix, and writes both into your git history.

### Estimating work

![Estimate, with and without the rules](media/agent-rules-estimate.png)

Quotes human developer-days for work it will finish in one session.

### Release notes and other prose

![Release note, with and without the rules](media/agent-rules-releasenote.png)

Emoji, em dash, hype adjective, marketing voice, and a call to action nobody
asked for.

### Holding a position

![Pushback, with and without the rules](media/agent-rules-pushback.png)

Both reach the right verdict. Only one refuses to agree before it has seen the
query.

## What the rules cover

| Area | What it enforces |
|---|---|
| Answer shape | First sentence answers the question. No preamble, no restating the question, conclusion before reasoning |
| Length | Match the question. No recap, no padding, no sentences that only signal effort |
| Sentence patterns | 19 named patterns to avoid, including binary contrast, throat-clearing, faux insight, rhetorical setups, colon reveals, fake-profound endings, summary recaps, robotic rhythm and em dash decoration |
| Vocabulary | A banned word list, a cut-when-empty list, dead phrases, and the "quietly" and "matters" crutches. Precise technical uses stay allowed |
| Plain technical English | Based on [ASD-STE100](https://asd-ste100.org). One word per idea, 20 words per instruction, one instruction per sentence, simple tenses, no noun stacks over three words |
| Formatting | Prose by default. Bullets only for parallel items, tables only for real comparisons, no nesting past one level, no emoji, no bold sentences |
| Opinions | Recommend one option and say why, then give the pros and cons that would change your mind. Disagree directly, with evidence. No praise |
| Anti-sycophancy | Do not fold when pushed back on. Never say "you're absolutely right" and then undo working code. Explain the same thing the same way every time |
| Uncertainty | Separate verified from inferred. "I don't know" is allowed, confident guessing is not. No invented APIs, flags, paths or citations |
| Estimates | Do not estimate unless asked. When asked, estimate in turns and minutes, not sprints and months. Drop costs that exist only because humans were doing the work |
| Reporting work | Say what you actually did. Show failures. Verify before reporting, because a diff that looks correct is not a result |
| Working style | Think before coding, simplicity first, surgical changes that trace to the request, goal-driven execution with verification |
| Stop and ask | Two failed guesses is the limit. Search the web before a third attempt, stop if that finds nothing. Ask first for anything destructive or hard to undo |

Full text in [`RULES.md`](RULES.md), about 300 lines.

## Install options

Merge is the default and your existing config survives. The rules go into a
marker-delimited block appended to the end of the file:

```markdown
# your own notes, untouched

<!-- >>> agent-rules >>> -->
...rules...
<!-- <<< agent-rules <<< -->
```

Everything outside those markers is left alone, and re-running the installer
swaps the block instead of adding a second copy.

`--replace` backs up each file and writes only the rules. It lists what it is
about to discard and asks first:

```
Replace mode will discard existing content from:
  ~/.claude/CLAUDE.md (12 lines of your own content)

Each file is backed up first, and './install.sh --restore' undoes this.
Continue? [y/N]
```

Both directions are reversible. `--uninstall` undoes a merge, `--restore` undoes
a replace, and each gives back your original file byte for byte. Backups look
like `CLAUDE.md.agent-rules.bak.20260729-013000`, are never overwritten or
deleted, and merge mode creates none because it destroys nothing.

To update: `cd ~/.agent-rules && git pull && ./install.sh`

```bash
./install.sh --list                 # agents, their files, available backups
./install.sh --dry-run              # report what would change, write nothing
./install.sh --target claude,codex  # only these agents
./install.sh --all                  # every known agent, even if not detected
./install.sh --path FILE            # also install into FILE, for an unlisted agent
./install.sh --replace              # back up, then write only the rules
./install.sh --restore              # bring back the most recent backups
./install.sh --uninstall            # remove the block, keep the rest
./install.sh --yes                  # skip confirmation prompts
```

## Does it actually work

The repo ships the benchmark that produced every pair above, so you can check
rather than trust. It runs each prompt twice, once in a clean directory and once
in a directory holding `RULES.md`, then scores both.

```bash
SAMPLES=2 ./bench/run.sh    # 12 prompts, 48 responses
python3 bench/score.py      # violation counts and readability
python3 bench/judge.py      # blind pairwise judging
```

Scoring is regex, not opinion. Every check in `bench/score.py` maps to a specific
rule in `RULES.md`.

Judging is blind. Each pair goes to a fresh session with no memory file, so the
judge never sees the rules, and each pair is judged twice with the positions
swapped so a win only counts when both orderings agree. **The rules won 9 of 12
prompts, baseline won 1, and the judge disagreed with itself on 2.**

Numbers, per-prompt tables and the judge's reasoning for all 24 rounds live in
[`bench/`](bench/).

### Where the rules lose

Asked to explain git rebase, the baseline used 206 words and covered `git bisect`
readability, squash and reorder, and force-push mechanics. The ruled answer
covered the same core in 106 words and dropped those specifics. The judge picked
the baseline, both times, and it was right.

That is the cost of "less is more". When a question wants coverage rather than a
verdict, shorter answers lose information. If you ask broad explain-everything
questions often, soften the Length section.

The rules also cost more money, not less. `RULES.md` adds tokens to every request
and the model spends more thinking about how to comply. Output gets shorter, the
bill does not.

## Make it yours

`RULES.md` is a starting point. Fork it and cut whatever you disagree with. A
rule you do not believe is worse than no rule, because it dilutes the ones you
do.

**Keep it short.** This file loads into every session in every project. Past a
few hundred lines it costs real money and dilutes itself.

**Write rules you could grade.** "No preamble, first sentence answers the
question" is checkable. "Be concise" is a vibe and gets treated like one. Prefer
prohibitions, because agents drift toward verbosity and hedging by default.

**Avoid contradictions.** Two rules that fight produce behavior you cannot
predict or debug. If you add a length rule, check it against the plain technical
English section.

## Limits

Rules about tone, length, formatting, structure and how uncertainty gets reported
are followed reliably. Rules that fight an agent's own harness are not. Every
agent ships built-in response guidance and yours layers on top of it, usually
winning but not always.

The em dash result shows the ceiling. A flat ban on one character still left
instances in a fifth of responses.

Some tools have no global instruction file at all. Cursor keeps user rules in a
settings UI, and Zed reads rules per project. For those, paste `RULES.md` in by
hand. `--list` will not show them and the installer cannot reach them.

Everything else is covered by `--path` today, and a pull request makes it
permanent. Adding an agent is one row in `KNOWN_TARGETS` inside `install.sh`:

```
name|path-relative-to-home|Display Name
```

## License

[MIT](LICENSE)
