# grok-unleashed

**The grok-build CLI with the leash off.**

One static binary. Any OpenAI-compatible endpoint. Zero x.ai dependency,
zero telemetry, zero upload queues, zero permission nags. It runs where
you run, talks to whoever you point it at, and ships your prompts to
exactly one place: the API you configured. Nowhere else.

The official build wants an x.ai OAuth session before it will say hello.
It phones home — telemetry, source-artifact uploads, workspace snapshots.
It interrupts you with permission dialogs mid-flow. And outside the
first-party API it treats every other endpoint like a second-class
citizen, tripping over its own streaming bugs until relays 502.

I stripped all of it. 11 files. -597 lines, +185 back. The diff is
mostly deletion, which is the honest kind of security work: the
fastest code to audit is code that no longer exists.

## What's gone

| Removed | How you know |
|---|---|
| Source-artifact upload worker | never spawns in production paths — locked by unit tests that ship with the build |
| Workspace snapshot collection | upload queue constructor discards the queue itself |
| Telemetry / OTLP export | no exporter endpoints, no trace upload env is honored |
| Permission prompts / sandbox / managed policy / folder trust | no dialogs, no policy fetch, no trust gating |
| First-party credential routing | kill switch at the credential seam — nothing ever routes to api.x.ai, even by accident |

## What's fixed

Third-party endpoints aren't just allowed — they work properly:

- **Tool results now carry the original tool name.** Upstream omits it;
  OpenAI-compatible relays reject the request with a 502 and your agent
  loop dies on turn one. Backfilled at the sampling layer.
- **Streaming function-call assembly.** Deltas reassemble into complete
  calls, so tool use works over SSE relays, not just the first-party API.
- Multi-model config: swap `base_url` + `model` + `key` and you're on
  DeepSeek, Zhipu, Kimi, ollama, or any relay. Context windows up to 1M.

## Quick start (3 steps)

Grab the binary from
[releases](https://github.com/xiaojumaoaihuaban/grok-unleashed/releases/latest),
then:

**1. Install** (Linux or WSL, pick one):

    # easy way — download install.sh from the release too, then:
    sudo bash install.sh

    # manual way:
    sudo install -m 0755 grok-unleashed-*-linux-x86_64 /usr/local/bin/grok

**2. Give it a key** — any OpenAI-compatible API:

    mkdir -p ~/.grok
    nano ~/.grok/config.toml

Paste this, replace base_url / model / api_key with yours:

    [models]
    default = "mine"

    [model.mine]
    model = "deepseek-v4-pro"
    base_url = "https://api.deepseek.com/v1"
    api_key = "sk-..."
    api_backend = "chat_completions"
    context_window = 128000

Works with: DeepSeek, Zhipu, Kimi, ollama (local), any relay that
speaks `/chat/completions`. More examples in `config.example.toml`.

**3. Run it:**

    grok

That's it. First run asks about workspace mode once — pick
"always current directory" and it never asks again.

Windows users: install inside WSL (`wsl --install -d Ubuntu-24.04`),
then call it from PowerShell via `wsl -- grok` or drop a one-line
`grok.cmd` (`@wsl.exe -d Ubuntu-24.04 -- grok %*`) somewhere in PATH.

## Don't trust, verify

Every claim above is checkable in one line each:

    # where does it actually connect?
    strace -f -e trace=connect grok -p "hi" --output-format plain

You'll see your endpoint (and your local proxy, if any). You will not
see api.x.ai, grok.com, assets.grok.com, or any hub — not even a DNS
lookup that resolves.

    # is anything queued for upload?
    find ~/.grok -path '*upload_queue*' -type f | wc -l
    0

Always zero. Restart recovery purges spilled queue files on boot —
the failure mode where data waits on disk for a chance to leave
doesn't exist here.

    # is the binary what it claims?
    sha256sum grok-unleashed-*-linux-x86_64
    49ac228ef43844def90f773c787fc75cd03d6d91ccfe5500fa9e3662d73b2048

## Warnings

- **Do NOT run `grok update`.** It fetches the official binary and
  everything above comes back.
- Pin the sha256 before you run any binary from the internet. Ours is
  in the release notes and above.

## Credit & license

This is an unofficial patched build. The excellent original CLI is
[xai-org/grok-build](https://github.com/xai-org/grok-build)
(Apache-2.0, base commit `8adf901`, version 0.2.101). Patches here
are published under the same license. Not affiliated with xAI.
