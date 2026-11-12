<div align="center">

# 🦞 AutoLoop

**AutoLoop is a zero-glue, issue-driven auto-fix pipeline for GitHub repos: cron polls labeled issues, Claude Code (headless `claude -p`) attempts the fix, the next cycle re-verifies, and the issue is closed — or escalated to a human after N failures. Built for solo devs and small teams who run their own Linux servers.**

中文：基于 GitHub Issue 的 Claude Code 自动修复/自动运维管线，cron 轮询 + 延迟验证 + 失败升级人工，纯 Shell，无需数据库或队列。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![OpenClaw Skill](https://img.shields.io/badge/OpenClaw-Skill-blue.svg)](https://github.com/openclaw/openclaw)
[![GitHub stars](https://img.shields.io/github/stars/ythx-101/autoloop-old?style=social)](https://github.com/ythx-101/autoloop-old)

*Issue → Cron → Claude Code fix → Delayed verify → Auto-close · Works on any GitHub repo*

[Quick Start](#-quick-start) · [Core Mechanism](#-core-mechanism-zero-glue) · [Issue Format](#-issue-format) · [Security](#-security-notes) · [FAQ](#-faq) · [Logs & Debug](#-logs--debug)

</div>

---

## 😤 Problem

```
Ops alert fires at 3 AM.
You: create a GitHub issue, assign someone, wait for morning standup…
3 hours later the fix is a one-liner.
```

Most incidents don't need a human in the loop — they need a **loop**. AutoLoop watches your GitHub issues, dispatches Claude Code to fix them, verifies the result, and closes the issue. If it fails 3 times, *then* it pings a human.

## 🚀 Quick Start

```bash
git clone https://github.com/ythx-101/autoloop-old.git autoloop
cd autoloop
sudo bash install.sh --repo OWNER/REPO
```

Prerequisites:

- Linux with root access (the installer uses `useradd` and `crontab`).
- `gh auth login` and a `claude` login already done as root (the user that runs the installer and the cron jobs; its credentials are copied to `ccworker`).

The installer creates a `ccworker` user (unless `--skip-user`), 8 GitHub labels in the target repo, and 2 cron entries (unless `--skip-cron`).

### Custom parameters

```bash
sudo bash install.sh \
    --repo myorg/myapp \
    --user agent \
    --cron-interval 15 \
    --max-retries 5 \
    --work-dir /opt/workspace
```

### Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `--repo` | (required) | Target GitHub repo `OWNER/REPO` |
| `--user` | `ccworker` | CC execution user |
| `--work-dir` | `/root/clawd` | Working directory |
| `--log-dir` | `/var/log/autoloop` | Log directory |
| `--cron-interval` | `30` | Cron poll interval in minutes (1–59, used as `*/N`) |
| `--max-retries` | `3` | Max auto-fix retries per issue |
| `--tg-script` | (none) | Telegram notification script; called as `bash <script> "<message>"` |
| `--skip-user` | — | Skip user creation |
| `--skip-cron` | — | Skip cron setup |

## ⚙️ Core Mechanism (Zero Glue)

AutoLoop is a **zero-glue** pipeline — no orchestrator, no queue, no database. GitHub Issues *are* the state machine. Labels *are* the transitions. Cron *is* the scheduler.

```
GitHub Issue (type:service label)
    ↓  cron */30
gh-issue-router.sh — logs label classification
    ↓
auto-fix.sh — Claude Code executes fix
    ↓  outputs FIXED:
mark pending-verify
    ↓  next cron cycle
delayed verification (verify block or CC verify)
    ↓  pass → auto-close issue
    ↓  fail ≥3 times
mark needs-decision + TG notify human
```

### Why "Zero Glue"?

| Traditional | AutoLoop |
|-------------|----------|
| Jira + webhook + Lambda + SQS + worker | GitHub Issue + cron + shell script |
| Redis/DB for state | GitHub Labels for state |
| Custom retry logic | Cron = built-in retry |
| Dashboard for monitoring | `gh issue list` = dashboard |

### Key Features

| Feature | How it works |
|---------|-------------|
| **Issue-driven** | Label an issue `type:service` → pipeline picks it up automatically |
| **Memory retry** | Each retry carries the last failure comment — CC can avoid repeating it. Verify failures also count toward retries |
| **Delayed verification** | Fixes aren't trusted immediately; next cron cycle re-verifies |
| **Human escalation** | After N failures, labels `needs-decision` and optionally pings Telegram |
| **Inline verify blocks** | Embed test commands in issue body — the next cycle runs them to validate |
| **Label classification** | Only `type:service` issues are auto-fixed; `gh-issue-router.sh` currently logs the label classification for other types (`type:bug`, `type:reading`, `type:enhancement`) |

## 📝 Issue Format

Title is for humans. Body is for Claude Code:

```markdown
Title: Redis connection pool exhausted causing API 500

Body:
Check /srv/myapp/services/api Redis connection config.
Current max_connections=10 is insufficient, increase to 50.

Modify REDIS_MAX_CONNECTIONS in config.py.
Restart service and verify API returns 200.
```

### Optional: Inline verify block

Add a ` ```verify ` code block for automatic validation:

````markdown
```verify
curl -s http://localhost:8080/health | grep -q '"status":"ok"'
```
````

### Labels

| Label | Meaning |
|-------|---------|
| `type:service` | Service/ops — auto-fixed |
| `type:bug` | Bug — logged by router (not auto-fixed) |
| `type:enhancement` | Feature — logged by router, human handles |
| `type:reading` | Research — logged by router |
| `pending-verify` | Awaiting next-cycle verification |
| `needs-decision` | Retries exhausted, needs human (skipped) |
| `auto-fixed` | Already fixed (skipped) |
| `stale` | Expired (skipped) |

## ⚠️ Security notes

- Claude Code runs with `--permission-mode bypassPermissions` and holds copies of your `gh` and Claude credentials (the installer copies them to the `ccworker` user).
- The ```` ```verify ```` block is executed with `bash -c` by the cron user (usually root).
- Use it on **private repos**, or on repos where only trusted collaborators can label and edit issues.
- Only people who can apply the `type:service` label can trigger a fix.

## 🧭 When to use / Alternatives

| Approach | Good fit | Poor fit |
|----------|----------|----------|
| **AutoLoop** | Self-hosted single machine, one-line ops fixes, low-frequency events | Multi-host clusters, high-frequency alerts, teams needing audit trails and approval flows |
| GitHub Actions + Claude Code Action | Code changes reviewed through PRs on GitHub-hosted runners | Fixes that must act on your own server's local state |
| Self-built webhook + queue worker | High volume, custom routing, strict control | Solo devs who don't want to run extra infrastructure |
| Human on-call | Judgment-heavy or risky incidents | Repetitive fixes that wake someone up |

## ❓ FAQ

**How do I auto-fix GitHub issues with Claude Code? / 怎么让 Claude Code 自动修 GitHub issue？**
Run `install.sh --repo OWNER/REPO`, then open an issue with the `type:service` label. Each cron cycle `auto-fix.sh` hands the issue body to Claude Code via `claude -p`.

**Does it need a server, database or webhook?**
It needs a Linux host with cron. No database and no webhook; state lives in GitHub labels and comments.

**How does verification work?**
If the issue body has a ```` ```verify ```` block, the next cycle runs it. Otherwise Claude Code is asked to check read-only and answer `VERIFIED` or `NOT_FIXED`.

**What happens when a fix keeps failing?**
Failures are counted from issue comments that carry the pipeline's failure markers (`auto-fix 无法修复` / `延迟验证未通过`) and were posted by the repo owner, members or collaborators. Both failed fix attempts and failed verifications count. At `--max-retries` the issue gets the `needs-decision` label, and a Telegram message is sent if `--tg-script` is set.

**Which issues are processed?**
Open issues with the `type:service` label, none of `needs-decision`/`stale`/`auto-fixed`/`pending-verify`, and not pull requests. Each cycle looks at the first 20 open issues returned by the API.

**Why does it run Claude Code as a separate `ccworker` user?**
For isolation: `cc.sh` runs Claude Code via `su` as that user rather than as the cron user.

**Is it safe for public repos?**
Not by default — see [Security notes](#-security-notes).

## 📦 Dependencies

| Dependency | Install |
|------------|---------|
| `gh` (GitHub CLI) | https://cli.github.com/ |
| `claude` (Claude Code) | `npm install -g @anthropic-ai/claude-code` |
| `python3` | System default or `apt install python3` |
| `setfacl` (optional) | `apt install acl` |

## 🔧 Scripts

| Script | Purpose |
|--------|---------|
| `install.sh` | Install & config |
| `scripts/cc.sh` | CC invocation wrapper |
| `scripts/auto-fix.sh` | Main loop: scan issues → CC fix → verify → close |
| `scripts/gh-issue-router.sh` | Log issue classification by label |

## 📊 Logs & Debug

```bash
# Live logs
tail -f /var/log/autoloop/auto-fix.log

# Cron logs
tail -f /var/log/autoloop/cron.log

# Manual trigger (<install-dir> = your clone)
. <install-dir>/.env && bash <install-dir>/scripts/auto-fix.sh

# Check cron
crontab -l | grep autoloop
```

## 🗑️ Uninstall

```bash
# Remove cron entries
crontab -l | grep -v '# autoloop:' | crontab -

# Delete logs
rm -rf /var/log/autoloop

# Delete the clone
rm -rf <install-dir>

# Optional: remove the worker user (also deletes the credentials copied to it)
userdel -r ccworker
```

## 🤝 Contributing

Issues and PRs welcome! AutoLoop is part of the [OpenClaw](https://github.com/openclaw/openclaw) ecosystem.

## 📄 License

[MIT](LICENSE)

---

<div align="center">

*Issue-driven. Zero glue. Fully automatic.* 🦞

**[GitHub](https://github.com/ythx-101/autoloop-old)** · **[Issues](https://github.com/ythx-101/autoloop-old/issues)** · **[OpenClaw](https://github.com/openclaw/openclaw)**

</div>
