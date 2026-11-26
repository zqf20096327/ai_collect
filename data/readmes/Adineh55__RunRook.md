<p align="center">
  <img src="https://raw.githubusercontent.com/Adineh55/RunRook/main/logo-mark.svg" width="88" alt="RunRook logo">
</p>

<h1 align="center">RunRook</h1>

<p align="center">
  See every AI agent running on your computers in one native Mac app.<br>
  Know what each agent is doing, what it did, and when it needs you.
</p>

---

**[Download the latest RunRook](https://github.com/Adineh55/RunRook/releases/latest)** — open the DMG and drag RunRook to Applications. macOS 14 or later on Apple silicon. Free to use; Pro removes the limits. Updates install automatically.

This repository holds RunRook's releases only. The app's source is private.

## What you get

- **Every session in one list:** Claude Code and Codex (including sessions started before RunRook opened, and the last 7 days), agents built on the Claude Agent SDK, local models in Ollama and LM Studio, and Cursor (preview).
- **The story of each session:** your messages, the agent's replies, the commands it ran and what failed.
- **"Needs you" alerts** in Notification Center and the menu bar when an agent waits for you.
- **Answer and follow up:** pick an answer to an agent's question, send a follow-up, or continue a closed Claude Code or Codex session right inside RunRook with Allow and Deny for its permission prompts. Only you can reply.
- **Your other computers:** add a Mac, Linux or Windows computer with one setup command and a matching code on both screens.
- **Viewers:** invite someone to see status from their own device. Viewers never see message text.
- **Free and Pro:** Free connects 2 other computers and shares with 3 viewers. Pro ($39 once, 12 months of updates, for one Mac) removes the limits. For now Pro is available by email: see **Settings › Plan and licence** in the app.

## Privacy

- RunRook watches, and acts only when you ask: it can deliver a message, an answer or an Allow/Deny you choose to a Claude Code or Codex session, through the runtime's own documented route. It never starts, stops or changes your agents on its own.
- Nothing is read until you connect a source. RunRook reads the transcripts of the agents you connect to work out their status and show you their story. Conversation text stays on your Mac, isn't stored by RunRook, and is never sent to viewers.
- Everything RunRook keeps is in `~/Library/Application Support/RunRook`. Sessions not seen for 90 days are forgotten. **Settings › Remove RunRook data** deletes it and undoes anything RunRook set up.

### What leaves your Mac

| What | When | Goes to | Carries |
| --- | --- | --- | --- |
| Update check | Every few hours, unless automatic update checks are off in Settings | GitHub, which hosts RunRook's releases | Nothing about you or your agents. GitHub sees the request, like any download |
| Daily count | The first automatic update check of each day | GitHub | A download of a copy of the update feed, so Macs can be counted. No ID |
| Plan limits | While Codex or Cursor is connected on this Mac | OpenAI, through your own Codex app; Cursor's servers, with your Cursor sign-in | The same request those apps make for your own account. Claude Code's limits are read locally |
| Network port 47821 | Only while another computer is linked, a viewer has access or an invite, a script sends events, or you're adding a computer | Your local network | Encrypted with this Mac's own key. While computers are linked, a network announcement named only "RunRook" helps them find this Mac; this Mac's name appears only while you add a computer |
| Linked computers | While linked | This Mac only, over the encrypted connection that trusts this Mac's key | Their sessions and status, and a session's story only when you open it |
| Viewers | While they have access | Their own browser | The computers and fields you share. Never message text |
| Your replies | Only when you send a message or answer from a session page | The computer that holds the session, then that agent's own provider (Anthropic or OpenAI) as when you type in it. Your own agents fetch theirs from RunRook | Your message, answer or Allow/Deny, to that session only. RunRook keeps nothing, except a message for your own agent until it fetches it (at most 24 hours) |
| Licence check | Only for a key bought through Dodo Payments: when you add it, at most once a day after, and when you remove it. Keys issued by RunRook are checked on your Mac and send nothing | Dodo Payments, which sells RunRook licences | The key and a random install name. Never this Mac's name or anything about your agents. **Upgrade** opens Dodo Payments' checkout in your browser; RunRook sends nothing for it |

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

Open an [issue](https://github.com/Adineh55/RunRook/issues) for bugs and ideas. Report a security problem privately: see [SECURITY.md](SECURITY.md). You can support development on [Ko-fi](https://ko-fi.com/adineh) or [PayPal](https://paypal.me/adineh55).

## License

© 2026 Horizon Path SPC. All rights reserved. RunRook is free to use under the terms in [LICENSE](LICENSE); Pro features follow the terms shown at purchase. It includes open-source components under their own licenses, listed inside the app. Product names and logos belong to their owners; RunRook isn't affiliated with or endorsed by them.
