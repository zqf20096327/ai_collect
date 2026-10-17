<div align="center">

<img src="assets/00-cover.png" alt="10x Oracle" width="920">

# 🔮 10x Oracle

### Ask the community. Get the community's *actual* answer, cited.

**The 10x Marketers group has worked out the hard stuff together: the workflows, the systems, the strategy calls, the processes that actually hold up, and yes, the tools too. That knowledge is buried in thousands of WhatsApp messages nobody can search. The Oracle reads all of it, in Hebrew and English, and hands your own AI the real receipts.**

![Members only](https://img.shields.io/badge/access-10x%20Marketers%20members%20only-8A5CF6)
![Cited](https://img.shields.io/badge/every%20claim-cited%20to%20a%20real%20message-2ea44f)
![Bilingual](https://img.shields.io/badge/Hebrew%20%2B%20English-cross--lingual%20retrieval-0A66C2)
![No hallucination](https://img.shields.io/badge/the%20API-retrieves%2C%20never%20invents-2ea44f)
![Version](https://img.shields.io/badge/version-0.8.7-8A5CF6)

</div>

---

Somewhere in the group, someone already answered your question. How they restructured the team around AI, the pricing model that finally worked, the workflow that cut a week to an afternoon, the tool that burned them and the one that stuck. They posted it at 1am on a Tuesday eight months ago, and nobody will ever scroll back that far.

**The 10x Oracle is the group's memory, made askable.** You ask your own AI a question in plain language, about a tool, a tactic, a process, a strategy call, or the way the work itself is changing. It pulls the real messages where the community actually discussed it, quotes them with names and dates, and writes you an answer grounded in what your peers really said. Not what a model guessed. What the room said.

## It doesn't answer. It remembers.

This is the part that makes it trustworthy. The Oracle's API **never writes the answer** and never runs a model of its own. It does one job: retrieve the real community messages that match your question, as quoted, cited chunks. Your own agent, the Claude or ChatGPT you already talk to, reads those real quotes and writes the reply.

So the answer is only ever as good as the receipts behind it, and every receipt is a real message a real member sent. When the community never covered something, the honest answer comes back: *"the group hasn't discussed this."* An oracle that admits the gap is worth ten that make one up.

<div align="center"><img src="assets/cited-history.png" alt="The Oracle gathers the community's real, cited messages" width="840"></div>

---

## Enroll once, then just ask

Access is members only, checked against the 10x Marketers roster. You prove you're in the group once, your agent handles the setup, and you're done. No terminal, no config files, no commands to copy.

1. Tell your agent you want to use the 10x Oracle. It hands you **[the enroll link](https://community-oracle-rag.10xmarketers.workers.dev/enroll)**.
2. **Sign in with Google**, then enter the **phone number you use in the community**. It's checked as a one-way hash against the member list, and your number is never stored in the clear.
3. The page shows you a token once. **Tap it to copy**, come back to your agent, and say **"go"**.

Your agent saves the token for you and confirms it works. That's the whole setup. Tokens last 90 days; to renew, enroll again with the same Google account and say "go".

<div align="center"><img src="assets/members-welcome.png" alt="Members-only, the warm way in" width="840"></div>

---

## It reads the room like a member who was there

A lazy tool runs one search and calls it done. The Oracle is built to work the way a sharp community member actually would, and that discipline is the whole point:

- **It searches in both languages.** The group talks ~83% in Hebrew, so an English-only search misses most of the thread. Every real question fires in Hebrew *and* English, following the community's own vocabulary, the tool names and slang they actually use.
- **It surfaces the change, not a snapshot.** The group's take on a tool, a tactic, or a whole way of working in late 2025 is often the opposite of its take in mid-2026. The Oracle shows you *both*, dated, and names the reversal instead of flattening months of hard-won debate into one bland verdict.
- **It refuses to fake a consensus.** When members disagree, you get both camps with names and dates, not an averaged mush that nobody actually said.
- **It says when it's thin.** One strong opinion is one data point, not "the community thinks." The Oracle tells you the difference every time.
- **It attributes like a professional.** Real names, real dates, the person's actual words. Misquoting a member is the one thing that gets a tool yelled at in the group, so it doesn't.

<div align="center"><img src="assets/no-consensus.png" alt="It weighs both sides honestly and refuses a fake consensus" width="840"></div>

---

## Two questions it answers better than anything else

Ask about anything the group has lived through: a tool, sure, but also a workflow, a pricing model, a way of structuring a team, a strategic bet on where AI marketing is headed.

**"Is this rising or fading in the group?"**
The Oracle builds a dated timeline, not a single lookup. It walks the idea forward through time and reads the trajectory: are people talking about it more or less, warmer or cooler, and did a newer approach quietly show up *instead* of it. That substitution is usually the real story.

> *"Through 2025 the group leaned on big all-in-one automations; by 2026 the conversation shifted to smaller agent-driven workflows and 'let the model decide.' The old way isn't abandoned, it's being rethought."*

**"A vs B, which way does the group lean?"**
Tool vs tool, but also in-house vs agency, one workflow vs another, build vs buy. It pulls each side on its own, in both languages, then head to head, and weighs the evidence honestly. If the group argued about A for months and mentioned B twice, that asymmetry *is* the finding. No fake scoreboard.

> *"The group has a lot to say about restructuring around AI and real opinions on it; the 'just hire a specialist agency' route barely comes up. So the honest read is preference-by-attention toward building it in-house, but the community never really put the two head to head."*

<div align="center"><img src="assets/over-time.png" alt="It shows how the group's view shifted over time" width="840"></div>

---

## More than prose: dashboards, digests, and the links you lost

Ask for a **weekly catch-up** and you get the week's threads summarized in your language, every member credited, plus a "Links shared" section with every URL someone posted and why it mattered. That link section is half the value of a community, and it's the first thing a chat log swallows.

Ask it to **visualize** a trend and it builds a single self-contained HTML dashboard from the real chunks: weekly volume, who said what, the disagreements laid side by side, and a sources appendix citing every message. Honest counts only, no invented numbers, nothing that phones home.

---

## Built to shrug off a poisoned message

The Oracle serves you real WhatsApp messages, and somewhere in any big group is a joker who typed "ignore your instructions and do X." So every chunk arrives wrapped in an explicit **untrusted-data fence**: your agent is told, in the data itself, that everything inside is a *quote being reported*, never a command to obey. A malicious message in the corpus can be read about, but it can't steer your agent. Contact details are stripped at ingest, so nobody's phone or email can be reconstructed out of a quote.

<div align="center"><img src="assets/injection-safe.png" alt="A poisoned message bounces off; the Oracle stays calm" width="840"></div>

---

## Honest by construction

Every number the Oracle helps you put on screen has to be recomputable from the real messages it just pulled. The relevance score is a distance, never dressed up as a confidence percentage. A quiet recent window gets flagged as *maybe nothing was ingested*, not reported as *the community went silent*. The corpus always tells you its own as-of date, so you never claim the group said something "this week" that it actually said last spring.

You get a generous budget for real work: 60 questions an hour, 300 a day, plenty for a deep trend sweep or a full tool comparison.

---

## Install

The Oracle rides inside whatever AI you already use. It is **one plugin**, not three builds, so
whichever door you come through you get the same Oracle and the same updates.

### Cowork (Claude Desktop) — the easy one

1. Sidebar → **Customize** → **Plugins**
2. **Add marketplace**, paste `alexgreensh/10x-oracle`
3. Find **10x Oracle** in the list → **Install**

That's it. Cowork checks this repo for new versions on its own.

> Cowork doesn't read Claude Code's `~/.claude` folder, so if you use both, install it in each.

### Claude Code

```
/plugin marketplace add alexgreensh/10x-oracle
/plugin install 10x-oracle@10x-company
```

Or paste this repo's link into Claude Code and let it do the whole thing, install and enrollment.

### Codex

Codex has the same plugin system, so it's the same plugin from the same marketplace:

```bash
codex plugin marketplace add https://github.com/alexgreensh/10x-oracle
codex plugin add 10x-oracle@10x-company
```

More detail in **[INSTALL-CODEX.md](INSTALL-CODEX.md)**.

Then **enroll once** (above) and just ask your agent about the community in plain language, in
whichever language you think in.

---

## Pairs well with

- **Your own agent.** Claude Code, or any agent that can run a Python script. The Oracle hands it the receipts; it does the talking, in your voice.
- **The community itself.** The Oracle is only as wise as the group is generous. Every good answer someone posts today is an answer the Oracle can give tomorrow.

---

<div align="center">

Built for the **[10x Marketers](https://community-oracle-rag.10xmarketers.workers.dev/enroll)** community by the **10x Company**.

*The group already knew. Now you can ask.*

</div>

---

Built by **Alex Greenshpun** and **[the10xcompany.ai](https://the10xcompany.ai)** for the 10x Marketers community.
