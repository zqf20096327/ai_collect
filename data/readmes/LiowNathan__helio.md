<div align="center">

<img src="https://i.imgur.com/DevH94V.png" width="88" alt="Helio">

# Helio

**The assistant built into the Helius docs.**

Ask about your RPC in plain language and get the call, the request body and the reference, without leaving the page.

</div>

<p align="center">
  <img src="https://img.shields.io/badge/release-29.11.2026-24292f?style=flat" alt="release">
  <img src="https://img.shields.io/badge/staged-not%20live%20yet-24292f?style=flat" alt="staged">
  <img src="https://img.shields.io/badge/keys-never%20stored-24292f?style=flat" alt="keys">
</p>

> **Release 29.11.2026.** Not live on helius.dev yet. This repository is the staging source: the site build reads it and picks up the release on deploy.

<p align="center">
  <a href="#what-it-is">What it is</a> · <a href="#why">Why</a> · <a href="#desktop">Desktop</a> · <a href="#mobile">Mobile</a> · <a href="#answers">Anatomy of an answer</a> · <a href="#streaming">Streaming</a> · <a href="#keys">Keys</a> · <a href="#limits">Limits</a> · <a href="#faq">FAQ</a>
</p>

---

<div align="center">

### Two questions, answered properly

`how do I call it` · `how do I stream it` · `and nothing else`

</div>

## What it is

Helio is our own assistant. It is built and maintained by the team that writes the documentation it reads, and it ships as part of the site: in the corner of the docs, the dashboard and the blog.

It answers the two things people actually get stuck on: making an RPC call, and keeping a subscription alive. It is not a general chatbot, and it does not pretend to be one.

<img src="https://i.imgur.com/ars1OSc.png" alt="Helio declining an off-topic question and offering its two topics" width="820">

Every answer is grounded in the documentation index behind the site. If a page does not exist, the answer says so instead of inventing one.

## Why

Because the two most expensive mistakes on Solana are both small: a malformed request body and a socket nobody reconnects. Both are cheap to explain and expensive to debug, and both were being answered by strangers in group chats.

Helio is the answer written down once, by the people who maintain the endpoint, with a reference to the page so you can check it. When the docs change, the index changes with them in the same deploy. That is the whole trick, and it is why a stale answer here is a bug rather than a fact of life.

## Start

Helio opens from the mark in the bottom-right corner of any page.

- Click the mark
- Or press Cmd+K on macOS, Ctrl+K elsewhere
- Or take one of the two suggested actions in an empty chat

No account, no install, no key to ask. A key is only needed when you want to run the call yourself.

## Desktop

### Empty state

Two lines, both of them doors. Nothing else competes for the cursor.

<img src="https://i.imgur.com/n9Gj1sT.png" alt="Empty Helio chat with two suggested actions" width="820">

### Typing

The send button turns orange the moment there is text, so the state is never ambiguous.

<img src="https://i.imgur.com/nrOGTPg.png" alt="Composing a question, send button active" width="820">

### Analyzing

While it works, the header says so. No fake streaming, no progress bar pretending to know how far along it is.

<img src="https://i.imgur.com/AHR56Be.png" alt="Helio analyzing the question" width="820">

### An answer

Method, request body in a copyable block, reference link. The body is formatted and complete, with no ellipsis in the middle of the JSON.

<img src="https://i.imgur.com/Sg6uD1c.png" alt="Answer with getSlot and a formatted request body" width="820">

### Copy

One press, one confirmation. The block is the same bytes that will hit the wire.

<img src="https://i.imgur.com/3oNgb7b.png" alt="Request body after pressing Copy" width="820">

### Streaming

Same shape, different topic: the transport, the subscription call, and what to do when the socket drops.

<img src="https://i.imgur.com/WRI1X4Q.png" alt="Answer recommending accountSubscribe over polling" width="820">

### Done

When you confirm the result, the mark changes. It is the only celebration in the product.

<img src="https://i.imgur.com/2Qtqf4n.png" alt="Confirmed result, Helio in a done pose" width="820">

## Mobile

The same conversation, laid out for a phone. The composer sits directly under the last message, with no floating gap to scroll past and no width clipping on code.

<div align="center">

<img src="https://i.imgur.com/vJcvIpb.png" alt="Empty chat on mobile" width="300">
<img src="https://i.imgur.com/a9yVSxu.png" alt="RPC answer on mobile with an intact JSON block" width="300">
<img src="https://i.imgur.com/W9XXNlo.png" alt="Streaming conversation on mobile" width="300">

</div>

## Answers

Every answer is assembled from the same five parts, in the same order:

1. **The call.** Method name, transport, and whether it is a subscription.
2. **The body.** Complete JSON, formatted, copyable. Parameters are annotated the first time they appear.
3. **The reference.** A direct link to the method page, always last, never inline.
4. **The caveat.** The thing that bites people: rate limits, commitment levels, socket lifetime.
5. **The next step.** One sentence on what to do with the result.

If a part cannot be filled from the docs, it is left out rather than guessed.

## Streaming

Helio prefers subscriptions to polling and says why. For account updates that means `accountSubscribe`, not a `getAccountInfo` loop.

For reconnect it gives the shape of the fix, not a snippet to paste blind:

- subscribe with a request id and keep it
- detect close, not just error
- exponential backoff with jitter, capped
- re-subscribe on the same id
- dedupe by slot, not by signature

The full transport guide is linked at the end of the answer.

## Keys

Helio never stores a key. It asks for the endpoint URL, and if the URL carries a key it warns about where that key becomes visible.

- mainnet URL with a key: the key is in the URL, treat it as public
- client-side code: proxy through your own server
- the "Protect your keys" page is linked whenever a browser call is suggested

## Limits

| Limit | Behaviour |
| :--- | :--- |
| Off-topic question | says so, offers the two topics |
| No page for the method | says it is not in the index, links the closest match |
| Ambiguous question | asks one clarifying question, not three |
| Answer longer than a screen | collapses the body, keeps the call and the reference |
| No key available | gives the body and the curl form, skips the run button |

## Status

| Area | State |
| :--- | :--- |
| RPC method answers | shipping |
| Request body and copy | shipping |
| Reference links | shipping |
| Streaming guidance | shipping |
| Mobile layout | shipping |
| Run against your own key | beta |
| Saved conversations | planned |

## Built by

Helius Labs. The docs index, the method pages and Helio ship from the same repository and the same deploy.

## FAQ

**Is it free?**
Asking is free. Running a call uses your own key and your own quota.

**Does it write to chain?**
No. Read methods and subscriptions only.

**Where do the answers come from?**
The documentation index. If a page does not exist, the answer says so.

**Why only two topics?**
Because those are the two where a wrong answer costs real debugging time.

**Can it see my endpoint?**
Only the URL you paste into the chat. Nothing is persisted server-side.

**Does it work on mobile?**
Yes, and the layout is built for it rather than shrunk into it.

**Is this the same as the models in the API?**
No. Helio is a surface on the site; the API is separate and documented on its own pages.

<div align="center">

<sub>Helius Labs · Helio is part of the docs surface · feedback goes to the docs repository</sub>

</div>