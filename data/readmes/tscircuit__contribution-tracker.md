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

# Contribution Overview 2026-11-03

The current week is shown below. There are 3 major sections:

- [Contributor Overview](#contributor-overview)
- [PRs by Repository](#prs-by-repository)
- [PRs by Contributor](#changes-by-contributor)
- [Scoring & Sponsorship Details](/docs/sponsorship-calculation-explanation.md)

## PRs by Repository

```mermaid
pie
    "tscircuit/pcb-viewer" : 16
    "tscircuit/3d-viewer" : 6
    "tscircuit/core" : 47
    "tscircuit/tscircuit-autorouter" : 66
    "tscircuit/tiny-hypergraph" : 1
    "tscircuit/high-density-repair01" : 4
    "tscircuit/high-density-repair03" : 7
    "tscircuit/bus-lanes-solver" : 16
    "tscircuit/circuit-json-webgpu" : 3
    "tscircuit/schematic-viewer" : 2
    "tscircuit/tscircuit" : 98
    "tscircuit/runframe" : 62
    "tscircuit/circuit-json" : 14
    "tscircuit/tscircuit.com" : 29
    "tscircuit/eval" : 27
    "tscircuit/cli" : 28
    "tscircuit/svg.tscircuit.com" : 43
    "tscircuit/circuit-json-to-step" : 3
    "tscircuit/schematic-trace-solver" : 5
    "tscircuit/copper-pour-solver" : 3
    "tscircuit/test-github-automerge" : 2
    "tscircuit/circuit-json-to-kicad" : 15
    "tscircuit/circuit-json-schematic-placement-analysis" : 24
    "tscircuit/drawing-viewer" : 7
    "tscircuit/circuit-json-to-pnp-csv" : 3
    "tscircuit/repair04" : 1
    "tscircuit/trace-simplification-solver" : 2
    "tscircuit/tscircuit-standalone" : 7
    "tscircuit/docs" : 9
    "tscircuit/circuit-json-to-altium" : 1
    "tscircuit/signal-integrity-pipeline" : 13
    "tscircuit/props" : 5
    "tscircuit/circuit-json-to-bom-csv" : 1
    "tscircuit/jlcsearch" : 3
    "tscircuit/motorcontrol" : 2
    "tscircuit/system-block-viewer" : 4
    "tscircuit/circuit-to-svg" : 2
    "tscircuit/tscircuit.com-landing" : 3
    "tscircuit/jscad-electronics" : 1
    "tscircuit/circuit-json-to-gltf" : 1
    "tscircuit/modelprinter" : 1
    "tscircuit/parts-engine" : 1
    "tscircuit/easyeda-converter" : 2
    "tscircuit/kicad-mod-cache" : 1
    "tscircuit/contribution-tracker" : 1
    "tscircuit/power-trace-expander" : 1
    "tscircuit/circuit-json-util" : 3
```

## Contributor Overview

| Contributor | 🐳 Major | 🐙 Minor | 🐌 Tiny | Score | ⭐ |
|-------------|---------|---------|---------|-------|-----|
| [ShiboSoftwareDev](#ShiboSoftwareDev) | 43 | 5 | 35 | 199 | 👑👑👑 |
| [seveibar](#seveibar) | 32 | 12 | 25 | 165 | 👑👑👑 |
| [0hmX](#0hmX) | 6 | 9 | 8 | 51 | ⭐⭐⭐ |
| [imrishabh18](#imrishabh18) | 7 | 3 | 13 | 47 | ⭐⭐ |
| [MustafaMulla29](#MustafaMulla29) | 5 | 6 | 20 | 45 | ⭐⭐ |
| [Abse2001](#Abse2001) | 2 | 7 | 8 | 39 | ⭐⭐ |
| [techmannih](#techmannih) | 5 | 0 | 6 | 26 | ⭐⭐ |
| [AnasSarkiz](#AnasSarkiz) | 5 | 1 | 4 | 26 | ⭐⭐ |
| [rushabhcodes](#rushabhcodes) | 3 | 1 | 6 | 20 | ⭐⭐ |
| [tscircuitbot](#tscircuitbot) | 0 | 0 | 307 | 12 | ⭐⭐ |
| [mohan-bee](#mohan-bee) | 2 | 1 | 2 | 12 | ⭐⭐ |
| [GokulPandi-M](#GokulPandi-M) | 2 | 1 | 0 | 10 | ⭐ |
| [abdalraof-albarbar](#abdalraof-albarbar) | 1 | 1 | 1 | 7 | ⭐ |
| [danielshawellis](#danielshawellis) | 0 | 0 | 1 | 1 |  |

## Staff Pass Ratio (SPR)

| Contributor | Reviewed PRs | Rejections | Approvals | SPR |
|-------------|--------------|------------|-----------|-----|
| [ShiboSoftwareDev](#ShiboSoftwareDev) | 18 | 0 | 18 | 100.0% |
| [Abse2001](#Abse2001) | 7 | 0 | 7 | 100.0% |
| [techmannih](#techmannih) | 5 | 0 | 5 | 100.0% |
| [GokulPandi-M](#GokulPandi-M) | 4 | 1 | 3 | 75.0% |
| [AnasSarkiz](#AnasSarkiz) | 3 | 0 | 3 | 100.0% |
| [imrishabh18](#imrishabh18) | 3 | 0 | 3 | 100.0% |
| [mohan-bee](#mohan-bee) | 3 | 1 | 3 | 66.7% |
| [0hmX](#0hmX) | 2 | 0 | 2 | 100.0% |
| [rushabhcodes](#rushabhcodes) | 2 | 1 | 2 | 50.0% |
| [abdalraof-albarbar](#abdalraof-albarbar) | 1 | 0 | 1 | 100.0% |

<details>
<summary>ShiboSoftwareDev SPR PRs (18)</summary>

- [#308](https://github.com/tscircuit/schematic-viewer/pull/308) Fit schematics to the selected sheet frame
- [#1163](https://github.com/tscircuit/pcb-viewer/pull/1163) Speed up WebGPU copper pours by updating Earcut
- [#1095](https://github.com/tscircuit/3d-viewer/pull/1095) Release the 3D canvas WebGL context on teardown
- [#3555](https://github.com/tscircuit/tscircuit-autorouter/pull/3555) fix: preserve via space beside trapped BGA targets
- [#3564](https://github.com/tscircuit/tscircuit-autorouter/pull/3564) Preserve regional DDR repairs for exact search
- [#3547](https://github.com/tscircuit/tscircuit-autorouter/pull/3547) Repair Pipeline9 DDR routes beside completed copper
- [#3520](https://github.com/tscircuit/tscircuit-autorouter/pull/3520) Preserve fixed native traces throughout Pipeline 9
- [#3480](https://github.com/tscircuit/tscircuit-autorouter/pull/3480) Avoid retaining every temporary topology cell on DDR boards
- [#3471](https://github.com/tscircuit/tscircuit-autorouter/pull/3471) Fix DDR pad drills through the existing repair search
- [#3514](https://github.com/tscircuit/tscircuit-autorouter/pull/3514) Avoid full mesh-edge scans when connecting target regions
- [#308](https://github.com/tscircuit/tiny-hypergraph/pull/308) Preserve fixed native routes during hypergraph rerouting
- [#159](https://github.com/tscircuit/bus-lanes-solver/pull/159) fix: avoid exhaustive surface-site search for untimed A13 buses
- [#147](https://github.com/tscircuit/bus-lanes-solver/pull/147) Route A64’s fourth DDR byte through available pad-edge escape sites
- [#156](https://github.com/tscircuit/bus-lanes-solver/pull/156) Preserve escape gaps beside rotated rectangular pads
- [#136](https://github.com/tscircuit/bus-lanes-solver/pull/136) Fix STMP157 DDR byte routing with valid pad-to-via approaches
- [#104](https://github.com/tscircuit/circuit-json-webgpu/pull/104) Reuse large copper-pour triangulations across PCB presets
- [#102](https://github.com/tscircuit/circuit-json-webgpu/pull/102) Write WebGPU mesh arrays one chunk at a time
- [#101](https://github.com/tscircuit/circuit-json-webgpu/pull/101) perf: build WebGPU meshes in typed array chunks

</details>

<details>
<summary>Abse2001 SPR PRs (7)</summary>

- [#955](https://github.com/tscircuit/circuit-json/pull/955) feat: allow panel fabrication notes without fake footprints (core#5067)
- [#974](https://github.com/tscircuit/props/pull/974) fix: require at least three courtyard outline points
- [#5076](https://github.com/tscircuit/core/pull/5076) fix: use the requested tab span and wider mouse-bite webs (#5066)
- [#5071](https://github.com/tscircuit/core/pull/5071) fix: replace rounded panel slivers with continuous routing slots (#5065)
- [#5722](https://github.com/tscircuit/cli/pull/5722) feat: synchronize CLI converter versions from core
- [#5663](https://github.com/tscircuit/cli/pull/5663) fix: update STEP converter and preserve assembly ZIP exports (#5661)
- [#177](https://github.com/tscircuit/circuit-json-to-step/pull/177) fix: export round pill drills without non-finite STEP directions (#176)

</details>

<details>
<summary>techmannih SPR PRs (5)</summary>

- [#5182](https://github.com/tscircuit/core/pull/5182) fix: allow ground-plane routing past trace-length preflight
- [#5143](https://github.com/tscircuit/core/pull/5143) Skip redundant autorouting between copper-connected terminals
- [#3496](https://github.com/tscircuit/tscircuit-autorouter/pull/3496) fix: pin repair03 with physical copper contact protection
- [#190](https://github.com/tscircuit/high-density-repair03/pull/190) fix: prevent new trace-to-via shorts during repair
- [#187](https://github.com/tscircuit/high-density-repair03/pull/187) perf: reuse broad-force passes and avoid redundant DRC work

</details>

<details>
<summary>GokulPandi-M SPR PRs (4)</summary>

- [#5224](https://github.com/tscircuit/core/pull/5224) Fix false errors when importing split routed traces
- [#5137](https://github.com/tscircuit/core/pull/5137) Reproduce false connectivity errors for split via-to-via traces
- [#5223](https://github.com/tscircuit/core/pull/5223) fix: preserve BGA dogbone fanout when adding a ground pour
- [#5186](https://github.com/tscircuit/core/pull/5186) repro: ground pour prevents BGA dogbone fanout

</details>

<details>
<summary>AnasSarkiz SPR PRs (3)</summary>

- [#975](https://github.com/tscircuit/circuit-json/pull/975) Preserve custom KiCad properties in component metadata
- [#987](https://github.com/tscircuit/props/pull/987) Allow custom KiCad metadata property names
- [#5177](https://github.com/tscircuit/core/pull/5177) Fix split physical ports for custom schematic symbols

</details>

<details>
<summary>imrishabh18 SPR PRs (3)</summary>

- [#3477](https://github.com/tscircuit/tscircuit-autorouter/pull/3477) perf: reduce Pipeline9 clearance projection cost via repair04
- [#62](https://github.com/tscircuit/repair04/pull/62) perf: prune clearance pairs and simplify via-pad distances
- [#49](https://github.com/tscircuit/tscircuit-standalone/pull/49) refactor: preserve the normal standalone package graph

</details>

<details>
<summary>mohan-bee SPR PRs (3)</summary>

- [#290](https://github.com/tscircuit/circuit-json-util/pull/290) move brep copper pours with pcb transforms
- [#3442](https://github.com/tscircuit/tscircuit-autorouter/pull/3442) use upstream power trace expansion batching
- [#68](https://github.com/tscircuit/power-trace-expander/pull/68) batch power trace expansion while preserving work budgets

</details>

<details>
<summary>0hmX SPR PRs (2)</summary>

- [#5109](https://github.com/tscircuit/core/pull/5109) fix: warn when fabricatorPreset has no stackup template for the board
- [#5121](https://github.com/tscircuit/core/pull/5121) fix: default board thickness to 1.6mm

</details>

<details>
<summary>rushabhcodes SPR PRs (2)</summary>

- [#283](https://github.com/tscircuit/circuit-json-util/pull/283) fix: support position tolerance when matching route vias
- [#3](https://github.com/tscircuit/drawing-viewer/pull/3) Render engineering drawings from Circuit JSON

</details>

<details>
<summary>abdalraof-albarbar SPR PRs (1)</summary>

- [#6111](https://github.com/tscircuit/runframe/pull/6111) Fix Pipeline9 solver reconstruction in the Solvers tab

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
| [0hmX](#0hmX) | 6 | 3 | 0 | 11 | 0 | 40 | 24 | 0 |
| [1932819331hy-debug](#1932819331hy-debug) | 3 | 0 | 0 | 0 | 0 | 23 | 0 | 0 |
| [abdalraof-albarbar](#abdalraof-albarbar) | 3 | 3 | 0 | 0 | 0 | 7 | 3 | 0 |
| [Abse2001](#Abse2001) | 8 | 8 | 0 | 9 | 0 | 45 | 17 | 0 |
| [Albertito-AI](#Albertito-AI) | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| [alokudyogi](#alokudyogi) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [AnasSarkiz](#AnasSarkiz) | 7 | 7 | 0 | 0 | 0 | 16 | 10 | 0 |
| [balckwell](#balckwell) | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 |
| [btctony1](#btctony1) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [cocvn157](#cocvn157) | 0 | 0 | 0 | 0 | 0 | 319 | 0 | 0 |
| [Crodify](#Crodify) | 0 | 0 | 0 | 0 | 0 | 15 | 0 | 0 |
| [CrowAleksito](#CrowAleksito) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [cyczzhao-lab](#cyczzhao-lab) | 0 | 0 | 0 | 0 | 0 | 13 | 0 | 0 |
| [danielshawellis](#danielshawellis) | 2 | 1 | 0 | 0 | 0 | 2 | 1 | 0 |
| [Devesh36](#Devesh36) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [DoctorLaplace](#DoctorLaplace) | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| [frds3445](#frds3445) | 2 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| [GokulPandi-M](#GokulPandi-M) | 6 | 4 | 2 | 0 | 0 | 5 | 3 | 0 |
| [HarsH-1877](#HarsH-1877) | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 |
| [imrishabh18](#imrishabh18) | 5 | 5 | 0 | 6 | 1 | 31 | 24 | 0 |
| [jeffrey-graham](#jeffrey-graham) | 0 | 0 | 0 | 0 | 0 | 38 | 0 | 0 |
| [khuxaiphi-stack](#khuxaiphi-stack) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [KrishnaX12](#KrishnaX12) | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 |
| [longdungai](#longdungai) | 3 | 0 | 0 | 0 | 0 | 3 | 0 | 0 |
| [mau16ro](#mau16ro) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [mohan-bee](#mohan-bee) | 3 | 3 | 0 | 0 | 0 | 7 | 5 | 0 |
| [MustafaMulla29](#MustafaMulla29) | 7 | 4 | 0 | 2 | 0 | 41 | 31 | 0 |
| [nhausmna](#nhausmna) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [Plugv3](#Plugv3) | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 |
| [rafagil11](#rafagil11) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [ronanchnlps-bit](#ronanchnlps-bit) | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 |
| [rushabhcodes](#rushabhcodes) | 22 | 10 | 0 | 0 | 0 | 19 | 10 | 0 |
| [seveibar](#seveibar) | 33 | 1 | 0 | 56 | 1 | 100 | 69 | 0 |
| [ShiboSoftwareDev](#ShiboSoftwareDev) | 34 | 34 | 0 | 5 | 0 | 99 | 83 | 0 |
| [Shokun123](#Shokun123) | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 |
| [siddikmallik1999-design](#siddikmallik1999-design) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [techmannih](#techmannih) | 9 | 6 | 0 | 0 | 0 | 19 | 11 | 0 |
| [tscircuitbot](#tscircuitbot) | 0 | 0 | 0 | 0 | 0 | 428 | 309 | 0 |
| [voropaevv](#voropaevv) | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| [zenoutlabs](#zenoutlabs) | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |

## Changes by Repository

### [tscircuit/pcb-viewer](https://github.com/tscircuit/pcb-viewer)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#1163](https://github.com/tscircuit/pcb-viewer/pull/1163) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Updates the Earcut library to version 3.2.4 to improve the performance of triangulating copper pours in WebGPU, resulting in faster scene compilation and PCB painting times. |
| [#1153](https://github.com/tscircuit/pcb-viewer/pull/1153) | 🐙 Minor | ⭐⭐ | imrishabh18 | Fixes hover overlay overflow issue when zooming in on PCB pads, ensuring labels and outlines remain within the viewer bounds. |
| [#1191](https://github.com/tscircuit/pcb-viewer/pull/1191) | 🐙 Minor | ⭐⭐ | 0hmX | Fixes the issue of duplicated mm units in anchor offset labels by ensuring that mm is only appended when necessary, improving label clarity in the PCB viewer. |

<details>
<summary>🐌 Tiny Contributions (13)</summary>

| PR # | Impact | Contributor | Description |
|------|--------|-------------|-------------|
| [#1194](https://github.com/tscircuit/pcb-viewer/pull/1194) | 🐌 Tiny | ShiboSoftwareDev | Updates the WebGPU renderer to version 0.0.17, allowing for the reuse of large copper-pour triangulations when switching PCB presets, resulting in improved load times for specific presets. |
| [#1185](https://github.com/tscircuit/pcb-viewer/pull/1185) | 🐌 Tiny | ShiboSoftwareDev | Updates the WebGPU renderer to version 0.0.16, allowing the PCB viewer to write mesh buffers in batches, improving rendering performance. |
| [#1168](https://github.com/tscircuit/pcb-viewer/pull/1168) | 🐌 Tiny | ShiboSoftwareDev | Bump the WebGPU renderer bundled by the PCB viewer to 0.0.15 to pick up typed mesh buffers and lower peak PCB memory use |
| [#1195](https://github.com/tscircuit/pcb-viewer/pull/1195) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#1192](https://github.com/tscircuit/pcb-viewer/pull/1192) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#1186](https://github.com/tscircuit/pcb-viewer/pull/1186) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#1169](https://github.com/tscircuit/pcb-viewer/pull/1169) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#1157](https://github.com/tscircuit/pcb-viewer/pull/1157) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#1182](https://github.com/tscircuit/pcb-viewer/pull/1182) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#1164](https://github.com/tscircuit/pcb-viewer/pull/1164) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#1154](https://github.com/tscircuit/pcb-viewer/pull/1154) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#1156](https://github.com/tscircuit/pcb-viewer/pull/1156) | 🐌 Tiny | techmannih | Fixes unsupported color errors in WebGPU rendering by updating the circuit-json-webgpu package to support named colors and correct PCB note layout. |
| [#1181](https://github.com/tscircuit/pcb-viewer/pull/1181) | 🐌 Tiny | imrishabh18 | Fixes the height mismatch of the component search button in the pcb-viewer when embedded in runframe by setting the SVG display to inline-block to match the surrounding text controls height. |

</details>

### [tscircuit/3d-viewer](https://github.com/tscircuit/3d-viewer)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#1121](https://github.com/tscircuit/3d-viewer/pull/1121) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Keeps the active GLB on screen while its replacement loads, swapping models on the existing canvas and preserving the camera. |
| [#1095](https://github.com/tscircuit/3d-viewer/pull/1095) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Releases the old WebGL context after disposing the renderer, ensuring the old context is lost and the replacement canvas works correctly. |
| [#1094](https://github.com/tscircuit/3d-viewer/pull/1094) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Fixes the issue where a detached WebGL canvas retains its context after unmounting, leading to unexpected behavior in rendering. |
| [#1091](https://github.com/tscircuit/3d-viewer/pull/1091) | 🐳 Major | ⭐⭐⭐ | seveibar | Right-clicking an object now offers Isolate name, which hides every other object. Unhide All (renamed from Unhide All Components) restores everything. The PCB board can now be picked, so right-clicking it offers Hide Board  Isolate Board (Panel when a panel is rendered). Before this change the board had no id, so only CAD components could be hidden. Cables (cad_cable) can be picked, hidden and isolated the same way. |
| [#1092](https://github.com/tscircuit/3d-viewer/pull/1092) | 🐳 Major | ⭐⭐⭐ | seveibar | Right-clicking a model and choosing Download GLTF now downloads a GLTF of just that model, named after it (e.g. USBC.gltf). Right-clicking the board or empty space still downloads the whole scene as scene.gltf. |
| [#1093](https://github.com/tscircuit/3d-viewer/pull/1093) | 🐙 Minor | ⭐⭐ | seveibar | Fixes the issue where boards in GLB mode could not be hidden or isolated due to missing identifiers, enabling proper visibility controls for board components. |

### [tscircuit/core](https://github.com/tscircuit/core)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#5240](https://github.com/tscircuit/core/pull/5240) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Bumps tscircuitcapacity-autorouter from 0.0.1047 to 0.0.1049 to include the disconnected-graph retry fix |
| [#5122](https://github.com/tscircuit/core/pull/5122) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Bumps tscircuitcapacity-autorouter from 0.0.1035 to 0.0.1037, bringing in the DDR mesh-memory fix. |
| [#5182](https://github.com/tscircuit/core/pull/5182) | 🐳 Major | ⭐⭐⭐ | techmannih | Fixes ground-plane routing failure by allowing connections to a declared inner-layer GND pour to pass the trace-length preflight check. |
| [#5143](https://github.com/tscircuit/core/pull/5143) | 🐳 Major | ⭐⭐⭐ | techmannih | Fixes redundant autorouting requests for terminals already connected by a same-net copper pour by incorporating their physical connectivity into the autorouting process. |
| [#5158](https://github.com/tscircuit/core/pull/5158) | 🐳 Major | ⭐⭐⭐ | seveibar | Adds rounded connections for system-block TSX after Dagre layout, with tighter layout spacing and improved self-loop handling. |
| [#5113](https://github.com/tscircuit/core/pull/5113) | 🐳 Major | ⭐⭐⭐ | seveibar | Assembly TSX now emits cad_assembly_bom_item records for materials with or without CAD geometry, using released tscircuitprops0.0.718 from tscircuitprops973. |
| [#5116](https://github.com/tscircuit/core/pull/5116) | 🐳 Major | ⭐⭐⭐ | seveibar | Fixes the positioning of JST plug tips inside board and motor sockets to ensure proper electrical contact, addressing issues with misalignment and contact row offsets. |
| [#5112](https://github.com/tscircuit/core/pull/5112) | 🐳 Major | ⭐⭐⭐ | seveibar | Adds systemblock.page, .group, .component, and .connection to core. TSX now produces resolved system_block_ Circuit JSON: page dimensions, block bounds, nested group membership, connection routes, and label_anchor_center. The render phase also resolves optional PCB componentsubcircuit associations without creating electrical connectivity. Uses dagrejsdagre 2.x for synchronous compound graph layout: one dependency, approximately 44 KB for its minified ESM module, and no DOM requirement. Supports all four page directions, parallel connections, cycles, self-loops, disconnected blocks, and empty groupspages. The existing props APIs kind maps to Circuit JSONs is_signal  is_power booleans. Invalid names, hierarchy, endpoints, and PCB references produce errors using readable names. The TSX fixtures(https:github.comtscircuitcoretreefeatsystem-blockstestsfeaturessystem-blocks) include 12 system SVG snapshots plus a PCB snapshot, rendered with published circuit-to-svg 0.0.455. Examples cover a nested wireless sensor system, four flow directions, motor-control power and feedback, multiple pages, long text, PCB associations, and updates. Usage documentation(https:github.comtscircuitcoreblobfeatsystem-blocksdocssystem-blocks.md). |
| [#5161](https://github.com/tscircuit/core/pull/5161) | 🐳 Major | ⭐⭐⭐ | seveibar | Fixes the issue where saved routing phases expose through vias as obstacles only on specific layers, ensuring proper handling of physical via spans during autorouting. |
| [#5176](https://github.com/tscircuit/core/pull/5176) | 🐳 Major | ⭐⭐⭐ | AnasSarkiz | Fixes the ambiguous source-port reference issue in the ESP32-S3-WROOM-1-N16 import by ensuring all ground pads are correctly mapped to their physical ports. |
| [#5241](https://github.com/tscircuit/core/pull/5241) | 🐳 Major | ⭐⭐⭐ | AnasSarkiz | Preserves KiCad symbol metadata when inserting default schematic boxes, ensuring that metadata is retained for both default and custom symbols. |
| [#5223](https://github.com/tscircuit/core/pull/5223) | 🐳 Major | ⭐⭐⭐ | GokulPandi-M | Fixes autorouting failure when adding an inner-layer ground pour that prevents BGA dogbone fanout from functioning correctly. |
| [#5186](https://github.com/tscircuit/core/pull/5186) | 🐳 Major | ⭐⭐⭐ | GokulPandi-M | Fixes autorouting failure when adding a ground pour that prevents BGA dogbone fanout from routing correctly. |
| [#5251](https://github.com/tscircuit/core/pull/5251) | 🐙 Minor | ⭐⭐ | ShiboSoftwareDev | Fixes HTTP 403 error when posting benchmark results to PR conversation due to insufficient permissions for the reporting job. |
| [#5231](https://github.com/tscircuit/core/pull/5231) | 🐙 Minor | ⭐⭐ | 0hmX | Fixes unsupported-component error when importing Circuit JSON with simple_fuse and corrects schema mismatches in PCBschematic output. |
| [#5109](https://github.com/tscircuit/core/pull/5109) | 🐙 Minor | ⭐⭐ | 0hmX | Adds a warning when a fabricatorPreset is set but no matching stackup template exists for the specified board parameters, improving user feedback on stackup issues. |
| [#5155](https://github.com/tscircuit/core/pull/5155) | 🐙 Minor | ⭐⭐ | 0hmX | Allows simulation declarations to reference pins in nested subcircuits, enabling board-level simulations without requiring all components to be in the same subcircuit. |
| [#5121](https://github.com/tscircuit/core/pull/5121) | 🐙 Minor | ⭐⭐ | 0hmX | Changes the default board thickness from 1.4mm to 1.6mm to align with JLCPCB standards, ensuring proper stackup generation for 2- and 4-layer boards. |
| [#5157](https://github.com/tscircuit/core/pull/5157) | 🐙 Minor | ⭐⭐ | 0hmX | Fixes issue with schPortArrangement by ensuring side pins are stored as pin numbers instead of labels, resolving compatibility with circuit-json requirements. |
| [#5162](https://github.com/tscircuit/core/pull/5162) | 🐙 Minor | ⭐⭐ | seveibar | Fixes the issue where multi-port power paths incorrectly inherit a capacitors local decoupling limit, preventing autorouting on longer paths. |
| [#5177](https://github.com/tscircuit/core/pull/5177) | 🐙 Minor | ⭐⭐ | AnasSarkiz | Fixes the issue where custom schematic symbols prevented the split-pad inference from creating and connecting separate physical source ports for repeated footprint pin hints. |
| [#5076](https://github.com/tscircuit/core/pull/5076) | 🐙 Minor | ⭐⭐ | Abse2001 | Fixes mouse-bite rows to fill the requested tab span and maintain appropriate material clearance between adjacent holes. |
| [#5071](https://github.com/tscircuit/core/pull/5071) | 🐙 Minor | ⭐⭐ | Abse2001 | Fixes routing of rounded panel corners to use continuous polygon slots instead of invalid rounded rectangles, ensuring valid geometry and improved routing for curved boards. |
| [#5069](https://github.com/tscircuit/core/pull/5069) | 🐙 Minor | ⭐⭐ | Abse2001 | Reproduces a bug where a 22 panel of 1418 mm boards with 2 mm rounded corners creates 1,024 invalid sliver rectangles, producing a comb of tiny routing slots. |
| [#5137](https://github.com/tscircuit/core/pull/5137) | 🐙 Minor | ⭐⭐ | GokulPandi-M | Reproduces false connectivity errors when split via-to-via traces are imported, demonstrating the loss of connection identity in the autorouting process. |

<details>
<summary>🐌 Tiny Contributions (22)</summary>

| PR # | Impact | Contributor | Description |
|------|--------|-------------|-------------|
| [#5273](https://github.com/tscircuit/core/pull/5273) | 🐌 Tiny | ShiboSoftwareDev | Bump tscircuitcapacity-autorouter to 0.0.1059 to include the BGA via-space fix from https:github.comtscircuittscircuit-autorouterpull3555. |
| [#5272](https://github.com/tscircuit/core/pull/5272) | 🐌 Tiny | ShiboSoftwareDev | Updates the tscircuitcapacity-autorouter dependency from version 0.0.1054 to 0.0.1058, including improvements related to regional DDR repair as noted in tscircuittscircuit-autorouter3564, and updates the affected PCB snapshots accordingly. |
| [#5252](https://github.com/tscircuit/core/pull/5252) | 🐌 Tiny | ShiboSoftwareDev | Bumps the tscircuitbus-lanes-solver package from version 0.0.47 to 0.0.48 to include the H616 second-byte BGA escape fix. |
| [#5248](https://github.com/tscircuit/core/pull/5248) | 🐌 Tiny | ShiboSoftwareDev | Add a full TSXCore DDR benchmark for H3, A64, STMP157, OrangeCrab, A13, H616, ButterStick, Glider, i.MX6 and iCEPi. |
| [#5246](https://github.com/tscircuit/core/pull/5246) | 🐌 Tiny | ShiboSoftwareDev | Bump tscircuitbus-lanes-solver from 0.0.46 to 0.0.47 to include the A13 routing search optimization |
| [#5153](https://github.com/tscircuit/core/pull/5153) | 🐌 Tiny | ShiboSoftwareDev | Pins tscircuitbus-lanes-solver to 0.0.43 to include the A64 DDR escape-site fix from the related pull request. |
| [#5120](https://github.com/tscircuit/core/pull/5120) | 🐌 Tiny | ShiboSoftwareDev | Bump cores tscircuitbus-lanes-solver pin from 0.0.40 to 0.0.41 to include the STMP157 DDR pad-to-via approach fix |
| [#5243](https://github.com/tscircuit/core/pull/5243) | 🐌 Tiny | ShiboSoftwareDev | Updates the autorouter and bus-lanes-solver dependencies to their latest versions, addressing the A13 rotated-pad fix in the bus-lanes-solver. |
| [#5235](https://github.com/tscircuit/core/pull/5235) | 🐌 Tiny | ShiboSoftwareDev | Bump tscircuitcapacity-autorouter from 0.0.1044 to 0.0.1047 to include the Glider DDR fixed-copper clearance fix |
| [#5189](https://github.com/tscircuit/core/pull/5189) | 🐌 Tiny | ShiboSoftwareDev | Bump tscircuitcapacity-autorouter from 0.0.1043 to 0.0.1044 to pick up the DDR mesh-edge lookup optimization |
| [#5187](https://github.com/tscircuit/core/pull/5187) | 🐌 Tiny | ShiboSoftwareDev | Bumps tscircuitcapacity-autorouter from 0.0.1041 to 0.0.1043 to include the Glider DDR via-contact fix |
| [#5168](https://github.com/tscircuit/core/pull/5168) | 🐌 Tiny | ShiboSoftwareDev | Updates the tscircuitcapacity-autorouter and tscircuitbus-lanes-solver dependencies to their latest versions to incorporate recent routing fixes and refreshes the PCB snapshot for improved alignment of via placement and inner-layer lanes. |
| [#5146](https://github.com/tscircuit/core/pull/5146) | 🐌 Tiny | ShiboSoftwareDev | Pins tscircuitbus-lanes-solver to version 0.0.42 to include the DDR escape-site fix from a previous pull request. |
| [#5110](https://github.com/tscircuit/core/pull/5110) | 🐌 Tiny | ShiboSoftwareDev | Bumps the version of tscircuitcapacity-autorouter to 0.0.1035 to include DDR pad-drill fix and copper-pourplated-hole corrections. |
| [#5129](https://github.com/tscircuit/core/pull/5129) | 🐌 Tiny | ShiboSoftwareDev | Bumps the tscircuitcapacity-autorouter dependency to version 0.0.1038, addressing the circular-pad DDR routing fix and tightening clearance limits for A13. |
| [#5179](https://github.com/tscircuit/core/pull/5179) | 🐌 Tiny | techmannih | Reproduces a bug where a declared GND pour is not considered during trace-length preflight checks, preventing autorouting. |
| [#5142](https://github.com/tscircuit/core/pull/5142) | 🐌 Tiny | techmannih | Reproduces a bug where the autorouter requests redundant routes between terminals that are already connected by a continuous copper pour, including comprehensive tests and snapshots to validate the behavior. |
| [#5106](https://github.com/tscircuit/core/pull/5106) | 🐌 Tiny | 0hmX | Reproduces the issue where the jlcpcb_standard preset with default board thickness of 1.4mm results in no pcb_stackup being emitted, highlighting the lack of user feedback regarding this behavior. |
| [#5253](https://github.com/tscircuit/core/pull/5253) | 🐌 Tiny | seveibar | Bump Cores tscircuitcapacity-autorouter development dependency from 0.0.1051 to 0.0.1054. |
| [#5188](https://github.com/tscircuit/core/pull/5188) | 🐌 Tiny | Abse2001 | Add 12 missing converter packages to devDependencies in package.json for version tracking. |
| [#5073](https://github.com/tscircuit/core/pull/5073) | 🐌 Tiny | Abse2001 | Reproduces a bug where a requested 3 mm tab results in undersized mouse-bite holes, leading to insufficient web clearance. |
| [#5104](https://github.com/tscircuit/core/pull/5104) | 🐌 Tiny | danielshawellis | Fixes the issue where a redundant ground trace is drawn between pads A and B, which are already connected by a copper pour, while only the connection from the pour to pad C should be routed. |

</details>

### [tscircuit/tscircuit-autorouter](https://github.com/tscircuit/tscircuit-autorouter)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#3555](https://github.com/tscircuit/tscircuit-autorouter/pull/3555) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Fixes autorouting failure by preserving via space beside trapped BGA targets, ensuring connectivity for all signals in the routing process. |
| [#3564](https://github.com/tscircuit/tscircuit-autorouter/pull/3564) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Preserve accepted regional work as a private input to Pipeline9s existing exact repair, optimizing the repair process and maintaining data integrity. |
| [#3474](https://github.com/tscircuit/tscircuit-autorouter/pull/3474) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Fixes routing issues where copper pours cause overlapping escape vias and plated-hole transitions move outside their pads. |
| [#3547](https://github.com/tscircuit/tscircuit-autorouter/pull/3547) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Fixes autorouting failure by repairing DDR routes adjacent to completed copper in Pipeline9, resulting in zero DRC findings and preserving existing copper integrity. |
| [#3519](https://github.com/tscircuit/tscircuit-autorouter/pull/3519) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Reproduces the native DDR copper trace policy and mesh expansion for the STM32MP157, ensuring that completed DDR traces are retained as native traces during routing. |
| [#3504](https://github.com/tscircuit/tscircuit-autorouter/pull/3504) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Preserves Glider DDR ADDR6s contact when force improvement moves its escape via and enables fixed topology-port anchors in Pipeline 9 and worker requests. |
| [#3503](https://github.com/tscircuit/tscircuit-autorouter/pull/3503) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Reduces validation time for DDR topology by using the Flatbush index to check nearby regions instead of all pairs, improving performance significantly. |
| [#3492](https://github.com/tscircuit/tscircuit-autorouter/pull/3492) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Fixes autorouting failure for DQS0NP signals due to loss of net ownership in H3 DDR3 circuit routing. |
| [#3520](https://github.com/tscircuit/tscircuit-autorouter/pull/3520) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Keeps completed bus and manual routes native, with optional isFixed policy carried through hypergraph assignments and detailed routing, ensuring fixed copper survives reripping, repair, simplification and power cleanup. |
| [#3480](https://github.com/tscircuit/tscircuit-autorouter/pull/3480) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Reduces memory usage by preventing the retention of excessive temporary topology cells during DDR board processing, allowing for successful completion of mesh slices without memory exhaustion. |
| [#3479](https://github.com/tscircuit/tscircuit-autorouter/pull/3479) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Fixes memory retention issue in STMP157 DDR board routing by limiting retained cells during topology merging. |
| [#3471](https://github.com/tscircuit/tscircuit-autorouter/pull/3471) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Fixes the issue where repair skipped connected pads entirely, making forbidden drill overlaps invisible to its search. |
| [#3546](https://github.com/tscircuit/tscircuit-autorouter/pull/3546) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Fixes the issue where the completed STM32MP157 mesh retains temporary cells after validating its output, ensuring that the mesh is cleaned up properly before final output. |
| [#3516](https://github.com/tscircuit/tscircuit-autorouter/pull/3516) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Fixes copper clearance issues in the Pipeline9 joint repair, resolving DRC errors from 1 to 0 for the Gliders LDQSN. |
| [#3513](https://github.com/tscircuit/tscircuit-autorouter/pull/3513) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Replays the real A64 and STM32MP157 remaining-routing inputs through Pipeline9 edge construction, targeting handling that scans the complete edge array to check connectivity between regions. |
| [#3493](https://github.com/tscircuit/tscircuit-autorouter/pull/3493) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Restores conductive contacts for disconnected terminal pairs in DDR routing, resolving stalls in H3s DQS0 routing. |
| [#3487](https://github.com/tscircuit/tscircuit-autorouter/pull/3487) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Fixes routing errors by treating round BGA pads as squares in DRC evaluation and repulsion, ensuring zero physical DRC findings and maintaining all connected nets. |
| [#3473](https://github.com/tscircuit/tscircuit-autorouter/pull/3473) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Fixes the handling of copper pours as component pads and preserves existing plated-hole transitions as new vias, preventing extra escape vias from being created during routing. |
| [#3531](https://github.com/tscircuit/tscircuit-autorouter/pull/3531) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Stops retrying disconnected DDR planner graphs after proving no legal path exists, reducing iterations significantly and improving routing efficiency. |
| [#3529](https://github.com/tscircuit/tscircuit-autorouter/pull/3529) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Adjusts the boards clearance for fixed native copper from 0.150 mm to 0.089 mm, affecting the routing of 15 accepted route pieces. |
| [#3524](https://github.com/tscircuit/tscircuit-autorouter/pull/3524) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Adds a test to reproduce the issue of the H3 DDR planner exhausting iterations on disconnected signals, along with captured board input and SVG output for analysis. |
| [#3514](https://github.com/tscircuit/tscircuit-autorouter/pull/3514) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Reduces the time taken to connect target regions by reusing the node-edge map to check only incident edges instead of scanning all mesh edges. |
| [#3548](https://github.com/tscircuit/tscircuit-autorouter/pull/3548) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Releases scratch memory after a large topology completes and validates its output, reducing retained JS heap significantly. |
| [#3496](https://github.com/tscircuit/tscircuit-autorouter/pull/3496) | 🐳 Major | ⭐⭐⭐ | techmannih | Fixes pin repair03 to prevent new physical trace-to-via shorts while preserving exact via anchors and existing repair search budgets. |
| [#3541](https://github.com/tscircuit/tscircuit-autorouter/pull/3541) | 🐳 Major | ⭐⭐⭐ | imrishabh18 | Speeds up index updates during route replacement in the trace simplification process. |
| [#3477](https://github.com/tscircuit/tscircuit-autorouter/pull/3477) | 🐳 Major | ⭐⭐⭐ | imrishabh18 | Reduces the clearance projection cost in Pipeline9 by optimizing the underlying calculations in repair04, resulting in significant performance improvements without altering the existing DRC utilities. |
| [#3572](https://github.com/tscircuit/tscircuit-autorouter/pull/3572) | 🐳 Major | ⭐⭐⭐ | seveibar | Fixes RVboys native reroute issue where the entering-layer endpoint of a via is lost during path simplification, causing disconnected transitions and errors in crossing-via reduction. |
| [#3568](https://github.com/tscircuit/tscircuit-autorouter/pull/3568) | 🐳 Major | ⭐⭐⭐ | seveibar | RVboys native reroute exposed two routing-input errors after 3565 fixed the cleanup crash. A ground escape via ending logically at inner1 was reserved only on topinner1 despite through-hole manufacturing, allowing a bottom-layer signal to cross its pad. Reserving its full physical span then exposed a ground-pad escape incorrectly discarded because a two-step search found free space inside a closed pocket. Reserve and place through-hole escape vias against all copper layers. Explicit blindburied-via support retains the limited span. Check numerical bridges and cramped exits against actual point-pair destinations, including generated escape vias. Preserve explicitly selected terminal bridges through the later filter; keep the component planners exits and older pipelines filtering unchanged. Add the exact full native RVboy input, cropped visual regressions, and focused tests for opposite-side pad clearance, blind-via behavior, and closed-pocket connectivity. |
| [#3565](https://github.com/tscircuit/tscircuit-autorouter/pull/3565) | 🐳 Major | ⭐⭐⭐ | seveibar | Fixes native routing crash during trace simplification by preserving plated-hole boundary precision and ensuring proper cleanup of routes. |
| [#3558](https://github.com/tscircuit/tscircuit-autorouter/pull/3558) | 🐳 Major | ⭐⭐⭐ | seveibar | Fixes autorouting failure by restoring necessary terminal escapes across numerical mesh gaps in RVboys LCD pad regions, ensuring traversable port points are generated correctly. |
| [#3557](https://github.com/tscircuit/tscircuit-autorouter/pull/3557) | 🐳 Major | ⭐⭐⭐ | seveibar | RVboys native Pipeline9 search fails because accepted capacity edges at the LCD pads have no port points. This repro preserves the exact saved phase input byte-for-byte: 197 connections, 1,066 obstacles and 28 previous traces. SHA-256: 51be0b31f378d8feb9577d351f8e8aa8164624012e31fb968e2346ad3f0c15d9. The test runs the entire input through native port-point generation, snapshots fixed viewboxes around LCD pins 30 and 43, then reproduces the native No path failure. Only the drawing is cropped. The fixture also exposes the same close-ups and the full interactive pipeline debugger. Red lines are capacity edges with missing ports; green dots are actual top-layer port points. They depict topology, not copper. Fix PR 3558 is stacked on this repro and uses the same snapshots, input and camera. Its image diff shows the restored pad escapes: LCD pin 30 changes from 02 to 22 usable side edges, and pin 43 from 01 to 11. Validation: repro test passes (13 assertions); tsc --noEmit passes with an 8 GB Node heap. Both rendered snapshots inspected. |
| [#3442](https://github.com/tscircuit/tscircuit-autorouter/pull/3442) | 🐳 Major | ⭐⭐⭐ | mohan-bee | Reduces routing time for power trace expansion from 20s to 1.5s by utilizing upstream batching in the powerTraceExpansionSolver. |

<details>
<summary>🐌 Tiny Contributions (34)</summary>

| PR # | Impact | Contributor | Description |
|------|--------|-------------|-------------|
| [#3554](https://github.com/tscircuit/tscircuit-autorouter/pull/3554) | 🐌 Tiny | ShiboSoftwareDev | The real H3 DDR3 circuit routes its two data bytes, then fails to find a path for DQS1. Core buffers the phases, leaving 017 accepted signals. Adds the native TSX board, captured routing inputs and generated SVGs. The same repro runs unchanged on the stacked fix, 3555.  Board  request  Initial result  goal  Latest verified progress   ---  ---  ---   H3: 16 DQ  DQS1  017 accepted; goal 1717  Both DQ phases route, then DQS1 fails path planning |
| [#3532](https://github.com/tscircuit/tscircuit-autorouter/pull/3532) | 🐌 Tiny | ShiboSoftwareDev | Reproduces the native circuit snapshot for OrangeCrabs detailed-routing clearance, addressing clearance issues and ensuring accurate representation of the routing phase. |
| [#3486](https://github.com/tscircuit/tscircuit-autorouter/pull/3486) | 🐌 Tiny | ShiboSoftwareDev | Reproduces the issue of through-via shorts in the OrangeCrab DDR routing, capturing the core input and generating the board SVG while retaining the no-short assertion for a stacked fix. |
| [#3543](https://github.com/tscircuit/tscircuit-autorouter/pull/3543) | 🐌 Tiny | ShiboSoftwareDev | Reproduces the i.MX6 DDR board with completed data-byte copper for a stacked fix. |
| [#3517](https://github.com/tscircuit/tscircuit-autorouter/pull/3517) | 🐌 Tiny | ShiboSoftwareDev | Reproduces Gliders LDQSN through-via touching the completed DATA4 trace on the bottom layer, including a board snapshot with 49 nets and 1 DRC error. |
| [#3502](https://github.com/tscircuit/tscircuit-autorouter/pull/3502) | 🐌 Tiny | ShiboSoftwareDev | Captures the real A64 and STM32MP157 remaining-routing inputs after 32 DQ signals complete through TSXcore. The runner reproduces slow topology validation and reports the completed mesh hash. |
| [#3579](https://github.com/tscircuit/tscircuit-autorouter/pull/3579) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3578](https://github.com/tscircuit/tscircuit-autorouter/pull/3578) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3573](https://github.com/tscircuit/tscircuit-autorouter/pull/3573) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3570](https://github.com/tscircuit/tscircuit-autorouter/pull/3570) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3567](https://github.com/tscircuit/tscircuit-autorouter/pull/3567) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3563](https://github.com/tscircuit/tscircuit-autorouter/pull/3563) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3562](https://github.com/tscircuit/tscircuit-autorouter/pull/3562) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3556](https://github.com/tscircuit/tscircuit-autorouter/pull/3556) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3495](https://github.com/tscircuit/tscircuit-autorouter/pull/3495) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3552](https://github.com/tscircuit/tscircuit-autorouter/pull/3552) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3526](https://github.com/tscircuit/tscircuit-autorouter/pull/3526) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3506](https://github.com/tscircuit/tscircuit-autorouter/pull/3506) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3499](https://github.com/tscircuit/tscircuit-autorouter/pull/3499) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3491](https://github.com/tscircuit/tscircuit-autorouter/pull/3491) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3550](https://github.com/tscircuit/tscircuit-autorouter/pull/3550) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3542](https://github.com/tscircuit/tscircuit-autorouter/pull/3542) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3530](https://github.com/tscircuit/tscircuit-autorouter/pull/3530) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3518](https://github.com/tscircuit/tscircuit-autorouter/pull/3518) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3489](https://github.com/tscircuit/tscircuit-autorouter/pull/3489) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3484](https://github.com/tscircuit/tscircuit-autorouter/pull/3484) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3476](https://github.com/tscircuit/tscircuit-autorouter/pull/3476) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3472](https://github.com/tscircuit/tscircuit-autorouter/pull/3472) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3510](https://github.com/tscircuit/tscircuit-autorouter/pull/3510) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3545](https://github.com/tscircuit/tscircuit-autorouter/pull/3545) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3535](https://github.com/tscircuit/tscircuit-autorouter/pull/3535) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3482](https://github.com/tscircuit/tscircuit-autorouter/pull/3482) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3368](https://github.com/tscircuit/tscircuit-autorouter/pull/3368) | 🐌 Tiny | techmannih | Pins the repair03 broad-force performance fix to a specific commit to avoid repeated native DRC evaluations and common broad-force passes, while preserving existing geometries and including regression tests. |
| [#3441](https://github.com/tscircuit/tscircuit-autorouter/pull/3441) | 🐌 Tiny | mohan-bee | Motivation Reproduce slow uncached power-trace expansion on the four-gang WiFi controller(https:tscircuit.commohan-beefour-gang-wifi-switch-layoutblobcontroller.circuit.tsx).  Before The captured JOINT_LV workload takes 2,997,249 power-expansion wrapper steps. Matching the board runners 256 steps per yield produces 12,208 timer yields: two local runs on an Apple M5 took 23.123.7 seconds overall, with 20.321.0 seconds in power expansion. This is the low-voltage phase from published v0.0.9, replayed through native Pipeline9 at 0.0.1029. The five earlier mains traces are preloaded; those phases are not rerun.  After Add the exact solver-ready SRJ, uncropped 48  50 mm board context, a cache-disabled native debugger fixture, and a snapshot test. The test preserves the published adapters physical via policy; the full controller snapshot includes 37 new low-voltage traces, five mains traces, all 71 original obstacles, and 0 measured relaxed DRC errors. Snapshot verification passes with 13 assertions; type checking and the package build pass. This is a reproduction PR, with the batching fix kept separate. !Full controller board including preloaded mains routes(https:raw.githubusercontent.comtscircuittscircuit-autorouterceb0bbe039037d0aaa35ec959f55bc71c06d4607testsbugs__snapshots__controller-power-expansion.snap.svg) |

</details>

### [tscircuit/tiny-hypergraph](https://github.com/tscircuit/tiny-hypergraph)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#308](https://github.com/tscircuit/tiny-hypergraph/pull/308) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Preserves fixed native routes during hypergraph rerouting by retaining their initial assignments and excluding them from rip sets, while allowing same-net reuse of their occupied ports. |

### [tscircuit/high-density-repair01](https://github.com/tscircuit/high-density-repair01)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#44](https://github.com/tscircuit/high-density-repair01/pull/44) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Add opt-in anchors for endpoint vias to prevent copper disconnection in neighboring nodes during force improvement. |
| [#49](https://github.com/tscircuit/high-density-repair01/pull/49) | 🐳 Major | ⭐⭐⭐ | seveibar | Fixes clearance regression in autorouter by preserving coordinates of through-obstacle anchors while maintaining existing grid quantization for ordinary routing anchors. |
| [#48](https://github.com/tscircuit/high-density-repair01/pull/48) | 🐳 Major | ⭐⭐⭐ | seveibar | Fixes routing failure by preserving fixed-point precision at plated-hole boundaries, preventing unintended layer transitions. |
| [#43](https://github.com/tscircuit/high-density-repair01/pull/43) | 🐙 Minor | ⭐⭐ | ShiboSoftwareDev | Fixes Glider DDR escape via placement issue by adjusting its position to separate it from neighboring topology fragments. |

### [tscircuit/high-density-repair03](https://github.com/tscircuit/high-density-repair03)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#199](https://github.com/tscircuit/high-density-repair03/pull/199) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Fixes DRC evaluation and repulsion for circular SMT pads by treating them correctly as circles instead of rectangles, leading to a reduction in DRC findings. |
| [#198](https://github.com/tscircuit/high-density-repair03/pull/198) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Fixes the issue where existing plated-hole transitions were converted into new vias, ensuring that these transitions are preserved during the repair DRC process. |
| [#196](https://github.com/tscircuit/high-density-repair03/pull/196) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Fixes the issue where repair skips connected pads and trades away cleared drills while improving copper clearance when an SRJ disallows vias in pads. |
| [#190](https://github.com/tscircuit/high-density-repair03/pull/190) | 🐳 Major | ⭐⭐⭐ | techmannih | Repair could reduce reported DRC errors while creating a physical trace-to-via short because publication checks omitted via annuli. Check via copper across its physical drill layers, include via-to-via contacts, and invalidate prepared geometry when via diameter changes. Contact identities distinguish wire crossings from annulus contacts; same-net copper remains allowed. Preserve exact via anchors and circular pad geometry. The deferred final owner prioritizes wire crossings, tries local wire displacements and coupled moves of up to two via stacks, and validates each candidate against the whole board. It can restore affected connections while retaining independent repairs, within the existing search budgets. The portfolios early-exit heuristic remains wire-only; publication checks all copper. Reduce work and allocations in this path: prune board edges with conservative coordinate bounds, use numeric spatial-grid columns and allocate contact keys only after overlap. Native contact repair first rejects proven pad overlaps on changed or already-overlapping connections. Geometry is built only for selected owners while preserving global via ownership and numbering. Surviving proposals receive complete DRC and rejected proposals consume the original budget. Retain a bounded prefix of exact primitive geometry from the last full DRC evaluation to avoid serializing unchanged inputs. Compare coordinates, ownership, ports, widths, via dimensions and layers explicitly, including in-place mutations. Geometry shares the existing cache accounting budget with primitive keys. Engine-owned query errors are copied once at the public-result boundary, preserving caller mutation isolation. At 8ec1f3acf1c5f2b228e6f6d8c8972d4ee2045962, official standalone SRJ18(https:github.comtscircuithigh-density-repair03actionsruns42032055563) is 2.84 total time, DRC 1,079  1,078; DRC14(https:github.comtscircuithigh-density-repair03actionsruns42032060529) is -11.83, DRC 5  5. Both compare stacked base 892ddb1 on one Ubuntu runner, two basePR pairs in opposite orders, concurrency 2, Bun 1.4.4 x64. No per-case DRC increases. A separate fixed Blacksmith comparison(https:github.comtscircuittscircuit-autorouteractionsruns42031516576), using Bun 1.4.2 arm64 and copied dependencies, measures SRJ18 1.30  -1.54 and DRC14 -11.49  -12.18 against the same stacked base. Against the previous published repair 6ec16dc, isolated cases 6 and 13 are 10.2113.35 and 7.4810.44 faster with identical output hashes. Case 13 memory is mixed. Full-pipeline measurements, including all slower repeats and identical-main memory controls, are in the consumer PR(https:github.comtscircuittscircuit-autorouterpull3496). All 186 repair tests pass (50,526 assertions) and both TypeScript projects pass. Tests cover 3,606 exhaustive board-distance pairs, 3,200 spatial-order oracle cases, obstacle-filter parity, duplicate-via ownership, mutation isolation, cache eviction and bounded geometry reuse. Consumer integration passes six tests  637 assertions and typecheck. Hosted CI is green; the branch is conflict-free. Stacked on 189; merge 189 first. The six-route output gap becomes 0.05572 mm instead of -0.06523 mm; the real Game Boy replay retains 0.08638 mm clearance instead of publishing -0.00107 mm overlap. |
| [#187](https://github.com/tscircuit/high-density-repair03/pull/187) | 🐳 Major | ⭐⭐⭐ | techmannih | Reduces redundant DRC evaluations by reusing broad-force passes and optimizing candidate evaluations in the autorouting process. |

<details>
<summary>🐌 Tiny Contributions (2)</summary>

| PR # | Impact | Contributor | Description |
|------|--------|-------------|-------------|
| [#189](https://github.com/tscircuit/high-density-repair03/pull/189) | 🐌 Tiny | techmannih | Reproduces a repair scenario that introduces a trace-to-via short in a Game Boy circuit, validating DRC errors and providing visual snapshots of the output. |
| [#186](https://github.com/tscircuit/high-density-repair03/pull/186) | 🐌 Tiny | techmannih | Adds a regression test to reproduce duplicate native DRC evaluations across different force scales without changing production code. |

</details>

### [tscircuit/bus-lanes-solver](https://github.com/tscircuit/bus-lanes-solver)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#162](https://github.com/tscircuit/bus-lanes-solver/pull/162) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Fixes routing issues for the H616 second DDR byte by utilizing a legal BGA escape that was previously missed, ensuring all signals are accepted and DRC clean. |
| [#159](https://github.com/tscircuit/bus-lanes-solver/pull/159) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Avoids exhaustive surface-site search for untimed A13 buses by attempting ordinary lane routing first, retaining surface-site search on the first retry for timing-constrained buses. |
| [#147](https://github.com/tscircuit/bus-lanes-solver/pull/147) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Adds drill-clear positions beside round pads and broadens blocked site domains for A64s fourth data byte routing, enabling connection of all data lines with zero physical findings. |
| [#141](https://github.com/tscircuit/bus-lanes-solver/pull/141) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Preserves successful allocations while allowing negotiation of generated signal sites when routing fails due to blocked DDR copper. |
| [#136](https://github.com/tscircuit/bus-lanes-solver/pull/136) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Fixes routing issues for STMP157 DDR byte connections by implementing valid pad-to-via approaches, ensuring all connections pass DRC checks. |
| [#151](https://github.com/tscircuit/bus-lanes-solver/pull/151) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Fixes routing issues by connecting shared DDR RAM and test-point branches to ensure all endpoints are preserved and connected correctly. |
| [#135](https://github.com/tscircuit/bus-lanes-solver/pull/135) | 🐳 Major | ⭐⭐⭐ | seveibar | Stacked on 134. The exact native core MT8395 LPDDR4X board now routes and exports 138138 signals, 18 buses and 12 differential pairs, preserving its original layer, timing, coupling, obstacle and via constraints. The completed Circuit JSON contains 138 PCB traces and 276 physical vias, with zero core circuit errors. No core input fix or normalization is required. !Completed native core board(https:raw.githubusercontent.comtscircuitbus-lanes-solver375ca9df3f8a31f7634fe2bb506c712488ec57a7reprosmt8395-lpddr4xcore-board.snap.png) Annotated routing snapshot(https:github.comtscircuitbus-lanes-solverblob375ca9df3f8a31f7634fe2bb506c712488ec57a7reprosmt8395-lpddr4xboard.snap.svg)  Circuit JSON(https:github.comtscircuitbus-lanes-solverblob375ca9df3f8a31f7634fe2bb506c712488ec57a7reprosmt8395-lpddr4xroutedcore-full.circuit.json.gz)  SRJ copper(https:github.comtscircuitbus-lanes-solverblob375ca9df3f8a31f7634fe2bb506c712488ec57a7reprosmt8395-lpddr4xroutedfull.srj.json.gz)  Coreexport validation report(https:github.comtscircuitbus-lanes-solverblob375ca9df3f8a31f7634fe2bb506c712488ec57a7reprosmt8395-lpddr4xroutedcore-full-report.json) The solver reserves coupled pairs first, routes commandaddress carriers before data escapes become fixed, and preserves and extends clear command paths during matching. Adaptive repair remains scoped to the pinned-bus strategy. Final acceptance checks connectivity, copper DRC, joined self-clearance, whole-signal buspair lengths, coupling and forbidden via-in-pad holes. Native core rendering exposed two additional failures at bf1bd6e that the earlier solver-only validator missed: tuning on EMI0_CK_T and EMI1_DQS0_T touched its own via land. Pinned-bus pair tuning now uses the terminal-via guard and checks the joined result again. Small fixtures preserve both rejected approaches, and regressions agree with cores self-short checker. The full retained copper and overview are replaced by the corrected, accepted result; existing native strategies keep their previous tuning options.  Reproduction and validation Fresh native core render at solver revision 220b7949bbdef8e4d58fec539cd6da12bb6a582e: 138138 accepted, all 18 bus constraints and 12 paircoupling checks pass, no invalid geometry, terminal-via approaches or via-in-pad holes. Core reports no circuit errors. The export audit verifies each physical trace and plated via against accepted solver copper. Core render and checks: 791.35 seconds with the default routing budget; independent validation ran afterward. Bun 1.4.4, Linux x64, 2 GiB JSC heap hint. This is not a controlled performance comparison. Original input SHA-256: be7707c9188ba888fc551fcc341b424eefdb5c65e2ab9e593c3a9829b1fe4221. Accepted SRJ: 34ecb9dc4ba22b9cf6cb8c17fe63b18e56da1e0daff1d81bc7780591edb490a6. Circuit JSON: 4211deedc11e6ecaa408abfab2cdd9b0b6524cde6e6e936a9fde28dc9fa4a097. Targeted fresh pairbyte routing, native-pair behavior, input constraints, via regressions, retained snapshots and board-export tests pass. Export regressions reject missingduplicate traces, changed copper and moved drill holes. Typecheck, formatting, build and isolated NodebrowserTypeScript package consumers pass. The saved full-board images were independently revalidated, rendered and visually inspected. Retained-output tests are separate from the fresh core solve. Artifact commit 375ca9df3f8a31f7634fe2bb506c712488ec57a7 has the same library tree as 220b794. The pinned published core bundles an older solver. The end-to-end harness substitutes only that dependency binding in memory using a guarded Bun loader; it retains cores native adapter, SRJ construction, render lifecycle, circuit checks and export. It does not use algorithmFn or change solver options. The published package alone does not yet contain this fix. See the repro instructions(https:github.comtscircuitbus-lanes-solvertree375ca9df3f8a31f7634fe2bb506c712488ec57a7reprosmt8395-lpddr4x). sh bun install (cd reprosmt8395-lpddr4xsource  bun install --frozen-lockfile --ignore-scripts) BUN_JSC_forceRAMSize2147483648 BUN_JSC_miniVMHeapGrowthFactor1.05  bun reprosmt8395-lpddr4xsourceroute.tsx full bun reprosmt8395-lpddr4xboard-export.ts full  This completes the DDR routing research fixture. Power, reference planes, decoupling, boot circuitry and hardware SI qualification remain outside its scope.  AM3352 benchmark effect Final-revision Blacksmith comparison passed: 1111  1111, with no lost completions, failures or timeouts. Both revisions passed 4747 connectivity, DRC, buspair matching, couplinggeometry quality and fixed-copper preservation on every sample. Input hashes and reported skews agree. Timings are mixed: P50 76.069  58.912 s (22.6), P90 612.712  533.177 s (13.0), P95 716.283  718.257 s (0.3). Observed regressions include outer-layers 612.712  903.337 s (47.4), left 20.810  32.192 s (54.7), and inner-layers 52.291  58.912 s (12.7). No uniform speedup is claimed. The via guard is enabled for pinned native buses; existing native strategies retain their tuning options. The final head and pinned basecontroller revisions are listed in the comparison below. Both used identical fixtures, harness and 3,600-second per-solversample budgets, Bun 1.4.0 on Blacksmith 4-vCPU Linux runners, with dependency installation before timing. For each of the 11 entries in scriptspr-benchmarksamples.json, CI ran bun basescriptspr-benchmarkrun-pair.ts --sample sample --timeout-seconds 3600 --main baselibindex.ts --pr headlibindex.ts --main-sha base --pr-sha head --controller-sha base --output resultssample.json. This launches the same fresh worker entry point as .benchmark.sh; saved routes are not counted as solves. Raw reports and the analysis are retained in the linked workflow artifacts. details summaryComplete final-revision measurements and provenancesummary AM3352 benchmark for PR 135  workflow artifacts(https:github.comtscircuitbus-lanes-solveractionsruns41898205718) Main: 023bc220e55905d5141599ad6a0d7a219c64c699  PR: 375ca9df3f8a31f7634fe2bb506c712488ec57a7  timeout budget: 3600 s per sample. Controller: 023bc220e55905d5141599ad6a0d7a219c64c699. Lost completions (main accepted, PR not accepted): none. Gained completions: none. Budgeted time to valid completion  all 11 canonical samples Acceptance requires solving strictly before the timeout budget. An accepted sample contributes min(actual solve time, timeout budget). Every failure, timeout, crash, missing artifact, or invalid result contributes the full budget. These are completion-aware budgeted values, not percentiles of actual elapsed durations.  Metric  Main  PR  Change   ---  ---:  ---:  ---:   Completion  1111 (100.0)  1111 (100.0)  0.0 pp   Timeouts  0  0  0   Other failures  0  0  0   P50 time  76.069 s  58.912 s  -22.6   P80 time  224.250 s  196.935 s  -12.2   P90 time  612.712 s  533.177 s  -13.0   P95 time  716.283 s  718.257 s  0.3  Completion changes are percentage points (pp); timing changes are relative percentages, with negative values faster. Other failures include crashes, invalid results, and missing artifacts. Actual solve time on the same 11 samples accepted on both revisions  Metric  Main  PR  Change   ---  ---:  ---:  ---:   P50 time  76.069 s  58.912 s  -22.6   P80 time  224.250 s  196.935 s  -12.2   P90 time  612.712 s  533.177 s  -13.0   P95 time  716.283 s  718.257 s  0.3  Percentiles use linear interpolation at (n  1)  p. A PR change has no percentage when the main value is zero.  Sample  Main status  actual elapsed  PR status  actual elapsed  Completion   ---  ---  ---  ---   control  accepted (4747 signals; DRC passed)  solve 36.296 s  wall 37.817 s  accepted (4747 signals; DRC passed)  solve 29.127 s  wall 30.536 s  both accepted   control-inner1  accepted (4747 signals; DRC passed)  solve 819.854 s  wall 821.782 s  accepted (4747 signals; DRC passed)  solve 533.177 s  wall 535.092 s  both accepted   right  accepted (4747 signals; DRC passed)  solve 21.310 s  wall 23.498 s  accepted (4747 signals; DRC passed)  solve 16.418 s  wall 17.710 s  both accepted   left  accepted (4747 signals; DRC passed)  solve 20.810 s  wall 23.102 s  accepted (4747 signals; DRC passed)  solve 32.192 s  wall 34.922 s  both accepted   above  accepted (4747 signals; DRC passed)  solve 33.353 s  wall 35.475 s  accepted (4747 signals; DRC passed)  solve 29.551 s  wall 31.366 s  both accepted   inner-layers  accepted (4747 signals; DRC passed)  solve 52.291 s  wall 54.657 s  accepted (4747 signals; DRC passed)  solve 58.912 s  wall 60.838 s  both accepted   inner-layers-right  accepted (4747 signals; DRC passed)  solve 76.069 s  wall 78.943 s  accepted (4747 signals; DRC passed)  solve 53.427 s  wall 54.822 s  both accepted   inner-layers-left  accepted (4747 signals; DRC passed)  solve 196.458 s  wall 202.745 s  accepted (4747 signals; DRC passed)  solve 196.935 s  wall 201.057 s  both accepted   inner-layers-above  accepted (4747 signals; DRC passed)  solve 156.755 s  wall 159.224 s  accepted (4747 signals; DRC passed)  solve 138.809 s  wall 140.687 s  both accepted   inner-layers-complete-ca  accepted (4747 signals; DRC passed)  solve 224.250 s  wall 233.016 s  accepted (4747 signals; DRC passed)  solve 184.383 s  wall 191.268 s  both accepted   outer-layers  accepted (4747 signals; DRC passed)  solve 612.712 s  wall 615.779 s  accepted (4747 signals; DRC passed)  solve 903.337 s  wall 905.511 s  both accepted  Accepted total-copper bus and differential-pair skews (skew  tolerance, mm)  Sample  Main buses  PR buses  Main pairs  PR pairs   ---  ---  ---  ---  ---   control  DDR95;BYTE0: 0.6350  0.6350brDDR95;BYTE1: 0.6350  0.6350  DDR95;BYTE0: 0.6350  0.6350brDDR95;BYTE1: 0.6350  0.6350  pair95;0: 0.0779  0.1270brpair95;1: 0.1269  0.1270brpair95;2: 0.0728  0.1270  pair95;0: 0.0779  0.1270brpair95;1: 0.1269  0.1270brpair95;2: 0.0728  0.1270   control-inner1  DDR95;BYTE0: 0.6350  0.6350brDDR95;BYTE1: 0.6350  0.6350  DDR95;BYTE0: 0.6350  0.6350brDDR95;BYTE1: 0.6350  0.6350  pair95;0: 0.0489  0.1270brpair95;1: 0.0047  0.1270brpair95;2: 0.0302  0.1270  pair95;0: 0.0489  0.1270brpair95;1: 0.0047  0.1270brpair95;2: 0.0302  0.1270   right  DDR95;BYTE0: 0.6350  0.6350brDDR95;BYTE1: 0.6350  0.6350  DDR95;BYTE0: 0.6350  0.6350brDDR95;BYTE1: 0.6350  0.6350  pair95;0: 0.0960  0.1270brpair95;1: 0.1218  0.1270brpair95;2: 0.1026  0.1270  pair95;0: 0.0960  0.1270brpair95;1: 0.1218  0.1270brpair95;2: 0.1026  0.1270   left  DDR95;BYTE0: 0.6350  0.6350brDDR95;BYTE1: 0.5111  0.6350  DDR95;BYTE0: 0.6350  0.6350brDDR95;BYTE1: 0.5111  0.6350  pair95;0: 0.0105  0.1270brpair95;1: 0.1270  0.1270brpair95;2: 0.1054  0.1270  pair95;0: 0.0105  0.1270brpair95;1: 0.1270  0.1270brpair95;2: 0.1054  0.1270   above  DDR95;BYTE0: 0.6350  0.6350brDDR95;BYTE1: 0.6350  0.6350  DDR95;BYTE0: 0.6350  0.6350brDDR95;BYTE1: 0.6350  0.6350  pair95;0: 0.1270  0.1270brpair95;1: 0.1270  0.1270brpair95;2: 0.1270  0.1270  pair95;0: 0.1270  0.1270brpair95;1: 0.1270  0.1270brpair95;2: 0.1270  0.1270   inner-layers  DDR95;BYTE0: 0.6350  0.6350brDDR95;BYTE1: 0.6350  0.6350  DDR95;BYTE0: 0.6350  0.6350brDDR95;BYTE1: 0.6350  0.6350  pair95;0: 0.0779  0.1270brpair95;1: 0.1269  0.1270brpair95;2: 0.1270  0.1270  pair95;0: 0.0779  0.1270brpair95;1: 0.1269  0.1270brpair95;2: 0.1270  0.1270   inner-layers-right  DDR95;BYTE0: 0.6350  0.6350brDDR95;BYTE1: 0.6350  0.6350  DDR95;BYTE0: 0.6350  0.6350brDDR95;BYTE1: 0.6350  0.6350  pair95;0: 0.1270  0.1270brpair95;1: 0.1270  0.1270brpair95;2: 0.1270  0.1270  pair95;0: 0.1270  0.1270brpair95;1: 0.1270  0.1270brpair95;2: 0.1270  0.1270   inner-layers-left  DDR95;BYTE0: 0.6350  0.6350brDDR95;BYTE1: 0.6350  0.6350  DDR95;BYTE0: 0.6350  0.6350brDDR95;BYTE1: 0.6350  0.6350  pair95;0: 0.1270  0.1270brpair95;1: 0.0000  0.1270brpair95;2: 0.1054  0.1270  pair95;0: 0.1270  0.1270brpair95;1: 0.0000  0.1270brpair95;2: 0.1054  0.1270   inner-layers-above  DDR95;BYTE0: 0.6350  0.6350brDDR95;BYTE1: 0.6350  0.6350  DDR95;BYTE0: 0.6350  0.6350brDDR95;BYTE1: 0.6350  0.6350  pair95;0: 0.1269  0.1270brpair95;1: 0.1270  0.1270brpair95;2: 0.0000  0.1270  pair95;0: 0.1269  0.1270brpair95;1: 0.1270  0.1270brpair95;2: 0.0000  0.1270   inner-layers-complete-ca  DDR95;BYTE0: 0.6350  0.6350brDDR95;BYTE1: 0.6350  0.6350brDDR95;ADDR95;CTRL95;CK: 0.6350  0.6350  DDR95;BYTE0: 0.6350  0.6350brDDR95;BYTE1: 0.6350  0.6350brDDR95;ADDR95;CTRL95;CK: 0.6350  0.6350  pair95;0: 0.0754  0.1270brpair95;1: 0.0000  0.1270brpair95;2: 0.0664  0.1270  pair95;0: 0.0754  0.1270brpair95;1: 0.0000  0.1270brpair95;2: 0.0664  0.1270   outer-layers  DDR95;BYTE0: 0.6350  0.6350brDDR95;BYTE1: 0.6350  0.6350  DDR95;BYTE0: 0.6350  0.6350brDDR95;BYTE1: 0.6350  0.6350  pair95;0: 0.0192  0.1270brpair95;1: 0.1270  0.1270brpair95;2: 0.1270  0.1270  pair95;0: 0.0192  0.1270brpair95;1: 0.1270  0.1270brpair95;2: 0.1270  0.1270  detailssummaryFixture input SHA-256 hashessummary  Sample  Main input  PR input   ---  ---  ---   control  b7a4e9d09a22fe0ed131a544548b14eef20fbf4e88b6dc6ffaa11ca44e6bfe59  b7a4e9d09a22fe0ed131a544548b14eef20fbf4e88b6dc6ffaa11ca44e6bfe59   control-inner1  14b5b318540ce7bac367cf22338abd7f9fffd2f7ce6c2a12f903116f50ca9bde  14b5b318540ce7bac367cf22338abd7f9fffd2f7ce6c2a12f903116f50ca9bde   right  78c22c8d818ee2c2abe2eec9c6b6e408161a9d0eaf09afbafc3242e71e8f5778  78c22c8d818ee2c2abe2eec9c6b6e408161a9d0eaf09afbafc3242e71e8f5778   left  6042ca0f0889a983a6ccf8f929a6a46b18cc57134e1b9f3b49c19063b936caa5  6042ca0f0889a983a6ccf8f929a6a46b18cc57134e1b9f3b49c19063b936caa5   above  20fc884f08accd368e4ce049ab3fc180a1926f425787a504dbc4040f651bfa69  20fc884f08accd368e4ce049ab3fc180a1926f425787a504dbc4040f651bfa69   inner-layers  1b91e6c5207e4b7e132aa5ac246e94777f926c7beab8675adf0356634b8280ad  1b91e6c5207e4b7e132aa5ac246e94777f926c7beab8675adf0356634b8280ad   inner-layers-right  2eaf3dedcd84fbfed10262f4d4c99370a0ca00a7a060f87b7a1cdcba9de37a8e  2eaf3dedcd84fbfed10262f4d4c99370a0ca00a7a060f87b7a1cdcba9de37a8e   inner-layers-left  1c3db8ee018bc90df7fbbb0c198c42efcc0ca948a6a213338650cf81a51f7ab2  1c3db8ee018bc90df7fbbb0c198c42efcc0ca948a6a213338650cf81a51f7ab2   inner-layers-above  68a86ef74f8ec9628954e909464c009d98fb2c902a6376e20b3a32d4b5cff555  68a86ef74f8ec9628954e909464c009d98fb2c902a6376e20b3a32d4b5cff555   inner-layers-complete-ca  a6def279fa2d3356a66ee94b1760a76eebb6c6d8e605005ce5903bd2fbca8776  a6def279fa2d3356a66ee94b1760a76eebb6c6d8e605005ce5903bd2fbca8776   outer-layers  de3fd915f3c7d8c9bf4fd3c9b197596ba5e08c1be328f9c5223d7ab78736588f  de3fd915f3c7d8c9bf4fd3c9b197596ba5e08c1be328f9c5223d7ab78736588f  details details |
| [#156](https://github.com/tscircuit/bus-lanes-solver/pull/156) | 🐙 Minor | ⭐⭐ | ShiboSoftwareDev | Fixes the issue where rotated pads were enclosed in horizontalvertical boxes, blocking legal pin escapes by using an oriented capsule that covers the entire rectangular pad, including its corners. |

<details>
<summary>🐌 Tiny Contributions (8)</summary>

| PR # | Impact | Contributor | Description |
|------|--------|-------------|-------------|
| [#161](https://github.com/tscircuit/bus-lanes-solver/pull/161) | 🐌 Tiny | ShiboSoftwareDev | Reproduces H616 DQ8DQ15 failing with all eight DQ0DQ7 routes fixed, retaining the original routing input and source provenance, with a test that intentionally fails until a stacked fix is included. |
| [#158](https://github.com/tscircuit/bus-lanes-solver/pull/158) | 🐌 Tiny | ShiboSoftwareDev | Captures the wasted surface search steps for A13 CPU data bytes while retaining the original circuit design and validating the PCB SVG without altering the production solver or input changes. |
| [#150](https://github.com/tscircuit/bus-lanes-solver/pull/150) | 🐌 Tiny | ShiboSoftwareDev | ButterSticks first DDR byte joins FPGA U4 and both RAM packages, U11U12. The exact core-generated request has eight signals and 24 endpoints, but routing stops at two terminals required before creating copper. The repro keeps the real board input and snapshots the failed baseline before asserting successful routing. No solver changes. Input provenance and source PCB fingerprint are beside the fixture. !Failed baseline: eight shared DDR signals(https:raw.githubusercontent.comtscircuitbus-lanes-solver86c691174b633d6b3a0af46733e1b80e43b33e07testsrepros__snapshots__butterstick-shared-ddr.snap.svg) Validation: the focused test reproduces the named guard failure. Benchmark effect: production code and benchmark inputs are unchanged; paired AM3352 runs are provided by this PRs benchmark workflow. |
| [#140](https://github.com/tscircuit/bus-lanes-solver/pull/140) | 🐌 Tiny | ShiboSoftwareDev | H3 byte1 and A64 byte2 stall after earlier DDR bytes have routed. This captures the real TSX boards and their unchanged core inputs. The tests are intentionally red. Their SVGs show the supplied copper and label the eight new routes as unaccepted; the stacked fix replaces those same snapshots after connectivity and DRC pass.  H3 baseline  A64 baseline   ---  ---   !H3(https:raw.githubusercontent.comtscircuitbus-lanes-solverafe52fdccd276c39387ad022addf26f7ad21926dtests__snapshots__h3-preloaded-byte.snap.svg)  !A64(https:raw.githubusercontent.comtscircuitbus-lanes-solverafe52fdccd276c39387ad022addf26f7ad21926dtests__snapshots__a64-preloaded-byte.snap.svg)  Production routing and AM3352 benchmark behavior are unchanged. The required fresh comparison finished with 1111 acceptance green. The eleven-case control gallery(https:github.comtscircuitbus-lanes-solverblob4d4c355bdb89e911d28719b13e8a9e0bd3ccf196reprospreloaded-ddram3352-controlsREADME.md) includes inspected, completed snapshots, raw basehead reports and provenance. Both revisions produce identical complete outputs. |
| [#155](https://github.com/tscircuit/bus-lanes-solver/pull/155) | 🐌 Tiny | ShiboSoftwareDev | The real A13 CPU-side DDR data byte fails with 08 signals connected. Its 45 rectangular pads become oversized horizontalvertical boxes in the visibility router, blocking space beside the pins. Includes the original TSX, exact Core input and a native PCB SVG. All 378 pads and the existing routing rules are preserved. The regression intentionally fails until the stacked fix; no candidate copper is shown. !Failed baseline(https:raw.githubusercontent.comtscircuitbus-lanes-solver6d71897f630fe3bc19496956c45c37960825edb7tests__snapshots__a13-cpu-byte0-pcb.snap.svg) Benchmark effect: no production code changes. The required paired Blacksmith benchmark(https:github.comtscircuitbus-lanes-solveractionsruns42240052569) completed with 1111 head cases accepted, including connectivity, DRC, matching, coupling and fixed-copper preservation. Base 4c911ae, head 6d71897f; Bun 1.4.0, identical fixtures and 3,600s per solversample. The intentionally failing A13 regression is fixed in 156. |
| [#137](https://github.com/tscircuit/bus-lanes-solver/pull/137) | 🐌 Tiny | ShiboSoftwareDev | Reproduces the STMP157 fourth DDR data-byte failure using unchanged core capture, generating a failed solver SVG before asserting complete routing. |
| [#146](https://github.com/tscircuit/bus-lanes-solver/pull/146) | 🐌 Tiny | ShiboSoftwareDev | Reproduces a failure in routing the last eight data lines of the A64 TSX circuit after successfully routing the first 24, capturing the cores exact input and adding a failing SVG regression without changing production solver behavior. |
| [#134](https://github.com/tscircuit/bus-lanes-solver/pull/134) | 🐌 Tiny | seveibar | Adds a reproducible MT8395AVZA LPDDR4X routing case using the exact SimpleRouteJson emitted by cores built-in bus_lanes phase. Includes independent full-board (138 signals), byte-zero (11), and DQS-pair (2) captures, all retaining 1,446 pads. The replay loads this checkouts solver without adding global layers or modifying geometry, ownership, matching constraints, or via permissions. The repro includes pinned TSX recapture tooling, input hashes and signal names, baseline measurements, and a visual input snapshot. The snapshot labels dashed connections as unrouted airwires, refuses suppliedpartial copper, and has a narrowly scoped AGENTS exception for this requested diagnostic. Accepted output still requires complete connectivity, DRC, buspair matching, coupling, and an ownership-independent via-in-pad check. |

</details>

### [tscircuit/circuit-json-webgpu](https://github.com/tscircuit/circuit-json-webgpu)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#104](https://github.com/tscircuit/circuit-json-webgpu/pull/104) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Reuse the triangulation of large copper pours across scene changes, optimizing performance and memory usage during rendering. |
| [#102](https://github.com/tscircuit/circuit-json-webgpu/pull/102) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Writes vertices and indices directly into each typed-array chunk, optimizing the process by avoiding separate rest-argument arrays and chunk lookups for each vertex or index. |
| [#101](https://github.com/tscircuit/circuit-json-webgpu/pull/101) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Builds WebGPU mesh vertices and indices in fixed-size typed chunks, optimizing memory usage and performance during rendering. |

### [tscircuit/schematic-viewer](https://github.com/tscircuit/schematic-viewer)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#308](https://github.com/tscircuit/schematic-viewer/pull/308) | 🐙 Minor | ⭐⭐ | ShiboSoftwareDev | Adjusts the schematic viewer to fit the TMDS62LEVM sheet frame correctly and allows panning beyond the SVG viewport while clipping to the container. |

<details>
<summary>🐌 Tiny Contributions (1)</summary>

| PR # | Impact | Contributor | Description |
|------|--------|-------------|-------------|
| [#304](https://github.com/tscircuit/schematic-viewer/pull/304) | 🐌 Tiny | abdalraof-albarbar | Hides internal Circuit JSON IDs from the user-facing schematic component details popup, ensuring only meaningful fields are displayed. |

</details>

### [tscircuit/tscircuit](https://github.com/tscircuit/tscircuit)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#6238](https://github.com/tscircuit/tscircuit/pull/6238) | 🐙 Minor | ⭐⭐ | ShiboSoftwareDev | Fixes package updater failure due to missing core DDR benchmark dependency in the dependency sync process. |
| [#6143](https://github.com/tscircuit/tscircuit/pull/6143) | 🐙 Minor | ⭐⭐ | seveibar | Adds support for system block diagrams and integrates the Dagre library as a runtime dependency, enabling enhanced layout capabilities for system blocks in the tscircuit package. |

<details>
<summary>🐌 Tiny Contributions (96)</summary>

| PR # | Impact | Contributor | Description |
|------|--------|-------------|-------------|
| [#6214](https://github.com/tscircuit/tscircuit/pull/6214) | 🐌 Tiny | ShiboSoftwareDev | Excludes 11 CLI-only converters from core dependency synchronization to resolve package-update workflow failures caused by missing dependencies. |
| [#6203](https://github.com/tscircuit/tscircuit/pull/6203) | 🐌 Tiny | ShiboSoftwareDev | Fixes package update workflow failure by excluding the circuit-json-to-bom-csv converter from dependency sync as it is only used in assembly tests and a build smoke test. |
| [#6246](https://github.com/tscircuit/tscircuit/pull/6246) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6245](https://github.com/tscircuit/tscircuit/pull/6245) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6244](https://github.com/tscircuit/tscircuit/pull/6244) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6243](https://github.com/tscircuit/tscircuit/pull/6243) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6242](https://github.com/tscircuit/tscircuit/pull/6242) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6241](https://github.com/tscircuit/tscircuit/pull/6241) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6240](https://github.com/tscircuit/tscircuit/pull/6240) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6237](https://github.com/tscircuit/tscircuit/pull/6237) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6235](https://github.com/tscircuit/tscircuit/pull/6235) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6234](https://github.com/tscircuit/tscircuit/pull/6234) | 🐌 Tiny | tscircuitbot | Updates the package version from 0.0.3106 to 0.0.3107 in package.json |
| [#6232](https://github.com/tscircuit/tscircuit/pull/6232) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6231](https://github.com/tscircuit/tscircuit/pull/6231) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6230](https://github.com/tscircuit/tscircuit/pull/6230) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6229](https://github.com/tscircuit/tscircuit/pull/6229) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6224](https://github.com/tscircuit/tscircuit/pull/6224) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6222](https://github.com/tscircuit/tscircuit/pull/6222) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6221](https://github.com/tscircuit/tscircuit/pull/6221) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6219](https://github.com/tscircuit/tscircuit/pull/6219) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6210](https://github.com/tscircuit/tscircuit/pull/6210) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6209](https://github.com/tscircuit/tscircuit/pull/6209) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6208](https://github.com/tscircuit/tscircuit/pull/6208) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6206](https://github.com/tscircuit/tscircuit/pull/6206) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6205](https://github.com/tscircuit/tscircuit/pull/6205) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6202](https://github.com/tscircuit/tscircuit/pull/6202) | 🐌 Tiny | tscircuitbot | Updates the package version from 0.0.3092 to 0.0.3093 in package.json |
| [#6201](https://github.com/tscircuit/tscircuit/pull/6201) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6199](https://github.com/tscircuit/tscircuit/pull/6199) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6197](https://github.com/tscircuit/tscircuit/pull/6197) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6196](https://github.com/tscircuit/tscircuit/pull/6196) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6194](https://github.com/tscircuit/tscircuit/pull/6194) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6193](https://github.com/tscircuit/tscircuit/pull/6193) | 🐌 Tiny | tscircuitbot | Updates the tscircuitcli package version from 0.1.2436 to 0.1.2437 |
| [#6191](https://github.com/tscircuit/tscircuit/pull/6191) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6189](https://github.com/tscircuit/tscircuit/pull/6189) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6188](https://github.com/tscircuit/tscircuit/pull/6188) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6187](https://github.com/tscircuit/tscircuit/pull/6187) | 🐌 Tiny | tscircuitbot | Automated package update to version 0.0.3086 |
| [#6186](https://github.com/tscircuit/tscircuit/pull/6186) | 🐌 Tiny | tscircuitbot | Updates the tscircuitcli package version from 0.1.2435 to 0.1.2436 in package.json |
| [#6185](https://github.com/tscircuit/tscircuit/pull/6185) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6181](https://github.com/tscircuit/tscircuit/pull/6181) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6180](https://github.com/tscircuit/tscircuit/pull/6180) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6179](https://github.com/tscircuit/tscircuit/pull/6179) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6178](https://github.com/tscircuit/tscircuit/pull/6178) | 🐌 Tiny | tscircuitbot | Updates the tscircuitcore package from version 0.0.2267 to 0.0.2268 |
| [#6177](https://github.com/tscircuit/tscircuit/pull/6177) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6176](https://github.com/tscircuit/tscircuit/pull/6176) | 🐌 Tiny | tscircuitbot | Updates the tscircuitcli package to version 0.1.2434 |
| [#6175](https://github.com/tscircuit/tscircuit/pull/6175) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6173](https://github.com/tscircuit/tscircuit/pull/6173) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6172](https://github.com/tscircuit/tscircuit/pull/6172) | 🐌 Tiny | tscircuitbot | Updates the tscircuitcli package to version 0.1.2433 |
| [#6169](https://github.com/tscircuit/tscircuit/pull/6169) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6168](https://github.com/tscircuit/tscircuit/pull/6168) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6167](https://github.com/tscircuit/tscircuit/pull/6167) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6166](https://github.com/tscircuit/tscircuit/pull/6166) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6163](https://github.com/tscircuit/tscircuit/pull/6163) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6160](https://github.com/tscircuit/tscircuit/pull/6160) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6159](https://github.com/tscircuit/tscircuit/pull/6159) | 🐌 Tiny | tscircuitbot | Updates the tscircuitcli package to version 0.1.2432 |
| [#6158](https://github.com/tscircuit/tscircuit/pull/6158) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6157](https://github.com/tscircuit/tscircuit/pull/6157) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6155](https://github.com/tscircuit/tscircuit/pull/6155) | 🐌 Tiny | tscircuitbot | Updates the tscircuitcli package to version 0.1.2431 in package.json |
| [#6154](https://github.com/tscircuit/tscircuit/pull/6154) | 🐌 Tiny | tscircuitbot | Updates the package version from 0.0.3069 to 0.0.3070 in package.json |
| [#6149](https://github.com/tscircuit/tscircuit/pull/6149) | 🐌 Tiny | tscircuitbot | Updates the tscircuitcli package to version 0.1.2430 in the package.json file |
| [#6148](https://github.com/tscircuit/tscircuit/pull/6148) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6146](https://github.com/tscircuit/tscircuit/pull/6146) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6145](https://github.com/tscircuit/tscircuit/pull/6145) | 🐌 Tiny | tscircuitbot | Updates the versions of the tscircuitrunframe and tscircuiteval packages in the project dependencies. |
| [#6144](https://github.com/tscircuit/tscircuit/pull/6144) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6142](https://github.com/tscircuit/tscircuit/pull/6142) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6236](https://github.com/tscircuit/tscircuit/pull/6236) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6228](https://github.com/tscircuit/tscircuit/pull/6228) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6226](https://github.com/tscircuit/tscircuit/pull/6226) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6225](https://github.com/tscircuit/tscircuit/pull/6225) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6211](https://github.com/tscircuit/tscircuit/pull/6211) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6207](https://github.com/tscircuit/tscircuit/pull/6207) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6200](https://github.com/tscircuit/tscircuit/pull/6200) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6198](https://github.com/tscircuit/tscircuit/pull/6198) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6184](https://github.com/tscircuit/tscircuit/pull/6184) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6183](https://github.com/tscircuit/tscircuit/pull/6183) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6171](https://github.com/tscircuit/tscircuit/pull/6171) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6165](https://github.com/tscircuit/tscircuit/pull/6165) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6162](https://github.com/tscircuit/tscircuit/pull/6162) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6156](https://github.com/tscircuit/tscircuit/pull/6156) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6150](https://github.com/tscircuit/tscircuit/pull/6150) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6233](https://github.com/tscircuit/tscircuit/pull/6233) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6227](https://github.com/tscircuit/tscircuit/pull/6227) | 🐌 Tiny | tscircuitbot | Updates the tscircuitcli package version from 0.1.2442 to 0.1.2443 |
| [#6220](https://github.com/tscircuit/tscircuit/pull/6220) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6216](https://github.com/tscircuit/tscircuit/pull/6216) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6215](https://github.com/tscircuit/tscircuit/pull/6215) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6195](https://github.com/tscircuit/tscircuit/pull/6195) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6192](https://github.com/tscircuit/tscircuit/pull/6192) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6182](https://github.com/tscircuit/tscircuit/pull/6182) | 🐌 Tiny | tscircuitbot | Updates the tscircuitcli package to version 0.1.2435 in package.json |
| [#6174](https://github.com/tscircuit/tscircuit/pull/6174) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6170](https://github.com/tscircuit/tscircuit/pull/6170) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6152](https://github.com/tscircuit/tscircuit/pull/6152) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6153](https://github.com/tscircuit/tscircuit/pull/6153) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6151](https://github.com/tscircuit/tscircuit/pull/6151) | 🐌 Tiny | tscircuitbot | Updates the version of tscircuitcore from 0.0.2261 to 0.0.2263 and tscircuitmodelprinter from 0.0.18 to 0.0.37 in package.json |
| [#6147](https://github.com/tscircuit/tscircuit/pull/6147) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6223](https://github.com/tscircuit/tscircuit/pull/6223) | 🐌 Tiny | seveibar | Updates the circuit-json-to-gltf package to version 0.0.165 to resolve an import failure related to the footprinter dependency. |
| [#6161](https://github.com/tscircuit/tscircuit/pull/6161) | 🐌 Tiny | MustafaMulla29 | Updates tscircuiteval from 0.0.1700 to 0.0.1701 to bring in parts-engine 0.0.41  EasyEDA 0.0.389 update. |
| [#6164](https://github.com/tscircuit/tscircuit/pull/6164) | 🐌 Tiny | MustafaMulla29 | Regenerates bun.lock to match the manifest and resolves the direct eval dependency to 0.0.1701, while retaining 0.0.1700 for the existing nested tscircuit dependency. |

</details>

### [tscircuit/runframe](https://github.com/tscircuit/runframe)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#6111](https://github.com/tscircuit/runframe/pull/6111) | 🐳 Major | ⭐⭐⭐ | abdalraof-albarbar | Fixes autorouting failure when selecting AutoroutingPipelineSolver9_PreloadedTraceGraph due to undefined properties in solver parameters. |
| [#6079](https://github.com/tscircuit/runframe/pull/6079) | 🐳 Major | ⭐⭐⭐ | seveibar | Add System to RunFrames More views dropdown and render System pages with tscircuitsystem-block-viewer. This displays the resolved geometry emitted by system block TSX. |
| [#6089](https://github.com/tscircuit/runframe/pull/6089) | 🐳 Major | ⭐⭐⭐ | rushabhcodes | Adds Drawing to More views, using a direct DrawingViewer import like the existing viewer integrations. Runframe forwards Circuit JSON and provides tab selectionavailability, shared panel sizing, the empty preview state, and an error boundary that resets when the circuit changes. |
| [#6109](https://github.com/tscircuit/runframe/pull/6109) | 🐙 Minor | ⭐⭐ | abdalraof-albarbar | Fixes stale solver debugger when switching between different solvers in the Solvers tab, ensuring the correct debugger state is displayed for the selected solver. |
| [#6085](https://github.com/tscircuit/runframe/pull/6085) | 🐙 Minor | ⭐⭐ | seveibar | Enables navigation from System block components to their corresponding schematic symbols, highlighting the selected symbol in the schematic view. |
| [#6134](https://github.com/tscircuit/runframe/pull/6134) | 🐙 Minor | ⭐⭐ | Abse2001 | Updates the compatible dependency set for the 3D viewer to resolve issues with core and props exports, enabling successful viewer updates. |

<details>
<summary>🐌 Tiny Contributions (56)</summary>

| PR # | Impact | Contributor | Description |
|------|--------|-------------|-------------|
| [#6138](https://github.com/tscircuit/runframe/pull/6138) | 🐌 Tiny | ShiboSoftwareDev | Updates the core dependency to remove a transitive JS CDN dependency that causes installation failures for consumers using newer core versions. |
| [#6098](https://github.com/tscircuit/runframe/pull/6098) | 🐌 Tiny | ShiboSoftwareDev | Moves tscircuitsystem-block-viewer back to devDependencies to resolve npm-install audit failures caused by its previous placement in runtime dependencies. |
| [#6144](https://github.com/tscircuit/runframe/pull/6144) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1708 to 0.0.1709 |
| [#6143](https://github.com/tscircuit/runframe/pull/6143) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6142](https://github.com/tscircuit/runframe/pull/6142) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1707 to 0.0.1708 |
| [#6141](https://github.com/tscircuit/runframe/pull/6141) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6140](https://github.com/tscircuit/runframe/pull/6140) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1706 to 0.0.1707 |
| [#6139](https://github.com/tscircuit/runframe/pull/6139) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6135](https://github.com/tscircuit/runframe/pull/6135) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6130](https://github.com/tscircuit/runframe/pull/6130) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6129](https://github.com/tscircuit/runframe/pull/6129) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1704 to 0.0.1706 in the package.json file. |
| [#6128](https://github.com/tscircuit/runframe/pull/6128) | 🐌 Tiny | tscircuitbot | Updates the tscircuitpcb-viewer package to version 1.11.450 |
| [#6127](https://github.com/tscircuit/runframe/pull/6127) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6126](https://github.com/tscircuit/runframe/pull/6126) | 🐌 Tiny | tscircuitbot | Updates the tscircuitschematic-viewer package from version 2.0.107 to 2.0.108 |
| [#6077](https://github.com/tscircuit/runframe/pull/6077) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1697 to 0.0.1698 |
| [#6120](https://github.com/tscircuit/runframe/pull/6120) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6112](https://github.com/tscircuit/runframe/pull/6112) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6108](https://github.com/tscircuit/runframe/pull/6108) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6101](https://github.com/tscircuit/runframe/pull/6101) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6096](https://github.com/tscircuit/runframe/pull/6096) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6081](https://github.com/tscircuit/runframe/pull/6081) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6078](https://github.com/tscircuit/runframe/pull/6078) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6075](https://github.com/tscircuit/runframe/pull/6075) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1696 to 0.0.1697 |
| [#6067](https://github.com/tscircuit/runframe/pull/6067) | 🐌 Tiny | tscircuitbot | Updates the circuit-json-to-kicad package version from 0.0.263 to 0.0.265 in package.json |
| [#6124](https://github.com/tscircuit/runframe/pull/6124) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6122](https://github.com/tscircuit/runframe/pull/6122) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6119](https://github.com/tscircuit/runframe/pull/6119) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1701 to 0.0.1702 |
| [#6117](https://github.com/tscircuit/runframe/pull/6117) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6116](https://github.com/tscircuit/runframe/pull/6116) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1700 to 0.0.1701 |
| [#6115](https://github.com/tscircuit/runframe/pull/6115) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6114](https://github.com/tscircuit/runframe/pull/6114) | 🐌 Tiny | tscircuitbot | Updates the tscircuitpcb-viewer package to version 1.11.449 in the package.json file. |
| [#6110](https://github.com/tscircuit/runframe/pull/6110) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6103](https://github.com/tscircuit/runframe/pull/6103) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6100](https://github.com/tscircuit/runframe/pull/6100) | 🐌 Tiny | tscircuitbot | Updates the tscircuitpcb-viewer package to version 1.11.447 |
| [#6095](https://github.com/tscircuit/runframe/pull/6095) | 🐌 Tiny | tscircuitbot | Updates the tscircuitpcb-viewer package to version 1.11.446 |
| [#6092](https://github.com/tscircuit/runframe/pull/6092) | 🐌 Tiny | tscircuitbot | Updates the tscircuitpcb-viewer package to version 1.11.445 |
| [#6090](https://github.com/tscircuit/runframe/pull/6090) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6088](https://github.com/tscircuit/runframe/pull/6088) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6087](https://github.com/tscircuit/runframe/pull/6087) | 🐌 Tiny | tscircuitbot | Updates the circuit-json-to-kicad package version from 0.0.265 to 0.0.267 in package.json |
| [#6083](https://github.com/tscircuit/runframe/pull/6083) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6082](https://github.com/tscircuit/runframe/pull/6082) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1699 to 0.0.1700 |
| [#6080](https://github.com/tscircuit/runframe/pull/6080) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1698 to 0.0.1699 |
| [#6065](https://github.com/tscircuit/runframe/pull/6065) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6064](https://github.com/tscircuit/runframe/pull/6064) | 🐌 Tiny | tscircuitbot | Updates the tscircuitpcb-viewer package to version 1.11.443 |
| [#6113](https://github.com/tscircuit/runframe/pull/6113) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6102](https://github.com/tscircuit/runframe/pull/6102) | 🐌 Tiny | tscircuitbot | Updates the tscircuitpcb-viewer package to version 1.11.448 |
| [#6099](https://github.com/tscircuit/runframe/pull/6099) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6073](https://github.com/tscircuit/runframe/pull/6073) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6068](https://github.com/tscircuit/runframe/pull/6068) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6123](https://github.com/tscircuit/runframe/pull/6123) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1703 to 0.0.1704 |
| [#6121](https://github.com/tscircuit/runframe/pull/6121) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1702 to 0.0.1703 |
| [#6107](https://github.com/tscircuit/runframe/pull/6107) | 🐌 Tiny | tscircuitbot | Updates the tscircuitschematic-viewer package from version 2.0.106 to 2.0.107 |
| [#6076](https://github.com/tscircuit/runframe/pull/6076) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#6072](https://github.com/tscircuit/runframe/pull/6072) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1695 to 0.0.1696 |
| [#6071](https://github.com/tscircuit/runframe/pull/6071) | 🐌 Tiny | imrishabh18 | Updates the tscircuitpcb-viewer dependency to version 1.11.444 to include a fix for hover label and outline clipping issues. |
| [#6094](https://github.com/tscircuit/runframe/pull/6094) | 🐌 Tiny | seveibar | Upgrades the System viewer to the published jscdn 0.0.5 release and declares it as a runtime dependency, ensuring curved routes work in standalone previews. |

</details>

### [tscircuit/circuit-json](https://github.com/tscircuit/circuit-json)

| PR # | Impact | Rating | Contributor | Description |
|------|---