# AI Stack

Stay in the harness you are already in. When that subscription is spent,
route the job to another CLI — Grok 4.6, Fable 5, or Sol 5.6 in Cursor —
or run **Claude Code, Codex and Cursor at the same time**.

Type `/aistack`. Files are the bus. Whoever builds it does not grade it.

This repository is the open-source skill. MIT. Built by
[NavAIgate](https://navaigate.dev).

## Install

You need at least one of [Claude Code](https://docs.anthropic.com/en/docs/claude-code),
[Codex](https://github.com/openai/codex), or
[Cursor](https://cursor.com) signed in. Two or three is the point.

```bash
git clone https://github.com/skyremote/aistack.git
cd aistack
bash ./install.sh
```

That links `/aistack` (and `/stack-loop`) into Claude, Cursor, Codex and
`~/.agents/skills`, and puts `aistack` on `~/.local/bin`. Open a **new**
session, then type `/aistack`.

```bash
aistack probe    # what is installed and signed in — no model call
aistack models   # Grok / Fable / Sol slugs
```

## What `/aistack` asks

1. **Mode** — one Cursor model, or all three seats at the same time
2. **Cursor model** — Grok 4.6, Fable 5, or Sol 5.6
3. **Speed** — fast, or not fast
4. **How long** — 3, 5 or 10 minutes
5. **Depth** — read-only suggestions, or do the work

Then it needs a job. An empty brief is not a run.

## CLI

```bash
aistack takeover --seat cursor --brief /tmp/brief.md --cwd ~/code/foo \
  --model cursor-grok-4.6-xhigh --timeout 600
aistack fanout --brief /tmp/brief.md --cwd ~/code/foo \
  --pick grok --duration long --seats claude,codex,cursor
```

`fanout` is read-only unless you pass `--write`, and write still needs each
seat to own different paths. `stack-loop` is the same binary: sequential
review, opposite-provider inspect.

## Tests

```bash
python3 -m unittest discover -s tests -v
```

No model quota. Fake CLIs cover verdicts, fan-out, and “builder cannot inspect”.

## Credit

Cross-provider inspection follows Chase AI’s
[claudex-loop](https://github.com/chaseai-yt/claudex-loop) (MIT). This is a
rewrite for three seats, not a fork.
