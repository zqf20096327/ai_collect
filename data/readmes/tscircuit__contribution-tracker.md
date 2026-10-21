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

# Contribution Overview 2026-10-13

The current week is shown below. There are 3 major sections:

- [Contributor Overview](#contributor-overview)
- [PRs by Repository](#prs-by-repository)
- [PRs by Contributor](#changes-by-contributor)
- [Scoring & Sponsorship Details](/docs/sponsorship-calculation-explanation.md)

## PRs by Repository

```mermaid
pie
    "tscircuit/core" : 56
    "tscircuit/checks" : 7
    "tscircuit/tscircuit.com" : 71
    "tscircuit/cli" : 109
    "tscircuit/tscircuit-autorouter" : 32
    "tscircuit/parts-engine" : 2
    "tscircuit/circuit-json-to-gltf" : 2
    "tscircuit/solver-utils" : 2
    "tscircuit/fanout-solver" : 1
    "tscircuit/bus-lanes-solver" : 5
    "tscircuit/motorcontrol" : 25
    "tscircuit/single-layer-grid-router" : 1
    "tscircuit/schematic-viewer" : 1
    "tscircuit/props" : 3
    "tscircuit/circuit-json-to-gerber" : 3
    "tscircuit/internal-dynamic-import" : 5
    "tscircuit/circuit-json-webgpu" : 12
    "tscircuit/tscircuit-standalone" : 14
    "tscircuit/easyeda-converter" : 4
    "tscircuit/circuit-json-to-kicad" : 25
    "tscircuit/stepts" : 4
    "tscircuit/pcb-viewer" : 5
    "tscircuit/tscircuit" : 203
    "tscircuit/eval" : 67
    "tscircuit/runframe" : 103
    "tscircuit/svg.tscircuit.com" : 61
    "tscircuit/circuit-json-to-step" : 18
    "tscircuit/test-github-automerge" : 1
    "tscircuit/rectdiff" : 2
    "tscircuit/circuit-json-schematic-placement-analysis" : 46
    "tscircuit/3d-viewer" : 6
    "tscircuit/circuit-json-to-connectivity-map" : 2
    "tscircuit/circuit-json-to-tscircuit" : 4
    "tscircuit/schematic-symbols" : 5
    "tscircuit/altium-to-circuit-json" : 1
    "tscircuit/circuit-json" : 1
    "tscircuit/dataset-tsx35-kicad-boards" : 4
    "tscircuit/circuit-json-util" : 1
    "tscircuit/footprinter" : 7
    "tscircuit/circuit-to-svg" : 2
    "tscircuit/ti" : 3
    "tscircuit/sysconfigts" : 1
    "tscircuit/models.tscircuit.com" : 2
    "tscircuit/jscad-electronics" : 1
    "tscircuit/modelprinter" : 1
    "tscircuit/docs" : 1
    "tscircuit/circuit-to-canvas" : 1
    "tscircuit/circuit-json-placement-analysis" : 2
    "tscircuit/dataset-srj24" : 2
    "tscircuit/copper-pour-solver" : 4
    "tscircuit/kicad-to-circuit-json" : 1
    "tscircuit/circuit-json-to-bom-csv" : 2
```

## Contributor Overview

| Contributor | 🐳 Major | 🐙 Minor | 🐌 Tiny | Score | ⭐ |
|-------------|---------|---------|---------|-------|-----|
| [seveibar](#seveibar) | 26 | 25 | 18 | 167 | 👑👑👑 |
| [imrishabh18](#imrishabh18) | 22 | 15 | 24 | 131 | 👑👑 |
| [ShiboSoftwareDev](#ShiboSoftwareDev) | 9 | 8 | 10 | 77 | ⭐⭐⭐ |
| [MustafaMulla29](#MustafaMulla29) | 6 | 14 | 28 | 65 | ⭐⭐⭐ |
| [techmannih](#techmannih) | 7 | 1 | 10 | 41 | ⭐⭐ |
| [rushabhcodes](#rushabhcodes) | 2 | 8 | 7 | 32 | ⭐⭐ |
| [Abse2001](#Abse2001) | 0 | 3 | 4 | 25 | ⭐⭐ |
| [GokulPandi-M](#GokulPandi-M) | 1 | 4 | 7 | 19 | ⭐⭐ |
| [tscircuitbot](#tscircuitbot) | 0 | 0 | 625 | 18 | ⭐⭐ |
| [0hmX](#0hmX) | 3 | 1 | 2 | 17 | ⭐⭐ |
| [trixie010](#trixie010) | 1 | 6 | 1 | 17 | ⭐⭐ |
| [Devesh36](#Devesh36) | 1 | 2 | 7 | 16 | ⭐⭐ |
| [AnasSarkiz](#AnasSarkiz) | 2 | 2 | 3 | 15 | ⭐⭐ |
| [anil08607](#anil08607) | 0 | 3 | 8 | 14 | ⭐⭐ |
| [hrithik18k](#hrithik18k) | 1 | 4 | 1 | 13 | ⭐⭐ |
| [KrishnaX12](#KrishnaX12) | 0 | 4 | 3 | 11 | ⭐⭐ |
| [mohan-bee](#mohan-bee) | 0 | 3 | 1 | 8 | ⭐ |
| [raykholo](#raykholo) | 0 | 0 | 1 | 1 |  |

## Staff Pass Ratio (SPR)

| Contributor | Reviewed PRs | Rejections | Approvals | SPR |
|-------------|--------------|------------|-----------|-----|
| [imrishabh18](#imrishabh18) | 12 | 0 | 12 | 100.0% |
| [MustafaMulla29](#MustafaMulla29) | 10 | 1 | 10 | 90.0% |
| [0hmX](#0hmX) | 6 | 1 | 5 | 83.3% |
| [rushabhcodes](#rushabhcodes) | 5 | 0 | 5 | 100.0% |
| [Abse2001](#Abse2001) | 3 | 0 | 3 | 100.0% |
| [techmannih](#techmannih) | 3 | 2 | 2 | 33.3% |
| [trixie010](#trixie010) | 3 | 0 | 3 | 100.0% |
| [AnasSarkiz](#AnasSarkiz) | 1 | 0 | 1 | 100.0% |
| [hrithik18k](#hrithik18k) | 1 | 1 | 0 | 0.0% |
| [mohan-bee](#mohan-bee) | 1 | 0 | 1 | 100.0% |
| [raykholo](#raykholo) | 1 | 0 | 1 | 100.0% |
| [ShiboSoftwareDev](#ShiboSoftwareDev) | 1 | 0 | 1 | 100.0% |

<details>
<summary>imrishabh18 SPR PRs (12)</summary>

- [#5395](https://github.com/tscircuit/cli/pull/5395) Search baked datasheets in standalone
- [#5390](https://github.com/tscircuit/cli/pull/5390) Route standalone imports through the baked asset server
- [#5384](https://github.com/tscircuit/cli/pull/5384) Use embedded eval worker configuration for standalone dev
- [#5388](https://github.com/tscircuit/cli/pull/5388) Block network fallbacks for standalone imports
- [#5368](https://github.com/tscircuit/cli/pull/5368) Serve baked assets and expose parts-engine base URLs
- [#5344](https://github.com/tscircuit/cli/pull/5344) Copy prepared JS CDN packages for static site builds
- [#5348](https://github.com/tscircuit/cli/pull/5348) Serve prepared JS CDN packages in tsci dev
- [#5324](https://github.com/tscircuit/cli/pull/5324) Add --jscdn-base-url to static site builds
- [#67](https://github.com/tscircuit/parts-engine/pull/67) Support configurable provider base URLs
- [#38](https://github.com/tscircuit/internal-dynamic-import/pull/38) Support window.TSCIRCUIT_JSCDN_BASE_URL for browser imports
- [#16](https://github.com/tscircuit/tscircuit-standalone/pull/16) Add macOS terminal installation without browser quarantine
- [#11](https://github.com/tscircuit/tscircuit-standalone/pull/11) Launch shared CLI with bundled RunFrame JS CDN packages

</details>

<details>
<summary>MustafaMulla29 SPR PRs (10)</summary>

- [#4799](https://github.com/tscircuit/core/pull/4799) Stop emitting deprecated from_layer/to_layer on pcb_via
- [#4649](https://github.com/tscircuit/core/pull/4649) Preserve required schematic branches when removing redundant net-label wires
- [#4596](https://github.com/tscircuit/core/pull/4596) Add standalone solder paste apertures
- [#338](https://github.com/tscircuit/circuit-json-schematic-placement-analysis/pull/338) Detect fuse connector misalignment
- [#284](https://github.com/tscircuit/circuit-json-schematic-placement-analysis/pull/284) feat: detect resistors separated from crystals
- [#291](https://github.com/tscircuit/circuit-json-schematic-placement-analysis/pull/291) feat: detect misaligned parallel diode capacitor pairs
- [#288](https://github.com/tscircuit/circuit-json-schematic-placement-analysis/pull/288) feat: detect parallel LED branches drawn inline
- [#271](https://github.com/tscircuit/circuit-json-schematic-placement-analysis/pull/271) feat: detect ungrouped switch RC networks
- [#249](https://github.com/tscircuit/circuit-json-schematic-placement-analysis/pull/249) feat: detect separated switch diodes and excessive matrix spacing
- [#277](https://github.com/tscircuit/circuit-json-schematic-placement-analysis/pull/277) feat: detect inline parallel capacitor pairs

</details>

<details>
<summary>0hmX SPR PRs (6)</summary>

- [#908](https://github.com/tscircuit/circuit-json/pull/908) Add external IBIS transient simulation records
- [#910](https://github.com/tscircuit/circuit-json/pull/910) Store optional JLCPCB stackup ID on PCB boards
- [#945](https://github.com/tscircuit/props/pull/945) Add props for external IBIS transient simulations
- [#4765](https://github.com/tscircuit/core/pull/4765) Render external IBIS simulation declarations from TSX
- [#4529](https://github.com/tscircuit/core/pull/4529) fix: report disallowed blind/buried vias in manual paths
- [#442](https://github.com/tscircuit/checks/pull/442) Repro: missed dead-end copper pour finger on a UART adapter

</details>

<details>
<summary>rushabhcodes SPR PRs (5)</summary>

- [#930](https://github.com/tscircuit/footprinter/pull/930) fix: parse explicit polarity pins in LED footprint strings
- [#4624](https://github.com/tscircuit/core/pull/4624) fix: honor oval plated-hole rotation during autorouting
- [#4571](https://github.com/tscircuit/core/pull/4571) Fix footprint keepouts staying behind after PCB layout
- [#4570](https://github.com/tscircuit/core/pull/4570) fix: respect rotated pad geometry when assigning routed source traces
- [#857](https://github.com/tscircuit/circuit-to-svg/pull/857) fix: default polygon-pad drill offsets to zero

</details>

<details>
<summary>Abse2001 SPR PRs (3)</summary>

- [#1088](https://github.com/tscircuit/pcb-viewer/pull/1088) feat: search PCB components and briefly highlight results
- [#943](https://github.com/tscircuit/props/pull/943) Add symbol contain fitting and an explicit local viewbox (#4698)
- [#197](https://github.com/tscircuit/circuit-json-to-gerber/pull/197) Preserve filled fabrication polarity artwork on a real LED board

</details>

<details>
<summary>techmannih SPR PRs (3)</summary>

- [#4641](https://github.com/tscircuit/core/pull/4641) Fix polygon cutout coverage gaps in generated routing obstacles
- [#4597](https://github.com/tscircuit/core/pull/4597) Preserve native keepout outlines with verified autorouter coverage
- [#3054](https://github.com/tscircuit/tscircuit-autorouter/pull/3054) Preserve coverage of unconnected rotated keepouts

</details>

<details>
<summary>trixie010 SPR PRs (3)</summary>

- [#598](https://github.com/tscircuit/easyeda-converter/pull/598) fix: stop emitting a duplicate pcb_cutout for every HOLE record
- [#153](https://github.com/tscircuit/circuit-json-to-step/pull/153) repro: circular holes are only half cut in STEP exports
- [#149](https://github.com/tscircuit/circuit-json-to-step/pull/149) fix: honour pcb_plated_hole drill offset and route every variant

</details>

<details>
<summary>AnasSarkiz SPR PRs (1)</summary>

- [#605](https://github.com/tscircuit/easyeda-converter/pull/605) fix: preserve non-plated hole shapes and rotation in generated TSX

</details>

<details>
<summary>hrithik18k SPR PRs (1)</summary>

- [#861](https://github.com/tscircuit/circuit-to-svg/pull/861) Fix route-via dimensions and standalone via deduplication

</details>

<details>
<summary>mohan-bee SPR PRs (1)</summary>

- [#4378](https://github.com/tscircuit/core/pull/4378) preserve initial rectangular cutout rotation and bounds

</details>

<details>
<summary>raykholo SPR PRs (1)</summary>

- [#636](https://github.com/tscircuit/circuit-json-to-kicad/pull/636) Export pcb_via tenting to KiCad vias

</details>

<details>
<summary>ShiboSoftwareDev SPR PRs (1)</summary>

- [#58](https://github.com/tscircuit/circuit-json-to-connectivity-map/pull/58) Index connected network membership

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
| [0hmX](#0hmX) | 36 | 5 | 2 | 9 | 0 | 21 | 6 | 0 |
| [Abse2001](#Abse2001) | 5 | 4 | 0 | 16 | 1 | 20 | 7 | 0 |
| [adamscarmccoy-boop](#adamscarmccoy-boop) | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 |
| [amartya1523](#amartya1523) | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 |
| [AnasSarkiz](#AnasSarkiz) | 7 | 7 | 0 | 0 | 0 | 8 | 7 | 0 |
| [anil08607](#anil08607) | 20 | 16 | 3 | 0 | 0 | 17 | 11 | 0 |
| [ArnavK-09](#ArnavK-09) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [atani](#atani) | 24 | 0 | 0 | 0 | 0 | 16 | 0 | 0 |
| [CloudCorpRecords](#CloudCorpRecords) | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| [CreedTech](#CreedTech) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [daniellachev](#daniellachev) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [deus-intus](#deus-intus) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [Devesh36](#Devesh36) | 14 | 10 | 1 | 1 | 0 | 19 | 10 | 0 |
| [duongynhi000005-oss](#duongynhi000005-oss) | 0 | 0 | 0 | 0 | 0 | 157 | 0 | 0 |
| [DurandA](#DurandA) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [elcuervo171234](#elcuervo171234) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [gelismarvel](#gelismarvel) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [GokulPandi-M](#GokulPandi-M) | 17 | 13 | 2 | 0 | 0 | 16 | 12 | 0 |
| [hiyouwhatsapp](#hiyouwhatsapp) | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 |
| [hrithik18k](#hrithik18k) | 23 | 7 | 5 | 0 | 0 | 23 | 6 | 0 |
| [huynhnhatquandongnai-source](#huynhnhatquandongnai-source) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [imrishabh18](#imrishabh18) | 27 | 21 | 0 | 43 | 21 | 74 | 61 | 0 |
| [jloa-dev](#jloa-dev) | 0 | 0 | 0 | 0 | 0 | 31 | 0 | 0 |
| [JohnNuwan](#JohnNuwan) | 0 | 0 | 0 | 0 | 0 | 9 | 0 | 0 |
| [Keven-Crick](#Keven-Crick) | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| [KrishnaX12](#KrishnaX12) | 10 | 8 | 0 | 0 | 0 | 11 | 7 | 0 |
| [LuisaW07](#LuisaW07) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [mohan-bee](#mohan-bee) | 5 | 3 | 1 | 1 | 0 | 33 | 4 | 0 |
| [mukesh-dev-git](#mukesh-dev-git) | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 0 |
| [MustafaMulla29](#MustafaMulla29) | 32 | 22 | 3 | 15 | 0 | 62 | 50 | 0 |
| [oziass](#oziass) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [Pr1yansu](#Pr1yansu) | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 |
| [prajwal-0706](#prajwal-0706) | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 |
| [proofline-studio](#proofline-studio) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [QAQTam](#QAQTam) | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 |
| [Ratanlavate](#Ratanlavate) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [raykholo](#raykholo) | 2 | 2 | 0 | 0 | 0 | 12 | 2 | 0 |
| [rjwalters](#rjwalters) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [robertomartinezconsultor](#robertomartinezconsultor) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [rushabhcodes](#rushabhcodes) | 84 | 23 | 5 | 1 | 0 | 39 | 18 | 0 |
| [ryder777777](#ryder777777) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [Sayandevxyz](#Sayandevxyz) | 0 | 0 | 0 | 0 | 0 | 75 | 0 | 0 |
| [sebas8866](#sebas8866) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [seveibar](#seveibar) | 19 | 1 | 0 | 50 | 3 | 105 | 69 | 0 |
| [ShiboSoftwareDev](#ShiboSoftwareDev) | 27 | 21 | 0 | 42 | 0 | 143 | 27 | 0 |
| [smartcalsystems-sketch](#smartcalsystems-sketch) | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 |
| [tarazum](#tarazum) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [techmannih](#techmannih) | 38 | 13 | 2 | 11 | 2 | 34 | 18 | 0 |
| [trixie010](#trixie010) | 21 | 13 | 3 | 0 | 0 | 12 | 8 | 0 |
| [tscircuitbot](#tscircuitbot) | 0 | 0 | 0 | 0 | 0 | 789 | 625 | 0 |
| [venkateshyadagiri468](#venkateshyadagiri468) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [vreview](#vreview) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [WilliamxLeismer](#WilliamxLeismer) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| [ZhaZhaBei](#ZhaZhaBei) | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |

## Changes by Repository

### [tscircuit/core](https://github.com/tscircuit/core)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#4667](https://github.com/tscircuit/core/pull/4667) | 🐳 Major | ⭐⭐⭐ | seveibar | Supplier Circuit JSON can contain permanent internal pin groups, but core discards those groups while importing the footprint. Retain the groups as derived component metadata, resolve supplier-local source-port IDs to component pin names, and use them for emitted source connectivity and missing-trace checks. Explicit internallyConnectedPins, including , takes precedence without mutating user props or imported Circuit JSON. Groundpower connection queries now follow permanent internal contacts on both ends of a trace; overlapping groups are traversed transitively. Ground attributes and aliases take precedence over fallback power-name detection, so a ground ball address such as V3 does not disable automatic decoupling trace limits when reached through an internal group. Push buttons opt into parts-engine datasheet enrichment so a four-terminal switch can share AB and CD without connecting its momentary switch terminals. Runtime datasheet enrichment requires the parts-engine change in https:github.comtscircuitparts-enginepull68 to be published and used by the calling parts engine. This PR consumes the existing Circuit JSON internal-connection field and needs no schema change. Source design-rule checks also compare the explicit internallyConnectedPins prop against datasheet groups and warn when a reported connection is missing from the declaration. For example: The datasheet reports pins A and B are internally connected, but the internallyConnectedPins prop isnt set on SW1. Imported defaults do not suppress this warning. Empty or incomplete declarations warn too; pin aliases, numbers, and transitive groups count as equivalent declarations. Warnings update or disappear when the declaration changes, and respect the DRC disable controls. Custom-footprint chips, pushbuttons, and op amps can fetch comparison metadata even without pinAttributes; supplier-footprint imports reuse their existing metadata request. Fetching comparison facts does not replace custom geometry or mutate props. Validation: 25 focused tests pass, including suppliercustom footprint warnings, missing and empty declarations, equivalent aliasestransitive groups, disabled checks, warning updates, imported connectivity, and existing datasheet pin-attribute checks. Labeled PCB snapshots are included and visually reviewed. Package build, typecheck, and formatting pass. Related PRs: website https:github.comtscircuittscircuit.compull5454; core https:github.comtscircuitcorepull4667; CLI https:github.comtscircuitclipull5397; parts engine https:github.comtscircuitparts-enginepull68. Homepage smoke test: rebuilt the exact homepage releases of seveibarnrf-smart-watch0.1.1, imrishabh18rp2040-motor-controller1.0.41, absewifi-smart-switch1.0.29, and absegameboy1.0.15 against the PR and its base, using the same cached live network responses and the parts-engine internal-pin support. All 274 components rendered with identical diagnostics after the routing-disable fix. This check keeps autorouting disabled. Async datasheet validation now respects routing-disable controls on update, preventing routing diagnostics during a disabled-routing render. A regression test covers both platform and board controls. seveibarf1c100s-linux-dev-board1.9.2 fails on both versions before rendering: its routingBoundaryRef callback calls the absent internal method doInitialPcbImplicitCopperPourRender. This existing compatibility issue prevents a complete smoke test of that board. |
| [#4604](https://github.com/tscircuit/core/pull/4604) | 🐳 Major | ⭐⭐⭐ | seveibar | Allows chips and connectors to use physical BGA ball names directly in pinLabels, connections, footprint hints, schematic arrangements, and pin styles, resolving previous issues with alias resolution. |
| [#4603](https://github.com/tscircuit/core/pull/4603) | 🐳 Major | ⭐⭐⭐ | seveibar | Fixes autorouting failure by resolving bare trace names and explicit trace selectors, ensuring proper diagnostics for unmatched or ambiguous selectors. |
| [#4624](https://github.com/tscircuit/core/pull/4624) | 🐳 Major | ⭐⭐⭐ | rushabhcodes | Fixes autorouting issues by ensuring that oval plated-hole dimensions are correctly rotated and used as routing obstacles during PCB design. |
| [#4689](https://github.com/tscircuit/core/pull/4689) | 🐳 Major | ⭐⭐⭐ | techmannih | Fixes the omission of the via-in-pad policy during SRJ conversion, ensuring that the routing input retains the boards permission for vias in pads. |
| [#4597](https://github.com/tscircuit/core/pull/4597) | 🐳 Major | ⭐⭐⭐ | techmannih | Reduces the number of SRJ obstacles from 1430 to 475 for open keepout arcs while ensuring full coverage during autorouting. |
| [#4602](https://github.com/tscircuit/core/pull/4602) | 🐳 Major | ⭐⭐⭐ | techmannih | Records the behavior of Sample024s five open keepout arcs expanding into 1,430 SRJ obstacles while leaving sampled points uncovered, with visual reproductions and tests. |
| [#4669](https://github.com/tscircuit/core/pull/4669) | 🐳 Major | ⭐⭐⭐ | techmannih | Preserves native keepout outlines and improves autorouter coverage by implementing an approved patch from a previous pull request, ensuring no uncovered stroke points and reducing obstacles significantly. |
| [#4596](https://github.com/tscircuit/core/pull/4596) | 🐳 Major | ⭐⭐⭐ | MustafaMulla29 | Problem and change solderpaste is defined by tscircuitprops, but Core rejects it as an unregistered element. This adds the native primitive so one continuous copper pad can carry several independent stencil apertures. The renderer uses the existing props and pcb_solder_paste schemas, supports rectangles and circles on either outer layer, and preserves parent rotations, footprint flips, layout movement, and removal. Cached subcircuits retain independent apertures and their orientation, including suppressed full-pad openings. User props remain immutable. Uses the published tscircuitcircuit-json-util0.0.122, which includes https:github.comtscircuitcircuit-json-utilpull238. Cached PCB primitives use the shared transform utility. Circuit JSON import retains an apertures existing rotation as derived state because authored solder-paste props only expose axis-aligned shapes. Cached circular through-hole paste is restored as independent paste geometry, so inflated round holes must not generate it again. This uses Cores existing _isInflatedFromCircuitJson state. Two focused regressions verify that a mixed footprint keeps three automatic paste records and that an explicitly overlapping aperture is preserved, with caching on and off. Each new regression has its own file and labeled snapshot. Pill and oval generation are unchanged. Includes ten solder-paste tests, including a six-window pattern over a single exposed copper pad. Updated to mains isSmt support; keeps tscircuitprops0.0.701 and the released paste transformation fix. Fixes 3577.  Validation All 10 solder-paste tests pass. The two new cache regressions failed before the fix (5 instead of 3 records, and 6 instead of 4). Focused suite: 34 pass, 1 existing pill-paste snapshot mismatch. The 0.12 mismatch reproduces on unchanged main f518678 with the same dependencies and produces an identical diff image; its snapshot is unchanged. Existing isSmt tests, manual-via regression, and standalone primitive caching pass. The manual-via test now matches main exactly. Polygon plated-hole test and both new snapshot comparisons pass after removing ternaries from the newly touched primitive. bunx tsc --noEmit, bun run build, and bun run smoke-test:dist pass. bun run format, git diff --check, and INPUT_PACKAGE_TYPEinternal_lib bunx tscircuitdependency-check pass. Zero ternaries in the 17 changed TSTSX files. The neighboring polygon-paste caching snapshot previously showed a 0.04 mismatch on both this PR and unchanged code with the same dependencies. That baseline is unchanged. The full test suite was not rerun for this update.  Scope This implements Core rendering and Circuit JSON importcache support. It does not change downstream Gerber or KiCad exporters; they must consume independent pcb_solder_paste records to preserve these apertures. |
| [#4725](https://github.com/tscircuit/core/pull/4725) | 🐳 Major | ⭐⭐⭐ | hrithik18k | Creates physical pcb_via elements from via points in a pcbtrace route, ensuring correct dimensions and preventing duplicates during imports. |
| [#4723](https://github.com/tscircuit/core/pull/4723) | 🐙 Minor | ⭐⭐ | seveibar | Updates the bundled tscircuitfanout-solver from version 0.0.78 to 0.0.81, enhancing layer-aware dogbone clearance checks for PCB routing. |
| [#4636](https://github.com/tscircuit/core/pull/4636) | 🐙 Minor | ⭐⭐ | seveibar | Exposed testprobe pads can now use smtpad noSolderPaste  to omit pcb_solder_paste while keeping copper exposed, affecting all six pad shapes and ensuring proper paste creation checks. |
| [#4632](https://github.com/tscircuit/core/pull/4632) | 🐙 Minor | ⭐⭐ | ShiboSoftwareDev | Fixes incorrect source trace attribution for routed endpoints overlapping adjacent pads in PCB designs. |
| [#4627](https://github.com/tscircuit/core/pull/4627) | 🐙 Minor | ⭐⭐ | ShiboSoftwareDev | Prefers exact PCB-port matches for routed endpoints to avoid incorrect source trace attribution when endpoints fall inside adjacent pads. |
| [#4621](https://github.com/tscircuit/core/pull/4621) | 🐙 Minor | ⭐⭐ | ShiboSoftwareDev | Fixes the issue where a requested teardrop is missing when routed copper is attributed to another source trace on the same physical net. |
| [#4619](https://github.com/tscircuit/core/pull/4619) | 🐙 Minor | ⭐⭐ | ShiboSoftwareDev | Fixes the issue where teardrops for equivalent source traces were not rendered correctly, leading to missing teardrops on routed copper. |
| [#4529](https://github.com/tscircuit/core/pull/4529) | 🐙 Minor | ⭐⭐ | 0hmX | Reports disallowed blind or buried vias in manual paths when the board disables them, preserving saved copper and aggregating all disallowed vias. |
| [#4571](https://github.com/tscircuit/core/pull/4571) | 🐙 Minor | ⭐⭐ | rushabhcodes | Fixes the issue where footprint keepouts do not move with their associated PCB components during layout, allowing copper to intrude into designated clearance areas. |
| [#4570](https://github.com/tscircuit/core/pull/4570) | 🐙 Minor | ⭐⭐ | rushabhcodes | Fixes incorrect source trace assignments for routed traces on rotated SMT pads, resolving trace-continuity validation failures. |
| [#4785](https://github.com/tscircuit/core/pull/4785) | 🐙 Minor | ⭐⭐ | trixie010 | Fixes incorrect reference designator prefix matching by allowing multi-letter prefixes that start with the expected letter. |
| [#4784](https://github.com/tscircuit/core/pull/4784) | 🐙 Minor | ⭐⭐ | trixie010 | Fixes a warning emitted for unnamed traces created from the connections prop, ensuring that users are not incorrectly alerted about missing names for traces that cannot be named. |
| [#4783](https://github.com/tscircuit/core/pull/4783) | 🐙 Minor | ⭐⭐ | trixie010 | Fixes spurious convention warnings for multi-letter reference designator prefixes in circuit components. |
| [#4656](https://github.com/tscircuit/core/pull/4656) | 🐙 Minor | ⭐⭐ | imrishabh18 | Fixes alignment of generated rounded board outlines with the resolved board center during rendering, preventing false outside-board errors. |
| [#4623](https://github.com/tscircuit/core/pull/4623) | 🐙 Minor | ⭐⭐ | Devesh36 | Fixes the issue where mounting slots do not rotate with the connector footprint in PCB designs, ensuring visual consistency in the layout. |
| [#4649](https://github.com/tscircuit/core/pull/4649) | 🐙 Minor | ⭐⭐ | MustafaMulla29 | Preserves required schematic branches and routes when removing redundant net-label wires, ensuring connectivity to fixed net labels without altering source-net connectivity. |
| [#4648](https://github.com/tscircuit/core/pull/4648) | 🐙 Minor | ⭐⭐ | MustafaMulla29 | Reproduces the dangling EP trace below U_PDs explicit GND symbol in the PD sheet, preserving schematic symbols and connections without altering production behavior. |
| [#4645](https://github.com/tscircuit/core/pull/4645) | 🐙 Minor | ⭐⭐ | MustafaMulla29 | Fixes the issue of extra built-in terminals being created when a custom symbol declares its own ports, preventing false unconnected-pin warnings. |
| [#4769](https://github.com/tscircuit/core/pull/4769) | 🐙 Minor | ⭐⭐ | hrithik18k | Reproduces the issue of missing physical via records in pcbtrace routes, highlighting discrepancies between explicit via controls and rendered vias. |
| [#4593](https://github.com/tscircuit/core/pull/4593) | 🐙 Minor | ⭐⭐ | hrithik18k | Modifies solder paste generation logic to respect the isSmt property, preventing unwanted paste for through-hole components while retaining paste for mixed footprints. |
| [#4694](https://github.com/tscircuit/core/pull/4694) | 🐙 Minor | ⭐⭐ | KrishnaX12 | Fixes false supplier-footprint mismatch warnings that occur after rotating components by adjusting the calculation of copper bounds without altering the emitted geometry. |
| [#4652](https://github.com/tscircuit/core/pull/4652) | 🐙 Minor | ⭐⭐ | mohan-bee | Demonstrates that an exposed pad with noSolderPaste still receives solder paste, by adding a test and PCB snapshot showing paste on both pads, including the one marked no paste. |
| [#4377](https://github.com/tscircuit/core/pull/4377) | 🐙 Minor | ⭐⭐ | mohan-bee | Reproduces a bug where a rectangular cutout does not rotate with its footprint in a PCB design, ensuring the cutout aligns with the rotated pads. |
| [#4378](https://github.com/tscircuit/core/pull/4378) | 🐙 Minor | ⭐⭐ | mohan-bee | Fixes the issue where a rectangular cutout does not rotate correctly with its footprint, ensuring alignment during board design. |

<details>
<summary>🐌 Tiny Contributions (23)</summary>

| PR # | Impact | Contributor | Description |
|------|--------|-------------|-------------|
| [#4732](https://github.com/tscircuit/core/pull/4732) | 🐌 Tiny | seveibar | Updates the tscircuitcapacity-autorouter dependency from version 0.0.985 to 0.0.986 to utilize the Pipeline9 joint DRC repair speedup, while retaining existing functionality and ensuring all tests pass. |
| [#4609](https://github.com/tscircuit/core/pull/4609) | 🐌 Tiny | seveibar | Updates tscircuitcapacity-autorouter from 0.0.974 to 0.0.982. |
| [#4795](https://github.com/tscircuit/core/pull/4795) | 🐌 Tiny | tscircuitbot | Updates the version of the tscircuitchecks package from 0.0.257 to 0.0.258 in package.json |
| [#4789](https://github.com/tscircuit/core/pull/4789) | 🐌 Tiny | tscircuitbot | Updates the version of the tscircuitchecks package from 0.0.256 to 0.0.257 in package.json |
| [#4665](https://github.com/tscircuit/core/pull/4665) | 🐌 Tiny | tscircuitbot | Updates the tscircuitchecks package from version 0.0.253 to 0.0.255 in package.json |
| [#4787](https://github.com/tscircuit/core/pull/4787) | 🐌 Tiny | rushabhcodes | Updates the direct tscircuitcircuit-json-util development dependency from 0.0.122 to 0.0.123, adopting the released fix from tscircuitcircuit-json-util252 to keep component-owned PCB cutouts aligned during packing and repositioning. |
| [#4618](https://github.com/tscircuit/core/pull/4618) | 🐌 Tiny | rushabhcodes | Reproduces a bug where CC traces of a rotated USB-C connector touch grounded shield slots, providing a comprehensive test to validate the issue. |
| [#4617](https://github.com/tscircuit/core/pull/4617) | 🐌 Tiny | rushabhcodes | Update the circuit-json development dependency and override from 0.0.525 to 0.0.528, ensuring the installed schema and public types recognize the ownership field for components. |
| [#4705](https://github.com/tscircuit/core/pull/4705) | 🐌 Tiny | Abse2001 | Fixes symbol rendering by preserving custom proportions and local viewbox sizing for schematic symbols, ensuring correct scaling behavior for various fit modes. |
| [#4706](https://github.com/tscircuit/core/pull/4706) | 🐌 Tiny | Abse2001 | Fixes symbol rendering to preserve proportions using fit modes and local viewbox settings, ensuring consistent scaling for schematic symbols. |
| [#4788](https://github.com/tscircuit/core/pull/4788) | 🐌 Tiny | anil08607 | Bump tscircuitfootprinter from 0.0.440 to 0.0.442 to incorporate fixes for alias modifier and thermal-pad length-unit conversion. |
| [#4766](https://github.com/tscircuit/core/pull/4766) | 🐌 Tiny | imrishabh18 | Updates tscircuitcapacity-autorouter from 0.0.986 to the latest published version, 0.0.988, bringing in the QFP thermal-pad copper connectivity fix from tscircuit-autorouter3127, which fixes routing for bugreport109. |
| [#4666](https://github.com/tscircuit/core/pull/4666) | 🐌 Tiny | imrishabh18 | Updates the tscircuitchecks dependency to version 0.0.256 and aligns existing fixtures with courtyard-aware boundary checks, including adjustments to board dimensions and validation of routing fixtures. |
| [#4682](https://github.com/tscircuit/core/pull/4682) | 🐌 Tiny | Devesh36 | Updates tscircuitfootprinter from 0.0.431 to 0.0.440, ensuring core uses the latest footprint definitions and fixes. |
| [#4671](https://github.com/tscircuit/core/pull/4671) | 🐌 Tiny | Devesh36 | Fixes overlapping copper pads in the imported ESD5Z5.0T1G TVS footprint when using a 0.8 mm flex gap. |
| [#4622](https://github.com/tscircuit/core/pull/4622) | 🐌 Tiny | Devesh36 | Reproduces a bug where LED silkscreen rectangles do not rotate with their corresponding pads when set at 45 degrees. |
| [#4688](https://github.com/tscircuit/core/pull/4688) | 🐌 Tiny | techmannih | Reproduces the issue of dropped board via-in-pad policy in routing input, ensuring that the boards via-in-pad permission is preserved during routing processes. |
| [#4780](https://github.com/tscircuit/core/pull/4780) | 🐌 Tiny | MustafaMulla29 | Reproduces the issue of ignored schRotation values for connected custom MOSFETs in a snapshot test without changing production code. |
| [#4779](https://github.com/tscircuit/core/pull/4779) | 🐌 Tiny | MustafaMulla29 | Fixes the issue where custom JSX symbols ignore the parent components schRotation, ensuring that their artwork, terminals, and port directions are correctly rotated according to the specified rotation. |
| [#4644](https://github.com/tscircuit/core/pull/4644) | 🐌 Tiny | MustafaMulla29 | Fixes the issue where the custom DPDT symbol incorrectly inherits an extra phantom pin4, leading to missing trace warnings. |
| [#4693](https://github.com/tscircuit/core/pull/4693) | 🐌 Tiny | KrishnaX12 | Fixes false footprint mismatch warnings for rotated components in the supplier footprint matching system. |
| [#4653](https://github.com/tscircuit/core/pull/4653) | 🐌 Tiny | mohan-bee | Honors the noSolderPaste directive on exposed SMT pads in the design files. |
| [#4557](https://github.com/tscircuit/core/pull/4557) | 🐌 Tiny | GokulPandi-M | Fixes rendering issue where a female pinheader with an explicit footprint incorrectly renders male pins instead of female sockets in 3D. |

</details>

### [tscircuit/checks](https://github.com/tscircuit/checks)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#427](https://github.com/tscircuit/checks/pull/427) | 🐳 Major | ⭐⭐⭐ | seveibar | Reduces unnecessary computation in continuity validation by deferring the construction of the physical trace graph until needed, optimizing the process of checking connectivity between traces. |
| [#448](https://github.com/tscircuit/checks/pull/448) | 🐳 Major | ⭐⭐⭐ | rushabhcodes | Fixes incorrect reporting of component containment by ensuring components are checked against their owning board, resolving issues with multi-board setups and ownership references. |
| [#451](https://github.com/tscircuit/checks/pull/451) | 🐳 Major | ⭐⭐⭐ | imrishabh18 | Optimizes trace-continuity validation by resolving readable names for PCB traces only when emitting diagnostics, reducing unnecessary naming work and preserving existing behavior for connectivity and geometry checks. |
| [#433](https://github.com/tscircuit/checks/pull/433) | 🐳 Major | ⭐⭐⭐ | imrishabh18 | Fixes incorrect reporting of component overhangs by using actual footprint geometry for boundary checks instead of bounding rectangles. |
| [#446](https://github.com/tscircuit/checks/pull/446) | 🐙 Minor | ⭐⭐ | MustafaMulla29 | Fixes NaN drill geometry and Illegal Parameters exception by applying nullish defaults for undefined plated-hole offsets in routing DRC. |

<details>
<summary>🐌 Tiny Contributions (2)</summary>

| PR # | Impact | Contributor | Description |
|------|--------|-------------|-------------|
| [#449](https://github.com/tscircuit/checks/pull/449) | 🐌 Tiny | rushabhcodes | Reproduces component containment changing when only the order of two PCB boards changes, demonstrating incorrect behavior in the checker. |
| [#445](https://github.com/tscircuit/checks/pull/445) | 🐌 Tiny | MustafaMulla29 | Reproduces a bug where routing DRC throws an error due to undefined plated-hole offsets without changing production code. |

</details>

### [tscircuit/tscircuit.com](https://github.com/tscircuit/tscircuit.com)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#5454](https://github.com/tscircuit/tscircuit.com/pull/5454) | 🐳 Major | ⭐⭐⭐ | seveibar | Displays each pins permanently connected contacts in the datasheet, makes them searchable, and includes internallyConnectedPins in the generated TSX component. |
| [#5517](https://github.com/tscircuit/tscircuit.com/pull/5517) | 🐳 Major | ⭐⭐⭐ | imrishabh18 | Delays loading of package release history until the version dropdown is opened, reducing initial page load time and preventing Vercel function timeouts due to slow responses from the release endpoint. |
| [#5409](https://github.com/tscircuit/tscircuit.com/pull/5409) | 🐳 Major | ⭐⭐⭐ | imrishabh18 | Download  3D Models  STEP now downloads one named STEP assembly containing the PCB panelboards and all supported CAD and printed parts. Remove the separate Assembly STEP (ZIP) download. |
| [#5490](https://github.com/tscircuit/tscircuit.com/pull/5490) | 🐳 Major | ⭐⭐⭐ | imrishabh18 | Adds an endpoint for uploading archive files to the fake registry, aligning it with the production API and implementing necessary validations and error handling. |

<details>
<summary>🐌 Tiny Contributions (67)</summary>

| PR # | Impact | Contributor | Description |
|------|--------|-------------|-------------|
| [#5437](https://github.com/tscircuit/tscircuit.com/pull/5437) | 🐌 Tiny | seveibar | Removes the blue introduction label, the entire Downloads and versions section, and the closing local-project sentence, while adjusting typography for consistency. |
| [#5516](https://github.com/tscircuit/tscircuit.com/pull/5516) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5515](https://github.com/tscircuit/tscircuit.com/pull/5515) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5514](https://github.com/tscircuit/tscircuit.com/pull/5514) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5513](https://github.com/tscircuit/tscircuit.com/pull/5513) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1639 to 0.0.1640 |
| [#5512](https://github.com/tscircuit/tscircuit.com/pull/5512) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5509](https://github.com/tscircuit/tscircuit.com/pull/5509) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package version from 0.0.1636 to 0.0.1639 in package.json |
| [#5496](https://github.com/tscircuit/tscircuit.com/pull/5496) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1634 to 0.0.1635 in the package.json file. |
| [#5483](https://github.com/tscircuit/tscircuit.com/pull/5483) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3012 to 0.0.3013 |
| [#5508](https://github.com/tscircuit/tscircuit.com/pull/5508) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5504](https://github.com/tscircuit/tscircuit.com/pull/5504) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5501](https://github.com/tscircuit/tscircuit.com/pull/5501) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5500](https://github.com/tscircuit/tscircuit.com/pull/5500) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3019 to 0.0.3021 in package.json |
| [#5498](https://github.com/tscircuit/tscircuit.com/pull/5498) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1635 to 0.0.1636 |
| [#5497](https://github.com/tscircuit/tscircuit.com/pull/5497) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3018 to 0.0.3019 |
| [#5494](https://github.com/tscircuit/tscircuit.com/pull/5494) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3017 to 0.0.3018 |
| [#5492](https://github.com/tscircuit/tscircuit.com/pull/5492) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5488](https://github.com/tscircuit/tscircuit.com/pull/5488) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3013 to 0.0.3016 |
| [#5486](https://github.com/tscircuit/tscircuit.com/pull/5486) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1633 to 0.0.1634 |
| [#5484](https://github.com/tscircuit/tscircuit.com/pull/5484) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1632 to 0.0.1633 |
| [#5507](https://github.com/tscircuit/tscircuit.com/pull/5507) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5491](https://github.com/tscircuit/tscircuit.com/pull/5491) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5482](https://github.com/tscircuit/tscircuit.com/pull/5482) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5481](https://github.com/tscircuit/tscircuit.com/pull/5481) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5480](https://github.com/tscircuit/tscircuit.com/pull/5480) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3010 to 0.0.3011 |
| [#5479](https://github.com/tscircuit/tscircuit.com/pull/5479) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5477](https://github.com/tscircuit/tscircuit.com/pull/5477) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5476](https://github.com/tscircuit/tscircuit.com/pull/5476) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3006 to 0.0.3008 in package.json |
| [#5475](https://github.com/tscircuit/tscircuit.com/pull/5475) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1629 to 0.0.1630 |
| [#5474](https://github.com/tscircuit/tscircuit.com/pull/5474) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3005 to 0.0.3006 |
| [#5473](https://github.com/tscircuit/tscircuit.com/pull/5473) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1628 to 0.0.1629 in the package.json file. |
| [#5472](https://github.com/tscircuit/tscircuit.com/pull/5472) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3003 to 0.0.3005 |
| [#5471](https://github.com/tscircuit/tscircuit.com/pull/5471) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1627 to 0.0.1628 |
| [#5469](https://github.com/tscircuit/tscircuit.com/pull/5469) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1625 to 0.0.1627 in the package.json file. |
| [#5467](https://github.com/tscircuit/tscircuit.com/pull/5467) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3002 to 0.0.3003 |
| [#5463](https://github.com/tscircuit/tscircuit.com/pull/5463) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3001 to 0.0.3002 |
| [#5462](https://github.com/tscircuit/tscircuit.com/pull/5462) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3000 to 0.0.3001 |
| [#5461](https://github.com/tscircuit/tscircuit.com/pull/5461) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5460](https://github.com/tscircuit/tscircuit.com/pull/5460) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5459](https://github.com/tscircuit/tscircuit.com/pull/5459) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5458](https://github.com/tscircuit/tscircuit.com/pull/5458) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.2998 to 0.0.2999 in package.json |
| [#5457](https://github.com/tscircuit/tscircuit.com/pull/5457) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1622 to 0.0.1623 in the package.json file. |
| [#5456](https://github.com/tscircuit/tscircuit.com/pull/5456) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.2997 to 0.0.2998 |
| [#5453](https://github.com/tscircuit/tscircuit.com/pull/5453) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5452](https://github.com/tscircuit/tscircuit.com/pull/5452) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1619 to 0.0.1622 in the package.json file. |
| [#5451](https://github.com/tscircuit/tscircuit.com/pull/5451) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package to version 0.0.2996 |
| [#5449](https://github.com/tscircuit/tscircuit.com/pull/5449) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5446](https://github.com/tscircuit/tscircuit.com/pull/5446) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.2992 to 0.0.2993 |
| [#5445](https://github.com/tscircuit/tscircuit.com/pull/5445) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1616 to 0.0.1618. |
| [#5427](https://github.com/tscircuit/tscircuit.com/pull/5427) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1611 to 0.0.1612 in the package.json file. |
| [#5444](https://github.com/tscircuit/tscircuit.com/pull/5444) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5441](https://github.com/tscircuit/tscircuit.com/pull/5441) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1613 to 0.0.1616 |
| [#5429](https://github.com/tscircuit/tscircuit.com/pull/5429) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5447](https://github.com/tscircuit/tscircuit.com/pull/5447) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1618 to 0.0.1619 |
| [#5426](https://github.com/tscircuit/tscircuit.com/pull/5426) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5436](https://github.com/tscircuit/tscircuit.com/pull/5436) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5434](https://github.com/tscircuit/tscircuit.com/pull/5434) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5425](https://github.com/tscircuit/tscircuit.com/pull/5425) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1609 to 0.0.1611 |
| [#5424](https://github.com/tscircuit/tscircuit.com/pull/5424) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5422](https://github.com/tscircuit/tscircuit.com/pull/5422) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5421](https://github.com/tscircuit/tscircuit.com/pull/5421) | 🐌 Tiny | tscircuitbot | Updates the tscircuiteval package from version 0.0.1607 to 0.0.1609 in the package.json file. |
| [#5420](https://github.com/tscircuit/tscircuit.com/pull/5420) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package to version 0.0.2981 |
| [#5419](https://github.com/tscircuit/tscircuit.com/pull/5419) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5433](https://github.com/tscircuit/tscircuit.com/pull/5433) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package to version 0.0.2987 in package.json |
| [#5489](https://github.com/tscircuit/tscircuit.com/pull/5489) | 🐌 Tiny | imrishabh18 | Update circuit-json-to-step from 0.0.56 to 0.0.57 in package.json to pick up the merged converter performance improvements. |
| [#5468](https://github.com/tscircuit/tscircuit.com/pull/5468) | 🐌 Tiny | Devesh36 | Removes the unused CodeEditorHeader component and replaces its FileName alias with string in remaining helper imports. |
| [#5465](https://github.com/tscircuit/tscircuit.com/pull/5465) | 🐌 Tiny | Devesh36 | Remove tscircuitprompt-benchmarks and the obsolete srccomponentspackage-portCodeEditor.tsx, as requested in review. The website already uses WorkspaceCodeEditor from tscircuitmonaco-code-editor, and nothing imports the old editor. Deleting the old editor removes the last import of prompt-benchmarks, resolving the typecheck error from removing the dependency. Regenerate bun.lock to prune dependencies that are no longer needed. |

</details>

### [tscircuit/cli](https://github.com/tscircuit/cli)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#5397](https://github.com/tscircuit/cli/pull/5397) | 🐳 Major | ⭐⭐⭐ | seveibar | Fetches and validates datasheet pin attributes and permanent internal pin groups, passing them as typed options to easyedas convertRawEasyToTsx. |
| [#5384](https://github.com/tscircuit/cli/pull/5384) | 🐳 Major | ⭐⭐⭐ | imrishabh18 | When TSCIRCUIT_STANDALONE1, serve the bundled RunFrame and preset the CLIs pinned eval version through the existing TSCIRCUIT_LATEST_EVAL_VERSION global. Disable online version selection, telemetry, and hosted page resources. Normal CLI behavior is unchanged. |
| [#5368](https://github.com/tscircuit/cli/pull/5368) | 🐳 Major | ⭐⭐⭐ | imrishabh18 | Starts a loopback asset server for every command when TSCIRCUIT_BAKED_ASSET_SERVER_DIR is set, sets provider base URLs, and honors them in CLI searchimport lookups. |
| [#5324](https://github.com/tscircuit/cli/pull/5324) | 🐳 Major | ⭐⭐⭐ | imrishabh18 | Add --jscdn-base-url url to tsci build, allowing users to set the JS CDN base URL for dynamic imports in the generated static site. |
| [#5371](https://github.com/tscircuit/cli/pull/5371) | 🐙 Minor | ⭐⭐ | rushabhcodes | Fixes the issue where the diode identity and polarity were lost during the import of footprint strings, ensuring accurate representation in the PCB design. |
| [#5456](https://github.com/tscircuit/cli/pull/5456) | 🐙 Minor | ⭐⭐ | imrishabh18 | Fixes the issue where a compressed push can reach the registry even when its response times out, leading to retransmission of every file and reporting a failed archive upload. |
| [#5390](https://github.com/tscircuit/cli/pull/5390) | 🐙 Minor | ⭐⭐ | imrishabh18 | Replaces the standalone import bailout with platformFetch routing to the local baked asset server, allowing EasyEDA requests, model downloads, and registry requests to stay local while handling missing baked responses appropriately. |
| [#5380](https://github.com/tscircuit/cli/pull/5380) | 🐙 Minor | ⭐⭐ | imrishabh18 | Adds functionality to import generated datasheet TSX files in standalone mode, saving them to the imports directory before searching JLCSearch. |
| [#5388](https://github.com/tscircuit/cli/pull/5388) | 🐙 Minor | ⭐⭐ | imrishabh18 | Standalone imports that cannot use the baked TSX now exit with code 1 and display a message indicating unavailability in tscircuit standalone, preventing fallback to online sources. |
| [#5350](https://github.com/tscircuit/cli/pull/5350) | 🐙 Minor | ⭐⭐ | imrishabh18 | Copies prepared JS CDN packages to distjscdn when TSCIRCUIT_STANDALONE is set, allowing for automatic site builds with a default base URL. |
| [#5344](https://github.com/tscircuit/cli/pull/5344) | 🐙 Minor | ⭐⭐ | imrishabh18 | Copies prepared JS CDN packages from TSCIRCUIT_JSCDN_DIR into distjscdn for static site builds, preserving paths and contents without downloading or rebuilding packages. |
| [#5348](https://github.com/tscircuit/cli/pull/5348) | 🐙 Minor | ⭐⭐ | imrishabh18 | Serve prepared packages from TSCIRCUIT_JSCDN_DIR at jscdn and set window.TSCIRCUIT_JSCDN_BASE_URL  jscdn before runframe loads, with support for local testing via --jscdn-dir path. |
| [#5410](https://github.com/tscircuit/cli/pull/5410) | 🐙 Minor | ⭐⭐ | GokulPandi-M | Fixes KiCad export to preserve the root schematic when a child sheet has the same name as the project, preventing loss of hierarchy in exported projects. |
| [#5236](https://github.com/tscircuit/cli/pull/5236) | 🐙 Minor | ⭐⭐ | GokulPandi-M | Fixes KiCad export to include hierarchical child schematics, preventing blank pages when opening child sheets. |
| [#5218](https://github.com/tscircuit/cli/pull/5218) | 🐙 Minor | ⭐⭐ | GokulPandi-M | Fixes the issue where KiCad exports do not include hierarchical child schematic files, resulting in blank pages when attempting to open them. |

<details>
<summary>🐌 Tiny Contributions (94)</summary>

| PR # | Impact | Contributor | Description |
|------|--------|-------------|-------------|
| [#5492](https://github.com/tscircuit/cli/pull/5492) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5491](https://github.com/tscircuit/cli/pull/5491) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3029 to 0.0.3031 in package.json |
| [#5487](https://github.com/tscircuit/cli/pull/5487) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5486](https://github.com/tscircuit/cli/pull/5486) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3026 to 0.0.3027 |
| [#5484](https://github.com/tscircuit/cli/pull/5484) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5482](https://github.com/tscircuit/cli/pull/5482) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5481](https://github.com/tscircuit/cli/pull/5481) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3025 to 0.0.3026 |
| [#5462](https://github.com/tscircuit/cli/pull/5462) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3017 to 0.0.3018 |
| [#5455](https://github.com/tscircuit/cli/pull/5455) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3014 to 0.0.3015 |
| [#5452](https://github.com/tscircuit/cli/pull/5452) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3013 to 0.0.3014 |
| [#5479](https://github.com/tscircuit/cli/pull/5479) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3024 to 0.0.3025 |
| [#5477](https://github.com/tscircuit/cli/pull/5477) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3023 to 0.0.3024 |
| [#5474](https://github.com/tscircuit/cli/pull/5474) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5472](https://github.com/tscircuit/cli/pull/5472) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5471](https://github.com/tscircuit/cli/pull/5471) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3018 to 0.0.3022 |
| [#5466](https://github.com/tscircuit/cli/pull/5466) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5464](https://github.com/tscircuit/cli/pull/5464) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5460](https://github.com/tscircuit/cli/pull/5460) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3016 to 0.0.3017 |
| [#5457](https://github.com/tscircuit/cli/pull/5457) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5453](https://github.com/tscircuit/cli/pull/5453) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5451](https://github.com/tscircuit/cli/pull/5451) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5450](https://github.com/tscircuit/cli/pull/5450) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3012 to 0.0.3013 in package.json |
| [#5446](https://github.com/tscircuit/cli/pull/5446) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5480](https://github.com/tscircuit/cli/pull/5480) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5473](https://github.com/tscircuit/cli/pull/5473) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3022 to 0.0.3023 |
| [#5458](https://github.com/tscircuit/cli/pull/5458) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3015 to 0.0.3016 |
| [#5442](https://github.com/tscircuit/cli/pull/5442) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3011 to 0.0.3012 |
| [#5443](https://github.com/tscircuit/cli/pull/5443) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5440](https://github.com/tscircuit/cli/pull/5440) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5439](https://github.com/tscircuit/cli/pull/5439) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3010 to 0.0.3011 |
| [#5438](https://github.com/tscircuit/cli/pull/5438) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5437](https://github.com/tscircuit/cli/pull/5437) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3009 to 0.0.3010 |
| [#5435](https://github.com/tscircuit/cli/pull/5435) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3008 to 0.0.3009 |
| [#5434](https://github.com/tscircuit/cli/pull/5434) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5432](https://github.com/tscircuit/cli/pull/5432) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5431](https://github.com/tscircuit/cli/pull/5431) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3007 to 0.0.3008 |
| [#5429](https://github.com/tscircuit/cli/pull/5429) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5427](https://github.com/tscircuit/cli/pull/5427) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5426](https://github.com/tscircuit/cli/pull/5426) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3005 to 0.0.3006 |
| [#5423](https://github.com/tscircuit/cli/pull/5423) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5422](https://github.com/tscircuit/cli/pull/5422) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3004 to 0.0.3005 |
| [#5421](https://github.com/tscircuit/cli/pull/5421) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5420](https://github.com/tscircuit/cli/pull/5420) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3003 to 0.0.3004 |
| [#5436](https://github.com/tscircuit/cli/pull/5436) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5428](https://github.com/tscircuit/cli/pull/5428) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3006 to 0.0.3007 |
| [#5399](https://github.com/tscircuit/cli/pull/5399) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.2997 to 0.0.2999 in package.json |
| [#5412](https://github.com/tscircuit/cli/pull/5412) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.3002 to 0.0.3003 |
| [#5404](https://github.com/tscircuit/cli/pull/5404) | 🐌 Tiny | tscircuitbot | Updates the version of the tscircuitrunframe package from 0.0.3000 to 0.0.3001 in package.json |
| [#5419](https://github.com/tscircuit/cli/pull/5419) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5413](https://github.com/tscircuit/cli/pull/5413) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5411](https://github.com/tscircuit/cli/pull/5411) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5407](https://github.com/tscircuit/cli/pull/5407) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5405](https://github.com/tscircuit/cli/pull/5405) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5403](https://github.com/tscircuit/cli/pull/5403) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5402](https://github.com/tscircuit/cli/pull/5402) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.2999 to 0.0.3000 in package.json |
| [#5396](https://github.com/tscircuit/cli/pull/5396) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5418](https://github.com/tscircuit/cli/pull/5418) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5409](https://github.com/tscircuit/cli/pull/5409) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.3001 to 0.0.3002 in package.json |
| [#5400](https://github.com/tscircuit/cli/pull/5400) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5389](https://github.com/tscircuit/cli/pull/5389) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5383](https://github.com/tscircuit/cli/pull/5383) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5379](https://github.com/tscircuit/cli/pull/5379) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5391](https://github.com/tscircuit/cli/pull/5391) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.2995 to 0.0.2997 in package.json |
| [#5387](https://github.com/tscircuit/cli/pull/5387) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5337](https://github.com/tscircuit/cli/pull/5337) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5334](https://github.com/tscircuit/cli/pull/5334) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package to version 0.0.2980 in package.json |
| [#5361](https://github.com/tscircuit/cli/pull/5361) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.2988 to 0.0.2989 |
| [#5359](https://github.com/tscircuit/cli/pull/5359) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.2987 to 0.0.2988 |
| [#5357](https://github.com/tscircuit/cli/pull/5357) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package to version 0.0.2987 in the package.json file |
| [#5356](https://github.com/tscircuit/cli/pull/5356) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5355](https://github.com/tscircuit/cli/pull/5355) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package to version 0.0.2986 |
| [#5354](https://github.com/tscircuit/cli/pull/5354) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5353](https://github.com/tscircuit/cli/pull/5353) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.2984 to 0.0.2985 |
| [#5347](https://github.com/tscircuit/cli/pull/5347) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5345](https://github.com/tscircuit/cli/pull/5345) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package version from 0.0.2983 to 0.0.2984 in package.json |
| [#5342](https://github.com/tscircuit/cli/pull/5342) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.2982 to 0.0.2983 |
| [#5336](https://github.com/tscircuit/cli/pull/5336) | 🐌 Tiny | tscircuitbot | Updates the tscircuitrunframe package from version 0.0.2980 to 0.0.2981 |
| [#5335](https://github.com/tscircuit/cli/pull/5335) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5362](https://github.com/tscircuit/cli/pull/5362) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5358](https://github.com/tscircuit/cli/pull/5358) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5349](https://github.com/tscircuit/cli/pull/5349) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5343](https://github.com/tscircuit/cli/pull/5343) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5340](https://github.com/tscircuit/cli/pull/5340) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5351](https://github.com/tscircuit/cli/pull/5351) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#5370](https://github.com/tscircuit/cli/pull/5370) | 🐌 Tiny | rushabhcodes | Reproduces a bug where the import of the C82046 component loses diode identity and polarity markings during the import process. |
| [#5463](https://github.com/tscircuit/cli/pull/5463) | 🐌 Tiny | anil08607 | Updates the circuit-json-to-kicad dependency from 0.0.236 to 0.0.241, fixing the trace-count iteration issue for boards with 1,000 or more PCB traces during conversion. |
| [#5488](https://github.com/tscircuit/cli/pull/5488) | 🐌 Tiny | imrishabh18 | Updates the RunFrame dependency to version 0.0.3029, which includes the 3D viewer version 0.0.627 using Manifold 3.5.1. |
| [#5433](https://github.com/tscircuit/cli/pull/5433) | 🐌 Tiny | imrishabh18 | Removes the --private flag from the tsci push command, clarifying that it does not affect existing package visibility and replaces it with a regression test for help output. |
| [#5363](https://github.com/tscircuit/cli/pull/5363) | 🐌 Tiny | imrishabh18 | Excludes the running executable from initial file synchronization and filesystem watching during tsci dev, preventing upload timeouts. |
| [#5378](https://github.com/tscircuit/cli/pull/5378) | 🐌 Tiny | imrishabh18 | Update tscircuiteval to 0.0.1619 and tscircuitrunframe to 0.0.2995 to consume the merged parts-engine base URL support in the CLI and browser worker. |
| [#5483](https://github.com/tscircuit/cli/pull/5483) | 🐌 Tiny | MustafaMulla29 | Updates tscircuitcircuit-json-schematic-placement-analysis from 0.0.68 to 0.0.72, keeping the existing https:jscdn.tscircuit.com...version.tgz dependency format. |
| [#5417](https://github.com/tscircuit/cli/pull/5417) | 🐌 Tiny | MustafaMulla29 | Updates the dependency for circuit-json-schematic-placement-analysis from version 0.0.50 to 0.0.68, ensuring compatibility with existing tarball URL formats and updating related metadata in the bun.lock file. |
| [#5406](https://github.com/tscircuit/cli/pull/5406) | 🐌 Tiny | MustafaMulla29 | Updates circuit-json-to-kicad from 0.0.230 to 0.0.235 and kicadts from 0.0.47 to 0.0.58 to resolve CLI startup failure due to missing exports. |
| [#5444](https://github.com/tscircuit/cli/pull/5444) | 🐌 Tiny | GokulPandi-M | Updates the BOM converter dependency to version 0.0.21 to enable source MPN export in the generated BOM. |

</details>

### [tscircuit/tscircuit-autorouter](https://github.com/tscircuit/tscircuit-autorouter)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#3114](https://github.com/tscircuit/tscircuit-autorouter/pull/3114) | 🐳 Major | ⭐⭐⭐ | seveibar | Run bounded regional repair before the broad exactB01 portfolio on boards without preloaded copper, achieving a 3.96 local speedup while maintaining zero-issue reference DRC results. |
| [#2998](https://github.com/tscircuit/tscircuit-autorouter/pull/2998) | 🐳 Major | ⭐⭐⭐ | seveibar | Adds a post-repair cleanup stage that commits only valid improvements and preserves route endpoints while reducing via counts in autorouting. |
| [#3142](https://github.com/tscircuit/tscircuit-autorouter/pull/3142) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Uses a temporary spatial index to find bridge-node neighbors instead of repeatedly scanning every node, preserving the same output order and adjacency checks. |
| [#3138](https://github.com/tscircuit/tscircuit-autorouter/pull/3138) | 🐳 Major | ⭐⭐⭐ | ShiboSoftwareDev | Skip overlap checks when topology nodes have disjoint bounds, avoiding temporary layer and geometry allocations. |
| [#3139](https://github.com/tscircuit/tscircuit-autorouter/pull/3139) | 🐳 Major | ⭐⭐⭐ | imrishabh18 | Removes unused DRC naming and repeated ownership checks in the autorouting process, optimizing performance and maintaining routing integrity. |
| [#3135](https://github.com/tscircuit/tscircuit-autorouter/pull/3135) | 🐳 Major | ⭐⭐⭐ | imrishabh18 | Updates the rectdiff Git dependency to improve performance by sharing sorted projections and reusing rectangle-expansion queries, resulting in reduced processing times without altering routing outcomes. |
| [#3127](https://github.com/tscircuit/tscircuit-autorouter/pull/3127) | 🐳 Major | ⭐⭐⭐ | imrishabh18 | Fixes copper connectivity issues for QFP thermal pads, ensuring proper routing and obstacle handling in autorouting. |
| [#3054](https://github.com/tscircuit/tscircuit-autorouter/pull/3054) | 🐳 Major | ⭐⭐⭐ | techmannih | Fixes autorouting failure when routing around unconnected rotated keepouts by ensuring proper clearance is maintained without increasing approximation rectangle count. |
| [#3098](https://github.com/tscircuit/tscircuit-autorouter/pull/3098) | 🐳 Major | ⭐⭐⭐ | techmannih | Applies the approved rotated keepout fix from 3054 to main, preventing Pipeline9 from routing through uncovered portions of an unconnected rotated keepout. |
| [#3131](https://github.com/tscircuit/tscircuit-autorouter/pull/3131) | 🐙 Minor | ⭐⭐ | seveibar | benchmark --dataset 18 --threads 4 currently fails on the PR base with Unknown argument: --threads: 3126 was squashed into 3125s feature branch, not main. Comment-triggered workflows execute from main, so rebasing 3125 alone cannot fix this. Add the shellcontrollerworkflow flag and sample CPUmemory budgeting to main first. For N  1, sample concurrency is capped at CPUs  (N  1), the requested concurrency, and the existing 6 GiBsample limit (minimum one sample). Pipeline9 stays synchronous in this prerequisite: the runner explicitly logs that and reports effectiveThreadsPerSample: 1, alongside the requested budget. No workerruntime imports or algorithm changes are included. Merge this first, then rebase 3125 and repost benchmark --dataset 18 --threads 4. Both revisions will accept the same reserved budget while comparing the serial base against 3125s parallel implementation. Each revision retains its own harness and algorithms; copying a new harness into an older base would introduce missing runtimebuild imports. Validation: six focused tests  131 assertions, including real serial Pipeline9 outputiteration parity with a four-thread budget, shell forwarding, command validation, CPUmemory limits, and legacy concurrency overrides. |
| [#3126](https://github.com/tscircuit/tscircuit-autorouter/pull/3126) | 🐙 Minor | ⭐⭐ | seveibar | Adds the ability to specify the number of routing threads per sample for Pipeline9 in the benchmarking process, allowing for improved concurrency and resource management during routing tasks. |

<details>
<summary>🐌 Tiny Contributions (21)</summary>

| PR # | Impact | Contributor | Description |
|------|--------|-------------|-------------|
| [#3155](https://github.com/tscircuit/tscircuit-autorouter/pull/3155) | 🐌 Tiny | seveibar | Pins the build and test workflows to Bun 1.4.3 to ensure CI reproducibility and compatibility with threaded solver-utils. |
| [#3063](https://github.com/tscircuit/tscircuit-autorouter/pull/3063) | 🐌 Tiny | seveibar | Updates the tscircuitchecks dependency to version 0.0.255 to recover via-cleanup performance by incorporating continuity geometry optimization. |
| [#3044](https://github.com/tscircuit/tscircuit-autorouter/pull/3044) | 🐌 Tiny | seveibar | Updates the trace simplification solver dependency to a specific upstream commit, improving the handling of routed-copper vias and related cache test instrumentation. |
| [#3052](https://github.com/tscircuit/tscircuit-autorouter/pull/3052) | 🐌 Tiny | seveibar | Updates the dependency on tscircuitchecks to version 0.0.249 and modifies two tests for upstream readable-name diagnostics, ensuring tracegap assertions and structured trace-pair identity are retained. |
| [#3064](https://github.com/tscircuit/tscircuit-autorouter/pull/3064) | 🐌 Tiny | seveibar | Updates the high-density-repair02 dependency to optimize sequential repair by implementing conservative obstacle pruning, cached clearances, boundary checks, and reused spatial-query hits, while preserving candidate ordering and acceptance checks. |
| [#3156](https://github.com/tscircuit/tscircuit-autorouter/pull/3156) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3151](https://github.com/tscircuit/tscircuit-autorouter/pull/3151) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3150](https://github.com/tscircuit/tscircuit-autorouter/pull/3150) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3141](https://github.com/tscircuit/tscircuit-autorouter/pull/3141) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3133](https://github.com/tscircuit/tscircuit-autorouter/pull/3133) | 🐌 Tiny | tscircuitbot | Updates the package version from 0.0.988 to 0.0.989 in package.json |
| [#3129](https://github.com/tscircuit/tscircuit-autorouter/pull/3129) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3128](https://github.com/tscircuit/tscircuit-autorouter/pull/3128) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3119](https://github.com/tscircuit/tscircuit-autorouter/pull/3119) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3100](https://github.com/tscircuit/tscircuit-autorouter/pull/3100) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3097](https://github.com/tscircuit/tscircuit-autorouter/pull/3097) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3069](https://github.com/tscircuit/tscircuit-autorouter/pull/3069) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3062](https://github.com/tscircuit/tscircuit-autorouter/pull/3062) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3057](https://github.com/tscircuit/tscircuit-autorouter/pull/3057) | 🐌 Tiny | tscircuitbot | Automated package update |
| [#3149](https://github.com/tscircuit/tscircuit-autorouter/pull/3149) | 🐌 Tiny | ShiboSoftwareDev | Adds .githubCODEOWNERS with  ShiboSoftwareDev 0hmX seveibar, making all three accounts code owners for every file in the repository. |
| [#3088](https://github.com/tscircuit/tscircuit-autorouter/pull/3088) | 🐌 Tiny | imrishabh18 | Add bugreport109-book-reading-clip-lamp for the full placements-only book reading clip lamp 0.4.3(https:tscircuit.commusebook-reading-clip-lampfiles). Placements, connections and board rules are preserved; existing copper is removed. The number follows the packages bug-report script: highest existing number (108) plus one. The directory contains the matching .fixture.tsx and .srj.json files. There is no provenance file. Start the debugger with bun run start, then select bug-reports  bugreport109-book-reading-clip-lamp. One test attempts the entire circuit at effort 1 with caching disabled and saves a single native pipeline snapshot. Current Pipeline 9 stops at the static reachability precheck for source_net_0_mst26 (U5 EP  GND1), before detailed routing. The test asserts that existing failure. No solver changes. !Full-circuit Pipeline 9 routing attempt(https:raw.githubusercontent.comtscircuittscircuit-autorouterf3bf5bc4e944523437d470100800994b2a3ed88dtestsbugs__snapshots__bugreport109-book-reading-clip-lamp.snap.svg) Validation: renamed test passes against the existing snapshot; type check and full format check pass. sh bun test --timeout 9999999 testsbugsbugreport109-book-reading-clip-lamp.test.ts |
| [#3055](https://github.com/tscircuit/tscircuit-autorouter/pull/3055) | 🐌 Tiny | techmannih | Reproduces a bug where Pipeline9 incorrectly routes traces through a rotated keepout area, adding tests and fixtures to validate the issue without changing production code. |

</details>

### [tscircuit/parts-engine](https://github.com/tscircuit/parts-engine)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#68](https://github.com/tscircuit/parts-engine/pull/68) | 🐳 Major | ⭐⭐⭐ | seveibar | Preserves internal pin connections from datasheets by converting them to source_component.internally_connected_source_port_ids and ensuring complete groups are published during reconciliation. |
| [#67](https://github.com/tscircuit/parts-engine/pull/67) | 🐙 Minor | ⭐⭐ | imrishabh18 | Allows JLC, DigiKey, Mouser, and datasheet requests to use serialized base URL options or their TSCIRCUIT__BASE_URL environment variables, preserving local server path prefixes and isolating cached responses by request URL. |

### [tscircuit/circuit-json-to-gltf](https://github.com/tscircuit/circuit-json-to-gltf)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#256](https://github.com/tscircuit/circuit-json-to-gltf/pull/256) | 🐳 Major | ⭐⭐⭐ | seveibar | Fixes GLB import issues by correctly decoding interleaved vertex data and applying glTF normalization for various component types, ensuring accurate rendering of positions and normals. |

<details>
<summary>🐌 Tiny Contributions (1)</summary>

| PR # | Impact | Contributor | Description |
|------|--------|-------------|-------------|
| [#257](https://github.com/tscircuit/circuit-json-to-gltf/pull/257) | 🐌 Tiny | seveibar | Reproduces issue 255 through generated component GLBs, convertCircuitJsonToGltf, and PoppyGL, capturing broken behavior in GLB accessors for further debugging and fixing. |

</details>

### [tscircuit/solver-utils](https://github.com/tscircuit/solver-utils)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#50](https://github.com/tscircuit/solver-utils/pull/50) | 🐳 Major | ⭐⭐⭐ | seveibar | Solvers can now register their constructors once and execute by name through an inline runtime or a reusable BunNode worker pool. The same registration supplies the serial implementation; callers do not pass a separate fallback function. ts class HighDensityNodeSolver extends BaseSolver  static readonly solverName: string  HighDensityNodeSolver  Existing solver implementation...  SolverRuntime.registerSolver(HighDensityNodeSolver)  Both forms use the same registration and worker selection. const byName  await runtime.executeAsync(HighDensityNodeSolver, params) const byClass  await runtime.executeAsync(HighDensityNodeSolver, params)  Every registered class must define its own non-empty static solverName, including subclasses; runtime validation rejects inheritedmissinginvalid names and conflicting registrations. Class calls infer constructor input and getOutput() types. Constructors are never sent through worker messages, and class invocation does not auto-register. Each request constructs the registered solver, awaits solveAsync(runtime) when implemented (otherwise calls synchronous solve()), rejects reported failure, and returns getOutput(). Existing BaseSolver, stepping, and synchronous solving are unchanged.  Parallel orchestration Keep the parent on the host and let its async method submit child solvers: ts async solveAsync(runtime: SolverRuntimeExecutor): Promisevoid  const pending  this.nodeInputs.map(input  runtime.executeAsync(HighDensityNodeSolver, input), ) const outputs  await Promise.all(pending) for (const output of outputs) this.applyOutput(output) this.solved  true   Host const parent  new HighDensityPhaseSolver(input) await parent.solveAsync(runtime)  A parent submitted as a worker task also works, but descendants execute inline inside that worker. This initial policy prevents nested pools and starvation; host orchestration is necessary to parallelize children. Solvers still own deterministic commits, seeds, iteration budgets, and cache behavior.  Registration and packaging Default tscircuitsolver-utils entry exports the inline runtime and typed executortransport contracts, without Node worker imports. Optional runtimebun and runtimenode entries share the default registry. Prefer the native Bun adapter on Bun. Worker entrypoints import their solver registration modules, then call SolverRuntime.listen(). Registration in the parent does not install worker code. Hosts build those entrypoints into self-contained source strings: ESMBlob workers on Bun, CommonJSeval workers on Node. No adjacent worker path is required after rebundling. An explicit workerUrl option also supports unbundled applications. Inputsoutputs have native message-clone isolation in both modes, preserving intentional SharedArrayBuffer sharing. docssolver-runtime.md(https:github.comtscircuitsolver-utilsblobfeatsolver-runtimedocssolver-runtime.md) includes complete examples and the worker-source generation step.  Execution selection and lifecycle Workers advertise registrations during startup. Missing worker registration uses the local registered constructor; unknown names reject. Startup errors throw by default, with an opt-in diagnosed startupFailure: serial policy. requireWorker: true disables serial execution for CI and parity checks. Slow tasks never trigger serial retries. Solver exceptions reject without retries; unexpected worker exits reject outstandingfuture work. Disposal rejects pending work and terminates owned workers, including partially initialized pools. Inline synchronous work is not interruptible; per-task progresscancellation is outside this initial API. Threaded execution under Bun requires 1.4.2 after observing worker-cleanup hangscrashes on 1.3.2. Tested locally with the available Bun 1.4.2; downloading latest stable 1.4.3 was blocked by network access. The existing structural SolverExecutor contract remains unchanged. Downstream autoroutercoreevalCLI adoption is separate.  Validation 33 tests  184 assertions pass on Bun 1.4.2, including real concurrent leaf tasks, serialasync parity, nested dispatch, missing registrations, startuppartial startup failure, shared memory, failed solver states, worker exits, and disposal. Type checking, package builddeclarations, and repository format check pass. Minified packed tarball checks exercise both class and string invocation and pass on actual Node 26.4.0 and Bun 1.4.2, with externalized and fully rebundled consumers; tests require remote execution, exercise async orchestration and local registration sharing, and verify errors. Packed browser bundle runs inline without Node worker imports. CI now builds and runs the packed consumer checks with Node 22 and latest Bun. The isolated packaging check bundles the real installed graphics-debug peerdependencies rather than performing a network install; it tests solver-utils package boundary. |
| [#47](https://github.com/tscircuit/solver-utils/pull/47) | 🐳 Major | ⭐⭐⭐ | seveibar | Add a typed solver executor and shared-memory contracts to enable solvers to share execution resources without depending on a parent autorouter. |

### [tscircuit/fanout-solver](https://github.com/tscircuit/fanout-solver)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#255](https://github.com/tscircuit/fanout-solver/pull/255) | 🐳 Major | ⭐⭐⭐ | seveibar | Fixes the issue where dogbone matching rejects a legal TOP escape wire due to unrelated BOTTOM pad overlaps, by filtering source-wire obstacles based on the wires layer while retaining through-via clearance checks on every layer. |

### [tscircuit/bus-lanes-solver](https://github.com/tscircuit/bus-lanes-solver)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#61](https://github.com/tscircuit/bus-lanes-solver/pull/61) | 🐳 Major | ⭐⭐⭐ | seveibar | Fixes the handling of omitted optional allowedLayers in native-layer escape fallback to align with pipeline allocation, ensuring proper escape assignment for DDR routing. |
| [#59](https://github.com/tscircuit/bus-lanes-solver/pull/59) | 🐳 Major | ⭐⭐⭐ | seveibar | Stacked on 58, targeting its repro branch. A routable near-horizontal pair can return null when centerline shortening reverses one offset rail and creates a 135 corner. Add an optional validity predicate to the ordinary reducer and check conventional turns and self-clearance on both paired rails. Shortcuts preserve already-valid rails while allowing progressive repair of initially invalid paths. Ordinary callers retain their behavior and final routing validation remains in place. Add the exact repro as coupled-offset-shortening, the twelfth case in both the default CLI benchmark and the shared main-versus-PR manifest. It routes through each selected revisions public pipeline, with independent requirements for 2 signals, no fixed copper or buses, and one matched pair. The eleven AM3352 cases retain their original 47-signal161-fixed-fanout checks. Tests cover revision selection, failedcontradictory solver states, missing cases, strict reports and completion statistics. Validation: Original repro unchanged: 3 tests  86 assertions pass. Current benchmarkregression suite: 35 tests  987 assertions across 7 files pass; type checking and the full 338-file format check pass. The actual new benchmark worker fails on pre-fix revision 7726294 with coupled_routing_failed (02 signals), and passes on the fix (22, full DRCconnectivitycouplingmatching, 0 mm pair skew, 68.263 ms solve). A fresh AM3352 control run passes 4747 signals with full DRCmatching and all 161 fixed fanouts preserved: 42.978 s solve. Total-copper byte-bus skews are approximately 0.635 mm; pair skews are 0.077868, 0.126884 and 0.072830 mm. The prior completed eleven-case AM3352 run and all eleven inspected PNGs remain unchanged. A separate fully validated reduced-case PNGSVG and native worker report are added; its PNG was opened and inspected. See measurements, native reports and completed snapshots(https:github.comtscircuitbus-lanes-solverblobd61928ea9b2ab6640b06932d10fdcf25b3dbcdc0docscoupled-offset-shortening-fixREADME.md). The historical eleven-case run is not presented as a newly rerun twelve-case aggregate. Its mixed GC settings remain documented, and its original JSON capture stays byte-for-byte intact. GitHub benchmark uses the trusted default-branch harness: it will include the new case after this harnessmanifest change reaches main. |
| [#62](https://github.com/tscircuit/bus-lanes-solver/pull/62) | 🐙 Minor | ⭐⭐ | seveibar | Preserve the exact first-byte native input that timed out after 30 minutes  572,200 steps: 11 signals, 1,144 obstacles, no supplied copper, 0.500.30 mm full-through vias, TOPBOTTOM cohorts and the original 33.58527734.220277 mm length window. Compressedraw SHA-256 checks prevent fixture changes. Core passes this valid first-phase SRJ directly to bus-lanes; no earlier-phase traces or capacity-autorouter conversion are involved. The headless baseline also stalls: 60 seconds  11,364 steps, attempt 6, 5,515 visibility vertices. At 11 fixed-layer signals, negotiation is disabled: one DQS corridor stays locked while ordinary-lane orders retry against it. The fast regression compares the original input with a redundant global TOPBOTTOM restriction. Per-bus restrictions already constrain all signals to those layers, but the two select different routing stages. It intentionally fails on main (lanes_coupled_pairs versus route_shared_layers). The bounded CLI runs searches serially without waiting 30 minutes. A diagnostic independent-bus strategy routed 11 candidate carriers within both length windows in about 16 seconds  6,640 steps, then failed the physical exterior-coupling check (about 2.04 mm edge gap versus 0.140 mm allowed). This is rejected intermediate geometry, not a completed route. The fixture notes record the verified search behavior and further native-pad pair-tuning hypotheses. No production changes or partial-route images are included. Run bun test testsam3352-byte-stall-layer-dispatch.test.ts or bun scriptsrepro-am3352-byte-stall.ts --case both --steps 12000 --seconds 60. |
| [#64](https://github.com/tscircuit/bus-lanes-solver/pull/64) | 🐙 Minor | ⭐⭐ | seveibar | The exact native AM3352 11-signal byte capture from 62 now completes in 16.8 seconds  5,222 steps, instead of timing out after 30 minutes. Its 1,144 obstacles, original pads, layer assignments, timing windows, DQS coupling constraints, and 0.50 mm land  0.30 mm full-through drills are unchanged. Stacked on 62 (reproam3352-byte-routing-stall). Integration with main includes the already merged 61. The solver negotiates independent fixed-layer buses, joins coupled approaches into owned native package pads, and tries an equal-length alternative shared-centerline bend when the first corridor blocks ordinary signals. Request-local memoization and pair-route exclusions avoid repeating identical failed searches. Stable bend ties and joint package-entry repair apply to fresh native pads; existing fanout handoffs retain their established ordering and geometry. All copper is generated from the original input, without saved route guides. Validation: Exact capture: all 11 connections, both whole-copper length windows, DQS skew and exterior coupling, copperdrillNPTH clearance, board edges, unchanged nontrace geometry, and all twelve 0.30 mm drills pass independent checks. Snapshot export rejects incomplete or invalid output. CI: 484 tests pass, plus formatting, types, package validation and preview. Local integration with merged main passes all 486 tests. Fresh strict legacy placement proof, updated solver plus merged 61: 1111 solved, each with all 47 connections, independent native DRC, full-copper buspair matching and physical coupling. One-hour-per-case limit; longest control-inner1 1,590.859 s, outer-layers 955.370 s; total solver time 3,643.172 s. All input hashes and all 161 fixed power fanouts per sample are preserved. All eleven fresh routed snapshots were inspected. The earlier 180-second comparison remains available as historical evidence: six accepted cases and five timeouts. No solver, fixture or constraint changes were made for the long-budget proof. Fresh 1111 proof, measurements and route images(https:github.comtscircuitbus-lanes-solverblob8efb7acc6ba9e7e19dcd8ce30dde326afedd9ea0docsrouted-am3352-bytelegacy-full-proofREADME.md)  Validated native byte route(https:github.comtscircuitbus-lanes-solverblob8efb7acc6ba9e7e19dcd8ce30dde326afedd9ea0docsrouted-am3352-byteREADME.md)  Earlier bounded placement comparison(https:github.comtscircuitbus-lanes-solverblob8efb7acc6ba9e7e19dcd8ce30dde326afedd9ea0docsrouted-am3352-bytelegacy-placement-comparison.md) This validates the captured byte phase; the complete SBC has not been rerouted in this PR. |

<details>
<summary>🐌 Tiny Contributions (1)</summary>

| PR # | Impact | Contributor | Description |
|------|--------|-------------|-------------|
| [#60](https://github.com/tscircuit/bus-lanes-solver/pull/60) | 🐌 Tiny | seveibar | Reproduces a bug where the fresh AM3352 DDR input fails due to omitted optional global allowedLayers, causing the native-layer fallback to treat it as no permitted layers. |

</details>

### [tscircuit/motorcontrol](https://github.com/tscircuit/motorcontrol)

| PR # | Impact | Rating | Contributor | Description |
|------|--------|--------|-------------|-------------|
| [#33](https://github.com/tscircuit/motorcontrol/pull/33) | 🐳 Major | ⭐⭐⭐ | seveibar | The earlier NEMA17 current-pattern indicator used one 500 ms harmonic model and often missed fixture-confirmed stalls at other speeds. Replace it with a speed-conditioned, six-feature model trained from 24 user-labelled recordings. Feature windows are 100 ms at 60100 full stepssec, 400 ms at 25, and 800 ms at 12.5. Thresholds reject the free-running envelope instead of using a class midpoint. Expose explicit freesuspecteduncertain states, keep the unreliable low-speed profile uncertain, and flag interpolation, unfamiliar current patterns and temperatures outside the recorded range. Unsupported speedsvoltage requests return unknown. This remains observational and never controls motion or power. Evaluate every 50 ms and emit lightweight motion telemetry every 100 ms. Trainingexport tools, dataset fingerprint and nested whole-trial validation results are checked in. Retrospective outer-fold worst window error was 61.5, 10, 0, and 8.6 at 12.52560100 respectively; these are small-data development estimates, not universal accuracy claims or a new blind test. Validation: native tests replay eight recorded waveform windows and verify featurescore parity, timing, uncertaintydomain gates, gaps and trace retention; host comparison matches all 24 final-model cases. Dashboard tests and all 45 Python tests pass. RP2040 build succeeds. Firmware 1.0.13 was flashed and re-identified on the target NEMA17; bounded commanded-motion checks verify pulse counts and no dropped samples. A fresh fixture-confirmed stall validation is still needed beyond the recorded data. |
| [#25](https://github.com/tscircuit/motorcontrol/pull/25) | 🐳 Major | ⭐⭐⭐ | seveibar | NEMA23 runtime interlock and driver reports previously latched off firmware and independently stopped browser jogging. Add a report-only default and an explicit Stop on detected stall  electrical fault checkbox, off after reboot. Both firmware and browser honor the policy. Hardware interlocks and driver protection still act independently; the UI warns when shaft motion is inhibited and labels positions as commanded. Observe the DRV8452 sensorless torque counter by default, with a configurable software threshold, startupsteady-motion warmup, invalid-data exclusion and 200 ms persistence. Stall indication does not drive nFAULT and causes no software stop unless the optional policy is enabled. Show stall suspected as an uncalibrated indication, with unknown states for shortstoppedstartupfault conditions. Add a torque-count plot sharing the currenttemperature time window. Thermal, sensor, communication and SPI configuration shutdown behavior remains independent. Validation: native defaultopt-in policy, stall debouncerecoveryinvalid-data and protection regressions; all dashboard tests including browser policy, stall controls and chart gaps; 45 Python tests; local NEMA23 UF2 build. Physical shaft-stall accuracy is not yet calibrated. Firmware version: 1.0.6. Connected-board verification: report-only full-scaleinterlock test completed all 160 commanded pulses while recording hardware inhibition, with no firmware latch. The same interlock test with stopping enabled latched off after 49 pulses. At 1 A, forwardreverse commands completed 640 pulses each, and a longer run yielded live torque counts of 1226. FNB58 input-voltagecurrent packets were CRC-validated throughout. These are commandsensor checks, not calibrated physical stall detection. The live stall-notification path was also checked with a deliberately high temporary threshold (4095), without inducing a physical shaft stall: reporting-only emitted stall suspected and completed all 1280 requested pulses; opt-in stopping latched on the indication after 608 pulses. Threshold 3, stop mode off, the users 3 A setting and disabled motor power were restored afterward. This validates notificationpolicy integration, not physical-stall classification accuracy. |
| [#36](https://github.com/tscircuit/motorcontrol/pull/36) | 🐳 Major | ⭐⭐⭐ | seveibar | Changes Add saved stall sensitivity and Run Stall-based Homing on the single-axis, XY, and general motor pages. The sensitivity slider moves the current-score threshold used by the graph, warning and homing detector. NEMA23 retains its torque-threshold control. Homing seeks both ends, verifies release during each backoff, applies a conservative contactdetector allowance, saves the usable travel range, and returns to zero. Each leg has a finite travel ceiling and timeout. Stop, USBheartbeat loss and faults abort. Two connected axes run sequentially, and a failed axis cancels the batch. The firmware reserves queued STEP pulses against the saved bounds, rejects out-of-range finite moves and clips joggingbraking at the boundary. Reboot preserves bounds but requires a fresh home; homing changes the coordinate session so old saved positions cannot be reused.  Validation Native tests: two-contact state machine, clear-stall requirement, no-contacttimeoutcancel paths, settings migrationpersistence, both travel bounds and queued-pulse reservations. Dashboard tests: sensitivity commands, singleXY homing, sequential execution, cancellation, connectionpower failures. Existing nativedashboard suites and 45 Python tests pass. Local ARM builds pass for all three board profiles. Physical end-stop homing has not been run: mechanism suitability is awaiting operator confirmation. These are inferred commanded-step bounds, not encoder-backed travel protection. |
| [#34](https://github.com/tscircuit/motorcontrol/pull/34) | 🐳 Major | ⭐⭐⭐ | seveibar | Changes Add persistent Stall beeping on and Stall time until auto stop settings to the controller and all motor-control pages. Beeping defaults on; auto-stop defaults off (0 seconds). A detected stall produces three rapid 1800 Hz chirps, distinct from the higher-pitched overheat alarm, which retains priority. A configured timeout stops only after a continuous valid stall detection. Free, uncertain, stale, stopped, and unknown states reset the timer. NEMA17 uses its experimental current estimator and NEMA23 uses valid torque stall detection; unsupported DRV8847 boards do not expose the controls. Existing temperature and USB-name settings migrate without being reset.  Validation Native host suite including protocol validation, actual stop behavior, alarm priority, settings migrationpersistence, timeout reset, disabled timeout, and chirp cadence. All dashboard tests and 45 Python tests pass. RP2040 builds for all three board profiles. The NEMA17 detector remains experimental; timing follows its reported stall state and does not supply independent shaft feedback. |
| [#31](https://github.com/tscircuit/motorcontrol/pull/31) | 🐳 Major | ⭐⭐⭐ | seveibar | Move the NEMA17 current-pattern estimator into firmware so USB drops no longer determine its input. Consume the 100 kHz-per-winding ADC stream with an independent cursor, extract 1 kHz waveform features in bounded chunks, and report score, extrapolation status, sample losses, raw ripple RMS and processing time. No estimator result controls motion or power. Normalize logical step modes to physical full-step frequency. Other voltage requests, directions, speeds and temperature conditions produce explicitly unvalidated extrapolations; missing current, faults, insufficient cycles or bandwidth report unknown. The supported feature range is 4320 full stepssec. The dashboard prefers firmware scores and retains the browser estimator for older firmware. Waveform export is now opt-in for this target; default USB traffic contains scores and ordinary telemetry. Optional export uses peak-preserving 10 ms summaries. Firmware 1.0.11. Validation: recorded freestalled waveform tests; logical-resolution, gap, stoppedfault and extrapolation tests; dashboard and Python suites; native firmware builds. Connected-board tests covered all five logical step modes, reverse direction, alternative voltage requests and low speed. Final default-mode runs at 60 and 4 full stepssec analyzed approximately 100,000 samplessec, reported no analysis drops or pulse underruns, and completed commanded pulse counts. Optional waveform export can reduce availability of long uninterrupted windows; 15 V requested produced insufficient winding current to estimate on this setup. |
| [#17](https://github.com/tscircuit/motorcontrol/pull/17) | 🐳 Major | ⭐⭐⭐ | seveibar | The published NEMA23 1.3.2 board has a different driver, GPIO map, current scale and power interlocks from the DRV8825 controller. Add a separate MOTOR_BOARDnema23_drv8452 native C target and matching controls on the bench, single-motor and gantry pages. This PR is based on 16s current-capture work. The profile uses the published STEPDIRSPIRGBbuzzer wiring, nominal 0.2 VA current sensing, a conservative 1 A peak current default and a verified fixed 116 driver configuration. Both regular telemetry and high-rate graph frames use the boards current scale. Driver SPI is checked with ARM low before motion; fault clearing is limited to explicit power arming. Sensorless stall detection and the DNP encoder are not enabled. POWER_ARMARMWAKEbuffer enable boot low. Voltage changes isolate and discharge the rail for 12 seconds, then require fresh PD communicationprotocolcurrent checks. PG is ignored by default so a deasserted signal cannot prevent the first software voltage request. The UI exposes optional strict PG gating, and changing it disarms the rail. Raw PG telemetry remains separate from the override and measured voltage remains unavailable. Power needs explicit arming below 55C; 60C folds current back and 70C or sensoreFusedriverSPI failure latches off the rail. HeartbeatUSB loss disarms. The buffer is disabled after disarm, communication failure or any latched fault. Validation: Both ARM targets built; UBSan motionprotocolsettingscurrent and new production NEMA23 parserpowerSPI tests passed. All 45 Python regressions and dashboardjogpositionssongcurrent-graphcontrol tests passed. CI builds both board profiles and runs ASanUBSan. Flashed two physical NEMA23 controllers. The second (e6658c344b0a562a) is connected to a motor and reported healthy temperaturecurrent sensing, approximately 100k ADC samplessec per winding, a 1 A peak default, and disabled motorpower rail. Driver-disabled PIO tests emitted exact counts at 1k64k200k settings with zero queue underruns while current data streamed. With PG ignored, the second board completed a 15 V request and reported a 3 A PD contract. Protected-rail and SPI readback checks passed. At a 1 A peak limit it completed ten full steps forward and ten back (18 commanded each way) at 20 full stepssec, with 160 counted pulses each direction and about 0.7 A measured in an energized winding. The user confirmed seeing forwardreverse motion. Test ended stopped and disarmed. Actual rail voltage, calibrated current and loaded positional accuracy remain unmeasured. Matching UI deployed to https:motorcontrol.tscircuit.com; explicit armcurrent controls preserve legacy board behavior. |
| [#13](https://github.com/tscircuit/motorcontrol/pull/13) | 🐳 Major | ⭐⭐⭐ | seveibar | The latest RP2040 motor controller uses DRV8825 STEPDIR, transistor-driven RGB outputs, winding-current ADC inputs and GPIO-controlled CH224K voltage selection. The firmware and dashboard, single-motor jog and gantry pages now support that board while retaining the original DRV8847 profile. Startup keeps the motor disabled at 5 V. Voltage changes disable the driver and enforce a settling interval; temperature, heartbeat, watchdog and driver-fa