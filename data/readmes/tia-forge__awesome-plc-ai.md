# Awesome PLC AI [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of AI tools, agents and MCP bridges for **PLC engineering** — writing, reviewing, verifying and documenting control code for Siemens TIA Portal, CODESYS, TwinCAT, Studio 5000, GX Works and friends.

**中文简介**：面向 PLC / 自动化工程师的「AI × 工业控制」清单：MCP 网关、Agent 技能包、工程 Copilot、静态校验与仿真工具，以及厂商侧的工程智能体。

This list is maintained by 汇智网 (hubwiz.com). The maintainer's own product, TiaLink, is listed by the same criteria as everything else and disclosed at the end of this file.

**Scope** — things that help an engineer program, review, verify, document or operate PLC-based control systems with AI:

- MCP servers, gateways and bridges that connect an AI agent to an engineering tool or a live controller.
- Agent skills, rule packs and plug-ins for Claude Code, Codex, GitHub Copilot, Cursor and similar.
- Engineering copilots and code-intelligence products, vendor-built or third-party.
- Verification, linting, simulation and code-lifecycle tooling.
- Vendor AI platforms and foundation models, for orientation.
- Formats, standards, learning resources and current research.

**Out of scope** — general SCADA/MES analytics, robot learning, and marketing pages with nothing runnable behind them.

**How entries are written.** *Open source* means the repository carries an open-source licence, named with its SPDX id, together with a rounded star count. *Commercial* means closed source. *Source-available* means readable code with no reuse rights. *On-prem* means the tool runs with no cloud round-trip. Star counts, licences and vendor facts were last verified on 2026-10-15; they are a popularity hint, not a quality score.

> ⚠️ **Safety first.** PLC code runs machines. Nothing in this list removes the need for review, static analysis, simulation and on-machine commissioning. Safety functions belong in hardware (safety relay or safety PLC), hard interlocks in electrics or pneumatics, and no AI output should be downloaded to a live controller unchecked. Every tool here is a draft generator, not an authority.

## Contents

- [MCP bridges and gateways](#mcp-bridges-and-gateways)
  - [Siemens TIA Portal](#siemens-tia-portal)
  - [CODESYS](#codesys)
  - [Rockwell / Studio 5000](#rockwell--studio-5000)
  - [Beckhoff TwinCAT](#beckhoff-twincat)
  - [Mitsubishi GX Works](#mitsubishi-gx-works)
  - [Runtime and protocol bridges](#runtime-and-protocol-bridges)
- [Agent skills and rule packs](#agent-skills-and-rule-packs)
- [Engineering copilots, code intelligence and Industrial DevOps](#engineering-copilots-code-intelligence-and-industrial-devops)
- [Verification and static analysis](#verification-and-static-analysis)
- [Simulation and virtual controllers](#simulation-and-virtual-controllers)
- [Vendor engineering agents](#vendor-engineering-agents)
- [Industrial AI platforms and foundation models](#industrial-ai-platforms-and-foundation-models)
- [General-purpose coding agents](#general-purpose-coding-agents)
- [Formats and standards](#formats-and-standards)
- [Learning and community](#learning-and-community)
- [Reading: case studies, research and security](#reading-case-studies-research-and-security)
- [Before you connect an agent to a real project](#before-you-connect-an-agent-to-a-real-project)
- [Disclosure](#disclosure)
- [Review log](#review-log)

## MCP bridges and gateways

The layer that decides whether an agent can only talk about your project or actually work in it. Bridges either drive a vendor engineering API (Siemens Openness, CODESYS scripting, Rockwell L5X) or talk to a running controller.

### Siemens TIA Portal

- [TIA_Portal_Openness_MCP](https://github.com/bulaofen0036-coder/TIA_Portal_Openness_MCP) - Open source (MIT), ~310★. MCP server driving TIA Portal V20/V21 through Openness for any MCP client (Cursor, VS Code, Claude Desktop); ships a declarative CLI, skills and Git version control. The open engine behind the commercial TIA 助手 desktop app.
- [tiaportal-mcp](https://github.com/heilingbrunner/tiaportal-mcp) - Open source (MIT), ~110★. MCP server for TIA Portal project browsing, block import/export and compilation.
- [tia-portal-mcp](https://github.com/Czarnak/tia-portal-mcp) - Open source (MIT), ~80★. MCP server written specifically for LLM and agent workflows around TIA Portal.
- [vscode-tiaportal-mcp](https://github.com/heilingbrunner/vscode-tiaportal-mcp) - Open source (MIT), ~60★. VS Code extension that exposes TIA Portal to agents over MCP.
- [tiacommander-mcp](https://github.com/a4webdev/tiacommander-mcp) - Source-available. Connects any MCP-capable AI assistant to TIA Openness; the MCP face of the commercial TiaCommander tool.
- [tia-copilot-genai-bridge](https://github.com/feelautom/tia-copilot-genai-bridge) - Open source (MIT), ~20★. Bridges generative AI to TIA Portal for SCL generation and project-structure exploration; the open part of the T-IA Connect platform.
- [Smart200-MicroWIN-MCP](https://github.com/bulaofen0036-coder/Smart200-MicroWIN-MCP) - Source-available. MCP engine for S7-200 SMART / STEP 7-MicroWIN — the low-end and installed-base side of the Siemens world.
- [TiaLink](https://tia.hubwiz.com/tia-link) - Commercial, on-premises. TIA Portal MCP gateway over Siemens Openness, agent-agnostic (any MCP client with Streamable HTTP and a Bearer header). Covers hardware and network configuration, block and SCL import, compile, HMI screens, PLCSIM download and read-back, with dry-run, compile gate and rollback. **Maintained by the maintainer of this list.** Early access: no public download.

### CODESYS

- [codesys-mcp-toolkit](https://github.com/johannesPettersson80/codesys-mcp-toolkit) - Open source (MIT), ~125★. MCP server toolkit for automating CODESYS projects.
- [Codesys-MCP](https://github.com/luke-harriman/Codesys-MCP) - Open source (MIT), ~85★. Exposes 41 tools of the CODESYS V3.5 scripting API, with a ready-to-copy `.mcp.json` for Claude Code.
- [mcptoolkit-for-codesys](https://github.com/zbest1000/mcptoolkit-for-codesys) - Open source (MIT), ~20★. Drive CODESYS V3.5 SP22 from Claude or any MCP client.

### Rockwell / Studio 5000

- [studio5000-AI-Assistant](https://github.com/rivie13/studio5000-AI-Assistant) - Source-available, ~35★. Assistant for Studio 5000 / Logix projects. Readable Python, but no licence file: treat reuse rights as reserved.
- [studio5000-mcp-server](https://github.com/Nodeblue-AI/studio5000-mcp-server) - Open source (MIT), ~20★. MCP server that parses L5X exports to give an agent real project context.

### Beckhoff TwinCAT

- [twincat-validator-mcp](https://github.com/agenticcontrolio/twincat-validator-mcp) - Open source (MIT), ~35★. Validates and auto-fixes TwinCAT XML — a useful "verify before compile" primitive for agent loops.
- [twincat-agent](https://github.com/TechIndustryX/twincat-agent) - Source-available, ~30★. Agent tooling for TwinCAT projects.

### Mitsubishi GX Works

- [gxworks-agent](https://github.com/Arienax/gxworks-agent) - Open source (MPL-2.0). Agent integration for GX Works2, usable from Codex and MCP clients.
- [gxworks3-mcp-bridge](https://github.com/coder007rahul/gxworks3-mcp-bridge) - Open source (MIT). Read, write and compile Structured Text projects in GX Works3 over MCP.

### Runtime and protocol bridges

- [OPCUA-MCP](https://github.com/IndustriAgents/OPCUA-MCP) - Open source (MIT), ~30★. OPC UA MCP server documented for Claude, ChatGPT, Gemini and Cursor.
- [opcua-mcp](https://github.com/kukapay/opcua-mcp) - Open source (MIT), ~30★. MCP access to OPC UA servers for reading live tag values.
- [s7-mcp-bridge](https://github.com/cadugrillo/s7-mcp-bridge) - Open source (MIT), ~25★. Reaches S7 PLCs through their built-in web API for runtime monitoring. Read-oriented: it gives an agent plant data, not engineering capability.

## Agent skills and rule packs

Skills, prompts and rule packs are where the working practice lives: how an agent should plan, which checks it must run, what it may never do. This is the part that experienced engineers say took real effort to get right.

- [totally-integrated-claude](https://github.com/Czarnak/totally-integrated-claude) - Open source (MIT), ~70★. TIA Portal automation plug-in for agents: works with Claude Code, Codex, GitHub Copilot in VS Code and the Copilot CLI.
- [tia-harness](https://github.com/renanlido/tia-harness) - Open source (MIT), ~10★. Claude Code plug-in bundling skills, subagents and a TIA MCP server.
- [siemens-tia-skill-suite](https://github.com/arkbsz/siemens-tia-skill-suite) - Open source (MIT), ~5★. Skill suite for Siemens TIA Portal work.
- [plc-automation-skill](https://github.com/Michaelr1985/plc-automation-skill) - Source-available. A Codex skill pack for PLC automation tasks.
- [phobic-iec-61131-3-skill](https://github.com/phobicdotno/phobic-iec-61131-3-skill) - Source-available, ~2★. Claude Code plug-in with IEC 61131-3 rules and conventions.
- [codesys-modifier-skill](https://github.com/KRST-Kerstin/codesys-modifier-skill) - Source-available. A Claude skill that exports PLCopen XML, modifies it and re-imports the result.

## Engineering copilots, code intelligence and Industrial DevOps

Commercial products that already wrap the whole loop — project parsing, documentation, verification, versioning — rather than exposing raw tools.

- [T-IA Connect](https://t-ia-connect.com/) - Commercial, on-premises. TIA Portal engineering automation platform by FeelAutom (France): several hundred MCP tools and REST endpoints across 24 categories, workplan sequencing, PLCSIM Advanced, a test harness, Git-based version control and FAT/SAT report packages. Supports TIA Portal V17–V21. Data stays on the machine, but installation and activation require internet. Day-pass and monthly seat pricing.
- [PLCs.ai](https://www.plcs.ai/) - Commercial. Cross-brand PLC code understanding, troubleshooting and documentation: parses TIA Portal, Studio 5000 and CODESYS V3 projects, adds runtime tag context through a desktop companion app, and exposes an API plus MCP server. Changes are produced as proposals for approval, never as automatic downloads. Priced per PLC project, not per seat.
- [Copia Automation](https://copia.io/) - Commercial. Industrial DevOps for PLC code: Git-based source control, DeviceLink device-to-code consistency checks and backups, Copia AI for documentation and Ladder-to-Structured-Text conversion, Copia Actions workflows. Covers Rockwell, Siemens, Omron Sysmac Studio, Schneider Control Expert, B&R and CODESYS. The pitch is OT resilience and auditability first.
- [TIA 助手](https://www.aeenhance.com/) - Commercial, on-premises option. Desktop AI workbench for TIA Portal V20/V21 from a one-person team: Openness plus S7CommPlus, several hundred engine tools, MCP and skill extensions, optional local models through Ollama, and an approve-before-write workflow. Distributed via WeChat with machine-bound licensing.
- [RealPLC](https://realplc.com/) - Commercial. Closed-source desktop connector plus cloud agent for CODESYS and Siemens TIA Portal, built around a generate → verify → diagnose → fix loop. Note: its GitHub repository distributes binaries and is not open source.
- [rungs.dev](https://rungs.dev/) - Free tier. Browser PLC simulator for ladder and Structured Text with a built-in test runner, trends and the Relay AI assistant, which reads the actual logic, tags and tests instead of pasted snippets. Aimed at learning, teaching and prototyping.
- [Outerport](https://outerport.com/) - Commercial. Turns electrical and control design into a structured model so drawings, BOM, calculations and control-logic simulation all come from one source; can parse existing P&IDs and single-line diagrams. Public references include semiconductor equipment makers and EPC firms.
- [electrical-copilot](https://github.com/clei32879-gif/electrical-copilot) - Open source (MIT per the repository licence file), ~5★. Local electrical-engineer agent that reads and writes ladder logic and emits project files for Xinje, Mitsubishi, Inovance, Siemens, Panasonic and Delta.

## Verification and static analysis

Where the honest wins are. An agent that can lint, review and prove its output is worth more than one that writes faster.

- [Spec2Control](https://github.com/hkoziolek/Spec2Control) - Open source (Apache-2.0), ~40★. Turns control narratives into IEC 61131-3 function block diagrams through an explicit LLM workflow.
- [plc-st-review](https://github.com/HeytalePazguato/plc-st-review) - Open source (MIT), ~15★. Deterministic semantic linter and pull-request reviewer for IEC 61131-3 Structured Text — catches the class of mistake a model will not notice about itself.
- [eplan-pdf-io-extraction](https://github.com/wenjunyi16-del/eplan-pdf-io-extraction) - Source-available. Extracts PLC I/O lists from EPLAN PDF schematics into Excel for tagging and variable-table import. Documentation is in Chinese.

## Simulation and virtual controllers

- [OpenPLC](https://github.com/thiagoralves/OpenPLC_v3) - Open source (GPL-3.0), ~1.5k★. Open-source software PLC runtime widely used for learning and test rigs. The v3 repository is archived; kept here as the reference implementation of an open PLC runtime.
- [PLCnext Community](https://www.plcnext-community.net/) - Vendor ecosystem (Phoenix Contact). Linux-based, software-defined controller platform with a public developer community; a virtual PLC can host AI workloads next to the control program.
- [Neuron Industries](https://neuronindustries.com/) - Commercial, announced for 2027. AI-native controller positioning itself against the PLC itself: natural-language logic compiled to deterministic real-time Python, high scan rates, built-in IDE, HMI and historian.

## Vendor engineering agents

What each automation vendor ships itself. Useful precisely because the limits are the point: these agents see one ecosystem, and their competence is scoped to it.

- [Siemens TIA Portal](https://www.siemens.com/global/en/products/automation/industry-software/automation-software/tia-portal.html) - Eigen Engineering Agent (2026) and Industrial Copilot (2023) inside the TIA Portal ecosystem, with the Industrial Foundation Model underneath. The official path, and the boundary of it.
- [FactoryTalk Design Studio](https://www.rockwellautomation.com/en-us/products/software/factorytalk/design-studio.html) - Generative Copilot for Logix projects, from Rockwell Automation. Practitioner reports are consistent: strong at explaining and documenting existing code, unremarkable at writing new logic.
- [TwinCAT](https://www.beckhoff.com/en-en/products/automation/twincat/) - Beckhoff's CoAgent (2025) is a built-in AI programming assistant for TwinCAT 3.
- [CODESYS](https://www.codesys.com/) - The vendor-neutral IEC 61131-3 toolchain, where AI integration is moving from code assistant toward a chat-based engineering assistant.
- [WAGO](https://www.wago.com/global/) - Controller and I/O vendor shipping an AI assistant for engineering, announced 2026.
- [EcoStruxure](https://www.se.com/ww/en/) - Industrial AI on the EcoStruxure platform with Microsoft, from Schneider Electric. Their 2026 acquisitions of Cognite (industrial data) and PTC (design and PLM) are the clearest statement that the value is in the data layer, not the chatbot.
- [Omron](https://www.omron.com/global/en/) - DX1 edge controller plus digital-twin work with NVIDIA Omniverse.
- [Experion](https://www.honeywell.com/us/en) - Honeywell's Experion Cognition (2026) pushes the DCS toward an "autonomous control room" — agentic operation above the control layer.
- [Emerson](https://www.emerson.com/en-us) - Enterprise industrial AI on AspenTech, with AI advisors for process operations.
- [ctrlX AUTOMATION](https://www.boschrexroth.com/en/us/) - Additions around AI, security and edge compute on an open automation platform, from Bosch Rexroth.

## Industrial AI platforms and foundation models

Orientation layer: who is building the models and data platforms that PLC-side tools will eventually call. Links point to the vendor's own site.

- [SUPCON (中控技术)](https://www.supcon.com/) - China. TPT process-industry foundation model and an industrial AI data alliance; the most visible Chinese industrial LLM play alongside its DCS business.
- [HollySys (和利时)](https://www.hollysys.com/) - China. XMagital industrial world model and an "autonomous operation" direction for control systems.
- [Baosight (宝信软件)](https://www.baosight.com/) - China. Steel-industry vertical foundation model: "AI + steel" white paper, hundreds of AI scenarios in production.
- [COSMOPlat (卡奥斯)](https://www.cosmoplat.com/) - China. Tianzhi industrial LLM, positioned as a digital plant manager.
- [Huawei (华为)](https://www.huawei.com/cn/) - China. Pangu models plus Ascend compute and industrial HarmonyOS: the platform layer under a large part of China's industrial AI.
- [AInnovation (创新奇智)](https://www.ainnovation.com/) - China. Kongming industrial large model and an agent-development framework.
- [SmartMore (思谋科技)](https://www.smartmore.com/) - China. Industrial AI agents for inspection and manufacturing, seeking a public listing.
- [Blacklake (黑湖科技)](https://www.blacklake.cn/) - China. Manufacturing collaboration plus industrial AI, profitable after a large D round.
- [Inovance (汇川技术)](https://www.inovance.com/) - China. Drives and PLC vendor investing in edge models and robotics platforms.
- [Xinje (信捷电气)](https://www.xinje.com/) - China. XS Studio programming environment for the domestic PLC installed base.
- [Advantech (研华科技)](https://www.advantech.com/zh-cn) - Taiwan. Edge AI compute and industrial PCs for physical AI deployments.
- [Kyland (东土科技)](https://www.kyland.com/) - China. Intewell industrial operating system for equipment control.

## General-purpose coding agents

Not PLC-specific, listed because these are what engineers actually connect to the bridges above. The bridges matter more than the model choice: the same agent is far more useful with project context than with pasted code snippets.

- [Claude Code](https://claude.com/product/claude-code) - Anthropic's terminal coding agent; the most frequently referenced agent in the PLC bridge ecosystem.
- [GitHub Copilot](https://github.com/features/copilot) - In-editor completion plus CLI and agent modes, used inside VS Code for Structured Text and scripting work.
- [Codex](https://openai.com/codex/) - OpenAI's coding agent, with a growing set of PLC skill packs built around it; its terminal CLI is released under Apache-2.0.
- [Lingma (通义灵码)](https://lingma.aliyun.com/) - Alibaba Cloud's coding assistant, widely used in Chinese enterprises.

## Formats and standards

Know what your tool is emitting. Most cross-tool work in this space is an exchange-format problem before it is a model problem.

- [PLCopen](https://plcopen.org/) - The organisation behind PLCopen XML and other interchange specifications; the format most tools use to move code between IDEs.
- [OPC Foundation](https://opcfoundation.org/) - OPC UA specifications and information models — the interface most runtime agent bridges read from.

Also worth knowing: IEC 61131-3 for the languages themselves, SimaticML for TIA Portal block export, and L5X for Rockwell Logix, plus vendor HMI formats that rarely exchange cleanly.

## Learning and community

- [r/PLC](https://www.reddit.com/r/PLC/) - The main practitioner community. Search before posting, and note that AI-generated content is restricted by the subreddit rules.
- [controlbyte.tech](https://controlbyte.tech/) - Practitioner tutorials and notes on PLC programming and industrial AI.
- [AI in industrial and PLC engineering (汇智网 hub)](https://www.hubwiz.com/blog/ai-industrial-stack/) - Chinese-language content map: writing PLC code with AI, TIA Portal and Openness automation, PLC fundamentals, simulation. Maintained by the maintainer of this list.

A warning about Chinese-language sources: quantity is high and signal is mixed. CSDN in particular is dominated by content farms, with recycled titles and unreliable date stamps. Prefer vendor documentation, project repositories and this list's vendor links.

## Reading: case studies, research and security

- [How Wipro PARI accelerates PLC code generation using Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/how-wipro-pari-accelerates-plc-code-generation-using-amazon-bedrock/) - Industry case study of LLM-based PLC code generation at an engineering organisation.
- [Engineering at scale: how AI is transforming PLC coding](https://blog.se.com/digital-transformation/artificial-intelligence/2025/11/14/engineering-at-scale-how-ai-is-transforming-plc-coding/) - Schneider Electric on the productivity argument in engineering teams.
- [AI-generated exploit scripts target Siemens S7 PLCs in US critical infrastructure](https://thehackernews.com/2026/08/ai-generated-exploit-scripts-target.html) - The security side of the same capability: AI lowers the barrier to attacking control systems, which is why verification and network isolation are not optional.

## Before you connect an agent to a real project

A short checklist distilled from practitioner reports, worth applying to any tool in this list:

1. Read-only first — begin with a bridge that only reads the project, and let the agent summarise, cross-reference and document before it writes anything.
2. Require a compile gate — no change is "done" until the project compiles clean; treating warnings as errors is the working standard reported by engineers who get results.
3. Prefer a diff or a proposal over a write — tools that produce an approvable change, and tools with dry-run and rollback, keep the review burden proportional.
4. Simulate before hardware — PLCSIM Advanced or an equivalent virtual controller, then read the values back and compare against expectations.
5. Keep the data in — on-premises operation is a procurement requirement in most plants, and a practical one for anything involving real project files.
6. Check the licence, not the star count — a repository that only distributes binaries is not an open-source ecosystem, however many stars it carries.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) first — entries need a stable public link, a stated licence and a description that says what the thing actually does. One pull request per addition.

## Disclosure

This list is maintained by [汇智网 (hubwiz.com)](https://www.hubwiz.com/), which sells TiaLink, a commercial TIA Portal MCP gateway, and provides related engineering tools. Those products appear in this list (**TiaLink** under Siemens TIA Portal and the Chinese-language hub under Learning and community), marked as maintained by the maintainer of this list. They are listed by the same criteria as everything else, entries are not ranked, and the maintainer's products are capped at two entries. Corrections from affected vendors are welcome and will be applied to the entry text.

All product names and trademarks belong to their respective owners. Listing here does not imply endorsement by or affiliation with any vendor, and 汇智网 is not affiliated with or endorsed by Siemens AG.

The content of this list is dedicated to the public domain under CC0 1.0 (see [LICENSE](LICENSE)). Resources linked from it remain under their own licences and terms.

## Review log

**2026-10-15** — first published. Every link was opened and checked; star counts, licences and vendor facts were verified on that date.
