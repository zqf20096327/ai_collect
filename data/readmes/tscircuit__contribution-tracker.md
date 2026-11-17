# contribution tracker

[contributions.tscircuit.com](https://contributions.tscircuit.com) ・ [tscircuit.com](https://tscircuit.com) ・ [Contribution Overviews](./contribution-overviews/) ・ [Changelogs](./changelogs/)

Generates weekly contribution overviews for tscircuit contributors. Check out all
the [contribution overviews here](./contribution-overviews/)
You can find AI-generated monthly changelogs in the [changelogs directory](./changelogs/)

- All PRs in the tscircuit org are scanned/summarized via an LLM
- The LLM classifies each Diff/PR as into a set of attributes for scoring
- All the PRs, summaries, and classifications are organized into charts and tables for [the website](https://contributions.tscircuit.com)

> Want to run locally? See the [Development Section](#development)

## Current Week

<!-- START_CURRENT_WEEK -->

# Contribution Overview 2026-11-10

The current week is shown below. There are 3 major sections:

- [Contributor Overview](#contributor-overview)
- [PRs by Repository](#prs-by-repository)
- [PRs by Contributor](#changes-by-contributor)
- [Scoring & Sponsorship Details](/docs/sponsorship-calculation-explanation.md)

## PRs by Repository

```mermaid
pie
    "tscircuit/circuit-json" : 6
    "tscircuit/props" : 7
    "tscircuit/core" : 91
    "tscircuit/circuit-to-svg" : 2
    "tscircuit/tscircuit.com" : 142
    "tscircuit/jlcsearch" : 13
    "tscircuit/runframe" : 139
    "tscircuit/cli" : 23
    "tscircuit/svg.tscircuit.com" : 54
    "tscircuit/docs" : 5
    "tscircuit/high-density-repair02" : 8
    "tscircuit/high-density-repair03" : 11
    "tscircuit/fanout-solver" : 6
    "tscircuit/bus-lanes-solver" : 13
    "tscircuit/circuit-json-to-drawing" : 2
    "tscircuit/tscircuit-desktop" : 20
    "tscircuit/schematic-viewer" : 1
    "tscircuit/3d-viewer" : 2
    "tscircuit/status" : 1
    "tscircuit/common" : 1
    "tscircuit/tscircuit.com-landing" : 1
    "tscircuit/motorcontrol" : 1
    "tscircuit/circuit-json-webgpu" : 3
    "tscircuit/drawing-viewer" : 3
    "tscircuit/pcb-viewer" : 2
    "tscircuit/tscircuit" : 120
    "tscircuit/eval" : 114
    "tscircuit/tscircuit-autorouter" : 106
    "tscircuit/schematic-trace-solver" : 6
    "tscircuit/circuit-json-to-kicad" : 14
    "tscircuit/circuit-json-schematic-placement-analysis" : 4
    "tscircuit/circuit-json-to-3d-png" : 4
    "tscircuit/dogbone-solver" : 7
    "tscircuit/circuit-json-to-jlcpcb-quote" : 11
    "tscircuit/manufacturing-simulation" : 5
    "tscircuit/footprinter" : 1
    "tscircuit/tscircuit-standalone" : 1
    "tscircuit/checks" : 7
    "tscircuit/math-utils" : 1
    "tscircuit/tiny-hypergraph" : 1
    "tscircuit/length-matching-solver" : 7
    "tscircuit/repair04" : 4
    "tscircuit/trace-simplification-solver" : 2
    "tscircuit/circuit-json-to-spice" : 1
    "tscircuit/circuit-json-to-gerber" : 4
    "tscircuit/kicad-to-circuit-json" : 6
    "tscircuit/contribution-tracker" : 2
```

## Contributor Overview

| Contributor | 🐳 Major | 🐙 Minor | 🐌 Tiny | Score | ⭐ |
|-------------|---------|---------|---------|-------|-----|
| [ShiboSoftwareDev](#ShiboSoftwareDev) | 84 | 17 | 47 | 394 | 👑👑👑 |
| [seveibar](#seveibar) | 35 | 17 | 18 | 187 | 👑👑👑 |
| [Abse2001](#Abse2001) | 8 | 15 | 17 | 83 | 👑 |
| [imrishabh18](#imrishabh18) | 6 | 16 | 5 | 62 | ⭐⭐⭐ |
| [0hmX](#0hmX) | 9 | 4 | 2 | 47 | ⭐⭐ |
| [MustafaMulla29](#MustafaMulla29) | 5 | 6 | 18 | 45 | ⭐⭐ |
| [AnasSarkiz](#AnasSarkiz) | 5 | 5 | 6 | 37 | ⭐⭐ |
| [rushabhcodes](#rushabhcodes) | 3 | 9 | 4 | 34 | ⭐⭐ |
| [techmannih](#techmannih) | 3 | 2 | 3 | 19 | ⭐⭐ |
| [tscircuitbot](#tscircuitbot) | 0 | 0 | 608 | 15.5 | ⭐⭐ |
| [GokulPandi-M](#GokulPandi-M) | 0 | 0 | 5 | 4.5 | ⭐ |
| [KrishnaX12](#KrishnaX12) | 0 | 0 | 1 | 1 |  |
| [hrithik18k](#hrithik18k) | 0 | 0 | 1 | 1 |  |
| [abdalraof-albarbar](#abdalraof-albarbar) | 0 | 0 | 1 | 1 |  |

## Staff Pass Ratio (SPR)

| Contributor | Reviewed PRs | Rejections | Approvals | SPR |
|-------------|--------------|------------|-----------|-----|
| [ShiboSoftwareDev](#ShiboSoftwareDev) | 18 | 0 | 18 | 100.0% |
| [0hmX](#0hmX) | 13 | 1 | 13 | 92.3% |
| [Abse2001](#Abse2001) | 12 | 2 | 12 | 83.3% |
| [rushabhcodes](#rushabhcodes) | 7 | 3 | 7 | 57.1% |
| [imrishabh18](#imrishabh18) | 4 | 0 | 4 | 100.0% |
| [techmannih](#techmannih) | 4 | 0 | 5 | 100.0% |
| [AnasSarkiz](#AnasSarkiz) | 3 | 1 | 2 | 66.7% |
| [MustafaMulla29](#MustafaMulla29) | 3 | 0 | 3 | 100.0% |
| [mukesh-dev-git](#mukesh-dev-git) | 1 | 1 | 0 | 0.0% |

<details>
<summary>ShiboSoftwareDev SPR PRs (18)</summary>

- [#5523](https://github.com/tscircuit/core/pull/5523) Handle plated-hole passages in supplied bus routing copper
- [#5524](https://github.com/tscircuit/core/pull/5524) Honor explicit fanout layers and staggered edge capacity
- [#75](https://github.com/tscircuit/circuit-json-to-spice/pull/75) fix: let custom SPICE subcircuits replace built-in components
- [#3795](https://github.com/tscircuit/tscircuit-autorouter/pull/3795) fix: preserve regional repair progress across error priorities
- [#3796](https://github.com/tscircuit/tscircuit-autorouter/pull/3796) Fix through-via clearance across the physical board stack
- [#3783](https://github.com/tscircuit/tscircuit-autorouter/pull/3783) fix: pass the board via copper minimum to node repair
- [#3770](https://github.com/tscircuit/tscircuit-autorouter/pull/3770) fix: preserve preloaded vias at routing cell boundaries
- [#3765](https://github.com/tscircuit/tscircuit-autorouter/pull/3765) fix: honor explicit via clearance in regional repair guard
- [#3760](https://github.com/tscircuit/tscircuit-autorouter/pull/3760) fix: honor declared via clearance when validating projection
- [#3733](https://github.com/tscircuit/tscircuit-autorouter/pull/3733) fix: preserve validated gaps in stitch paths
- [#3671](https://github.com/tscircuit/tscircuit-autorouter/pull/3671) Avoid repeated mesh scans during DDR port spacing
- [#3667](https://github.com/tscircuit/tscircuit-autorouter/pull/3667) Use faster DDR length-matching obstacle checks
- [#3664](https://github.com/tscircuit/tscircuit-autorouter/pull/3664) Restore physically clear BGA via columns at the gap threshold
- [#3693](https://github.com/tscircuit/tscircuit-autorouter/pull/3693) repro: ButterStick bus wires ignore allowed layers
- [#3660](https://github.com/tscircuit/tscircuit-autorouter/pull/3660) fix: retain H616 DDR repairs during final contact restoration
- [#201](https://github.com/tscircuit/high-density-repair03/pull/201) fix: preserve independent repairs during contact restoration
- [#90](https://github.com/tscircuit/length-matching-solver/pull/90) Skip distant pads before DDR meander clearance checks
- [#198](https://github.com/tscircuit/bus-lanes-solver/pull/198) Avoid repeated pad-alias expansion during pending exit search

</details>

<details>
<summary>0hmX SPR PRs (13)</summary>

- [#996](https://github.com/tscircuit/circuit-json/pull/996) fix: enforce ordered length-only differential pair buses
- [#5549](https://github.com/tscircuit/core/pull/5549) refactor: remove archived infgrid and soup-util dependencies (blocked migration)
- [#5382](https://github.com/tscircuit/core/pull/5382) feat: include per-connection compute cost in autorouting events
- [#5413](https://github.com/tscircuit/core/pull/5413) fix: emit the ordered path of every multi-port trace
- [#5412](https://github.com/tscircuit/core/pull/5412) test: reproduce trace path order not emitted or routed
- [#5415](https://github.com/tscircuit/core/pull/5415) test: cover three-pad differential path routing data flow
- [#5760](https://github.com/tscircuit/cli/pull/5760) feat: capture per-connection compute cost in autorouter diagnostics
- [#3710](https://github.com/tscircuit/tscircuit-autorouter/pull/3710) fix: pass ordered differential lane hops to length matching
- [#3709](https://github.com/tscircuit/tscircuit-autorouter/pull/3709) fix: length-match ordered differential pair lanes
- [#3651](https://github.com/tscircuit/tscircuit-autorouter/pull/3651) Add a per-connection compute cost summary to the pipeline 9 solver
- [#3708](https://github.com/tscircuit/tscircuit-autorouter/pull/3708) fix: route connection path points in order
- [#1441](https://github.com/tscircuit/schematic-trace-solver/pull/1441) feat: opt into interior-channel recovery for wire-only consumers
- [#315](https://github.com/tscircuit/tiny-hypergraph/pull/315) Report each connection's solo search iterations from DuplicateCongestedPortSolver

</details>

<details>
<summary>Abse2001 SPR PRs (12)</summary>

- [#1011](https://github.com/tscircuit/props/pull/1011) Add defaultSolderPasteMargin to board props
- [#5500](https://github.com/tscircuit/core/pull/5500) Apply board defaultSolderPasteMargin to its SMT pads (#4800)
- [#5217](https://github.com/tscircuit/core/pull/5217) feat: V-score panel tabs with vScore (#5067)
- [#5214](https://github.com/tscircuit/core/pull/5214) feat: implement finished panel size limits (#5067)
- [#5211](https://github.com/tscircuit/core/pull/5211) feat: implement tooling rail elements (#5067)
- [#5208](https://github.com/tscircuit/core/pull/5208) feat: implement panel tab child elements (#5067)
- [#5205](https://github.com/tscircuit/core/pull/5205) feat: implement panel silkscreen (#5067)
- [#5202](https://github.com/tscircuit/core/pull/5202) feat: implement panel tooling holes and fiducials (#5067)
- [#256](https://github.com/tscircuit/circuit-json-to-gerber/pull/256) Skip soldermask for inner-layer copper pours (#127)
- [#246](https://github.com/tscircuit/circuit-json-to-gerber/pull/246) Merge cutouts that are flush with the board edge into the board outline
- [#632](https://github.com/tscircuit/jlcsearch/pull/632) Expose JLCPCB's Standard-only mark on verified parts
- [#5771](https://github.com/tscircuit/cli/pull/5771) Implement tsci quote estimate with the JLCPCB quote estimator

</details>

<details>
<summary>rushabhcodes SPR PRs (7)</summary>

- [#1002](https://github.com/tscircuit/circuit-json/pull/1002) feat: preserve nominal board trace width in Circuit JSON
- [#5400](https://github.com/tscircuit/core/pull/5400) fix: preserve authored pad layers in mixed-side footprints
- [#5375](https://github.com/tscircuit/core/pull/5375) [2/2] Preserve unbroken inner copper planes in remote autorouting
- [#5404](https://github.com/tscircuit/core/pull/5404) fix: preserve plated-slot rotation on flipped footprints
- [#5402](https://github.com/tscircuit/core/pull/5402) fix: render pcbtrace coordinate routes
- [#108](https://github.com/tscircuit/circuit-json-webgpu/pull/108) Show Classic F1 ground traces when copper pours are hidden
- [#12](https://github.com/tscircuit/drawing-viewer/pull/12) Render assembly stages and exploded views in Drawing Viewer

</details>

<details>
<summary>imrishabh18 SPR PRs (4)</summary>

- [#646](https://github.com/tscircuit/jlcsearch/pull/646) Keep stock cleanup scans small and resume them between runs
- [#635](https://github.com/tscircuit/jlcsearch/pull/635) Fix JSON output after D1 stock-sync retries
- [#638](https://github.com/tscircuit/jlcsearch/pull/638) Add a safe search-index-only rebuild action
- [#7](https://github.com/tscircuit/manufacturing-simulation/pull/7) Simulate the Amazon partnered carrier label at Ship-ready

</details>

<details>
<summary>techmannih SPR PRs (4)</summary>

- [#5343](https://github.com/tscircuit/core/pull/5343) Fix named-net routing via a phase-selected pin
- [#5341](https://github.com/tscircuit/core/pull/5341) Fix plated-hole solder paste ownership
- [#557](https://github.com/tscircuit/checks/pull/557) Use the board via-to-pad clearance for routing DRC
- [#5750](https://github.com/tscircuit/cli/pull/5750) Fix autorouter worker count in tsci build

</details>

<details>
<summary>AnasSarkiz SPR PRs (3)</summary>

- [#540](https://github.com/tscircuit/checks/pull/540) fix: recognize explicit pin role attributes as specified
- [#5780](https://github.com/tscircuit/cli/pull/5780) fix: warn when imports omit an explicit 3D model
- [#15](https://github.com/tscircuit/tscircuit-desktop/pull/15) feat(circuit): stack two Circuit views vertically

</details>

<details>
<summary>MustafaMulla29 SPR PRs (3)</summary>

- [#5426](https://github.com/tscircuit/core/pull/5426) fix: preserve copper-plane connectivity at breakout endpoints
- [#5438](https://github.com/tscircuit/core/pull/5438) fix: keep board plane reservations independent of child groups
- [#268](https://github.com/tscircuit/fanout-solver/pull/268) fix: generate exact-angle dogbone sites for imported pad grids

</details>

<details>
<summary>mukesh-dev-git SPR PRs (1)</summary>

- [#5544](https://github.com/tscircuit/core/pull/5544) fix: support pinLabels on mosfet to match physical package pins

</details>

> Note: AI evaluates PRs and assigns 1-3 star ratings automatically. 4 and 5 star ratings require manual staff review.

## Review Table

[reviews-received-hover]: ## "Number of reviews received for PRs for this contributor"
[approvals-received-hover]: ## "Number of approvals received for PRs this contributor authored"
[rejections-received-hover]: ## "Number of rejections received for PRs this contributor authored"
[prs-opened-hover]: ## "Number of PRs opened by this contributor"
[issues-created-hover]: ## "Number of issues created by this contributor"

| Contributor | Reviews Received | Approvals Received | Rejections Received | Approvals | Rejections Given | PRs Opened | PRs Merged | Issues Created |
|---|---|---|---|---|---|---|---|---|
| [0hmX](#0hmX) | 57 | 14 | 1 | 34 | 0 | 75 | 17 | 0 |
| [1932819331hy-debug](#1932819331hy-debug) | 0 | 0 | 0 | 0 | 0 | 34 | 0 | 0 |
| [abdalraof-albarbar](#abdalraof-albarbar) | 0 | 0 | 0 | 0 | 0 | 3 | 1 | 0 |
| [Abse2001](#Abse2001) | 16 | 15 | 0 | 9 | 0 | 64 | 40 | 0 |
| [ameenalqershi](#ameenalqershi) | 0 | 0 | 0 | 0 | 0 | 9 | 0 | 0 |
| [AnasSarkiz](#AnasSarkiz) | 13 | 12 | 1 | 2 | 0 | 29 | 16 | 0 |
| [Andresdev14](#Andresdev14) | 0 | 0 | 0 | 0 | 0 | 11 | 0 | 0 |
| [aswadi](#aswadi) | 0 | 0 | 0 | 0 | 0 | 204 | 0 | 0 |
| [Asymtode712](#Asymtode712) | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 |
| [BHAWESHBHASKAR](#BHAWESHBHASKAR) | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| [Burapa-J](#Burapa-J) | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 |
| [cocvn157](#cocvn157) | 0 | 0 | 0 | 0 | 0 | 28 | 0 | 0 |
| [contactmelvinlevard](#contactmelvinlevard) | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| [CrowAleksito](#CrowAleksito) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [deep-bhikadiya](#deep-bhikadiya) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [Devesh36](#Devesh36) | 1 | 0 | 0 | 0 | 0 | 4 | 0 | 0 |
| [ghost](#ghost) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [GokulPandi-M](#GokulPandi-M) | 7 | 5 | 1 | 0 | 0 | 9 | 5 | 0 |
| [hrithik18k](#hrithik18k) | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 |
| [imrishabh18](#imrishabh18) | 9 | 6 | 0 | 15 | 3 | 40 | 27 | 0 |
| [imyelo](#imyelo) | 1 | 0 | 0 | 0 | 0 | 3 | 0 | 0 |
| [jeffrey-graham](#jeffrey-graham) | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| [KrishnaX12](#KrishnaX12) | 1 | 1 | 0 | 0 | 0 | 2 | 1 | 0 |
| [LBCron](#LBCron) | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 0 |
| [mohan-bee](#mohan-bee) | 1 | 0 | 0 | 0 | 0 | 15 | 0 | 0 |
| [mukesh-dev-git](#mukesh-dev-git) | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |
| [MustafaMulla29](#MustafaMulla29) | 13 | 12 | 1 | 4 | 1 | 37 | 29 | 0 |
| [nitina-ariveguru](#nitina-ariveguru) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [nolanntibi-dot](#nolanntibi-dot) | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 |
| [OLuHneschastniy](#OLuHneschastniy) | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 |
| [peteking](#peteking) | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| [rafagil11](#rafagil11) | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| [rushabhcodes](#rushabhcodes) | 24 | 9 | 2 | 0 | 0 | 53 | 17 | 0 |
| [sainath998](#sainath998) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [satoshinakamoto666666](#satoshinakamoto666666) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [seveibar](#seveibar) | 18 | 1 | 0 | 66 | 4 | 92 | 72 | 0 |
| [ShiboSoftwareDev](#ShiboSoftwareDev) | 61 | 61 | 0 | 13 | 0 | 228 | 151 | 0 |
| [singhaditya21](#singhaditya21) | 0 | 0 | 0 | 0 | 0 | 9 | 0 | 0 |
| [techmannih](#techmannih) | 23 | 7 | 1 | 0 | 0 | 30 | 8 | 0 |
| [tirumallaharish0200](#tirumallaharish0200) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [trixie010](#trixie010) | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 |
| [tscircuitbot](#tscircuitbot) | 0 | 0 | 0 | 0 | 0 | 716 | 608 | 0 |
| [tungnguyen84](#tungnguyen84) | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| [ulixes](#ulixes) | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 |
| [Umutplvn](#Umutplvn) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [VB-Blue](#VB-Blue) | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 |
| [voropaevv](#voropaevv) | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 |
| [xtruel](#xtruel) | 0 | 0 | 0 | 0 | 0 | 13 | 0 | 0 |
| [yan0lovesha](#yan0lovesha) | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 |

## Changes by Repository

### [tscircuit/circuit-json](https://github.com/tscircuit/circuit-json)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#1003](https://github.com/tscircuit/circuit-json/pull/1003) | 🐳 Major | ⭐⭐⭐ | seveibar | Adds assembly-stage drawings with a dedicated drawing_explosion_view record, allowing for independent explosion views with configurable moves, factors, and trails. |
| [#1004](https://github.com/tscircuit/circuit-json/pull/1004) | 🐳 Major | ⭐⭐⭐ | seveibar | Add optional schematic_group.show_boundary, schematic_port.schematic_group_id, and schematic_port.boundary_position to define expanded subcircuit boundaries and public terminal geometry. |
| [#1002](https://github.com/tscircuit/circuit-json/pull/1002) | 🐙 Minor | ⭐⭐ | rushabhcodes | Adds the optional pcb_board.default_nominal_trace_width field to the canonical schema to store the boards preferred routing width for connections without an explicit width, addressing issues with SRJ conversion. |

<details>
<summary>🐌 Tiny Contributions (3)</summary>

| PR # | Impact | Contributor | Description |
|------|--------|-------------|-------------|
| [#1009](https://github.com/tscircuit/circuit-json/pull/1009) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#1007](https://github.com/tscircuit/circuit-json/pull/1007) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#1005](https://github.com/tscircuit/circuit-json/pull/1005) | 🐌 Tiny | tscircuitbot | Automated package update |

</details>

### [tscircuit/props](https://github.com/tscircuit/props)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#1010](https://github.com/tscircuit/props/pull/1010) | 🐳 Major | ⭐⭐⭐ | seveibar | Refactors the drawing explosion view to inherit moves from assembly explosion stages, removing the need for inline moves and standalone drawing explosions. |
| [#1009](https://github.com/tscircuit/props/pull/1009) | 🐳 Major | ⭐⭐⭐ | seveibar | Adds assembly drawing capabilities with explosion views and reusable stage definitions, enhancing the drawing functionality for parts and assemblies. |
| [#1011](https://github.com/tscircuit/props/pull/1011) | 🐙 Minor | ⭐⭐ | Abse2001 | Adds defaultSolderPasteMargin to board for setting a uniform solder paste margin across all pads on the board, allowing for more consistent solder paste application without altering individual pad settings. |

<details>
<summary>🐌 Tiny Contributions (4)</summary>

| PR # | Impact | Contributor | Description |
|------|--------|-------------|-------------|
| [#1022](https://github.com/tscircuit/props/pull/1022) | 🐌 Tiny | 0hmX | Adds pinLabels to mosfetProps, allowing users to specify physical package pins mapped to terminal names for MOSFET components. |
| [#1004](https://github.com/tscircuit/props/pull/1004) | 🐌 Tiny | 0hmX | Documents that trace paths should always be ordered, clarifying that the trace is routed as a chain from the first port to the last. |
| [#999](https://github.com/tscircuit/props/pull/999) | 🐌 Tiny | Abse2001 | Changes the paneltab component to use center offsets from board edges instead of a single offset, introducing new properties for better tab placement and width specification. |
| [#1000](https://github.com/tscircuit/props/pull/1000) | 🐌 Tiny | Abse2001 | Updates documentation to clarify that panel size limits now shape the grid layout, allowing auto-sized panels to grow and grids to rearrange based on specified limits. |

</details>

### [tscircuit/core](https://github.com/tscircuit/core)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#5497](https://github.com/tscircuit/core/pull/5497) | 🐳 Major | ⭐⭐⭐ | seveibar | Connects the merged drawing propsschema to core: assembly.drawing.explosionview stageReflift-cover now emits an exploded drawing from the referenced assembly.explosion.stage and its assembly.explosion.move children. Authors do not supply a drawing moves prop. Core reuses existing ordered explosion evaluation through the selected stage, including preceding moves, overlapping parentchild targets and mounted owner frames. It emits one final CAD-world translation per source component, preserving assembled geometry. Each view has independent factorshowTrails; factor 0 restores assembled placement. Qualified references select nested stages. Also registers drawing membership stages, part labels and pageview notes. Assembled views can select reusable stages, including PCB substrates and fitted components. Labels follow their targets, notes support per-axis view offsets, and page anchors use anchorAlignment. References are validated before committing a page; dimensions are computed from the displayed pose, including factor and section cuts. Labeled legacy board views get explicit membership for the identity-preserving renderer path. Uses published props 0.0.731, Circuit JSON 0.0.550 and drawing renderer 0.0.6. The snapshot adapter converts the existing glTF export frame to the renderers canonical CAD-to-scene frame; native dimensions use the paired camera transform. Validation: 139 assemblynamespaced tests pass across the suite and focused runs, including 24 drawing tests; typecheck, build, built-package drawing smoke test, class-export check, dependency check and formatting pass. Six new committed SVG snapshots cover inherited cumulative moves, independent view factors, rotated owner frames, displayed-pose section dimensions, PCB membership, labelspage anchors and invalid references. Existing drawing snapshots are unchanged. !Inherited moves, independent drawing factors(https:raw.githubusercontent.comtscircuitcorefeatassembly-drawing-explosion-viewstestsassembly__snapshots__assembly-drawing-explosionview.snap.svg) !Qualified stages in mounted owner frames(https:raw.githubusercontent.comtscircuitcorefeatassembly-drawing-explosion-viewstestsassembly__snapshots__assembly-drawing-explosion-frames.snap.svg) Existing assembly playback restrictions remain: moving PCBcable geometry is unsupported, while stationary boards can be shown. Geometry loading for dimensions retains the existing native-model support boundary. Authoring and emission documentation(https:github.comtscircuitcoreblobfeatassembly-drawing-explosion-viewsdocsassembly-drawings.mdexplosion-views-and-assembly-stages). |
| [#5507](https://github.com/tscircuit/core/pull/5507) | 🐳 Major | ⭐⭐⭐ | seveibar | Problem System diagrams drew hooks, 12 mm S-bends and angular corners. Four causes: Every labelled wire was routed through a label slot Dagre picked before routing, so wires detoured to reach their own text. Port slots on facing blocks rarely lined up, which put a short jog into wires that should be straight. When two parallel wires turned together, the outer one was left angular. The slot-swap optimizer could move a port to the far side of its block to remove a crossing, wrapping the wire around the block.  Change Route each wire directly, then place its label on the finished wire: inline on a horizontal run, otherwise beside it. Only self-loops still reserve their label first. Slide an attachment along its block face, without passing a neighbor, when that straightens the wire. A port never starts on, or is swapped to, a face that looks away from the block it connects to. Wires that double back are penalized in the diagram score. The path search counts turns at the port stubs as bends, and stubs are a full 6 mm so the first fillet and the arrowhead have room. Rounding compares neighboring wires in their rounded form, so nested corners keep concentric fillets.  Results   Before  After  ---------  Flip-phone fixture (23 wires): bends  105  46   Flip-phone fixture: sharp or under 3 mm radius  62  1   250 random diagrams (1,917 wires): bends  8,705  3,320   250 random: sharp corners  566  4   250 random: fillets under 1.5 mm  2,849  27   250 random: crossing wire pairs  501  350   250 random: layout time  63 s  12 s  The random-diagram numbers come from a throwaway script that is not part of this PR.  Tests New system-blocks-flip-phone test and fixture, with an assertSystemWireSmoothness helper. It fails on the previous router. The existing no-crossing and 3 mm separation checks on both RVBoy pages pass unchanged. Two tests asserted that every wire contains a curve. Some wires are now straight, so they assert that every bend is a fillet instead. Nine existing snapshots are regenerated.  Known limits In tight downup diagrams a label can land beside the wrong wire. In the power-feedback snapshot, Feedback sits left of the dashed 3.3 V wire. Very dense graphs still produce long detours where the router avoids crossings. docssystem-blocks.md is edited only where this change made existing sentences false. |
| [#5559](https://github.com/tscircuit/core/pull/5559) | 🐳 Major | ⭐⭐⭐ | rushabhcodes | Store the boards authored defaultTraceWidth in pcb_board.default_nominal_trace_width using circuit-json0.0.551. Restore the saved value through defaultTraceWidth when loading boards and use each owning boards default for SRJ connections without an explicit width. |
| [#5399](https://github.com/tscircuit/core/pull/5399) | 🐳 Major | ⭐⭐⭐ | rushabhcodes | An explicit component layer collapses a mixed-side footprint onto one side. Centralize the duplicated SMT pad layer resolver without changing behavior, and capture the bug with a minimal four-pad example plus a real imported connector footprint. The real example is the Amphenol 132289 edge-mount SMA(https:github.comKiCadkicad-footprintsblob7ebfa6b23cc292a56f751b7b5f4a0e12eeef69ddConnector_Coaxial.prettySMA_Amphenol_132289_EdgeMount.kicad_modL39) from the pinned KiCad library: three SMT pads on F.Cu and two ground pads on B.Cu. This branch incorrectly emits all five pads on the components placement layer. A single three-pane image shows the PCB, 3D top, and 3D bottom, including the actual KiCad SMA STEP model(https:gitlab.comkicadlibrarieskicad-packages3D-blob77236890410eb655ba2e63e23f59a85cf45af290Connector_Coaxial.3dshapesSMA_Amphenol_132289_EdgeMount.step). The unmodified model is served locally during tests, and the connectors mount on opposite board edges. The real-component regression also exercises ordinary 0402 controls and cached placement once the dependent fix is applied. This work follows up on Jan Mrzeks November 9, 2026 email to Severin Ibarluzea, titled Re: mind.dump() Interest in work with tscircuit (new venture-backed EDA tool). Item 3 under Placement reported:  Setting layer on a component forces all of its pads onto that layer, so a mixed-side footprint loses its other-side pads. Both regressions use test.failing to record the known layer bug. Snapshot assertions run separately in beforeAll, so visual mismatches still fail CI. The dependent fix, 5400, removes the expected-failure markers and updates the snapshots. The minimal example uses a single redtop, bluebottom view with fixed pad positions; the real connectors three-pane image exposes the coincident ground pads on each face. !Broken baseline: PCB, 3D top, 3D bottom(https:raw.githubusercontent.comtscircuitcore4f7fd1c56ddcf9fd4a6bc95565ea237a0ffc2e52testsrepros__snapshots__amphenol-132289-mixed-side-pad-layers.snap.svg) Validation: both expected-failure regressions, all ten CI test shards, typecheck, build preview, and smoke checks pass. Part 1 of GitHub stack 5401(https:github.comtscircuitcorestack5401): main  5399  5400. |
| [#5375](https://github.com/tscircuit/core/pull/5375) | 🐳 Major | ⭐⭐⭐ | rushabhcodes | Preserves unbroken inner copper planes in remote autorouting by ensuring that raw Circuit JSON requests maintain the intended copper pour intent during routing processes. |
| [#5384](https://github.com/tscircuit/core/pull/5384) | 🐳 Major | ⭐⭐⭐ | imrishabh18 | Adds an optional ordered path of point IDs to the existing SRJ connection for each explicitly declared multi-pad differential trace, preserving matching explicit paths attached to named nets as their own SRJ connections. |
| [#5424](https://github.com/tscircuit/core/pull/5424) | 🐳 Major | ⭐⭐⭐ | MustafaMulla29 | After native copper-pour generation, the STM32s ground pads already connect through their escape vias and a shared ground plane. Core loses that physical connection when exporting breakout endpoints, so the native router requests redundant connections. This TSX repro uses U70s complete STM32MP157DAB1 footprint from our four-motor USB-CUSB-PD motherboard: All 354 literal pad definitions match the JLCPCB C1236721 import, including its original coordinates and sizes. All 104 motherboard GND assignments are retained, with semantic ball names from the board. The same six-layer arrangement, 20  20 mm breakout region, native dogbone settings and relevant tracevia rules are used. The chip remains at its motherboard position, (0, 20). A 24  24 mm inspection board contains the chip and one native inner1 ground pour. Other nets, other motherboard components and unused 3D assets are omitted. The test runs native dogbone routing  native ground-pour generation  core SRJ export  native point-pair generation. All 104 escape vias are generated afresh and checked geometrically against the same ground pour. Expected: 0 new routes; actual: 103 redundant requests. No patched solver, saved routes, injected copper or dependencyconfiguration changes. The snapshot separates existing copper from connection requests. The complete chip, TOP escape close-up and INNER1 plane close-up are pixel-identical before and after the fix. A separate aligned INNER3 panel shows the actual native requests as dashed pink lines. The written path follows F7 pad  short trace  F7 via  shared INNER1 plane  G6 via  short trace  G6 pad. Pink dashes mean connect these endpoints; they are neither copper nor a prescribed track shape. The test uses routeRemainingfalse: it skips full-board routing so native pour generation can complete, then tests the export of that existing copper. It does not reproduce or fix the motherboards initial routing iteration-limit failure, which occurs before the physical pours are generated. This defect was found when motherboard path search exhausted its budget on ground links before reaching DDR signals. The stacked fix is 5426; its matching full-STM32 snapshot changes 103 requests to 0. Validation: the updated native STM32 repro and full TypeScript check pass on both the repro and fix branches; changed-file formatting passes. Rendered beforeafter images were compared and all three physical-copper panels are pixel-identical. The existing copper-pour terminal-routing test passed in earlier verification. Every imported pad definition matches the motherboard source. The previously investigated full-suite failure is the existing AM62L direct-decoupling snapshot mismatch, also present on unchanged main: repro log(https:github.comtscircuitcoreactionsruns43183539146job131065071153), main log(https:github.comtscircuitcoreactionsruns43140285484job130925346524). That unrelated snapshot is unchanged. The full suite was not rerun locally for this fixture update. |
| [#5426](https://github.com/tscircuit/core/pull/5426) | 🐳 Major | ⭐⭐⭐ | MustafaMulla29 | Fixes copper-plane connectivity issues at breakout endpoints, preventing redundant routing requests in the autorouter. |
| [#5437](https://github.com/tscircuit/core/pull/5437) | 🐳 Major | ⭐⭐⭐ | MustafaMulla29 | Fixes incorrect board-level plane reservations caused by child groups affecting autorouting output. |
| [#5556](https://github.com/tscircuit/core/pull/5556) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Fixes autorouting failure for ButterStick power input by updating checks to version 0.0.279, allowing proper routing without placement or connectivity errors. |
| [#5552](https://github.com/tscircuit/core/pull/5552) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Bumps the tscircuitcapacity-autorouter dependency from version 0.0.1101 to 0.0.1102 to include fixes for movable preload ports and enhance reachability in autorouting. |
| [#5523](https://github.com/tscircuit/core/pull/5523) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Fixes autorouting failure when handling plated-hole passages in bus routing, enabling successful routing of DQ signals. |
| [#5524](https://github.com/tscircuit/core/pull/5524) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Fixes autorouting failure by honoring explicit fanout layers for unbused connections and adjusting edge capacity to accommodate staggered layer assignments. |
| [#5486](https://github.com/tscircuit/core/pull/5486) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Bumps the tscircuitcapacity-autorouter dependency from 0.0.1090 to 0.0.1092, incorporating fixes for same-net negotiation and board clearance propagation, while ensuring compatibility with native iMX6. |
| [#5442](https://github.com/tscircuit/core/pull/5442) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Bumps capacity-autorouter from 0.0.1083 to 0.0.1084 to bring in the regional portfolio candidate-validation fix, allowing the H616 SVREF region to reject invalid candidates and keep searching for a legal route. |
| [#5388](https://github.com/tscircuit/core/pull/5388) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Bumps tscircuitcapacity-autorouter from 0.0.1071 to 0.0.1074, incorporating fixes for faster DDR length-matching obstacle checks, retaining H616 DDR repairs, and restoring physically clear BGA via columns at the gap threshold. |
| [#5413](https://github.com/tscircuit/core/pull/5413) | 🐳 Major | ⭐⭐⭐ | 0hmX | Fixes the emission of ordered paths for every multi-port trace, ensuring that paths with 3 or more ports are correctly represented in the autorouting system. |
| [#5380](https://github.com/tscircuit/core/pull/5380) | 🐳 Major | ⭐⭐⭐ | 0hmX | Fixes autorouting failure when differential pairs are connected to nets that are not routed, leading to ratsnest lines and port-not-connected errors. |
| [#5412](https://github.com/tscircuit/core/pull/5412) | 🐳 Major | ⭐⭐⭐ | 0hmX | Reproduces a bug where trace paths are not emitted or routed in the correct order, specifically for paths involving multiple pins. |
| [#5343](https://github.com/tscircuit/core/pull/5343) | 🐳 Major | ⭐⭐⭐ | techmannih | Fixes autorouting failure when a phase-selected pin does not route a named net connection, resulting in zero routed traces on the PCB. |
| [#5341](https://github.com/tscircuit/core/pull/5341) | 🐳 Major | ⭐⭐⭐ | techmannih | Fixes the ownership assignment for solder paste records associated with circular plated holes in KiCad exports, ensuring correct PCB component IDs are applied. |
| [#5445](https://github.com/tscircuit/core/pull/5445) | 🐙 Minor | ⭐⭐ | seveibar | When a subcircuit is rendered as the sole root element, show its internal schematic inside a boundary with public terminals wired to internal pins. Reuse direct port children and existing exposedNets  exposeNets declarations; no new TSX prop is required. Core assigns frame and terminal geometry after internal layout and before routing. schPinArrangement supplies sideorder, with each ports direction as fallback. Terminals align with connected internal pins when space permits. Public source ports retain group ownership and electrical connectivity; exposed nets produce public ports deduplicated against explicit declarations. Boundary terminals get explicit connections to internal pins in the targets schematic section. This prevents section splitting from replacing their wires with disconnected labels. Boundary wires retain their actual source trace IDs. Other inter-section connections keep their net-label representation. Standalone section layout and solver membership use the root subcircuit when there is no board. The integration fixture adapts the real ShiboSoftwareDev CC2340R5 reference design, release bff7bbb1-c0df-4b3e-8cb2-5f5c706caa87. It retains all 27 components, values, and all 16 original nets, including RFantenna, crystals, DCDCdecoupling, reset and SWD circuitry. The module exports VDDS, GND, RESET_N, SWDIO, SWCLK and eight GPIOs: DIO8, DIO11, DIO12, DIO13, DIO20_A11, DIO21_A10, DIO24_A7 and DIO6_A1. Those GPIOs were marked unconnected in the published board; this adaptation removes their NC declarations and adds eight named nets. The result has 13 public terminals and 24 nets. U1s schematic pin arrangement aligns the interface on the left; the physical pin mappings are preserved. Tests compare the emitted electrical signature to the immutable published signature plus the explicit eight-net addition. They also traverse actual wire edges from every boundary terminal to its MCU pin, without using net labels as edges, for both direct-port and exposed-net modes. Four inspected visual snapshots cover direct ports, exposed nets with translation, board-nested use, and the collapsed module. The converter fixture is generated from actual core output. Initial scope: one standalone root subcircuit on one schematic sheet. Multi-sheet interface placement, arbitrary drawing primitives as layout inputs, and manual public-port coordinates are deferred. Routing respects the configured trace-distance limit. Schema 1004 and renderer 932 are merged. This PR now uses published circuit-json0.0.550 (including the override) and circuit-to-svg0.0.460; no local companion links or preview dependencies are required. The renderer upgrade also includes its simulation-legend sizing fix. Refresh 15 existing simulation snapshots for the expanded graph canvas and centered titles; plotted data, axes and legend text are unchanged. All 15 affected tests pass without update mode. Validation against those npm packages: all four CC2340R5 integration tests pass, including their actual wire-path assertions and visual snapshots. The remaining targeted subcircuit, group-port and schematic-section checks pass (one existing skip). Three snapshots were refreshed for the crystal symbol from cores installed symbol library, visually inspected, and rerun without update mode. TypeScript check and build pass. |
| [#5483](https://github.com/tscircuit/core/pull/5483) | 🐙 Minor | ⭐⭐ | seveibar | Enables the use of a string cadModel as a footprinter model for normal components, allowing for procedural generation of 3D models based on the cadModel string, independent of the PCB footprint. |
| [#5558](https://github.com/tscircuit/core/pull/5558) | 🐙 Minor | ⭐⭐ | rushabhcodes | Fixes the issue where regenerating Simple Route JSON (SRJ) does not apply the boards default trace width correctly, ensuring that the intended 0.35 mm width is used instead of the minimum width of 0.10 mm. |
| [#5403](https://github.com/tscircuit/core/pull/5403) | 🐙 Minor | ⭐⭐ | rushabhcodes | A bottom-mounted USB-C connector rotated 30 currently has plated-slot long axes at 60, while its shell-hole centers and model mounting tabs require 120. Add real C165948 USB-C ports on opposite PCB faces and one three-pane snapshot showing the PCB, 3D from above, and 3D from below. Assert that the slot axes follow the connector and that every rendered mounting-tab tip fits inside a plated slot. Use the regenerated C165948 fixture from easyeda0.0.389 with OBJ metadata, including the corrected native model bounds and origin from easyeda-converter 540(https:github.comtscircuiteasyeda-converterpull540). Check in the OBJ for reproducible rendering and refresh the shared PCB snapshot to the converters current pill-shaped copper. The geometry regression uses test.failing to record the known rotation error. Snapshot validation runs separately in beforeAll, so snapshot mismatches still fail CI. The implementation fix, enabled regression, and corrected snapshots are in 5404. Local validation: All 25 related tests pass, including the expected failure and every test using the shared C165948 fixture. Running the regression as a regular test before the fix fails with expected 120 and received 60. Full TypeScript checking, Biome formatting, and git diff --check pass. Part 1 of GitHub stack 5405(https:github.comtscircuitcorestack5405). |
| [#5400](https://github.com/tscircuit/core/pull/5400) | 🐙 Minor | ⭐⭐ | rushabhcodes | Fixes the issue where an explicit component layer overwrites authored topbottom pad layers in mixed-side footprints, ensuring that pads without an explicit layer retain the component-layer default and preserving the correct pad layers during footprint flipping. |
| [#5404](https://github.com/tscircuit/core/pull/5404) | 🐙 Minor | ⭐⭐ | rushabhcodes | Fixes misalignment of plated-slot rotations for bottom-side components when flipped, ensuring correct alignment with the component. |
| [#5455](https://github.com/tscircuit/core/pull/5455) | 🐙 Minor | ⭐⭐ | imrishabh18 | Updates the Footprinter to version 0.0.451 to ensure proper silkscreen placement for cathode-first LED footprints, fixing regression issues present in version 0.0.450. |
| [#5438](https://github.com/tscircuit/core/pull/5438) | 🐙 Minor | ⭐⭐ | MustafaMulla29 | Fixes incorrect board plane reservations by ensuring that child groups do not influence the boards routing dimensions when their subcircuit IDs match. |
| [#5382](https://github.com/tscircuit/core/pull/5382) | 🐙 Minor | ⭐⭐ | 0hmX | Expose per-connection solo search compute cost on autorouting events, allowing for detailed performance metrics during routing processes. |
| [#5491](https://github.com/tscircuit/core/pull/5491) | 🐙 Minor | ⭐⭐ | Abse2001 | Fixes the issue where the boards defaultSolderPasteMargin is ignored for pads that do not set their own solderPasteMargin, ensuring correct paste margins are applied during PCB rendering. |
| [#5500](https://github.com/tscircuit/core/pull/5500) | 🐙 Minor | ⭐⭐ | Abse2001 | Changes the solder paste margin resolution for SMT pads to include the boards default solder paste margin if not specified, affecting paste size calculations for components. |
| [#5217](https://github.com/tscircuit/core/pull/5217) | 🐙 Minor | ⭐⭐ | Abse2001 | Implements V-scored panel tabs that replace mouse bites with score lines along the board edge for panels using tab-routing and vScore. |
| [#5214](https://github.com/tscircuit/core/pull/5214) | 🐙 Minor | ⭐⭐ | Abse2001 | Implements finished panel size limits that enforce minimum and maximum dimensions for panels, affecting layout and error reporting. |
| [#5211](https://github.com/tscircuit/core/pull/5211) | 🐙 Minor | ⭐⭐ | Abse2001 | Implements tooling rail elements only from issue 5067, allowing for the addition of a toolingrail component within a panel with specified dimensions and positioning constraints. |
| [#5208](https://github.com/tscircuit/core/pull/5208) | 🐙 Minor | ⭐⭐ | Abse2001 | Implements panel tab child elements only from issue 5067, allowing for better control of panel tab placements and interactions within the circuit design. |
| [#5216](https://github.com/tscircuit/core/pull/5216) | 🐙 Minor | ⭐⭐ | Abse2001 | Reproduces the V-scored panel tabs portion of issue 5067, ensuring correct rendering of V-score lines in the panel layout. |
| [#5205](https://github.com/tscircuit/core/pull/5205) | 🐙 Minor | ⭐⭐ | Abse2001 | Implements panel silkscreen functionality, allowing silkscreen text to be placed in the panel frame of the PCB design. |
| [#5202](https://github.com/tscircuit/core/pull/5202) | 🐙 Minor | ⭐⭐ | Abse2001 | Implements panel tooling holes and fiducials only from issue 5067, updating the SVG output and allowing these elements in panels and subpanels. |
| [#5340](https://github.com/tscircuit/core/pull/5340) | 🐙 Minor | ⭐⭐ | techmannih | Fixes the issue where plated-hole solder paste ownership is not correctly assigned during the rendering process, leading to incorrect KiCad exports. |

<details>
<summary>🐌 Tiny Contributions (51)</summary>

| PR # | Impact | Contributor | Description |
|------|--------|-------------|-------------|
| [#5374](https://github.com/tscircuit/core/pull/5374) | 🐌 Tiny | rushabhcodes | Reproduces a bug where raw remote solve and job requests lose copperpour unbroken intent before copper pours render, affecting signal routing on inner planes. |
| [#5501](https://github.com/tscircuit/core/pull/5501) | 🐌 Tiny | tscircuitbot | Updates the tscircuitchecks package from version 0.0.277 to 0.0.278 |
| [#5446](https://github.com/tscircuit/core/pull/5446) | 🐌 Tiny | tscircuitbot | Updates the version of the tscircuitchecks package from 0.0.276 to 0.0.277 in package.json |
| [#5432](https://github.com/tscircuit/core/pull/5432) | 🐌 Tiny | tscircuitbot | Updates the tscircuitchecks package to version 0.0.274 in package.json |
| [#5416](https://github.com/tscircuit/core/pull/5416) | 🐌 Tiny | tscircuitbot | Updates the version of the tscircuitfanout-solver package from 0.0.81 to 0.0.84 in package.json |
| [#5433](https://github.com/tscircuit/core/pull/5433) | 🐌 Tiny | tscircuitbot | Updates the version of the tscircuitchecks package from 0.0.273 to 0.0.274 in package.json |
| [#5436](https://github.com/tscircuit/core/pull/5436) | 🐌 Tiny | tscircuitbot | Updates the tscircuitchecks package from version 0.0.274 to 0.0.276 |
| [#5408](https://github.com/tscircuit/core/pull/5408) | 🐌 Tiny | MustafaMulla29 | Updates the tscircuitdogbone-solver CDN dependency from 0.0.2 to 0.0.4, addressing native dogbone escape blockers found with the STM32MP157DAB1 in the four-motor USB-PD motherboard. |
| [#5394](https://github.com/tscircuit/core/pull/5394) | 🐌 Tiny | MustafaMulla29 | Updates the tscircuitdogbone-solver dependency from version 0.0.1 to 0.0.2, which includes a fix for escape vias being incorrectly blocked by unbroken ground planes on other layers. |
| [#5587](https://github.com/tscircuit/core/pull/5587) | 🐌 Tiny | ShiboSoftwareDev | Bumps the tscircuitcapacity-autorouter package version from 0.0.1107 to 0.0.1109, incorporating indexed fixed-copper checks in DDR repair and earlier rejection of malformed differential-pair declarations. |
| [#5578](https://github.com/tscircuit/core/pull/5578) | 🐌 Tiny | ShiboSoftwareDev | Bumps the tscircuitcapacity-autorouter package from version 0.0.1106 to 0.0.1107, incorporating fixes for copper repair defaults and ensuring compatibility with ECP5s clearance rules. |
| [#5574](https://github.com/tscircuit/core/pull/5574) | 🐌 Tiny | ShiboSoftwareDev | Bumps the tscircuitcapacity-autorouter dependency from version 0.0.1104 to 0.0.1106, incorporating various fixes and improvements from upstream. |
| [#5568](https://github.com/tscircuit/core/pull/5568) | 🐌 Tiny | ShiboSoftwareDev | Bumps the versions of the autorouter and bus solver dependencies in the project. |
| [#5555](https://github.com/tscircuit/core/pull/5555) | 🐌 Tiny | ShiboSoftwareDev | Reproduces the ButterStick r1.0 power-input placement error with the native C165U18 footprints and connections, demonstrating that the overlap error stops autorouting. |
| [#5553](https://github.com/tscircuit/core/pull/5553) | 🐌 Tiny | ShiboSoftwareDev | Bumps the tscircuitcapacity-autorouter dependency from version 0.0.1102 to 0.0.1103, incorporating updates from upstream repositories and ensuring compatibility with existing tests. |
| [#5550](https://github.com/tscircuit/core/pull/5550) | 🐌 Tiny | ShiboSoftwareDev | Updates the circuit-json-to-spice package from version 0.0.45 to 0.0.47, incorporating a parseable spicemodel for parts SPICE output. |
| [#5528](https://github.com/tscircuit/core/pull/5528) | 🐌 Tiny | ShiboSoftwareDev | Reproduces a bug where bus routing fails due to an existing plated-hole passage being rejected by the autorouter. |
| [#5527](https://github.com/tscircuit/core/pull/5527) | 🐌 Tiny | ShiboSoftwareDev | Records current fanout boundary-planning failures in PCB snapshots without production code changes. |
| [#5548](https://github.com/tscircuit/core/pull/5548) | 🐌 Tiny | ShiboSoftwareDev | Updates the capacity-autorouter to version 0.0.1101 and the bus-lanes-solver to version 0.0.57, ensuring compatibility and performance improvements in routing and bus lane solving. |
| [#5536](https://github.com/tscircuit/core/pull/5536) | 🐌 Tiny | ShiboSoftwareDev | Bumps the tscircuitcapacity-autorouter dependency from version 0.0.1099 to 0.0.1100 to include the Repair02 pin and improve solver functionality. |
| [#5533](https://github.com/tscircuit/core/pull/5533) | 🐌 Tiny | ShiboSoftwareDev | Bumps the tscircuitcapacity-autorouter package version from 0.0.1097 to 0.0.1098 to enable staged routing repairs for clearance beside earlier copper. |
| [#5535](https://github.com/tscircuit/core/pull/5535) | 🐌 Tiny | ShiboSoftwareDev | Bumps the tscircuitcapacity-autorouter dependency from version 0.0.1098 to 0.0.1099 to retain clearance-projection progress when clearing prioritized Circuit JSON errors. |
| [#5521](https://github.com/tscircuit/core/pull/5521) | 🐌 Tiny | ShiboSoftwareDev | Updates the capacity-autorouter to version 0.0.1097 and the bus-lanes-solver to version 0.0.56, incorporating various bug fixes and improvements from the respective releases. |
| [#5494](https://github.com/tscircuit/core/pull/5494) | 🐌 Tiny | ShiboSoftwareDev | Bumps the tscircuitcapacity-autorouter dependency from 0.0.1093 to 0.0.1094 to include updates related to node repair and copper queries. |
| [#5482](https://github.com/tscircuit/core/pull/5482) | 🐌 Tiny | ShiboSoftwareDev | Bumps tscircuitcapacity-autorouter from 0.0.1088 to 0.0.1089 to include tscircuittscircuit-autorouter3765, allowing regional repair to use the boards explicit via-to-pad clearance for ECP5 repairs. |
| [#5480](https://github.com/tscircuit/core/pull/5480) | 🐌 Tiny | ShiboSoftwareDev | Bumps capacity-autorouter from 0.0.1087 to 0.0.1088 to honor the boards declared via-to-pad clearance during projection validation, allowing the native ECP5 DDR repair to retain legal moved vias on its 0.089 mm board instead of being rejected by the implicit 0.1 mm guard. |
| [#5487](https://github.com/tscircuit/core/pull/5487) | 🐌 Tiny | ShiboSoftwareDev | Bumps the tscircuitcapacity-autorouter dependency from 0.0.1092 to 0.0.1093 to include fixes for width regression and improvements in DDR routing. |
| [#5484](https://github.com/tscircuit/core/pull/5484) | 🐌 Tiny | ShiboSoftwareDev | Bumps tscircuitcapacity-autorouter from 0.0.1089 to 0.0.1090 to include fixes for routing issues with neighboring wire sections while preserving original DDR via connectivity. |
| [#5474](https://github.com/tscircuit/core/pull/5474) | 🐌 Tiny | ShiboSoftwareDev | Bumps capacity-autorouter from 0.0.1086 to 0.0.1087 to preserve valid inner-layer crossing positions when centering a solitary port would overlap preloaded DDR copper, including the merged H616 ZQ1 crossing fix from autorouter PR 3752. |
| [#5459](https://github.com/tscircuit/core/pull/5459) | 🐌 Tiny | ShiboSoftwareDev | Bumps the capacity-autorouter version from 0.0.1085 to 0.0.1086, incorporating three merged fixes related to BGA pitch estimation, DDR copper checks, and topology layer reuse. |
| [#5443](https://github.com/tscircuit/core/pull/5443) | 🐌 Tiny | ShiboSoftwareDev | Bumps the capacity-autorouter version from 0.0.1084 to 0.0.1085 to ensure validated gaps are represented in stitch paths and the native H616 C3 route reaches its bottom-layer terminal, while rejecting output that misses a tagged PCB terminal layer. |
| [#5441](https://github.com/tscircuit/core/pull/5441) | 🐌 Tiny | ShiboSoftwareDev | Pins the native DDR benchmark correction to ensure imported net membership no longer prescribes pad order while maintaining checks on all native terminals, geometry, rules, and phase assignments. |
| [#5427](https://github.com/tscircuit/core/pull/5427) | 🐌 Tiny | ShiboSoftwareDev | Updates the tscircuitcapacity-autorouter and tscircuitbus-lanes-solver dependencies to their latest versions, ensuring compatibility and incorporating recent improvements in routing and board tuning. |
| [#5398](https://github.com/tscircuit/core/pull/5398) | 🐌 Tiny | ShiboSoftwareDev | Bumps the tscircuitcapacity-autorouter dependency from version 0.0.1076 to 0.0.1077, ensuring safe H616 DDR repairs after restoring a colliding connection through the updated repair03 dependency. |
| [#5395](https://github.com/tscircuit/core/pull/5395) | 🐌 Tiny | ShiboSoftwareDev | Bumps tscircuitcapacity-autorouter from 0.0.1075 to 0.0.1076, including the DDR intersection fix from tscircuitmath-utils69. |
| [#5406](https://github.com/tscircuit/core/pull/5406) | 🐌 Tiny | ShiboSoftwareDev | Bumps the tscircuitcapacity-autorouter package from version 0.0.1077 to 0.0.1078, incorporating optimizations and fixes from previous pull requests. |
| [#5397](https://github.com/tscircuit/core/pull/5397) | 🐌 Tiny | ShiboSoftwareDev | Updates the bus-lanes-solver dependency from version 0.0.51 to 0.0.52, ensuring compatibility and incorporating recent fixes. |
| [#5396](https://github.com/tscircuit/core/pull/5396) | 🐌 Tiny | ShiboSoftwareDev | Pins math-utils to version 0.0.39 to resolve false overlap findings in the ButterStick contact checks. |
| [#5440](https://github.com/tscircuit/core/pull/5440) | 🐌 Tiny | ShiboSoftwareDev | Updates the capacity-autorouter and bus-lanes-solver packages to their latest versions, bringing in new features and fixes related to routing and connection paths. |
| [#5393](https://github.com/tscircuit/core/pull/5393) | 🐌 Tiny | ShiboSoftwareDev | Bumps tscircuitcapacity-autorouter from 0.0.1074 to 0.0.1075, improving DDR port spacing by reusing a node-ID index for ownership lookups instead of scanning the mesh repeatedly. |
| [#5499](https://github.com/tscircuit/core/pull/5499) | 🐌 Tiny | Abse2001 | Bumps tscircuitprops to 0.0.732, which adds board defaultSolderPasteMargin (tscircuitprops1011). No code changes; the board-margin repro and fix for 4800 build on this. |
| [#5213](https://github.com/tscircuit/core/pull/5213) | 🐌 Tiny | Abse2001 | Reproduces the finished panel size limits portion of issue 5067 by adding a test that verifies the grid layout constraints for panel size limits. |
| [#5210](https://github.com/tscircuit/core/pull/5210) | 🐌 Tiny | Abse2001 | Reproduces the tooling rail elements portion of a previous issue, ensuring the test renders correctly and captures the expected output. |
| [#5207](https://github.com/tscircuit/core/pull/5207) | 🐌 Tiny | Abse2001 | Reproduces the panel tab child elements portion of issue 5067, ensuring the test renders correctly and captures the expected output. |
| [#5204](https://github.com/tscircuit/core/pull/5204) | 🐌 Tiny | Abse2001 | Reproduces the panel silkscreen portion of issue 5067, ensuring the test renders correctly and captures the expected output. |
| [#5411](https://github.com/tscircuit/core/pull/5411) | 🐌 Tiny | Abse2001 | Updates tscircuitprops from 0.0.724 to published 0.0.728, in the development dependency and the existing matching override. |
| [#5201](https://github.com/tscircuit/core/pull/5201) | 🐌 Tiny | Abse2001 | Reproduces the panel tooling holes and fiducials portion of issue 5067, providing a test that captures the rendering error when the panel is rejected by Core. |
| [#5509](https://github.com/tscircuit/core/pull/5509) | 🐌 Tiny | KrishnaX12 | Reproduces a bug where the reference-divider wire doubles back through the resistor in a specific circuit schematic. |
| [#5543](https://github.com/tscircuit/core/pull/5543) | 🐌 Tiny | AnasSarkiz | Moves tscircuitcore-ddr-benchmark from 7b05251 to 24dc44c, updating the A13 fixtures clearance from 0.2 mm to 0.1249 mm without any core code changes. |
| [#5460](https://github.com/tscircuit/core/pull/5460) | 🐌 Tiny | GokulPandi-M | Updates the schematic-trace-solver dependency from version 0.0.238 to 0.0.246 to remove redundant terminal paths in generated schematics. |
| [#5342](https://github.com/tscircuit/core/pull/5342) | 🐌 Tiny | techmannih | Reproduces the routing behavior of a named-net by selecting a specific pin phase for autorouting, ensuring that only the designated pins are routed while deferring unrelated connections. |

</details>

### [tscircuit/circuit-to-svg](https://github.com/tscircuit/circuit-to-svg)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#932](https://github.com/tscircuit/circuit-to-svg/pull/932) | 🐳 Major | ⭐⭐⭐ | seveibar | Render expanded subcircuits with a dashed labeled frame and persistent public terminals. Read resolved group and port coordinates from Circuit JSON, draw each stem and square boundary marker, and place exported names outside the frame. Internal connections do not hide public terminals. Include frames and labels in automatic bounds, preserve sourcegroup IDs in SVG attributes, and respect schematic sheet selection. Existing groups without show_boundary and component-owned ports retain their rendering. Both visual tests use actual core output from the real ShiboSoftwareDev CC2340R5 reference design(https:tscircuit.comShiboSoftwareDevcc2340r5-reference-designcustomize?package_release_idbff7bbb1-c0df-4b3e-8cb2-5f5c706caa87preview_filedist2Findex2Fcircuit.jsonschematic), release bff7bbb1-c0df-4b3e-8cb2-5f5c706caa87. The fixture preserves all 27 components and 16 original nets, and adapts eight formerly unconnected GPIO pins into named module nets. It exports those eight GPIOs plus VDDS, GND, RESET_N, SWDIO and SWCLK: 13 terminals, each with a wire to its real MCU pin. RFantenna, clock, DCDCdecoupling, reset and debug circuitry remains intact. The core companion checks the published electrical signature plus this explicit addition and verifies every terminals wire path. Provenance and regeneration are documented; schematic geometry is not postprocessed. Schema 1004(https:github.comtscircuitcircuit-jsonpull1004) is merged and published in circuit-json0.0.549. This PR updates the devDependency to 0.0.549 and the Bun lockfile to that published version. Core companion 5445(https:github.comtscircuitcorepull5445) can follow once this renderer is published. Validation against the installed npm release circuit-json0.0.549 (no local schema link): all 485 tests pass, one existing todo; TypeScript check and build pass. Snapshots were visually inspected and rerun without update mode, covering all 13 terminals, automatic bounds and sheet selection. !CC2340R5 with 13 wired public terminals(https:raw.githubusercontent.comtscircuitcircuit-to-svgdecededtestssch__snapshots__expanded-group-boundary-ports.snap.svg) |
| [#936](https://github.com/tscircuit/circuit-to-svg/pull/936) | 🐙 Minor | ⭐⭐ | ShiboSoftwareDev | Fixes the issue where simulation SVGs did not contain full legends when label text extended beyond the canvas, ensuring legends are fully visible without altering plot coordinates or layout behavior. |

### [tscircuit/tscircuit.com](https://github.com/tscircuit/tscircuit.com)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#5910](https://github.com/tscircuit/tscircuit.com/pull/5910) | 🐳 Major | ⭐⭐⭐ | seveibar | Adds Windows download option for tscircuit-desktop on the desktop page and prepares for future Linux support by indicating availability once a build is released. |
| [#5898](https://github.com/tscircuit/tscircuit.com/pull/5898) | 🐳 Major | ⭐⭐⭐ | seveibar | Package maintainers can select chips under General settings to publish their package as a reference design. Settings reads selections from packageslist_datasheet_references and saves them through packagesupdate_datasheet_references. |
| [#5813](https://github.com/tscircuit/tscircuit.com/pull/5813) | 🐳 Major | ⭐⭐⭐ | seveibar | Adds a Customize link in the package About section for packages with a manifest, allowing users to navigate to the Customize page directly from the sidebar. |
| [#5812](https://github.com/tscircuit/tscircuit.com/pull/5812) | 🐳 Major | ⭐⭐⭐ | seveibar | Adds a new page for customizing package configurations, allowing users to interact with published configurations through controls generated from preview data. |
| [#5851](https://github.com/tscircuit/tscircuit.com/pull/5851) | 🐳 Major | ⭐⭐⭐ | seveibar | Adds a copyable, syntax-highlighted TSX usage example beneath the customization preview, using the selected variants parameters and the packages published default or named component export. |
| [#5815](https://github.com/tscircuit/tscircuit.com/pull/5815) | 🐳 Major | ⭐⭐⭐ | seveibar | Adds a Reference designs button to the datasheet header that links to the curated catalog of designs using the chip. |
| [#5811](https://github.com/tscircuit/tscircuit.com/pull/5811) | 🐳 Major | ⭐⭐⭐ | seveibar | Adds the data layer for packages whose build publishes distpreview.json, including hooks for loading manifests and managing package configurations. |
| [#5907](https://github.com/tscircuit/tscircuit.com/pull/5907) | 🐙 Minor | ⭐⭐ | seveibar | Fixes broken URL issue during sign-in redirect by ensuring the query string retains the leading ? character. |
| [#5814](https://github.com/tscircuit/tscircuit.com/pull/5814) | 🐙 Minor | ⭐⭐ | seveibar | Adds two new pages for displaying reference designs for specific chips, enhancing the datasheet functionality. |
| [#5810](https://github.com/tscircuit/tscircuit.com/pull/5810) | 🐙 Minor | ⭐⭐ | seveibar | Adds change tracking between two circuits, allowing the Customize page to identify which schematic parts a configuration switch added or changed. |
| [#5852](https://github.com/tscircuit/tscircuit.com/pull/5852) | 🐙 Minor | ⭐⭐ | seveibar | Moves the TSX usage panel into the shared PackageConfigurationPreview to ensure both the datasheet reference-design pages and the package customize page display copyable code for the selected configuration. |
| [#5834](https://github.com/tscircuit/tscircuit.com/pull/5834) | 🐙 Minor | ⭐⭐ | seveibar | Draws dashed outlines around changed schematic parts on the Customize and reference-design pages for three seconds using the schematic viewers new props. |
| [#5809](https://github.com/tscircuit/tscircuit.com/pull/5809) | 🐙 Minor | ⭐⭐ | seveibar | Adds PackagePreviewScope, an optional context that supplies the release, preview file, circuit JSON and GLB for an embedded preview, allowing hooks to resolve identity without a provider. |
| [#5808](https://github.com/tscircuit/tscircuit.com/pull/5808) | 🐙 Minor | ⭐⭐ | seveibar | Adds support for loading gzip-compressed Circuit JSON preview files, allowing package pages to preview large circuits efficiently. |

<details>
<summary>🐌 Tiny Contributions (128)</summary>

| PR # | Impact | Contributor | Description |
|------|--------|-------------|-------------|
| [#5897](https://github.com/tscircuit/tscircuit.com/pull/5897) | 🐌 Tiny | seveibar | Removes the note about the app not being signed by Apple from the desktop page, simplifying the message for users. |
| [#5891](https://github.com/tscircuit/tscircuit.com/pull/5891) | 🐌 Tiny | seveibar | Replaces the screenshot on desktop with a dark mode conversation interface alongside the PCB view of the rp2040-motor-controller. |
| [#5890](https://github.com/tscircuit/tscircuit.com/pull/5890) | 🐌 Tiny | seveibar | Adds a new page at desktop for the tscircuit Desktop app, providing information about the app, download options, and features. |
| [#5965](https://github.com/tscircuit/tscircuit.com/pull/5965) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1789 to 0.0.1790 |
| [#5964](https://github.com/tscircuit/tscircuit.com/pull/5964) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3261 to 0.0.3262 |
| [#5959](https://github.com/tscircuit/tscircuit.com/pull/5959) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3260 to 0.0.3261 |
| [#5958](https://github.com/tscircuit/tscircuit.com/pull/5958) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3259 to 0.0.3260 in package.json |
| [#5957](https://github.com/tscircuit/tscircuit.com/pull/5957) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1788 to 0.0.1789 |
| [#5953](https://github.com/tscircuit/tscircuit.com/pull/5953) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3258 to 0.0.3259 in package.json |
| [#5952](https://github.com/tscircuit/tscircuit.com/pull/5952) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1787 to 0.0.1788 |
| [#5951](https://github.com/tscircuit/tscircuit.com/pull/5951) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3257 to 0.0.3258 in package.json |
| [#5950](https://github.com/tscircuit/tscircuit.com/pull/5950) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1786 to 0.0.1787 |
| [#5949](https://github.com/tscircuit/tscircuit.com/pull/5949) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3256 to 0.0.3257 |
| [#5948](https://github.com/tscircuit/tscircuit.com/pull/5948) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package version from 0.0.1785 to 0.0.1786 in package.json |
| [#5947](https://github.com/tscircuit/tscircuit.com/pull/5947) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3255 to 0.0.3256 in package.json |
| [#5946](https://github.com/tscircuit/tscircuit.com/pull/5946) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1784 to 0.0.1785 |
| [#5945](https://github.com/tscircuit/tscircuit.com/pull/5945) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3254 to 0.0.3255 |
| [#5944](https://github.com/tscircuit/tscircuit.com/pull/5944) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3253 to 0.0.3254 |
| [#5943](https://github.com/tscircuit/tscircuit.com/pull/5943) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5942](https://github.com/tscircuit/tscircuit.com/pull/5942) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1782 to 0.0.1783 |
| [#5941](https://github.com/tscircuit/tscircuit.com/pull/5941) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3252 to 0.0.3253 |
| [#5940](https://github.com/tscircuit/tscircuit.com/pull/5940) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3251 to 0.0.3252 |
| [#5939](https://github.com/tscircuit/tscircuit.com/pull/5939) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5938](https://github.com/tscircuit/tscircuit.com/pull/5938) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3250 to 0.0.3251 in package.json |
| [#5937](https://github.com/tscircuit/tscircuit.com/pull/5937) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1780 to 0.0.1781 |
| [#5936](https://github.com/tscircuit/tscircuit.com/pull/5936) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3249 to 0.0.3250 |
| [#5935](https://github.com/tscircuit/tscircuit.com/pull/5935) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package version from 0.0.1779 to 0.0.1780 in package.json |
| [#5934](https://github.com/tscircuit/tscircuit.com/pull/5934) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3248 to 0.0.3249 |
| [#5933](https://github.com/tscircuit/tscircuit.com/pull/5933) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1778 to 0.0.1779 |
| [#5919](https://github.com/tscircuit/tscircuit.com/pull/5919) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1776 to 0.0.1777 |
| [#5920](https://github.com/tscircuit/tscircuit.com/pull/5920) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3246 to 0.0.3247 in package.json |
| [#5904](https://github.com/tscircuit/tscircuit.com/pull/5904) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3237 to 0.0.3239 in package.json |
| [#5903](https://github.com/tscircuit/tscircuit.com/pull/5903) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1771 to 0.0.1772 |
| [#5901](https://github.com/tscircuit/tscircuit.com/pull/5901) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package version from 0.0.1770 to 0.0.1771 in package.json |
| [#5922](https://github.com/tscircuit/tscircuit.com/pull/5922) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3247 to 0.0.3248 |
| [#5921](https://github.com/tscircuit/tscircuit.com/pull/5921) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1777 to 0.0.1778 |
| [#5918](https://github.com/tscircuit/tscircuit.com/pull/5918) | 🐌 Tiny | tscircuitbot | Updates the version of the tscircuitrunframe package from 0.0.3245 to 0.0.3246 in the package.json file. |
| [#5917](https://github.com/tscircuit/tscircuit.com/pull/5917) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1775 to 0.0.1776 |
| [#5916](https://github.com/tscircuit/tscircuit.com/pull/5916) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3244 to 0.0.3245 |
| [#5915](https://github.com/tscircuit/tscircuit.com/pull/5915) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3243 to 0.0.3244 in the package.json file. |
| [#5914](https://github.com/tscircuit/tscircuit.com/pull/5914) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1774 to 0.0.1775 in the package.json file. |
| [#5913](https://github.com/tscircuit/tscircuit.com/pull/5913) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5912](https://github.com/tscircuit/tscircuit.com/pull/5912) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1773 to 0.0.1774 |
| [#5911](https://github.com/tscircuit/tscircuit.com/pull/5911) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3241 to 0.0.3242 |
| [#5909](https://github.com/tscircuit/tscircuit.com/pull/5909) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3240 to 0.0.3241 |
| [#5906](https://github.com/tscircuit/tscircuit.com/pull/5906) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1772 to 0.0.1773 |
| [#5905](https://github.com/tscircuit/tscircuit.com/pull/5905) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3239 to 0.0.3240 |
| [#5902](https://github.com/tscircuit/tscircuit.com/pull/5902) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3236 to 0.0.3237 |
| [#5900](https://github.com/tscircuit/tscircuit.com/pull/5900) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3235 to 0.0.3236 |
| [#5899](https://github.com/tscircuit/tscircuit.com/pull/5899) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1769 to 0.0.1770 |
| [#5908](https://github.com/tscircuit/tscircuit.com/pull/5908) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5896](https://github.com/tscircuit/tscircuit.com/pull/5896) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3234 to 0.0.3235 |
| [#5894](https://github.com/tscircuit/tscircuit.com/pull/5894) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package version from 0.0.1768 to 0.0.1769 in package.json |
| [#5893](https://github.com/tscircuit/tscircuit.com/pull/5893) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3232 to 0.0.3233 |
| [#5892](https://github.com/tscircuit/tscircuit.com/pull/5892) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5889](https://github.com/tscircuit/tscircuit.com/pull/5889) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5888](https://github.com/tscircuit/tscircuit.com/pull/5888) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1766 to 0.0.1767 |
| [#5887](https://github.com/tscircuit/tscircuit.com/pull/5887) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3230 to 0.0.3231 |
| [#5886](https://github.com/tscircuit/tscircuit.com/pull/5886) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3229 to 0.0.3230 |
| [#5885](https://github.com/tscircuit/tscircuit.com/pull/5885) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1765 to 0.0.1766 |
| [#5884](https://github.com/tscircuit/tscircuit.com/pull/5884) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3228 to 0.0.3229 in package.json |
| [#5883](https://github.com/tscircuit/tscircuit.com/pull/5883) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1764 to 0.0.1765 |
| [#5882](https://github.com/tscircuit/tscircuit.com/pull/5882) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3227 to 0.0.3228 |
| [#5881](https://github.com/tscircuit/tscircuit.com/pull/5881) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1763 to 0.0.1764 |
| [#5880](https://github.com/tscircuit/tscircuit.com/pull/5880) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3226 to 0.0.3227 |
| [#5879](https://github.com/tscircuit/tscircuit.com/pull/5879) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package version from 0.0.1762 to 0.0.1763 in package.json |
| [#5878](https://github.com/tscircuit/tscircuit.com/pull/5878) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3225 to 0.0.3226 in package.json |
| [#5877](https://github.com/tscircuit/tscircuit.com/pull/5877) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1761 to 0.0.1762 |
| [#5876](https://github.com/tscircuit/tscircuit.com/pull/5876) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3224 to 0.0.3225 |
| [#5875](https://github.com/tscircuit/tscircuit.com/pull/5875) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1760 to 0.0.1761 in the package.json file. |
| [#5895](https://github.com/tscircuit/tscircuit.com/pull/5895) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3233 to 0.0.3234 |
| [#5869](https://github.com/tscircuit/tscircuit.com/pull/5869) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1757 to 0.0.1758 |
| [#5866](https://github.com/tscircuit/tscircuit.com/pull/5866) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3219 to 0.0.3220 |
| [#5861](https://github.com/tscircuit/tscircuit.com/pull/5861) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3216 to 0.0.3218 |
| [#5829](https://github.com/tscircuit/tscircuit.com/pull/5829) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1741 to 0.0.1742 |
| [#5816](https://github.com/tscircuit/tscircuit.com/pull/5816) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1735 to 0.0.1736 |
| [#5864](https://github.com/tscircuit/tscircuit.com/pull/5864) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3218 to 0.0.3219 in package.json |
| [#5822](https://github.com/tscircuit/tscircuit.com/pull/5822) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1738 to 0.0.1739 |
| [#5818](https://github.com/tscircuit/tscircuit.com/pull/5818) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package version from 0.0.1736 to 0.0.1737 in package.json |
| [#5873](https://github.com/tscircuit/tscircuit.com/pull/5873) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package version from 0.0.1759 to 0.0.1760 in package.json |
| [#5872](https://github.com/tscircuit/tscircuit.com/pull/5872) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3222 to 0.0.3223 |
| [#5870](https://github.com/tscircuit/tscircuit.com/pull/5870) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3221 to 0.0.3222 |
| [#5867](https://github.com/tscircuit/tscircuit.com/pull/5867) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1756 to 0.0.1757 |
| [#5860](https://github.com/tscircuit/tscircuit.com/pull/5860) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1753 to 0.0.1754 |
| [#5857](https://github.com/tscircuit/tscircuit.com/pull/5857) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3215 to 0.0.3216 |
| [#5856](https://github.com/tscircuit/tscircuit.com/pull/5856) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1751 to 0.0.1752 |
| [#5854](https://github.com/tscircuit/tscircuit.com/pull/5854) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package version from 0.0.1750 to 0.0.1751 in package.json |
| [#5849](https://github.com/tscircuit/tscircuit.com/pull/5849) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package version from 0.0.1749 to 0.0.1750 in package.json |
| [#5848](https://github.com/tscircuit/tscircuit.com/pull/5848) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3212 to 0.0.3213 |
| [#5846](https://github.com/tscircuit/tscircuit.com/pull/5846) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5845](https://github.com/tscircuit/tscircuit.com/pull/5845) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1747 to 0.0.1748 in the package.json file. |
| [#5844](https://github.com/tscircuit/tscircuit.com/pull/5844) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3210 to 0.0.3211 |
| [#5843](https://github.com/tscircuit/tscircuit.com/pull/5843) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1746 to 0.0.1747 |
| [#5842](https://github.com/tscircuit/tscircuit.com/pull/5842) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3209 to 0.0.3210 |
| [#5840](https://github.com/tscircuit/tscircuit.com/pull/5840) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3208 to 0.0.3209 |
| [#5832](https://github.com/tscircuit/tscircuit.com/pull/5832) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3205 to 0.0.3206 |
| [#5830](https://github.com/tscircuit/tscircuit.com/pull/5830) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3204 to 0.0.3205 |
| [#5828](https://github.com/tscircuit/tscircuit.com/pull/5828) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3203 to 0.0.3204 |
| [#5825](https://github.com/tscircuit/tscircuit.com/pull/5825) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3201 to 0.0.3202 |
| [#5824](https://github.com/tscircuit/tscircuit.com/pull/5824) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1739 to 0.0.1740 |
| [#5817](https://github.com/tscircuit/tscircuit.com/pull/5817) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3197 to 0.0.3198 |
| [#5806](https://github.com/tscircuit/tscircuit.com/pull/5806) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1734 to 0.0.1735 in the package.json file. |
| [#5874](https://github.com/tscircuit/tscircuit.com/pull/5874) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3223 to 0.0.3224 |
| [#5871](https://github.com/tscircuit/tscircuit.com/pull/5871) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5868](https://github.com/tscircuit/tscircuit.com/pull/5868) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3220 to 0.0.3221 |
| [#5865](https://github.com/tscircuit/tscircuit.com/pull/5865) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1755 to 0.0.1756 |
| [#5863](https://github.com/tscircuit/tscircuit.com/pull/5863) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1754 to 0.0.1755 |
| [#5859](https://github.com/tscircuit/tscircuit.com/pull/5859) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1752 to 0.0.1753 |
| [#5850](https://github.com/tscircuit/tscircuit.com/pull/5850) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3213 to 0.0.3214 |
| [#5847](https://github.com/tscircuit/tscircuit.com/pull/5847) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1748 to 0.0.1749 |
| [#5841](https://github.com/tscircuit/tscircuit.com/pull/5841) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1745 to 0.0.1746 |
| [#5836](https://github.com/tscircuit/tscircuit.com/pull/5836) | 🐌 Tiny | tscircuitbot | Automated package update to version 0.0.227 |
| [#5831](https://github.com/tscircuit/tscircuit.com/pull/5831) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5827](https://github.com/tscircuit/tscircuit.com/pull/5827) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package version from 0.0.1740 to 0.0.1741 in package.json |
| [#5823](https://github.com/tscircuit/tscircuit.com/pull/5823) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3200 to 0.0.3201 in package.json |
| [#5821](https://github.com/tscircuit/tscircuit.com/pull/5821) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3199 to 0.0.3200 in package.json |
| [#5819](https://github.com/tscircuit/tscircuit.com/pull/5819) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3198 to 0.0.3199 |
| [#5803](https://github.com/tscircuit/tscircuit.com/pull/5803) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1733 to 0.0.1734 |
| [#5802](https://github.com/tscircuit/tscircuit.com/pull/5802) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3194 to 0.0.3195 |
| [#5855](https://github.com/tscircuit/tscircuit.com/pull/5855) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3214 to 0.0.3215 |
| [#5839](https://github.com/tscircuit/tscircuit.com/pull/5839) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package version from 0.0.1744 to 0.0.1745 in package.json |
| [#5820](https://github.com/tscircuit/tscircuit.com/pull/5820) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1737 to 0.0.1738 |
| [#5804](https://github.com/tscircuit/tscircuit.com/pull/5804) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3195 to 0.0.3196 in package.json |
| [#5838](https://github.com/tscircuit/tscircuit.com/pull/5838) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3207 to 0.0.3208 and the tscircuitschematic-viewer package from version 2.0.108 to 2.0.109 |
| [#5837](https://github.com/tscircuit/tscircuit.com/pull/5837) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1743 to 0.0.1744 and the tscircuitschematic-viewer package from version 2.0.110 to 2.0.108 in package.json |
| [#5835](https://github.com/tscircuit/tscircuit.com/pull/5835) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5807](https://github.com/tscircuit/tscircuit.com/pull/5807) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3196 to 0.0.3197 |
| [#5826](https://github.com/tscircuit/tscircuit.com/pull/5826) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3202 to 0.0.3203 |

</details>

### [tscircuit/jlcsearch](https://github.com/tscircuit/jlcsearch)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#643](https://github.com/tscircuit/jlcsearch/pull/643) | 🐳 Major | ⭐⭐⭐ | seveibar | Serve the last good copy when D1 fails, optimize cache key handling, and improve query efficiency with new indexes for resistors and capacitors. |
| [#637](https://github.com/tscircuit/jlcsearch/pull/637) | 🐳 Major | ⭐⭐⭐ | seveibar | Adds a Buzzers link on the home page and buzzerslist with package, Basic, and Preferred filters, and exposes the same results through the API at buzzerslist.json. |
| [#646](https://github.com/tscircuit/jlcsearch/pull/646) | 🐳 Major | ⭐⭐⭐ | imrishabh18 | Stock cleanup can scan almost the entire catalog to find unverified quantities, even when nothing needs clearing. This keeps the shared database busy and can make website requests queue up. |
| [#647](https://github.com/tscircuit/jlcsearch/pull/647) | 🐳 Major | ⭐⭐⭐ | imrishabh18 | This reduces repeated work in text searches by replacing LIKE checks on the FTS table with MATCH. The old query already used the text index; the improvement avoids extra reads and checks of the text stored in that index. Catalog matching, aliases and stock ordering remain. No index rebuild is needed. It also bounds expensive requests and handles invalid input consistently: Result limits must be 11,000 (default 100), and search text is limited to 256 characters. limit-1 no longer allows unlimited results. Searches need a term the index can use. DC, IC and 8MHz alone return 400 with examples such as dc connector, IC amplifier and 8MHz crystal. Adding another term preserves the existing 8MHz8M matching. Exact lookups such as C1 still work. Repeated parameters consistently use the last value for validation, caching, exact-part lookups and execution. This fixes the 500 from limit100limit1001. NUL characters (00) return 400 before database access, preventing an FTS parser error. The compatibility changes and error responses are documented in Search API input rules. Validation: 585 local tests passed (91 skipped), 57 Cloudflare simulator tests passed, and both TypeScript checks passed. Regression tests cover the reported errors, duplicate parameters, cache behavior, exact-part requests and index recovery. All testing used local data. Production data and settings were not changed. Broad searches can still read and sort many matches; local results do not establish production latency savings. |
| [#649](https://github.com/tscircuit/jlcsearch/pull/649) | 🐳 Major | ⭐⭐⭐ | imrishabh18 | Enables logging for a 10 sample of requests to track route timing, cache results, slow database queries, and database errors, improving visibility for diagnosing D1 overloads without reducing database load. |
| [#642](https://github.com/tscircuit/jlcsearch/pull/642) | 🐳 Major | ⭐⭐⭐ | imrishabh18 | This PR changes the search index rebuild process to retain completed entries, repair only missing or changed parts, and remove obsolete index entries in small batches, improving efficiency and reliability during rebuilds. |
| [#641](https://github.com/tscircuit/jlcsearch/pull/641) | 🐙 Minor | ⭐⭐ | imrishabh18 | When the search index is unavailable, text searches currently scan the full catalog and compete with the rebuild for database resources. This change keeps serving usable cached results, including when a forced refresh cannot run. Uncached text searches return a clear 503 response with a 60-second retry hint instead of scanning the catalog. Exact LCSC lookups and browsing still work, and text searches resume automatically once the rebuilt index is marked ready. Existing cache expiry stays the same. |
| [#640](https://github.com/tscircuit/jlcsearch/pull/640) | 🐙 Minor | ⭐⭐ | imrishabh18 | Changes the search index initialization process to avoid reliance on Cloudflares bulk-import service by using the normal query API instead. |
| [#635](https://github.com/tscircuit/jlcsearch/pull/635) | 🐙 Minor | ⭐⭐ | imrishabh18 | Fixes JSON output handling in stock-sync job by separating successful and failed JSON attempts, ensuring valid JSON is returned to the stock job. |
| [#638](https://github.com/tscircuit/jlcsearch/pull/638) | 🐙 Minor | ⭐⭐ | imrishabh18 | Adds a manual GitHub Action to rebuild only the search index, without changing the component catalogue or stock. |
| [#636](https://github.com/tscircuit/jlcsearch/pull/636) | 🐙 Minor | ⭐⭐ | imrishabh18 | Caches dropdown values for resistor and capacitor pages to reduce load by skipping dropdown queries for JSON requests and caching HTML dropdown values for 15 minutes. |
| [#632](https://github.com/tscircuit/jlcsearch/pull/632) | 🐙 Minor | ⭐⭐ | Abse2001 | Adds is_standard_only to the verified component that exact-part lookups return, indicating whether a part is marked as Standard only by JLCPCB, which affects the assembly service selection for PCBA. |

<details>
<summary>🐌 Tiny Contributions (1)</summary>

| PR # | Impact | Contributor | Description |
|------|--------|-------------|-------------|
| [#639](https://github.com/tscircuit/jlcsearch/pull/639) | 🐌 Tiny | imrishabh18 | Prevents queued search-index rebuilds from being cancelled when a scheduled inventory refresh replaces them in the waiting queue by adding GitHubs queue: max setting to workflows sharing the production database queue. |

</details>

### [tscircuit/runframe](https://github.com/tscircuit/runframe)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#6303](https://github.com/tscircuit/runframe/pull/6303) | 🐳 Major | ⭐⭐⭐ | seveibar | The 3D tab now mounts on first selection and stays mounted, hidden, while another tab is selected, preventing slow rebuilds of the scene on subsequent visits. |

<details>
<summary>🐌 Tiny Contributions (138)</summary>

| PR # | Impact | Contributor | Description |
|------|--------|-------------|-------------|
| [#6289](https://github.com/tscircuit/runframe/pull/6289) | 🐌 Tiny | seveibar | tscircuit desktop frames RunFrame and is getting its own view tabs (Source, PCB, Schematic, 3D, System, Assembly) in the apps style. For that the page around RunFrame needs three things RunFrame did not offer: remove RunFrames header, choose the tab from outside, and know what a circuit contains. The app also wants to frame the RunFrame that the tscircuit package ships, in place of runframe.tscircuit.comiframe.html, so the standalone bundle learns to take its props the same way. |
| [#6290](https://github.com/tscircuit/runframe/pull/6290) | 🐌 Tiny | seveibar | The publish workflow failed on the merge of 6289, so that change is not on npm yet: run(https:github.comtscircuitrunframeactionsruns43563166003).  Cannot pull with rebase due to unstaged changes in the following files: libhooksstyles.generated.ts  6289 added the class roletabpanel:!rf-mt-0. Tailwind emits two rules for it, the variant and a plain .!rf-mt-0. The styles.generated.ts I committed in that PR had only the first, so bun run build in the workflow rewrote the file and pver release refused to continue with a modified tree. This PR is the file exactly as bun run build:css writes it on main: one rule added, nothing removed. Running the build a second time leaves it unchanged. Until this is merged, every publish from main fails the same way. |
| [#6322](https://github.com/tscircuit/runframe/pull/6322) | 🐌 Tiny | rushabhcodes | Bumps tscircuitpcb-viewer from 1.11.451 to 1.11.452, incorporating WebGPU renderer 0.0.21 to maintain visibility of traces when copper pours are hidden. |
| [#6370](https://github.com/tscircuit/runframe/pull/6370) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6369](https://github.com/tscircuit/runframe/pull/6369) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1789 to 0.0.1790 |
| [#6368](https://github.com/tscircuit/runframe/pull/6368) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6367](https://github.com/tscircuit/runframe/pull/6367) | 🐌 Tiny | tscircuitbot | Updates the circuit-json-to-kicad package version from 0.0.277 to 0.0.278 in package.json |
| [#6364](https://github.com/tscircuit/runframe/pull/6364) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6363](https://github.com/tscircuit/runframe/pull/6363) | 🐌 Tiny | tscircuitbot | Updates the circuit-json-to-kicad package version from 0.0.276 to 0.0.277 in package.json |
| [#6361](https://github.com/tscircuit/runframe/pull/6361) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6360](https://github.com/tscircuit/runframe/pull/6360) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1788 to 0.0.1789 |
| [#6359](https://github.com/tscircuit/runframe/pull/6359) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6358](https://github.com/tscircuit/runframe/pull/6358) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1787 to 0.0.1788 |
| [#6357](https://github.com/tscircuit/runframe/pull/6357) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6356](https://github.com/tscircuit/runframe/pull/6356) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1786 to 0.0.1787 |
| [#6354](https://github.com/tscircuit/runframe/pull/6354) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6353](https://github.com/tscircuit/runframe/pull/6353) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1785 to 0.0.1786 |
| [#6352](https://github.com/tscircuit/runframe/pull/6352) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6351](https://github.com/tscircuit/runframe/pull/6351) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1784 to 0.0.1785 |
| [#6350](https://github.com/tscircuit/runframe/pull/6350) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6349](https://github.com/tscircuit/runframe/pull/6349) | 🐌 Tiny | tscircuitbot | Updates the circuit-json-to-kicad package version from 0.0.275 to 0.0.276 |
| [#6347](https://github.com/tscircuit/runframe/pull/6347) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6346](https://github.com/tscircuit/runframe/pull/6346) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1783 to 0.0.1784 in the package.json file. |
| [#6345](https://github.com/tscircuit/runframe/pull/6345) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6343](https://github.com/tscircuit/runframe/pull/6343) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6342](https://github.com/tscircuit/runframe/pull/6342) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1781 to 0.0.1783 in the package.json file. |
| [#6340](https://github.com/tscircuit/runframe/pull/6340) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6339](https://github.com/tscircuit/runframe/pull/6339) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1780 to 0.0.1781 |
| [#6337](https://github.com/tscircuit/runframe/pull/6337) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6336](https://github.com/tscircuit/runframe/pull/6336) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1779 to 0.0.1780 |
| [#6335](https://github.com/tscircuit/runframe/pull/6335) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6334](https://github.com/tscircuit/runframe/pull/6334) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1778 to 0.0.1779 |
| [#6327](https://github.com/tscircuit/runframe/pull/6327) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6316](https://github.com/tscircuit/runframe/pull/6316) | 🐌 Tiny | tscircuitbot | Updates the tscircuit3d-viewer package to version 0.0.651 in package.json |
| [#6311](https://github.com/tscircuit/runframe/pull/6311) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1772 to 0.0.1773 |
| [#6306](https://github.com/tscircuit/runframe/pull/6306) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1770 to 0.0.1771 |
| [#6305](https://github.com/tscircuit/runframe/pull/6305) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6330](https://github.com/tscircuit/runframe/pull/6330) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6329](https://github.com/tscircuit/runframe/pull/6329) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1777 to 0.0.1778 |
| [#6326](https://github.com/tscircuit/runframe/pull/6326) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1776 to 0.0.1777 in the package.json file. |
| [#6325](https://github.com/tscircuit/runframe/pull/6325) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6324](https://github.com/tscircuit/runframe/pull/6324) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1775 to 0.0.1776 in the package.json file. |
| [#6323](https://github.com/tscircuit/runframe/pull/6323) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6321](https://github.com/tscircuit/runframe/pull/6321) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6319](https://github.com/tscircuit/runframe/pull/6319) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6318](https://github.com/tscircuit/runframe/pull/6318) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1773 to 0.0.1774 |
| [#6317](https://github.com/tscircuit/runframe/pull/6317) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6315](https://github.com/tscircuit/runframe/pull/6315) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6314](https://github.com/tscircuit/runframe/pull/6314) | 🐌 Tiny | tscircuitbot | Updates the circuit-json-to-kicad package version from 0.0.272 to 0.0.275 in package.json |
| [#6312](https://github.com/tscircuit/runframe/pull/6312) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6310](https://github.com/tscircuit/runframe/pull/6310) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6309](https://github.com/tscircuit/runframe/pull/6309) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1771 to 0.0.1772 |
| [#6307](https://github.com/tscircuit/runframe/pull/6307) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6304](https://github.com/tscircuit/runframe/pull/6304) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1769 to 0.0.1770 |
| [#6302](https://github.com/tscircuit/runframe/pull/6302) | 🐌 Tiny | tscircuitbot | Updates the tscircuitpcb-viewer package to version 1.11.451 |
| [#6320](https://github.com/tscircuit/runframe/pull/6320) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1774 to 0.0.1775 |
| [#6279](https://github.com/tscircuit/runframe/pull/6279) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1762 to 0.0.1763 |
| [#6301](https://github.com/tscircuit/runframe/pull/6301) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6300](https://github.com/tscircuit/runframe/pull/6300) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6299](https://github.com/tscircuit/runframe/pull/6299) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6298](https://github.com/tscircuit/runframe/pull/6298) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1768 to 0.0.1769 |
| [#6297](https://github.com/tscircuit/runframe/pull/6297) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6296](https://github.com/tscircuit/runframe/pull/6296) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1767 to 0.0.1768 |
| [#6295](https://github.com/tscircuit/runframe/pull/6295) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6294](https://github.com/tscircuit/runframe/pull/6294) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1766 to 0.0.1767 |
| [#6291](https://github.com/tscircuit/runframe/pull/6291) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6288](https://github.com/tscircuit/runframe/pull/6288) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6287](https://github.com/tscircuit/runframe/pull/6287) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1765 to 0.0.1766 |
| [#6286](https://github.com/tscircuit/runframe/pull/6286) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6285](https://github.com/tscircuit/runframe/pull/6285) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1764 to 0.0.1765 |
| [#6282](https://github.com/tscircuit/runframe/pull/6282) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6281](https://github.com/tscircuit/runframe/pull/6281) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1763 to 0.0.1764 in the package.json file. |
| [#6280](https://github.com/tscircuit/runframe/pull/6280) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6277](https://github.com/tscircuit/runframe/pull/6277) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1761 to 0.0.1762 in the package.json file. |
| [#6276](https://github.com/tscircuit/runframe/pull/6276) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6275](https://github.com/tscircuit/runframe/pull/6275) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1760 to 0.0.1761 in the package.json file. |
| [#6278](https://github.com/tscircuit/runframe/pull/6278) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6271](https://github.com/tscircuit/runframe/pull/6271) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1758 to 0.0.1759 in the package.json file. |
| [#6269](https://github.com/tscircuit/runframe/pull/6269) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1757 to 