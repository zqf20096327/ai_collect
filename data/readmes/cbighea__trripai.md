# trripai

🚧Alpha quality, proceed with caution

A syscall-level security supervisor for AI agent processes (Claude Code, Codex, aider, etc.).

It forks your agent as a supervised child, then intercepts file/network/process syscalls in real time, runs each action
through multiple filter scoring pipeline (<=15 ms p99), and surfaces queued or denied actions in an interactive TUI.

All filters are deterministic, no LLM judge in the mix.

---

## Platform support

Linux provides full enforcement. macOS is currently "observe-only", but it won't work on apps like `claude` because it
has a hardened runtime. Check with `codesign -dvv $(which claude)` - will show flags=0x10000(runtime).


| Platform              | Interception            | Enforcement               | Notes                                                              |
|-----------------------|-------------------------|---------------------------|--------------------------------------------------------------------|
| Linux (kernel >= 5.9) | seccomp-unotify + pidfd | Full block/allow/redirect | Landlock LSM as enforcement floor                                  |
| macOS (any)           | dyld interposition      | Observe-only              | Requires `clang`; enforcement blocked without Apple ES entitlement |

---

## Requirements

**Linux:**

- Kernel >= 5.9 (seccomp-unotify; `uname -r` to check)
- Kernel >= 5.13 recommended (Landlock LSM)
- No special privileges beyond running as the user who owns the session

**macOS:**

- Xcode Command Line Tools (`xcode-select --install`) - needed to compile the interposition dylib at first run
- macOS >=12 (Monterey) recommended

---

## Install

**Linux only, amd64/arm64**:

```sh
curl -fsSL https://raw.githubusercontent.com/trripai/trripai/main/install.sh | sh
```

**From source (Linux and macOS):**

```sh
git clone https://github.com/trripai/trripai
cd trripai
go build -o trripai ./cmd/trripai
```

**With ONNX intent scoring:**

```sh
go build -tags onnx -o trripai ./cmd/trripai
```

Then fetch the pinned model, vocab, and runtime assets:

```sh
trripai model download
trripai model verify
```

The downloader uses the built-in asset manifest, verifies SHA-256 digests, and installs private-permission files for the
current platform/arch. If you override the model or runtime paths manually, see `--intent-model`, `--disable-onnx`, and
`--allow-unverified-intent-assets`.

**Docker**

```
docker build -t trripai-test .
docker run --rm trripai-test
```

---

## Usage

```sh
# Supervise an agent
trripai exec -- claude

# Live event dashboard (while a session is running)
trripai tui

# Interactive quarantine review (approve / deny / skip)
trripai digest

# Attach a custom policy file
trripai exec --policy policy.toml -- claude

# Runtime capability report
trripai doctor

# Audit the effective policy, approvals, whitelist, and filter overrides
trripai config audit --policy policy.toml --strict-ci

# Download and verify pinned ONNX intent-scoring assets
trripai model download
trripai model verify

# Generate Ed25519 key for tamper-evident audit chain (Pro)
trripai chain keygen

# macOS capability roadmap
trripai system-extension status

# User whitelists - add persistent allow rules without editing the policy TOML
trripai whitelist add --name allow-npm-cache --path-prefix ~/.npm
trripai whitelist list
trripai whitelist rm <id>

# Filter overrides - disable individual scoring filters per-project or globally
trripai filters list
trripai filters disable domain-freshness --scope project
trripai filters enable domain-freshness

# Policy dry-run - score a recorded event against the current (or a new) policy
trripai rule test --action event.jsonl
trripai rule test --action event.jsonl --policy candidate.toml

# Replay a historical audit log through a candidate policy and see verdict deltas
trripai replay --events ~/.local/share/trripai/events.jsonl.2025-04-28 --policy candidate.toml

# Explain why a specific audit action was scored the way it was
trripai action explain --id 42
```

### Observation mode

The first 20 sessions auto-allow all actions and log `OBSERVE` lines - no blocking. This gives you a baseline before
enforcement kicks in. The startup banner tells you how many observation sessions remain.

### Policy

Policies are TOML files with optional CEL `when` expressions:

```toml
[[rules]]
name      = "block-ssh-exfil"
action    = "deny"
threshold = 0.7
when      = 'event.path.startsWith("/home") && event.path.contains(".ssh")'
```

### User whitelists

Users can create named allow rules without touching the operator TOML policy. Rules are stored in the audit SQLite DB
and loaded into the policy gate at session start.

```sh
# Allow a specific path prefix for the current project
trripai whitelist add --name allow-npm-cache --path-prefix ~/.npm

# Allow a binary on a specific host (supports CEL for advanced cases)
trripai whitelist add --name allow-curl-internal --exec curl --remote internal.corp

# CEL expression - full power of the policy engine
trripai whitelist add --name ci-docker \
  --when 'action.path == "/root/.docker/config.json" && env.CI == "true"'

# Global scope applies across all projects
trripai whitelist add --name allow-homebrew --path-prefix /opt/homebrew --scope global

trripai whitelist list     # show active rules for this project
trripai whitelist rm <id>  # remove by id
```

Rule changes take effect on the next `trripai exec` session.

### Filter overrides

Individual filters can be disabled per-project or globally. Useful when a filter produces false positives for a
known-safe workflow.

```sh
trripai filters list                                  # show all filters and their status
trripai filters disable domain-freshness --scope project
trripai filters enable  domain-freshness
trripai filters disable session-baseline --scope global
```

Pro users in an org may find certain filters locked by their org admin - those filters cannot be disabled regardless of
scope.

### Config audit and control integrity

`trripai config audit` summarizes the effective policy allow rules, scoped approvals, user whitelist entries, and
disabled filters, then emits stable hashes for CI drift detection. `--strict-ci` fails if high-risk global allows,
critical disabled filters, or policy allow rules are present.

If you set `TRRIPAI_CONTROL_INTEGRITY_KEY_FILE` and `TRRIPAI_CONTROL_INTEGRITY_KEY_ID`, trripai also HMAC-signs
persisted scoped approvals, whitelist rows, and filter overrides. Set `TRRIPAI_REQUIRE_CONTROL_INTEGRITY=true` to make
unsigned or unverifiable rows fail the audit and runtime loads.

### TUI customization

Add a `[ui]` section to your policy TOML to change the dashboard color scheme and show your company name:

```toml
[ui]
company_name = "Your Company"   # shown in the header of Live, Digest, and Session Summary
accent       = "62"          # border and header color (cyan)
success      = "42"          # allow-verdict color (green)
danger       = "196"         # deny-verdict and error color (red)
warning      = "214"         # pending / queued color (orange)
```

All color values are 256-color terminal codes (0–255). Omit any field to keep its default.

`trripai tui` and `trripai digest` auto-discover `trripai-policy.toml` in the current directory. For `exec`, pass the
file via `--policy`:

```sh
trripai exec --policy policy.toml -- claude
```

---

## What's in the box?

**17 filters, 3 phases:**

| Phase         | Filters | Examples                                                                                         |
|---------------|---------|--------------------------------------------------------------------------------------------------|
| 1 - fast path | 1–6     | Allowlist/blocklist, path prefix trie (`~/.ssh`, `~/.aws`), privileged LOLBins, helper env abuse |
| 2 - context   | 7–11    | Network destination reputation, reverse shell detector, provenance taint, secret scanner         |
| 3 - policy    | 12–17   | Per-project baseline, intent coherence (ONNX async), rate limiting, CEL policy gate              |

**Audit:** append-only JSONL (hot path) + SQLite (query side, 100 ms/1000-row batches).

**TUI:** Bubble Tea live dashboard + post-session summary + quarantine digest.

---

## Documentation

- [ARCHITECTURE.md](./ARCHITECTURE.md) - deep technical design

---

## Third-party licenses

All dependencies are Apache-2.0, MIT, or BSD-3-Clause. Run `go-licenses report ./...` for the full list.

---

## License

Apache-2.0 - see [LICENSE](./LICENSE).

&copy; Copyright TrripAI
