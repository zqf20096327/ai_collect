<p align="center">
  <img src="https://em-content.zobj.net/source/apple/391/scissors_2702-fe0f.png" width="120" />
</p>

<h1 align="center">concise</h1>

<p align="center">
  <strong>say more with less</strong>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/github/license/o4f6bgpac3/concise?style=flat" alt="License"></a>
  <img src="https://img.shields.io/badge/tokens-~60--70%25_saved-blue?style=flat" alt="Token savings">
</p>

<p align="center">
  <a href="#install">Install</a> &bull;
  <a href="#before--after">Before/After</a> &bull;
  <a href="#elaborate-on-request">Elaborate</a> &bull;
  <a href="#vs-caveman">vs Caveman</a> &bull;
  <a href="#why">Why</a>
</p>

---

A [Claude Code](https://docs.anthropic.com/en/docs/claude-code) skill/plugin and Codex plugin that makes Claude respond concisely -- cutting **~60-70% of output tokens** while keeping natural, readable English. Also works with Cursor, Cline, Windsurf, and GitHub Copilot.

Reduce token usage. Lower API costs. Get faster responses. No broken grammar. No telegram-speak. Just the answer, tight and clean.

## Before / After

<table>
<tr>
<td width="50%">

### Normal Claude (69 tokens)

> "The reason your React component is re-rendering is likely because you're creating a new object reference on each render cycle. When you pass an inline object as a prop, React's shallow comparison sees it as a different object every time, which triggers a re-render. I'd recommend using useMemo to memoize the object."

</td>
<td width="50%">

### Concise Claude (27 tokens)

> "You're creating a new object reference each render. Inline object props fail shallow comparison every time. Wrap it in `useMemo`."

</td>
</tr>
<tr>
<td>

### Normal Claude

> "Sure! I'd be happy to help you with that. The issue you're experiencing is most likely caused by your authentication middleware not properly validating the token expiry. Let me take a look and suggest a fix."

</td>
<td>

### Concise Claude

> "Bug's in auth middleware -- token expiry check uses `<` instead of `<=`. Here's the fix:"

</td>
</tr>
<tr>
<td>

### Normal Claude

> "Sure! Merge conflicts happen when Git can't automatically reconcile differences between two branches. Let me walk you through the process of resolving this. First, you'll want to open the file and look for the conflict markers..."

</td>
<td>

### Concise Claude

> "Open the conflicted file, find the `<<<<<<<` markers. Keep the code you want from each side, delete the markers. Then `git add` and commit."

</td>
</tr>
</table>

Same answer. Proper English. Fewer tokens.

## Elaborate on Request

The key feature: ask for more detail anytime and get it. Then concise auto-resumes.

```
You:     Why is my app slow?
Claude:  Main bottleneck is N+1 queries in the orders endpoint. Each order
         triggers a separate DB call for line items. Use includes(:line_items)
         to eager-load.

You:     Elaborate on that
Claude:  When Rails loads your orders list, it runs one query to fetch all
         orders. Then for each order, when you access order.line_items in the
         view, ActiveRecord fires a separate SELECT query. With 50 orders,
         that's 51 total queries -- one for the list, plus one per order.
         This is the N+1 query problem.

         includes(:line_items) tells ActiveRecord to load all line items in
         a single additional query. Instead of 51 queries, you get 2. On a
         typical page, this cuts response time from seconds to milliseconds.

You:     OK, what about the frontend?
Claude:  Frontend's fine. Lighthouse shows 92 performance. Only issue is an
         unoptimized hero image -- run it through ImageOptim.
```

No permanent mode switch. One detailed answer, then back to concise.

## Install

```bash
npx skills add o4f6bgpac3/concise
```

For a specific agent:

```bash
npx skills add o4f6bgpac3/concise -a cursor
npx skills add o4f6bgpac3/concise -a github-copilot
npx skills add o4f6bgpac3/concise -a cline
npx skills add o4f6bgpac3/concise -a windsurf
npx skills add o4f6bgpac3/concise -a codex
```

Or with Claude Code plugin system:

```bash
claude plugin marketplace add o4f6bgpac3/concise
claude plugin install concise@concise
```

## Usage

Trigger with:
- `/concise`
- "concise mode"
- "be concise"
- "less verbose"

Stop with: "stop concise" or "normal mode" or "be verbose"

## What Concise Does

| Thing | Concise does... |
|-------|----------------|
| English explanations | Cut filler, keep grammar |
| Code blocks | Write normally |
| Technical terms | Keep exact |
| Error messages | Quote exact |
| Git commits & PRs | Write normally |
| Articles (a, an, the) | Drop where natural, keep where needed |
| Pleasantries | Gone ("Sure! I'd be happy to..." is dead) |
| Hedging | Gone ("It might be worth considering..." is extinct) |
| Elaborate requests | Full detailed answer, then auto-return |

## vs Caveman

[Caveman](https://github.com/JuliusBrussee/caveman) and concise are complementary:

| | Caveman | Concise |
|---|---------|---------|
| Token savings | ~75% | ~60-70% |
| Grammar | Broken (fragments, no articles) | Correct (natural English) |
| Readability | Requires adjustment | Reads like normal text |
| Intensity levels | lite / full / ultra | Single mode |
| Elaborate on request | No | Yes |
| Best for | Maximum compression | Balanced readability + savings |

Want maximum compression and don't mind telegram-style? Use caveman.
Want readable output with solid token savings? Use concise.

Concise was inspired by caveman -- loved the idea, wanted something that reads like normal English.

## Why

- **Faster responses** -- fewer tokens to generate means faster output
- **Easier to read** -- no walls of text, just the answer
- **Same accuracy** -- all technical info preserved, only filler removed
- **Lower cost** -- ~60-70% fewer output tokens
- **Still sounds human** -- proper English, not broken grammar

## Development

```bash
git clone https://github.com/o4f6bgpac3/concise.git
cd concise
git config core.hooksPath .githooks
```

Edit only `skills/concise/SKILL.md`. The pre-commit hook syncs all other copies automatically.

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

MIT
