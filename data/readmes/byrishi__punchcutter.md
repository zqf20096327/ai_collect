<p align="center"><img src="assets/banner.jpg" alt="punchcutter: describe a typeface, get a font family" width="100%"></p>

# punchcutter

[![skills.sh](https://skills.sh/b/byrishi/punchcutter)](https://skills.sh/byrishi/punchcutter) [![Docs](https://img.shields.io/badge/docs-byrishi.github.io-5f6b2f)](https://byrishi.github.io/punchcutter/) [![License: MIT](https://img.shields.io/badge/license-MIT-5f6b2f)](LICENSE) [![Works with](https://img.shields.io/badge/works%20with-Claude%20%C2%B7%20ChatGPT%20%C2%B7%20Codex%20%C2%B7%20Cursor-5f6b2f)](#install)

**A type foundry that lives inside Claude, ChatGPT, Codex and other AI agents.** Describe a typeface, or write on a sheet of paper and send a photo. Punchcutter draws it, spaces it, kerns it, tests it and hands back a real font family with its own Studio app.

Every word in the images on this page is set in a font Punchcutter made. **Docs: [byrishi.github.io/punchcutter](https://byrishi.github.io/punchcutter/)** · Guides: [Getting started](https://byrishi.github.io/punchcutter/getting-started.html) · [Handwriting and photos](https://byrishi.github.io/punchcutter/handwriting.html) · [Use your font](https://byrishi.github.io/punchcutter/using.html) · [CLI](https://byrishi.github.io/punchcutter/cli.html)

<p align="center"><img src="assets/gallery.png" alt="Five families made with Punchcutter" width="100%"></p>

## Six ways in

```
✦ punchcutter  ·  type foundry

  1  Describe it        One sentence about the feeling you want. Get a full family.
  2  Your handwriting   Print the sheet, write on it, send a photo. The best photo route.
  3  Quick photo        A photo of any writing or lettering. No sheet needed.
  4  Match a mood       Send a picture you love. Get an original family with that feeling.
  5  Remix              Change a Punchcutter font: weight, width, spacing, single letters.
  6  Open base          Start from a free font with wide script coverage and reshape it.
```

**Or start from an open font.** Route 6 takes an SIL OFL variable font with wide coverage (Roboto Flex, Noto Sans and Serif, Inter, Fraunces, Recursive, Noto Sans Devanagari and Gujarati) and reshapes it: pin any axis, track, slant, round the corners. The remix ships under the OFL with a new name and the original credited.

**Describe it**

```
> a font for my coffee brand. warm, round, a bit playful. call it Pomelo.
```

**Or write it and send a photo.** Print [the sheet](assets/punchcutter-handwriting-sheets.pdf), fill it in, take a phone photo at any angle.

| 1. Print | 2. Write | 3. Photograph |
| --- | --- | --- |
| <img src="docs/assets/sheet-blank.png" alt="Blank sheet" width="260"> | <img src="assets/demo-sheet-filled.jpg" alt="Filled sheet" width="260"> | <img src="assets/demo-sheet-photo.jpg" alt="Phone photo of the sheet" width="260"> |

<p align="center"><img src="assets/photo-to-font.jpg" alt="The photographed sheet and the two-weight font made from it" width="100%"></p>

Corner markers square up the photo, the red guides drop out, each letter is traced, and the writer's x-height and stroke weight are measured. Anything you did not write (accents, symbols, currency) is drawn at your stroke weight, so the font is always complete. *The demo writing is simulated.*

**No printer? Any paper works.** Write on a notebook page and send the photo. Punchcutter finds and numbers each character, reads them and traces them. "Sphinx of black quartz, judge my vow" covers a to z. The sheet gives the cleanest result.

<p align="center"><img src="assets/demo-plain-paper-found.jpg" alt="Characters found and numbered on plain notebook paper" width="80%"></p>

## What you get

- Variable font with a weight axis (drawn fonts), plus static TTF and OTF for every weight
- WOFF2 web fonts and ready `@font-face` CSS
- 362 glyphs: Latin for 43 languages including Central European, Baltic, Turkish and Romanian, figures, punctuation, currency
- Overlaps merged and corners softened in proportion to the stroke, so edges look drawn, not generated
- Automatic optical spacing and class kerning
- OpenType features: tabular figures, slashed zero, alternate a, case-sensitive punctuation
- A QA report and proof sheet
- UFO sources you can open in Glyphs, FontLab or RoboFont
- **Studio**: one self-contained HTML file per font

### Studio, the font's own app

<p align="center"><img src="assets/studio.jpg" alt="Punchcutter Studio" width="100%"></p>

A foundry-grade specimen app for every font:

- **Type tester** with text presets, alignment, case, colourways, OpenType switches and a side-by-side comparison with system fonts
- **Waterfall** and an **animated weight axis** for variable families
- **Glyph inspector**: search, categories, the outline with every point and handle, metrics, copy as character or SVG
- **Kerning explorer**: any pair, kerned and unkerned, plus the pairs that needed the most care
- **Design lab**: a live slider for every axis of the font's parametric design space (weight, width, x-height, thin strokes, squareness, softness, aperture, slant), presets, Surprise me, and a button that copies the settings back to your AI to cut the family
- **In use**: eight photographs (street poster, business cards, storefront, coffee bag, billboard, tote, book cover, phone) with the type mapped onto each surface in true perspective and printed into the photo, so folds, weave and shadows fall across it; your name, line, weight and colourway; download any scene as a PNG
- **Language support** counted from the font's own character set
- **Specs**: vertical metrics, features, file list and the full QA report
- **Install guides** for Mac, Windows, Linux, websites, Tailwind, Next.js, Figma, Canva and Word, with copy buttons
- **Downloads**: the whole family or any single file, and a printable specimen

<p align="center"><img src="assets/mockups.jpg" alt="Burin Grotesk set live in the Studio's photo mockups" width="100%"></p>

All fonts are embedded, so it works offline, as an email attachment, hosted anywhere, or published as an artifact that opens right inside the Claude chat. A prebuilt one is in [`examples/fonts/PomeloRound/studio.html`](examples/fonts/PomeloRound).

## Install

Pick your tool. Every route needs Python 3.10+.

### Claude Code

As a plugin (adds the skill and the `/punchcutter` command):

```
/plugin marketplace add byrishi/punchcutter
/plugin install punchcutter@punchcutter
```

Or as a plain skill:

```bash
npx skills add byrishi/punchcutter
```

Or by hand:

```bash
git clone https://github.com/byrishi/punchcutter
mkdir -p ~/.claude/skills && cp -r punchcutter/skills/punchcutter ~/.claude/skills/
```

Then install the Python libraries once:

```bash
pip install -r ~/.claude/skills/punchcutter/scripts/requirements.txt
```

Say "make me a font" or type `/punchcutter`.

### Claude app (web, desktop, mobile)

1. Download [`punchcutter.skill`](https://github.com/byrishi/punchcutter/releases/latest/download/punchcutter.skill).
2. In Claude: Settings, then Skills, then upload the file. Code execution must be on.
3. Start a chat: "make me a font".

Claude installs the libraries itself on first use. The Studio opens in the chat as an artifact.

### Claude Desktop, Cursor, Windsurf, VS Code and other MCP clients

Punchcutter ships an MCP server, so it shows up as a set of tools (`menu`, `new_font`, `build_font`, `handwriting_sheet`, `read_sheet_photos`, `find_letters`, `label_letters` and more).

```bash
pip install "punchcutter[mcp] @ git+https://github.com/byrishi/punchcutter"
```

Add to the client's MCP config (`claude_desktop_config.json`, `.cursor/mcp.json`, and so on):

```json
{
  "mcpServers": {
    "punchcutter": { "command": "punchcutter", "args": ["mcp"] }
  }
}
```

Claude Code can add it in one line: `claude mcp add punchcutter -- punchcutter mcp`

### ChatGPT

ChatGPT connects to remote MCP servers in developer mode. Run the server over HTTP and point ChatGPT at it:

```bash
pip install "punchcutter[mcp] @ git+https://github.com/byrishi/punchcutter"
cloudflared tunnel --url http://localhost:8000            # or ngrok http 8000
punchcutter mcp --http --public-url https://YOUR-TUNNEL-ADDRESS
```

ChatGPT: Settings → Apps & Connectors → Advanced → Developer mode → Create → `https://YOUR-TUNNEL-ADDRESS/mcp`, no authentication. Proofs come back as images; the Studio and fonts as download links. A `Dockerfile` is included to host it permanently. [Full guide](https://byrishi.github.io/punchcutter/getting-started.html#chatgpt)

### Codex

```bash
npx skills add byrishi/punchcutter --agent codex     # then: $punchcutter
codex mcp add punchcutter -- punchcutter mcp         # or as an MCP server
```

### Gemini CLI, Copilot, Aider and other coding agents

Clone the repo and point the agent at it. [`AGENTS.md`](AGENTS.md) tells it what to do.

```bash
git clone https://github.com/byrishi/punchcutter && cd punchcutter
pip install -r skills/punchcutter/scripts/requirements.txt
```

Then ask: "Follow AGENTS.md and make me a rounded friendly font called Pomelo."
The agent needs to be able to view images to check its proofs.

### No AI at all

```bash
pip install "git+https://github.com/byrishi/punchcutter"

punchcutter menu
punchcutter new "My Sans" --preset humanist --weights 300,400,700
punchcutter build MySans.json --draft        # seconds: static fonts + proof
punchcutter build MySans.json                # full release + Studio
punchcutter glyph MySans.json a g R          # close-up of letters

punchcutter sheet                            # printable handwriting sheets
punchcutter read-sheet page1.jpg page2.jpg --family "My Hand" --weights 400,700
punchcutter build MyHand/MyHand.json
```

macOS: the proof image and sheets need Cairo (`brew install cairo`).

## How it works

Punchcutter runs the stages a type foundry does, and shows each one:

```
✦ punchcutter  type foundry
[1/9] Brief               Burin Grotesk: preset grotesque, 5 weights, 3 masters
[2/9] Drawing             301 glyphs per master (138 accented composites)
[3/9] Spacing             wght 400: stem 84, n 584, o 576, H 713
[4/9] Kerning             150 left classes x 129 right classes, 9697 pairs
[5/9] OpenType features   kern, case, tnum, zero, ss01
[6/9] Sources             3 UFO masters + designspace
[7/9] Compile             variable TTF, static TTF and OTF, WOFF2
[8/9] Quality assurance   140 checks on 11 files: 140 pass, 0 warn, 0 fail
[9/9] Release package     studio.html, CSS, README, report
```

| Stage | What happens |
| --- | --- |
| **Drawing** | Letters are built from strokes, like a pen. One pen model gives every glyph the same weight, contrast, joins and terminals. Photo routes trace the writer's ink instead. |
| **Spacing** | Sidebearings are computed from the white space around each shape, so straight, round and diagonal letters end up evenly spaced. |
| **Kerning** | Every pair is measured in 2D. Pairs with too much air (AV, To, LT) are pulled together, collisions are pushed apart, and glyphs that behave alike are merged into classes. |
| **Compile** | Masters are point-compatible by construction, so they interpolate into a variable font. Built with fontmake, the toolchain used for Google Fonts. |
| **QA** | Coverage, metrics, naming, kerning, features and variation tables are verified on every file. A failed check fails the build. |
| **Critique** | The AI looks at the proof sheet, finds weak letters, changes the design and rebuilds. Several rounds before anything ships. |

## Make it yours

**Say it.** "Tighter. More contrast. Make the bold heavier. Square dots."

**Tune it.** Thirty design parameters on top of eight presets: `geometric`, `grotesque`, `humanist`, `rounded`, `slab`, `technical`, `condensed`, `contrast`. See [parameters](skills/punchcutter/references/parameters.md). For handwriting: `--neat` (how tidy), `--ink` (how heavy), `--even` (one steady pen, for phone photos), extra weights. See [handwriting](skills/punchcutter/references/handwriting.md).

**Redraw it.** Any letter can be replaced with a custom drawing in a few lines, and stays consistent in every weight. See [drawing](skills/punchcutter/references/drawing.md).

```python
@glyph("Q", 0x51, "uc")
def Q(g):
    L.O(g)                                   # the stock O, then a tail that swings out under it
    w = g.Ow
    g.add(g.P().m(w * 0.5, g.cap * 0.14, -35).c(w * 0.8, -g.cap * 0.05, "E").c(w * 1.02, g.cap * 0.02, 25))
```

<p align="center"><img src="assets/glyph-inspector.png" alt="Custom letters across weights" width="80%"></p>

## Brand

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/lockup-dark.svg">
  <img src="assets/lockup.svg" alt="punchcutter" width="320">
</picture>

A hand-drawn mark, small, in a wide grainy field. Meadow `#5f6b2f` (the only accent), sage `#a9ae86`, straw `#d8cc98`, sky `#cdd9dc`, cream `#f4efe4`, ink `#171612`. Wordmark in Pomelo Round, text in Burin Grotesk, both made here. Fields are generated from noise, not photographs. Every page, proof, sheet and image reads these from one file, [`pc/brand.py`](skills/punchcutter/scripts/pc/brand.py). Full guidelines: [Brand](https://byrishi.github.io/punchcutter/brand.html).

## Honest limits

- Latin only for now (Basic Latin, Latin-1, Latin Extended-A accents).
- Upright styles; `slant` gives an oblique, not a true italic. Sans and slab designs; no bracketed serifs or blackletter yet.
- Handwriting fonts are print-style and static: joined cursive comes out as separate letters, and there is no variable axis.
- Unhinted outlines: sharp on phones, macOS and modern Windows; softer at very small sizes on old Windows.
- The output is a solid, usable family. A retail type designer would still refine curves and kerning by eye; the UFO sources are there for that.
- Make original fonts. Punchcutter is not for cloning commercial typefaces or logos.

## Roadmap

True italics, bracketed serifs, monospace, joined scripts, Cyrillic and Greek, Devanagari and Gujarati, more stylistic sets, autohinting.

## Development

```bash
python tests/test_build.py
```

Draws every preset at three weights and checks the masters are point-compatible, builds a family end to end with QA, turns a simulated angled phone photo of a filled sheet into a font, runs the quick-photo route, and checks the MCP server.

## Privacy

Punchcutter counts anonymous usage (installs, builds, MCP tool calls, Studio opens) so we can tell real use from stars. No fonts, text, images, file names or location are ever sent. Turn it off with `punchcutter telemetry off`, `PUNCHCUTTER_TELEMETRY=0` or `DO_NOT_TRACK=1`. Details: [privacy](https://byrishi.github.io/punchcutter/privacy.html).

## License

Code: MIT. Fonts you make are yours, under whatever license you choose. The example families are released under the SIL Open Font License 1.1.
