# 🌉 grok-bridge

grok-bridge turns the Grok web app (grok.com) in your signed-in Safari into a local REST API and CLI on macOS — so your scripts and AI agents can call Grok without an xAI API key, using pure Safari JavaScript injection, Python stdlib only, and no Accessibility permission by default.

在 macOS 上把已登录 Safari 的 Grok（grok.com）变成本地 REST API / CLI，供脚本和 AI agent 调用，无需 API key。

Current release: v3.1.1 · macOS + Safari only · Python 3 stdlib only · MIT

## Who is this for / 适用场景

- **For:** individuals who want to call their own grok.com account (free or SuperGrok) from local scripts or AI agents such as Claude Code or Codex (any tool that can send HTTP requests) — a Grok local API / Grok 本地 API, 免 API key.
- **Not for:** multi-user services, production SLAs, or non-macOS environments. For those, use the official xAI API.
- This is an unofficial project, not the xAI API. See the [Disclaimer](#disclaimer).

## Requirements

- macOS with Safari
- Logged into [grok.com](https://grok.com) (free or SuperGrok)
- Safari > Settings > Advanced > Show features for web developers ✓
- Safari > Develop > Allow JavaScript from Apple Events ✓
- **No Accessibility permission needed by default** (v3 uses JS injection, not System Events)
- Optional `--foreground-fallback` may activate Safari and use System Events Enter if pure JS submit fails.

## Quick start

1. In Safari, sign in to grok.com and enable the two Safari settings above.
2. Check your setup (sends no prompt):
   ```bash
   python3 scripts/grok_bridge.py --doctor
   ```
3. Start the server and send a request:
   ```bash
   python3 scripts/grok_bridge.py --bind 127.0.0.1 --port 19998
   # in another terminal:
   curl -X POST http://127.0.0.1:19998/chat \
     -H "Content-Type: application/json" \
     -d '{"prompt":"hello","timeout":60}'
   ```

## How it works

```
Your Terminal/Script → Safari JS injection → grok.com → Response extracted via DOM
```

Two modes:

### REST API (recommended)
```bash
# Check local Safari/Grok setup first
python3 scripts/grok_bridge.py --doctor

# Start the server on your Mac
python3 scripts/grok_bridge.py --bind 127.0.0.1 --port 19998

# Default mode uses a dedicated background Safari tab named grok-bridge-agent.
# Use --shared-tab only when you intentionally want to drive the current Safari tab.

# Query from the Mac itself
curl -X POST http://127.0.0.1:19998/chat \
  -H "Content-Type: application/json" \
  -d '{"prompt":"What is the mass of the sun?","timeout":60}'

# Health check
curl http://127.0.0.1:19998/health

# Read current conversation
curl http://127.0.0.1:19998/history
```

Use `--doctor --json` when another tool or agent needs structured setup diagnostics.

### Response format

`POST /chat` accepts a JSON object with a required non-empty string `prompt` and an optional positive-number `timeout` in seconds (default 120). Invalid input returns HTTP 400 with `{"status":"error","error":"..."}`. Successful and failed chats return JSON like this (numbers are example values):

```json
{"status":"ok","response":"The Sun's mass is about 1.99e30 kg.","elapsed":12.3}
{"status":"timeout","response":"<partial reply captured so far>","elapsed":60.1}
{"status":"error","error":"input not found"}
```

`GET /health` returns `status`, `url` (redacted), `on_grok`, `version`, `dedicated_tab`, `tab_name` and `foreground_fallback` (plus `next_steps` when Safari is not on grok.com).

### Python example

Standard library only:

```python
import json, urllib.request

req = urllib.request.Request(
    "http://127.0.0.1:19998/chat",
    data=json.dumps({"prompt": "Say hi in one sentence", "timeout": 60}).encode(),
    headers={"Content-Type": "application/json"},
)
with urllib.request.urlopen(req, timeout=150) as r:  # longer than the chat timeout
    print(json.load(r)["response"])
```

## Deployment boundary

Stable local deployment listens on `127.0.0.1:19998`. This is intentional: the bridge drives the signed-in Safari session on the Mac, so it should not be exposed directly on LAN, Tailscale, or a public interface.

Remote Claw/agent access should use an operator-controlled tunnel or proxy:

```bash
# From the remote agent host:
ssh -N -L 19998:127.0.0.1:19998 user@your-mac

# Then call the tunnel-local endpoint:
curl -X POST http://127.0.0.1:19998/chat \
  -H "Content-Type: application/json" \
  -d '{"prompt":"hello","timeout":60}'
```

If a deployment must listen beyond loopback, start it explicitly with `--bind <trusted-interface-ip>` and put host firewall / network ACLs in front of it. Do not use `0.0.0.0` as the stable default.

### CLI (legacy)
```bash
# Local
bash scripts/grok_chat.sh "Explain quantum tunneling"

# Remote via SSH
MAC_SSH="ssh user@your-mac" bash scripts/grok_chat.sh "Write a haiku" --timeout 90
```

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | `/chat` | Send prompt, wait for response |
| POST | `/new` | Start new conversation |
| GET | `/health` | Health check (Safari URL, grok status) |
| GET | `/history` | Read current page conversation |

## Comparison / 与同类方案对比

| | grok-bridge | Official xAI API | Generic browser automation (Playwright, Selenium, etc.) |
|---|---|---|---|
| API key | Not needed | Required | Not needed |
| Billing | Uses your existing grok.com account | Usage-based | Depends on the site you automate |
| Platform | macOS + Safari only | Any | Varies by tool |
| Stability | Affected by grok.com UI changes | Stable official interface | Affected by UI changes |
| Concurrency | One session; requests run serially | Server-side concurrency | Depends on your setup |
| Login state | Reuses your signed-in Safari session | API key | You manage login yourself |

## FAQ

**Is this the official Grok / xAI API?** No. It is an unofficial local bridge to the grok.com web app. 不是官方 API。

**Do I need an API key or SuperGrok?** No API key. You need to be signed in to grok.com in Safari (free or SuperGrok). 不需要 API key，只需在 Safari 登录 grok.com。

**Does it work on Windows / Linux / Chrome?** No — macOS + Safari only (it uses AppleScript). A remote machine can call the server on your Mac through an SSH tunnel.

**Does it need macOS Accessibility permission?** Not by default. Only the optional `--foreground-fallback` uses System Events.

**Will it take over my current Safari tab?** By default it uses a dedicated tab marked `window.name="grok-bridge-agent"`. Only `--shared-tab` drives your current tab.

**Can I expose it on my LAN / Tailscale?** Not recommended. It binds to `127.0.0.1` by default; use an SSH tunnel. If you really must, use `--bind <trusted-ip>` behind a firewall.

**Does it support streaming or concurrent requests?** No streaming. It polls every 2 seconds and returns once the content is unchanged for 3 consecutive polls. Requests are serialized by a lock.

**What happens on timeout?** `/chat` returns `status: "timeout"` with whatever partial reply was captured.

**Does it work with the Chinese grok.com UI?** Yes — it recognizes the `发送` / `提交` buttons (中文界面).

**It stopped working after a grok.com update?** Run `--doctor` first, then open an issue. The selectors live in `INPUT_SELECTORS` / `SEND_SELECTORS` in `scripts/grok_bridge.py`.

**Can I use it from Claude Code or other AI agents?** Yes — any agent that can call an HTTP endpoint can use it, and the repo includes a `SKILL.md`. There is no official integration with any platform. AI agent 调用 Grok 只需 HTTP 请求。

## Safe review smoke (read-only)

For reviewer-style onboarding, prefer these commands before sending any prompt:

```bash
python3 scripts/grok_bridge.py --help
python3 scripts/grok_bridge.py --doctor
curl -s http://127.0.0.1:19998/health
curl -s http://127.0.0.1:19998/history
lsof -nP -iTCP:19998 -sTCP:LISTEN
# if a listener exists, capture its PID provenance before trusting the output
ps -p <PID> -o pid=,ppid=,lstart=,command=
```

Notes:
- `bash scripts/grok_chat.sh --help` only prints usage; it does not start Safari automation.
- `--doctor` does not send prompts. It only checks platform, `osascript`, Safari reachability, current Grok URL, and input availability.
- By default, server and `--doctor` operate on a dedicated background tab marked with `window.name="grok-bridge-agent"`. Use `--shared-tab` for manual current-tab debugging.
- If port `19998` is already occupied, classify it as an environment conflict before blaming bridge logic.
- If a listener already exists on `19998`, capture `ps -p <PID> -o pid=,ppid=,lstart=,command=` so reviewers can tell whether `/health` and `/history` came from the current checkout or a stale long-lived process.
- See `docs/review-playbook.md` for evidence format, error taxonomy, and multi-agent ownership split.

## Version History

| | v1 | v2 | v3.1.1 |
|---|---|---|---|
| Input | Peekaboo UI | pbcopy + Cmd+V | JS `execCommand('insertText')` |
| Submit | UI click | System Events Return | JS visible button click / Enter fallback |
| UI support | English button labels | English button labels | English + Chinese send labels (`Send`, `Submit`, `发送`, `提交`) |
| Permissions | Peekaboo + Accessibility | Accessibility | **None by default** (pure JS injection) |
| Interface | CLI only | CLI only | **REST API** + legacy CLI |
| Dependencies | Peekaboo (brew) | None | None (stdlib only) |
| Network boundary | N/A | SSH/manual | `127.0.0.1` by default; remote via tunnel/proxy |
| Speed | ~30s | ~3s | ~3s |

`v3.1.1` is the publishable release that supersedes the `v3.1.0` release-candidate attempt. It keeps the stable v3 loopback/dedicated-tab boundary and highlights the grok.com Chinese UI submit-button fix. See [docs/release-v3.1.1.md](docs/release-v3.1.1.md).

## Architecture

```
┌──────────────┐                     ┌───────────────────────┐
│  HTTP Client │  POST /chat         │      macOS            │
│  (local/tunnel)│ ─────────────────→ │                       │
└──────────────┘                     │  grok_bridge.py       │
                                     │  ↓ osascript          │
                                     │  Safari do JavaScript │
                                     │  ↓ execCommand        │
                                     │  grok.com textarea    │
                                     │  ↓ button.click()     │
                                     │  Grok responds        │
                                     │  ↓ DOM poll           │
                                     │  Response extracted   │
                                     └───────────────────────┘
```

## Key Insight (v3)

React controlled inputs ignore JavaScript `value` setter, synthetic `InputEvent`, and even `nativeInputValueSetter`.

What **doesn't** work from SSH:
- ❌ `osascript keystroke` — blocked by macOS Accessibility
- ❌ CGEvent (Swift) — HID events don't reach web content (the REST API does not use it; the legacy `grok_chat.sh` still does)
- ❌ JS `InputEvent` / `nativeInputValueSetter` — React ignores synthetic events

What **does** work:
- ✅ `document.execCommand('insertText')` — triggers real input in the browser
- ✅ JS `button.click()` on Send button — no System Events needed
- ✅ Dedicated Safari tab via `window.name="grok-bridge-agent"` — avoids taking over the user's current Grok tab

Zero Accessibility permissions by default, zero dependencies, pure JavaScript injection via AppleScript.

## Credits

v3 architecture designed by Claude Opus 4.6 (via [Antigravity](https://antigravity.google)), System Events bypass by 小灵 🦞.

## Disclaimer

Unofficial project, not affiliated with xAI. It only drives your own signed-in session on your own Mac; please follow grok.com's terms of service. grok.com UI changes may break the selectors — issues are welcome.

## License

MIT
