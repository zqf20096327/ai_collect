<img src="assets/rea-banner.png" alt="REA Cases — AI + Reverse Engineering" width="1280">

# Awesome REA Cases

**English (default)** | [简体中文](README.zh-CN.md)

### Explore software and hardware with AI.

A curated collection of **reverse-engineering projects, experiments, and ideas**: revive old devices, rebuild apps, preserve games, and understand hidden behavior.

# 980 cases & projects

**Latest case update:** October 27, 2026, 04:03 · **Last maintained:** October 27, 2026, 04:03 · Beijing time (UTC+8). Counts as of this maintenance.

Updates **6× daily** · [Full index](INDEX.en.md) · [Browse categories](#browse-by-category)

Covers [REA](https://github.com/morluto/rea) and other AI-assisted work. REA connects coding agents to local reverse-engineering tools through CLI and MCP.

*Based on author and project reports; not independently reproduced here. Evidence and project status are recorded in each case.*

![Cumulative case collection growth, by day](assets/case-growth.en.svg)

## Recent picks

**10 worth reading** for device interoperability, game preservation and hidden behavior. These picks favor public implementations, checkable comparisons and bounded tests. The full index also covers early firmware modifications and app rebuilds, including reported failures and unfinished attempts. Dates below are source or author-update dates, not collection dates.

1. **[Plustek scanner & ThinkPad camera](cases/en/schaller-opticfilm-thinkpad-linux.md)** · `2026-10-15` — Use Windows reference behavior to improve Linux drivers. Published measurements also disclose low-light and exposure defects. `In progress`
2. **[Where NIST curve seeds came from](cases/en/nist-ecdsa-origin-claude-report.md)** · `2026-10-16` — Anthropic reports Claude traced public parameters to **lrand48 and timestamps**, publishing code and unresolved questions. **Not an ECDSA break**; not independently recomputed here. `Research report`
3. **[LG UltraFine: repair the updater, not the firmware](cases/en/lg-ultrafine-codex-updater-patch.md)** · `2026-10-19` — Codex-assisted diagnosis and a **public, exact-build memory patch**; the author reports a scaler update reaching **100% with CRC passing**. Credits an earlier bug report; one Apple Silicon setup, not independently flashed here. `Author-tested patch`
4. **[Brother: scan straight to your NAS](cases/en/brother-scan-button-claude-rea-server.md)** · `2026-10-18` — Replace the PC button app with a **public Claude/REA-assisted Go service for SMB, FTP, S3 and local storage**, building on prior protocol work. A server is still required; only MFC-L2800DW firmware 1.32 is project-tested. `Public implementation`
5. **[Claude writes proofs; Rocq checks the binaries](cases/en/anthropic-theorem-claude-binary-formal-verification.md)** · `2026-10-22` — Anthropic/Theorem report machine-code no-crash proofs for **239 entry points across 123 libraries**. Single-threaded static RISC-V/Linux, inputs below 64MB; **not bug-free whole libraries**, and the checker was not independently rerun here. `Analysis test`
6. **[Ricoh GR: a small wireless viewfinder](cases/en/ricoh-gr-codex-sticks3-wireless-viewfinder-report.md)** · `2026-10-19` — Codex-assisted StickS3 firmware provides **Wi-Fi preview and generation-specific shutter control**. Public code and project-reported **93/93 host tests**; camera coverage varies. The hot shoe mounts the screen, not the image link. Not run here. `Unverified`
7. **[Ace Combat 04: from PS2 functions to native C++](cases/en/projectstonehenge-ace-combat04-ai-native-port.md)** · `2026-10-25` — ProjectStonehenge documents **Anthropic-assisted research and code**, using Ghidra/MCP and PCSX2 references. Configurable rendering up to a **360 FPS cap**, not a measured frame rate; game logic stays at 59.94 Hz. Windows, one disc revision, beta save interchange; not run here. `In progress`
8. **[Civilization: rebuild the 1991 DOS executable](cases/en/civilization-dos47405-ai-reconstruction-report.md)** · `2026-10-21` — Steve Melia's AI-assisted C/assembly reconstruction has **public code and successful exact-commit hash-checking CI**. A checked **four-byte startup correction** is part of the build, not a remaining mismatch. Inferred names, prior OpenCiv1 work; not original source or an independently rerun build here. `In progress`
9. **[BreezySRPG95: play old tactical RPGs with a modern client](cases/en/quof-breezysrpg95-claude-interpreter.md)** · `2026-10-25` — Quof reports **Claude-assisted disassembly of the original runtime**, adding keyboard controls, fast-forward and enemy ranges. Public project; early beta tried by only a few people, with save-compatibility limits. Not run here. `In progress`
10. **[KakaSoft: inspect what “Highest” protection actually does](cases/en/kakasoft-usb-copy-protection-ai-review.md)** · `2026-10-23` (Beijing time) — Xusheng Li reports AI tracing **a hidden test file, a modified hash and client-side key derivation**, then recovering his own file without its user password. Version 5.6.0.299; a researcher test, **not a break of Blowfish** or an independent reproduction here. `Analysis test`

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
| [Games & preservation](categories/en/games.md) | **214** |
| [Hardware & interoperability](categories/en/hardware.md) | **270** |
| [Applications & clients](categories/en/apps.md) | **413** |
| [Algorithms & feature recovery](categories/en/algorithms.md) | **83** |

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
