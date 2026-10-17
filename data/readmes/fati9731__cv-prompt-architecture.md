# cvforge

CV generation with a language model, built so the output can be checked rather
than trusted.

The model fills a JSON contract; the code validates it, hunts for claims the
candidate never made, lints it for applicant tracking systems, fixes the
British English locally, and asks for a repair naming the exact paths that
failed. Layout is a separate deterministic step.

```bash
pip install -e ".[dev]"
python examples/offline_demo.py    # the whole loop, scripted model, no API key
pytest                             # 147 tests, no network
```

---

## The failure this is built around

Ask a model to write a CV against a job advert and it will, unprompted, take
the advert's requirements and state them as the candidate's experience. Not
occasionally — reliably, and most strongly when the candidate's notes are
thin, because the advert is the richest text in the context.

The advert used in the demo contains "reduce our data acquisition costs by
30%" and "lead a team of four engineers". Neither appears anywhere in the
candidate's notes. Here is the first draft, and what the checks do with it:

```
what the first draft got wrong (caught, not shipped)
  [fabrication] summary: states '30%', which does not appear in the source notes
  [fabrication] experience[0].bullets[1]: claims 'Led a team of 4'; no such team
                size or seniority appears in the source notes

repair turn sent to the model (first 3 lines)
  Your previous output violated these rules:
    - summary: states '30%', which does not appear in the source notes
    - experience[0].bullets[1]: claims 'Led a team of 4'; ...

result: clean after 2 model call(s), 1 repair(s) | 6/19 keywords evidenced (32%)
```

The candidate would have carried both of those into an interview. **No prompt
wording prevents this reliably**, so it is not left to prompt wording: every
number, employer, job-title word and team size in the output must be traceable
to the candidate's own notes. The job advert is explicitly *not* a source of
facts — a figure that appears only in the advert is precisely the case the
guard exists to catch.

Run `python examples/offline_demo.py` to see it, no API key required.

---

## Why JSON and not prose

The model returns a JSON document against the contract in `schema.py`, never
HTML or markdown. Three reasons, all of which showed up in practice:

- **Prose cannot be checked.** A JSON bullet can be tested for a fabricated
  figure at a known path; a paragraph of HTML cannot.
- **Layout is not the model's job.** Asked for HTML, a model produces a table
  on roughly every other attempt however firmly the prompt forbids it — and a
  two-column CV extracts as interleaved nonsense in an ATS.
- **Repairs can be specific.** `experience[1].bullets[0] states a figure not
  present in the source` is actionable. "Try again" is not.

## The prompt is data, so it can be tested

`prompts.py` assembles the system prompt from named blocks rather than storing
one string. That buys two things:

The ordering is **asserted**, not just intended. The source-of-truth rule comes
before the job-advert rules, because the advert instructions are what cause the
failure the integrity rule prevents — and there is a test
(`test_the_source_of_truth_rule_precedes_the_job_advert_rules`) so a later edit
cannot quietly reorder them. Another test asserts the prompt forbids exactly
what the ATS lint checks for: *a rule with no check is a wish; a check with no
rule is a trap*.

A repair turn restates **only the rules that were broken**. Resending 3,000
tokens of instructions the model already followed wastes tokens and, worse,
invites it to rewrite the parts that were already correct. So a fabrication
sends back the source-of-truth block; a spelling slip sends back the style
block; neither sends the other.

## The checks

Four independent passes, each producing violations with a path.

**`find_fabrications`** — figures, employers, job titles and team sizes not
present in the notes. Three details earned their place by failing:

- *Job titles are checked word by word, not as a phrase.* A model may tidy
  "freelance data work" into "Freelance Data Developer" — that is rephrasing,
  and rejecting it would make the guard useless. It may not add a word the
  notes never contained, and the word it adds is usually a seniority: Senior,
  Lead, Head of.
- *Small numbers are exempt in general, but never in a team-size context.*
  "Owned 2 services" is not a quantified boast. "Led a team of 4" is, and it
  slipped past an earlier version of this guard for exactly that reason.
- *Numbers are compared as canonical tokens, not substrings.* Substring
  matching was the first attempt and it is wrong in both directions: `4` is a
  substring of `2024`, so an invented team of four passed; `85000` is not a
  substring of `85,000`, so the candidate's own figure was flagged.

**`lint_ats`** — content that applicant tracking systems mangle: markup and
markdown tables inside fields, embedded bullet glyphs, emoji, typographic
quotes, column-like spacing. These are constraints on the *content*; the
renderer already owns layout, but it cannot fix a model that puts a table in a
bullet.

**`check_british`** — American spellings, with a caveat that shows why this
kind of list has to be maintained carefully. `program` is absent on purpose: a
computer program is spelled that way in British English too, and flagging it
would train the model to write "programme" in the wrong place. And `resume` is
matched by phrase rather than by word, because it is two words in one
spelling — the noun a candidate sends and the verb a crawler does after a
failure. Rewriting every occurrence flagged "resumed from checkpoints" as an
Americanism.

**`validate_structure`** — the contract, plus length limits, date formats
(`MMM YYYY` / `YYYY` / `Present`), and roles that end before they start.

## Keyword coverage without stuffing

A CV that misses the advert's vocabulary is filtered out before a human reads
it. A CV that repeats it mechanically reads as spam to the human who does.
Both are measured.

`extract_keywords` pulls the advert's substantive terms, keeping multi-word
phrases whole — matching `machine learning` word-by-word would otherwise
report false coverage from a CV that says "learning" once. Phrases are matched
longest-first, because matching `data pipeline` before `data pipelines` leaves
a stray `s` behind as its own keyword.

`coverage` reports which terms the CV actually evidences **and where**, so a
gap is visible rather than papered over:

```
  web scraping           evidenced in skills[1]
  machine learning       evidenced in summary
  not evidenced: data pipelines, rest apis, unit tests, ...
```

The candidate has never written a unit test, so the CV does not claim one. That
is the correct output, and reporting the gap is more useful than hiding it.

`detect_stuffing` catches the other side, and judges repetition by **density
rather than raw count** — a raw count punishes a long CV for saying "data"
four times across two pages. Measured against a faithful CV and a deliberately
stuffed one: natural prose sits at or below 3 mentions per 100 words of prose,
a stuffed passage runs at 24. The threshold is 5, clear of both. Skills lists
are excluded entirely; naming a tool there is the point of the section.

It also flags the *other* stuffing failure — a bullet that is a bare tool
list, `Python, Django, PostgreSQL, Docker, AWS, Kafka`, with no verb and no
outcome. That is what a model produces when a prompt pushes too hard on
keyword coverage, and it is why the prompt's keyword instruction carries a
caveat rather than a demand.

## Honest failure

The repair loop is bounded (`max_repairs`, default 2) and the result is
reported either way:

```python
result = generate(source, model)

if not result.ok:
    for violation in result.fabrications:
        print("check before sending:", violation)
```

A caller gets either a CV that passed every check, or the CV **plus** the list
of what is still wrong — never a silent pass. For a document a person signs
their name to, "here is your CV, and these two bullets could not be verified
against your notes" is a usable answer. A confident CV with an invented figure
in it is not.

British-English fixes are applied locally rather than by asking the model:
spelling has one right answer, and a model call risks it rewriting a sentence
that was already correct.

## Rendering

`render.py` turns the validated JSON into single-column HTML: no tables, no
floats, no absolute positioning, real `<h2>` headings with the section names
parsers look for, URLs shown as text so a parser that drops the `href` still
recovers the address, and **everything escaped** — model output is untrusted
input like any other, and there is a test asserting a `<script>` in a bullet
comes out inert.

PDF generation is deliberately left out: it means bundling a browser or a
native library, and that choice belongs to whoever deploys this. The HTML is
print-styled, so `weasyprint`, headless Chromium or `wkhtmltopdf` all produce
the same result. `to_pdf_instructions()` names them, and names the trap — check
the text is selectable in the output, because a PDF whose text is an image
scores zero with every parser, and that is the one failure a candidate will
never be told about.

## Usage

```python
from cvforge.generate import generate
from cvforge.llm import OpenAIChatModel
from cvforge.render import render_html
from cvforge.schema import CandidateInput

source = CandidateInput(
    notes=open("notes.txt").read(),          # the only source of facts
    job_ad=open("advert.txt").read(),        # emphasis and vocabulary only
    contact={"full_name": "...", "email": "..."},
)

result = generate(source, OpenAIChatModel(model="gpt-4o"))
print(result.summary())

if result.ok:
    open("cv.html", "w").write(render_html(result.cv))
else:
    for violation in result.violations:
        print(violation)
```

The API key is read from `OPENAI_API_KEY` and is never accepted as an
argument, so there is no path by which one gets written into a call site and
committed.

To audit a CV that came from somewhere else — a hand-written one, or another
tool's output — skip generation entirely:

```python
from cvforge.generate import check_only

audit = check_only(existing_cv, source)
print(audit.summary())
```

## Layout

```
src/cvforge/
  schema.py     the JSON contract, in plain Python so its errors are prompt text
  prompts.py    system prompt as named blocks; the violation-specific repair turn
  checks.py     structure, fabrication guard, ATS lint, British English
  keywords.py   advert keyword extraction, coverage, density-based stuffing
  generate.py   the bounded repair loop and its honest result
  render.py     validated JSON to single-column, escaped, ATS-safe HTML
  llm.py        a one-method model protocol, an OpenAI client, and a scripted double
tests/          147 tests, no network
examples/
  offline_demo.py   the whole loop against a scripted model
```

## Tests

```bash
pytest    # 147 passed
```

The model is a one-method protocol, so the suite drives a queue of scripted
responses. That is the only way to assert what happens when a model returns
something *wrong*, which is the case the loop exists for:

- a first draft that borrows a figure and a team size from the advert is
  caught, repaired, and the repair prompt names the exact paths
- a model that keeps fabricating stops after `max_repairs` and reports the
  fabrications rather than passing silently
- a fenced or preamble-wrapped response is recovered without spending a retry;
  a truncated one is retried
- the repair turn restates the broken rule and **not** the others
- the source-of-truth rule is present, and first, in every prompt variant
- a `<script>` in a bullet renders inert
- fabrication edge cases: a rephrased job title passes, an added seniority
  does not; `4` in a team claim is not satisfied by the `4` inside `2024`;
  `85000` is not a fabrication when the notes say `85,000`

## Limitations

- **The fabrication guard is lexical.** It catches invented figures, names,
  titles and team sizes. It cannot catch a fabricated *relationship* between
  true facts — "built the crawler that saved the company £40,000" where both
  the crawler and the figure appear in the notes but the causal claim does
  not. That needs a human, and the honest reporting is what gets one.
- **Unit-blind on figures.** `30` in the notes will satisfy `30%` in the
  output. Tightening this produced more false positives than it prevented
  fabrications, so the figure is reported to the candidate instead.
- **British English only**, and only for the pairs in the table. It abstains
  rather than guessing outside them.
- **One model call per draft.** No streaming, no batching, no caching. For a
  service handling many candidates, the caching layer belongs above this.
- **The keyword scoring is deliberately simple.** A learned ranker would be
  harder to justify to the candidate, who has to stand behind every line.

## Licence

MIT — see [LICENSE](LICENSE).
