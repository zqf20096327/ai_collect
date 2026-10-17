# Codex Radar

**Find what slows down your Codex workflow. Leave with one concrete move to try next.**

Codex Radar turns your existing project sessions into a personal collaboration report: where work gets stuck, which habits help, and what to change in your next session. Copy a tailored prompt or workflow, then come back to see whether the measured behavior improved.

[中文](README_zh.md) · [Try the demo](https://lemomo-ai.github.io/codex-radar/demo.html) · [Website](https://lemomo-ai.github.io/codex-radar/) · [Methodology](docs/METHODOLOGY.md)

## From “that took too long” to a better next session

- **Find the bottleneck.** See your strongest pattern and most costly friction across communication, engineering, and observable outcomes. Open the cited message, session, or incident behind a recommendation.
- **Get an action you can use.** Copy a project-specific prompt, follow a short workflow, or adopt a setup-file draft. Suggestions are prioritized by the evidence; smaller samples receive shorter plans.
- **Check whether you improved.** The next comparable report checks structured targets such as edits followed by passing verification. It separates changes in formula scores from changes in model interpretation.
- **Review the period that matters.** Analyze all history, the last 30 days, or a chosen date range. Reports adapt to one-off tasks, feature work, long-running projects, learning, and automation.
- **Keep control of your evidence.** Standard mode removes common credentials. Strict mode also leaves out message and command excerpts, thread titles, search queries, and session opening/closing text.

The report is a bilingual, self-contained HTML file with a nine-dimension radar, a focused action plan, progress checks, and expandable evidence. It opens without a server. [Explore a complete synthetic example →](https://lemomo-ai.github.io/codex-radar/demo.html)

## Get your first report

Requires a Codex CLI with plugin support and **Node.js 20+**. No dependencies to install, no separate API key.

```bash
codex plugin marketplace add lemomo-ai/codex-radar
codex plugin add codex-radar@codex-radar-marketplace
```

Start a new Codex thread and ask:

```text
Run Codex Radar on this project.
```

You can also ask:

```text
Analyze my Codex collaboration over the last 30 days, in strict privacy mode.
```

Radar uses the project you selected, reads its local session history, and generates a report in `~/.codex-radar/reports/`. If there is too little evidence, it asks you to build up more history instead of filling a report with guesses.

**Next time:** try the first action, do some work, then run Radar with the same analysis window. Measurable targets are checked automatically; other actions include instructions for manual verification. A lack of new evidence is shown explicitly.

## What the nine dimensions tell you

| Area | What you can improve | Dimensions |
| --- | --- | --- |
| Communication | Clear requests, useful context, specific corrections | Lock-On · Scene Setting · Steering |
| Engineering | Tool use, reusable project setup, sustainable pacing | Toolcraft · Architecture · Tempo |
| Outcome | Observable output, verification, completed turns | Efficiency · Proof Check · Completion |

Scores are coaching indicators based on recorded behavior, not a measure of code quality or a comparison against other people. Scripts compute the baselines and final scores; your active Codex session writes the diagnosis and bounded, evidence-cited adjustments. Inapplicable dimensions remain unscored. [How scoring works →](docs/METHODOLOGY.md)

## Privacy and API keys

**Codex Radar itself needs no API key.** The credential protection is for secrets you may have pasted into past sessions, including JSON fields and command arguments. It reduces accidental carry-over into evidence and reports; it is not an exhaustive secret scanner.

Bundled scripts make no network calls and send no plugin telemetry. They read history without modifying it and save local artifacts with private permissions where supported. Model interpretation happens in your active Codex session and follows its configured data handling, so the complete workflow is not necessarily offline. Review a report before sharing it. [Privacy details →](PRIVACY.md)

## Develop and customize

```bash
git clone https://github.com/lemomo-ai/codex-radar.git
cd codex-radar
node --test tests/*.test.mjs
node scripts/build-demo.mjs
```

The [rubric](plugins/codex-radar/data/rubric.json) defines dimensions, profiles and suggestion recipes. [scoring.mjs](plugins/codex-radar/skills/analyze/scripts/scoring.mjs) is the executable formula source. Parser and privacy tests use synthetic sessions, never contributors’ history. See [Contributing](CONTRIBUTING.md) for the workflow.

## License

[CC BY-NC 4.0](LICENSE). Non-commercial use, sharing and modification are welcome with attribution and change notices. Commercial licensing: **leifdiao@gmail.com**.
