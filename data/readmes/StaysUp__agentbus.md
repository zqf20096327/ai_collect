<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/agentbus-logo-dark.svg">
  <img alt="AgentBus" src="docs/assets/agentbus-logo-light.svg" width="360">
</picture>

**Control every AI agent in a single place.**

[![GitHub stars](https://img.shields.io/github/stars/staysup/agentbus?style=flat)](https://github.com/staysup/agentbus/stargazers)
[![Latest release](https://img.shields.io/github/v/release/staysup/agentbus)](https://github.com/staysup/agentbus/releases)
[![CI](https://github.com/StaysUp/agentbus/actions/workflows/ci.yml/badge.svg)](https://github.com/StaysUp/agentbus/actions/workflows/ci.yml)

[Quickstart](#quickstart) &nbsp;&bull;&nbsp; [Demo](https://youtu.be/si0HHQFcCD0) &nbsp;&bull;&nbsp; [Docs](#docs) &nbsp;&bull;&nbsp; [Releases](https://github.com/staysup/agentbus/releases)

</div>

[![AgentBus demo](https://img.youtube.com/vi/si0HHQFcCD0/maxresdefault.jpg)](https://youtu.be/si0HHQFcCD0)

AgentBus sits between your coding agents and every model vendor. It runs the agents you already
have (Claude Code, Codex, Antigravity or any OpenRouter model) and tracks every step.

- **Your agents work together.** Claude can ask Codex, or any agent from any vendor, to answer a
  question, take on a task or check its work. The answer comes back into the same session.
- **You see every model call**, and what it cost: exactly what each model was sent, piece by piece,
  and what it answered.
- **Your folder stays as it is.** Each session works in its own copy. You review the changes and
  apply them to your folder. Turn on the sandbox to make the copy a hard wall.
- **Everything stays on your machine.** Your sessions, every model call and reply, and your sign-ins
  and keys are kept in AgentBus's data folder on your machine.

## Install

You need macOS or Linux, and `claude`, `codex` or `agy` installed. Use **one** of these:

**Install script** (puts the binary in `~/.local/bin`):

```sh
curl -fsSL https://raw.githubusercontent.com/staysup/agentbus/main/install.sh | sh
```

**Homebrew** (macOS or Linux):

```sh
brew install staysup/tap/agentbus
```

**From source** (Go 1.27.1 or later):

```sh
go install github.com/staysup/agentbus/cmd/agentbus@latest
```

The install script takes `AGENTBUS_INSTALL_DIR` (another folder) and `AGENTBUS_VERSION` (another
release). Check the install with `agentbus version`.

## Quickstart

A first run, from nothing to two vendors talking about the same work. You need `claude` and `codex`
installed, and a Claude and a ChatGPT subscription.

1. **Start AgentBus.**

   ```sh
   agentbus up -open
   ```

   It prints a sign-in link, `http://127.0.0.1:8787/?t=…`, and with `-open` opens it in your
   browser. Without `-open` (on a server, say) it only prints the link. The cockpit comes with
   `agentbus up`: nothing else to install. The link works once, for 10 minutes. The link expired?
   Stop `agentbus up` (Ctrl-C) and start it again for a new one.

   In another tab or browser, paste your token on the connect screen instead. The token is the file
   `token` in the data folder that `agentbus up` prints when it starts (`$AGENTBUS_HOME`, by default
   `~/.local/share/agentbus`). Copy it
   without showing it: `pbcopy < ~/.local/share/agentbus/token` on a Mac, or
   `xclip -sel c < ~/.local/share/agentbus/token` on Linux. Anyone with the token controls your
   agents, so keep it to yourself.

2. **Add your agents.** A new AgentBus starts with no agents. Press **+ Agent** at the top of the
   Agents column, pick Claude Code, and press **Create agent**. Do the same for Codex.

3. **Connect your subscriptions.** Open **Settings** (at the foot of the Agents column), then
   **Subscriptions**. Press **Connect** next to Claude Code and sign in as it asks. Do the same for
   Codex. You do this once.

4. **Bring your setup (optional).** In **Settings**, **Config**, press **Use my config**, look over
   the list and save. Your settings, skills, MCP servers and logins such as `gh` and `aws` then come
   into every session.

5. **Ask Claude something.** Press **+ Session**, pick Claude Code, type the path of a project
   folder, write a first message such as "what does this project do?", and press **Start**.

6. **Ask Codex about it.** In the same session, switch the agent beside Send to Codex, and send
   "what do you think about the answer above?". Codex reads Claude's answer and gives its own.

Every turn and every model call is now in the record, with its cost.

### Sign-ins and keys

Every turn uses the sign-in connected in Settings. A tool's own sign-in on your machine
(`~/.claude`, `~/.codex`) is not used: each session runs in a home of its own. A turn whose tool is
not connected is refused with "connect your claude subscription in Settings".

An agent can also use an API key instead of a subscription. Paste the key once in Settings,
Subscriptions: an OpenRouter key for any OpenRouter model, or the vendor's own key (Anthropic for
Claude Code, OpenAI for Codex, Gemini for Antigravity). AgentBus keeps it, adds it only to that
vendor's model calls, and never shows it again or gives it to an agent. **Replace** and **Remove**
change it.

## Settings

Settings apply to every session, from the next turn. Change them on the cockpit's Settings page, or
through the API (`/api/v0/settings/permissions` and `/api/v0/settings/instructions`; the keys and
their defaults are in `/docs`, under Settings).

- **Workspace:** each session works in its own copy of your folder. Shared folders (such as
  `node_modules`) are used read-only instead of copied; read folders may be read as well.
- **Config:** files from your home copied into each session's own home at each turn: your
  settings, skills, MCP servers and logins. **Use my config** fills the list. Sign-ins are never
  copied.
- **Permissions:** the AgentBus tools agents may use (ask another agent, review), whether they may
  start their own subagents (off by default, so the work is recorded), and whether an agent may
  apply its own changes (off by default; you always may).
- **Isolation:** the sandbox walls each session to its folder and its home. Network contain lets
  agents reach only the hosts you list. Commands: what agents may run, and what they may never run.
  Both are off by default.
- **Limits:** how much work one message may cause: how deep agents may ask each other, how many
  turns, and the cost.

## Known limits

- On Ubuntu 24.04 and later, AppArmor allows user namespaces only to a program with a profile, so
  the sandbox and network contain need one. The install script offers it when it installs into a
  folder only root can change: `curl -fsSL https://raw.githubusercontent.com/staysup/agentbus/main/install.sh | sudo AGENTBUS_INSTALL_DIR=/usr/local/bin sh`.
  The profile is `packaging/apparmor/agentbus`, also in each release archive. AgentBus says what is
  missing. The fallback is `sudo sysctl kernel.apparmor_restrict_unprivileged_userns=0`, which turns
  the rule off for every program, so the profile is the better choice.
- On ext4 a copy is a full copy. A clone (APFS) or a reflink (xfs, btrfs) is used where the disk can
  make one.
- MCP servers in your config load on normal turns, never on read-only ones. On a Mac, a server that
  signs in with OAuth keeps its token in the Keychain, and macOS asks to let the session read it;
  deny it to keep that server off. What a server does is outside AgentBus's record.
- Claude's browser (Chrome) cannot run in AgentBus sessions: it needs the tool's own sign-in.
- Antigravity: use it with a Gemini API key (Settings, Subscriptions). Its Google sign-in does not
  work through AgentBus yet: before any work it checks your account with Google directly, outside
  AgentBus, and that check fails. It gets no instructions from AgentBus, a turn with forbidden
  commands set is refused on it, and it cannot turn off its own subagents.

## Docs

The running service describes its own API, without the token or the internet:

- `http://127.0.0.1:8787/docs`: the API reference, as a page.
- `http://127.0.0.1:8787/api/v0/openapi.json`: the same, as OpenAPI 3.1. It is the contract.
  Generate a client from it in any language.
- `http://127.0.0.1:8787/docs/llms.txt`: one short page for coding agents.

Running agents on more than one machine is in [docs/RUNNER_PROTOCOL.md](docs/RUNNER_PROTOCOL.md). Third-party
code in the binary is listed in [THIRD_PARTY.md](THIRD_PARTY.md).

## License

Free to use, change and run, including inside your business. You can't sell it as a competing product or service. Each release becomes Apache 2.0 two years after it is published.

Licensed under the [Functional Source License](https://fsl.software) (FSL-1.1-ALv2). See [LICENSE](LICENSE).
