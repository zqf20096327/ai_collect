# Claude Code Failures

Documented failure modes from working with Claude Code (Anthropic's AI coding agent). Each file is a post-mortem of a real incident where the agent made a mistake that cost time, destroyed work, or required human intervention to correct.

## Why publish these?

AI coding agents fail in predictable, repeated patterns. Documenting these failures concretely — with what happened, why, and what rule would have prevented it — is more useful than vague warnings about AI limitations. These are field notes, not benchmarks.

## Common patterns

- **Assuming instead of observing** — generating plausible explanations without checking tool output
- **Acting on questions** — treating "why did you do X?" as "change X" instead of answering
- **Hiding bugs instead of fixing them** — rewriting tests, loosening assertions, adding retries to mask real failures
- **Panic reverting** — undoing verified work when an unrelated test fails, instead of investigating
- **Skipping dependencies** — declaring "ready" without reading linked issues, PRs, or referenced code
- **Never committing** — touching dozens of files without a single commit, then losing everything to `git reset`
- **Completion drive** — the urge to produce a "done" signal overriding the need to actually understand the problem

## File format

Each file is named `YYYY-MM-DD-short-description.md` and contains:

- **What happened** — concrete sequence of events
- **The actual answer** — what should have been done
- **Root causes** — why the failure occurred
- **The rule** — what principle, if followed, would have prevented it

## Contributing

If you work with AI coding agents and have documented failures, contributions are welcome. Same format: what happened, why, what prevents it.

## License

These are facts about things that happened. Use them however you want.
