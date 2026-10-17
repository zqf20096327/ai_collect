<div align="center">

<img src="assets/hero.svg" alt="feynman-technique — without feynman-technique: The request to /api/orders is being blocked by the browser&#x27;s same-origin policy. The preflight response from api.example.com carries no Access-Control-Allow- Origin header, so the fetch is rejected before your handler runs.  I&#x27;ll add the cors middleware to server.js and allow the origin http://localhost:3000. Apply this patch to server.js? — with feynman-technique: Your code didn&#x27;t fail. The browser stopped it.  It sent your request, got the answer back from the API, and then refused to hand it to your page.  It does that because you might be signed in over there. Without the rule, any tab you have open could quietly read what sits behind your login.  The API has to say your address is welcome. It never did, so the browser threw the answer away.  That&#x27;s also why it works in Postman and dies here. Postman has nobody to protect. Your browser has you.  I can make the API say your address is welcome. Want me to add you to its list?" width="820">

# Feynman Technique

### The AI gave you a fix. It worked. You still don't know why.

**This is for the second part.**

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-open%20standard-6b4fbb)](https://agentskills.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Works with](https://img.shields.io/badge/works%20with-Claude%20·%20ChatGPT%20·%20Codex%20·%20Cursor%20·%20Copilot%20·%20Gemini-333)](#installation)
[![Built from](https://img.shields.io/badge/built%20from-88%2C000%20words%20of%20Feynman-c2410c)](#where-this-comes-from)

**English** ·
[中文](docs/i18n/README.zh-CN.md) ·
[हिन्दी](docs/i18n/README.hi.md) ·
[Español](docs/i18n/README.es.md) ·
[Français](docs/i18n/README.fr.md) ·
[العربية](docs/i18n/README.ar.md) ·
[বাংলা](docs/i18n/README.bn.md) ·
[Português](docs/i18n/README.pt-BR.md) ·
[Русский](docs/i18n/README.ru.md) ·
[اردو](docs/i18n/README.ur.md)

</div>

---

## Same model. Same question. One line of setup.

> **"Why am I getting `Cannot read properties of undefined (reading 'map')`?"**

<table>
<tr>
<th width="50%">Without the skill</th>
<th width="50%">With the skill</th>
</tr>
<tr valign="top">
<td>

`.map()` is being invoked on an undefined reference. Your component renders before the asynchronous fetch resolves, so the state variable is still uninitialised at first paint. Initialise it as an empty array or guard the render path with a conditional.

</td>
<td>

You told the page: take my list of items, and draw one row for each.

But the list hasn't arrived yet — it's still on its way from the server. So at that moment there is no list at all, and the page trips over the empty space where one should have been.

Hand it an empty list to hold until the real one lands. Now it draws nothing, waits, then draws everything.

</td>
</tr>
<tr valign="top">
<td>

Six terms you had to already know. Correct, and you still can't picture it.

</td>
<td>

Zero. And you know which line to change, and what to expect after.

</td>
</tr>
</table>

Both answers are true. Only one of them was an explanation.

---

## Where this comes from

Feynman's father showed him a bird, and told him you can learn its name in every language
on earth and still know **absolutely nothing about the bird**. You would only know what
people call it. To know the bird, watch what it does.

> "There is a difference between the name of the thing and what goes on."
> — Richard Feynman, *What Is Science?*, 1966

That's the whole idea, and almost every AI fails it by default. Ask what something is and
you get its name in fancier words. This skill makes the model deliver the **mechanism
first** and the name last — the way Feynman did.

It was built from primary sources, not from blog posts about him. Around **88,000 words**
of his own writing were analysed to derive both the method and the prose: *Six Easy
Pieces*, the 1965 Nobel Lecture, *Cargo Cult Science*, *What Is Science?*, *There's Plenty
of Room at the Bottom*, and the Brazil chapter of *Surely You're Joking, Mr. Feynman!*

**The repo is in English. The answers aren't** — it replies in whatever language you write in.

---

## The four tests it runs

Not the folk version. These are Feynman's own, each traceable to a primary source.

<table>
<tr valign="top"><td width="30%">

**The rephrase test**

</td><td>

*"Without using the new word which you have just learned, try to rephrase what you have just learned in your own language."* (1966)

Cover the term. If the sentence dies without it, you wrote a definition, not an explanation.

</td></tr>
<tr valign="top"><td>

**The triboluminescence test**

</td><td>

Feynman opened a textbook at random: *"Triboluminescence is the light emitted when crystals are crushed."* His verdict — you have only said what a word means in terms of other words.

His rewrite: *"When you take a lump of sugar and crush it with a pair of pliers in the dark, you can see a bluish flash. Some other crystals do that too. Nobody knows why. The phenomenon is called 'triboluminescence.'"*

Something you can do → what you'd see → honest ignorance → **then** the name.

</td></tr>
<tr valign="top"><td>

**The "look at the water" test**

</td><td>

His Brazilian students could recite Brewster's Angle perfectly. Asked to point a polaroid at the bay outside the window, they froze.

An explanation you can only reach through its keyword is one you'll never reach in the wild.

</td></tr>
<tr valign="top"><td>

**The cargo cult test**

</td><td>

After reading, what can you actually *do* that you couldn't before? Correct form with nothing behind it means the planes don't land.

</td></tr>
</table>

---

## Installation

One folder. Works in any tool that supports the
[Agent Skills open standard](https://agentskills.io).

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.claude/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.claude/skills/
```

That's Claude Code. Then just ask:

```
/feynman-technique explain how database indexes work
```

<details>
<summary><b>Claude Code</b> — project-level, shared with your team</summary>

```bash
mkdir -p .claude/skills
cp -r /tmp/feynman-technique/skills/feynman-technique .claude/skills/
```

Commit it and everyone on the repo gets it. Run `/doctor` to confirm it loaded.

</details>

<details>
<summary><b>Or use the script</b> — and keep your copy from going stale</summary>

```bash
./install.sh              # personal, Claude Code
./install.sh --project    # into this repo, for the team
./install.sh --all        # every tool directory present on this machine
./install.sh --check      # report which copies have fallen behind, change nothing
```

`--check` is the one worth remembering. An installed skill is a *copy*; it does not
follow the repo. Pull, run `--check`, and it names any copy that no longer matches —
otherwise you find out weeks later, from an answer that should already have been fixed.

</details>

<details>
<summary><b>Claude.ai</b> — web and desktop</summary>

Requires **Pro, Max, Team, or Enterprise** with code execution enabled.

1. Download this repository ([**ZIP**](https://github.com/guicortei/feynman-technique/archive/refs/heads/main.zip)).
2. Zip the `skills/feynman-technique` **folder itself**, so `SKILL.md` sits at the archive root:
   ```bash
   cd skills && zip -r feynman-technique.zip feynman-technique
   ```
3. **Settings → Capabilities → Skills** (shown as *Features* on some plans) → **Upload skill**.
4. Select `feynman-technique.zip`.

Claude uses it automatically when you ask for an explanation, or you can ask for it by name.

> Custom skills on claude.ai are per-user — each teammate uploads their own copy.

</details>

<details>
<summary><b>ChatGPT</b> — desktop app</summary>

1. Download and unzip this repository.
2. Open the ChatGPT desktop app and select **Skills** in the sidebar.
3. Add the `feynman-technique` folder.
4. Invoke it by typing `@` and picking it from the list.

**No skills on your plan?** See [Any other AI](#any-other-ai-no-skills-support) below.

</details>

<details>
<summary><b>OpenAI Codex CLI</b></summary>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.agents/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.agents/skills/
```

Project-level: `.agents/skills/` in your repo root. Invoke with `$feynman-technique`, or
run `/skills` to list what's available.

</details>

<details>
<summary><b>Cursor</b></summary>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.cursor/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.cursor/skills/
```

Project-level: `.cursor/skills/` or `.agents/skills/`. Cursor also reads
`~/.claude/skills/`, so a Claude Code install already covers it. Type `/` in the Agent chat
and pick **feynman-technique**.

</details>

<details>
<summary><b>VS Code / GitHub Copilot</b></summary>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.copilot/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.copilot/skills/
```

Workspace-level: `.github/skills/` or `.agents/skills/`. Type `/` in Copilot Chat and
choose the skill. You can pass context after it:
`/feynman-technique the auth middleware in this repo`.

</details>

<details>
<summary><b>Gemini CLI</b></summary>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.gemini/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.gemini/skills/
```

Project-level: `.gemini/skills/` or `.agents/skills/`. Gemini CLI asks for consent before
activating a skill.

</details>

<details>
<summary><b>Everything else</b> — Amp, Goose, Kiro, Junie, Roo, Factory, Tabnine…</summary>

Most read one of these, in rough order of adoption:

```
~/.agents/skills/        # the emerging cross-tool convention
~/.claude/skills/        # widely supported as a fallback
<tool-specific>/skills/  # e.g. ~/.gemini/skills/, ~/.cursor/skills/
```

Drop the `feynman-technique` folder in whichever your tool documents. Full client list at
[agentskills.io/clients](https://agentskills.io/clients).

</details>

<details>
<summary id="any-other-ai-no-skills-support"><b>Any other AI</b> — no skills support needed</summary>

It's plain Markdown, so it works as a system prompt anywhere.

- **Custom GPT / Gem / Assistant:** paste
  [`skills/feynman-technique/SKILL.md`](skills/feynman-technique/SKILL.md) (minus the YAML
  block at the top) into the instructions field. Upload `references/` as knowledge files.
- **Project / custom instructions:** the same, in your project's instructions box.
- **One-off:** paste the file into chat and add *"Follow this for the rest of our conversation."*

</details>

### Did it load?

Ask about something you already know well:

```
/feynman-technique what is a hash function?
```

A correct answer opens with a one-sentence thesis, then a level 0 with **no technical
words at all**, and closes with "where the picture breaks". If it opens with *"A hash
function is a function that maps data of arbitrary size…"*, the skill didn't load.

---

## What comes back

```
In one sentence: ...          ← so an expert can stop reading here
The picture to hold: ...      ← the master analogy

0 · Kitchen table   no background in the field. Zero technical terms.
1 · Newcomer        the real names, tied to the level-0 picture
2 · Practitioner    how the pieces fit, and the first real trade-off
3 · Maintainer      failure modes, what breaks, what was rejected and why
4 · Specialist      edges, scale, and the limits of the model itself

Where the picture breaks      ← every analogy's limits, stated
Words introduced here         ← one line per new term
What I left out               ← named, not quietly dropped
```

Levels compress but never vanish. A narrow question gets **compact form** — thesis,
picture, the one level that matters. Marching an expert through five levels isn't
thoroughness; it measurably *degrades* their comprehension
([expertise reversal effect](skills/feynman-technique/references/evidence.md)).

📄 **[See a full answer, then annotated](skills/feynman-technique/assets/worked-example.md)** —
"what is a database index?" done properly, with every move labelled.

---

## Coach mode — the one that actually teaches you

```
/feynman-technique quiz me on how TCP handles congestion
```

Here it refuses to explain. **You** explain; it listens for vagueness, for technical words
used as stopping points, for steps asserted with no mechanism — and points at exactly one
hole at a time, without handing you the answer.

This is the mode with the strongest research behind it. Learners who prepare to teach
outperform learners who prepare for a test *even when the teaching never happens*
(Nestojko et al., 2014). Generating your own explanation beats reading someone else's
(Chi et al., 1989).

---

## The rules it follows

| | Typical "explain simply" prompt | This skill |
|---|---|---|
| **Jargon** | simpler sentences, same terms | every new term explained at first use, or it doesn't appear |
| **Analogies** | a fresh metaphor per paragraph | one master analogy, extended by complication — **and where it breaks** |
| **Accuracy** | simplified into being wrong | approximations marked *with their limits* |
| **Depth** | one flat level | a ladder you can get off at any rung |
| **Experts** | condescended to | thesis in line one, then compact form |
| **Names** | the name *is* the answer | mechanism first, name last |
| **Ignorance** | glossed over | "nobody knows" said plainly, where true |
| **Learning** | explains *at* you | coach mode makes *you* explain, and finds your holes |

Rule zero: **being clear is never an excuse for being wrong.** If simplifying would
distort, it says so, gives the limits, and delivers the exact version one level up.

---

## Under the hood

| File | What's in it |
|---|---|
| [**SKILL.md**](skills/feynman-technique/SKILL.md) | The skill itself. Start here. |
| [references/voice.md](skills/feynman-technique/references/voice.md) | Forensic style analysis of Feynman's prose, with corpus statistics |
| [references/ladder.md](skills/feynman-technique/references/ladder.md) | Level calibration and how to adapt the shape |
| [references/analogies.md](skills/feynman-technique/references/analogies.md) | Building, extending and stress-testing analogies |
| [references/failure-modes.md](skills/feynman-technique/references/failure-modes.md) | 14 ways explanations fail, each with a rewrite |
| [references/evidence.md](skills/feynman-technique/references/evidence.md) | The learning science — and where this method genuinely fails |
| [references/sources.md](skills/feynman-technique/references/sources.md) | Verified quotations, and the ones falsely attributed to him |
| [assets/checklist.md](skills/feynman-technique/assets/checklist.md) | The pre-send audit |

### From the style forensics

All measured against the 88,000-word corpus:

- **Burstiness is the signature.** Median sentence ≈ 20 words — but ~1 in 8 runs under
  eight words and ~1 in 6 past thirty-five. He builds long and lands short.
  *"Shake this one, that one shakes later."*
- **Pronouns switch by function.** "We" while teaching (19.95 per 1,000 words in *Six Easy
  Pieces*, ten times his "I"), "I" when admitting confusion (26.7/1k in the Nobel Lecture),
  "you" when instructing (20.6/1k in *Cargo Cult Science*).
- **Verbs a body can feel.** *jiggle* 27, *pull* 37, *push* 28, *shake* 20. Molecules
  jiggle; they do not "exhibit thermal agitation".
- **"Basically" appears zero times in 88,000 words.** *Trivial* appears once. That's why
  the skill bans them — measurement, not taste.

---

## Honest limitations

Rule zero applies to this page too.

- **Feynman did not invent "the Feynman Technique."** He never published a named four-step
  method. The four steps were assembled by later popularizers, chiefly Scott H. Young
  around 2011. This skill uses his *documented* tests instead, and says so.
- **"If you can't explain it simply, you don't understand it"** has no primary source for
  Feynman or Einstein. [sources.md](skills/feynman-technique/references/sources.md) lists
  what he verifiably said and what he didn't.
- **Some things do not simplify.** Feynman hit this wall himself: asked by his own father
  how a photon leaves an atom without having been inside it, he answered *"I'm sorry; I
  don't know. I can't explain it to you."* The skill is built to say that rather than fake
  a picture.
- **It costs tokens and time.** For a quick lookup, compact form — or no skill at all — is
  the right call.
- **It does little for memorisation or motor skills.** It targets causal, mechanistic
  understanding. Vocabulary and keybindings need spaced retrieval, not explanation.
- **A good explanation *feels* like understanding.** That feeling is not evidence. Where it
  matters, use coach mode.

---

## Credits and copyright

Richard P. Feynman (1918–1988) wrote everything worth reading here. This repository
contains **derived rules and short attributed quotations** used for analysis and
instruction — it does not redistribute his work.

His texts remain under copyright: *The Feynman Lectures on Physics* is free to *read* at
[feynmanlectures.caltech.edu](https://www.feynmanlectures.caltech.edu/) but is © Caltech
and **not public domain**. If you fork this, keep it that way: quote briefly, always
attribute, never paste chapters. Full provenance in
[sources.md](skills/feynman-technique/references/sources.md).

This skill began as `feynman-reply`, a Portuguese-language skill by
[@guicortei](https://github.com/guicortei). It was rebuilt from primary sources,
generalised beyond software, and extended with the style analysis, the evidence base and
coach mode — then renamed `feynman-technique`.

Not affiliated with or endorsed by the Feynman estate, Caltech, or Anthropic.

## Contributing

Improvements welcome — especially worked examples from other fields, failure modes found in
real use, and corrections to any quotation. See [CONTRIBUTING.md](CONTRIBUTING.md).

One request: if you add a claim about Feynman, cite the primary source. Being sloppy about
attribution while invoking his name for intellectual honesty is the one unforgivable bug
in this repository.

## License

[MIT](LICENSE). Use it, fork it, ship it.

---

<div align="center">

> *"The first principle is that you must not fool yourself — and you are the easiest person
> to fool."*
>
> — Richard Feynman, *Cargo Cult Science*, 1974

**[⭐ Star this repo](https://github.com/guicortei/feynman-technique)** if it changed an
answer you got today.

</div>
