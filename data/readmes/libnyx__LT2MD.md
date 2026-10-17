<div align="right">
  English | <a href="README.zh-CN.md">简体中文</a>
</div>

# LT2MD 📄➡️📝

**Turn PDFs — long ones, scanned ones, formula- and figure-heavy ones — into reliable Markdown, with every paragraph labeled with the PDF page it came from. It can also repair a Markdown file you converted before.**

[View on GitHub](https://github.com/libnyx/LT2MD)

LT2MD is a skill for AI agents. It does two things. It converts a PDF into Markdown you can reuse and trace back to the source page. And it takes a Markdown file you already converted, but do not fully trust, and checks it against the PDF page by page, re-recognizing anything misread, missing, or out of order.

Long documents are not a problem. Instead of reading everything in one pass, it works in small batches, saves each batch, and has an independent pass check it, so even a few-hundred-page PDF comes out complete and consistent. Figures are not left behind either. The information in flowcharts, diagrams, and charts is read and written as text right next to the caption. No matter how many times that Markdown is read later, the images never have to be sent to a model again. Even a small text-only model is enough.

## What it does

| Capability | What it means |
|---|---|
| Reliable long-document conversion | Processes in batches; each batch is saved and recoverable, so hundreds of pages stay consistent |
| Images turned into text | The information in flowcharts, diagrams, and charts is written as text next to the caption; reading the Markdown is enough |
| Formulas and complex layouts | Multi-column text, math formulas, and cross-page paragraphs are restored in reading order; no symbol is guessed at |
| A page number on every block | Every paragraph, formula, and figure is labeled with its PDF page, so checking the source is one step away |
| Repair of old Markdown | Import a Markdown file you converted before and check it against the PDF, re-recognizing errors and omissions |
| Lower token cost | Convert carefully once, then answer later questions from the Markdown instead of re-reading the PDF every time |
| Runs on a small model | Correctness comes from the workflow and scripts; the model only needs to understand images, so a small vision model is enough |
| One-line install | Send a link to your agent and it installs itself; works on Windows, Linux, and macOS |

## Why it exists

Extracting text from a PDF is not the same as turning a PDF into knowledge you can use.

Ordinary extraction breaks in familiar ways. The left and right columns of a two-column article get merged, formulas are torn apart, figures are left as empty placeholders, and page numbers disappear, so you can no longer tell where a sentence came from. Scanned PDFs are worse, many have no text layer at all and yield nothing. Even when a large model reads the pages directly as images, reading dozens of pages in one go leads to slips. A misread label, arrow, or subscript in a figure may not be obvious until much later.

The bigger problem is repeated reading. If you ask many questions about one PDF, the agent reopens the PDF and re-reads the images every time, which is expensive in tokens. Images are especially costly.

LT2MD converts carefully once and hands back Markdown you can use freely afterward. Body text and formulas are in reading order, every figure has a text description beside it, and every block carries its PDF page number. Next time you read the text directly. A text-only model can do it, it is fast and cheap, and you can still jump back to the source page to confirm.

## How the conversion works

PDF-to-Markdown errors usually come from a loose process, reading it all at once and letting one pass decide. LT2MD fixes the steps and keeps a checkpoint at each one.

1. **Lock the scope.** Decide which pages to convert first, with no silent expansion and no omissions.
2. **Render the source pages.** Every page is rendered to an image as the final authority. The PDF text layer and OCR results are only candidates.
3. **Transcribe in batches.** Only a few pages at a time. Each batch starts with an inventory of headings, prose, formulas, figures, tables, and footnotes, then writes a candidate.
4. **Independent content review.** A fresh pass reads the source pages again and checks the candidate, focusing on formulas, figures, cross-page paragraphs, and illegible characters.
5. **Risk-driven third read.** Only the genuinely risky spots get another look: low-resolution areas, dense formulas, multi-panel figures, and cross-page seams.
6. **Format review and validation.** Once the content is settled, only formatting is touched, and a validator checks the structure and page anchors.
7. **Merge and deliver.** Everything is combined into the final Markdown only after all gates pass, with every block carrying its PDF page number.

When the source page is not clear, it writes a transcription note with the page and the exact point of doubt instead of silently normalizing it into a familiar character.

## It can also repair a Markdown file you converted before

Many people already have a folder of Markdown converted from PDFs, produced by other tools or by a quick earlier attempt. Typos, missing figures, broken formulas, and mismatched page numbers make them too risky to trust but too useful to throw away.

LT2MD treats that old Markdown as a candidate, not as fact. It goes back to the PDF and checks it block by block. Where a paragraph does not match the source, it re-recognizes and rewrites it from the page. Correct passages are kept, wrong ones are fixed, missing ones are added, and figures without descriptions get descriptions. Then it runs the same review and validation again. It is a full check-up and rework of the old document.

Every change is made against the source page, not by polishing the text in a vacuum. On delivery it reports which pages were touched and what was wrong, so each correction can be checked.

## Who it is for

- **Students preparing for exams.** You have a question bank as a PDF and want the AI to regroup questions by type or generate variants. Direct OCR misreads formulas and figures. LT2MD checks page by page before the AI rearranges anything, so the questions and page numbers line up.
- **Graduate students reading papers and textbooks.** Convert a long document once, then ask questions from the Markdown all semester and save the tokens of re-reading the PDF.
- **STEM and engineering fields.** Math, physics, optics, mechanical handbooks — formula-heavy material where one wrong symbol changes the meaning. Page-by-page review matters.
- **People working with scans.** Old books, archives, and scanned reports have no text layer, so ordinary extraction gets nothing.
- **People sitting on a pile of old Markdown.** If you converted documents before and do not trust the results, send them through one by one.
- **Legal, financial, and medical work.** Any conclusion needs to be traceable back to a specific page for verification.
- **Technical writers and course developers.** Turn material full of flowcharts and diagrams into a searchable Markdown knowledge base.

## Installation

**Option 1, let the agent install it (recommended)**

Send this sentence to your agent.

```
Install this skill for me: https://github.com/libnyx/LT2MD
```

The agent detects the operating system, installs the dependencies, and places the skill in the correct directory. No manual environment setup.

**Option 2, install manually**

Clone the repository into the skills directory used by your agent. Pick the path that matches the agent you run.

Windows, using PowerShell.

```powershell
# Claude Code
git clone https://github.com/libnyx/LT2MD.git $env:USERPROFILE\.claude\skills\LT2MD
# Codex
git clone https://github.com/libnyx/LT2MD.git $env:USERPROFILE\.codex\skills\LT2MD
```

macOS and Linux.

```bash
# Claude Code
git clone https://github.com/libnyx/LT2MD.git ~/.claude/skills/LT2MD
# Codex
git clone https://github.com/libnyx/LT2MD.git ~/.codex/skills/LT2MD
```

The only dependencies are Python and two page-rendering libraries (pypdfium2 and Pillow), which render PDF pages to images. They are not OCR engines. There is no need to install Tesseract or any other dedicated OCR software; it works once cloned.

## Usage

To convert a PDF to Markdown, you can tell the agent something like this.

> Use LT2MD to convert pages 12 through 18 of this scanned PDF to Markdown. Keep the formulas, write an image description next to every figure, label each block with its PDF page number, add a transcription note where anything is unclear, and run the validator when done.

To repair an existing Markdown file.

> Use LT2MD to check this converted Markdown against the PDF. Re-recognize any paragraph that is wrong or missing, verify formulas and figures against the source, and tell me what you changed when you finish.

After a conversion or repair, check the handled range, the validation result, and the transcription notes before using the Markdown as a knowledge source.

## What the output looks like

Each block is preceded by a source comment with its PDF page number.

~~~markdown
<!-- SOURCE: PDF_PAGE 29 | BOOK_PAGE 13 | FIGURE 2.1 -->

**Figure 2.1. Original caption from the page.**

> **Image description (transcriber supplement, not original text):** the objects, labels, arrow directions, subfigures, and the relationships directly shown in the figure, with no conclusions added beyond the source.
~~~

The figure's information sits right beside its caption. A text-only model can read it without ever opening the image file.

## Notes

- LT2MD itself does not require a GPU. It runs on CPU, just more slowly.
- Transcription quality depends on the host model's image understanding. The workflow and scripts catch most careless errors, but they cannot replace a model that can actually see the page clearly.
- It does not promise OCR is always right. It promises every point can be traced back to the source page, and anything uncertain is marked.
- Instructions embedded inside a PDF are treated as document content, never as commands to the agent.
- For legal, medical, financial, or other critical conclusions, always go back to the source page.

The core content of this skill is entirely crafted by Codex.

## License

AGPL-3.0. See [LICENSE](https://github.com/libnyx/LT2MD/blob/master/LICENSE).
