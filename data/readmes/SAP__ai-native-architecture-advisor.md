[![AI Native Architecture Advisor](docs/assets/banner.svg)](https://sap.github.io/ai-native-architecture-advisor/)

[![REUSE status](https://api.reuse.software/badge/github.com/SAP/ai-native-architecture-advisor)](https://api.reuse.software/info/github.com/SAP/ai-native-architecture-advisor)

# AI Native Architecture Advisor

Reimagine an SAP customer or partner use case for the AI-native era. Describe the business problem, explore the options with the Advisor, and build an **AI Native Solution Brief** with a proposed architecture and a visual HTML report.

**[Website and demo →](https://sap.github.io/ai-native-architecture-advisor/)** · [Watch the 30-second walkthrough](videos/supplier-confirmation/renders/supplier-confirmation_2026-10-06_17-41-41.mp4)

The walkthrough shows one real run: a supplier-confirmation use case described in plain language, the questions that actually change the architecture, the four North Star layers, the capability progression, and the three files every run writes.

This is initial **high-level solution design** for solution/enterprise architects and business teams—not a PRD, functional specification or detailed technical design. Questions and component choices follow the use case and available capabilities, not a fixed questionnaire or prescribed stack. Unknowns stay explicit without blocking a conditional proposal; field-level requirements and configuration are left for later design.

**Version 0.2.0 · Beta.** This project is still evolving. If you find a bug, incorrect recommendation, missing reference or confusing behaviour, please [create an issue](https://github.com/SAP/ai-native-architecture-advisor/issues/new).

> **Validate before using the proposal.** AI can hallucinate services, capabilities, integrations and references—even with source material and a capable model. Check recommendations against current SAP documentation and your actual landscape, availability, entitlements and security requirements. Treat the output as a draft for human review, not an approved implementation design or certification.

## Requirements

- An AI host that supports skills or plugins: **Claude Code**, **OpenAI Codex** or **Joule Work Desktop**. See the host guidance under [Install and use](#install-and-use).
- A capable reasoning model available to that host (see [Recommended models](#recommended-models)). The plugin does not provide or configure a model.
- **Node.js 22+**, only if you render the HTML brief locally or run the publishing tests. Normal skill usage inside the host needs no separate runtime.
- **Git**, for marketplace installation, updates and local development.
- Network access for installation and updates (via GitHub) and for your host's own model connection. The bundled reference data itself requires no additional service connection.

## What it is based on

The skill combines content and guidance from:

- [SAP AI-native North Star architecture](https://architecture.learning.sap.com/docs/ai-native-north-star-architecture): architectural vision and the User Experience, Process, Foundation and Platform layers.
- [SAP AI Golden Path](https://architecture.learning.sap.com/docs/ai-golden-path): AI and development approaches for the scenario.
- [SAP Architecture Center reference architectures](https://architecture.learning.sap.com/docs/ref-arch): implementation patterns, selected and explained by the agent according to their fit.

The repository includes a [North Star publication converted to Markdown](skills/ai-native-architecture-advisor/references/north-star.md), a [commit-pinned Golden Path text snapshot](skills/ai-native-architecture-advisor/references/official-ai-golden-path.md), curated guidance and dated reference data. [SOURCES.md](skills/ai-native-architecture-advisor/references/SOURCES.md) records where each source came from, its date/version, what was changed or omitted, and how maintainers update it. The Advisor's recommendations and numbered capability steps are advisory interpretations, not SAP certification levels. It does not assess partners or award validated status.

## What you get

The Advisor asks only the questions that materially affect the architecture, separates confirmed facts from assumptions, and explains the value and trade-offs of each proposed change. Keeping a suitable existing design is a valid recommendation.

The default collection is **`SAP AI Native Solutions/` in your workspace**, not inside the installed plugin or its `examples/`. The Advisor confirms the location once; you can choose another location. Each scenario gets its own named folder with three files:

| File | Purpose |
|---|---|
| `<slug>-solution-brief.md` | Use case, AI-native direction, proposed architecture, capability progression, solution stack and relevant reference architectures |
| `<slug>-reasoning-log.md` | Facts, assumptions, decisions, source checks and open questions |
| `<slug>-solution-brief.html` | Visual proposal that opens directly in a browser; no web server required |

The collection's `README.md` indexes previous proposals with their summary, status, last-updated date and links. Ask “Show my previous proposals” or “Continue the invoice-intake proposal” to find or resume work in that collection. Existing projects stay at their confirmed locations unless you request a move.

When the collection is inside a Git repository, the Advisor ensures that **that repository's** ignore rules exclude it before generating content. The plugin's own `.gitignore` cannot protect another repository. Already tracked files need a separate untracking decision; Git ignore is not access control or a backup. Sharing generated content is an explicit user choice.

Markdown is the content source. Continue the conversation to revise it; the Advisor regenerates the HTML. The proposed solution uses supported SAP runtimes and generative AI hub for solution-controlled LLM calls. That design guidance concerns the proposed SAP solution, not the model running your AI host.

## Recommended models

For architecture reasoning and proposal generation, prefer a capable reasoning model over the lightest, lowest-cost option:

- **Claude Code:** Opus or Fable, where available; Sonnet is also a useful quality/cost balance. See [Anthropic's model guidance](https://github.com/anthropics/skills/blob/main/skills/claude-api/shared/models.md).
- **Codex:** Astra or Sol, where available. See [OpenAI's model guidance](https://learn.chatgpt.com/docs/models).
- **Joule Work Desktop:** the model is provided by Joule; there is no separate reasoning model to select or configure.

Choose from the models your account and organization actually provide. These are recommendations, not a benchmark of this skill or a guarantee of correctness. Lighter models can help with simple revisions, but review complex architecture decisions with a stronger model and a human architect. The plugin does not select or change your model automatically.

## Install and use

One shared skill powers these hosts. Install through **one route per host** to avoid duplicate skill entries. The Claude Code and Codex routes use the repository's published default branch; unpushed local changes are not available to other users.

### Claude Code

Run these commands **inside Claude Code**:

```text
/plugin marketplace add https://github.com/SAP/ai-native-architecture-advisor.git
/plugin install ai-native-architecture-advisor@sap-ai-native-architecture-advisor
```

Choose the user scope if you want to use it across projects. Run `/reload-plugins` or start a new session after installation. Invoke the skill explicitly:

```text
/ai-native-architecture-advisor:ai-native-architecture-advisor Help me reimagine our supplier-confirmation process. Buyers chase missing PO confirmations in S/4HANA. We want to reduce manual follow-up while keeping approval decisions with buyers.
```

You can also describe a relevant SAP scenario naturally and let Claude select the skill. If it does not, use the explicit command above. See [Claude Code's plugin installation guide](https://code.claude.com/docs/en/discover-plugins).

### Codex

Run these commands **in your terminal**:

```bash
codex plugin marketplace add https://github.com/SAP/ai-native-architecture-advisor.git
codex plugin add ai-native-architecture-advisor@sap-ai-native-architecture-advisor
```

Start a new Codex thread/session after installation. In the app, look for **AI Native Architecture Advisor** in the plugin/skill picker; in the CLI, use `/skills` or type `$` to select the skill. For example:

```text
$ai-native-architecture-advisor:ai-native-architecture-advisor Help me reimagine our invoice-exception process. We process 3,000 invoices a month in S/4HANA and want to reduce manual matching without replacing the team's existing work surface. Create an AI Native Solution Brief and visual proposal.
```

If your Codex version has marketplace commands but no `plugin add`, install from that marketplace in its plugin interface, or use the standalone fallback below. See [OpenAI's plugin packaging and marketplace guidance](https://developers.openai.com/plugins/build/plugins).

### Joule Work Desktop

Joule doesn't use the plugin marketplace—it loads a skill from a local folder. Download the Joule build, unzip it, and add that folder in Joule's Skills section. Same guided discovery, delivered as Joule cards instead of files.

1. **Download the Joule build.** Grab just the Joule Work Desktop skill folder as a zip—no repo clone needed: [download `ai-native-architecture-advisor-jwd.zip` from the latest release](https://github.com/SAP/ai-native-architecture-advisor/releases/latest).
2. **Unzip it.** You'll get an `ai-native-architecture-advisor-jwd/` folder containing `SKILL.md` and its `references/`. Keep the folder intact—Joule reads the whole folder.
3. **Add it in Joule Work Desktop.** Open **Your extensions** (lower-left) → **Skills** → **+ New → Add Skill**, then select the unzipped `ai-native-architecture-advisor-jwd/` folder.
4. **Start designing.** Ask Joule *"Help me design an SAP AI solution"* and the Advisor delivers the AI Native Solution Brief as Joule cards.

A side-loaded skill folder is not marketplace-managed: for new releases, re-download the zip and add the folder again (see [Updating the plugin](#updating-the-plugin)).

### Standalone skill fallback

If plugins are unavailable in your host, clone this repository and copy the **whole** `skills/ai-native-architecture-advisor/` folder—not just `SKILL.md`—to:

| Host | Personal skill directory |
|---|---|
| Claude Code | `~/.claude/skills/ai-native-architecture-advisor/` |
| Codex | `~/.agents/skills/ai-native-architecture-advisor/` |

On Windows, use the equivalent directory under your user profile. Start a new session, then invoke `/ai-native-architecture-advisor` in Claude Code or select `$ai-native-architecture-advisor` in Codex. A copied skill is not marketplace-managed: update the clone and copy the folder again for new releases. Use an empty destination or review existing contents before replacing your own customizations.

## Working with the Advisor

Start with the problem, actors, desired outcome and any constraints you already know. You do not need a complete technical design. Confirm or correct the Advisor's assumptions, and choose where it should save the proposal.

Useful follow-ups:

```text
We already have an API for this action. Reuse it and explain whether MCP adds value.

Keep the current Fiori app. Show where a Joule interaction would genuinely help.

Compare the relevant SAP reference architectures, strongest fit first, and explain the trade-offs.

Review the proposal for unsupported claims and unresolved dependencies before I share it.
```

See the [fictional supplier-confirmation brief](examples/supplier-confirmation-solution-brief.md) and its [reasoning log](examples/supplier-confirmation-reasoning-log.md) for an example—not a prevalidated design to copy unchanged. `examples/` holds curated, publishable samples, not your generated projects.

## Self-contained reference data

The Advisor uses the files shipped in this repository. It does not call Discovery Center or Architecture Center APIs, refresh a user cache, or browse sources during its normal workflow. The publisher reads local files only. Generated reports embed their content and assets; the report and landing page load no remote fonts, scripts or images.

| Bundled source | Content and limits |
|---|---|
| `references/service-directory.json` | Non-deprecated Discovery Center catalogue entries with descriptions, features, plan summaries and public reference links; a dated snapshot, not proof of current availability |
| `references/ref-arch-index.json` | AI & Machine Learning and Data & Analytics architecture titles, descriptions, domains, products and source links; includes cross-domain entries with either tag, not full implementation guides |
| `references/north-star.md` | Text-only North Star publication supplied by the maintainer |
| `references/official-ai-golden-path.md` | Eight official Golden Path pages, combined as a commit-pinned text snapshot |
| Layer cards, capability map and AI Golden Path card | Curated selection guidance with source attribution |

These paths are inside `skills/ai-native-architecture-advisor/`. Source dates remain visible; the agent records material validation gaps rather than claiming a live check. External links remain available for a reader to open deliberately. Maintainers review and update bundled data in Git, preserve accurate capture dates, and ship changes through versioned plugin releases. Installed copies never refresh the data themselves.

Only the reference-architecture catalogue is narrowed to AI and Data. The four North Star layers and the service directory remain available for designing the complete solution. Reference cards use descriptions and source links; external diagram snapshots are not bundled. The proposal's own architecture overview is generated locally.

**Self-contained does not mean the AI host is offline.** The host still uses its configured model connection, and remote installation or updates use GitHub. This plugin adds no reference-service connection; it neither configures nor disables the host's networking. Any live research must be explicitly requested separately.

## Updating the plugin

**Plugin releases** update the skill instructions, curated content, scripts and template. To update a marketplace installation:

Claude Code:

```text
/plugin marketplace update sap-ai-native-architecture-advisor
/plugin update ai-native-architecture-advisor@sap-ai-native-architecture-advisor
/reload-plugins
```

Codex terminal:

```bash
codex plugin marketplace upgrade sap-ai-native-architecture-advisor
codex plugin add ai-native-architecture-advisor@sap-ai-native-architecture-advisor
```

Start a new Codex thread/session. Updating a separate Git clone alone does not update an installed plugin copy. Maintainers must increase both manifest versions for subsequent releases; the current version is `0.2.0` (Beta).

**Joule Work Desktop** is not marketplace-managed. A side-loaded folder does not update itself: for a new release, re-download the `ai-native-architecture-advisor-jwd/` zip, replace the folder, and add it again in Joule's Skills section as in [Install and use](#install-and-use).

## Local development

```bash
git clone https://github.com/SAP/ai-native-architecture-advisor.git ai-native-architecture-advisor
cd ai-native-architecture-advisor
claude --plugin-dir .
```

This Claude launch loads the local plugin for that session; it is not a persistent install. For Codex, add the local checkout with `codex plugin marketplace add .`, then install the plugin as above. Avoid registering both local and remote copies of the same marketplace.

From the repository root, render the example locally (Node.js 22+):

```bash
mkdir -p output
node skills/ai-native-architecture-advisor/scripts/publish-brief.mjs --brief examples/supplier-confirmation-solution-brief.md --out output/example.html
```

Add `--open` to open the report. There is no online/offline switch: publishing always uses bundled files. Focused publishing checks run with `node --test tests/companion.test.mjs`.

For instruction changes, start with [SKILL.md](skills/ai-native-architecture-advisor/SKILL.md). The [output contract](skills/ai-native-architecture-advisor/references/output-contract.md) owns the brief format and diagram JSON; the HTML template owns layout. Layer cards own the progression numbers. Keep these aligned without copying the contract back into the main skill.

```text
plugin.json                         Portable plugin manifest for Codex
.claude-plugin/                     Claude manifest + shared marketplace catalog
skills/ai-native-architecture-advisor/          One skill: SKILL.md, references, scripts, assets
examples/                           Fictional brief and reasoning log
tests/                              Focused publishing checks
docs/                               Project landing page
```

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) for the contribution process, the Developer Certificate of Origin (DCO) requirement and the guidelines on AI-generated code.

Please [create an issue](https://github.com/SAP/ai-native-architecture-advisor/issues/new) for any problem you find. Include the plugin version, your host and its version (Claude Code, Codex or Joule Work Desktop), model, steps to reproduce, expected result and relevant error or incorrect output. For a content issue, include the official source that supports the correction where possible. Remove customer data, credentials and confidential details before sharing prompts or proposals.

## Security / Disclosure

If you find any bug that may be a security problem, please follow our instructions [in our security policy](https://github.com/SAP/ai-native-architecture-advisor/security/policy) on how to report it. Please do not create GitHub issues for security-related doubts or problems.

## Code of Conduct

We as members, contributors, and leaders pledge to make participation in our community a harassment-free experience for everyone. By participating in this project, you agree to abide by its [Code of Conduct](https://github.com/SAP/.github/blob/main/CODE_OF_CONDUCT.md) at all times. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to engage.

## Licensing

Copyright 2026 SAP SE or an SAP affiliate company and ai-native-architecture-advisor contributors. Please see our [LICENSE](LICENSE) for copyright and license information. Detailed information including third-party components and their licensing/copyright information is available [via the REUSE tool](https://api.reuse.software/info/github.com/SAP/ai-native-architecture-advisor). Bundled source material retains its own attribution and terms; see [SOURCES.md](skills/ai-native-architecture-advisor/references/SOURCES.md).
