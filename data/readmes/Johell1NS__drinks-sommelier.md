# drinks-sommelier

<p align="center">
  <img src="img/drinks-sommelier-logo.png" alt="drinks-sommelier" width="600">
</p>

<p align="center"><b>English</b> · <a href="i18n/README.zh-CN.md">简体中文</a> · <a href="i18n/README.es.md">Español</a> · <a href="i18n/README.ja.md">日本語</a> · <a href="i18n/README.ko.md">한국어</a> · <a href="i18n/README.pt-BR.md">Português (Brasil)</a> · <a href="i18n/README.fr.md">Français</a> · <a href="i18n/README.de.md">Deutsch</a> · <a href="i18n/README.ru.md">Русский</a> · <a href="i18n/README.ar.md">العربية</a> · <a href="i18n/README.hi.md">हिन्दी</a> · <a href="i18n/README.it.md">Italiano</a></p>



<p align="center">
  <strong>A sommelier in your pocket, always by your side.</strong><br>
  <em>Shelves, menus, wine cellars: wherever you are, it knows what to recommend.</em>
</p>

> **A skill for AI agents.** OpenClaw, Hermes Agent, OpenCode, Claude Code, Cursor, and beyond.
> A virtual sommelier specialized in beers and wines that learns your personal
> tastes and suggests the best choice from any shelf, menu,
> or list. **Free, open-source, self-hosted.**

---

## Why it exists

At the restaurant, at the pub, at the wine shop, at the supermarket: the problem is always
the same. **Dozens of options and no certainty** about what to pick that is
truly suited to your tastes.

You could ask the waiter, open five tabs on your phone, or
hope that the prettiest name is also the best. Or you can ask
your AI agent — and it already knows what you like.

**drinks-sommelier** teaches any AI agent to act as a personal
sommelier. The agent:

1. Learns your taste preferences, once and for all
2. Analyzes any input: photo of a shelf, digital menus, lists
   of names written by the user
3. Searches for updated information on each product
4. Compares each product against your taste profile
5. Tells you exactly what to pick — and why

All in a transparent, honest, free way and without inventing anything.

---

## Benefits

- **Learns your tastes over time.** The more you use the skill, the more the agent
  knows your palate. Each interaction refines the profile.

- **Beers and wines in a single skill.** You do not need to install two separate
  skills. The agent handles both categories, automatically recognizing
  what it is analyzing.

- **Analysis from images and text.** Take a photo of a shelf, a menu,
  a wine list. Or write a list. The agent extracts only
  the relevant products (beers and wines), ignoring everything else.

- **No hallucinations.** The agent has the absolute prohibition of using
  its own pre-training knowledge. Each product is
  promptly researched on the web before being evaluated.

- **Preference index 0-100%.** Each suggestion has a clear
  score that says how well a product fits your tastes. No
  half measures.

- **Persistent taste profile.** Your preferences are saved in
  readable and editable text files. They are not lost between
  one session and the next.

- **Agent-guided setup.** The first time, the agent asks you the
  right questions to understand your tastes, without leaving you in front of
  manual configurations.

- **Open-source, MIT license.** Free, no subscriptions, no
  API keys, no limits. You can use it, modify it, distribute it.

- **Works with any AI agent.** Written for OpenCode, but
  easily convertible for OpenClaw, Hermes Agent, Claude Code, Cursor,
  GitHub Copilot, and any other agent. Show this README to your
  agent for a simple and automatic conversion.

- **Fully customizable.** SKILL.md is a text file.
  Add rules, modify criteria, adapt it to your workflow.

---

⭐ **Enjoying drinks-sommelier?** Star the repo, follow the project,
and help it grow. The best recommendations are the ones you share —
suggestions and contributions are always welcome.

---

## How it works

The process is divided into 5 phases, executed in sequence by the agent each
time it is queried.

### Phase 1 — Taste profile setup (one-time)

The first time the skill is loaded, the agent checks whether the
paragraphs "User's tastes for beers" and "User's tastes for
wines" in SKILL.md have already been filled in.

If they have not, the agent opens the file `data/SETUP.md` which contains:
- Guiding questions to gather preferences (sweet/bitter, alcohol content,
  liked and disliked styles, etc.)
- Examples of correctly filled-in paragraphs
- Examples of populated `data/` files

The agent asks you the questions, collects the answers, and modifies
the two taste paragraphs in SKILL.md. If during the
setup the user mentions specific products, the agent
records them in the corresponding `data/` files (optional
operation but useful to refine the profile).

You can also fill in the paragraphs by hand, if you prefer.

The files `data/known-preferred-beers.md` and `data/known-preferred-wines.md`
are optional and contain specific products you have already evaluated
in the past. The more complete they are, the more the agent understands your nuances.

### Phase 2 — Input analysis

The agent identifies what you have available and in what format:

- **Text**: extracts the names of beers and wines from a written list
- **Image**: analyzes the photo (shelf, menu, wine list) and
  recognizes only products that are beers or wines.
  Completely ignores: spirits, liquors, snacks, meals,
  desserts, sodas, accessories. Anything that is not beer or wine.
- **Mixed**: if you send both text and images, it analyzes everything.

If the input is not clear, the agent asks before proceeding.

### Phase 3 — Web research (anti-hallucination)

The agent has the **absolute prohibition** of using its own
pre-training knowledge to evaluate a product. It could be obsolete,
imprecise, or worse: invented. For this reason, it performs a targeted web search
on each and every identified product.

What the agent searches for:

| Category | Collected information |
|---|---|
| **Beers** | Style, alcohol content, sweetness, bitterness (IBU), body, aromatic notes, ingredients |
| **Wines** | Grape variety, appellation, production area, vintage, body, acidity, tannicity, alcohol content, sweetness notes |

If a product is not findable online, the agent honestly states it
and does not invent characteristics.

### Phase 4 — Evaluation

The agent compares each product against your taste profile, which has
two distinct levels:

1. **Taste rules** — the general guidelines you have written
   in the taste paragraphs (e.g. "sweet beers", "wines not too
   sweet", "alcohol content ≤ 9°"). They are binding.
2. **Products in data/ files** — concrete examples of beers and wines
   that you liked or disliked. They serve to calibrate the
   taste rules (e.g. if you love beer X and hate Y, the agent
   understands what you mean by "sweet" and "bitter").

The agent assigns a **preference index from 0 to 100%**:

| Index | Meaning |
|---|---|
| 90-100% | Product perfect for your tastes |
| 70-89% | Excellent, slight discrepancies |
| 50-69% | Acceptable, but not optimal |
| 30-49% | Poorly suited to your tastes |
| 0-29% | To avoid |

If you have indicated a food context, the agent also evaluates
the food pairing (secondary priority).

### Phase 5 — Recommendation

The agent structures the response clearly:

1. **First choice**: the best product with preference index
   and explanation of why it is suitable for your tastes
2. **Alternatives** (if present): in descending order of preference
3. **Pairings**: food pairing suggestions for the products
4. **Products to avoid**: those that clearly do not respect
   your tastes, with explanation

---

## Project structure

```
drinks-sommelier/
├── README.md                ← This file
├── LICENSE                  ← MIT License
├── .gitignore
├── img/                     ← Logo and graphic assets
├── i18n/                    ← Translations
└── skills/
    └── drinks-sommelier/    ← The actual skill
        ├── SKILL.md         ← Complete instructions for the agent
        │                      (frontmatter, tastes, operations,
        │                       edge cases, best practices, examples,
        │                       preference updates)
        └── data/
            ├── SETUP.md                   ← Initial setup guide
            │                                (used only on first launch)
            ├── known-preferred-beers.md   ← Liked and disliked beers
            │                                (to be filled in with use)
            └── known-preferred-wines.md   ← Liked and disliked wines
                                              (to be filled in with use)
```

---

## Installation

You can install the skill in two ways:

### With npx skills (recommended)

```bash
npx skills add Johell1NS/drinks-sommelier --skill drinks-sommelier
```

### With git clone

```bash
git clone https://github.com/Johell1NS/drinks-sommelier.git
```

> **Note:** unlike `npx skills add`, git clone does not know where your
> agent's skills are stored. You need to place the skill in the correct
> path for your agent (e.g., OpenCode uses `~/.config/opencode/skills/`,
> other agents may differ). Once it's there, the agent detects it
> automatically.

---

## Configuration

The skill needs to know your tastes to work. You can
configure it in two ways:

### Guided configuration (recommended)

After installing the skill, ask your agent something like
"Help me configure the drinks-sommelier skill". The agent will load
SKILL.md, find the taste paragraphs still to be filled in, and
guide you through the initial setup using `data/SETUP.md`.

Alternatively, simply ask for a beer or wine recommendation:
the agent will automatically detect that the skill is not initialized
and will ask you the right questions.

### Manual configuration

Open `SKILL.md` and fill in the paragraphs:

**User's tastes for beers**
```
I prefer sweet and not bitter beers.
They must not exceed 9° alcohol by volume.
I like Belgian styles and fruity beers.
I dislike IPAs, stouts, and beers that are too bitter.
```

**User's tastes for wines**
```
I prefer red wines that are not too sweet.
For whites, I prefer vermentino and sauvignon.
I like wines with good acidity and freshness.
I dislike passito or fortified wines.
```

You can also populate the files `data/known-preferred-beers.md` and
`data/known-preferred-wines.md` with specific products you have
already tried and evaluated. This part is optional but useful
for refining the profile.

**Example — `data/known-preferred-beers.md`**
```
# LIKED BEERS
- Kwak
- Triple Karmeliet
- La Trappe Blond
- Flea Margherita

# DISLIKED BEERS
- Any IPA
- Stout
- Beers with alcohol content above 9°
```

**Example — `data/known-preferred-wines.md`**
```
# LIKED WINES
- Vermentino Costamolino
- Syrah Soraia Casale Valle Chiesa
- Rebeca Firriato

# DISLIKED WINES
- Passito wines
- Fortified wines
```

### Updating over time

Every time you express a judgment on a product ("I like this one",
"I don't like this one"), the agent automatically updates the
`data/` files. The taste rules in the SKILL.md paragraphs, on the other hand,
are updated only with your explicit confirmation, because
they are binding for future evaluations.

---

## Usage examples

### Scenario 1 — Wine shelf (image)
You take a photo of a wine shop shelf. The agent identifies the wines,
researches them all on the web, compares them against your profile. It tells you
which one to pick, why, and what to pair it with.

### Scenario 2 — Beer menu (image)
You take a photo of a pub's beer menu. The agent ignores cocktails,
spirits, etc... analyzes only the beers, searches for information on
each one. It suggests the beer most suited to your tastes.

### Scenario 3 — Mixed text list
You write "I have these wines: Chianti Classico, Vermentino Costamolino,
Amarone. And these beers: Kwak, local craft IPA, Leffe Blonde."
The agent evaluates both categories and tells you what the best
choice is overall.

### Scenario 4 — Request without a list
"I need to get a wine for a dinner, what do you recommend?" The agent
does not invent. It asks what you have available, what kind of dinner,
and if you already have any wines in mind.

### Scenario 5 — New preference expressed
After a suggestion you say "I really liked that beer".
The agent adds it to your favorites and updates the profile
to be even more precise next time.

---

## What this skill does NOT do

- **It does not provide professional tasting evaluations.** The
  suggestions are based on objective data (style, alcohol content,
  bitterness) and on declared preferences. It does not replace a
  human sommelier in formal contexts.

- **It does not handle other beverages.** Spirits, cocktails, liquors,
  sodas, non-alcoholic drinks — anything that is not beer or wine is
  ignored.

---

## Suggestions (optional)

**drinks-sommelier** works with any web search tool your agent natively
supports. If your agent already has reliable web search capabilities,
you do not need anything else.

However, if you want to ensure thorough, anti-bot-resistant searches
every time (especially useful when product pages are behind anti-bot systems),
consider installing the companion
**[browser-search](https://github.com/Johell1NS/browser-search)** skill.
It searches dozens of engines simultaneously and helps the agent find
product information even when standard tools struggle.

---

## License
MIT
