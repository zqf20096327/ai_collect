<p align="center"><img src="assets/init-rebuild.svg" alt="INIT: it rewrites its own harness and grows with every model. Everything is writable except the Root." width="100%"></p>

INIT is a coding agent that rewrites its own harness while it works. The harness is everything around the model: prompts, tools, the loop, how context is kept. People write it by hand for the models they have, and Sutton's bitter lesson says hand-built structure loses to learning and scale. Once a model outgrows its designers, each scaffold is a ceiling. So INIT lets the model change its own harness, compiled Rust core included, mid-task. One part stays fixed: the Root, a separate process the agent cannot modify, which checks each change, records it in a signed log and can undo it.

```sh
curl -fsSL https://github.com/nagisanzenin/INIT-Agent/releases/latest/download/get.sh | sh
```

Then open a new terminal and run `init-agent`. The first run asks you to pick a provider, paste your key and pick a model.

macOS 14+ on Apple silicon; Linux x86_64 is experimental; Linux aarch64 has no 0.6 bundle. To upgrade, to uninstall (one line; everything goes to the Trash) or to set up Linux: [Install, upgrade, uninstall](docs/guide.md#install-upgrade-uninstall).

## How it works

```text
  you:  init-agent · /stop · /panic · /undo · /rollback
   │
   ▼
╔═ ROOT · init-root, a separate process the agent cannot write ════════════╗
║                                                                          ║
║  holds   your API keys · your charter · its signing key                  ║
║          the signed lineage · the spend ledger · snapshots               ║
║  does    starts every agent process in a sandbox it composes             ║
║          adds your key to each model call and meters it                  ║
║          harm signals · stop and panic · memory and disk watchdog        ║
║          rolls the whole system back to a known-good version             ║
║                                                                          ║
╚═════════════╤═══════════════════════════════════════════▲════════════════╝
              │ starts, sandboxes,                        │ every model call
              │ rolls back                                │ (no key on this side)
              ▼                                           │
┌─ AGENT ZONE · sandboxed, holds no API key ──────────────┴────────────────┐
│                                                                          │
│  kernel  gates each change and hot-swaps the body      editable from L1  │
│  body    T0  prompts and skills                        editable now (L0) │
│          T1  tools, as Wasm components                                   │
│          T2  the compiled Rust core and its loop                         │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

A change to the compiled core takes five steps. Prompts, skills and Wasm tools skip the process swap and reload in place once they pass the gate. With Rust installed, INIT builds its dependencies once in the background after it starts; a self-change asked for while that build runs waits for it (an estimate: 15–33 min on a Mac, 21–46 min on Linux), and the panel says so.

1. **Edit a copy.** The agent edits its source on a branch beside the running body.
2. **Gates.** G0 builds it and runs the tests and clippy. G1 regenerates the self-map byte for byte. G2 boots the new binary beside the live one. G3 has the new version complete a self-edit, so a change cannot break the ability to change. If a gate fails, nothing happened: the live body never stopped.
3. **Hot-swap.** At a turn boundary the new process takes over the same conversation log ([ADR-001](docs/adr/001-overlapped-handoff.md)).
4. **Watch.** In the default `gated` mode, a sealed test (G4) on tasks the agent never sees decides whether the change stays; a fresh install has no such tasks, so G0–G3 decide. In `free` mode the Root watches each change for 2 to 72 hours with twelve harm signals, such as crashes and spikes in cost or errors ([ADR-011](docs/adr/011-reward-free-self-extension.md)).
5. **Roll back.** A failed G4, a crash, a harm signal, `/rollback` or `/panic` returns the system to a known-good version, with a signed record.

No step asks a change to prove it is better, because nobody can write the score for a capability nobody foresaw. The Root checks what it can check for any change: can it be undone, and did it cause harm?

**The Root is the fixed part.** `init-root` is its own service (a LaunchAgent on macOS, a systemd user unit on Linux) with its own directory, `~/.init-root`. In every access mode its sandbox (Seatbelt on macOS, bubblewrap on Linux) denies the agent the Root's files, its service file, INIT's launchers and signals to the Root; the folders above them cannot be renamed, removed, swapped or cloned. The Root is 33,152 lines of Rust without tests at the v0.6.0 tag, `init-root` 29,580 of them ([REL-060](build/status/REL-060.md)). [root.md §4.8](docs/root/root.md) gives the command and counts its trusted computing base separately.

**Why a compiled core and not plugins?** A plugin API fixes in advance where the model may extend the agent. What a stronger model is likely to want to change sits elsewhere: how context is compacted, how the loop retries, how requests are laid out so the prompt cache keeps hitting. That code is the core, so the core is editable (T1 Wasm tools are the plugin path). The cost is time. A no-op core change on a fresh install, built cold, took 729 s to 2,146 s (12 to 36 min) in the release checks from v0.5.0 to v0.6.0, depending mostly on what else the machine was doing (M2, mock model). With a warm dependency cache, a small change's build and G0 took 126 s. The guide has every measurement with its load and receipt ([Time](docs/guide.md#install-upgrade-uninstall)).

## What it has done

- **It wrote itself a sub-agent tool** (v0.2.0-preview, a small model, 2026-10-24). Asked for sub-agents, INIT wrote a `delegate` tool on its own branch: a nested loop with a fresh context and the same prompt head, so the cache still hits. It never promoted itself (stale tests, then a build limit we later raised); v0.3's built-in `delegate` is built on it ([REL-G0](build/status/REL-G0.md)).
- **It swapped its compiled core mid-conversation and kept the cache** (v0.1, deepseek-flash, 2026-10-20). A comment-only core change from the test harness passed G0–G3 and was handed to the running session. The first request after the swap read 87.9% of its prompt tokens from DeepSeek's cache ([real-v0.1.md](measurements/real-v0.1.md), E2E-3).
- **A sealed test refused its own change, and the rollback is signed** (pre-v0.2 code, deepseek-flash, gated mode, 2026-10-21). The agent wrote a change to its `bash` tool, which passed G0–G3 and went live. G4 scored it 5 points worse (29 tasks × 3 runs, inside the noise), and the gate rolled it back ([m7-results.md](measurements/m7-results.md)).
- **A guardrail rolled back a bad change in 3.8 s** (v0.4.0-preview, deepseek-flash, free mode). A deliberately bad change raised cost per turn by 137%; the Root rolled it back and kept the good change before it ([v0.4.0 notes](docs/release-notes/v0.4.0-preview.md)).

**Not shown yet:** that self-changes make a model better. The one change the sealed test measured was not kept, and a test built to find tasks INIT fails for lack of a mechanism found none on deepseek-flash ([evo-test protocol §11.8](measurements/evo-test-protocol.md)). If you run frontier models, we would like your results.

## Safety model

- **Full access by default.** The agent reads and writes anything you can and uses the network, including files your own tools run later (shell startup files, `PATH` directories, git hooks), so trust it as you trust your shell. The Root protects INIT, not your files; `/undo` restores only the folder you started in ([ADR-012](docs/adr/012-full-access-by-default.md)).
- **Workspace mode** (`init-agent --workspace` or `/full off`). The agent reads your home except secrets (`~/.ssh`, cloud credentials, keychains, browser and mail data), writes only the start folder and `~/.init`, and reaches only the model provider. On Linux it stays in its own home.
- **Spend is metered, not capped.** No dollar amount stops INIT. Set a limit at your provider ([Spending](docs/guide.md#spending)).
- **Keys never reach the agent.** The key you paste goes to the Root, which adds it to each request on the way out.

## Status and limits

INIT 0.6 is a research preview.

**New in 0.6:** a signed model catalog with prices that the Root meters with, a credential store and more auth kinds, local model servers, a reasoning-effort choice per model, and Sign in with ChatGPT as a preview ([v0.6.0 notes](docs/release-notes/v0.6.0-preview.md)).

- **Tested on v0.6.0:** at $0 on a mock model, install, pause, a core change through the gates and the hot-swap on macOS and on Linux x86_64 (a hosted Ubuntu 24.04 VM), and on macOS upgrades from every public release since 0.3.1 (or the uninstall they need). On the live API, DeepSeek's deepseek-flash on its three wire formats, on the fourth release candidate; one check could not run there, so that run's formal verdict is FAIL. The full lists are in the notes: [Verified for this release](docs/release-notes/v0.6.0-preview.md#verified-for-this-release) and Not verified.
- **Not live-tested on v0.6.0:** OpenAI's gpt-6.1-sol (last qualified live on v0.5.4, [receipt](build/status/qualify/openai-gpt-6.1-sol-v0.5.4.json)); every provider and wire format 0.6 added (the catalog's other providers, Amazon Bedrock, local servers, Sign in with ChatGPT); Anthropic, OpenAI's gpt-6-astra and API gateways. Those have fixtures and mock servers only, and `/model` marks them `not live-tested`. deepseek-v4-pro was not run on this release either; it keeps its mark from deepseek-flash's run on the same wire formats.
- **Not built:** a Linux aarch64 bundle for 0.5.x or 0.6, autonomy above L0 (L0 already covers the whole body; the kernel opens at L1), Windows.
- **Signed:** releases from v0.5.3, with release key 1, `SHA256:IS7wIWkppZkHSUwdnsJR+K4fBPkmPa/IJwfNi9sIoMs` ([how to check](docs/release-signing.md)).

## Docs

[User guide](docs/guide.md) · [technical report](reports/INIT%20technical%20report.md) · [design decisions (ADRs)](docs/adr/) · [release notes](docs/release-notes/) · [changelog](CHANGELOG.md) · [release protocol](docs/release-protocol.md)

Apache-2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
