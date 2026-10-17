# espai

**Any agent that can run `curl` gets a real browser.**

espai is a native messaging host and a Chromium extension. Together they put a running
browser behind a plain HTTP server on `127.0.0.1`. An agent lists tabs, snapshots a page,
clicks something, reads what came back.

No SDK, no client library, no language bindings, no WebDriver, no MCP server to register, no
API key. If it can shell out to `curl`, it can drive the browser — which includes cron jobs,
shell scripts, and whatever agent loop you wrote yourself.

**About the name.** *spy* + *AI*. It is meant as a reminder: while espai is running, you are
sharing your browser with something that is not you, and it can see everything you are
logged into.

> **Not hardened for a machine you do not trust.** Any process running as your user can
> drive your browser through it. See [Security](#security).

## Contents

- [How you use it](#how-you-use-it) — [Examples](#examples)
- [Install](#install) — [Check it works](#check-it-works)
- [The API describes itself](#the-api-describes-itself)
- [Finding the port](#finding-the-port)
- [Why it works on real sites](#why-it-works-on-real-sites)
- [Chromium only](#chromium-only)
- [Security](#security)
- [License](#license)

## How you use it

Install it once ([below](#install)). After that there are two things to know.

**Keep a browser window open.** The extension holds the connection to the host, and the host
is the HTTP server. The server lives exactly as long as a browser with the extension is
running. Quit the browser and it goes too. Nothing to start, nothing to leave running in a
terminal.

**Say one sentence to whatever agent you already use.** Put a clause in front of what you
were going to ask for anyway:

> Read `~/espai.toml`, then **whatever you wanted done in the browser — debugging,
> summarising, comparing, filling in, watching for a change**.

The bold half is your actual request. The clause in front of it is the whole integration:
that file says how to find the port, and the port serves a complete guide to the rest.

Works with anything that can run a shell command — **Claude Code, Codex, Cursor, Gemini CLI,
Copilot CLI** — or a script of your own.

### Examples

> Read `~/espai.toml`, then **go through my GitHub timeline and give me the three new repos
> actually worth checking, keep them open in tabs**.

![Claude Code in VS Code reading a GitHub timeline, the three repos it picked open in
Chrome](screenshots/claude-vscode-github.png)

---

> Read `~/espai.toml`, then **search Amazon for a 4-slice toaster, open the top three, and
> build me a table of price, rating, review count and wattage — keep the tabs open in
> browser so I can see them**.

![Cursor comparing three Amazon toasters, the product pages open in
Chrome](screenshots/cursor-amazon.png)

---

> Read `~/espai.toml`, then **open Polymarket and give me the ten biggest markets right now
> with their current odds and volume. Have two interesting open in browser**.

![Claude Code listing the ten largest Polymarket markets with volume and odds, two open in
Chrome](screenshots/claude-polymarket.png)

---

If you do this often, put the clause in your agent's instructions file — `CLAUDE.md`,
`AGENTS.md`, `.cursorrules`, a system prompt — and stop typing it:

```
When a task needs a real browser, read ~/espai.toml and follow what it says.
```

## Install

Linux and macOS, x86_64 and arm64:

```bash
curl -fsSL https://raw.githubusercontent.com/pouriya/espai/master/install.sh | sh
```

Windows, in PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -c "irm https://raw.githubusercontent.com/pouriya/espai/master/install.ps1 | iex"
```

Either one downloads a release, puts the host binary in `~/espai/`, and registers it with
Chrome, Chromium, Edge, Brave, Opera, Vivaldi and Arc. On Unix it copies a manifest into
every browser profile directory that already exists and skips the ones that do not. On
Windows browsers read the path from a registry key instead, so every key gets written — a
key for a browser you never install does nothing. Arc on Windows is the one gap, since its
key is undocumented.

Then load the extension. This is the one step no script can do for you:

`chrome://extensions` → enable **Developer mode** → **Load unpacked** → `~/espai/extension`

Two things to expect afterwards, both normal:

- Chrome warns about developer-mode extensions on every start. espai is not on the Web Store.
- While espai drives a tab, Chrome shows a **"espai started debugging this browser"** banner.
  That is `chrome.debugger`, and it is why DevTools and espai cannot both be open on one tab.

`ESPAI_PREFIX` changes where it installs, `ESPAI_VERSION` pins a version. To build from
source or uninstall, see [CONTRIBUTING.md](CONTRIBUTING.md).

### Check it works

The host is lazy: Chrome starts it when the extension connects, so open a page first. Then:

```bash
cat ~/espai.toml                             # one entry per running browser profile
curl -s http://127.0.0.1:$PORT/health        # {"espai":true,...}
curl -s http://127.0.0.1:$PORT/              # the full API guide
```

On Windows use `curl.exe`. Bare `curl` is an alias for `Invoke-WebRequest` and takes none of
these flags. `~/espai.toml` includes a PowerShell line for reading the port.

## The API describes itself

`GET /` returns a complete markdown guide to every endpoint. So does every 404. An agent
that guesses a path wrong gets the whole API back in the error body and gets it right on the
next call. Nobody writes integration notes, and there are none to go stale.

In practice that means four calls cover most of it:

```bash
PORT=$(grep -m1 '^port' ~/espai.toml | tr -dc 0-9)

curl -s -H 'X-Espai: 1' http://127.0.0.1:$PORT/tabs             # what is open
curl -s -H 'X-Espai: 1' http://127.0.0.1:$PORT/tabs/42/snapshot # the page, as refs
curl -s -H 'X-Espai: 1' -H 'Content-Type: application/json' -d '{"ref":17}' http://127.0.0.1:$PORT/tabs/42/click
curl -s -H 'X-Espai: 1' -H 'Content-Type: application/json' -d '{"text":"Posted"}' http://127.0.0.1:$PORT/tabs/42/wait
```

That `17` is a **ref**: a number `snapshot` gives to every element worth acting on, used
instead of a CSS selector. Nothing is generated and no code is written on either side.

`X-Espai: 1` goes on every call. It is not a password. It is a header no web page can send,
which is what keeps the site you are visiting away from this port. `GET /` and `GET /health`
are exempt so discovery works before you know the rule. See [Security](#security).

<details>
<summary>The surface it describes</summary>

```
GET  /                          this guide
GET  /health                    {"espai":true,...}, answered without the browser
GET  /events?since=N&wait=30    long-poll the event log
GET  /tabs                      every open tab
POST /tabs                      {"url":"...","active":true} → opens one
DELETE /tabs/{id}               closes it
GET  /tabs/{id}                 url, title, loading state, frames
GET  /tabs/{id}/title           title read from the live DOM
GET  /tabs/{id}/snapshot        the page as a ref-tagged outline
GET  /tabs/{id}/text            visible readable text
GET  /tabs/{id}/html            ?within=REF for one subtree
GET  /tabs/{id}/query?sel=CSS   matches with text, attributes, box, ref
GET  /tabs/{id}/screenshot      PNG bytes; ?full=1 for the whole page
GET  /tabs/{id}/network         captured requests; ?filter=SUBSTR &body=0:400
GET  /tabs/{id}/console         captured console lines
```

Everything below takes a JSON body and targets an element with `{"ref":17}` or
`{"sel":"CSS"}`:

```
POST /tabs/{id}/navigate   {"url":"..."} | {"back":true} | {"forward":true} | {"reload":true}
POST /tabs/{id}/click      {"ref":17,"button":"left","clicks":1,"modifiers":["Shift"]}
POST /tabs/{id}/type       {"ref":17,"text":"hello","clear":true,"submit":true}
POST /tabs/{id}/key        {"key":"Enter","modifiers":["Control"]}
POST /tabs/{id}/hover      {"ref":17}
POST /tabs/{id}/scroll     {"by":[0,800]} | {"to":[0,0]} | {"ref":17}
POST /tabs/{id}/select     {"ref":17,"value":"uk"}
POST /tabs/{id}/wait       {"sel":"CSS"} | {"text":"..."} | {"gone":"CSS"} | {"url":"SUBSTR"} | {"network_idle":true}
POST /tabs/{id}/collect    {"sel":"article","fields":{"who":"a","body":"[lang]"},"max":100}
POST /tabs/{id}/eval       {"js":"return document.title"}
```

Screenshots are real PNG bytes and work below the fold and in background tabs. `collect`
scrolls an infinite feed, pulls fields out of every match, and deduplicates until it hits a
limit or the bottom.

</details>

## Finding the port

Ports come from the OS at startup and are never fixed. Every running instance registers
itself in `~/espai.toml`:

```toml
[[instances]]
pid = 9182
port = 43111
started_at = 1754241234
origin = "chrome-extension://aaaabbbbccccddddeeeeffffgggghhhh/"
```

One entry per running browser profile. Two profiles means two independent browsers with
different tabs; `GET /tabs` on each says which is which. Entries that no longer answer are
cleaned up whenever an instance starts, so anything listed should respond.

The file has a comment header, written even when there are no entries, so a file listing
nothing still tells an agent what to check.

It is written `0600` on Unix. Home directories are world-readable on most distributions, so
the port would otherwise be legible to every account on the machine. **The port is not a
secret** — 127.0.0.1 is reachable by any local user, and 16 bits of port space is a short
scan against `/health`. The file mode raises reading a file to scanning for a server. It
authenticates nothing.

## Why it works on real sites

**Read the JSON, not the rendered DOM.** Feeds and product listings arrive as JSON long
before they become DOM, and that is easier to read and more complete than scraping the
render. Every response is logged with its metadata. Payloads stay in the browser until you
ask for a window onto one, so peeking at 400 characters of a 300KB response costs 400
characters.

**Refs, not CSS selectors.** App sites generate their class names, so a selector written
today breaks next week. `snapshot` returns the page as an outline where everything worth
acting on carries a number:

```
[1] link "Home" /home
[2] article
  [3] link "@someone"
      text "the post body here"
  [4] button "Like" pressed=false
```

A ref is stable across snapshots. A ref whose element is gone returns **410** — "the page
moved on, snapshot again" — instead of a generic failure you might retry forever.

**Trusted input.** Clicks and keystrokes go through `chrome.debugger` and the browser's own
input pipeline, so `isTrusted` is true and the page cannot tell them from a person's. React
and most of what large sites are built on ignore events synthesised from script, and the
failure mode there is a click that reports success and does nothing.

None of this is site-specific. Generic primitives plus the agent's own prompt beat a
selector file that rots.

## Chromium only

Firefox support was built and then removed. Firefox implements none of `chrome.debugger`, so
trusted input, screenshots, `eval` and the network capture are all impossible there. What is
left is reads and navigation, which is a worse way to fetch a page. A Firefox version would
be a different project with a different mechanism, not a flag here.

## Security

espai drives the browser you are logged into. Anything it clicks, you clicked. There are two
attackers, and only one of them is answered.

**A web page in your own browser — answered.** Any page can POST to a loopback port, and a
CORS simple request goes out without a preflight. Four checks run before the body is read,
so a refused request has no effect at all:

- a missing **`X-Espai`** header is **403**. A page cannot set one on an `<img>`, an
  `<iframe>` or a navigation, and setting it on `fetch` requires a CORS preflight that is
  never answered. This is the real defence, and the only one that covers GET. `GET /` and
  `GET /health` are exempt; neither touches a tab.
- an **`Origin`** header is **403**. Browsers always send it cross-origin; `curl` never does.
- a **`Host`** that is not `127.0.0.1` or `localhost` is **403**, which catches DNS rebinding.
- a **POST** that is not `application/json` is **415**.

Each one has a test behind it standing for a request a real page can make.

**Another process running as you — not answered.** espai is **not authenticated**. Any
process under your user reads the port from `~/espai.toml` and calls in exactly like a
legitimate agent. The checks above establish that a caller is not a web page. They establish
nothing about who it is.

A token would not fix this, because the token sits under the same user the attacker already
has. It is an OS boundary, not an HTTP one.

So there is no plan yet that makes espai safe against the machine it runs on. Treat the API
as equivalent to a logged-in browser session, because that is what it is.

## License

MIT. See [LICENSE](LICENSE).
