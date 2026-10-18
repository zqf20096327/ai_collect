<img src="assets/rea-banner.png" alt="REA Cases — AI + Reverse Engineering" width="1280">

# Awesome REA Cases

**English (default)** | [简体中文](README.zh-CN.md)

### Explore software and hardware with AI.

A curated collection of **reverse-engineering projects, experiments, and ideas**: revive old devices, rebuild apps, preserve games, and understand hidden behavior.

# 476 cases & projects

**Latest case update / maintenance:** October 19, 2026, 01:19 · Beijing time (UTC+8). Counts as of this update.

Updates **6× daily** · [Full index](INDEX.en.md) · [Browse categories](#browse-by-category)

Covers [REA](https://github.com/morluto/rea) and other AI-assisted work. REA connects coding agents to local reverse-engineering tools through CLI and MCP.

*Based on author and project reports; not independently reproduced here. Evidence and project status are recorded in each case.*

![Cumulative case collection growth, by day](assets/case-growth.en.svg)

## Recent picks

**10 worth reading**, chosen for concrete uses, inspectable evidence and dated engagement—not an automated ranking. Dates refer to featured sources or author updates, not collection dates.

1. **[Plustek scanner & ThinkPad camera](cases/en/schaller-opticfilm-thinkpad-linux.md)** · `2026-10-16` — Use Windows reference behavior to improve Linux drivers. Published measurements also disclose low-light and exposure defects. `In progress`
2. **[Where NIST curve seeds came from](cases/en/nist-ecdsa-origin-claude-report.md)** · `2026-10-16` — Anthropic reports Claude traced public parameters to **lrand48 and timestamps**, publishing code and unresolved questions. **Not an ECDSA break**; not independently recomputed here. `Research report`
3. **[Brother: scan straight to your NAS](cases/en/brother-scan-button-claude-rea-server.md)** · `2026-10-18` — Replace the PC button app with a **public Claude/REA-assisted Go service for SMB, FTP, S3 and local storage**, building on prior protocol work. A server is still required; only MFC-L2800DW firmware 1.32 is project-tested. `Public implementation`
4. **[LeanREA: direct CLI vs MCP](cases/en/leanrea-cli-skill-benchmark.md)** · `2026-10-17` — Trace Notion features, inspect a native lock and identify Go dependencies. The public **36-run comparison** reports lower time and cost, but scores are **74/75 vs 75/75**, not identical accuracy. One model and machine; not independently rerun. `Analysis test`
5. **[Frontkick vs Rikugan](cases/en/synacktiv-frontkick-rikugan-crebench.md)** · `2026-10-13` — Recover algorithms and keys from AES/ChaCha20 binaries. Synacktiv publishes per-run results, but **unequal library prompts confound the comparison**—not proof that CodeAct beats tool calling. Two tasks only; not independently rerun. `Analysis test`
6. **[Open Scrantic: Johnny Castaway returns](cases/en/johnny-castaway-rust-rea.md)** · `2026-10-17` — REA and Claude Code help recover a Windows 3.1 screensaver engine in Rust for three platforms. **Public code and successful project CI**; original assets required, known-build limits and deliberate behavior differences remain. `In progress`
7. **[NJFE: an ear camera on your PC](cases/en/njfe-claude-ear-camera-usb.md)** · `2026-10-10` — Claude-assisted USB bridging turns a cheap Wi-Fi camera into an inspection scope, **building on prior otoscope protocol work**. One device tested by the project; camera Wi-Fi remains open. `Public implementation`
8. **[Gears of War 3](cases/en/gears3-ai-graphics-recompile.md)** · `2026-10-17` — AI-assisted Linux graphics work through **mechanical PowerPC-to-C++ translation, not recovered original source**. The reported 4K WIP still drops frames in combat. `In progress`
9. **[Sonic 3D Blast: recreate the compiler first](cases/en/sonic-3d-blast-saturn-opus-port.md)** · `2026-10-16` — **A native port from decompiled code, not static recompilation**, according to the author. Visual defects remain; November 20 is a release plan. `In progress`
10. **[A gzip predicate inside Claude's Bun build](cases/en/claude-bun-gzip-gemini-rea-test.md)** · `2026-10-18` — After unpacking, REA supplies evidence for a Gemini rewrite; the author reports **69,121 passing tests**. One function, no public test harness here—not whole-client decompilation or independent reproduction. `Self-test`

## Classic cases

- **[Universal Modder](cases/en/universal-modder.md)** — AI-assisted cross-game mods, including Minecraft content in GTA V.
- **[Firefighter](cases/en/firefighter-rust.md)** — Recover Pascal logic from a DOS binary, then rewrite it in Rust, according to the author.
- **[Modern Warfare 2](cases/en/mw2-decompilation.md)** — Author-reported multi-agent reconstruction; **83% function byte matches**, no public code or independent reproduction here.
- **[Smart toilet from the Mac menu bar](cases/en/smart-toilet.md)** — Author-reported Bluetooth research and home-device control.
- **[Apple TV remote on Linux](cases/en/siri-remote-linux.md)** — Bluetooth interoperability with a public implementation; REA use unconfirmed.
- **[LG PlxNative](cases/en/lg-plxnative.md)** — Native Plex client; user-selection time reportedly falls from **30 seconds to 3 seconds**.

## Browse by category

| Category | Entries |
| :--- | ---: |
| [Games & preservation](categories/en/games.md) | **106** |
| [Hardware & interoperability](categories/en/hardware.md) | **101** |
| [Applications & clients](categories/en/apps.md) | **223** |
| [Algorithms & feature recovery](categories/en/algorithms.md) | **46** |

[**View all cases →**](INDEX.en.md) · [Contribute (中文)](CONTRIBUTING.md) · [Maintenance (中文)](MAINTENANCE.md)

<details>
<summary><strong>Update & evidence notes</strong></summary>

- **Continuous resolved-material cutoff:** October 15, 2026, 16:00, Beijing time. Older unresolved sources can hold this cutoff back while newer entries are added; it is not a verification date for every project.
- Searches run six times daily with keyword and pagination limits; coverage is bounded, not exhaustive, and some linked evidence remains unresolved. Source dates, evidence boundaries, and engagement snapshots are recorded in case details.
- Full descriptions, sources, and language switching are available on every case page.

</details>

## Scope & license

**Unofficial collection.** Original summaries and public links only; no proprietary software, game assets, keys, or private material.

Original curation and code: **[MIT](LICENSE)**. Linked work retains its own rights; use legally obtained targets and check the relevant permissions.
