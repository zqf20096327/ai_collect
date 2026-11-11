![Repo structure for in-house marketers](.github/banner.png)

# Repo structure for in-house marketers

The folder layout that gives Claude Code your company's context before it writes anything. Fork it, fill `context/` with what's true about your buyers, your positioning and your voice, and every draft after that starts from it. You stop re-explaining your product every session.

**[Use this template →](https://github.com/new?template_name=repo-structure-in-house&template_owner=matteotitta)**

---

## Start in three steps

1. **Create your copy.** Click *Use this template* above, or run:
   ```bash
   gh repo create my-marketing --template matteotitta/repo-structure-in-house --private --clone
   ```
2. **Read the example first.** `example/pulse-analytics/` is a made-up B2B SaaS company with every context file filled in. It shows the shape each file should take.
3. **Fill your context in this order:** ICP, competitors, voice, positioning, messaging. Each folder's `CLAUDE.md` says what goes in it. Write the files yourself, or with Claude, copying the shape of the example and never its facts.

---

## What's inside

```
repo-structure-in-house/
├── context/          what Claude reads first: icp, competitors, positioning,
│                     messaging, brand (your voice), docs
├── outputs/          what you ship, one folder per lane: content, website, seo-aeo,
│                     social, product-marketing, sales, paid, lifecycle, outbound
├── example/          PulseAnalytics, filled in. Read it, then delete it
└── .claude/
    └── rules/        one house rule: quote the source, or lower the confidence
```

Every folder has a one-page `CLAUDE.md` that says what goes there.

**The idea:** `context/` is written once and kept current. `outputs/` is where work happens. Because Claude reads `context/` before it writes, a landing page, a launch plan and a LinkedIn post all come out sounding like the same company.

---

## The skills come with the course

This repo is the layout only. The skills that fill `context/` for you (ICP research, competitor research, voice, positioning, messaging and more) and the skills for every lane in `outputs/` come with [Marketing Engineering University](https://maven.com/matteo-tittarelli/marketing-engineering-university-genesys-growth). Students build the whole system on their own company:

| | This repo | Course |
|---|---|---|
| Context folders, lanes and the worked example | ✓ | ✓ |
| Skills that research and write your context | | ✓ |
| Skills for every lane, with reference material and templates | | ✓ |
| Lanes split into research, strategy and execution | | ✓ |
| Agents, commands and hooks that chain skills and check their own work | | ✓ |
| Connectors set up for your stack (Slack, Notion, CRM, analytics) | | ✓ |
| Live sessions and feedback on your own company | | ✓ |

Want to try skills on this layout now? [genesys-skills](https://github.com/matteotitta/genesys-skills) has ten free ones you can install today.

---

## Keep it alive

- Every file in `context/` has one owner.
- Update a context file when something real changes: a new competitor, a pricing change, a new segment.
- Every 90 days, spend 30 minutes pruning anything nobody reads.

---

Built by [Matteo Tittarelli](https://www.linkedin.com/in/matteotittarelli/) at [Genesys Growth](https://genesysgrowth.com). MIT licensed: fork it, change it, use it with clients.
