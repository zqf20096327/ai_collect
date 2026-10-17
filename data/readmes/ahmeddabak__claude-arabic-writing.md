# claude-arabic-writing

A skill for [Claude](https://claude.com) that makes it write and translate **Arabic that reads
correctly and naturally** — grammatically sound, free of typos, idiomatic, and free of the
tell-tale signs of machine translation.

It covers **Modern Standard Arabic (الفصحى)** plus four major dialects — **Egyptian, Levantine,
Gulf, and Maghrebi** — distilling authoritative grammar, orthography, style, and localization
references into guidance Claude applies automatically while it writes.

## Why you might want it

Out of the box, LLM Arabic often *looks* fluent but reads as translated: من قبل passives, قام
بـ + verbal noun, الخاص بك for every "your", drifting gender/number agreement, calqued
collocations, and Latin punctuation. This skill encodes the rules native editors apply, so the
Arabic Claude produces for you sounds like a person wrote it — not a machine.

With the skill installed, Claude will:

- **Write** original Arabic prose in the right register for your audience.
- **Translate** into Arabic (especially from English) by re-composing meaning, not transferring
  English word-for-word.
- **Edit / proofread** Arabic for hamza, ة/ه, ى/ي, agreement, iḍāfa, numbers, punctuation,
  collocations, and naturalness.
- **Pick the right variety** — formal MSA for documents, or a specific dialect for marketing and
  conversational copy — without mixing them.

## See it in action — أمثلة

> Arabic below renders right-to-left. The ❌ column is typical machine/LLM output; the ✅ column
> is what the skill steers Claude toward.

### Removing the "machine-translated" tells

| English | ❌ Translationese | ✅ Natural Arabic |
|---|---|---|
| The plan was reviewed by the committee. | تمت مراجعة الخطة من قبل اللجنة | راجعت اللجنةُ الخطة |
| The company conducted a study of the market. | قامت الشركة بإجراء دراسة للسوق | أجرت الشركةُ دراسةً للسوق |
| Update your account. | قم بتحديث الحساب الخاص بك | حدِّث حسابك |
| The new cars are fast. | السيارات الجديدة سريعون | السيارات الجديدة سريعة |
| This tool is used to organize files. | يتم استخدام هذه الأداة لتنظيم الملفات | تُستخدَم هذه الأداة لتنظيم الملفات |
| The goal of the project is to raise awareness. | الهدف من المشروع هو رفع الوعي | يهدف المشروع إلى نشر الوعي |

Each ✅ fixes a specific tell: active voice instead of `من قبل`, a single verb instead of
`قام بـ`, an attached suffix instead of `الخاص بـ`, feminine-singular agreement for a non-human
plural, the internal passive instead of `يتم`, and a fronted verb instead of the copular calque.

### Translating a full sentence (English → natural MSA)

> **English:** We design, build, and operate the systems that mid-sized businesses rely on —
> from cloud platforms to autonomous AI.
>
> **العربية:** نُصمِّم الأنظمةَ التي تعتمد عليها الشركات المتوسطة ونبنيها ونُشغّلها — من المنصّات
> السحابية إلى الذكاء الاصطناعي المستقلّ.

Note the verb-first sentence, the relative clause with a resumptive pronoun (`التي تعتمد
**عليها**`), and the non-human plural `الأنظمة` taking `التي`.

### The same message in MSA and each dialect

> **English:** I want to go now — where's the restaurant?

| Variety | الترجمة |
|---|---|
| MSA (الفصحى) | أريد الذهاب الآن، فأين المطعم؟ |
| Egyptian (مصري) | عايز أروح دلوقتي، المطعم فين؟ |
| Levantine (شامي) | بدّي روح هلّق، وين المطعم؟ |
| Gulf (خليجي) | أبغى أروح الحين، وين المطعم؟ |
| Maghrebi (مغاربي) | بغيت نمشي دابا، فين المطعم؟ |

Notice how the verb, the word for "want", "now", and "where" all change per dialect — and that
Egyptian moves the question word to the end.

### Proofreading

> **Input:** `انا ذهبت الى المدرسه , و قابلت ثلاث طلاب هناك`
>
> **Corrected:** أنا ذهبت إلى المدرسة، وقابلت ثلاثة طلاب هناك.

Fixes: `انا → أنا` and `الى → إلى` (hamza), `المدرسه → المدرسة` (ة), `ثلاث → ثلاثة` (number
polarity — a masculine counted noun takes the ة), plus the Arabic comma `،` with no space before
it and the attached `و`.

## Requirements

- [Claude Code](https://www.claude.com/product/claude-code) (or any client that supports Agent
  Skills via a `SKILL.md`).
- `git` (to clone) — or you can download the repo as a ZIP.

## Installation

### For all your projects (personal)

```bash
git clone https://github.com/ahmeddabak/claude-arabic-writing.git
cp -r claude-arabic-writing/skills/arabic-writing ~/.claude/skills/arabic-writing
```

### For a single project

```bash
git clone https://github.com/ahmeddabak/claude-arabic-writing.git
mkdir -p .claude/skills
cp -r claude-arabic-writing/skills/arabic-writing .claude/skills/arabic-writing
```

Start a new Claude Code session afterward so the skill is picked up. That's it — no build step,
no dependencies.

## Usage

The skill activates **automatically** whenever you ask for Arabic. You don't need to mention it
by name. For example:

- "Translate this product description into natural MSA."
- "Rewrite this welcome message in Gulf Arabic for a Saudi audience."
- "Proofread this Arabic paragraph and list the fixes."
- "Say this in Egyptian Arabic: …"
- "This Arabic reads like a machine translated it — make it sound native."

You can also invoke it explicitly with `/arabic-writing`.

## What's inside

```
skills/arabic-writing/
├── SKILL.md                 # entry point: workflow + correctness checklist + "AI smell test"
├── references/
│   ├── grammar.md           # word order, إعراب, agreement, iḍāfa, numbers
│   ├── orthography.md       # hamza, ة/ه, ى/ي, tanwin, punctuation, diacritics, typos
│   ├── translationese.md    # machine-translation tells + English→Arabic pitfalls
│   ├── collocations.md      # awkward-calque → natural tables + verb–preposition government
│   ├── register-and-style.md# register choice, connectors, naturalness, tone
│   ├── conventions.md       # transliteration, numerals, dates, units, bidi
│   └── dialects/
│       ├── egyptian.md
│       ├── levantine.md
│       ├── gulf.md
│       └── maghrebi.md
└── evals/
    └── evals.json           # objective test cases
```

It's built on **progressive disclosure**: `SKILL.md` stays short (a workflow, a top-10
correctness checklist, and a "smell test" for machine-made Arabic), and the detailed rules live
in `references/` files that Claude reads **only when relevant** — so the skill is thorough
without bloating Claude's context.

## Testing it yourself

`skills/arabic-writing/evals/evals.json` contains objective test cases — each with a prompt and
checkable expected behaviors — covering agreement, the قام بـ / من قبل tells, possessives,
proofreading, register choice, dialect fidelity, and numbers/dates. Run any of them with and
without the skill to see the difference.

## Caveats

- The bundled Arabic examples illustrate documented patterns; some pairs are constructed rather
  than quoted. **A native-speaker review is recommended before relying on the output for
  published material.**
- A few orthographic choices have more than one accepted convention (مسؤول/مسئول، مئة/مائة).
- For high-stakes localization, target a specific country (Egyptian, Saudi, Moroccan, …) rather
  than "Arabic" in general.

## Contributing

Issues and pull requests are welcome — corrections from native speakers and professional
translators especially. Good contributions include: additional calque→natural collocation pairs,
dialect refinements, and new eval cases that expose a failure mode.

## License

[MIT](LICENSE) — free to use, modify, and redistribute.
