# Claude for Researchers

A practical guide and toolkit for researchers — especially physicists and mathematicians
— who want to use [Claude Code](https://claude.ai/code) productively on long, technically
demanding projects.

This guide is written from real experience running a months-long mathematical research
project with Claude Code, not a weekend experiment. It covers what works, what wastes time,
the failure modes you will hit, and how to set up a workflow that survives them.

**What this guide is not.** There are other projects focused on getting Claude to *conduct*
research autonomously — literature surveys, hypothesis generation, paper drafting.
This is not that. The goal here is to give you a well-structured workspace and a reliable
workflow so that *you* can do the research faster and more cleanly: less time on
housekeeping, better continuity across sessions, fewer mistakes from working in a big
messy codebase. Claude is the tool; you are the researcher.

**Version 2026.09 · v1.18.0** — see [CHANGELOG.md](CHANGELOG.md) for recent updates. If you
set up a project from an earlier copy, the changelog tells you what is worth
re-copying from `starter/`. (The calendar tag says how current your copy is; the SemVer
says how much has changed and whether anything breaks — see the changelog intro.)

---

## How to read this guide

This guide serves two audiences at once, so it is organised in parts:

- **Never used Claude Code?** Read [Part I](#part-i-getting-started) from the top.
  It takes you from nothing to a fully configured project — including a step where
  Claude does the setup for you. Then read Part II gradually, as the topics become
  relevant to your work. You do not need anything in Part III to be productive.
- **Already using Claude Code?** Skip Part I (except perhaps
  [Bootstrapping](#bootstrapping-a-new-project-with-claude), which is useful for any
  new project) and start with [Part II](#part-ii-the-core-workflow) — the workflow
  patterns there are the heart of this guide. Add the machinery in
  [Part III](#part-iii-power-tools) when you want it.
- **Everyone**, whatever your experience level: read
  [Honest limitations](#honest-limitations) before trusting anything Claude produces.
  The failure modes described there are not edge cases.

---

## Table of Contents

**[Part I: Getting started](#part-i-getting-started)** — *for readers new to Claude Code*

1. [Installation and first launch](#installation-and-first-launch)
2. [Bootstrapping a new project with Claude](#bootstrapping-a-new-project-with-claude)
3. [Quick-start flowcharts](#quick-start-flowcharts)
4. [The right mental model](#the-right-mental-model)

**[Part II: The core workflow](#part-ii-the-core-workflow)** — *the heart of the guide, for everyone*

5. [CLAUDE.md: the most important file](#claudemd-the-most-important-file)
6. [The dual-document pattern: workbook.tex and brief.tex](#the-dual-document-pattern-workbooktex-and-brieftex)
7. [Session continuity: next-session-prompts.md](#session-continuity-next-session-promptsmd)
8. [BUGS.md: the recurring-mistake registry](#bugsmd-the-recurring-mistake-registry)
9. [Claim discipline: name only what you computed](#claim-discipline-name-only-what-you-computed)
10. [Auditing a document before you rely on it](#auditing-a-document-before-you-rely-on-it)
11. [Session length and context limits](#session-length-and-context-limits)
12. [Plan mode: investigate before you edit](#plan-mode-investigate-before-you-edit)
13. [Skills: reusable procedures](#skills-reusable-procedures)
14. [Git workflow for academics](#git-workflow-for-academics)
15. [Numerics and computation](#numerics-and-computation)

**[Part III: Power tools](#part-iii-power-tools)** — *optional; adopt once the basics feel comfortable*

16. [Settings and hooks](#settings-and-hooks)
17. [Group projects: shared vs personal configuration](#group-projects-shared-vs-personal-configuration)
18. [Reducing token consumption: rtk](#reducing-token-consumption-rtk)
19. [The pipeline workflow: keep Claude fluent in your own code](#the-pipeline-workflow-keep-claude-fluent-in-your-own-code)
20. [distill: filtering noisy research-command output](#distill-filtering-noisy-research-command-output)
21. [GitHub README and LaTeX](#github-readme-and-latex)

**[Part IV: What Claude gets wrong](#part-iv-what-claude-gets-wrong)** — *required reading*

22. [Honest limitations](#honest-limitations)

**[Appendix](#appendix)**

23. [Templates and scripts in this repo](#templates-and-scripts-in-this-repo)
24. [The ChatGPT twin: chatgpt-for-researchers](#the-chatgpt-twin-chatgpt-for-researchers)
25. [Using both: Claude and Codex on one project](#using-both-claude-and-codex-on-one-project)

---

# Part I: Getting started

*New to Claude Code? Start here. By the end of this part you will have a working
installation and a fully configured research project — most of it set up by Claude
itself. Experienced users can skip ahead to [Part II](#part-ii-the-core-workflow).*

## Installation and first launch

This section is for readers who have never used VS Code or Claude Code before.
If you are already set up, skip to
[Bootstrapping a new project with Claude](#bootstrapping-a-new-project-with-claude).

### What you need

- A computer running macOS, Windows, or Linux
- An [Anthropic account](https://console.anthropic.com/) (the same account you use for Claude on the web)
- A Claude Pro subscription **or** API credits — Claude Code uses your API account

You do not need to know anything about terminal commands or configuration files
to get started. This guide walks through each step.

---

### Step 1 — Install VS Code

VS Code is a free text editor made by Microsoft. Claude Code runs inside it as
an extension. You can also run Claude Code in a standalone terminal, but VS Code
gives you a much better experience: you see the files Claude is editing, the
terminal where it runs, and the chat window all in one place.

1. Go to [https://code.visualstudio.com](https://code.visualstudio.com) and
   click the download button for your operating system.
2. Run the installer. On macOS, drag VS Code into your Applications folder.
   On Windows, the installer does everything for you.
3. Open VS Code. You will see a welcome screen. You can close it.

That is all. You do not need to configure anything in VS Code before continuing.

---

### Step 2 — Install the Claude Code extension

1. In VS Code, click the **Extensions** icon on the left sidebar (it looks like
   four squares, one slightly detached).
2. In the search box that appears, type `Claude Code`.
3. The first result should be "Claude Code" by Anthropic. Click **Install**.
4. After installation, a Claude icon appears in the left sidebar.

Alternatively, you can install Claude Code as a command-line tool and use it
from any terminal without VS Code:

```bash
npm install -g @anthropic-ai/claude-code
```

This requires Node.js to be installed. The VS Code extension is easier if you
are not familiar with the terminal.

---

### Step 3 — Sign in

1. Click the Claude icon in the VS Code sidebar.
2. Click **Sign in with Anthropic**.
3. A browser window will open. Sign in with your Anthropic account.
4. After signing in, return to VS Code. You should see a chat interface.

If you are using API credits instead of Claude Pro: in the sign-in screen,
choose **Use API key**, paste your key from
[console.anthropic.com/settings/api-keys](https://console.anthropic.com/settings/api-keys),
and confirm.

---

### Step 4 — Open your project folder

Claude Code works on a folder, not a single file. It reads the files in your
project folder and makes changes to them.

1. In VS Code, go to **File → Open Folder** (macOS: **File → Open...**).
2. Navigate to your research project directory and open it.
3. VS Code will show your files in the left sidebar under "Explorer."

If you do not have a project folder yet, create one:

```bash
mkdir my-research-project
cd my-research-project
git init
```

The `git init` command sets up version control, which Claude Code uses to track
changes and help you undo mistakes. If you do not have git installed, see
[git-scm.com/downloads](https://git-scm.com/downloads).

---

### Step 5 — Start a conversation

In the Claude Code chat panel (the one that opened when you clicked the Claude
icon), type a message and press Enter. For example:

> "I just opened my project folder. What files are in it?"

Claude will look at your folder and reply. From here, you can ask it to read
files, write code, compile LaTeX, run Python scripts, or help you organise your
work.

**The most important thing to do next** is create a `CLAUDE.md` file in your
project folder. This file tells Claude everything it needs to know about your
project every time you open it. Without it, Claude starts each session knowing
nothing about your work.

You can write it by hand — the [CLAUDE.md section](#claudemd-the-most-important-file)
below explains exactly what to put in it. Or, for the fastest path, skip to
[Bootstrapping a new project with Claude](#bootstrapping-a-new-project-with-claude)
— the next section: describe your project to Claude in plain language, point
it at this guide, and it will create all the files and install all the tools for you.

---

### A note on cost

Claude Code charges per message based on the length of the conversation. A
typical research session (a few hours of active use) costs roughly $1–5 USD in
API tokens, depending on how much context is loaded and how many files are read.

You can track your usage at
[console.anthropic.com/usage](https://console.anthropic.com/usage). If you have
a Claude Pro subscription, Claude Code usage is included in that plan.

---

## Bootstrapping a new project with Claude

The fastest path from nothing to a fully configured research project is to let
Claude do the setup for you — once. Here is how.

This section mentions pieces that are explained later in the guide — CLAUDE.md,
skills, hooks. You do not need to understand them first: set the project up now,
and learn what each piece does in Part II as you start working.

**Step 1 — Gather your materials.** Create a folder for the project. Put in it
whatever you have: a LaTeX draft, reference PDFs, computation scripts, handwritten
notes scanned to PDF, a plain-text outline. It does not matter how raw the state is.

**Step 2 — Open the folder in VS Code and start a Claude Code session.**

**Step 3 — Describe the project.** In your first message, tell Claude everything
it would need to know. Cover:
- What the project is and what mathematical or scientific object you are studying
- The open question you are working toward
- The files you added and what each one is for
- The notation and conventions you use (including sign and normalisation choices)
- Your preferences: how detailed should LaTeX write-ups be, what is your git remote
  setup, do you use Mathematica or Python for numerics, etc.
- Anything else you would put in a CLAUDE.md if you were writing it by hand

Do not worry about structure. Write it conversationally. The more you say, the
better the generated CLAUDE.md will be.

**Step 4 — Paste the setup message.** One message does the whole setup. It is
written to force Claude to *read your repo and your description* and generate real
content — not to paste templates. The distinction in the prompt between "copy
verbatim" and "generate from what I told you" is the part that matters; do not
soften it.

> I want to set up this project using the workflow at
> https://github.com/Mexregkan/claude-for-researchers/. First read that repo's
> `starter/` directory so you know the exact structure of every file. Then:
>
> **Copy these verbatim** — they are generic infrastructure and need no edits:
> - `.claude/settings.json` (from `starter/.claude/settings.json`)
> - `.claude/hooks/pre-compact.sh` and `.claude/hooks/promise-checker.sh`
> - `.gitignore` (from `starter/.gitignore`)
>
> **Copy this one and then fill it in:** `.claude/agents/git-committer.md` (from
> `starter/.claude/agents/git-committer.md`) — the sub-agent that does every commit
> and push. Replace the two clearly-marked project blocks with my real repos (their
> remotes and push order, including any nested repo such as an `Overleaf/` clone that
> must never be pushed) and my protected files. Ask me for anything you do not know;
> do not guess a remote. From now on, use this agent for every commit and push instead
> of running `git commit` yourself.
>
> **Copy this kit verbatim:** the claim-discipline kit —
> `.claude/skills/simple-case-gate/SKILL.md`, `.claude/skills/claim-audit/` (SKILL.md +
> `gate_audit.sh` + `selftest.sh`), `.claude/agents/claim-auditor.md` and
> `.claude/agents/round-planner.md`. It is not optional: the *Simple-case gate* and
> *Research-claim discipline* blocks of the `CLAUDE.md` you generate below name
> `/simple-case-gate` and `/claim-audit` by name, so skipping them leaves a dangling
> command. Run `bash .claude/skills/claim-audit/selftest.sh` once and tell me the pass count.
>
> **Copy this kit verbatim, then fill in one line:** the document-audit kit —
> `.claude/skills/doc-audit/` (all five files), `.claude/agents/doc-sweeper.md`,
> `.claude/agents/doc-auditor.md`, and `audits/README.md`. It evaluates one finished
> document without editing it, so it is useful in any project that keeps records. The
> one thing to fill in: the `SEARCH_DIRS` line near the top of `doc_lint.sh` must list
> the folders my documents cite scripts, logs and data from, or every pointer will be
> reported as unresolved. Run `bash .claude/skills/doc-audit/selftest.sh` once
> afterwards and tell me the pass count.
>
> **Install skills by relevance — NOT all of them.** The four generated files
> below are universal; skills are not. From my project description, decide which
> of these apply to this project:
> - `latex-compile`, `sync-brief` — every project (they serve the core files)
> - `verify-citation` — only if I will cite literature
> - `reality-check`, `cross-validate` — if Claude will be doing derivations or
>   calculations whose correctness matters (default: yes for research)
> - `nb-to-wolfbook`, `sync-wb-nb`, `wolfram-headless` — only if I use Mathematica
>   (`wolfram-headless` also applies to any heavy headless `wolframscript` use)
> - `wolfbook` — only if I drive Mathematica through the Wolfbook MCP from Claude
>   (the extension's `wolfbook.mcpEnabled` is on); skip it for headless-only or UI-only use
> - `overleaf-sync` — only if I mentioned a shared Overleaf project
>
> For each skill you selected, check `~/.claude/skills/<name>/SKILL.md` first:
>   - **Exists globally and covers the same ground**: skip — the global skill is
>     already available in every project, a local copy adds nothing.
>   - **Exists globally but the starter version is meaningfully more complete**
>     (has explicit error-handling rules, severity thresholds, or hard constraints
>     the global version lacks): install the starter version locally and report the
>     key differences in one sentence so I can decide whether to update my global
>     skill too.
>   - **Does not exist globally**: copy from `starter/.claude/skills/<name>/SKILL.md`.
>   End with a one-line summary in three groups: not relevant to this project
>   (not installed), found globally (skipped), installed locally (and why).
>
> If the project runs numerics, also create the empty staging folders
> `numerics/generated/` and `figures/generated/` — the CLAUDE.md you generate
> below explains their role (AI-produced outputs pending my review).
>
> Only if I told you I push to two git remotes (e.g. personal GitHub + institution
> GitLab): copy `starter/scripts/git-push-both.sh` to `scripts/`, and enable the
> dual-remote mirror hook by replacing the empty `PostToolUse` array in
> `.claude/settings.json` with the block documented in that file's
> `_comment_posttooluse`. Do NOT enable it for a single-remote project — it would
> fail silently. (The hook ships OFF by default for exactly that reason.)
>
> **Generate these from what I told you at the start of this session.** All five
> files below must be customised to THIS project. Use the starter files ONLY for
> their structure — preamble, macros, section layout, comment style — and replace
> every example sentence and every bracketed stub (`[Project Title]`,
> `[Statement of main result.]`, `[SHORT DESCRIPTIVE NAME]`, `[e.g., ...]`, etc.)
> with real content drawn from my description. Do not leave a single bracketed
> placeholder anywhere. If you genuinely lack the information for a section, ask
> me — do not invent it and do not leave the template text in place.
> - `CLAUDE.md` — based on `starter/CLAUDE.md`. Fill in Goal, Files,
>   Conventions, Current status, my real git remotes, my notation, and my
>   numerics setup, all from what I described.
> - `workbook.tex` — keep the starter's preamble and theorem environments, set
>   the real title and author, write a real introduction and a real conventions
>   section from my description, and make sections for the actual topics of this
>   project. Short is fine; generic is not — it must be about MY project.
> - `brief.tex` — keep the starter's preamble and the `\established` /
>   `\conjectured` / `\open` colour macros, set the real title and author, then
>   fill the Main results, Conventions, and Open problems sections with this
>   project's actual current state. Tag each item `[ESTABLISHED]`, `[CONJECTURED]`,
>   or `[OPEN]`. Delete the example theorem/definition stubs — do not ship them.
> - `next-session-prompts.md` — keep the structure (top task block + DONE log),
>   then write a real first task: its context, the precise what-to-do (naming the
>   file and section), and a concrete success criterion — all for this project.
>   Replace the `Prompt A` / `Prompt B` example text entirely; leave the DONE log
>   empty since nothing is done yet.
> - `BUGS.md` — based on `starter/BUGS.md`. Keep the standing rule, the legend, and
>   the section skeleton; put my name and today's date in the standing rule, keep
>   the sections that match my engine and workflow and delete the rest, and delete
>   every entry marked `[EXAMPLE]`. Leave the unmarked generic entries — they are
>   true here too until this project proves otherwise. Do not invent project-specific
>   traps: the file fills up as we hit them.
>
> If `workbook.tex`, `brief.tex`, or any target file already exists, do NOT
> overwrite it — tell me and stop.
>
> Create all of the above with the Write tool. Then run these install commands —
> I will approve the few one-time permission prompts they trigger:
> - `brew install rtk && rtk init -g --auto-patch`
> - `mkdir -p ~/.claude/skills/pdf && curl -o ~/.claude/skills/pdf/SKILL.md https://raw.githubusercontent.com/anthropics/skills/main/skills/pdf/SKILL.md`
>   (skip if `~/.claude/skills/pdf/SKILL.md` already exists)
> - `code --install-extension wolfbook.wolfbook` (only if I use Mathematica)
> - `curl -fsSL https://raw.githubusercontent.com/Mexregkan/claude-for-researchers/main/scripts/patch-wolfbook-splitter.py | python3 -`
>   (only if I use Mathematica — fixes Wolfbook's comment-split bug; reload the VS Code window after)
> - `curl -fsSL https://raw.githubusercontent.com/Mexregkan/claude-for-researchers/main/scripts/apply-notebook-ux.py | python3 -`
>   (only if I use Mathematica — notebook word wrap + Mathematica-style section-folding keybindings; reload the VS Code window after)
> - `git init` (only if this is not already a git repo)

**Step 5 — Approve the one-time install prompts.** Claude writes all the files
silently, then runs the four install commands. Those few commands will ask for
permission *in this first session only* (see the note below). Approve them.

**Step 6 — Review what Claude produced.** Read the generated `CLAUDE.md`,
`workbook.tex`, and `brief.tex`. The infrastructure (settings, hooks, skills) is
correct by construction. The parts that need your eyes are the domain-specific
ones — Conventions, Current status, the introduction — because those depend on
your knowledge. If Claude left anything generic or got a convention wrong, fix it
now, and you are ready to begin.

### Alternative: scripted setup

If you prefer answering questions over pasting a prompt, `scripts/bootstrap.sh`
does the same setup deterministically. Run it from your new project folder:

```bash
curl -fsSL https://raw.githubusercontent.com/Mexregkan/claude-for-researchers/main/scripts/bootstrap.sh | sh
```

It asks for the project title, author, numerics engine, and whether you cite
literature, want the validation skills, or pair with a shared Overleaf project.
It then installs the universal core — `CLAUDE.md`, the workbook /
brief / next-session-prompts trio with your title and author already filled
in, and `BUGS.md` — and **only the skills your answers make relevant**, skipping any skill
already in your global `~/.claude/skills/`. It never overwrites an existing
file, creates the `generated/` staging folders when you run numerics, and
offers `git init`.

The script handles *structure*; it cannot write your introduction or
conventions. It finishes by printing the short prompt to paste into your first
Claude session, which fills the remaining bracketed stubs from your project
description. Both routes end in the same place — with the prompt, Claude makes
the relevance decisions from your description; with the script, you make them
by answering questions.

**If you have existing Mathematica notebooks or scripts**, run `/nb-to-wolfbook` on
them after setup is complete. Point it at a file or a whole directory and it will
convert everything to Wolfbook's `.wb` format in one step — re-run the cells
afterwards to regenerate output.

**Why the install commands may prompt (once).** The `settings.json` Claude just
wrote asks before anything dangerous (`rm`, `mv`, `git reset --hard`, …) and blocks
edits to files you mark as irreplaceable, so you stay in control without ever being
stuck. Claude Code reads `settings.json` once, at session start, so it does not take
effect until your *next* session — which is why these install commands can ask for
permission in this very first session. Approve them. How much you are prompted from
here on depends on your [permission mode](#permissions): in **auto mode**, the
default since August 2026, routine commands run without prompting and a classifier
vets them instead; in Manual mode you approve each one.

This works because Claude Code can read a GitHub repository, run shell commands, and
write files, and because the guide it is reading contains explicit templates and
instructions. Filling those templates with your project — turning a description into
a working `CLAUDE.md`, `workbook.tex`, and `brief.tex` — is exactly the kind of
structured work Claude does reliably. The research that follows is yours.

---

## Quick-start flowcharts

Visual overviews of the two key workflows. Scan these before reading the full guide.

| Setting up a new project | Each working session |
|:---:|:---:|
| ![Project setup flowchart](assets/flowchart-setup.png) | ![Session workflow flowchart](assets/flowchart-session.png) |

Green = start/end · Blue = action · Gold = decision · Red label = no path · Green label = yes path

---

## The right mental model

Before setting anything up, it helps to understand what kind of tool Claude Code
actually is, because the wrong mental model leads to the wrong workflow.

**Claude Code is not a research collaborator.** It does not have intuition, taste,
or genuine understanding of your field. It has read an enormous amount of text,
including mathematical papers, and can pattern-match on that reading very
effectively. That is genuinely useful, but it is different from understanding.

**Claude Code is not an intelligent assistant that figures things out.** It follows
instructions. If your instructions are vague, the result will be vague. If your
instructions are precise — which file, which section, which formula, what to check —
the result will be precise and fast.

**Claude Code is a very capable junior research assistant.** It can:
- Write, edit, and compile LaTeX faster than you can, including tracking down obscure errors
- Write Python or Mathematica computation scripts from a clear specification
- Keep careful records — updating documents, maintaining logs, tracking what was tried
- Read and navigate a large document without losing track of the structure
- Do tedious mechanical work (checking all cases of a formula, renaming things consistently)
  without making the transcription errors a human would make

What it cannot do:
- Notice when a mathematical argument is wrong on its own terms (it may reproduce
  the error confidently)
- Supply physical intuition or mathematical taste
- Know when it is out of its depth (it will not tell you unprompted)
- Remember anything reliably between sessions without explicit help

The workflow described in this guide is designed to make the "capable junior assistant"
model actually work in practice: it keeps Claude well-informed about your project,
tells it precisely what to do, and keeps you in control of all decisions that matter.

---

# Part II: The core workflow

*The heart of the guide: how to organise a long research project so that every
Claude session is productive. This part is for everyone — but you do not need to
read it all on day one. Start working, and come back to each topic as it becomes
relevant.*

## CLAUDE.md: the most important file

### What it is

`CLAUDE.md` is a plain text file that lives at the root of your project directory.
Claude Code reads it automatically at the start of every session, before you type
anything. It is the primary way you communicate standing instructions, context,
and conventions to Claude.

Every session, Claude starts with no memory of previous sessions. Without CLAUDE.md,
you spend the first 20 minutes of every session re-explaining your project. With a
good CLAUDE.md, Claude starts the session already knowing:

- What the project is and what you are trying to achieve
- The notation and conventions you use
- Where everything is and which file is authoritative
- What has been established and what is still open
- Exactly what to do next
- How you want it to behave (chat style, writing style, what tools to use)

A good CLAUDE.md is the difference between a session that is productive from the
first message and one that wastes half an hour on orientation.

### Why it is the most important file

Every other practice in this guide — `brief.tex`, the session log, the
skills — feeds into the session through CLAUDE.md. If CLAUDE.md is wrong, incomplete,
or out of date, every session will be off. No amount of clever tooling fixes a bad
CLAUDE.md.

Conversely, a well-maintained CLAUDE.md is so effective that experienced Claude Code
users often say it is the one practice that most clearly separates productive from
unproductive research workflows.

### What to put in it

A CLAUDE.md for a research project should contain the following sections.

---

#### 1. Project goal

One or two paragraphs. What is this project? What is the mathematical or scientific
object you are studying? What is the open question you are working toward?

Be precise. Not "I am studying Eisenstein series" but "I am computing the regularised
integral of a product of four Eisenstein series over the modular fundamental domain
as a function of their spectral parameters, using the Rankin–Selberg method." The
more specific you are, the more accurately Claude understands the scope of the project
and can judge whether something is relevant.

---

#### 2. File map

A list of every file or directory Claude needs to know about, with one sentence each
explaining what it is and what it is for. Explicitly say which file is authoritative.

Example:
```
- brief.tex — 20-page self-contained reference; READ FIRST in every new session.
  Contains all current results, key formulas, and open problems. No proofs.
- workbook.tex — the full working record (~100–300 pages). Every proof, derivation,
  failed attempt, and discussion goes here in complete detail. Too large to read in
  full — grep or use section labels.
- next-session-prompts.md — task log. Top = next task; bottom = DONE log.
- numerics/ — computation scripts. numerics/README.md explains each file.
```

---

#### 3. Conventions

The exact notation and conventions Claude must get right. This is critical for
mathematical and physics projects, where a sign error or wrong normalisation
is not a style issue but a factual error.

Include:
- Definitions of every symbol that appears in your calculations
- Which normalisation convention you use (there are often several in the literature)
- Sign conventions
- Which branch of a function you take
- Any non-standard notation

Example:
```
- ξ(s) = π^{-s/2} Γ(s/2) ζ(s). Functional equation: ξ(s) = ξ(1-s).
  Simple poles at s=0 (residue -1) and s=1 (residue +1).
- E*_s = ξ(2s) E(z,s) is the completed Eisenstein series. NOT the same as E(z,s).
  Simple poles at s=0,1 with residues ∓1/2.
- M_3(μ_0,μ_1,μ_2,μ_3) = the depth-three Mellin transform. The variable s = μ_0
  is the Mellin variable; μ_1,μ_2,μ_3 are the spectral parameters of the three
  Eisenstein factors.
- ∏ξ always means ∏_{i=0}^3 ξ(2μ_i).
```

Do not assume Claude knows what your symbols mean "from context." Write the conventions
explicitly every time.

---

#### 4. Current status

A short, honest summary of where the project is right now. Not history — current state.
One screenful. This is the section you update most often.

It should answer:
- What has been established (what is rigorous and complete)?
- What is the most recent result?
- What is the exact next step?

Example structure:
```
## Current status

**Last result (2026-06-04):** The discrete Maass block D was observed directly
at (μ_0,μ_1,μ_2,μ_3) = (12,2,2,2). Residual R = M_3 − 2(½∏ξ·ΣΞ + ½∏ξ·C_cont)
= 2.64e-9 agrees with ∏ξ·D to 0.014% with no free parameters (L-values from LMFDB).

**Established:**
- All 8 boundary residues Res_{μ_i=1} = +½Z, Res_{μ_i=0} = -½Z (theorem)
- All 16 interior pole hyperplanes identified (pinch analysis)
- Interior residue formula R_σ = -∏ξ(2μ_i - [σ_i=-1]) (numerically validated at 3 tuples)
- M_3 is NOT a Langlands-Shahidi ratio (E ≠ 0 confirmed)

**Open:**
- Deep DK-derivation sections need the κ=1 factor-2 audit (~90 instances)

**Next step:** See next-session-prompts.md Prompt A.
```

---

#### 5. Chat formatting

Tell Claude explicitly how you want math written in chat. This matters because
Claude Code's chat interface does not render LaTeX. If Claude writes
`$\xi(s) = \pi^{-s/2}\Gamma(s/2)\zeta(s)$` in a chat reply, you see raw LaTeX,
not a formula.

The standard instruction:
```
## Chat formatting (NON-NEGOTIABLE)
In chat replies, do NOT use LaTeX markup ($...$, \frac{}{}, \xi, \Gamma, etc.).
Write math in plain Unicode: ξ, μ, Γ, ζ, ∑, ∏, ∫, √, ½, →, ≈, ≤, ⇒.
Single-character subscripts and superscripts: use Unicode — M₃, μ₀, sᵢ, x², yⁿ.
Multi-character sub/superscripts: use underscore/caret notation — M_{ab}, e^{-π t}, τ^{-2}.
LaTeX belongs ONLY inside .tex files.
```

Mark this as NON-NEGOTIABLE. Without this instruction, Claude will revert to LaTeX
in chat after a few exchanges.

---

#### 6. Open tasks

The current ranked list of things to do. This section is what Claude looks at to
decide what to work on next when you say "continue" or "pick up where we left off."

Keep it short — two or three items. The full task log lives in `next-session-prompts.md`.
This section is just the top of the queue.

---

#### 7. Skills

List every skill you have defined and what it does. See the [Skills section](#skills-reusable-procedures)
below for what skills are. A one-line description per skill is enough here.

Example:
```
## Skills
- /latex-compile — compile workbook.tex or brief.tex, fix errors and overfull boxes.
- /sync-brief — propagate new results from workbook.tex to brief.tex.
- /verify-residue — check a specific residue computation against the formula.
```

---

#### 8. Writing style for your workbook.tex

If Claude is helping you write or edit your workbook.tex, tell it explicitly what
level of detail you expect. Researchers have very different preferences, and Claude's
default is far too terse for most mathematical writing.

Example (verbose style):
```
## Writing style in workbook.tex (NON-NEGOTIABLE)
workbook.tex is the authoritative, comprehensive record. Show every step of every
calculation. State each substitution, each application of the functional equation,
each sign and factor-of-two choice — explicitly, in its own sentence. Never collapse
a multi-step manipulation into "one finds" or "a short computation gives." If in
doubt, over-explain. A reader must be able to reconstruct every result from workbook.tex
alone, with no external notes and no gaps.
```

If you prefer concise theorem-proof style instead, say that. The point is to say
something explicit rather than leaving it to Claude's default.

---

#### 9. Numerics configuration

If you run computations, tell Claude the setup:
```
## Numerics
- Primary engine: Python + mpmath (arbitrary precision)
- Precision: mp.dps = 30 unless stated otherwise
- venv: numerics/venv/ — run as numerics/venv/bin/python numerics/script.py
- Route long-running output to: numerics/run.log
- Mathematica (wolframscript): for symbolic verification only, not primary
```

---

#### 10. Git configuration

Tell Claude your exact remote setup:
```
## Git
- Remote 'github': https://github.com/YOUR_USER/YOUR_REPO.git (primary, main tracks it)
- Remote 'gitlab': git@git.YOUR_INSTITUTION.ac.uk:YOUR_ID/YOUR_REPO.git (institution mirror)
- Push: git push github main (hook auto-mirrors to gitlab)
- Commit author: YOUR_NAME <your-email>
- No Co-Authored-By trailers in commits.
```

Without this, Claude will push to the wrong remote or use the wrong identity.

---

### What NOT to put in CLAUDE.md

**Not a logbook.** CLAUDE.md is a current-state snapshot, not a history. When a
task is done, move it to the DONE log in `next-session-prompts.md`. When a status
changes, update the section in place — do not append a new dated block. Appended
blocks accumulate, CLAUDE.md grows, Claude reads old states as if they were current,
and sessions degrade.

**Not a full exposition.** CLAUDE.md should be navigable in one or two screenfuls
per section. Detailed content belongs in your brief.tex (see below).
CLAUDE.md points Claude to brief.tex; it does not replace it.

**Not speculative or in-progress work.** Only write what is established. In-progress
calculations belong in `next-session-prompts.md`. A CLAUDE.md that says something is
established when it is not will cause Claude to treat it as proven and build on it.

---

### How to maintain CLAUDE.md

The most important habit: **update the "Current status" and "Open tasks" sections
before ending every session.** This takes five minutes and saves thirty minutes of
re-orientation next session.

Before closing Claude Code:
- Change "last result" to what you just found
- Move completed items out of "Open tasks" to the DONE log in `next-session-prompts.md`
- Write the next open task clearly

If you forget to do this, the next session starts from the wrong state. If this
happens repeatedly, sessions become progressively less useful.

The pre-compact hook (see [Settings and hooks](#settings-and-hooks)) automatically
stamps CLAUDE.md with a timestamp when the context window fills up, so you can
see exactly when a compaction happened and use `next-session-prompts.md` to re-orient.

---

### Common CLAUDE.md mistakes

**Too long.** If CLAUDE.md is more than 5–6 screenfuls, Claude spends too much
context on it. Move detailed exposition to brief.tex. Keep CLAUDE.md
as a navigation index and current-status snapshot.

**Not updated.** A CLAUDE.md that has not been updated for a week is misleading.
Claude will work from the old state as if it were current.

**Wrong status.** Marking something as established when it is only conjectured, or
missing a correction to an earlier result. Claude will confidently build on wrong premises.

**No conventions section.** Without conventions, Claude will guess what your symbols
mean. It will often guess wrong in exactly the way that is hardest to catch — a
plausible-looking sign or normalisation error.

**Instructions given once and forgotten.** Things like "write math in plain Unicode
in chat" or "show every step in workbook.tex" need to be in CLAUDE.md permanently, not
said once in conversation. Claude does not remember conversation instructions between
sessions.

---

### When one CLAUDE.md isn't enough: nested files

A single `CLAUDE.md` at the project root is right for almost every project. But
once a project grows several sub-projects deep — each with its own conventions,
its own equations, its own "don't work on this here" rules — putting all of that
in the root file makes it long, and you pay for every line in *every* session,
even when you are working somewhere those rules do not apply.

Claude Code loads memory **hierarchically**. The root `CLAUDE.md` loads at the
start of every session. A `CLAUDE.md` placed *inside* a sub-directory is pulled
in **on demand** — only when Claude actually reads or edits files in that subtree.
So you can push branch-specific context down next to the branch it describes, and
it enters the context window only when it is relevant.

The two compose rather than clash: root = the whole-project base; nested = an
additive refinement scoped to one branch. Open the nested file by stating that
relationship explicitly, so the two never look contradictory:

```markdown
# <Branch> — local context for Claude

Branch-specific notes. The project-root CLAUDE.md (N folders up) still applies;
this file only adds what is special about this branch.

## What this branch is
...
## Where files go (mirror of the root file layout)
...
## Flags and gotchas special to this branch
...
```

If two levels ever genuinely conflict, the more specific (deeper) file governs
its own subtree. Run `/memory` at any time to see exactly which `CLAUDE.md` files
are currently loaded. The payoff is token economy: a branch's own sign
convention, its branch-only citations, or a local file-placement rule stays out
of context during unrelated work and appears exactly when you touch that branch.

---

### Status vs. changelog: keep the always-loaded file lean

`CLAUDE.md` is re-read at the start of every session, so every line in it is a
recurring cost — and on a long project the "Current status" section is where
bloat creeps in. Each finished result is tempting to leave in place as a paragraph
with its scripts, its data files, its little proof sketch. Do that for a few
months and the status section becomes a dated log of everything you have ever
done: dozens of screenfuls that bury the actual instructions and cost tokens
every session.

That dated log is worth keeping — but it is a **changelog**, not a status.
Split them:

- **`CLAUDE.md` → "Current status"** is a *snapshot*: for each branch, the
  headline DONE results and the current OPEN frontier. A handful of lines per
  branch, no dates.
- **The dated log** — the full "what landed when, with which script and which
  data file" — lives in the durable history file: the DONE log in
  `next-session-prompts.md` for most projects, or a dedicated `CHANGELOG.md` at
  the project root once that history gets long.

Rule of thumb: **if a status line has a date in it, it belongs in the dated log,
not in `CLAUDE.md`.** Condensing a status section that has grown to dozens of
paragraphs down to a per-branch snapshot can cut the always-loaded status content
by an order of magnitude while losing nothing — the detail just moves to where it
is read on demand instead of every session.

A snapshot template for a multi-branch project:

```markdown
## Current status

> Full dated log lives in the DONE log / CHANGELOG.md. Below is a snapshot of
> where each branch stands. When a result lands, append to the dated log; when a
> branch's DONE/OPEN frontier moves, refresh this snapshot.

**<Branch A>**
- DONE: <headline results, terse>
- OPEN: <the current frontier / what is next>
```

---

#### The research changelog: one row per result

Once the dated log outgrows the DONE log at the bottom of
`next-session-prompts.md`, give it its own file: `CHANGELOG.md` at the project
root. Not a software release changelog — a **research changelog**: the project's
long-term memory of *results*, where `next-session-prompts.md` is the memory of
*sessions*. Template: [`starter/CHANGELOG.md`](starter/CHANGELOG.md).

The format that works is a table, one row per result, grouped by branch:

| Item | Status |
|------|--------|
| *the claim, not the activity* | `DONE` / `IN PROGRESS` / `OPEN` / `FALSIFIED` / `SUPERSEDED` / `MOVED OUT`, then the payload |

and each row's payload carries the same five things every time:

- **the date**,
- **where it is written up** — the `workbook.tex` section *label*, not a page number,
- **which script produced it**, by path,
- **which data file holds the output**,
- **the honest residue** — what this result did *not* settle: the case still
  assumed, the range not covered, the step verified numerically rather than proved.

Close substantial rows with a **`Docs synced:`** line naming the other documents
you updated — `brief.tex`, `bigPicture.tex`, the strategy map, the `CLAUDE.md`
snapshot. When that line is missing, the doc set has usually drifted.

**Write the failures down.** `FALSIFIED` rows — the route that looked right and
broke at order four, the identity that failed at the first non-trivial case — are
the highest-value rows in the file. They are the only thing that stops you, a
collaborator, or Claude from cheerfully re-running a dead end six weeks later.
Record what broke, concretely, and what weaker statement survives.

**Why it pays even though it is never loaded into context.** `CLAUDE.md` gets read
every session; this file gets read on demand — which is exactly the point. It is
an *index into the project*: one `grep` for a symbol, a method, or a filename
returns the section label, the script, and the data file for every result that
touched it. A few hundred tokens instead of opening a hundred-page workbook. So
write rows so that grep works — put the searchable names *in* the row rather than
gesturing at "the usual script".

**How it starts.** Not on day one, and not as an empty file. It is born the day
your `CLAUDE.md` status section or DONE log has become a wall of dated paragraphs:
you *move* that content into `CHANGELOG.md` and replace it with a per-branch
snapshot. From then on the rule is two-way — append here when a result lands,
refresh the snapshot in `CLAUDE.md` when a branch's DONE/OPEN *frontier* moves.
Expect to re-condense: the snapshot quietly re-bloats as dated entries creep back
in, and the fix is the same move each time.

---

### Convention hygiene: pin decisions so they don't drift

Some decisions are easy to make once and then silently violate: a file rename, a
citation key, how a collaborator's name is spelled, which repo a file belongs in.
When the decision and the files drift apart you get dead cross-references, links
that break in a preview, and — worst for Claude — confident pointers at files that
no longer exist.

The fix is cheap: keep a short **conventions** block in `CLAUDE.md`, and
*maintain* it the moment a decision changes. Record the things that are easy to
get wrong as one-line rules:

- **File renames.** If `workbook.tex` becomes `workbookAlice.tex`, say so — and
  fix every stale reference in the same edit, or the old name lingers in prose
  and Claude follows it.
- **Citation keys.** "The cite key stays `Author:2021abc` even though we write the
  name out in full in prose."
- **Naming.** "The collaborator's name is spelled *X*, not *Y*" — so Claude stops
  guessing and getting it wrong in exactly the way that is hardest to notice.
- **File placement across repos** — see the multi-repo rule under
  [Git workflow for academics](#git-workflow-for-academics).

A maintained conventions block is far cheaper than the confusion it prevents. The
failure it heads off is the nasty kind: not a crash, but a plausible-looking
reference to something that has quietly moved.

---

## The dual-document pattern: workbook.tex and brief.tex

### The problem

Mathematical and physics research projects involve long documents. A paper draft,
after a few months of work, might be 150 to 300 pages. Claude Code has a finite
context window. When your workbook.tex exceeds what fits in context, something
breaks: Claude can no longer read the whole document, and sessions begin to
degrade — Claude forgets earlier results, contradicts itself, misses constraints
that were established weeks ago.

You cannot solve this by making Claude read the document in pieces each session.
That takes too long and the pieces do not form a coherent picture. And you cannot
solve it by making CLAUDE.md longer — a CLAUDE.md that attempts to summarise a
200-page paper is itself too long and misses exactly the details that matter.

### The solution: two documents with different purposes

Maintain two documents in parallel:

**The workbook** (`workbook.tex`) is your full, detailed working record — a research
journal in LaTeX. Everything goes here: proofs, derivations, failed attempts,
discussions, corrections, numerical experiments, and your thinking as it develops.
This document is deliberately verbose. It is **not** a paper draft and **not** what
you submit for publication — it is the place where you work things out in writing,
for a reader (you, months later, or Claude) who wants to see every step. Claude does
not read it in full each session — it is too long. Instead, Claude navigates it with
`grep` and targeted reads when it needs a specific equation or section.

**The brief** (`brief.tex`) is a short (15–30 pages / 1000–3000 lines)
self-contained reference. It contains the current state of the project: what is
established, what the key formulas are, what is open, and where to find things in
`workbook.tex`. It contains no proofs, no derivations, no history. Claude reads it
at the start of new sessions as the primary orientation source. Because it states
results cleanly without the working-out, `brief.tex` — not `workbook.tex` — is the
document closest to an eventual published paper.

`brief.tex` acts as a compressed session memory. When `workbook.tex` has grown
beyond what fits in context, Claude reads `brief.tex` and stays accurately oriented.

### Collaborative projects: naming workbooks by author

For collaborative projects with multiple contributors, consider naming each person's
workbook by their name (e.g., `workbookAlice.tex`, `workbookBob.tex`) instead of a
shared `workbook.tex`. Benefits:

- **Ownership clarity**: Each proof and derivation is explicitly attributed without
  needing `git blame`. When Claude sees `workbookAlice.tex` has a new theorem, it knows
  Alice worked on that section.
- **Fewer merge conflicts**: Each person has their own file. Parallel work on separate
  results does not require merging textual changes.
- **Natural aggregation**: Everyone pulls from their personal workbook into a shared
  `brief.tex`, which becomes the canonical record of established results. The brief
  is where you reconcile and publish consolidated findings.

Each author maintains their own comprehensive workbook; `brief.tex` serves as the
project's integrated reference.

### What to put in workbook.tex

Everything. `workbook.tex` is the authoritative record, and "authoritative"
means complete. There are no results too numerical or too routine to include in full.
If a calculation was worth doing, it is worth recording in full detail.

Specifically:
- Every theorem and proposition with a complete proof
- Every formula with the full derivation shown step by step
- Every numerical result: what was computed, the method, the precision, the validation,
  and any caveats
- Every correction: if you found an error and fixed it, the corrected statement and
  an explicit note that the old version was wrong
- Every failed attempt that taught you something, with an explanation of why it failed

The reason for this completeness is practical, not pedantic. A result you "know"
but did not write down will be forgotten when the context rolls over. The main
document is what survives.

### Structuring workbook.tex so Claude can navigate it

Claude does not read `workbook.tex` from top to bottom each session. It navigates
with `grep` and targeted reads, jumping to whatever section is relevant right now.
Two things make this work or fail:

**Cross-references.** Use `\label` and `\ref` (or `\eqref`) liberally — more than
you would for human readers. Every theorem, equation, section, and subsection
should be labelled, and results should refer to each other explicitly. When Claude
reads Section 4 and needs to know what Proposition 2.3 says, a cross-reference
tells it where to look. Without them, Claude either guesses or misses the
connection entirely.

**Section structure.** Flat documents — everything in one or two large sections —
are hard for Claude to navigate. A clear, deep hierarchy (sections → subsections →
subsubsections, with meaningful names) lets Claude find the right part of the
document without reading everything around it.

**Why it pays off: token economy.** Every line Claude reads to *find* something is
context spent. A labelled result it can jump to with a single targeted read costs a
fraction of scanning the surrounding pages — so dense `\label`s and a deep hierarchy
are not just navigation aids: they make each session cheaper and let Claude survey a
large workbook to pull exactly what it needs, without burning its context window on
the search.

Both of these are also just good LaTeX practice. They cost almost nothing when you
write them and save significant friction later.

### Make the workbook self-teaching: crash-course appendices

A research workbook accumulates specialist vocabulary fast — every new technique
brings its own definitions, and six months in, half the file is written in a
language only present-you speaks fluently. When a returning human, or a fresh
Claude session, hits that vocabulary cold, it has to reconstruct the meaning from
scattered sources before it can do anything useful.

The cure is to make the workbook **self-teaching**: carry a set of short
lecture-note appendices — crash courses — that define every piece of machinery the
body relies on, and cross-reference them. Each body section that leans on a
technique points at the crash course for it ("see Appendix B for the definition of
the transform used here"), so a reader can learn the machinery from the same file
that uses it, without leaving to hunt through papers.

This costs a little discipline and pays back twice: you (six months later) and
Claude (cold) both get a document that explains itself. It also keeps the overview
document (below) clean — jargon is defined once, in the workbook, not smeared
across every tier.

---

### Corrections must replace, not append

This is a non-negotiable rule: if you discover that something in `workbook.tex` is
wrong, **correct it in place**. Do not write a new paragraph further on saying
"earlier I claimed X but actually Y." Delete or replace the wrong content.

The reason is specific to how Claude uses the document. Claude reads different parts
of `workbook.tex` in different sessions — it does not read everything. If the wrong
version stays in the file and the correction is only a few pages later, there is a
real risk that Claude reads the wrong statement in a future session and never
encounters the correction. It will then work from incorrect information, confidently.

In-place corrections also produce a cleaner document for human readers. There is
no legitimate reason to keep wrong content in an authoritative record.

### What to put in brief.tex

Only what is established and currently relevant. The brief.tex is a snapshot
of the current state of knowledge about the project, compressed to what is essential.

**Include:**
- Every established theorem and proposition, stated precisely (without proof)
- Every key formula, with the exact normalizations and signs you use
- A cross-reference to workbook.tex for each result (section label or equation name)
  so Claude can navigate there when it needs the derivation
- The current status: what is proved, what is conjectured, what is open
- Open problems, ranked by importance
- A concise conventions section
- Recent corrections (the corrected statement, clearly marked as corrected)

**Exclude:**
- Proofs and derivations
- Pedagogical examples and motivation
- History (how you arrived at results, what you tried first)
- In-progress or speculative work
- Anything that is not yet established

### How to structure brief.tex

A structure that works well:

```
§1  Abstract / main results
    The 2–3 key theorems stated precisely. Someone reading only this
    section should know what the project has established.

§2  Conventions and definitions
    Every symbol defined, with the exact normalisation used.
    This section prevents Claude from guessing.

§3–N  Results by topic
    One section per topic. Theorem statement, key formula,
    cross-reference to workbook.tex.
    Mark each result: ESTABLISHED / CONJECTURED / OPEN.

§N+1  Numerical results
    Exact computed values, method used, what was validated.

§N+2  Open problems
    Ranked list. "Item 1 is the next thing to prove."
```

### The sync discipline

The brief.tex and workbook.tex will drift apart unless you actively
maintain them. Two situations require a sync:

**After a new result is established:** Add the theorem statement (not the proof) to
the brief.tex. Update the status of related open problems. This takes five
minutes and saves the result from being lost in workbook.tex.

**After a correction:** If you find that something in brief.tex is wrong,
fix it immediately. A wrong brief.tex is worse than no brief.tex —
Claude will confidently work from incorrect information.

The `/sync-brief` skill in this repository automates part of this: it classifies
which changes in workbook.tex are "load-bearing" (new theorems, corrected formulas)
and prompts you to propagate them.

### What "load-bearing" means

Not every change to workbook.tex needs to go into brief.tex.

**Propagate to brief.tex:**
- A new theorem or proposition (statement only)
- A corrected formula (sign, factor, argument — whatever changed)
- A result that changes the status of an open problem
- A new definition that other results depend on

**Do not propagate:**
- A new proof of an already-stated theorem
- A pedagogical re-derivation of an existing result
- A reorganisation or renaming that does not change content
- Footnotes, remarks, summary subsections

When in doubt, propagate. It is easier to trim an unnecessary update than to
recover a missing one.

### Common mistakes with the dual-document pattern

**The brief.tex grows.** When it exceeds 30 pages, it starts to function
like a smaller version of workbook.tex — still too large for an orienting read.
Prune it: collapse routine results into tables, remove historical context, cut anything
that is not load-bearing for future work.

**In-progress work ends up in brief.tex.** `brief.tex`
contains only what is established. When you are in the middle of a calculation, that
belongs in `next-session-prompts.md`, not in brief.tex.

**Syncing stops.** A brief.tex that is two months out of date is useless.
Treat syncing as part of the cost of every new result, not as a separate task.

**The brief.tex is not self-contained.** If someone (or Claude) reading
only brief.tex cannot understand what the project has established,
it is not doing its job. Every result should be understandable without reference
to workbook.tex, even if workbook.tex is where the proof lives.

**Corrections in workbook.tex are appended rather than replaced.** This is the most
dangerous mistake. If you write "earlier I said X, but actually Y" at the end of
a section, a later Claude session may read only the beginning of that section and
work from X, never seeing the correction. Wrong content must be replaced in place,
not annotated. See the section above on corrections.

---

### Scaling up: a big-picture overview as a third tier

The dual-document pattern (workbook + brief) is the right default. On a large
project it is worth adding one tier *above* the brief: a short, standalone
**overview** (`bigPicture.tex`, ~4–8 pages, equation-light) that is the thing to
read *first* — before the brief, before the workbook.

The reason is that even the brief is optimised for *precision*, not for a
five-minute orientation. A newcomer — a collaborator, or a fresh Claude session —
needs the *shape* of the project first: what the goal is, the one organising idea
everything hangs on, what follows from it, and an honest sense of where things
stand. The overview states exactly that and nothing more; for every claim it
points to the workbook `\S`/`eq.` rather than reproducing the derivation. The
reading order becomes:

> **overview** (the shape, in five minutes) → **brief** (the current results,
> stated cleanly) → **workbook** (the full derivations, navigated by `grep`).

The most valuable part of the overview is a **status ledger** — a single
glanceable box, split by epistemic status (proven / numerically known / open) —
that answers "where are we?" at a glance. That ledger is only useful if it is
honest and current, which ties directly into
[Make epistemic status explicit](#make-epistemic-status-explicit-a-trust-ledger)
in Part IV: keep it in sync in the *same commit* as the workbook result it
summarises, and quote the workbook's **real** section titles in the pointers — a
plausible-but-invented section name is worse than no pointer, and is a common
failure when a weaker model drafts the overview.

The starter package ships a [`bigPicture.tex`](starter/bigPicture.tex) template
with the two ledger box styles ready to fill in.

---

## Session continuity: next-session-prompts.md

### The problem

Even with a well-maintained CLAUDE.md and brief.tex, there is
context that lives only in the conversation — the details of what you just tried,
why a particular approach failed, what the next micro-step is. This context does
not survive between sessions. A new session starts without it.

The consequence is a common, frustrating experience: you end a session knowing
exactly what to do next, then start the next session and spend 20 minutes
reconstructing where you were.

### The solution: a human-maintained session log

`next-session-prompts.md` is a file you maintain by hand. It has two sections:

**The current task queue** (top of the file): one to three self-contained task
descriptions, written well enough that you could paste one into a new Claude session
and have Claude understand exactly what to do. Each task should include:
- What you are trying to do and why it matters
- What is already known (so Claude does not re-derive it)
- The specific instruction: which file, which section, which formula, what to change
- What success looks like (a number, a passing test, a compiled document, a sentence written)

**The DONE log** (bottom of the file): a timestamped record of completed tasks,
with results and any caveats. This is the durable history of the project. CLAUDE.md
is the current-state snapshot; the DONE log is the record of how you got there.

### Why this works better than relying on Claude's memory

Claude Code has an auto-memory system. It saves facts between sessions (conventions,
preferences, who you are). This is useful for stable information. It is not useful
for in-flight research state — what you just tried, why it failed, what the next
step is.

The auto-memory system does not know the difference between "I established this
formula" and "I am currently trying to prove this formula." `next-session-prompts.md`
does, because you write it.

The other reason: when you write a task description carefully enough to hand it to
Claude, you often clarify your own thinking in the process. The discipline of writing
"here is what I want to do, here is why, here is what success looks like" is valuable
independently of Claude.

### Writing a good task description

The quality of the task description determines the quality of the next session.

A bad task description is vague:

> "Work on the boundary residue calculation."

Claude does not know which boundary, which residue, what the current state is, or
what you want to produce.

A good task description is self-contained:

> **Context:** We are verifying the formula R_σ = -∏ξ(2μ_i - [σ_i = -1]) for the
> interior pole residues of M_3. We have checked it for the n_- = 1 representative
> at three integer tuples and it passes to ratio 1.0003.
>
> **What to do:** Check the formula for the n_- = 2 representative at the integer
> point (μ_0,μ_1,μ_2,μ_3) = (5,4,3,2). This should give Res = -ξ(9)ξ(7)ξ(5)ξ(3).
> Write the residue extraction script in numerics/residue_n2.py following the
> pattern of residue_general.py.
>
> **Success:** The computed ratio (numerical residue)/(formula value) is within
> 0.1% of 1.0.

Someone reading this description — Claude, or you three months from now — knows
exactly what to do and how to check that it is done correctly.

### The DONE log

Every completed task gets a brief entry at the bottom of the file:

```
### 2026-06-04 — Interior residue R_σ: n_-=1 check
Result: Ratio 1.0003 at three tuples (4,2,2,2), (5,2,2,3), (6,2,2,4).
Files changed: numerics/residue_general.py, workbook.tex sec:numStrategy:ansatzCheck
Notes: n_-=1 residue validated; other 15 hyperplanes follow by G_3 symmetry.
```

The DONE log is the long-term record. When you need to explain what your project
established and in what order, the DONE log is where that history lives.

On a long project it will outgrow this file. When it does, graduate it to a
dedicated `CHANGELOG.md` — see
[The research changelog](#the-research-changelog-one-row-per-result). The two are
not the same artifact: the DONE log is *chronological, per session* ("what did I
finish on Tuesday"), while the research changelog is *an index, per result*
("everything we know about the residue formula, with its script and its
limitation"). Start with the DONE log; move to the changelog when you find
yourself scrolling to answer "did we already check this?".

---

### Strategy maps: planning the route, not just the next task

`next-session-prompts.md` answers *what do I do next*. It does not answer *what is
the overall plan to get from here to the goal, and which routes have already been
tried and ruled out*. For a multi-month proof or analysis you want that map
written down too.

A **strategy map** is a short file (one per active branch, e.g.
`topic-a-strategy.md`) that lays out the research route as a set of named, ordered
strategies — A, B, C — each a multi-step plan toward one sub-goal, with a
recommended order, a status, and cross-references. It is the *strategy*; the
session log is the *next action*. Writing it down does three things: it stops you
re-attempting dead ends (record the falsified detours), it makes the dependency
structure between sub-goals explicit, and it lets a fresh session pick up a *plan*
rather than just a task. It applies to analytic work, proofs, and write-ups — not
only to code.

```markdown
# <Branch> — strategy map (route plan)

Recommended order: A → C → E  (B, D optional / parallel).

## Strategy A — <sub-goal>
Idea: <one line>.  Status: <done / in progress / blocked on X>.
1. <step> — <script or workbook section> — <result or "open">
2. ...
Falsified detours: <what was tried and ruled out, so nobody repeats it>
```

Keep a short **honesty ledger** at the foot of the file — a blunt list of what is
proven versus merely checked (see
[Make epistemic status explicit](#make-epistemic-status-explicit-a-trust-ledger)).
When a strategy completes, fold its result into the dated log and the overview's
status ledger. The starter ships a [`strategy-map.md`](starter/strategy-map.md)
template.

> **Not to be confused with the [pipeline workflow](#the-pipeline-workflow-keep-claude-fluent-in-your-own-code)**
> in Part III, which documents a large *code*. A strategy map plans the *research*;
> a pipeline doc maps a *program*. A big project may want both.

---

### Memory: what to keep re-teaching Claude vs. what goes in CLAUDE.md

Claude Code has a built-in **memory** system: a small store of notes it carries
between sessions, separate from `CLAUDE.md`. The two are for different things, and
keeping them separate is what keeps `CLAUDE.md` lean.

- **`CLAUDE.md`** is for the whole project / whole team: the goal, the file map,
  the conventions, the standing rules. It loads in full every session.
- **Memory** is for the things you find yourself *re-teaching* Claude across
  sessions — a package's quirk, a recurring numerics trap, "this file was
  renamed", how a collaborator's name is spelled. These are recalled by relevance,
  so you do not pay for all of them at once.

A durable way to run memory is **one fact per file**, each with a little
front-matter tag, indexed by a one-line-per-entry `MEMORY.md`. Tag each note by
type: `user` (who the researcher is, preferences), `feedback` (a correction or a
confirmed working practice — *with the why*), `project` (state or goals not
derivable from the code), `reference` (a pointer to a tool, package, or external
resource).

```markdown
---
name: convolution-precision-trap
description: why the naive convolution loses digits here; use the stable form
metadata:
  type: reference
---

<the one fact, stated plainly>. Related: [[other-note-name]].
```

with a pointer line in `MEMORY.md`:
`- [Convolution precision trap](convolution-precision-trap.md) — use the stable form`.
Link related notes with `[[name]]`. Before saving, check for an existing note that
already covers it — update it rather than adding a duplicate; and delete a note the
moment it turns out to be wrong. Do not store what the repo already records (code
structure, git history, results that live in the workbook): memory is for the
things that are true but *not written down anywhere Claude will re-read*.

---

## BUGS.md: the recurring-mistake registry

### The problem: the expensive failures do not crash

A bug that raises an error costs you ten minutes. The bugs that cost days are the
ones that hand back a **plausible number with no error at all** — a pattern that
matched nothing and so "changed nothing", a control that could not have failed, a
convention imported from a paper that computes beautifully and answers a different
question. These do not look like bugs. They look like results.

Two things make them worse in an AI-assisted project. They **recur**: the same
class of mistake comes back in a new disguise months later, and neither you nor
Claude remembers the first time. And they are **invisible to review**: the code
reads fine, the run is clean, the output is a number of the right size.

### The solution: one file, read before any code is written

`BUGS.md` is a registry of every class of mistake the project has hit, each as one
short **symptom → cause → guard** entry, organised by failure mode. It sits at the
project root next to the trinity, and it carries a standing rule at the top:

> **Before writing or editing any code, read this file first** and confirm the
> change does not repeat a mistake below. After hitting a NEW class of bug, add it
> here in the same turn you fix it.

The unit is the **class**, not the incident. "The run on 3 June gave the wrong
normalisation" is a logbook entry. "A formula imported from a paper carries the
paper's conventions, so gate it against something this project measured
independently" is a registry entry — it will fire again, on a different paper, in
a different section, next year.

A worked entry, in the shape they all take:

```markdown
- 🔴⚠ **A rewrite rule that matches nothing returns the input unchanged.**
  Symptom: a normalisation step "succeeds" and the expression is untouched, so the
  next stage silently works on un-normalised input. Cause: the pattern was written
  for the pre-expansion form and never fires after expansion.
  **Guard: assert the rewrite fired** — compare a term count before and after, and
  abort if the expression is identical. (workbook §sec:norm; CHANGELOG 2026-06-03.)
```

Bold the guard. The guard is the reusable part; the symptom is only there so a
future session recognises the shape.

### The legend, and why the counter matters

Three marks, at the front of each entry:

| Mark | Meaning |
|------|---------|
| 🔴 | has bitten us **more than once** |
| ⚠ | **silent** — produced a confident *wrong answer*, not an error |
| ✅ | has a **mechanical guard** (an assert that aborts, not a sentence you must remember) |

Promoting an entry from ⚠ to 🔴 the second time it bites is the point of the
counter: a 🔴 is a standing instruction to go build the ✅. That is the file's real
endgame — every entry that can be turned into an abort gate should be, and the
prose entry then stays as the explanation of *why* the gate exists and what it does
**not** cover.

### The two rules that pay for the whole file

Every version of this file I have seen converges on the same preamble, and it is
worth carrying in your head even without the file open:

1. **When two diagnostics in one run disagree, the bug is in a diagnostic, not in
   the science.** That disagreement is usually the *only* tell you get. The
   temptation is to trust the one that flatters the claim and debug the other.
2. **A control that cannot fail is worse than no control**, because it reads as
   confirmation. Before reporting a control as passing, ask what it could possibly
   have detected — and if the answer is "nothing", say **vacuous** out loud. Make
   that a word Claude is required to use.

The second one is the single highest-value line to put in `CLAUDE.md`, because it
is a rule about *reporting*, and reporting is exactly where an eager assistant
rounds "the test was empty" up to "the test passed".

### Add it in the same turn you fix it

This is the discipline that makes the file work, and it is the one that slips. A
trap written down a week later is written down wrong — the guard has been forgotten
and only the story survives. The rule is: the commit that fixes the bug also adds
the entry.

It grows faster than you would expect. In a project running this pattern the file
went from 279 lines to just over 400 in its first three days, across twelve commits
— each one the class of mistake that round had just hit. That is not a sign of a bad
project; it is a count of traps that will not be paid for twice.

### What does NOT go in it

- **Narratives.** The full story of an incident goes in `workbook.tex` and gets a
  `CHANGELOG.md` row; the entry links to them in one parenthesis. An entry with no
  guard is a story, and it will not survive being skimmed.
- **Open questions or to-dos.** Those belong in
  [`next-session-prompts.md`](#session-continuity-next-session-promptsmd). A
  registry of mistakes is not an issue tracker: nothing here is ever "closed", and
  entries stay after they are fixed — the guard is the whole value.
- **A second copy of anything.** If a rule already lives in `CLAUDE.md` or a skill,
  point at it. Two copies drift, and the stale one gets believed.

### Wiring it in

Three lines of setup, and it is worth doing all three:

1. **A pointer in `CLAUDE.md`**, in the *Files* list, marked non-optional: "read
   `BUGS.md` before writing or editing any code."
2. **A place in the session-start order.** Both live projects put it third — after
   the status snapshot and the task queue, before any code is opened.
3. **A first step in code-heavy skills.** A skill that drives a long build can open
   with "read `BUGS.md`; if the failure you are seeing is not in it, stop and
   report" — which is also how new entries get noticed.

If a **second agent** works in the repo, keep the registry in one file both read and
say so at the top. This is the same one-source-of-truth rule as
[`AGENTS.md`](#using-both-claude-and-codex-on-one-project) — and it is why one
project *moved* its trap list out of the always-loaded instruction file into
`BUGS.md` entirely, leaving a pointer behind: the traps had grown to a substantial
fraction of a file that was being re-read, in full, at the start of every session by
both agents.

That relocation is the honest cost argument, too. `BUGS.md` is not free — it is
several hundred lines, and reading it before code work costs tokens every time. It
earns that by being read **on demand rather than always**, by staying a checklist
instead of a log, and by shrinking in effect over time as its 🔴 entries turn into
✅ gates. If your copy stops earning it, the fix is to promote entries into asserts,
not to stop reading it.

The template is [`starter/BUGS.md`](starter/BUGS.md) — the section skeleton, the
legend, the standing rule, and a small set of starting entries that are true in
almost any computational project.

---

## Claim discipline: name only what you computed

[`BUGS.md`](#bugsmd-the-recurring-mistake-registry) catches mistakes in a *calculation*.
This section is about the two mistakes that happen on either side of one: choosing which
case to test, and choosing what to call the result. Both are cheap to fix and expensive to
leave, and neither produces an error message.

### The two failure modes

**Escalating after a failure.** A mechanism is proposed for a whole family. It fails at the
smallest case. The next thing tried is a *bigger* one — a higher order, another parameter,
a richer ansatz — on the unstated hope that the missing structure will show up there. This
is the single most expensive pattern in agent-assisted research, because it converts a
five-minute counterexample into a fortnight of work, and every run along the way looks like
progress. It also has the wrong shape logically: a failure at the simplest admissible case
*is* a counterexample to a claim that was made about every case.

**Naming more than you computed.** The calculation is right; the noun is wrong. The code
built a leading term and the summary says "the operator". The code applied a sign flip
twice and the label says "an involution on the actual data". The number is correct in both,
and the sentence is not.

### The simple-case gate

Before computing: identify the **simplest admissible nondegenerate case**, and make the
*exact* proposal pass there before increasing anything. "Admissible" and "nondegenerate"
are doing real work — a case where the thing you are probing vanishes identically will pass
for free and tell you nothing.

If it fails, the rule is **stop escalating**: preserve the first exact residual and diagnose
it. Is it an implementation bug, a convention mismatch, a degenerate test, a false auxiliary
assumption, or the idea being wrong? Repair the proposal on that same case, or narrow the
claim. A modified proposal is a *new* proposal and restarts the gate.

The one legitimate escape is deriving the exclusion, not asserting it. "That case is
degenerate" is a fine reason to skip a case — if it follows from the domain you stated
before you ran the test. Said for the first time immediately after the case broke your
proposal, it is not a reason, it is a reflex.

The [`simple-case-gate`](starter/.claude/skills/simple-case-gate/SKILL.md) skill is the
workflow, and there is a matching non-negotiable block in
[`starter/CLAUDE.md`](starter/CLAUDE.md) so it applies without being invoked.

### The claim audit, and where a claim is actually minted

Here is the part worth internalising, because it tells you *where to intervene*.

An overclaim is not written in the summary. It is minted earlier, in the **label on a
check** — and the summary, the commit message, the changelog row and the workbook section
then all inherit that label, because they are written in the same pass, from the same
context, by the same process. By the time prose is being drafted, the claim is being
*copied*, not made. Auditing the summary audits the copy.

That has a structural consequence. If nobody reads the label against the body, the **first
adversarial reader of a result is whoever you send it to** — your collaborator, a referee,
or a second agent. Of course they find something; nothing upstream of them ever tested the
claim against a hostile reading. The fix is to do that read yourself, before the claim
leaves the session: **script passes → audit → prose**, never prose first.

The audit has one load-bearing step, the **computed-object ledger**. One row per headline
you intend to write, filled left to right:

| symbol **literally constructed in the code** | restriction actually established | headline as drafted |
|---|---|---|
| `L = A @ D` (leading term only) | leading order; no higher term exists in the file | ~~"the full operator is constructed"~~ |

The rule that does the work: **a noun in column 3 that does not appear in column 1 is
banned.** Writing the columns left to right is not a stylistic preference — writing column 3
first and reverse-engineering column 1 is exactly the failure being prevented.

Then, for every check, ask the question that makes labels honest: **what is the weakest
statement that makes this body pass?** Make *that* the label. Three things kill a check:

1. **It is true for every input of its type.** `M @ M.T` is symmetric for every `M`.
   `f(a) - f(a) == 0`. A determinant is nonzero on a matrix you assembled to be invertible.
   The test: substitute a random object of the same type. If it still passes, it says
   nothing about yours.
2. **It was evaluated where it cannot bite** — a degenerate case, a vanishing leading term,
   one sampled point standing in for a general statement.
3. **It tests your typing rather than the mathematics.** A value assigned by hand, with a
   later check confirming a consequence of it, holds because the algebra is consistent with
   your typing. Every hand-assignment is *assumed*; downstream checks say "consistent with
   the assumption", never "derived".

And the cheapest tell of all, which costs nothing to apply:

> **If you are writing a sentence explaining why a check is *not* trivial, the check is
> trivial.** That sentence is advocacy. It is generated by anticipating the objection, not
> by reading the body — which is why it tends to appear on the same line as the flaw it
> denies. Delete the defence and read the body.

### Label your checks, or there is nothing to audit

All of this needs your checks to carry labels. The change is small:

```python
def gate(label, ok):
    print(("PASS  " if ok else "FAIL  ") + label)
    return ok

gate("R vanishes at n=1 to 30 digits", abs(R) < 1e-30)
```

Five lines, and it buys three things. The check now has a written claim attached at the
moment you understood it, instead of a sentence invented later from memory. The label and
the body sit on the same line, so comparing them is possible at all. And a mechanical
pre-filter can read them:

```bash
bash .claude/skills/claim-audit/gate_audit.sh numerics/my_script.py
```

[`gate_audit.sh`](starter/.claude/skills/claim-audit/gate_audit.sh) reports four things:
values assigned by hand, labels over the length budget, advocacy language in labels, and
bodies whose *shape* may be true for every input. It reads both the `gate(...)` and
`gate[...]` forms, so Python, Julia and Wolfram all work.

Two honest limits. It is a **pre-filter, not a verdict** — it cannot read mathematics, and a
clean run means "no cheap tell fired", never "the labels are honest". And if it finds no
labelled checks it says so loudly and exits non-zero, rather than printing an all-clear on a
file it could not parse: a silent clean report is the one failure that would make a tool like
this worse than useless.

That second point generalises into a design rule worth stealing for your own tools. **A tool
whose output is mostly the word "none" needs a regression suite more than most code does**,
because a detector that quietly stops firing is indistinguishable from a clean input. Two real
bugs in this one make the case: a file containing no checks at all was once reported as a clean
run, and the helper's own *definition* (`gate[l_, c_] := ...`) was counted as a check, inflating
every number the tool had ever printed by one. Neither crashed. Both printed a plausible number.
So it ships with [`selftest.sh`](starter/.claude/skills/claim-audit/selftest.sh), where every
case asserts that a detector **fires** on input designed to trip it — the same "a control that
cannot fail is not a control" rule the skill applies to your research, turned on the tool
itself. Run it after any edit. Its section `[0]` also reconciles the checks it parsed against an
independent count of call sites, so a parser that silently *drops* checks is caught too, not
just one that finds none.

### The report shape, and one tag per claim

The report — a summary to you, a commit message, a changelog row, a message to another
agent — carries four things in order: **what was computed** (the ledger's column 1, with its
restrictions), **what that licenses**, **what it explicitly does not establish** (never
omitted, never softened to "further work will show"), and **which checks were vacuous**.

Each claim also carries a status, and being specific here is what stops a partial result
inflating into the thing it is not:

`definition` · `exact identity` · `proved theorem` · `conditional theorem` ·
`finite verification` · `numerical evidence` · `conjecture` · `obstruction`

The two easy ones to conflate are the middle pair. **Finite verification** is exact but
bounded — you checked every case in a stated finite range. **Numerical evidence** is
approximate — agreement to N digits at sampled points. Both are real evidence at their
stated range and neither is an all-cases claim; an all-cases claim needs a symbolic
identity, an induction, a uniqueness argument, or a cited theorem whose hypotheses you
checked. `obstruction` is worth its own slot because a proved negative is a genuine result
and tends to get filed as a failure.

This is the fine-grained version of the
[trust ledger](#make-epistemic-status-explicit-a-trust-ledger); the three-way tags in
`brief.tex` (ESTABLISHED / CONJECTURED / OPEN) and in the overview document are deliberate
*coarsenings* of it for documents that need to be skimmable. Keep the fine status with the
result in `workbook.tex` and let the summaries coarsen.

A last one, for projects where two agents or two people exchange results: **separate the
verdict from the new claim**. A line reading "confirmed, all corrections accepted — and this
round establishes X" lets an acceptance token launder a claim nobody has read. The
acceptance was real; X was not audited. Two claims, two lines. And never promote an accepted
correction into a stronger claim than the corrector made — "the obstacle is not where you
said" does not become "the obstacle is gone".

### Hand the audit to a context that does not know the story

Doing the audit yourself works, and it is most of the value. But you are auditing a claim
you just wrote, in the context that produced it, and the reasoning that generated the
overclaim is still in the window. For a result that would change what you do next, hand it
to a reader that has none of that.

The starter ships [`claim-auditor`](starter/.claude/agents/claim-auditor.md), a sub-agent
whose whole job is to say what the artifacts support. The instruction that makes it work is
about what you *withhold*:

> Give it the script, the log, and the drafted claim. Do **not** give it your reasoning,
> the story of how you got there, or what you hope is true.

Those are precisely what the audit is testing around. A fresh context handed the narrative
will reconstruct your conclusion from it, agree with you, and tell you nothing.

The second agent, [`round-planner`](starter/.claude/agents/round-planner.md), answers a
different question: *is this thread still moving?* Sessions are bad at noticing that they
have spent three rounds renaming the same residual, because every individual round looks
productive. Its mechanical test is to compare a tuple — target, simplest case in play, exact
residual, the step being established — against the previous round. If nothing in it changed
and no quantifier got stronger, it is a loop, however different the new code looks. It also
carries the loop signals worth knowing by name: escalating after the simple case failed,
replacing an exact failure with a looser test that cannot see the residual, reopening a
parked branch without resolving its blocker, and proposing a calculation where neither
outcome would change the strategy.

Run them in that order — audit the claim, then decide whether the round advanced anything —
and spawn several `claim-auditor`s in parallel on different axes when a claim is
load-bearing, since a single auditor can be captured by the framing of the question.

**One design detail worth copying into your own agents.** Both are declared
`tools: Read, Grep, Glob` — no `Bash`. A sub-agent that has `Bash` can write files through
the shell no matter what its prompt says, so "read-only" is a promise rather than a
property. Dropping `Bash` makes it a property, and it costs these two agents nothing: an
auditor that cannot launch a job is behaving correctly anyway. If yours genuinely needs to
run something, keep `Bash` and describe it honestly as read-mostly rather than read-only.

### Wiring it in

- Two skills: [`simple-case-gate`](starter/.claude/skills/simple-case-gate/SKILL.md)
  (before computing) and [`claim-audit`](starter/.claude/skills/claim-audit/SKILL.md)
  (after the script passes, before prose).
- Two non-negotiable blocks in [`starter/CLAUDE.md`](starter/CLAUDE.md) — *Simple-case gate*
  and *Research-claim discipline* — so the rules apply when nobody invokes a skill.
- Two sections in [`starter/BUGS.md`](starter/BUGS.md), **H** (escalation) and **I** (claim
  generation), so a specific instance can be cited later the way any other trap is.
- Two read-only sub-agents, [`claim-auditor`](starter/.claude/agents/claim-auditor.md) and
  [`round-planner`](starter/.claude/agents/round-planner.md), for the results that warrant a
  reader who does not know the story.

The bootstrap script installs all of it. Both skills are cheap: `simple-case-gate` is 42
lines and `claim-audit` is read only when a result is about to be written up.

---

## Auditing a document before you rely on it

The previous section guards one moment: a computation becoming prose. Nothing yet guards
what happens next — the prose becoming *the record*, and the record becoming the input to
every later session, every message to a collaborator, and eventually a paper.

That gap has a specific shape, and it is worth stating plainly. **A record is written in
the same pass, from the same context, as the claim it records.** Your workbook section, the
status line in your strategy map and the changelog row are not three independent witnesses;
they are three copies of one sentence you wrote once, while you were pleased with a result.
Nobody reads any of them adversarially before they are relied on. So the first hostile
reader of your record is whoever you send it to — and of course they find something.

A document audit is doing that read yourself, first.

### What it is, and what it deliberately is not

`/doc-audit <path>` takes **one document** and produces an evaluation of it: every headline
claim extracted, typed, traced to the evidence it cites, checked against the sibling
records, and written up as a report in `audits/`. It is a
[skill](starter/.claude/skills/doc-audit/SKILL.md) plus a
[mechanical lint](starter/.claude/skills/doc-audit/doc_lint.sh) plus two read-only
sub-agents.

Three things it is not, each of them a deliberate subtraction:

- **Not a referee report.** No recommendation, no novelty judgment, no author to address.
  Everything editorial is removed; what is left is "is this supported".
- **Not an edit.** The audit never changes the document. Findings carry *proposed
  replacement text* in quotes, and you decide what to apply, in a later turn. An agent that
  can fix what it finds has an obvious incentive to find fixable things — and, worse, an
  audit that edits as it goes leaves you unable to tell what it changed from what it
  checked.
- **Not truth.** The report is itself a document written in one pass, so it overclaims like
  everything else. More on that below, because it is the most useful thing in this section.

### The five moves

**1. Run the mechanical pre-filter first.** [`doc_lint.sh`](starter/.claude/skills/doc-audit/doc_lint.sh)
reads a `.tex` or `.md` file and reports: dangling `\ref`/`\cite` keys and dead relative
links; strength words ("proved", "for every n", "canonical") in paragraphs that carry none of
the eight claim statuses; hand-wave phrases; count leads; **file pointers that no longer
resolve**; unfinished markers; append-style retractions; relative dates; and a structural
check per document type.

The one to read literally is the pointer section. After you reorganise folders, nothing
errors — the prose still reads fine, and every path in it now points at nothing. That
section is the cheap way to see which evidence a document can no longer reach, and it tells
"moved" (the basename exists elsewhere) apart from "gone" (not in the repository at all).

Everything else in the lint is a *lead*, not a finding: read the flagged line before you
write anything down. And the same rule as `gate_audit.sh` applies — a clean run means "no
cheap tell fired", never "the document is sound", and an empty or unparseable file exits
non-zero with a loud banner rather than reporting zero problems.

**2. Sweep before you judge.** The next step reads the whole document and extracts one row
per checkable claim — location, the claim phrased *so that it could be false*, the type as
written, whether it is load-bearing, and **the check that would settle it** — with no
verdicts at all. On a long document this fans out to several
[`doc-sweeper`](starter/.claude/agents/doc-sweeper.md) agents in parallel, one per section.

Separating these two passes is the load-bearing design choice. If you read and judge at the
same time, you get confident verdicts on the claims that were easy to check and silence on
the ones that mattered — and the silence looks exactly like agreement. Proposing the check
is half the value of the sweep; a claim nobody can name a check for is itself a finding.

**3. Verify each load-bearing row, and say how.** Every row gets an evidence class, and
naming it is what stops "I read it and it seemed fine" from passing as verification:

| class | what it means |
|---|---|
| **TRACE** | the cited script/log/output exists, and the *check whose body tests this claim* is identified — label matched against body, vacuous checks named |
| **DERIVE** | re-derive a cheap step with the document's answer covered, then compare |
| **DRIFT** | the same statement in the strategy map, changelog, brief, big picture, newest handoff — same strength, same conditions, same numbers? |
| **TYPE** | the type as written vs. the type the evidence supports, with **the weakest supported statement written out in full** |
| **CITE** | the reference exists, and is cited for what it actually says |
| **CONVENTION** | checked against your pinned conventions, including where a quantity was translated from someone else's |

Verdicts come from a fixed vocabulary — `SUPPORTED`, `OVERCLAIMED`, `UNSUPPORTED`,
`CONTRADICTED`, `STALE`, `UNVERIFIABLE`, `QUESTION` — and each carries what the check does
*not* cover. `SUPPORTED` needs the same evidence as `OVERCLAIMED`: agreement is a result,
and "looks right" is not evidence for it.

**4. Get a second witness who does not know the story.** The top load-bearing claims go to
[`doc-auditor`](starter/.claude/agents/doc-auditor.md), which is handed **only** the bare
claim, its location, the definitions it needs and the evidence paths — never your verdict,
your ledger or the session narrative, since those are exactly what the fresh read is testing
around. Disagreement is the payoff, not a problem: report both readings and the single check
that would decide between them, and never average.

Two rules here came from getting it wrong in a real run:

- **Quote the document, never a sibling record.** Hand the reader the strategy map's
  paraphrase of a claim and it audits a sentence the document does not contain. Its verdict
  is then worthless in a way that is very hard to notice.
- **If a fresh read is lost** — a rate limit, an interrupted run — rerun it. Silently
  falling back to a single witness turns a two-witness verdict into a one-witness verdict
  with a two-witness label.

**5. Walk the rubric for that document type.** A workbook section, a big picture, a strategy
map, a handoff message and a paper fail in different ways, so
[`rubrics.md`](starter/.claude/skills/doc-audit/rubrics.md) carries a checklist per type:
pedagogy and in-place correction for workbooks; ledger-versus-strategy-map for big pictures;
currency and stop rules for strategy maps; the verdict/new-claim split for handoffs;
abstract-versus-body for papers. Each item is PASS / FAIL with a location, or N-A.

### Sibling records are co-claims, not ground truth

This is the idea most worth taking even if you never install the skill. When you check a
workbook statement against the strategy map and they agree, you have learned almost nothing
— both were written in the same session by the same process. When they *disagree*, you have
learned something real, and **the disagreement is the finding**. Do not resolve it by
picking the more recent file or the more authoritative-sounding one. Quote both sides, and
decide only if evidence decides.

The corollary is that "the strategy map says so" is never a reason a statement is true. Nor
is "12/12 checks passed" — a count is a control, and it belongs in a status line, not in the
place where the reason should be.

### The honest half of the report

Two sections do the most work and are the easiest to skip.

**"What was not checked."** Every row left unverified and why; scripts not re-run; citations
not checked; sections not swept. An audit with a short "not checked" list is usually an
audit that did not look. In a real workbook audit this list ran to seven bullets,
including "the remaining ~250 checks were not read" — which is the fact a reader most needs
in order to know what the report does *not* license.

**"Audit-tooling notes."** What the tools got wrong during this run. The first real run
produced four: a lint regex that read the LaTeX fraction `T^2/2` as a count lead; sweepers
reporting labels as missing because they were only given one file of a multi-file document;
a lost fresh-context read that nearly became a silent downgrade; and a claim handed to a
reader in the strategy map's wording rather than the document's. All four are fixed in the
version shipped here, and the first has a regression case in
[`selftest.sh`](starter/.claude/skills/doc-audit/selftest.sh). The point of the section is
that a checking tool improves only if each run is allowed to indict it.

### Audit the audit

The first real use of this workflow produced fifteen findings on one workbook. The user then
had a second agent evaluate the audit itself, with the same standard of evidence. Twelve
findings were accepted as written. **Three had their strongest wording rejected**: a count
was off by one (eight uncited scripts, not nine); "the proof survives only in an old commit"
was wrong, because the proof scripts were still on disk and the strategy map still held an
outline; and a terminology correction was right but had dropped the exceptional cases.

All three were accepted *in substance*. That is the expected shape, and it is worth knowing
before you run this on your own work, for two reasons. It is why the report proposes
replacement text instead of applying it — a 20%-overclaimed report that edits your workbook
is worse than no report. And it is a fair estimate of what an adversarial pass costs and
buys: roughly a fifth of the findings will be too strongly worded, and the other four fifths
will be things you would otherwise have shipped.

### When to run it

Not routinely — this is expensive, and on a long document it spawns a lot of agents. Run it
at the moments where a record stops being yours:

- before a document is relied on by a later session as settled background;
- before you send a section to a collaborator, or hand it to a second agent;
- before a workbook result becomes a paper claim;
- after a folder reorganisation (for the pointer check alone, `--depth quick` is enough);
- when a document and a sibling record seem to disagree and you want it settled.

If you do nothing else, three checks take five minutes on any document and catch most of
what the full audit catches:

1. **Does every pointer resolve?** Run the lint; read section `[5]`.
2. **Is every headline typed?** Any sentence with "proved", "for all", "canonical" that
   carries none of the eight statuses in the same paragraph is a claim nobody has priced.
3. **Does the strongest sentence appear identically in the sibling records?** Grep its most
   distinctive constant or phrase across the strategy map, changelog and brief, and compare
   the condition lists word for word.

### Wiring it in

- The skill [`doc-audit`](starter/.claude/skills/doc-audit/SKILL.md) with its
  [lint](starter/.claude/skills/doc-audit/doc_lint.sh),
  [rubrics](starter/.claude/skills/doc-audit/rubrics.md),
  [report template](starter/.claude/skills/doc-audit/report-template.md) and
  [self-test](starter/.claude/skills/doc-audit/selftest.sh).
- Two read-only sub-agents: [`doc-sweeper`](starter/.claude/agents/doc-sweeper.md) (declared
  `tools: Read, Grep, Glob` — no `Bash`, so read-only is a property, not a promise) and
  [`doc-auditor`](starter/.claude/agents/doc-auditor.md), which keeps `Bash` because it has
  to count lines in logs and ask git what is tracked; its file says so, and says what you
  give up by removing it.
- An [`audits/`](starter/audits/README.md) folder, with a README stating what a report is
  and is not.
- A paragraph in [`starter/CLAUDE.md`](starter/CLAUDE.md)'s *Research-claim discipline*
  block, so the rule survives without anyone invoking a skill.

One thing to fill in after installing: `doc_lint.sh` has a `SEARCH_DIRS` line near the top
listing the folders your documents cite scripts, logs and data from. If it does not know
where your evidence lives, it will report every pointer as unresolved.

---

## Session length and context limits

### The context window

Every Claude session has a finite context window — the total amount of text
(your messages, Claude's replies, file contents, tool outputs) that can fit in a
single conversation. As the session grows, this fills up. When it gets close to
the limit, Claude Code automatically compacts the session. If the session grows
beyond what even repeated compaction can manage, you will see an error along the
lines of **"context window full"** or **"API context token limit reached"**. This
is not a bug or a network problem — it means the session has accumulated more than
the model can hold at once. The fix is to start a new session.

### Seeing how full the window is

You do not have to guess. Two built-in commands show you, and both are read-only —
they report information and never change your work, so there is no reason not to
glance at them:

- **`/context`** draws a coloured map of what is currently filling the context
  window — file reads, tool outputs, the conversation itself — and warns you as you
  approach capacity. Use it when a session starts to feel long: it tells you
  *whether* you actually need to act and *what* is taking up the room (often a single
  large file read, or a chatty command you could have routed through rtk).
- **`/usage`** (also `/cost`) shows the session's token cost and where it is going,
  broken down by skill, sub-agent, and tool. It is the honest scoreboard for whether
  the token-saving machinery — rtk, distill, condensed notes — is actually paying off.

Together they turn "is this session getting too big?" from a guess into something you
can see, which is what tells you when to reach for compaction or a fresh session below.

**A rule of thumb for when to act.** There is no magic number, but a workable habit:

- **Around 50% full**, glance at `/context` — not to act, but as a reminder to write
  anything load-bearing from the conversation into `workbook.tex`/`brief.tex` while the
  detail is still there.
- **By around 70%**, do something: either `/compact` if you are mid-task and need to
  keep going, or — better for research — wrap the current sub-task and start a fresh
  session. Quality degrades *well before* the window is full, because every turn the
  model re-reads everything accumulated and your real signal gets diluted.
- **Do not wait for auto-compaction.** It only fires when the window is nearly full, by
  which point you have already been working in the degraded zone. It is a safety net,
  not a target.

Two things matter more than the percentage. First,