<img src="assets/rea-banner.png" alt="REA Cases — AI + Reverse Engineering" width="1280">

# Awesome REA Cases

**English (default)** | [简体中文](README.zh-CN.md)

### Explore software and hardware with AI.

A curated collection of **reverse-engineering projects, experiments, and ideas**: revive old devices, rebuild apps, preserve games, and understand hidden behavior.

# 1164 cases & projects

**Latest case update:** October 29, 2026, 00:13 · **Last maintained:** October 29, 2026, 00:13 · Beijing time (UTC+8). Counts as of this maintenance.

Updates **6× daily** · [Full index](INDEX.en.md) · [Browse categories](#browse-by-category)

Covers [REA](https://github.com/morluto/rea) and other AI-assisted work. REA connects coding agents to local reverse-engineering tools through CLI and MCP.

*Based on author and project reports; not independently reproduced here. Evidence and project status are recorded in each case.*

![Cumulative case collection growth, by day](assets/case-growth.en.svg)

## Recent picks

**10 worth reading** for device interoperability, game preservation and useful replacements. Look for what was actually compared: binaries, old quirks, or even a speaker's lights and sound. Dates below are source or author-update dates, not collection dates.

1. **[Plustek scanner & ThinkPad camera](cases/en/schaller-opticfilm-thinkpad-linux.md)** · `2026-10-15` — Use Windows reference behavior to improve Linux drivers. Published measurements also disclose low-light and exposure defects. `In progress`
2. **[Where NIST curve seeds came from](cases/en/nist-ecdsa-origin-claude-report.md)** · `2026-10-16` — Anthropic reports Claude traced public parameters to **lrand48 and timestamps**, publishing code and unresolved questions. **Not an ECDSA break**; not independently recomputed here. `Research report`
3. **[LG UltraFine: repair the updater, not the firmware](cases/en/lg-ultrafine-codex-updater-patch.md)** · `2026-10-19` — Codex-assisted diagnosis and a **public, exact-build memory patch**; the author reports a scaler update reaching **100% with CRC passing**. Credits an earlier bug report; one Apple Silicon setup, not independently flashed here. `Author-tested patch`
4. **[Brother: scan straight to your NAS](cases/en/brother-scan-button-claude-rea-server.md)** · `2026-10-18` — Replace the PC button app with a **public Claude/REA-assisted Go service for SMB, FTP, S3 and local storage**, building on prior protocol work. A server is still required; only MFC-L2800DW firmware 1.32 is project-tested. `Public implementation`
5. **[Claude writes proofs; Rocq checks the binaries](cases/en/anthropic-theorem-claude-binary-formal-verification.md)** · `2026-10-22` — Anthropic/Theorem report machine-code no-crash proofs for **239 entry points across 123 libraries**. Single-threaded static RISC-V/Linux, inputs below 64MB; **not bug-free whole libraries**, and the checker was not independently rerun here. `Analysis test`
6. **[PlainMount: write to an old NTFS drive on a Mac](cases/en/laplaced-plainmount-rea-ntfstool-macos.md)** · `2026-10-28` — Laplaced reports **REA inspection of NTFSTool**, then a native app using existing NTFS components; reading, writing and reconnection tested on one old drive. Public source, Apple Silicon/macOS 14+; **mixed backend licenses, no Apple notarization**, no independent disk test here. `In progress`
7. **[Instance: preserve GameMaker's quirks, not just its features](cases/en/instance-gamemaker81-claude-blackbox-rust.md)** · `2026-10-28` — A report credits **Claude-assisted, black-box-spec-driven Rust reconstruction** of the 8.1 editor and runtime. Public code and browser entry include old event, RNG and audio behavior; **three weeks, not just a morning**, according to the report. No full-parity or legal-compliance guarantee; not run here. `In progress`
8. **[Civilization: rebuild the 1991 DOS executable](cases/en/civilization-dos47405-ai-reconstruction-report.md)** · `2026-10-21` — Steve Melia's AI-assisted C/assembly reconstruction has **public code and successful exact-commit hash-checking CI**. A checked **four-byte startup correction** is part of the build, not a remaining mismatch. Inferred names, prior OpenCiv1 work; not original source or an independently rerun build here. `In progress`
9. **[PicasaPy: keep a local photo workflow alive](cases/en/picasapy-ghidra-claude-codex-photo-manager.md)** · `2026-10-28` (Beijing time) — Virág Attila's **Ghidra/Claude/Codex-assisted Python/Qt rewrite** has public research specifications and successful exact-commit CI. Shared **.picasa.ini** files are not conflict-safe synchronization; project documents separate static coverage from click tests. Full parity not established; not run here. `In progress`
10. **[Klipsch Lumina: let the agent see and hear the test](cases/en/klipsch-promedia-lumina-ai-ble-mac-sensor-loop.md)** · `2026-10-28` — Pawan Deshpande reports **BLE sniffing and mobile-binary research** for a Mac controller, then webcam/microphone feedback to check LEDs and audio. Includes a claimed screen-color lighting mode; source entry and physical results not independently checked. `Author report`

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
| [Games & preservation](categories/en/games.md) | **245** |
| [Hardware & interoperability](categories/en/hardware.md) | **328** |
| [Applications & clients](categories/en/apps.md) | **477** |
| [Algorithms & feature recovery](categories/en/algorithms.md) | **114** |

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
