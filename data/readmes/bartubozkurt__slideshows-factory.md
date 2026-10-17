# Slideshows Factory

A Claude Code workspace that turns your website into a brand brief, and screenshots of
TikTok slideshows into hooks, captions, and slide text for your own product.

**Output is text only.** It never generates, crops, or designs images. The deliverable is
always words you type into a slideshow editor yourself, plus a plain description of what
should be on each frame so you can go source it.

There is no code here. No install, no dependencies, no build step. It's a set of context
files and skills that Claude Code reads.

---

## Requirements

- [Claude Code](https://claude.com/claude-code) installed and logged in
- A website or store listing for your product (so `build-brand` has something to read)

## Run

```bash
git clone https://github.com/bartubozkurt/slideshows-factory.git
cd slideshows-factory
claude
```

That's the whole setup. `CLAUDE.md` loads automatically every session.

The `cd` matters — Claude Code reads `CLAUDE.md` and `.claude/skills/` from the directory you
launch it in. Start it anywhere else and you get a plain Claude session with none of this loaded.

---

## First session — build your brand file

Paste your URL and nothing else:

```
> https://yoursite.com
```

`build-brand` fires, reads your homepage plus up to 3 sub-pages, writes `context/brand.md`,
and shows you the pain points it extracted.

**Then correct those pain points by hand.** They drive every hook you will ever generate,
and a landing page describes features, not frustrations. Five minutes here is worth more
than any prompt tweak.

Anything the skill inferred rather than read is marked `[inferred]` so you know where to look.

---

## The four modes

Routing is automatic — you just send the thing.

| You send | Skill | You get |
|---|---|---|
| a URL | `build-brand` | `context/brand.md` filled in |
| a screenshot of someone else's post | `swipe` | breakdown + 5 hooks + slide text + 3 captions |
| your own photos | `photo-post` | 3 slideshows built around those exact frames |
| "give me ideas" | `make-slides` | batch of 3 full slideshow scripts |

**Image routing.** Both image skills trigger on images, so the image itself decides:

- Text overlay, a hook, visible slide structure, or app UI chrome → someone else's post → `swipe`
- A plain photograph with no text → your own asset → `photo-post`

### Reference posts

Drag a screenshot into the terminal, or save it to `inbox/` and say:

```
> swipe inbox/post3.png
```

You get the breakdown, 5 hooks, full slide text for the strongest one, and 3 captions.
The swipe file updates itself.

### Your own photos

```
> here are my photos [drag 5 images in]
```

Every slide gets assigned a specific photo letter or "plain text slide" — never a description
of an image you'd have to go find. It also tells you up front what your photo set *can't* do.

### Ideas with no reference

```
> give me 3 slideshow ideas
```

Say `more` for a fresh batch using different formulas and different pain points. It won't
re-serve the same angle with new words.

---

## Usage examples

A full walkthrough so you can see the shape of what comes back. The examples below use a
made-up invoicing app for freelancers called **Tally** — yours will read nothing like it,
that's the point.

### 1. First run

```
> https://tally.example.com
```

It fetches the homepage plus a few sub-pages, writes `context/brand.md`, and reports back
short:

```
Tally — invoicing for freelancers who don't want an accounting suite.

Pain points I extracted:
1. "i finish the work and then lose two hours making the invoice"
2. "i don't know if this month was good until my accountant tells me in april"
3. "chasing a late payment feels like begging someone who owes me money"
4. "i priced that job three months ago and still don't know if i made anything"  [inferred]
5. "every simple invoicing tool wants me to run a whole business dashboard"

Couldn't determine: price (no /pricing page), founder story, any traction numbers.
Proof section is empty, so F06 and F14 stay locked.
```

### 2. Correcting it — this is the five minutes that matters

Just talk to it. Pain points are the engine of every hook, and the ones it inferred from
marketing copy are usually the weakest:

```
> #4 is wrong. the real one is "i undercharged and i knew it while i was
  typing the number". and add: "i have three unpaid invoices and i've only
  chased one because the other two feel awkward"
```

It rewrites those lines in `brand.md`. Everything downstream improves immediately.

### 3. A batch of ideas

```
> give me 3 slideshow ideas
```

Full scripts go to `output/2026-08-14-batch-1.md`. The chat summary stays deliberately short:

```
1. F12 — "31 and still guessing whether this month was good"
2. F11 — "pov: it's the 14th and they still haven't paid"
3. F02 — "stop sending invoices from a word doc"

Written to output/2026-08-14-batch-1.md. Say the number for the full text.
```

Then:

```
> 2
```

```
### Slideshow 2 — F11 — the late payment spiral, from inside it

**Slide 1 (hook):** pov: it's the 14th and they still haven't paid
**Slide 2:** the invoice was due on the 1st. you sent it on the 28th.
**Slide 3:** you open the thread and reread your own message to check you weren't rude.
**Slide 4:** you draft a follow-up. you delete "just checking in" four times.
**Slide 5:** you send it anyway and feel weird about it. it's your money.
**Slide 6:** the fix isn't a better email. it's the invoice chasing them without you.
**Final slide (CTA):** tally does that part. free to start, link's in my bio.

**Caption:** the worst bit is rehearsing the follow-up like it's a hard conversation.
it's an invoice.
**Hashtags:** #freelance #freelancelife #selfemployed #invoicing #freelancetips
**Image direction:**
  1 — plain text slide, large type, flat background
  2 — screenshot of a calendar with the 1st and the 14th both visible
  3 — phone screen showing a sent email thread, sender name blurred
  4 — same thread with a half-typed reply visible
  5 — plain text slide
  6 — plain text slide
  7 — app screen showing an automatic reminder already sent
**Why this should work:** F11 keeps the reader inside the scene for four slides before any
point arrives, so the product reads as relief rather than a pitch.
```

### 4. Swiping someone else's post

Drag a screenshot in, or drop it in `inbox/` and name it:

```
> swipe inbox/post3.png
```

The breakdown is capped at six lines on purpose — it's scaffolding, not the deliverable:

```
Hook (verbatim): "nobody warns you about the 3rd month"
Slide count: 6
Structure: names the month → what breaks → why everyone hits it → three fixes → what changed
Formula: F08 (nobody-tells-you)
Mechanic: dates a specific moment, so the reader checks their own timeline against it
         before any advice arrives
Transfers to: pain #2 — not knowing whether a month was good until it's far too late
```

Then the actual output — 5 hooks carrying that same mechanic, each on a *different* pain
point rather than five rewordings of one:

```
1. nobody warns you about your third unpaid invoice
2. nobody tells you invoicing is most of the job
3. nobody warns you about the january after a good december
4. nobody tells you your best month can also be your worst
5. nobody warns you that "i'll invoice later" becomes march
```

Followed by full slide text for whichever hook is strongest, three captions at different
lengths (one under 8 words, one medium, one adding context the slides skipped), and:

```
logged as E01
```

That last line is the flywheel — the entry is now in `swipe-file.md` and every later batch
learns from it. If the post used a structure not in `formulas.md`, it gets appended as a
new `F##` too.

### 5. Your own photos

```
> here are my photos  [drag 5 images in]
```

It inventories them first, then names what the set can't do — which is the part that makes
this different from just generating copy and hoping you have matching images:

```
Photo A — laptop and coffee on a cafe table
Photo B — spreadsheet open, lots of red cells
Photo C — phone showing a payment notification
Photo D — you at a desk, mid-laugh, someone off-frame
Photo E — empty notebook and pen

Mix: 1 problem (B), 1 proof (C), 1 payoff (D), 2 texture (A, E).

The constraint: you have one problem shot and one proof shot, so anything built on
before/after will lean on plain text slides for the "before". That's native to the
format and costs nothing. F07 (versus) needs two comparable shots you don't have —
skipping it.
```

Every slide then gets assigned a specific photo letter or `plain text slide`. It never
describes an image you'd have to go find, because you already sent the images.

### 6. Iterating

Plain language works. A few that come up constantly:

```
> more
```
Fresh batch, different formulas, different pain points. It won't re-serve an angle.

```
> 3 is too soft. same hook, make the middle slides meaner
> kill F04, it doesn't fit us
> do #1 again but aim it at people who've been freelancing 5+ years
> that hook is 14 words
```

Tell it when a hook is bad. The feedback log at the bottom of `swipe-file.md` records what
you praised or killed, and later batches lean toward what you actually pick.

### 7. What it will push back on

Worth knowing before it surprises you:

```
> can you do one with a stat about how many freelancers get paid late
```
```
F14 is locked — brand.md has no sourced number, and I'm not going to generate a
plausible-sounding one. Give me a real stat with its source and it's usable.
Otherwise F11 or F12 hit the same nerve without needing a number.
```

Same for F06 (receipts) until you have real proof. Ask it to make or edit an image and it
describes the frame instead. Use a banned word in a request and it'll write around it.

---

## Structure

```
slideshows-factory/
├── CLAUDE.md                       # voice rules + output contract, loaded every session
├── .claude/
│   ├── settings.json               # pre-allowed permissions — read this before you run it
│   └── skills/
│       ├── build-brand/SKILL.md    # URL    -> brand.md
│       ├── swipe/SKILL.md          # their post -> hooks + captions + slide text
│       ├── photo-post/SKILL.md     # your photos -> 3 slideshows around those frames
│       └── make-slides/SKILL.md    # "ideas" -> batch of 3 scripts
├── context/
│   ├── brand.md                    # auto-filled from your URL, then hand-corrected
│   ├── formulas.md                 # 14 hook templates with slots and lock rules
│   ├── swipe-file.md               # few-shot library, grows as you send screenshots
│   └── scorecard.md                # six-dimension self-critique, runs before you see output
├── inbox/                          # drop screenshots here
└── output/                         # generated scripts, YYYY-MM-DD-batch-N.md
```

### The four context files

| File | What it does |
|---|---|
| `brand.md` | Your product, audience, pain points, tone. The source of every hook. |
| `formulas.md` | 14 hook templates. F06 and F14 are locked unless you have real numbers. |
| `swipe-file.md` | Posts that already worked, broken into structure. This is why output sounds like a real TikTok instead of marketing copy. |
| `scorecard.md` | PASS/WEAK/FAIL on six dimensions, run silently before anything reaches you. |

---

## Guardrails worth knowing about

These are enforced in `CLAUDE.md` and the skills, not suggestions:

- **Hook is 12 words or fewer.** If it needs more, the idea isn't sharp enough.
- **No invented numbers.** Formulas F06 (receipts) and F14 (statistic) stay locked until
  `brand.md` has real, sourced proof. It will tell you they're locked rather than make
  something up.
- **The product appears exactly once**, on the last or second-to-last slide, framed as a tool
  that happens to solve the problem — never as the point of the post.
- **A banned-word list** covers the usual LinkedIn residue ("unlock", "elevate", "game-changer",
  "seamless", "level up", "leverage", sentences starting with "Whether you're", and friends).
- **No `#fyp`**, no emojis in slide text, at most one in the caption.
- **Never generates images.** It describes what should be on screen; you source it.

You can change any of this — edit `CLAUDE.md`.

---

## Customizing

- **Voice rules and banned words** → `CLAUDE.md`
- **Hook formulas** → `context/formulas.md`. Add your own as `F##` with the same fields.
  When `swipe` finds a structure that isn't listed, it appends one automatically.
- **What counts as good** → `context/scorecard.md`
- **How a skill behaves** → the matching `SKILL.md`

---

## Notes and known rough edges

- **Output quality is bounded by `swipe-file.md`.** It starts empty and will say so. Ten
  entries in, it gets noticeably better. Aim to cover at least 4 different formulas.
- **Check `.claude/settings.json` before your first run.** It ships pre-allowing `Read`,
  `Write`, `Edit`, `WebFetch`, and `WebSearch` inside this folder, so setup isn't twenty
  permission clicks. That means Claude will write files here and fetch URLs without asking
  you each time. Every skill needs it — they all write to `context/` or `output/` — but it's
  your machine, so delete any line you'd rather approve manually.
- **WebFetch permission rules in Claude Code are unreliable**, so `settings.json` may not
  stop every prompt anyway. Approve the first few — it's once per domain.
- **Client-rendered sites may come back empty** from WebFetch. `build-brand` falls back to
  `curl`, and if that fails too it asks you to paste your copy directly rather than guessing
  at what your product does.
- **Feedback loop:** the log at the bottom of `swipe-file.md` tracks which formulas you praised
  or killed. Later batches lean toward what you actually pick — so tell it when a hook is bad.

---

## If you fork this

`context/brand.md` ships as an empty template and is tracked by git, so your filled-in version
will be committed if you push. That's fine for a private repo. If you're publishing your fork
publicly and don't want your positioning and pain points in it, either add `context/brand.md`
to `.gitignore` or reset it to the template before pushing.

`output/` and `inbox/` are already gitignored — your generated scripts and screenshots stay local.
