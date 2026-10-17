# Claude Code for Non-Coders

**The complete method a non-developer uses to build a real application with
Claude Code — without being able to read the code it writes.**

This repo is not a collection of prompt tips. It's a **governance system**:
how to decide, verify, constrain, and sustain a software project when you
can't personally review what the AI produces. Everything here was forged on a
real project — a family mobile app (React Native + Firebase, some thirty
server functions, security rules tested in continuous integration) — by
someone whose job is not software development.

Every rule in this repo was born from a real accident. These are scars, with
the user manual attached.

## One-sentence install

Paste this into Claude Code:

> *"Read https://raw.githubusercontent.com/Arlenjim/claude-code-for-non-coders/main/INSTALL.md
> and follow its instructions."*

Claude becomes your **private technical installer**: you hand it the keys to
the site, it puts up its own scaffolding. It installs the skills, asks you
three questions to fit the method to YOUR project, and explains every piece
as it lays it down. Nothing is overwritten without your consent, no guardrail
is imposed. (Manual install: see "Where to start" below.)

🇫🇷 Ce dépôt est né en français — voir [README.fr.md](README.fr.md).

## The story in three acts

**Act 1 — over-armoring.** At first, the fear of not being able to verify the
code produced a pile of guardrails: six automatic blocking hooks, a mandatory
planning process for the smallest edit, isolated environments, numbered
rituals. The result: lots of friction, false positives, and the real risk —
errors of *judgment* — slipped through anyway.

**Act 2 — "lighten, don't harden."** An external audit and a few incidents
led to this method's central decision: we **removed** four hooks out of six,
made the heavyweight process optional, and moved trust to the only barriers
that deserve it — tests replayed automatically by CI. A general-contractor
process is absurd for changing a light bulb.

**Act 3 — balance.** Few barriers, but the right ones, on the right tier:
discipline rules that are always loaded, method skills you can invoke, a
written doctrine for the critical domain, deterministic tests in CI, and a
session ritual that lets a memoryless AI pick the work back up cold.

## What's in this repo

```
INSTALL.md              The install instructions — written for Claude,
                        not for you (see "One-sentence install")
CLAUDE-global.md        The rules file loaded into ALL your sessions
                        (copy to ~/.claude/CLAUDE.md and adapt)
skills/                 3 generic method skills, ready to copy
                        into ~/.claude/skills/
  work-discipline/          decompose, prove, refuse shortcuts
  scientific-debugging/     reproduce, bisect, prove the cause
  framing-vague-requests/   turn a vague request into executable work
templates/              The files to create in every long-lived project
  SESSION-HANDOFF.md        the handoff journal between sessions
  CLAUDE-project.md         the minimal project CLAUDE.md (incl. the
                            "non-negotiable domain")
  PROJECT-RESUME.txt        the ready-to-paste session opener
guardrails/             The 6 defense patterns + what we removed and why
  hooks-templates/          2 generic fill-in-the-blanks hooks, ready to wire
field-notes/            The method confronted with the wild — viral tips,
                        incidents, hard questions, and what we keep from them
examples/               The method shown, not told — a real session handoff,
                        the ritual catching real drift, and the lessons
```

## Where to start (manual install)

The automatic path is above ("One-sentence install"). If you'd rather lay
everything down yourself:

1. **Copy `CLAUDE-global.md`** to `~/.claude/CLAUDE.md` (create the folder if
   needed) and replace the `<...>` fields: your first name, your technical
   level, your paths.
2. **Copy the three folders from `skills/`** into `~/.claude/skills/`.
3. **On your first long-lived project**, ask Claude to initialize the setup
   (the "Bootstrapping" section of CLAUDE-global): it will create the
   handoff, the project CLAUDE.md, and the resume template.
4. **Read `guardrails/README.md`** before adding any automatic guardrail. The
   classic mistake is adding too many, not too few.

## The five principles that carry everything

1. **Front-loading**: the pilot's effort is spent BEFORE the work (precise
   brief, written constraints, chosen execution mode), not during it. A fuzzy
   brief costs more than any AI mistake.
2. **Asking ≠ announcing**: an AI announcing what it's about to do has not
   asked permission. Any scope extension requires a question and an answer.
   And a flagged problem = full stop ("flag then STOP") — no coding in the
   same breath.
3. **The non-negotiable domain**: every project has a zone where a mistake is
   expensive (money, data, security). You define it in writing and apply a
   reinforced protocol there — everywhere else, you lighten up.
4. **The guardrail hierarchy**: tests replayed in CI (deterministic) >
   specialized review (probabilistic) > regex hooks (cosmetic). Place your
   trust on the highest tier available, never in a lint.
5. **Proof, not narrative**: "it should work" is not verification; an agent's
   report is not proof; a stale doc map is worse than no map. Everything gets
   verified observably.

## Who this is for

This repo doesn't teach you to code: it teaches you to **act as a technical
director in front of a team of virtual developers**. It's for anyone driving
Claude Code (or an equivalent tool) on a project that matters, **without
being able to read the code in depth**: non-technical founders, designers,
product managers, side-project artisans. Developers will find plenty here
too — half of these rules are simply good engineering, written to be demanded
rather than performed.

## What this repo is not

- **A service.** Maintained as a field-tested method: no individual support
  guaranteed, no feature roadmap — but reproducible failures, documented
  incidents, and evidence-backed improvements are actively reviewed. The
  [scar-report issue template](.github/ISSUE_TEMPLATE/scar-report.yml) is
  the front door.
- **A guarantee.** This method drastically reduces the damage; it replaces
  neither a security audit nor a developer for the stakes that require one.
- **Dogma.** The method itself was cut down once ("lighten, don't harden").
  Take what serves you, discard the rest — but discard knowingly: every piece
  documents the problem it solves.

## Built the same way

Two small reference sites this same non-coder built with Claude Code, kept as
living examples of the method applied end to end (brief, build, verify, ship):

- **[skillinjection.com](https://skillinjection.com)** — a plain-language
  definition of *skill injection*, an attack class against LLM agent skills.
- **[sleeperattack.com](https://sleeperattack.com)** — a plain-language
  definition of *sleeper attack*, a dormant compromise of an LLM agent's memory.

## License

MIT — see [LICENSE](LICENSE). Do what you want with it; a mention is
appreciated, not required.
