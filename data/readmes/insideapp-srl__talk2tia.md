<p align="center">
  <img src="site/public/favicon.svg" width="72" height="72" alt="Talk2Tia logo" />
</p>

<h1 align="center">Talk2Tia</h1>

<p align="center">
  <strong>Talk to TIA Portal.</strong> An MCP server that lets your AI assistant work inside Siemens TIA Portal V21 through the official Openness API.
</p>

<p align="center">
  <img alt="Status: public beta" src="https://img.shields.io/badge/status-public%20beta-46cdcf" />
  <img alt="Version 0.12.0" src="https://img.shields.io/badge/version-0.12.0-335eea" />
  <img alt="TIA Portal V21" src="https://img.shields.io/badge/TIA%20Portal-V21-1b2a4e" />
  <img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-42ba96" />
  <a href="https://ko-fi.com/insideappsrl"><img alt="Support on Ko-fi" src="https://img.shields.io/badge/support-Ko--fi-ff5e5b?logo=kofi&logoColor=white" /></a>
</p>

<p align="center">
  <a href="https://talk2tia.insideapp.it">Website</a> ·
  <a href="https://talk2tia.insideapp.it/docs">Documentation</a> ·
  <a href="https://talk2tia.insideapp.it/tools">Tool catalog</a> ·
  <a href="https://github.com/insideapp-srl/talk2tia/releases">Download</a>
</p>

> [!WARNING]
> **Public beta (v0.12).** Talk2Tia is feature-complete but still in beta. Use it on test projects, review every change
> before saving or downloading to a PLC, and please [report issues](https://github.com/insideapp-srl/talk2tia/issues).

## What it does

Talk2Tia exposes **123 MCP tools** to Claude Code, Claude Desktop or any MCP client, so you can work on a TIA Portal
project in plain language:

- **PLC code** — read and write SCL as source, LAD/FBD through SIMATIC SD text documents, anything else via SimaticML
- **Libraries** — global and project libraries, types and versions, edit/release, master copies, update, harmonize, clean-up
- **Tags & types** — tag tables, constants and UDTs in bulk
- **Compile & online** — compile with located errors, online/offline compare, controlled download
- **Visual diffs** — every change comes back as a diff: SCL as unified diff, LAD/FBD networks drawn before and after
  (plus the [`talk2tia`](plugins/talk2tia/skills/talk2tia) skill that shows them in chat)
- **Diagnostics** — CPU operating mode, diagnostic buffer, alarms, live variables and watch tables through the CPU Web API
- **Hardware & HMI** — device tree, catalog, modules, networks, WinCC screens and tags
- **Generic object model** — browse, read, write and invoke any Openness object

Changes are live in the project you have open and stay unsaved until you save them. Destructive actions always
require explicit confirmation; a download never stops the CPU or re-initializes data blocks without permission.

## Requirements

- Windows 10/11 x64
- TIA Portal V21 with the **Openness** option
- Your Windows user in the local **Siemens TIA Openness** group
- An MCP client (Claude Code, Claude Desktop, …)

## Quick start

1. Install the latest `Talk2Tia-<version>-x64.msi` from [Releases](https://github.com/insideapp-srl/talk2tia/releases)
   (the setup asks you to accept the [legal notice](https://talk2tia.insideapp.it/legal/)).
2. Check the environment:
   ```powershell
   talk2tia --doctor
   ```
3. Register the server in Claude Code:
   ```powershell
   claude mcp add talk2tia -- "C:\Program Files\Talk2Tia\talk2tia.exe"
   ```
4. Optional, in Claude Code: install the Talk2Tia plugin (skill + MCP server) from this repository:
   ```text
   /plugin marketplace add insideapp-srl/talk2tia
   /plugin install talk2tia@talk2tia
   ```
5. Open TIA Portal, start Claude and ask: *"Attach to TIA Portal and list the blocks of PLC_1."*
   Confirm the Openness access dialog in TIA Portal.

Choose what the assistant may do with a configuration file: toolsets, single tools, or a read-only profile
(`talk2tia --read-only` for a quick start). The same file declares the PLCs read by the diagnostics tools. See the
[documentation](https://talk2tia.insideapp.it/docs) for details.

## Repository layout

| Path | Content |
|---|---|
| `src/Talk2Tia.Core` | MCP tools and Openness integration (C#, .NET Framework 4.8) |
| `src/Talk2Tia.Server` | `talk2tia.exe` host (stdio MCP server) |
| `tests/Talk2Tia.Tests` | Unit and MCP protocol tests |
| `installer` | WiX MSI installer |
| `site` | Website and documentation (Astro), published at talk2tia.insideapp.it |
| `docs` | Markdown documentation (source for the website) |
| `.github/workflows` | CI, signed releases and GitHub Pages |

## Building

Building and testing need TIA Portal V21 installed: the Openness assemblies are referenced from the local
installation and are never copied or redistributed.

```powershell
dotnet build -c Release
dotnet test -c Release
dotnet publish src/Talk2Tia.Server -c Release -o artifacts/publish
dotnet build installer -c Release
```

Releases are built on a self-hosted runner with TIA Portal and signed with the InsideApp code-signing certificate.

## Support the project

Talk2Tia is free and open source. If it saves you time, you can support its development on
[Ko-fi](https://ko-fi.com/insideappsrl) — it helps us test on more PLCs and TIA Portal versions, add tools and
keep releases signed. A ⭐ on GitHub helps too!

## License and disclaimer

Released under the [MIT License](LICENSE), with an additional notice on industrial use and limitation of liability.
Talk2Tia is provided "as is": every change must be reviewed, tested and approved by qualified personnel before it
reaches a real machine. See the [legal notice](https://talk2tia.insideapp.it/legal).

Siemens, SIMATIC, STEP 7, WinCC and TIA Portal are trademarks of Siemens AG. Talk2Tia is not affiliated with Siemens AG.

---

<p align="center">A project by <a href="https://www.insideapp.it">InsideApp</a></p>
