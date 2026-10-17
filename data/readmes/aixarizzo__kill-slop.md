# kill-slop

Two Claude Code skills for finding and fixing AI-sounding text in writing that is supposed to sound like a person.

`kill-slop` is the workflow. Point it at a file or a pasted draft and it audits the text against the author's voice, reports every failing line with the reason and a suggested replacement, and applies only the fixes you approve. It runs one fix pass, two at most.

`anti-slop` is the method it loads: a catalog of AI tells, a scoring rubric, and a protocol for binding a voice from a file or from writing samples. It also works on its own when drafting new text.

## Where the method comes from

~18 papers on RLHF diversity collapse and voice replication, Wikipedia's WP:AISIGNS catalog, a 23,854-tweet single-author voice study, and a backtested voice-clone redteam. Banning words doesn't fix AI-sounding text, it produces a new recognizable style. So these skills judge against the author's real voice instead of a global banlist, and they flag repeating patterns, not single words.

## Install

```bash
git clone https://github.com/aixarizzo/kill-slop.git
cp -R kill-slop/anti-slop kill-slop/kill-slop ~/.claude/skills/
```

Then give it a voice to judge against: a voice file you maintain, 5 or more real writing samples, or a named register. With none of those, the skill stops and says so instead of grading your writing against a generic list.

## Use

```
/kill-slop path/to/draft.md
```

Or ask in plain words: "find the slop in this", "audit this deck", "make this sound like me". The anti-slop skill triggers on its own when you draft new text in Claude Code.

## How it judges

One suspicious word does not get flagged. Three catalog tells within about 100 words mark that span for a rewrite. The author's own habits set the limits, so if you use em dashes, em dashes are fine at your usual rate. Replacements are written the way the author writes, including their typos and irregular grammar when those are part of the voice, and the skill stops after two fix passes because over-corrected text is recognizable too. If the current session wrote the draft, the audit runs in a separate fresh-context agent instead of self-grading.

## Layout

```
kill-slop/
  SKILL.md                   # the audit-and-fix workflow
anti-slop/
  SKILL.md                   # the method
  references/
    master-list.md           # full consolidated catalog: tells, binding rules, gates, audit honesty
    tells.md                 # fast tell catalog with cluster rules and default caps
    audit-rubrics.md         # per-format gates and the score sheet
    generation.md            # verbalized-sampling recipes
    voice-binding.md         # building a voice card from samples
```

MIT licensed.
