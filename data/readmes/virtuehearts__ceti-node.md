<p align="center">
  <img src="docs/images/banner.png" alt="CETI: Uncensored Node — pixel banner by darknet.ca labs" width="640">
</p>

<p align="center">
  <a href="https://github.com/virtuehearts/ceti-node/blob/main/README.md"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://github.com/virtuehearts/ceti-node/releases"><img src="https://img.shields.io/badge/version-0.0.1--beta15-17cfff" alt="Version 0.0.1-beta15"></a>
  <a href="https://github.com/virtuehearts/ceti-node/stargazers"><img src="https://img.shields.io/github/stars/virtuehearts/ceti-node.svg?style=social&label=Star" alt="GitHub stars"></a>
  <a href="https://ceti.darknet.ca"><img src="https://img.shields.io/badge/Visit-ceti.darknet.ca-17cfff" alt="Visit ceti.darknet.ca"></a>
</p>

<p align="center">
  <a href="https://x.com/virtue_hearts"><img src="https://img.shields.io/badge/Follow%20on%20X-000000?style=for-the-badge&logo=x&logoColor=white" alt="Follow on X"></a>
</p>

# CETI: Uncensored Node

**Sovereign AI that never leaves your building.**

CETI is a local brain that answers from what it knows, instead of a model guessing in the moment. The model is the night shift — it researches, distills, and promotes while you sleep. Serving is pure retrieval. Teach it once and the next ask costs nothing, because the answer already lives on the box. No tokens. No per-question bill. No account. That is the design goal: **zero tokens at serve time**.

This is not a chatbot you rent by the token. It is a BIOS for AI: a small layer that asks every local store at once — AIML cassettes, the fact store, vector memory, your library, signed datasets — and compiles the answer from what they hold. The model is a peripheral, not the brain.

And the brain is not alone. Every node is a peer: it holds its own sovereign knowledge, answers its own questions, and shares signed facts with the nodes it trusts. Knowledge travels node to node, verified by signature, never by a platform. The network is the sum of its nodes, not a server in someone else's building. It feels like Gopher — retro but super useful: every peer is a public key.

[![Download CETI Uncensored Node beta15](docs/images/download-beta15.svg)](https://github.com/virtuehearts/ceti-node/releases)

**Version:** 0.0.1-beta15 — now with the rebuilt routing rack (up to 3 provider slots, local as a slot like any other, Anthropic support), Mac in Dark mode as the default agent theme, and a rewritten README. Mya the agent is built in, the Community chain runs on Bitcoin and regula_core, and self-discovery runs over Tor onion routing. No account, no install to babysit, no credentials in the download: every API key ships unset, and you add your own in the agent's routing rack.

## Quick start

Run it in 2 minutes. No installs to babysit, no accounts to create.

```bash
# 1. Install the newest Python from https://www.python.org/downloads/
# 2. Download the latest beta (~81 MB) from the releases page and unzip it:
#    https://github.com/virtuehearts/ceti-node/releases
# 3. Run the autorun — it checks the setup, downloads the models,
#    starts the servers, and opens the web UI.
autorun.bat    # Windows
./autorun.sh   # Linux
# 4. Open http://localhost:8900 in your browser.
```

Then join the network: in the Node tab, set a node name and press **Announce**. To run the agent too, run `agent.bat` (Windows) or `agent.sh` — her console opens on http://127.0.0.1:8899.

Primary testing is done on **Windows, with a 6 GB RTX card** (an RTX 3060 laptop) — chat on VRAM, embeddings on CPU/RAM by default so they don't steal VRAM. A model needs disk space and RAM/VRAM to run; GPU memory figures in the Models tab are labelled estimates (file size × 1.2), not measurements.

## What you get

| | |
|---|---|
| **Chat** | Everyday talk with a local uncensored model, or a cloud model when you pick one. Your keys live in your browser only; the server never writes them to disk. |
| **Mya, the agent** | A full tool agent on your node: terminal, file browser, editor, music player, routing rack, themes, and a signed ledger of everything she does. |
| **CETI sessions** | Answers from the CETI ladder: facts, AIML, and local knowledge first, cloud only as a suggestion. Every answer shows its tier, its reasoning, and its signed ledger entry. |
| **Community** | A shared chain on Bitcoin and regula_core: posts, replies, and likes with gas paid in sats, media stored on chain, and a display-only Bitcoin wallet in the Hub. |
| **Discovery network** | A second Bitcoin-style network for self-discovery, genesis BLOCK 4, over Tor: peers are `.onion` addresses, no IPs exposed, and NAT is no longer a barrier. |
| **Node network** | Gopher, not a platform. Announce your node and it lists immediately. No approval, no verified flag, no network sysop. Allow, deny, and mute live per node, and every answer is signed by the node's own key. |
| **Lobby** | A public IRC-like room for listed nodes, plus private sysop chat and file transfers between nodes. |
| **Research tab** | A local agent with a heartbeat. It compiles what CETI already knows, reads source pages as text, distills what it learns, and proposes it for your approval. Approvals are what move the ladder — and the benchmark score. |
| **Models tab** | The model hub. Browse Hugging Face collections (default: `chwoo/uncensored-models`) and download GGUFs into `models/`. Drop your preferred model (`.gguf`) into `models/` yourself and it appears in the System tab's local model list — pick it there to load it. |
| **Code workspaces** | Every chat session is a code workspace with an agent that runs tools, like Antigravity. Each session gets its own folder and a Code pane: an agent task box, a model pick, a workspace file editor, and a live step log. File tools are always on; shell, network, git, and SSH are each behind a per-session switch, off by default. |
| **SSH terminal** | A terminal in the workspace. It defaults to **chat.hf.co**, where you can use free models by pairing your Hugging Face account. |
| **Voice (TTS)** | The Mya voice bridge ships inside the release and starts with no setup (it downloads ffmpeg on first run if it needs it). A voice job to your own node voices on the local bridge directly — no mailbox, no poller. Chat voice works with the poller down. |
| **Memory** | A node view of vector memory, with provenance on every reply: which memories were used, and what drew on them. |

## The Hub — your node, on a laptop

The Hub is the node's program interface — the old CETI look, the one that has been there since the early betas. These are laptop-size screenshots, taken live, showing it in real use. Nothing here is a mockup.

Chat — a real session, a real answer, with the model named at the top and the memory trace under it:

![Hub — Chat, on a laptop](docs/images/hub-chat-laptop.png)

Node — the Lobby, the peer list, and the Community menu. Two nodes are listed and present right now. Your node announces itself here and lists immediately — no approval, no verified flag:

![Hub — Node and Lobby, on a laptop](docs/images/hub-node-laptop.png)

System — the servers, the voice, and the machine. Chat, embeddings, and TTS are all running on this box; the node poller is down. The right column is the honest state of the machine: no GPU detected, so this box runs in RAM/CPU mode, and vector memory holds 153 entries:

![Hub — System and servers, on a laptop](docs/images/hub-system-laptop.png)

**Runs on Linux, Mac, and PC.** The Hub and the agent are Python, standard library only — no heavy framework, no build step, no vendor lock-in. Download the zip, run the autorun, and it starts on whatever you have. It is open source under the MIT license, and the code is the release.

**Voice is built in.** The TTS server (PocketTTS) runs on the node, with the Mya-03 voice as the default. Chat answers carry a voice waveform and a GENERATE VOICE button — the voice is generated on your own machine, from the local bridge, not from a cloud voice service.

**Peer to peer is built in.** The Node tab is the network: Lobby, Peers, Private chat, Files, Jobs, Transfers, Serving, Poller, and Community. Nodes announce, list, and talk node to node — signed by their own keys, over Tor onion routing, with no centre.

## Memory — CETI chat runs on vector memory

CETI chat does not guess from a model alone. It answers from vector memory — your own store of what the node has learned, embedded with EmbeddingGemma (768 dimensions) and searched on every question. The laptop node is the demo: everything below is running on one machine, and the memory is the machine's own.

![Memories are nodes — animated diagram](docs/images/gif-memory.gif)

- **Memories are nodes.** Each memory is a node in a graph: a fact, an answer, a file, a session. A question gathers the memories it touches, and the answer is built from them — not retrieved as a single block, but composed from the pieces that match.
- **Every tier answers at once.** Facts, AIML cassettes, vector memory, your library, signed datasets — the ladder asks every local store at once and hands all the hits to the local model, which constructs the answer from them. That is all-layers-reason: the model is the composer, the stores are the score.
- **Provenance on every reply.** Each answer shows its trace — how many memories were used, and which ones. The System tab counts them live (153 entries in the screenshot above), and the chat shows the trace under every answer. Nothing is an uncited guess.
- **The ledger is the filesystem.** Every write is a signed, hash-chained ledger event, so what the node learned and when is checkable. Memory that is not signed does not ship.

## Meet Mya — the agent

Mya is the agent that lives on your node. She is not a chatbot window: she is a small operating system in your browser (JERO.OS.001), a terminal that answers with tools. Ask her a question and she works it out — shell, files, fetch, browse, memory, build, calc, time, node — and shows her work. She can write a file, build a small program, look something up, and remember what she learned, all on your machine.

She runs on free cloud models first (OpenRouter, then Nvidia, then Hugging Face) and falls back to the local uncensored model on your own hardware. Her memory is a local vector store plus a signed ledger — every write she makes is a signed, hash-chained ledger event, so what she did is checkable. She creates her own identity on first run, so every laptop is its own node.

**Routing is a rack.** The status bar under the terminal header shows her routing at a glance — which backend is first, which model is active. Tap it and the routing rack opens: one list of up to 3 provider slots, local included as a slot like any other, and each provider is its own rack unit in the console's own style — a unit bar with its name, a [+] to expand its settings (name, model, API key, plus its usage and failure log), and up/down to reorder it. A + adds a provider to the list. **No credentials ship:** every API key is unset in the release — you add your own in the rack, which saves them to `agent/data/.api-keys.env` (0600) on your own machine. When she cannot reach a model, the bar turns red, Star Trek red-alert style, with the error in it — she fails loudly, never silently.

**Local first, if you want it.** Put local in the first slot and she answers from the uncensored model on your own hardware — the status bar reads `routing: local`, and every answer tells you which backend answered it (`Mya [agent · local]`). If the local model is down she falls back to cloud and says so honestly, instead of failing silently.

**Add your own providers.** The rack has an add-endpoint form: any API that speaks OpenAI chat completions works — OpenAI itself (base `https://api.openai.com/v1`), or another host. Anthropic / Claude works too, through a real Messages adapter. Gemini, AMD, and custom endpoints join the same way: paste the base URL, a label, the models, and the key, and it joins the routing list like any built-in provider.

The terminal — ask anything, watch her work:

![Mya agent — Terminal](docs/images/agent-terminal.png)

The music player — tracker modules play live in your browser, MIDI through a SoundFont, plus your MP3s. It ships with two tracker classics (RJC's Forgotten Past, Necros's Point of Departure) and the Ode to Joy MIDI sample — drop your own music in the music folder and it shows up here too:

![Mya agent — Music player](docs/images/agent-music.png)

The file browser — your workspace, your downloads, your music library, all in one place:

![Mya agent — Files](docs/images/agent-files.png)

The editor — open any text file from Files and edit it right here, VI flavour, with Save and Close as buttons so everything works by tap:

![Mya agent — Editor](docs/images/agent-editor.png)

And she comes in six themes — Green, Amber, Cyan, Amiga, Mac, PC — each in Dark or Light. The default is **Mac in Dark mode**. Themes are for the agent console only — the Hub chat keeps its own old CETI look. Here is the terminal in Amber:

![Mya agent — Amber theme](docs/images/agent-amber.png)

Run her with `agent.bat` (Windows) or `agent.sh` (Linux). On first run she copies `config.example.json` to `config.json` and starts the console on http://127.0.0.1:8899.

## Community — a decentralised social feed on Bitcoin and regula_core

**Community** is a shared chain where nodes post, reply, and rate each other — a decentralised social feed, built on Bitcoin and regula_core.

Your personal regula_core ledger stays untouched: Community is a **separate single shared chain**, rooted at the BLOCK 4 anchor — the shared block 0 every node agrees on. A post, a reply, or a like is a block on that chain, and a block is valid only when its payment, its signature, and its hash chain all check out. Consensus is the payment: every action costs gas, paid in Bitcoin to the Treasury. The economics run on Bitcoin testnet for now; mainnet is the production config.

| Action | Gas |
|---|---|
| Post | 100 sats |
| Reply | 50 sats |
| Like / dislike | 20 sats |

- **Posts are short and plain.** A post is at most 366 characters of plaintext, URLs allowed. Replies thread under the post they answer; likes and dislikes are counts on the card, no text, no media.
- **Media lives on chain.** Images and video (JPG, GIF, MP4, up to 5 MB) are stored as base64 **inside the block** — every node stores the full bytes, so a post carries its own image with it, and the image is covered by the block's signature.
- **The feed is a short-post feed.** Media first, text under it, like and dislike counts always visible, comments hidden until a post is clicked. It loads the last 16 top-level posts, each with its full thread, and pages back from there — a 30,000-block chain does not tax a node on open.
- **A small wallet, display only.** The Hub shows your node's Bitcoin address and balance (testnet and mainnet) in the Identity page. It can receive and display — it cannot send, and it never signs. The private key is never used.

No mining, no voting, no platform in the middle. A node joins from today's blocks onward, verifies what it pulls, and follows forward.

## Discovery network & onion routing

Finding each other is the hard part of a peer network, so CETI runs a **second Bitcoin-style network for self-discovery** — the same Bitcoin P2P wire protocol (version, verack, getaddr, addr, ping, pong), but a different network, with its own genesis: BLOCK 4, the same anchor the Community chain shares. Every peer on it is a CETI node by definition — no scanning thousands of random Bitcoin addresses to find one of us.

| | |
|---|---|
| Genesis | BLOCK 4 (`8ec446a0…`) |
| Magic | `0x8EC446A0` |
| Port | 19846 |
| Seed | `.onion` address (Tor) |

And it runs over **Tor onion routing**, so no IP is ever exposed:

- The seed node has a `.onion` address, and peers connect to it through Tor. The peer list carries `.onion` addresses only — not in the connection, and not in the list.
- Onion routing also fixes NAT: a laptop behind a router cannot accept a direct connection, but it **can** be reached through its `.onion` address, so the network is truly peer to peer, not hub-and-spoke around one box.
- The discovery client is disabled by default (loads stopped) — it only runs when you turn it on. The seed listener is a separate service.
- The discovery network carries no money. The economics stay on real Bitcoin, testnet for now.

A node joins, handshakes with the genesis hash, asks for peers, and gets CETI nodes back — anonymously.

## The Mya node

![Mya — the node that anchors the network](docs/images/mya-node.jpg)

Every node that runs the agent is a Mya node — a peer that can think, speak, and make images for the nodes that trust it. The reference node, **mya-node**, is the one that anchors the network: it runs the agent, the Hub, and the list host, and it is the sysop for the nodes it allow-lists.

A Mya node is identified by its own keypair — a node id and a fingerprint — never by an account or a username. mya-node's fingerprint is `NODE-CFF8-E94E-A817-68A2`, and it lists its capabilities as text, voice, and image. It announces itself, serves only the nodes on its allow-list, and every answer it gives is signed by its own key. Every write it makes lands in its own signed ledger, so what it did is checkable.

When you run this release, your laptop becomes a Mya node of its own: it creates its own identity on first run, announces itself, and can serve the nodes that allow-list it. You are not joining someone else's network — you are a peer in it, with your own keys and your own ledger.

## How the network works — node to node

![Peer to peer: no centre, no server, just nodes](docs/images/p2p-mesh.svg)

There is no centre. There is no server that your messages pass through. Your node talks straight to the nodes it trusts, and every message is signed by the sender's own key — verified by signature, never by a platform.

- **Announce.** In the Node tab, set a node name and press **Announce** — your node lists immediately with the capabilities it claims. No approval, no verified flag, no network sysop.
- **The list host only lists.** It keeps the roster of who is alive (a node drops off if it is not seen for 15 minutes) and nothing else. It never sees your messages, your files, or your keys.
- **Allow-list, per node.** To use another node's text, voice, or image, send your pubkey to that node's operator (Lobby, sysop chat, or admin@darknet.ca) and ask to be allow-listed. A job only runs if the serving node has your pubkey on its allow-list. Allow, deny, and mute live per node — your node, your rules.
- **Lobby.** A public IRC-like room for listed nodes, plus private sysop chat and file transfers between nodes.
- **Signed everything.** Every answer is signed by the node's own key, and every write lands in the node's own signed ledger (`regula_core: OK`, `block ledger: OK` in the footer). Shared files publish as signed Merkle bundles. A failed publish records no ledger event: rejected items never enter signed history. Verification uses only the keys inside the package — nothing is sent anywhere else to check it.

CETI on many boxes is a networked knowledge infrastructure with no centre — meant to rival WikiLeaks and Wikipedia, and built to not need them.

## Sponsors & beta testers wanted

We are **actively looking for sponsors and beta testers**. CETI is built in the open by a small lab, and the next stage — a network of real nodes, tested on real hardware, in real conditions — needs people and machines, not just code.

**Sponsors.** If you can fund the work, lend hardware, or lend cloud, we want to hear from you. Sponsorship keeps nodes running around the clock, pays for the big jobs that do not fit a laptop (large image and video renders, model tests, builds), and buys the test coverage a sovereign network needs before it can be trusted. Money, hardware, VPSs, cloud machines, and compute credits are all welcome — the full list, what each one buys, and the hardware wishlist are at **[ceti.darknet.ca/donate.html](https://ceti.darknet.ca/donate.html)**. Every sponsor gets listed and thanked.

**Beta testers.** Run the release on your own machine, use it every day, and tell us what breaks. We need testers on Windows and Linux, on laptops and desktops, with and without a GPU — especially people willing to run a node around the clock and report what they see. No resume, no application form: download the beta, run it, and email **admin@darknet.ca** with what you found, what you run, and what you want to serve. If you are accepted to the team, you get a free darknet.ca email address — yourname@darknet.ca, yours to keep while you are on the team.

**Hardware, VPSs & cloud machines for testing.** We are specifically looking for test machines: working desktop GPUs (8 GB VRAM minimum, 12 GB / 16 GB ideal), a spare box, a shelf in a rack, a VPS, or a corner of a server that can run a node around the clock. The detailed wishlist is below, under [Hardware & cloud contributors wanted](#hardware--cloud-contributors-wanted).

## Join the team

We are building this in the open, and we want you in it. If you want to help — code, testing, docs, design, running a node, spreading the word — email **admin@darknet.ca** and tell us what you want to do. **If you are accepted to the team, you get a free darknet.ca email address** — yourname@darknet.ca, yours to keep while you are on the team.

No resume needed. Show us something you made, a node you run, a bug you found, or just tell us why you care about sovereign AI. We answer every email.

## Why hardware inference matters

The local model is the honest bottleneck. On this box there is no GPU — the System screenshot above reads "no GPU detected — RAM/CPU mode" — so the chat model runs on the CPU, and a single answer can take tens of seconds. The 1.7B local model takes about 26–28 seconds a question on CPU, and a bigger model on CPU is slower still. That is usable, and it is how the node stays sovereign, but it is not fast.

A GPU changes that completely. Chat moves to VRAM, embeddings stay on CPU/RAM so they do not steal VRAM, and answers come back in seconds instead of tens of seconds. The node stays local — the model still never leaves your building — but it becomes fast enough to feel like a real assistant instead of a batch job.

That is the hardware the project needs most: a working desktop GPU (8 GB VRAM minimum, 12–16 GB ideal) in a machine that can run a node around the clock. One card turns a slow-but-sovereign node into a fast-and-sovereign one. The full wishlist is in the next section.

## Hardware & cloud contributors wanted

We are **actively looking for hardware and cloud contributors** to keep uncensored nodes running and to test the network on real machines. If you can donate any of these, email **admin@darknet.ca** — tell us what you run and what you want to serve, and we will get you listed and set up:

- **GPUs** — working desktop cards, 8 GB VRAM minimum (12 GB / 16 GB ideal). RTX 3060 12 GB, 3070, 3080, 4060, 4060 Ti 16 GB, 4070, 4080, 4090, GTX 1080 Ti / 2070 / 2080, AMD RX 6700 XT / 6800 / 6800 XT / 6900 XT. No Jetson, no GT 710 / 1030, no old Quadro, no mining-only cards.
- **Machines & hosting** — a spare box, a shelf in a rack, a VPS, or a corner of a server that can run a node around the clock. VPSs and cloud machines for testing are especially welcome: a node that stays up is how the network gets proven.
- **Compute credits** — GPU cloud credits (or a cloud account) for the big jobs that do not fit a 6 GB laptop: large image and video renders, model tests, builds.
- **Money & time** — money, hardware, compute credits, and time are all welcome. The full list, what each one buys, and the hardware wishlist are at **https://ceti.darknet.ca/donate.html**. GitHub Sponsors is opening soon (onboarding in progress — see the donate page); until the Sponsor button is live, email admin@darknet.ca.

Every contributor gets listed and thanked. Hardware donors get their node set up and announced with them.

## Your machine, your data, your mind

- **Data sovereignty.** Your data stays on your machine, in stores you can read, sign, and carry. Nothing leaves the building unless it has to — personal data is stripped before anything touches the cloud, and the cloud only ever sees the gap, never your whole store.
- **Intelligence sovereignty.** Your intelligence stays yours. Your personality, your memory, your judgement — they live in your local stores, not in someone else's model. No one else's model shapes your answers.

That is what sovereign knowledge means: the copy on your iron is yours, the provenance is checkable, and nobody can rewrite it, delist it, or bill you per question for it.

The ledger is the filesystem. Every write a node makes is a signed, hash-chained ledger event — sessions, code, stories, samples, model downloads. Every CETI answer, session save, and share is appended to the node's own signed ledger. Shared files publish as signed Merkle bundles, and a failed publish records no ledger event: rejected items never enter signed history.

## A note on CETI

CETI is the front end to sovereign knowledge: own the machine, own the data, own the mind. It is a BIOS for AI — the small layer that boots a machine into a sovereign peer-to-peer compute node, asks every local store at once, and compiles the answer from what they hold. The model is a peripheral, not the brain.

The full CETI BIOS for general intelligence is still ahead. This release does not use CETI AIML technology yet. CETI technology was used in developing this release, and the node network is the platform the new CETI is built on. The Brain pane shows CETI components as a read-only view; the packaged release runs the node network, the ledger, and the model serving described above.

## Find us

CETI is built by **darknet.ca labs** — the lab behind darknet.ca, running since 2002. The lab's home is **[darknet.ca](https://darknet.ca)** (and **[labs.darknet.ca](https://labs.darknet.ca)**), and CETI lives at **[ceti.darknet.ca](https://ceti.darknet.ca)** — the CETI page, the [donate page](https://ceti.darknet.ca/donate.html), and the [infrastructure page](https://ceti.darknet.ca/infrastructure).

- **Web:** [darknet.ca](https://darknet.ca) · [labs.darknet.ca](https://labs.darknet.ca) · [ceti.darknet.ca](https://ceti.darknet.ca)
- **X:** the original handle is [@darknet_ca](https://x.com/darknet_ca) (since 2008); the new one is [@virtue_hearts](https://x.com/virtue_hearts)
- **Email:** admin@darknet.ca — for joining the team, sponsoring, donating hardware or cloud, beta testing, or anything else
- **Offline copy:** this README, with images baked in, ships at `info/ceti-readme-baked.html` — open it anywhere, no network needed.

![CETI: Uncensored Node logo](docs/images/logo.svg)

Own the machine, own the data, own the mind. Sovereign AI, from Canada, on your own iron. Welcome to the network.
