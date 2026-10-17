# SingCompress

[![license](https://img.shields.io/github/license/dljw/singcompress)](https://github.com/dljw/singcompress/blob/main/LICENSE)

**Cut your AI costs by up to 72% — using Singapore English grammar.**

## What Is This?

AI assistants (ChatGPT, Claude, Copilot) charge based on how many words they produce. These words are called **tokens** — and fewer tokens means lower cost.

SingCompress tells the AI to respond using **Singlish** — a real language spoken by millions in Singapore — which naturally says the same thing in fewer words. Think of it as shorthand for AI, but based on a real spoken language with [decades of linguistic research](https://en.wikipedia.org/wiki/Singlish).

Inspired by [caveman](https://github.com/JuliusBrussee/caveman), but linguistically grounded.

## Before / After

All examples from **Claude Opus 4.6**:

| | Default | Siudai | Medium | Gao |
|---|---|---|---|---|
| **SQL Injection Review** | "This code has a **critical security flaw**: it's vulnerable to **SQL injection**. String interpolation inserts user input directly into the SQL query with no sanitization..." | "**SQL injection vulnerability** — attacker can pass `'; DROP TABLE users; --` as username and destroy your data. Fix: use parameterized queries." | "**SQL injection vulnerability sia.** User pass `'; DROP TABLE users;--` as username, GG **liao**. Use parameterized query." | "SQL injection **sia**. **Jialat**. Use parameterized q **lor**. Raw f-string → anyone can inject one." |
| **CORS Error** | "This is one of the most common development issues. The browser blocks requests between different origins (different ports count as different origins). Here are the solutions..." | "Install `cors` middleware on your Express server. For production, lock down to specific origin." | "Classic CORS issue. Frontend and backend diff ports → browser block cross-origin req. **Fix: Install and use `cors` middleware in Express.**" | "Classic one. Install `cors` mw. Want restrict to your React port only, use `cors({ origin: 'http://localhost:3000' })`." |
| **Stale Closure** | "This is one of the most common React pitfalls: **stale closures**. When your useEffect callback is created, it captures the state variable's value at the time of that render..." | "Classic React stale closure problem. Your useEffect callback captures state value from render it was created in, and if dependency array not updated properly, it keeps referencing old value." | "Stale closure **lah**. useEffect callback capture state value from render it was created. You update state → new render → but old effect still holding old value." | "Stale closure **lah**. React `useEffect` captures vals from render it was created in. If dependency array **bo** include that state var, cb still sees old value one." |
| **React Re-renders** | "The core issue is **referential identity**. Every time the parent renders, your inline object prop creates a **new object in memory**, even if its contents are identical..." | "Every time parent renders, inline object `{}` creates **new reference** in memory. React does shallow comparison for props — different reference means different prop, so child re-renders." | "Inline obj → new ref every render → React sees different prop → re-render. Same thing for inline fn — use `useCallback`." | "Inline obj = new ref every render → `===` check fail → child re-render **cfm**. Same thing for inline fns & arrays **hor**." |
| **Race Condition** | "This is a classic **lost update** / **read-modify-write race condition**. Your code likely does a read-then-write pattern concurrently..." | "Multiple requests doing **read-then-write** pattern concurrently. Both get same value, both write same increment, lost one update." | "Classic race condition **lah**. Got lost update problem. Two req read counter same time → both get same value → both write 6 → lost one increment." | "**Cfm** race condition one. Classic lost update problem **sia**. 2 req read counter = 5 same time → both write 6 → lost 1 increment. GG." |
| **Security Headers** | "There are several security issues and missing best practices in this setup: Wildcard CORS Origin is critical, setting `origin: '*'` allows **any website** to make requests to your API..." | "Few security issues here: CORS wide open, no rate limiting, app vulnerable to brute force and DDoS..." | "Got few security issues here: CORS wide open — `origin: '*'` means any domain can hit your API. Kena CSRF attack easy." | "Few issues **sia**: CORS `origin: '*'` — **jialat**, any domain can hit your API. **Bo** rate limiting — kena DDoS **cfm** GG. **Bo** helmet — `app.use(helmet())` **steady** one." |

Same technical content. Up to **88% fewer tokens.** Quotes are excerpted for brevity.

## Why Should I Care?

- **Save money** — Up to 72% fewer output tokens = proportionally lower API bills
- **Faster responses** — Fewer tokens to generate = quicker replies
- **Linguistically grounded** — Not random abbreviation. Based on Singlish, a rule-governed contact language with [extensive linguistic research](https://en.wikipedia.org/wiki/Singlish_grammar)

---

## Table of Contents

- [Quick Start](#quick-start)
- [How It Works](#how-it-works)
- [Compression Levels](#compression-levels)
- [More Examples](#more-examples)
- [Benchmarks](#benchmarks)
- [Singlish Grammar Patterns](#singlish-grammar-patterns)
- [Model Compatibility](#model-compatibility)
- [Running the Eval](#running-the-eval)
- [Why Singlish?](#why-singlish)

---

## Quick Start

### Claude Code Plugin

```bash
claude plugin marketplace add dljw/singcompress
claude plugin install singcompress@singcompress
```

Auto-activates on every session. Use `/singcompress siudai|medium|gao|off` to switch levels.

### AI Coding Agents (Cursor, Copilot, Windsurf, Cline, 40+ more)

```bash
npx skills add dljw/singcompress -a cursor
npx skills add dljw/singcompress -a github-copilot
npx skills add dljw/singcompress -a windsurf
npx skills add dljw/singcompress -a cline
```

Uses the [Vercel Skills CLI](https://github.com/vercel-labs/skills) to install the SKILL.md into your agent's skills directory.

<details>
<summary><strong>Manual install (any agent)</strong></summary>

Copy `skills/singcompress/SKILL.md` into your agent's skills directory:

```bash
# Claude Code
cp -r skills/singcompress ~/.claude/skills/singcompress

# Cursor
cp -r skills/singcompress .cursor/skills/singcompress

# Or just read the SKILL.md and paste it into your agent's system prompt
```

</details>

## How It Works

SingCompress is a system prompt that instructs the LLM to respond using Singlish grammatical patterns that naturally compress meaning. It is not a post-processor or proxy — the model generates compressed output directly.

**What gets compressed:** Natural language prose — explanations, descriptions, instructions.

**What stays untouched:** Code blocks, error messages, technical terms, file paths, URLs, JSON, YAML, SQL, shell commands.

**Safety:** Auto-Clarity mode automatically reverts to Standard English for security warnings, irreversible operations, and anything where fragmented language risks misinterpretation.

## Compression Levels

### Light (siudai) — Professional compression
Drop articles, copulas, filler, pleasantries. Grammar stays intact.

> "Server returning 500 error because database connection pool exhausted."

### Medium (default) — Recommended for most use cases
Full Singlish grammar: "got" existential, "liao"/"already" completion, PRO-drop, topic-comment, "can meh?", abbreviations (DB, auth, fn, etc.), arrow causality, aggressive fragmentation.

> "SQL injection vulnerability **lah**. Never sanitise input → attacker can break out of string."

### Heavy (gau) — Maximum compression
All medium rules plus SG particles (lor, sia, hor, one, leh), Singlish vocabulary (jialat, shiok, simi, sian, steady, bo), SG text shortcuts (cfm, tmr, alr, nvm), symbol compression (&, w/, b/c).

> "SQL injection **sia**. **Jialat**. Use parameterized q **lor** — DB driver handle escaping, safe **liao**."

## More Examples

<details>
<summary><strong>See more before/after examples (Sonnet)</strong></summary>

### Debugging: CORS Error

> **Default (1032 tokens):** "This is one of the most common issues in local full-stack development! Here's a thorough breakdown of what's happening and how to fix it..."

> **Medium (162 tokens):** "Install `cors` pkg, then add to Express: `app.use(cors({ origin: 'http://localhost:3000' }));` Put **before** all routes **lah**."

### Debugging: Stale Closure

> **Default (870 tokens):** "This is a very common React gotcha known as a stale closure. Here's what's happening and why..."

> **Medium (179 tokens):** "Classic stale closure **lah**. useEffect captures state value at render time. Got deps array wrong (or empty `[]`), so callback never re-created → always sees old value."

### Debugging: Race Condition

> **Default (1587 tokens):** "What you're experiencing is a classic race condition caused by a non-atomic read-modify-write cycle..."

> **Heavy (431 tokens):** "**Race condition / lost update lor.** Multiple reqs read same val → each increment own copy → write back → earlier write overwritten."

</details>

## Benchmarks

Medium mode achieves **72% token reduction** on Sonnet and beats generic "be concise" prompts by **16-32%** across all models.

<details>
<summary><strong>Full benchmark results — tested across 24 prompts on 3 Claude models</strong></summary>

### Token Reduction vs Default Baseline

| Level | Sonnet | Opus | Haiku |
|-------|:------:|:----:|:-----:|
| Light (siudai) | -64% | -48% | -33% |
| **Medium** | **-72%** | **-60%** | **-44%** |
| Heavy (gau) | -65% | -61% | -28% |

### Does it beat generic "be concise"?

| Level | Sonnet | Opus | Haiku |
|-------|:------:|:----:|:-----:|
| Light | -12% | +9% | -4% |
| **Medium** | **-32%** | **-16%** | **-19%** |
| Heavy | -16% | -19% | +5% |

Medium mode beats a generic concise prompt by **16-32%** across all models — Singlish compression is structurally more efficient than just "be brief".

### Per-Category Breakdown — Sonnet (vs Default)

| Category | Light | Medium | Heavy |
|----------|:-----:|:------:|:-----:|
| Coding explanation | -62% | -69% | -62% |
| Debugging | -66% | **-76%** | -70% |
| Architecture | -64% | -72% | -66% |
| Code review | -63% | -74% | -71% |
| Multi-step | -59% | -67% | -58% |
| Conversational | -70% | -75% | -65% |

</details>

## Singlish Grammar Patterns

<details>
<summary><strong>Full table of Singlish grammar patterns used</strong></summary>

| Pattern | Standard English | SingCompress | Tokens Saved |
|---------|-----------------|-------------|:------------:|
| **"Got" existential** | "There is a bug in line 42" | "Got bug in line 42" | 2-3 |
| **"Already" / "liao" completion** | "I have already fixed it" | "Fix already" / "Fix liao" | 3-4 |
| **PRO-drop** | "I cannot find the file" | "Cannot find file" | 2 |
| **Topic-comment** | "This is the function that handles auth" | "This function — handle auth" | 4-5 |
| **Bare conditionals** | "If you get an error, restart" | "Got error, restart" | 3 |
| **"Can/Cannot"** | "Yes, that's possible" | "Can." | 3-4 |
| **"Lah" emphasis** | "No, that definitely won't work" | "Cannot lah" | 4-5 |
| **"Can meh?" doubt** | "Are you sure that will work?" | "Can meh?" | 5-6 |
| **Arrow causality** | "This causes that which leads to" | "X → Y → Z" | 3-5 |
| **Copula omission** | "The server is busy" | "Server busy" | 2 |
| **"Jialat" (heavy)** | "This is seriously broken" | "Jialat" | 3-4 |
| **"Sia" emphasis (heavy)** | "This is surprisingly fast" | "Fast sia" | 3-4 |
| **"Lor" resigned (heavy)** | "Well, that's just how it is" | "Like that lor" | 6-7 |
| **SG text shortcuts (heavy)** | "confirm", "tomorrow", "already" | "cfm", "tmr", "alr" | 1-2 each |
| **Symbol compression (heavy)** | "with", "without", "because" | "w/", "w/o", "b/c" | 1-2 each |

These are not random simplifications — they are documented features of Singlish grammar, a rule-governed contact language with [extensive linguistic research](https://en.wikipedia.org/wiki/Singlish_grammar).

</details>

## Model Compatibility

| Model | Singlish Quality | Best Level | vs Default | vs Concise |
|-------|:----------------:|:----------:|:----------:|:----------:|
| Claude Sonnet | Fluent, natural | Medium | **-72%** | **-32%** |
| Claude Opus | Precise, idiomatic | Heavy | **-61%** | **-19%** |
| Claude Haiku | Functional | Medium | **-44%** | **-19%** |

All three models beat generic "be concise" prompts. Sonnet delivers the highest compression. Opus is the only model where heavy outperforms medium — it fully leverages the expanded Singlish vocabulary. Haiku works well on medium but struggles with the heavy rule set.

## Running the Eval

<details>
<summary><strong>Eval instructions (for developers)</strong></summary>

```bash
# Install dependencies
npm install

# Run full eval (uses your Claude Code subscription)
npx tsx evals/run.ts --model sonnet

# Run a single prompt
npx tsx evals/run.ts --prompt-id debug-cors --model sonnet

# Analyze results
npx tsx evals/measure.ts

# With semantic preservation scoring
npx tsx evals/measure.ts --with-semantic
```

</details>

## Why Singlish?

Singlish evolved as a contact language among multilingual speakers in Singapore. Its grammar systematically drops redundant elements — articles, copulas, subject pronouns, tense markers — while adding efficient particles ("lah", "liao", "got") that pack pragmatic meaning into single tokens. These aren't deficiencies; they're **compressions that evolved to communicate meaning quickly**.

SingCompress applies these same compressions to LLM output. The result is fewer tokens with the same technical content — and if you're Singlish-literate, it reads naturally.

## License

MIT
