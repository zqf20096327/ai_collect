<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/brand/design-mark-dark.svg">
    <img src="docs/brand/design-mark-light.svg" alt="OpenConstructionDesign logo" width="72" height="72">
  </picture>
</p>

<h1 align="center">OpenConstructionDesign</h1>

<p align="center">A free, open-source CAD-BIM editor that your AI can drive.</p>

<p align="center">
  <a href="https://github.com/datadrivenconstruction/OpenConstructionDesign/releases/latest"><img src="https://img.shields.io/github/v/release/datadrivenconstruction/OpenConstructionDesign?style=flat-square&label=release&color=3b6cf6" alt="Latest release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/licence-AGPL--3.0-3b6cf6?style=flat-square" alt="Licence: AGPL-3.0"></a>
  <img src="https://img.shields.io/badge/platform-Windows%20%C2%B7%20Linux%20%C2%B7%20Browser-0f172a?style=flat-square" alt="Platforms: Windows, Linux, browser">
  <img src="https://img.shields.io/badge/rust-1.89%2B-b7410e?style=flat-square&logo=rust&logoColor=white" alt="Rust 1.89+">
  <img src="https://img.shields.io/badge/IFC-2X3%20%C2%B7%204%20%C2%B7%204.3-2f855a?style=flat-square" alt="IFC 2X3, 4 and 4.3">
  <a href="#mcp-server"><img src="https://img.shields.io/badge/MCP-compatible-6d4aff?style=flat-square" alt="MCP compatible"></a>
  <a href="#erp-link-change-the-model-the-estimate-follows"><img src="https://img.shields.io/badge/ERP-estimate%20follows%20the%20model-e8590c?style=flat-square" alt="ERP link"></a>
  <img src="https://img.shields.io/badge/works-offline-0f172a?style=flat-square" alt="Works offline">
  <a href="https://openconstructiondesign.com"><img src="https://img.shields.io/badge/website-openconstructiondesign.com-3b6cf6?style=flat-square" alt="Website"></a>
  <a href="#contributing"><img src="https://img.shields.io/badge/PRs-welcome-2f855a?style=flat-square" alt="PRs welcome"></a>
</p>

<p align="center">
  <a href="#download">Download</a> ·
  <a href="#install-in-60-seconds">Install</a> ·
  <a href="#erp-link-change-the-model-the-estimate-follows">ERP link</a> ·
  <a href="#quickstart">Quickstart</a> ·
  <a href="#what-you-can-build">Gallery</a> ·
  <a href="#the-editor">Editor</a> ·
  <a href="#ai-and-mcp">AI and MCP</a> ·
  <a href="#building-services-mep">MEP</a> ·
  <a href="#export-ifc4-and-the-erp-link">Export</a> ·
  <a href="#lua-scripting">Lua</a> ·
  <a href="#browser-version">Browser</a> ·
  <a href="#build-from-source">Build</a>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/images/hero-ui-dark.webp">
    <img src="docs/images/hero-ui-light.webp" alt="The OpenConstructionDesign editor with a six-storey housing block: project browser, plan and 3D side by side, AI chat, generate and check, and the properties of a selected room" width="100%">
  </picture>
</p>

<h2 id="download" align="center">Download</h2>

<p align="center">
  <a href="https://github.com/datadrivenconstruction/OpenConstructionDesign/releases/latest"><picture>
      <source media="(prefers-color-scheme: dark)" srcset="docs/images/download-windows-dark.webp">
      <img src="docs/images/download-windows-light.webp" alt="Download for Windows (zip, 62 MB)" width="300"></picture></a>
  <a href="https://github.com/datadrivenconstruction/OpenConstructionDesign/releases/latest"><picture>
      <source media="(prefers-color-scheme: dark)" srcset="docs/images/download-linux-dark.webp">
      <img src="docs/images/download-linux-light.webp" alt="Download for Linux (tar.gz, 71 MB)" width="300"></picture></a>
</p>

<p align="center">
  <b>v1.3.0</b> · Windows 10/11 x64 · Linux x64 · macOS (beta) · 8 GB RAM · works offline · no account
</p>

| Platform | Get it | Notes |
|---|---|---|
| **Windows 10/11 x64** | [**Download the zip**](https://github.com/datadrivenconstruction/OpenConstructionDesign/releases/latest) | Full editor. Unzip and run `ddc-app.exe`. |
| **Browser** | [**Open the online demo**](https://openconstructiondesign.com/demo/) | Full editor in a browser tab with sample projects, nothing to install. Register with your email, then the editor opens right away. |
| **Linux x64** | [**Download the tar.gz**](https://github.com/datadrivenconstruction/OpenConstructionDesign/releases/latest) (71 MB) | Editor `ddc-app` and `ddc` CLI. Ubuntu 22.04+, Debian 12+ (glibc 2.35), X11 or Wayland. |
| **macOS, Apple silicon (beta)** | [**Download the tar.gz**](https://github.com/datadrivenconstruction/OpenConstructionDesign/releases/latest) (`…-macos-arm64-beta`) | Editor `ddc-app` and `ddc` CLI. Built by CI, not tested on a Mac, not signed. If macOS blocks it, run `xattr -dr com.apple.quarantine <folder>`. |
| **macOS, Intel (beta)** | [**Download the tar.gz**](https://github.com/datadrivenconstruction/OpenConstructionDesign/releases/latest) (`…-macos-x64-beta`) | Same as above. |

<p align="center">
  <a href="https://github.com/datadrivenconstruction/OpenConstructionDesign/releases">All releases</a> ·
  <a href="https://openconstructiondesign.com">Website</a> ·
  <a href="docs/USER_GUIDE.md">User guide</a>
</p>

<p align="center">
  If OpenConstructionDesign is useful to you, a ⭐ on GitHub helps a lot. It is the easiest way to
  help the project grow and reach more people who build.
</p>

<p align="center">
  <img src="docs/images/how-to-star.gif" alt="Click Star at the top right of the repository page" width="480">
</p>

OpenConstructionDesign is a CAD-BIM editor written in Rust, with its own geometry kernel and file
readers. You describe a building in the built-in chat, over MCP or as a JSON brief; the editor
produces real walls, rooms, doors, stairs and building services as a highlighted preview, and
nothing changes in your model until you press **Apply**. Bring a cloud model with your own key,
or run a local model through Ollama. The model and its full change history live in one SQLite
file on your machine, and IFC goes in and out.

> [!NOTE]
> The latest release is **v1.3.0**. The project file format, the APIs and the interface
> can still change between releases. Keep the original of every model you open and keep an IFC
> export for long-term storage. See [Current limits](#current-limits).

## Install in 60 seconds

1. **Download** [the Windows zip (`…-windows-x64.zip`)](https://github.com/datadrivenconstruction/OpenConstructionDesign/releases/latest) (62 MB).
2. **Unzip anywhere and run `ddc-app.exe`.** Nothing is installed in the system and no account is
   needed. The build is not code-signed yet, so Windows SmartScreen may warn once: choose
   **More info → Run anyway**, and check the SHA-256 on the release page if you want to be sure.
   If the window does not open or rendering is broken, start `ddc-app.exe --safe-graphics`.
3. **Make something.** Open **Ask AI** in the ribbon and describe a change, open an IFC file, or
   generate a whole building from the sample brief
   [`brief.de-residential.json`](crates/io/contract/examples/brief.de-residential.json)
   (see [Quickstart](#quickstart)).

<details>
<summary>Build from source</summary>

Needs Git, the MSVC build tools and Rust 1.89+ via [rustup](https://rustup.rs/); details in
[Build from source](#build-from-source) and [docs/BUILDING.md](docs/BUILDING.md).

```powershell
git clone https://github.com/datadrivenconstruction/OpenConstructionDesign.git
cd OpenConstructionDesign
cargo build --release -p ddc-app -p ddc-cli
cargo run --release -p ddc-app
```
</details>

<details>
<summary>CLI quick start: a building from a brief</summary>

`ddc gen` and `ddc publish` are in the `ddc` of every release from v1.4.0. Older releases and a
plain `cargo build` do not have them; build with `cargo build --release -p ddc-cli --features link`.

```sh
ddc gen --brief crates/io/contract/examples/brief.de-residential.json --out housing.ddc
ddc info housing.ddc
ddc open housing.ddc --export ifc4 housing.ifc
```
</details>

## ERP link: change the model, the estimate follows

<p align="center">
  <a href="https://openconstructiondesign.com/#erp">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="docs/images/erp-link-dark.webp">
      <img src="docs/images/erp-link-light.webp" alt="Flow from an ERP project brief through ddc gen, the editor and ddc publish to an estimate in OpenConstructionERP, next to the estimate screen" width="100%">
    </picture>
  </a>
</p>

<table>
<tr>
<td width="62%" valign="top"><a href="https://openconstructiondesign.com/#erp"><img src="docs/images/erp-estimate.webp" alt="OpenConstructionERP estimate built from the housing block model: grand total EUR 3,560,405.95 over seven positions" width="100%"></a></td>
<td width="38%" valign="top">
<h3>&euro;3,560,405.95</h3>
<b>Estimate of the 6-storey housing block, priced straight from the model.</b><br><br>
7 positions · 6,730 elements · 7 levels · quantities from the model, rates from the DE_BERLIN cost database.<br><br>
Move a wall, add a floor or change a type in the editor, publish, and the quantities, the estimate, the 4D schedule and procurement in <a href="https://github.com/datadrivenconstruction/OpenConstructionERP">OpenConstructionERP</a> update with it.
</td>
</tr>
</table>

[OpenConstructionERP](https://github.com/datadrivenconstruction/OpenConstructionERP) is the open
construction ERP from the same team. The editor hands it every element with a stable key, its
quantities and its level.

- **Brief in, model out.** An ERP project brief goes through `ddc gen --brief`; you review the
  preview in the editor and press **Apply**.
- **One revision package.** `ddc publish` writes `elements.parquet`, quantities, the diff to the
  last revision, sheets and IFC4; the ERP matches keys and updates the estimate, 4D schedule and
  procurement.
- **Files or a live session.** Exchange packages as files (offline) or link a session through a
  `.ddclink` file with the token in the OS key store. Code does the maths, not the AI. An ERP
  edition with the editor built in is in preparation.

[OpenConstructionERP on GitHub](https://github.com/datadrivenconstruction/OpenConstructionERP) ·
[openconstructionerp.com](https://openconstructionerp.com) ·
[ERP link on the website](https://openconstructiondesign.com/#erp) ·
[Details below](#export-ifc4-and-the-erp-link)

## Quickstart

1. Start `ddc-app.exe`.
2. Open **Ask AI** in the ribbon and pick a model: Ollama on your own computer (no key), or paste
   a key for a cloud provider. The key stays in the Windows credential store.
3. Describe a change in plain words, for example
   *"Add a 2-storey extension on the east side, 12 × 8 m, joined to the corridor on both levels."*
4. Review the highlighted preview in plan and 3D, untick items or change values, then press
   **Apply**. The whole plan is one undo step. Then keep editing by hand.

### A whole building from a brief

For a new building, write a short JSON brief (use, storeys, structure, flat mix) and let the
generator lay it out. The schema is [`crates/io/contract/schemas/brief.schema.json`](crates/io/contract/schemas/brief.schema.json);
a full example is [`brief.de-residential.json`](crates/io/contract/examples/brief.de-residential.json).

```sh
ddc gen --brief brief.json --out housing.ddc
ddc info housing.ddc
ddc open housing.ddc --export ifc4 housing.ifc
```

<details>
<summary>Brief excerpt: five-storey housing with a lift (from <code>brief.de-residential.json</code>)</summary>

```json
{
  "schema": "ddc-brief/1",
  "name": "Wohnhaus Beispielstraße",
  "norm_pack": "de",
  "use": { "category": "residential_multi", "detail": "Mehrfamilienhaus, ein Treppenhaus" },
  "massing": {
    "floors_above": 5, "floors_below": 1, "floor_height_m": 3.0,
    "footprint": { "width_m": 34.0, "depth_m": 12.0 }, "lift": true
  },
  "programme": {
    "units": [
      { "name": "2-Zimmer", "count": 10, "area_m2": 52,
        "rooms": [{ "kind": "living" }, { "kind": "bedroom" }, { "kind": "kitchen" }, { "kind": "bath" }, { "kind": "hall" }] },
      { "name": "3-Zimmer", "count": 10, "area_m2": 74,
        "rooms": [{ "kind": "living" }, { "kind": "bedroom", "count": 2 }, { "kind": "kitchen" }, { "kind": "bath" },
                  { "kind": "hall" }, { "kind": "storage" }] }
    ],
    "spaces": [{ "kind": "technical", "name": "Technik", "floors": [-1], "area_m2": 40 }]
  },
  "structure": { "system": "masonry", "foundation": "raft" },
  "envelope": { "roof": "flat" }
}
```
</details>

> [!NOTE]
> `ddc gen` and `ddc publish` belong to the ERP link. Releases from v1.4.0 include them; to add
> them to a source build, use `cargo build --release -p ddc-cli --features link`.

## What you can build

Each model is regenerated from its source in one command: a brief for the housing block, a Lua
script for the stadium and the tower. Times are wall-clock generation on one laptop with release
0.10; figures come from each run's own summary.

<table>
<tr>
<td width="33%"><img src="docs/images/pj-housing.webp" alt="Six-storey U-shaped housing block around a garden court" width="100%"></td>
<td width="33%"><img src="docs/images/pj-stadium.webp" alt="Football stadium bowl under a ring roof, with parking and trees" width="100%"></td>
<td width="33%"><img src="docs/images/pj-tower.webp" alt="Steel diagrid tower on a podium with a pool terrace and planting" width="100%"></td>
</tr>
<tr>
<td valign="top"><b>6-storey housing block</b> (brief → <code>ddc gen</code>)<br>U-shaped block around a garden court with HVAC, water, drainage and electrical.<br>10,274 elements · 504 walls · 354 rooms · 4,521 MEP runs · 412 circuits · 0 audit errors · 7 min</td>
<td valign="top"><b>Football stadium</b> (Lua)<br>A bowl under a ring roof, with site, parking and planting. Structure and envelope only.<br>6,441 elements · 12 min</td>
<td valign="top"><b>Diagrid tower</b> (Lua)<br>A steel diagrid tower on a podium, with a mast and a landscaped site. Structure and envelope only.<br>6,203 elements · 13 min</td>
</tr>
</table>

Known gap in the housing block: 30 kitchen taps are not yet connected to the water network.

### Lua recipes that ship with the editor

The recipes live in [`crates/script/data/recipes`](crates/script/data/recipes) (5 files). Each
one passes `audit{strict = true}` with its default parameters:

| Recipe | What it builds |
|---|---|
| `arches_and_vaults.lua` | Ribbed vault with glass panels and a row of free arches |
| `long_span_grid.lua` | Double-layer space frame on perimeter columns |
| `radial_array.lua` | Nodes on a circle joined to a hub, one component at every node |
| `surface_lattice.lua` | Diagrid over a dome with an oculus; swap in a vault, hypar, loft or wave |
| `tiered_frame.lua` | Storeys of columns and slabs with taper and twist |

## The editor

Plan and 3D in one window. Whatever the AI proposes, you can open, edit and finish by hand.

<p align="center"><picture><source media="(prefers-color-scheme: dark)" srcset="docs/images/editor-3d-props-dark.webp"><img src="docs/images/editor-3d-props-light.webp" alt="3D view of the six-storey housing block with flat 5.1 selected and its properties: area 16.27 m², perimeter 16,850 mm, height 3,000 mm, phases and project parameters" width="100%"></picture><br><sub>The six-storey housing block in the editor. Select anything in 3D or on the plan; the Properties panel shows the real values and edits them in place.</sub></p>

<table>
<tr>
<td width="50%"><picture><source media="(prefers-color-scheme: dark)" srcset="docs/images/editor-plan-rooms-dark.webp"><img src="docs/images/editor-plan-rooms-light.webp" alt="Level 2 plan of the housing block: numbered flats with names and areas, corridor, stair and lift, with water and ventilation runs" width="100%"></picture><br><sub><b>Plans.</b> Rooms are named, numbered and measured, and follow every edit.</sub></td>
<td width="50%"><img src="docs/images/editor-mep-services.webp" alt="Housing block in four layers: architecture, supply air, supply and extract air, fixtures and appliances" width="100%"><br><sub><b>MEP services.</b> Ducts, pipes and fixtures run through the same model, layer by layer.</sub></td>
</tr>
<tr>
<td><picture><source media="(prefers-color-scheme: dark)" srcset="docs/images/editor-ai-generate-dark.webp"><img src="docs/images/editor-ai-generate-light.webp" alt="The Generate panel: a short brief, building type, storeys and floor height, with the steps Generate, Check and apply, Drawings, Files" width="100%"></picture><br><sub><b>AI generate and review.</b> The AI builds a preview from a brief. Nothing changes until you press Apply.</sub></td>
<td><img src="docs/images/editor-drawings.webp" alt="Generated floor plan sheet of the housing block with rooms, dimensions and services" width="100%"><br><sub><b>Drawings.</b> Plans, sections and sheets come out of the model and stay in sync.</sub></td>
</tr>
</table>

**Scripted shapes**

<table>
<tr>
<td width="25%"><a href="https://openconstructiondesign.com/#ai"><img src="docs/images/lua-twisted-diagrid-tower.webp" alt="Twisted diagrid tower" width="100%"></a></td>
<td width="25%"><a href="https://openconstructiondesign.com/#ai"><img src="docs/images/lua-stadium-roof.webp" alt="Stadium roof of cantilever trusses" width="100%"></a></td>
<td width="25%"><a href="https://openconstructiondesign.com/#ai"><img src="docs/images/lua-timber-gridshell.webp" alt="Timber gridshell dome" width="100%"></a></td>
<td width="25%"><a href="https://openconstructiondesign.com/#ai"><img src="docs/images/lua-cable-stayed-footbridge.webp" alt="Cable-stayed footbridge" width="100%"></a></td>
</tr>
</table>

<sub>Shapes made with Lua scripts, rendered with default parameters. <a href="https://openconstructiondesign.com/#ai">More on the site</a>.</sub>

<details>
<summary>Full feature list</summary>

**Modelling**
- Levels, grids, reference planes, walls (layered types, automatic joins), floors, ceilings,
  roofs, stairs, railings, ramps, curtain walls, openings, doors, windows, rooms and zones.
- Own geometry kernel: exact predicates, B-rep solids, CSG, sweeps, NURBS, sketch constraints.
- Parametric families: components with types and parameters defined inside the model.
- Every edit is a journaled step with undo, redo, per-change history with its author, and
  version comparison.

**Documentation and drawings**
- Plans, sections, elevations, 3D views, schedules, dimensions, tags, text, legends.
- Sheets with title blocks and views placed at scale; vector PDF and SVG export.

**Structure**
- Beams, columns, braces, structural walls and floors, footings, foundation slabs,
  reinforcement that follows its host; steel connections with plates and bolts.

**Formats**
- Import IFC2X3, IFC4, IFC4X1 to IFC4X3 and `.ifczip`; export IFC2X3, IFC4 and IFC4.3.
- Read `.dwg` and `.dxf` with independent decoders. The original file is never modified.
- Export glTF, STEP, STL, OBJ, 3MF; issues as BCF 2.1/3.0.
- `.rvt` through an optional, separately distributed bridge module that speaks the published
  [bridge protocol](docs/plugins/BRIDGE_PROTOCOL.md); it is not part of this repository.
- Clash detection, rule checks and model integrity checks.

**Spreadsheets**
- Round-trip element parameters through XLSX; an import is one undo step with a per-cell report.
- Query elements and open them as an editable table.

**Automation**
- JSON edit scripts with preview, and recording of actions into a script.
- Sandboxed Lua geometry scripts; the headless `ddc` CLI (`open`, `info`, `batch`, `run`;
  `gen` and `publish` with the ERP link).
</details>

## AI and MCP

The editor runs no AI service of its own and is not tied to a vendor. It speaks OpenAI-style chat
completions and Anthropic-style messages, plus MCP for external clients. You pay your provider
directly, or nothing with a local model.

<table>
<tr>
<td width="50%"><img src="docs/images/ui2-ai.webp" alt="AI assistant settings: connection set to an Ollama model on this computer, design depth D1 to D5 per discipline" width="100%"></td>
<td width="50%" valign="top">

| Connection | What you set |
|---|---|
| **Local** | Ollama on `localhost:11434` is found automatically. No key; data stays on the machine. |
| **Cloud** | An address and a key (Anthropic, OpenAI, Google Gemini, Mistral, DeepSeek and others). The key is kept in the OS secure store, never in the project file. |
| **Model gateway** | One key for many models: the address of a chat-completions compatible gateway is filled in; the model list brings prices and context sizes, and the money left is shown next to the session cost. A spent key limit and an empty account are told apart. |
| **Custom** | Protocol, address and headers for your own server. An allow-list says which hosts the editor may call. |
| **MCP** | Off by default, local only, same Apply rule. |

Design depth (D1 to D5) is set per discipline: architecture, structure, MEP, documents.
</td>
</tr>
</table>

> [!IMPORTANT]
> **Preview, then Apply.** The AI plans on a scratch copy, runs the model checks on its result and
> shows it highlighted under a *Preview, model unchanged* banner, with the quantities it
> adds. Nothing reaches your model until you press **Apply**; an applied plan is one undo step.

### MCP server

Turn on **MCP server** in the editor. It listens on `127.0.0.1:47621` only and copies a client
config with a fresh token; revoke the token with one click.

| Tool | Purpose |
|---|---|
| `get_context` | Project, levels and the current selection |
| `query_elements` | Find walls, rooms, doors by any parameter |
| `create_elements` | Add elements into the preview |
| `run_checks` | Run the audit on the preview |
| `request_apply` | Ask the user to press Apply |

<details>
<summary>Client configuration</summary>

HTTP clients (for example `.cursor/mcp.json`):

```json
{ "mcpServers": { "ddc-editor": {
    "type": "http", "url": "http://127.0.0.1:47621/mcp",
    "headers": { "Authorization": "Bearer <token>" } } } }
```

Command-line clients:

```sh
claude mcp add --transport http ddc-editor http://127.0.0.1:47621/mcp \
  --header "Authorization: Bearer <token>"
```

Clients that need a stdio bridge (for example `claude_desktop_config.json`):

```json
{ "mcpServers": { "ddc-editor": {
    "command": "npx",
    "args": ["mcp-remote", "http://127.0.0.1:47621/mcp", "--header", "Authorization:${DDC_AUTH}"],
    "env": { "DDC_AUTH": "Bearer <token>" } } } }
```
</details>

More: [docs/user/ai-assistant.md](docs/user/ai-assistant.md).

## Building services (MEP)

The generator lays out services together with the building: ducts sized for the air each room
needs, pipes with their fittings, cooling and power for a data centre. They export as real IFC
classes (`IfcDuctSegment`, `IfcPipeSegment`, `IfcCableCarrierSegment`), not as boxes. Each grid
steps from the architecture through a ghosted shell to the service systems.

<table>
<tr>
<td width="50%"><img src="docs/images/mep-school-layers.webp" alt="School in four steps: architecture, ventilation, water, drainage and heating, all services" width="100%"><br><b>3-storey school</b>: ventilation, then water, drainage and heating. 276 service runs.</td>
<td width="50%"><img src="docs/images/mep-clinic-layers.webp" alt="Clinic in four steps: architecture, cold and hot water, drainage and fixtures, all services" width="100%"><br><b>4-storey clinic</b>: cold and hot water, drainage and fixtures. 983 service runs. No ventilation yet.</td>
</tr>
<tr>
<td><img src="docs/images/mep-housing-layers.webp" alt="Housing block in four steps: architecture, supply air, supply and extract air, fixtures and appliances" width="100%"><br><b>6-storey housing</b>: supply and extract air, fixtures and appliances. 702 service runs.</td>
<td><img src="docs/images/mep-data-centre-layers.webp" alt="Data centre in four steps: architecture, chilled water and racks, power, all services" width="100%"><br><b>Data centre</b>: chilled water (×2) with the rack rows, then power (×2). 330 service runs.</td>
</tr>
</table>

<details>
<summary>Process plant</summary>

<img src="docs/images/mep-process-plant.webp" alt="Process plant: storage tanks in a bund, a jacketed reactor, a distillation column, pumps and heat exchangers on a steel pipe rack" width="100%">

Process plant, 90 m³/h, from one brief: 29 units, 285 pipe runs, 978 m of pipe, 245 supports.
46 of 69 nozzles are connected so far; the plant check lists every open line.
</details>

> [!NOTE]
> Room-level electrical (boards, circuits, luminaires) is still being completed in the generator,
> and the clinic has no ventilation yet. Both appear in the generator's own report.

## Export: IFC4 and the ERP link

IFC read and write covers IFC2X3 to IFC4.3. The model is data first: every element carries a
stable key, its parameters and quantities, so an estimating or ERP system can price it. The
editor never invents a cost.

<p align="center">
  <img src="docs/images/erp-link.svg" alt="Diagram: a project brief from the ERP generates a model; the editor publishes a revision package with element rows and quantities; the ERP turns it into an estimate, a schedule and procurement" width="100%">
</p>

- `ddc gen --brief` turns a project brief from the ERP into a model; `ddc publish` sends a model
  back as a revision package: element rows (`elements.parquet`), quantities, a diff against the
  parent revision, sheets, IFC and 3D geometry.
- As files, this works offline and through any file share. A `.ddclink` file opens a linked
  session straight from the ERP; the project token lives only in the OS key store.

The housing block above, exported to IFC4 and opened in [OpenConstructionERP](https://github.com/datadrivenconstruction/OpenConstructionERP) 18.8.2:

<table>
<tr>
<td width="50%"><img src="docs/images/erp-model.webp" alt="OpenConstructionERP BIM viewer with the housing block from IFC4: 6,730 elements on 7 levels" width="100%"><br>Imported model: 6,730 elements on 7 levels, counted by category and storey. The ERP draws imported geometry as simplified boxes.</td>
<td width="50%"><img src="docs/images/erp-element.webp" alt="Wall 105 selected, with length 12 m, height 3 m, net volume 9.837 m³" width="100%"><br>Quantities per element: Wall 105 on Level 1, 12 m long, 3 m high, 9.837 m³ net volume.</td>
</tr>
<tr>
<td><img src="docs/images/erp-rules.webp" alt="Dry run of seven quantity rules: 2,060 matched elements and 7 bill positions" width="100%"><br>A dry run of 7 quantity rules matches 2,060 elements and shows the 7 bill positions it would create.</td>
<td><img src="docs/images/erp-estimate.webp" alt="Estimate with seven positions from the model, such as 2,698.30 m³ of concrete walls" width="100%"><br>The estimate: seven positions with quantities from the model. Total EUR 3,560,405.95; unit rates are typed in as an example.</td>
</tr>
</table>

The ERP edition with the editor built in is in preparation. Without the ERP the editor works on
its own.

## Lua scripting

Some shapes are a rule. A recipe declares its parameters with `param`, calls a builder and
ends with an audit; change a number and the whole shape rebuilds. Scripts run sandboxed: no
files, network, clock or randomness.

```lua
-- Twisted diagrid tower: steel diagonals in staggered rows, ring beams on every floor, slabs round a concrete core.
local floors = param("floors", 24, {min = 4, max = 80})
local radius = param("radius", "16 m", {min = "8 m", max = "40 m"})
local twist = param("twist", "90 deg", {min = "-180 deg", max = "180 deg"})
local taper = param("taper", 0.8, {min = 0.5, max = 1.2})
tower{floors = floors, floor_h = "4 m", radius = radius, sides = 12, twist = twist,
      taper = taper, system = "diagrid", module = 2, diagonal = "CHS 508x25",
      beam = "I 500x200", name = "tower"}
audit{strict = true}
```

Run it headless and override a parameter:

```sh
ddc run project.ddc crates/script/data/recipes/tiered_frame.lua --out tower.ddc --param floors=32
```

## Browser version

The editor also runs in a browser tab. It is the same code as the desktop application, compiled to
WebAssembly (`crates/web-editor`, with the page entry and build tools in `tools/web`). The model,
checks, generators, IFC and the ERP revision package work as on the desktop; Lua scripts, OS file
dialogs, the update check, local AI keys, the MCP server and the external format converters stay
desktop only. AI requests go through the host page, so keys never reach the browser. On touch
devices and small screens it opens view only.

**In OpenConstructionERP** nothing has to be installed by hand. The ERP reads the release feed
[`erp-link/release/latest-web.json`](erp-link/release/latest-web.json), downloads the zip from the
GitHub release, checks its size and SHA-256, verifies its minisign signature against the public key
shipped with the ERP (key id `BF094D8BDEC11250`) and unpacks it under its data folder
(`design/web-editor/`). A newer feed installs the newer bundle the same way and removes the old one.

**On your own machine** you need Rust with the `wasm32-unknown-unknown` target, clang and llvm-ar,
the `wasm-bindgen` CLI in the version from `Cargo.lock`, and Python 3:

```bash
rustup target add wasm32-unknown-unknown
cargo install wasm-bindgen-cli --version 0.2.130 --locked
bash tools/web/build_bundle.sh            # bundle in dist/web-editor/
mkdir -p tools/web/pkg && cp -r dist/web-editor/* tools/web/pkg/
python3 -m http.server 8080 -d tools/web  # open http://localhost:8080/
```

Full guide, including how releases are built, signed and updated: [docs/BROWSER.md](docs/BROWSER.md).

## Repository layout

| Crate | Role |
|---|---|
| `app` | The desktop editor (`ddc-app`) |
| `cli` | Headless CLI (`ddc`) |
| `ui` | Application shell on egui: tokens, icons, commands, ribbon, localisation |
| `render` | wgpu viewport renderer: scene chunks, instancing, camera, picking |
| `model` | Building model stored in SQLite with an edit journal |
| `ops` | Serialisable edit language shared by tools, imports, scripts and external clients |
| `geom` | Geometry kernel |
| `solver` | Geometric constraint solver for plan points |
| `gen` | Seed-deterministic building generators and family templates |
| `script` | Sandboxed Lua geometry scripts that emit one ops envelope |
| `ai` | AI assistant core: providers, wire protocols, conversation loop, tool catalogue |
| `io` | Import and export: IFC, DXF, XLSX, PDF, glTF; closed formats via an out-of-process bridge |
| `bridge-proto` | Neutral interchange frames for out-of-process import bridges |
| `link` | ERP link client: link file, token, context, lock, revisions |
| `calc` | Structural analysis job: analytical model and loads to solver input |
| `fem` | Linear static 3D frame finite elements |

Architecture: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Build from source

Windows 10/11 x64 is the primary platform. You need Git, the MSVC build tools ("Desktop
development with C++"; a C compiler is needed for the bundled SQLite and Lua) and Rust via
[rustup](https://rustup.rs/) (stable, MSVC target, 1.89 or newer; CI uses 1.95.0).

```powershell
rustup component add rustfmt clippy
git clone https://github.com/datadrivenconstruction/OpenConstructionDesign.git
cd OpenConstructionDesign
cargo build --release -p ddc-app -p ddc-cli
cargo run --release -p ddc-app             # the editor
cargo run --release -p ddc-cli -- --help   # the CLI (binary name: ddc)
```

### Tests

```sh
cargo test -q -p ddc-model         # one crate
cargo test -q --workspace          # everything (slow)
cargo fmt --all --check
cargo clippy --workspace -- -D warnings
```

Details and other platforms: [docs/BUILDING.md](docs/BUILDING.md).

| Platform | Status |
|---|---|
| Windows 10/11, x64 | Supported; primary development platform |
| Linux | Editor and CLI in every release, built on Ubuntu 22.04; library crates tested in CI |
| macOS | Beta builds (Apple silicon and Intel) in every release, built by CI; not tested on a Mac |
| Browser (wasm32) | [Online demo](https://openconstructiondesign.com/demo/) after a short registration; the browser build is not part of this repository yet |

## Current limits

- The `.dwg` and `.dxf` decoders are independent implementations covering common building
  elements and geometry, not every feature. Compare imports with the source.
- The AI assistant can make mistakes; always read the preview and diff. Small local models
  handle only simple requests.
- The structural solver is a library and is not yet exposed in the editor.
- The project file format is not frozen; keep an IFC export for long-term storage.
- Very large models can be slow.

## Documentation

| Document | Contents |
|---|---|
| [Getting started](docs/user/getting-started.md) | First model, files, saving |
| [AI assistant](docs/user/ai-assistant.md) | Providers, preview, Apply |
| [Video and frames](docs/user/video-and-frames.md) | Stills, interface shots and build-up animation |
| [Formats](docs/user/formats.md) | Supported formats and IFC round trip |
| [Families](docs/user/families.md) | Parametric families |
| [User guide](docs/USER_GUIDE.md) | Core workflows and shortcuts |
| [Architecture](docs/ARCHITECTURE.md) | Crates, data flow, journal, AI contract |
| [Building](docs/BUILDING.md) | Building and testing |
| [Browser version](docs/BROWSER.md) | Browser build, ERP install and updates |
| [Changelog](CHANGELOG.md) | What shipped |

## Contributing

Contributions are welcome; read [CONTRIBUTING.md](CONTRIBUTING.md). Every contributor signs the
[Contributor License Agreement](CLA.md) before the first merge and signs off each commit
(`git commit -s`). Follow the [Code of Conduct](CODE_OF_CONDUCT.md). Report vulnerabilities
privately as described in [SECURITY.md](SECURITY.md), not in public issues.

## Part of the DataDrivenConstruction family

<p align="center">
  <a href="https://openconstructionerp.com"><picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/brand/erp-mark-dark.svg">
    <img src="docs/brand/erp-mark-light.svg" alt="" width="28" height="28" align="absmiddle"></picture></a>&nbsp;
  <a href="https://github.com/datadrivenconstruction/OpenConstructionERP"><b>OpenConstructionERP</b></a>
  &emsp;&emsp;&emsp;
  <a href="https://openconstructionacademy.com"><picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/brand/academy-mark-dark.svg">
    <img src="docs/brand/academy-mark-light.svg" alt="" width="28" height="28" align="absmiddle"></picture></a>&nbsp;
  <a href="https://openconstructionacademy.com"><b>OpenConstructionAcademy</b></a>
  <br>
  <sub>Estimates, schedules and procurement priced from your model&ensp;·&ensp;Courses on data-driven construction</sub>
</p>

Found this useful? A ⭐ at the top of the page is the best way to say thanks.

## Licence

[GNU Affero General Public License, version 3 only](LICENSE) (AGPL-3.0-only). If you run a
modified version as a network service, you must offer its source to that service's users.
Third-party components keep their own licences; see [THIRD_PARTY_LICENSES.txt](THIRD_PARTY_LICENSES.txt)
and [NOTICE](NOTICE). A commercial licence is available where the AGPL does not fit; see
[COMMERCIAL.md](COMMERCIAL.md).
