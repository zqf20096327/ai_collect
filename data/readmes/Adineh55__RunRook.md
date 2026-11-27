<p align="center">
  <img src="https://raw.githubusercontent.com/Adineh55/RunRook/main/logo-mark.svg" width="88" alt="RunRook logo">
</p>

<h1 align="center">RunRook</h1>

<p align="center">
  See every AI agent running on your computers in one native Mac app.<br>
  Know what each agent is doing, what it did, and when it needs you.
</p>

---

**[Download the latest RunRook](https://github.com/Adineh55/RunRook/releases/latest)** (more at **[runrook.app](https://runrook.app)**) — open the DMG and drag RunRook to Applications. macOS 14 or later on Apple silicon. Free to use; Pro removes the limits. Updates install automatically.

This repository holds RunRook's releases only. The app's source is private.

## What you get

- **Every session in one list:** Claude Code and Codex (live, started before RunRook opened, and the last 7 days), local models in Ollama and LM Studio, and Cursor (preview). Open one for its story: your messages, the agent's replies, the commands it ran and what failed.
- **"Needs you" alerts** in Notification Center and the menu bar when an agent waits for you.
- **Answer and follow up:** pick an answer to an agent's question, send a follow-up, or continue a closed Claude Code or Codex session inside RunRook, with Allow and Deny for its permission prompts. Only you can reply.
- **Your other computers:** add a Mac, Linux or Windows computer with one setup command and a matching code. Add a Linux server over SSH with the setup you already use: RunRook shows its fingerprint to compare, keeps its helper up to date and finds agents in containers under your account. <!-- feature: server-history -->
- **Server history, even while your Mac sleeps:** tick **Kept here** to copy a server's Claude Code and Codex history to your Mac, encrypted. Watch mode saves what its agents do, sealed with your Mac's key, until your Mac collects it. <!-- feature: watch -->
- **Search and carry over context:** ⌘K searches kept history, **Copy context** makes a summary to paste into another chat or agent, and **Settings › Agents** lets Claude, Codex, Cursor and LM Studio search your past sessions themselves, read-only (Pro).
- **Scripts and hooks:** `runrook event` reports cron jobs, long scripts and agent hooks to RunRook, with no key and no network. Recipes are in the [events guide](EVENTS.md). <!-- feature: events -->
- **Cloud agents (Preview):** a **Cloud** page for Claude cloud sessions you start or bring in, GitHub Copilot agent tasks, and the pull requests agents opened in repositories you choose. Each is off until you turn it on. <!-- feature: copilot -->
- **Viewers:** invite someone to see status from their own device. Viewers never see message text. With Pro, viewers on your network open your invite links without a browser warning. <!-- feature: trusted-links -->

## Plans

**Free** connects 2 other computers and shares with 3 viewers. **Pro** ($39 once, 12 months of updates, for one Mac) removes the limits and adds agent access. For now Pro is available by email from [support@runrook.app](mailto:support@runrook.app): see **Settings › Plan and licence** in the app.

## Privacy

**Your chats, code and sessions stay on your Mac.** We don't store them, we can't see them and we have no access to them: nothing you or your agents write is sent to us or kept in any database or cloud of ours. There's no account and no analytics. A few features you turn on yourself send something to a place you choose (an agent's own provider, a cloud environment you connect), and when a conversation passes through a RunRook service on the way (cloud saving), it's sealed with a key we don't have.

The rest of this section is the detail, so you can check that promise: what RunRook reads, what it keeps, and every request that leaves your Mac. When RunRook starts sending anything new, it's added to the table below in the same release.

- RunRook watches, and acts only when you ask: it can deliver a message, an answer or an Allow/Deny you choose to a Claude Code or Codex session, through the runtime's own documented route. It never starts, stops or changes your agents on its own.
- Nothing is read until you connect a source. RunRook reads the transcripts of the agents you connect to work out their status and show you their story. Conversation text stays on your Mac and is never sent to viewers.
- Kept session history, on by default: Claude Code deletes its transcripts after 30 days and compacts long sessions, so RunRook keeps an encrypted copy of what matters (prompts, replies, commands, errors, plans; never thinking or successful command output) on your Mac for a year or up to a size you choose, to search later. The key stays in your Mac's keychain. **Settings › Kept session history** turns it off and deletes it.
- Agent access (Pro) is read-only and off until you connect an agent. What an agent reads from RunRook goes to that agent's model provider, like the rest of its chat.
- Everything RunRook keeps is in `~/Library/Application Support/RunRook`. Sessions not seen for a year are forgotten. **Settings › Remove RunRook data** deletes it and undoes anything RunRook set up.

### What leaves your Mac

| What | When | Goes to | Carries |
| --- | --- | --- | --- |
| Update check | Every few hours, unless automatic update checks are off in Settings | GitHub, which hosts RunRook's releases | Nothing about you or your agents. GitHub sees the request, like any download |
| Daily count | The first automatic update check of each day | GitHub | A download of a copy of the update feed, so Macs can be counted. No ID |
| Plan limits | While Codex or Cursor is connected on this Mac | OpenAI, through your own Codex app; Cursor's servers, with your Cursor sign-in | The same request those apps make for your own account. Claude Code's limits are read locally |
| Network port 47821 | On by default (**Settings › Access from other devices**). Open while another computer is linked, a viewer has access or an invite, a script sends events, and for 15 minutes after you open Computers, so a new computer can find this Mac. Turn it off there to keep RunRook to this Mac | Your local network | Encrypted with this Mac's own key. While computers are linked, a network announcement named only "RunRook" helps them find this Mac; this Mac's name appears only while you add a computer |
| Linked computers | While linked | This Mac only, over the encrypted connection that trusts this Mac's key | Their sessions and status, and a session's story only when you open it |
| Trusted network links (Pro) | Only with Pro, and only while you share with viewers on your network (a viewer has access or an invite is open) | RunRook's naming service (`names.runrook.app`, hosted on Cloudflare), which publishes the name in public DNS; Let's Encrypt, which issues the certificate; Cloudflare's public DNS (`cloudflare-dns.com`, over HTTPS), which this Mac asks whether its new names are published yet | A random ID for this Mac and its addresses on your local network (for example `192.168.1.20`), never its name or anything about your agents. Certificates are public, so the random ID appears in Certificate Transparency logs; the addresses don't. The certificate's key stays on this Mac. The names are removed when sharing stops <!-- feature: trusted-links --> |
| Viewers | While they have access | Their own browser | The computers and fields you share. Never message text |
| Your replies | Only when you send a message or answer from a session page | The computer that holds the session, then that agent's own provider (Anthropic or OpenAI) as when you type in it. Your own agents fetch theirs from RunRook | Your message, answer or Allow/Deny, to that session only. RunRook keeps nothing, except a message for your own agent until it fetches it (at most 24 hours) |
| Licence check | Only for a key bought through Dodo Payments: when you add it, at most once a day after, and when you remove it. Keys issued by RunRook are checked on your Mac and send nothing | Dodo Payments, which sells RunRook licences | The key and a random install name. Never this Mac's name or anything about your agents. **Upgrade** opens Dodo Payments' checkout in your browser; RunRook sends nothing for it |
| Continue in Claude cloud, bring a session in | Only when you click it | Anthropic, through your own Claude Code | The brief you previewed, or the cloud session's ID. The conversation comes back to this Mac <!-- feature: claude-cloud --> |
| Copilot agent tasks | While GitHub Copilot is on in Cloud | GitHub, through your own GitHub CLI (`gh`) | The same request `gh agent-task list` makes to list your Copilot coding agent tasks <!-- feature: copilot --> |
| GitHub activity | Only for the repositories you choose in Cloud › GitHub activity, while it's on: a few repositories every 2 minutes | GitHub, through your own GitHub CLI (`gh`) | The repository names and the pull request lookups `gh pr list` makes for them. Nothing from your computer <!-- feature: github-activity --> |
| Agents on your servers asking RunRook | Only for the servers and agents you connect in Settings › Agents | Nowhere new: the question travels over the SSH connection RunRook already uses, and is answered from that server's kept history | The question and the part of kept history that answers it, then that agent's model provider as part of its chat <!-- feature: server-agents --> |
| Server watch mode | Only for the Linux servers you turn it on for in Sources (Keep reading while this Mac is away) | Nowhere new: it stays on that server until this Mac collects it over the SSH connection it already uses | What that server's Claude Code and Codex sessions did while this Mac was away, sealed with this Mac's key on the server, so the server can't read it back. At most 256 MB there; deleted from the server once this Mac has it <!-- feature: watch --> |

Nothing else leaves your Mac. No analytics, crash reports or account.

## Verifying a download

Each release is signed with Developer ID (Horizon Path SPC, team B96DZZW55C) and notarized by Apple. Its `MANIFEST.txt` lists the SHA-256 of every file. To check a download:

```bash
shasum -a 256 ~/Downloads/RunRook-*.dmg
```

```bash
spctl -a -vv -t open --context context:primary-signature ~/Downloads/RunRook-*.dmg
```

## Help and feedback

Guides and news: [runrook.app](https://runrook.app). Open an [issue](https://github.com/Adineh55/RunRook/issues) for bugs and ideas, or write to [hey@runrook.app](mailto:hey@runrook.app); for help, [support@runrook.app](mailto:support@runrook.app). Report a security problem privately: see [SECURITY.md](SECURITY.md). You can support development on [Ko-fi](https://ko-fi.com/adineh) or [PayPal](https://paypal.me/adineh55).

## License

© 2026 Horizon Path SPC. All rights reserved. RunRook is free to use under the terms in [LICENSE](LICENSE); Pro features follow the terms shown at purchase. It includes open-source components under their own licenses, listed inside the app. Product names and logos belong to their owners; RunRook isn't affiliated with or endorsed by them.
