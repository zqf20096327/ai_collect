# jobfit

Match job openings against your CV, rank them with any LLM, and get a ranked report PDF plus a tailored CV PDF per worthwhile opening.
It never recommends the same opening twice.
Use it from any agent harness that can run a shell command, including the ones in the table below.

The harness finds openings, jobfit does the matching, tailoring and PDF rendering with deterministic code.
The LLM is reached through a shell command, never an SDK.
The tailoring step cannot invent employers, dates, education or your name.

## Install

Requires Python 3.11 or newer and [uv](https://docs.astral.sh/uv/).
WeasyPrint needs Pango and GLib system libraries.

```sh
brew install pango                                    # macOS
sudo apt install libpango-1.0-0 libpangocairo-1.0-0   # Debian/Ubuntu
uv tool install git+https://github.com/Sipty/jobfit
```

From source instead:

```sh
git clone https://github.com/Sipty/jobfit && cd jobfit
uv sync
uv run jobfit --help
```

macOS note: Homebrew's Pango and GLib live outside the default dyld search path.
The CLI detects this and re-execs itself once with the right `DYLD_FALLBACK_LIBRARY_PATH`.
If you import `jobfit.render` as a library, set it yourself before starting the interpreter:

```sh
export DYLD_FALLBACK_LIBRARY_PATH="$(brew --prefix)/lib"
```

## Quick start

This run needs no API key.
It uses the fictional example CV, four example openings and a fake LLM that scores by keyword in the opening title.

```sh
git clone https://github.com/Sipty/jobfit && cd jobfit
uv sync
uv run jobfit run \
  --cv examples/cv.example.json \
  --jobs examples/openings.example.json \
  --llm 'python3 scripts/fake_llm.py' \
  --out-dir /tmp/jobfit-demo
# Open /tmp/jobfit-demo/report.pdf in any PDF viewer.
```

Run it a second time and the two openings that were tailored in the first run are skipped: the report covers only the remaining two, and no new CVs are written.
Delete `.jobfit/` to start over.

Check the render on its own before a real run:

```sh
uv run jobfit render --cv examples/cv.example.json --out cv-check.pdf
```

For a real run, put your CV in `cv.json` in the working directory and write an openings file:

```json
{"openings": [{"id": "1", "title": "Data Engineer", "company": "Fabrikam Retail",
  "url": "https://example.org/jobs/1", "location": "Lisbon", "description": "..."}]}
```

Then pick the LLM command for your harness from the table below:

```sh
jobfit run --jobs openings.json --llm 'claude -p --model haiku' --top 3
```

Set `JOBFIT_LLM` once and leave out `--llm`:

```sh
export JOBFIT_LLM='claude -p --model haiku'
jobfit run --jobs openings.json
```

You can also let jobfit collect openings from public Greenhouse and Lever boards.
List one board per line in `companies.txt` (`greenhouse:<board>` or `lever:<board>`):

```sh
jobfit fetch --companies companies.txt --out openings.json
```

## Harnesses

`--llm` must read the prompt on stdin, or receive it as an argument via `"$(cat)"`, and print the answer to stdout.

| Harness | `--llm` command | Skill install path |
|---|---|---|
| Claude Code | `claude -p --model haiku` | `~/.claude/skills/jobfit/` |
| Codex CLI | `codex exec -` | `~/.agents/skills/jobfit/` |
| omp | `omp -p` | `~/.omp/agent/skills/jobfit/` |
| Hermes | `hermes -z "$(cat)"` | `~/.hermes/skills/jobfit/` |
| Gemini CLI | `gemini -p "$(cat)"` | none |
| Ollama | `ollama run llama3` | none |
| llm (Simon Willison) | `llm` | none |

To install the agent skill, copy the folder into the harness skill directory.
For example, for Claude Code: `cp -R skills/jobfit ~/.claude/skills/`.
The skill walks the agent through converting your CV, finding openings and running jobfit.

## CV format

The CV is one JSON object.
See [`examples/cv.example.json`](examples/cv.example.json) for a complete, realistic example that uses every section.

Required keys:

- `contact.name`
- `experience`: a list of `{"org", "roles": [{"title", "dates", "bullets"}]}` entries

Every other key is optional.
The renderer skips empty or missing sections, so a CV with only `contact` and `experience` renders.
Optional keys: `contact.tagline`, `contact.location`, `contact.phone`, `contact.email`, `contact.links`, `contact.mobility_note`, `profile`, `opportunities`, `skill_groups`, `education`, `additional_skills`, `leadership`, `funding`, `publications`, `languages`, `mobility`.

`jobfit run` and `jobfit render` read `cv.json` in the working directory unless you pass `--cv`.
Problems found by the validator are printed as warnings; `render` stops on them.

## Outputs

Outputs land in `.jobfit/out/` unless you pass `--out-dir`:

- `report.pdf`: every opening ranked with scores and rationales, the "apply to these" document
- `base_cv.pdf`: your unmodified CV, for comparison
- `<company>-<role>/cv.pdf`: a tailored CV for each opening scoring at least `--min-score` (default 40), up to `--top` (default 5); when one company posts the same title twice, the second folder ends in `-2`

## Seen-opening memory

Recommended openings are stored in `.jobfit/memory.json` and skipped on later runs.
Matching ignores word order, punctuation, gender markers such as "(m/f/d)" and small typos, so a reworded re-posting is still caught.
A title with a different word is a different job: "Backend Engineer" and "Senior Data Engineer" on the same team are both recommended.
`--keep-seen` turns skipping off; `--min-score 0` tailors everything in the top N.

## LLM contract

jobfit asks the LLM for JSON and salvages it tolerantly: code fences, prose around the JSON and malformed entries are handled.
A failed scoring call gives every opening a score of 0 instead of aborting the report.
For smoke-testing without an API, use `scripts/fake_llm.py`.

## Tailoring guarantees

The tailored CV may reword, reorder and drop material.
Where your CV already shows a skill the opening asks for, it uses the opening's own wording for it, so keyword filters find it; it never adds a skill your CV does not show.
`validation_guards` mechanically rejects any tailored CV that changes:

- employers, or adds one
- role dates
- education entries
- the contact name

A rejected CV is reported and that opening is skipped.
Do not override the guard: a tailored CV with an invented credential is worse than no tailored CV.

## Privacy

Your CV is sent to the LLM command you configure, on every run.
If that command is a hosted model, the CV leaves your machine under that provider's terms.
`cv.json`, `cv-check.pdf` and `.jobfit/` are git-ignored, so they stay out of commits.

## Development

```sh
uv sync
uv run pytest    # 90 tests; they also exercise the real WeasyPrint render path
uvx ruff check
```

Layout: `src/jobfit/` holds the code (`jobs` schema, `fetch` board harvesters, `memory` dedup store, `llm` shell bridge, `match` scorer, `tailor` tailorer and guards, `cv` validator, `render` PDF engines).
`examples/` holds the fictional CV and openings, `scripts/fake_llm.py` is the offline LLM stand-in, and `skills/jobfit/` is the harness-agnostic agent skill.

## License

MIT. See [LICENSE](LICENSE).
