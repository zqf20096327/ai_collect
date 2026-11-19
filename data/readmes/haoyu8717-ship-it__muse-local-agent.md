# Muse Local Agent

Let Muse operate your Windows PC, Linux cloud VM, and Android phone as one system — a verified local-agent setup (Windows-MCP + SSH/Tailscale bridge) that another Muse can rebuild from this skill alone.

## What this is

A skill for [Muse](https://muse.ai) (Meta's personal AI agent) that teaches it to operate your machines as one system:

- **Windows 11 PC** — driven as a local agent via [Windows-MCP](https://github.com/CursorTouch/windows-mcp) (UIA accessibility tree) in the login session
- **Linux cloud VM** — the agent's home, connected to the PC over an SSH/Tailscale bridge
- **Android phone** — automated via Tasker + AutoX.js + Shizuku + scrcpy

The core is the **verified end-to-end local-agent stack recipe** (in `SKILL.md`): SSH bridge, Windows-MCP server, logon task + `start-server.cmd`, self-healing SSH tunnel, and VM-side MCP client — every step built, broken, fixed, and verified on 2026-11-17. It includes the real measured latency numbers, the definitive findings (e.g. direct Tailscale from a sandboxed VM is impossible — the SSH tunnel is mandatory), and the iteration mechanism that keeps the stack improving.

## Files

| File | What it is |
|---|---|
| `SKILL.md` | The skill. The recipe is the section "The verified local-agent stack — end-to-end recipe". The rest is distilled rules from the Knowledge OS. |
| `skill.yaml` | Skill metadata. |
| `mcp-tunnel.sh` | Self-healing SSH tunnel loop (VM 18000 → PC 8000). No systemd, no cron. |
| `ensure-tunnel.sh` | On-demand tunnel check — run only before a desktop task. |
| `windows-mcp-tunnel.service` | systemd unit (archived — `/etc` does not survive VM replacement; the shell loop is the real mechanism). |
| `OPTIMIZATION_LOG.md` | The iteration log — where the stack gets stuck, and how it was fixed. |

## The stack in one paragraph

A cloud Linux VM runs the agent. It reaches the Windows PC through an SSH tunnel (via an egress proxy, because the VM's network sandbox blocks direct tailnet connections). On the PC, a Windows-MCP server runs inside the user's login session (a logon Scheduled Task — never a service, Session 0 cannot show UI). The server exposes 18 tools (PowerShell and Registry excluded) over streamable-HTTP on `127.0.0.1:8000`, authenticated by Bearer token. The VM's MCP client connects through the tunnel at `127.0.0.1:18000`. A separate non-admin SSH account (`<SSH_ACCOUNT>`) provides PowerShell access and a fallback when MCP is down. Real latency: ~1.5–2s per lightweight call, ~9s per screenshot. Prefer the UIA tree over screenshots.

## The iteration mechanism

`OPTIMIZATION_LOG.md` is the memory. Every entry: date, component, symptom, impact, root cause, fix/status. The rules: on demand only, never poll (a 5-minute watchdog would be 288 agent runs/day); fix the cause and record it, don't just restart; one loop, one watchdog; verify out of band; prefer a side test over killing the live server. Review happens on the next desktop session, not on a schedule.

## Install

Clone this repo and copy `SKILL.md` and `skill.yaml` into your Muse custom skills directory (`~/workspace/custom-skills/muse-local-agent/`), or read `SKILL.md` directly — the recipe section is self-contained.

## License

MIT. See [LICENSE](LICENSE).
