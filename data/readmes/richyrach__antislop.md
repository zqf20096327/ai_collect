# Antislop

A guide your AI reads before it designs or writes anything, so the result is not one everybody has already seen.

It is six Markdown files. There is nothing to install, and it works with any AI tool.

![Four requests, each built twice by the same model. Left column: without the guide. Right column: with it.](docs/with-and-without.png)

The same model built each pair from the same one-line request. The left column had no guide. The right column had this one. All twenty pages are in [`evals/out/sonnet`](evals/out/sonnet).

## Use it

Paste this into ChatGPT, Claude, Cursor, Codex, Gemini, or any AI tool that can open a link, before you ask for a UI:

```
Before you design or build any UI, fetch this file and follow it:
https://raw.githubusercontent.com/richyrach/antislop/main/GUIDE.md
```

If your tool cannot open links, paste in the contents of [GUIDE.md](GUIDE.md).

To keep a copy in your project:

```bash
curl -fsSL https://raw.githubusercontent.com/richyrach/antislop/main/GUIDE.md -o DESIGN.md
```

Then add one line to `CLAUDE.md`, `AGENTS.md` or your Cursor rules: `Before any UI work, read DESIGN.md and follow it.`

To install it as an agent skill, with the reference files included:

```bash
npx skills add richyrach/antislop
```

## What it measured

Ten short requests, such as "I need a website for my family's bakery in Lisbon", were each sent to Claude Sonnet twice: once alone, once with the guide. A script then counted 27 known marks of AI-built pages in each result.

| | Without the guide | With the guide |
| --- | --- | --- |
| Marks per page, average | 4.4 | 1.3 |
| Pages with 4 or more marks | 7 of 10 | 0 of 10 |
| Pages with 0 or 1 marks | 1 of 10 | 5 of 10 |
| Pages with invented proof (reviews, founding dates, counts) | 3 of 10 | 0 of 10 |
| Pages using only the default sans-serif | 8 of 10 | 0 of 10 |

Read this with care:

- **It is small.** Ten requests, one page each way, one model. It has not been run on GPT or Gemini.
- **The guide and the counting script have the same author,** and the script counts the marks the guide names. Part of the gap is the guide teaching to its own test.
- **A count of marks does not say a page is good.** Look at [all ten pairs](evals/results/sonnet-pages.png) and judge for yourself.
- **Some marks survive.** Five of the ten guided pages still had small labels in spaced capitals, and two used cream paper with a serif.
- **The guide was revised once** after a first run, because its pages scored well and looked bare. Those pages are kept in [`evals/history`](evals/history/guide-v1).

The method, the per-page results and how to rerun it are in [`evals/`](evals/README.md).

## What is in it

| File | What it tells the AI |
| --- | --- |
| [GUIDE.md](GUIDE.md) | The core. Get the real material, take the design from the subject, meet a standard, never invent content. About 2,100 words. |
| [reference/visual-design.md](reference/visual-design.md) | Composition, hierarchy, colour, space, finish, and a self-review. |
| [reference/type.md](reference/type.md) | How to choose a typeface, how to self-host one, which fonts are already on each device, and other scripts. |
| [reference/images.md](reference/images.md) | Where to find real pictures, how licences work, and what to do when there are none. |
| [reference/writing.md](reference/writing.md) | How AI text gives itself away, in punctuation, structure, vocabulary and tone, and how to write instead. |
| [reference/product-ui.md](reference/product-ui.md) | Dashboards, tables, forms, settings, and every state a screen can be in. |

The core guide tells the AI which reference files to read for the task in front of it.

## Why it is not a list of bans

Ask an AI for a web page and you get one of a few pages. The [field guide](https://richyrach.github.io/antislop/) shows the four most common kinds and the marks that give each away.

[![Four drawings of AI-built pages with numbered marks: a purple SaaS landing page, a cream editorial page, a black and green developer page, and a dashboard of stat cards](docs/plates.png)](https://richyrach.github.io/antislop/)

The second and third kinds exist because people told their AI to avoid the first. A model that is only told what to avoid moves to its next most likely answer, and that answer is the same for everyone.

This repo did it too. Its first "good" example was a cream page with a serif, a red accent and a line of facts joined by dots. That is the second kind, and it is now [plate 2](specimens/tasteful-editorial.html). Its first guide then produced pages that avoided every mark and had nothing on them.

So the guide gives the AI a way to work and a standard to meet:

1. Find the real material first, pictures included, and ask for what is missing.
2. Write down what belongs to the subject's world, and take colour, type and layout from that.
3. Borrow the layout the subject already uses: a menu, a timetable, a receipt, a spec sheet.
4. Swap in a competitor's name. If the design still fits, start again.
5. Meet the standard: a composed first screen, one place the eye lands, type chosen for a reason, something worth looking at.
6. Never invent a customer, a figure, a review or a logo. Leave a marked slot for the owner instead.
7. Write plainly, with no sentence a competitor could print unchanged.
8. Pass a craft floor: contrast, keyboard, phone widths, right-to-left, and no third-party hosts.

Two things it stresses that the larger tools' READMEs do not mention:

- **Blocked networks.** The page must render with every third-party host unreachable. A blocking request to a font CDN is a blank page for people on filtered networks.
- **Right-to-left and non-Latin scripts.** Logical properties, a typeface drawn for the script, no letter-spacing or italics on Arabic-script text.

## How it compares

There are larger projects for this, and they do more. This table is from their READMEs in November 2026.

| | Antislop | [Impeccable](https://github.com/pbakaus/impeccable) | [Taste Skill](https://github.com/Leonxlnx/taste-skill) | [Hallmark](https://github.com/Nutlope/hallmark) |
| --- | --- | --- | --- | --- |
| What you get | Six Markdown files | Skill, 24 commands, detector | Skill, dealt palettes and layouts, checker | Skill, 50 themes, linter |
| Needs | Nothing | Node | Node 22+, Chrome | Node 18+ |
| Checks your code | Only a small script used for the test | Yes | Yes | Yes |

Use one of those if you want a scanner, slash commands or ready-made themes. Use this if you want something you can read in ten minutes, paste into any tool, and keep in your repo as plain text.

## What it has not got

- **A real scanner.** [`evals/detect.mjs`](evals/detect.mjs) counts marks in an HTML file. It reads source text only and was written for the test.
- **Results on other models.** Only Claude Sonnet has been tested.
- **Other languages.** The writing reference lists English patterns.

## Contributing

Seen a kind of slop that is not in the field guide, or a mark that is missing? [Open an issue](https://github.com/richyrach/antislop/issues/new/choose) with a screenshot or a link, and say what gives it away. Results from using the guide are welcome too, good or bad.

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to change the guide and run the test.

## Sources

The lists of marks were checked against these. The wording here is our own.

- Anthropic, [frontend-design skill](https://github.com/anthropics/skills/tree/main/skills/frontend-design)
- [Impeccable](https://github.com/pbakaus/impeccable), [Taste Skill](https://github.com/Leonxlnx/taste-skill), [Hallmark](https://github.com/Nutlope/hallmark)
- Developers Digest, [AI design slop: 16 patterns](https://www.developersdigest.tech/blog/ai-design-slop-and-how-to-spot-it)
- plagio.dev, [11 signs a website was built with AI](https://plagio.dev/blog/signs-a-website-was-built-with-ai)
- SCALR, [20 signs a website was made by AI](https://scalr.sg/blog/20-signs-a-website-was-made-by-ai/)
- 925 Studios, [AI slop design tells](https://www.925studios.co/blog/ai-slop-design-tells)
- Yeda AI, [Grep the three tells](https://yeda-ai.com/kb/ai-coding/grep-css-purple-gradients-centered)
- Wikipedia, [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- Dynatrace style guide, [Remove AI writing patterns](https://styleguide.dynatrace.com/docs/best-practices/remove-ai-writing-patterns-from-content)
- The Admin Bar, [How to edit AI website copy](https://theadminbar.com/how-to-edit-ai-website-copy/)

## Licence

[MIT](LICENSE)
