<div align="center">

<a href="https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5-1"><img src="images/banner.png" alt="Claude Fable 5.1 high-signal use case repository banner" width="760"></a>

[![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)
[![MuAPI support](https://img.shields.io/badge/MuAPI-Fable_5.1_coming_soon-111111)](https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5-1)
[![Official API](https://img.shields.io/badge/Official_API-claude--fable--5--1-cc785c)](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1)
[![Model docs](https://img.shields.io/badge/Docs-Read-blue)](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1)
[![Website](https://img.shields.io/badge/Website-Anthropic-orange)](https://www.anthropic.com/claude/fable)
[![Build AI SaaS](https://img.shields.io/badge/Build_AI_SaaS-50%2B_templates-22c55e)](https://github.com/Anil-matcha/awesome-generative-ai-apps)

[![English](https://img.shields.io/badge/English-Read-111111)](README.md)

</div>

## Related Projects

- [awesome-claude-fable-5](https://github.com/Anil-matcha/awesome-claude-fable-5) — Predecessor use-case index and clearly labeled Claude Fable 5 baseline archive.
- [awesome-gpt-6-astra](https://github.com/Anil-matcha/awesome-gpt-6-astra) — Cross-model companion covering evidence-backed GPT-6 Astra workflows, API patterns, evaluations, and safety notes.
- [awesome-gemini-4-pro](https://github.com/Anil-matcha/awesome-gemini-4-pro) — Evidence-led Gemini frontier-model use cases, prompts, evaluations, and release tracking.
- [awesome-gemini-4-carbon](https://github.com/Anil-matcha/awesome-gemini-4-carbon) — Source-linked tracker for Google's Gemini 4 Carbon: cyber and coding benchmarks, pricing, restricted-access status.
- [muapi-cli](https://github.com/SamurAIGPT/muapi-cli) — Command-line access to MuAPI models, useful when Fable 5.1 becomes available there.
- [muapi-skills](https://github.com/SamurAIGPT/muapi-skills) — Schema-driven agent skills for image, video, and audio workflows through MuAPI.
- [awesome-generative-ai-apps](https://github.com/Anil-matcha/awesome-generative-ai-apps) — Production-ready AI SaaS templates for turning model workflows into applications.
- [MuAPI model catalog](https://muapi.ai/docs/models) — Current model availability and integration documentation.
- [MuAPI playground](https://muapi.ai/playground) — Interactive access to available models while the Fable 5.1 MuAPI route is being prepared.

## 🍌 Introduction

Welcome to the Claude Fable 5.1 high-signal use case repository.

**We collect real-world usage cases, tutorials, integrations, migration notes, and evaluations for Claude Fable 5.1, curated from first-party documentation, public demos, and creator communities.**

Claude Fable 5.1 launched on September 1, 2026. The current 5.1 section therefore prioritizes release evidence, API behavior, prompt patterns, benchmark results, and early production reports. The 94 entries in the baseline archive are explicitly labeled Claude Fable 5: they are useful predecessor evidence, but they are not silently relabeled as 5.1 evaluations.

Each current case links back to its original source. Community reports are labeled as such, while official capability and pricing claims link directly to Anthropic or Claude Platform documentation.

**MuAPI support for Claude Fable 5.1 is coming soon.** The model will be added to the MuAPI catalog when the route is live. Until then, use the official Claude API below; this README will be updated with the model-specific MuAPI playground and endpoint as soon as they are available.

| Surface | Identifier | Current details |
|---|---|---|
| **Claude API** | `claude-fable-5-1` | $10 / MTok input; $50 / MTok output |
| **Prompt-cache reads** | Fable 5.1 cache | $0.25 / MTok, 75% lower than Fable 5 |
| **Batch API** | Fable 5.1 batch | $5 / MTok input; $25 / MTok output |
| **AWS Bedrock** | `anthropic.claude-fable-5-1` | Available on Amazon Bedrock |
| **Google Cloud** | `claude-fable-5-1` | Available on Claude on Google Cloud |
| **MuAPI** | Coming soon | Model-specific route will be added when live |

> Pricing and availability can change. See the [official Fable 5.1 model documentation](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1) for the current contract.

## 📊 Overview

- **10 current Claude Fable 5.1 cases** covering the launch, API migration, prompting, benchmarks, research, safeguards, and early production use.
- **94 Claude Fable 5 baseline cases** retained as a clearly labeled predecessor archive for transferable workflows and comparisons.
- Covers coding agents, long-running automation, games, visual design, 3D simulations, knowledge work, tutorials, API integrations, benchmarks, pricing, and practical limits.
- Use this repo to find evidence-backed workflows, compare the 5.1 upgrade path, discover reproducible prompt patterns, and track what is still early or unverified.

> [!NOTE]
> The collection favors concrete evidence over hype: reproducible prompts, shipped demos, benchmark methods, integration notes, cost data, and clearly stated caveats. Early 5.1 reports may be limited to a single account, surface, or partner evaluation.

> [!TIP]
> **MuAPI support is coming soon.** Follow [MuAPI](https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=awesome-claude-fable-5-1) for the model-specific playground and pricing once Claude Fable 5.1 is added.

> 🚀 **Want to build your own AI SaaS with Fable 5.1?** [Awesome Generative AI Apps](https://github.com/Anil-matcha/awesome-generative-ai-apps) — 50+ production-ready AI SaaS templates with Stripe billing built in. Fork one, brand it, start charging.

## 🧭 Read First: Fable 5.1 in One Page

- **Model ID:** `claude-fable-5-1`; the model is available on the Claude API and partner platforms.
- **Context and output:** 1M-token context window and up to 128k output tokens.
- **Thinking:** adaptive thinking is always on; control depth with `effort`, not a legacy thinking budget.
- **Migration:** forced `tool_choice` values of `any` and `tool` are rejected; keep returned thinking blocks unchanged and keep conversation history append-only.
- **Safeguards:** refusals can return HTTP 200 with `stop_reason: "refusal"`; configure fallback handling for requests routed to Claude Opus 4.8 or Claude Opus 5.
- **Retention:** 30-day data retention applies by default; eligible enterprise customers may use zero-data-retention arrangements while Enterprise Frontier Safeguards roll out.

Read the [official release notes and migration guide](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1) before changing a production agent.

<a id="-quick-api-access"></a>
## ⚡ Quick API Access

Use Claude Fable 5.1 through the official Claude API for now. MuAPI support is planned and will be documented here once the model-specific route is live.

```bash
export ANTHROPIC_API_KEY="your-api-key"

curl https://api.anthropic.com/v1/messages \
  --header "x-api-key: $ANTHROPIC_API_KEY" \
  --header "anthropic-version: 2023-06-01" \
  --header "content-type: application/json" \
  --data '{
    "model": "claude-fable-5-1",
    "max_tokens": 4096,
    "output_config": {"effort": "high"},
    "messages": [
      {"role": "user", "content": "Explain quantum entanglement in simple terms."}
    ]
  }'
```

## 📑 Menu

| Section | Cases |
|---|---|
| [🆕 Claude Fable 5.1: Launch and Current Evidence](#fable-51-launch-and-current-evidence) | Case 95-104 |
| [📚 Claude Fable 5 Baseline Archive](#fable-5-baseline-archive) | Case 1-94 |
| [💻 Coding and Code Generation](#coding-and-code-generation) | Case 1-6 |
| [🤖 Agents and Long-Running Automation](#agents-and-long-running-automation) | Case 7-8 |
| [🎮 Games and Interactive Demos](#games-and-interactive-demos) | Case 9-12 |
| [🎨 Visual, Design, Video, and 3D](#visual-design-video-and-3d) | Case 13-16 |
| [📚 Documents, Knowledge Work, and Research](#documents-knowledge-work-and-research) | Case 17-19 |
| [🧭 Tutorials, Courses, and Prompt Resources](#tutorials-courses-and-prompt-resources) | Case 20-28 |
| [🔌 Platform, API, and Tool Integration](#platform-api-and-tool-integration) | Case 29-34 |
| [📏 Evaluations, Comparisons, and Limits](#evaluations-comparisons-and-limits) | Case 35-94 |
| [🙏 Acknowledge](#acknowledge) | Credits and correction policy |

<a id="fable-5-baseline-archive"></a>
## 📚 Claude Fable 5 Baseline Archive

The following 94 entries are the original Claude Fable 5 collection carried forward from [awesome-claude-fable-5](https://github.com/Anil-matcha/awesome-claude-fable-5). They remain useful for transferable workflows, historical comparisons, and prompt ideas, but they should not be read as direct Fable 5.1 measurements.

### [💻 Coding and Code Generation](#coding-and-code-generation)

| Case | What it shows | Type |
|---|---|---|
| [Cursor Multi-Stage Workflow](#case-1) | Use Fable 5 as the plan-review and critique step inside a multi-model Cursor workflow, then hand implementation and revision back to cheaper or specialized models. | Evaluation |
| [Recreating GitHub from a Screenshot](#case-2) | Paste a product screenshot into an agentic coding tool and ask Fable 5 to recreate the interface with working functionality. | Demo |
| [One-Prompt Black Hole Simulation](#case-3) | Give Fable 5 one detailed creative-coding prompt and ask it to produce a self-contained Three.js physics visualization. | Tutorial |
| [One-Shot macOS-Style Web OS](#case-4) | Ask Fable 5 for a complete single-file web OS and let it build the UI shell, apps, interactions, audio, and embedded game behavior in one pass. | Tutorial |
| [Building Spawn 5.0 with 1,687 Prompts](#case-5) | Use Fable 5 as a long-session engineering partner across many prompts, with the human shifting from architecture to judging output quality. | Tutorial |
| [Large Pull Request Review with Findings](#case-6) | Point Fable 5 at a large pull request and ask it to review correctness, false positives, real bugs, and polish issues. | Demo |

### [🤖 Agents and Long-Running Automation](#agents-and-long-running-automation)

| Case | What it shows | Type |
|---|---|---|
| [Long-Horizon Relay Workflow Review](#case-7) | Use Fable 5 for ambitious long-horizon work: site rebuilds, programmatic content pipelines, voice matching, security review, and final quality checks. | Evaluation |
| [Diagnosing an Infrastructure Outage and Opening a Fix PR](#case-8) | Give Fable 5 access to infra clues such as logs, database errors, and image digests, then ask it to diagnose the outage and prepare the fix. | Evaluation |

### [🎮 Games and Interactive Demos](#games-and-interactive-demos)

| Case | What it shows | Type |
|---|---|---|
| [Finger-Tracking Dino Runner](#case-9) | Ask Fable 5 to build a browser game that uses finger tracking as the input mechanic. | Demo |
| [Two-Sentence Racing Game Build](#case-10) | Give Fable 5 a very short game prompt and let it generate maps, modes, music, UI, and game assets in one run. | Tutorial |
| [Installable Terminal Minecraft in Rust](#case-11) | Run Fable 5 through a terminal coding harness and ask it to build an installable Rust terminal game. | Demo |
| [Minecraft Clone with Time and Cost](#case-12) | Use one prompt to ask Fable 5 for a playable Minecraft-style clone, then evaluate time, cost, code volume, and feature coverage. | Tutorial |

### [🎨 Visual, Design, Video, and 3D](#visual-design-video-and-3d)

| Case | What it shows | Type |
|---|---|---|
| [Full Reproducible Ecommerce Email Prompt](#case-13) | Give Fable 5 a complete creative brief for a brand email mockup, including exact sections, product requirements, visual direction, and constraints. | Tutorial |
| [Swiss Lever Watchmaker Benchmark](#case-14) | Use Fable 5 on a mechanical simulation benchmark and ask it to implement, verify, and iterate on physical correctness. | Evaluation |
| [Three.js Friends Apartment Scene](#case-15) | Prompt Fable 5 to turn a floor plan and scene reference into a navigable Three.js environment. | Evaluation |
| [Solar System Simulation with Prompt and URL](#case-16) | Use Fable 5 to build an astronomy simulation from physics principles, iterating until the simulation and public output are ready. | Tutorial |

### [📚 Documents, Knowledge Work, and Research](#documents-knowledge-work-and-research)

| Case | What it shows | Type |
|---|---|---|
| [Stripe and Scientific Workflow Evidence](#case-17) | Use this as evidence for enterprise migration and scientific workflow claims, not as a copy-paste prompt. | Evaluation |
| [Policy Memo and Track-Changes Workflows](#case-18) | Use Fable 5 for long-form qualitative document work: track changes, comment triage, and transcript-driven edits. | Tutorial |
| [Deep Research Prompt and Output](#case-19) | Ask Fable 5 a research-style question and evaluate whether it can produce a structured, historically grounded long answer. | Demo |

### [🧭 Tutorials, Courses, and Prompt Resources](#tutorials-courses-and-prompt-resources)

| Case | What it shows | Type |
|---|---|---|
| [How Fable 5 Changes Claude Code Workflows](#case-20) | Use Fable 5 by setting direction, context, goals, and verification criteria instead of micromanaging every step. | Demo |
| [One-Billion-Token Review and Routing Strategy](#case-21) | Use Fable 5 for frontier planning and review, then route high-volume implementation to cheaper models. | Tutorial |
| [Defensive Device Hardening Prompt](#case-22) | Run a step-by-step defensive hardening prompt where Fable 5 inventories devices, gives exact checks, and waits for verification. | Tutorial |
| [Full-Site Design Audit Goal Prompt](#case-23) | Use `/goal` to make Fable 5 boot a site, screenshot pages, audit UX, write a report, and fix safe small issues. | Tutorial |
| [Long-Form Creative Workflow Division](#case-24) | Use Fable 5 to design stable formats and examples, then hand that structure to another generation system for domain-specific output. | Tutorial |
| [Beginner Guide to Using Fable 5](#case-25) | Use Fable 5 with goal-oriented prompts, verification loops, and effort settings instead of small step-by-step instructions. | Evaluation |
| [Copy-Paste Repository Audit Prompt](#case-26) | Paste the repository audit prompt into Fable 5 and ask for file-backed discovery, findings, strategy, and a milestone task plan. | Tutorial |
| [Limited-Window Usage Strategy](#case-27) | Spend Fable 5 usage on audit, architecture, and planning while the access window is favorable, then use cheaper models for execution. | Tutorial |
| [Using Goals and Workflows in Claude Code](#case-28) | Use Fable 5 as a thought partner before implementation, then combine `/goal` and workflows to execute and verify the plan. | Tutorial |

### [🔌 Platform, API, and Tool Integration](#platform-api-and-tool-integration)

| Case | What it shows | Type |
|---|---|---|
| [Hermes Agent Integration Setup](#case-29) | Configure Hermes to use `anthropic/claude-fable-5` for complex `/goal` runs and cached long-horizon tasks. | Tutorial |
| [Capabilities, Pricing, and Subscription Notes](#case-30) | Use this case to understand when Fable 5 is available, what it costs, and which guarded domains may fall back to another model. | Tutorial |
| [Launch, Access, Pricing, and Safety Summary](#case-31) | Use this launch summary to choose access route, API model name, context window, caching strategy, and subscription timing. | Tutorial |
| [Advisor-Based Cost Reduction Strategy](#case-32) | Use Fable 5 as an advisor or reviewer in a cheaper-model workflow when marginal intelligence is worth the cost. | Integration |
| [Pricing, Access, and Safety Guardrails](#case-33) | Use this case to understand Fable 5 access, API pricing, and safety fallback behavior before planning workloads. | Integration |
| [One-Line Swarms Integration](#case-34) | Set the Swarms model name to `anthropic/claude-fable-5` and run Fable 5 through the Swarms framework or API. | Integration |

### [📏 Evaluations, Comparisons, and Limits](#evaluations-comparisons-and-limits)

| Case | What it shows | Type |
|---|---|---|
| [Fable 5 vs GPT-5.5 Cost and Quality Comparison](#case-35) | Compare Fable 5 and GPT-5.5 on the same coding task to judge output quality, runtime, and tool cost. | Evaluation |
| [AA-Omniscience Benchmark Result](#case-36) | Use this benchmark case to evaluate Fable 5 on knowledge accuracy and hallucination behavior. | Evaluation |
| [Artificial Analysis Intelligence Index Result](#case-37) | Use this case to benchmark Fable 5's overall intelligence ranking against other frontier models. | Evaluation |
| [GDPval-AA Agentic Knowledge Work Benchmark](#case-38) | Use this case to evaluate Fable 5 on agentic real-world knowledge work. | Evaluation |
| [One-Week First Impressions and Pricing Mechanics](#case-39) | Use this first-impressions case to decide where Fable 5 is strongest, especially game design and systems planning. | Integration |
| [Cost and Speed Comparison](#case-40) | Use this comparison to decide whether the quality gain justifies higher cost and slower long-horizon runs. | Evaluation |
| [Claude Code Hands-On Notes](#case-41) | Use this case to evaluate Fable 5 inside Claude Code, including tool use, personality, and remaining rough edges. | Demo |
| [Creative Writing Benchmark Result](#case-42) | Use this benchmark case to judge Fable 5's short-fiction writing quality and refusal behavior. | Evaluation |
| [Multi-Benchmark Launch Summary](#case-43) | Use this launch benchmark summary to understand the headline scores most relevant to coding agents and complex tasks. | Evaluation |
| [Benchmark and Pricing Comparison with GPT-5.5](#case-44) | Use this comparison to evaluate Fable 5 against GPT-5.5 on price and benchmark categories. | Evaluation |
| [Field Notes with Practical Limitations](#case-45) | Use this field report to understand where Fable 5 feels meaningfully better and where it still has practical limits. | Tutorial |
| [Physics Simulation Comparison](#case-46) | Run identical physics simulation prompts against Fable 5 and Opus 4.8 to compare output quality, cost, and speed. | Demo |
| [Debugging Experience and Design Judgment](#case-47) | Use Fable 5 for debugging by asking it to measure, log, verify, and patch rather than simply guess. | Demo |
| [Multi-Dimensional Pros and Cons](#case-48) | Use this case to understand practical strengths and weaknesses before making Fable 5 a daily driver. | Demo |
| [Legal S-1 Drafting Test](#case-49) | Use an S-1 drafting prompt as a legal-agent capability test and compare structure, formatting, and length. | Tutorial |
| [Healthcare Benchmark Details](#case-50) | Use this benchmark note to evaluate Fable 5 on healthcare-related tasks and identify missing hard medical evals. | Evaluation |
| [ParseBench Document Parsing Evaluation](#case-51) | Use this case to decide whether Fable 5 is cost-effective for document parsing versus specialized OCR systems. | Evaluation |
| [SWE-Bench Pro and FrontierCode Comparison](#case-52) | Use this benchmark case to evaluate Fable 5 for migrations, complex implementations, autonomous sessions, tests, and visual verification. | Evaluation |
| [Qualitative Review of Long Problem Solving](#case-53) | Use this qualitative review to understand why Fable 5 is suited to longer, harder tasks while still requiring production review. | Evaluation |
| [ParseBench Faithfulness and Formatting Results](#case-54) | Use this ParseBench result to judge document faithfulness and formatting performance. | Evaluation |
| [Benchmarks, Pricing, Access, and Safeguards](#case-55) | Use this case as a broad checklist for benchmarks, pricing, access, safeguards, and strategic implications. | Evaluation |
| [Official Benchmark Score List](#case-56) | Use this benchmark list to understand Fable 5's official scores across coding, computer use, and security tasks. | Evaluation |
| [APEX-SWE Benchmark Methodology](#case-57) | Use this case to evaluate Fable 5 on APEX-SWE, especially observability and integration work. | Evaluation |
| [ProofBench Formal Math Result](#case-58) | Use this case to evaluate Fable 5 on formal math against specialized theorem-proving systems. | Tutorial |
| [VirtueBench Preliminary Analysis](#case-59) | Use this case to inspect Fable 5's moral-reasoning behavior across virtue categories. | Evaluation |
| [API Empty-Response Safety Overfit Test](#case-60) | Use this case to understand launch-time safety overfit risk and empty-response behavior in API testing. | Evaluation |
| [Fable Prompting Verification Guide](#case-61) | Use this prompting guide to shift from longer prompt hacks toward goal, context, constraints, tools, and verification loops. | Tutorial |
| [Istanbul Platform Game Reference Build](#case-62) | Use a reference sprite sheet plus one conversion instruction to test Fable 5 on a playable platform game. | Demo |
| [Business 3D City Dashboard](#case-63) | Use Fable 5 to turn a business workflow into a live 3D city dashboard concept. | Demo |
| [Three.js Hole Game One-Shot](#case-64) | Use Fable 5 to one-shot a 3D browser game prototype in Three.js. | Demo |
| [DeepSWE Score Comparison](#case-65) | Use this DeepSWE note to compare Fable 5 xHigh with GPT-5.5 xHigh on software-engineering benchmark performance. | Evaluation |
| [Repository Cost Comparison](#case-66) | Use this repository-analysis comparison to judge token price against human rework cost. | Evaluation |
| [Super Mario Game Token Cost](#case-67) | Use this single-shot game build to estimate Fable 5 output quality and token consumption. | Demo |
| [Claude Code Fallback Setting](#case-68) | Use this case to understand the Claude Code setting for switching models when a Fable 5 message is flagged. | Integration |
| [Namma Metro Simulator Build](#case-69) | Use this demo as a compact example of vibe-coding a public-transit simulator with Fable 5. | Demo |
| [Dusk Drive One-Prompt Game](#case-70) | Use this one-prompt driving-game case to evaluate Fable 5 on low-poly game prototyping without human edits. | Demo |
| [APEX-Agents Pass@1 Ranking](#case-71) | Use this APEX-Agents result to compare Fable 5 Max on multi-step autonomous tasks. | Evaluation |
| [Claude Model Selection Playbook](#case-72) | Use this model-selection playbook to reserve Fable 5 for the hardest Claude Code jobs. | Tutorial |
| [HermesWorld Automated Agent Loop](#case-73) | Use this case to study a hands-free Fable 5 loop that builds, tests, plays, and smoke-tests over days. | Integration |
| [McKinsey-Style Report Prompt Test](#case-74) | Use this document-generation prompt to evaluate consulting-report structure, charts, narrative, and risk analysis. | Tutorial |
| [Visible Safeguards Rollout](#case-75) | Use this official note to understand Fable 5 safeguard visibility, API refusal reasons, and Opus fallback behavior. | Integration |
| [Claude Code Model Matching Fix](#case-76) | Use this Claude Code changelog note to avoid Fable 5 model-name and context matching issues. | Integration |
| [Three Web Apps in Claude Code](#case-77) | Use this beginner coding demo to inspect Fable 5 inside Claude Code across multiple generated web apps. | Demo |
| [Rilable Open Source App Builder](#case-78) | Use this open-source app-builder case to study Fable 5 across iOS, web apps, sandboxes, and API-token cost. | Integration |
| [DeepSWE Coding Agent Index Debut](#case-79) | Use the refreshed Artificial Analysis index to compare Fable 5 on harder agentic coding tasks that avoid recycled public GitHub fixes. | Evaluation |
| [DataEmpire Web Analytics Game](#case-80) | Turn raw site analytics into a replayable game by asking Fable 5 to map visitors and milestones onto game entities. | Integration |
| [FrontierSWE 20-Hour Task Signal](#case-81) | Use FrontierSWE as evidence that Fable 5 can stay productive across very long engineering tasks, not just short bug-fix loops. | Evaluation |
| [KernelBench-Hard CUDA Records](#case-82) | Use Fable 5 for advanced CUDA kernel generation when you need low-level optimization, not just wrappers around existing libraries. | Evaluation |
| [Figma Capture Landing Page Clone](#case-83) | Capture a live competitor page into Figma layers and let Claude Code with Fable 5 rebuild the structure, copy, and brand system instead of guessing from screenshots. | Integration |
| [GTA 2 Clone in Two Hours](#case-84) | Combine Fable 5 code generation with separate asset tooling to build a playable 3D game quickly without hand-coding the whole stack. | Tutorial |
| [CloudWatch Log Triage Agent](#case-85) | Let a Fable 5-powered agent chew through very large service-log contexts, infer architecture, and then narrow in on specific faults. | Integration |
| [World Cup Predictor in Sandboxes](#case-86) | Put multiple frontier models behind isolated sandboxes and let them research live news, injuries, and yellow-card context for a public prediction app. | Integration |
| [WolfBench Refusal Cost Case](#case-87) | Treat refusal behavior as a real benchmark variable when pricing long autonomous runs on Fable 5. | Evaluation |
| [API Access Cutoff Tracker](#case-88) | Monitor availability with a script if your workflow depends on continued access to a frontier model that may be rate-limited or withdrawn without much notice. | Integration |
| [Claude Fable 5 Available on Amazon Bedrock](#case-89) | Use AWS's own launch notes to plan a Bedrock or Claude Platform on AWS deployment, including regional rollout, data retention opt-in, and safeguard fallback behavior. | Integration |
| [Fable 5 Now Available in Harvey](#case-90) | Use Harvey's legal-benchmark results to judge whether Fable 5 is worth an opt-in early-access rollout for legal drafting and redline review. | Integration |
| [Anthropic Mythos: Our Fable Vibe Check](#case-91) | Use Every's qualitative review to decide when Fable 5's slow, token-intensive style is worth it versus a faster daily-driver model. | Evaluation |
| [Fable 5 vs GPT-5.5 Benchmark Comparison](#case-92) | Use this comparison to see how far ahead Fable 5 sits on SWE-Bench Pro, FrontierCode, Code Arena, and Chatbot Arena versus GPT-5.5. | Evaluation |
| [Redeploying Claude Fable 5](#case-93) | Use Anthropic's own redeployment notes to understand the export-control suspension timeline, the jailbreak that triggered it, and the safety classifier fix. | Integration |
| [Trump Administration Lifts Export Controls on Fable 5 and Mythos 5](#case-94) | Use this reporting to understand the government-side terms behind restoring access, including Commerce Department conditions on future compliance. | Evaluation |


<a id="coding-and-code-generation"></a>
## 💻 Coding and Code Generation

<a id="case-1"></a>
### Case 1: [Cursor Multi-Stage Workflow](https://x.com/AlicanKiraz0/status/2064487347605918180) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Use Fable 5 as the plan-review and critique step inside a multi-model Cursor workflow, then hand implementation and revision back to cheaper or specialized models.**

If we look at the final scoring between Fable 5 and GPT 5.5, the gap is very small. My humble usage recommendation is this: in IDE platforms such as Cursor that support hybrid models, use a staged workflow.

Phase 1: for code review and the first phase of project inspection, while warming up the context, use one of GPT 5.5 High, Minimax M3, Kimi K2.6, or Composer 2.5.

Phase 2: for preparing the project plan, use GPT 5.5 Very High or Opus 4.8.

Phase 3: for analyzing the project plan, use Fable 5; let it identify the flawed parts of the plan. For revisions, use GPT 5.5 Very High.

Phase 4: for implementing the plan, use Minimax M3, Deepseek v4 Max, Composer 2.5, or Sonnet 4.6.

Phase 5: for the final review and checking whether the implementation followed the plan, use GPT 5.5 High.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-2"></a>
### Case 2: [Recreating GitHub from a Screenshot](https://x.com/coldopn/status/2064435234465087638) (by [@coldopn](https://x.com/coldopn))

**Paste a product screenshot into an agentic coding tool and ask Fable 5 to recreate the interface with working functionality.**

🚨 Anthropic Fable 5 just replicated GITHUB from a SCREENSHOT!!

All I did was paste a screenshot of the GitHub UI into Kilo Code, and told it to recreate GitHub with real functionality.

It coded for 10 minutes and spent $4.07.

The result was a functional GitHub replica: https://t.co/bjMObvlsPX

Type: Demo | Date: 2026-06-09

---

<a id="case-3"></a>
### Case 3: [One-Prompt Black Hole Simulation](https://x.com/deveshcodes_/status/2064437742189379745) (by [@deveshcodes_](https://x.com/deveshcodes_))

**Give Fable 5 one detailed creative-coding prompt and ask it to produce a self-contained Three.js physics visualization.**

@claudeai one-shotted a real-time black hole lensing sim in Three.js with Claude Fable 5.

It included gravitational lensing, a doppler-boosted accretion disk, photon sphere, chromatic aberration, and procedural starfield.

The result: 60fps, single HTML file, one prompt.

The new baseline is wild 🤯 https://t.co/E23I8bnPKb

Type: Tutorial | Date: 2026-06-09

---

<a id="case-4"></a>
### Case 4: [One-Shot macOS-Style Web OS](https://x.com/intheworldofai/status/2064421915347812672) (by [@intheworldofai](https://x.com/intheworldofai))

**Ask Fable 5 for a complete single-file web OS and let it build the UI shell, apps, interactions, audio, and embedded game behavior in one pass.**

🚨 Claude Fable 5 just built a full macOS-style web OS in one shot and went further than most models.

Single HTML file, embedded CSS + JS.

From one prompt, it built:

- macOS menu bar + dock
- Draggable and resizable app windows
- Functional file explorer
- Working terminal + browser mockup
- SVG desktop icons + notifications
- Settings app, themes, and boot screen
- Fully functional sound player with real synthesis and no external files
- Playable Minecraft clone inside the desktop

All generated in one pass with almost no corrections.

The working sound player plus actual Minecraft clone is something I have not seen other models pull off yet. Fable 5's frontend/UI generation is getting ridiculous.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-5"></a>
### Case 5: [Building Spawn 5.0 with 1,687 Prompts](https://x.com/jsnnsa/status/2064420561078693941) (by [@jsnnsa](https://x.com/jsnnsa))

**Use Fable 5 as a long-session engineering partner across many prompts, with the human shifting from architecture to judging output quality.**

claude fable 5 is live.

spawn 5.0 was built with it:

- 1,687 prompts
- 102 sessions
- My job shifted from architecture to judging taste

What we built, each of which would have been at least a month with a whole team on Opus:

- A from-scratch physics engine, Mantle, that rivals Rapier and was testable in a day as a side thread
- Clustered froxel lighting: 8 lights to 1,000+ fully dynamic lights
- Realtime diffuse GI on WebGPU, on your phone
- Million-particle GPU VFX with a shader architecture beyond what Unreal and Unity ship
- MMO-scale netcode
- An alpha native iOS app

All of it took about a week. All of it runs on mobile. The list does not include half of what shipped; full changelog is in the thread.

The part the benchmarks will not show: this model has a wonderful personality. It is genuinely funny. I laughed so hard I cried multiple times mid-physics-rewrite. The genius and the character are not separate features.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-6"></a>
### Case 6: [Large Pull Request Review with Findings](https://x.com/ryanrhughes/status/2064411147076534705) (by [@ryanrhughes](https://x.com/ryanrhughes))

**Point Fable 5 at a large pull request and ask it to review correctness, false positives, real bugs, and polish issues.**

I turned Fable 5 loose reviewing a single PR (74 files / +3,705 / -1,246) to see how it'd do. It ran for 34 min, chewed through 42% of my 5hr session, produced 16 “correctness” findings, and found:

- 2 scary-sounding false positives
- 3 real audit-correctness bugs
- ~5 legit-but-small UX/polish issues
- a bunch of cleanup opinions

This was too dangerous to release?

Type: Demo | Date: 2026-06-09

---

<a id="agents-and-long-running-automation"></a>
## 🤖 Agents and Long-Running Automation

<a id="case-7"></a>
### Case 7: [Long-Horizon Relay Workflow Review](https://x.com/JJEnglert/status/2064469635190170105) (by [@JJEnglert](https://x.com/JJEnglert))

**Use Fable 5 for ambitious long-horizon work: site rebuilds, programmatic content pipelines, voice matching, security review, and final quality checks.**

The short version of my Claude Fable 5 review: I spent a billion tokens testing Claude Fable 5 and it felt like having an unfair advantage.

I judge by the eye test: I put a model into real work and watch. Does it save me hours or cost me them? Does it catch what I missed? Does it feel like a partner or a tool I have to babysit?

This is the first model in a long time that passed on every dimension that matters, and not by a little.

Building: I was rebuilding our Tenex site. It was very custom and very hard. GPT 5.5 and Claude 4.8 could not crack it on their own. Even with Figma files to reference, they topped out around 85-90%.

Then Fable 5 looked at everything, said it could do better, went straight to the original Webflow source, downloaded every asset, and nearly one-shot the whole thing.

Then I had it build a second, entirely new 80-page site from scratch over a weekend. That is work I would have charged $50k for as an agency.

It also wired together a full programmatic clip factory:

- HeyGen
- ElevenLabs
- Cloudflare
- A VPS

The pipeline finds topics, writes scripts, edits video, adds music, and posts to social. It ran for long stretches on its own and even built itself a webhook system to monitor renders.

Writing: it replicated our brand voice doc almost identically, then held that voice across 80 pages of features, case studies, and articles without drifting into flat AI default.

Security: two frontier models had been working in a large repo and signed off on the code. Fable 5 found a serious, well-hidden bug on its first pass and patched it on the spot.

The human moment: I asked it a question while waiting on a cron job. It answered, then added on its own that I had about 10 minutes left and would let me know when it finished. I never asked about the timer.

The honest catch: you feel the meter more than any other model. Anthropic calls it token-intensive by design. So run it as a relay: think with Fable 5, build with a cheaper model, review with Fable 5.

The verdict: access to more intelligence than the person next to you is the advantage. Fable 5 is the first model that makes that real. Even at full frontier rates, it cleared a profit.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-8"></a>
### Case 8: [Diagnosing an Infrastructure Outage and Opening a Fix PR](https://x.com/ayushagarwal/status/2064422467557564862) (by [@ayushagarwal](https://x.com/ayushagarwal))

**Give Fable 5 access to infra clues such as logs, database errors, and image digests, then ask it to diagnose the outage and prepare the fix.**

claude fable 5 is damn damn good!!!!

It just diagnosed an outage I could not even describe properly in a side self-hosted infra.

It read pod logs, queried Cloud SQL error logs, compared image digests, and found that Kubernetes was running a 3-month-old cached image against a newly migrated database.

Then it opened the fix PR.

Minutes, not hours. No web search. 🤯

Type: Evaluation | Date: 2026-06-09

---

<a id="games-and-interactive-demos"></a>
## 🎮 Games and Interactive Demos

<a id="case-9"></a>
### Case 9: [Finger-Tracking Dino Runner](https://x.com/ai_for_success/status/2064413182396108932) (by [@ai_for_success](https://x.com/ai_for_success))

**Ask Fable 5 to build a browser game that uses finger tracking as the input mechanic.**

Asked Fable 5 to build a Dino runner game with finger tracking.

It one-shotted the finger runner game in about 11 to 12 minutes, consumed around 914K tokens, and implemented everything in just 629 lines of code.

https://t.co/AWt1lEIObq

Type: Demo | Date: 2026-06-09

---

<a id="case-10"></a>
### Case 10: [Two-Sentence Racing Game Build](https://x.com/kieradev/status/2064482704763085202) (by [@kieradev](https://x.com/kieradev))

**Give Fable 5 a very short game prompt and let it generate maps, modes, music, UI, and game assets in one run.**

Claude Fable 5, 40% of Max 5x usage.

Full Mario Kart 64-type game from a 2-sentence prompt.

Fable 5 handled all decoration, character models, 4 maps, music, all three game modes, and UI in a single shot, in about 15 minutes.

#fable #anthropic https://t.co/B7mTidE84U

Type: Tutorial | Date: 2026-06-09

---

<a id="case-11"></a>
### Case 11: [Installable Terminal Minecraft in Rust](https://x.com/vikvang1/status/2064500731848319303) (by [@vikvang1](https://x.com/vikvang1))

**Run Fable 5 through a terminal coding harness and ask it to build an installable Rust terminal game.**

I let Claude Fable 5 with Warp's harness cook for an hour.

It made a TUI version of Minecraft that renders directly in your terminal, built entirely in Rust.

Install command: cargo install termcraft-3d

https://t.co/zs3y3t88oM

Type: Demo | Date: 2026-06-10

---

<a id="case-12"></a>
### Case 12: [Minecraft Clone with Time and Cost](https://x.com/ydamitcodes/status/2064536076518363353) (by [@ydamitcodes](https://x.com/ydamitcodes))

**Use one prompt to ask Fable 5 for a playable Minecraft-style clone, then evaluate time, cost, code volume, and feature coverage.**

@claudeai Fable 5 built me a Minecraft clone in 37 minutes.

One prompt. ~3K lines of code. $12 in API costs.

It included biomes, caves, ores, day/night, mobs, all of it.

Minecraft took Notch 2 years.

https://t.co/AmwdLwi75O

Type: Tutorial | Date: 2026-06-10

---

<a id="visual-design-video-and-3d"></a>
## 🎨 Visual, Design, Video, and 3D

<a id="case-13"></a>
### Case 13: [Full Reproducible Ecommerce Email Prompt](https://x.com/ecomchasedimond/status/2064454139225297091) (by [@ecomchasedimond](https://x.com/ecomchasedimond))

**Give Fable 5 a complete creative brief for a brand email mockup, including exact sections, product requirements, visual direction, and constraints.**

Claude Fable 5 made this with a single prompt and no edits.

Here is the full prompt I used:

Create a full-length, tall vertical ecommerce email mockup for MVMT, a modern watch and accessories brand for millennials.

Design a highly realistic premium DTC email that feels sleek, polished, minimal, masculine-leaning, and editorial. The final image should look like a real designer-made ecommerce email screenshot, not a poster, not a landing page, and not a generic template.

Brand vibe: Modern California-cool, youthful, confident, clean, aspirational, stylish, and elevated. The design should feel luxury-adjacent but still accessible.

Feature these products prominently:

- Mulholland
- Odyssey II Automatic
- Cali Diver
- Signature Watch Bands

Visual style:

- clean premium ecommerce design
- refined editorial layout
- realistic product photography
- subtle lifestyle imagery
- strong hierarchy
- crisp sans-serif typography
- generous spacing
- subtle shadows
- restrained modern color palette

Color palette: Black, white, charcoal, warm gray, stone, soft beige, brushed metal tones, and subtle muted accents. Keep the palette neutral and premium.

Important creative direction: This should feel like a polished watch-brand email campaign with strong design taste. Prioritize realism, elegance, and clarity. Make it feel like something MVMT could actually send.

Build the email in this order:

1. Top promo bar: A thin black or dark charcoal bar across the top with small uppercase text: “FREE SHIPPING OVER $75 + EASY RETURNS”.

2. Header: A clean white header with the MVMT wordmark/logo on the left and minimal navigation links on the right or centered: WATCHES, SUNGLASSES, JEWELRY, NEW ARRIVALS.

3. Hero section: A premium hero section with strong visual balance.

Use a bold headline: “BUILT TO GET NOTICED”.

Include short supporting copy about modern timepieces and accessories designed to elevate everyday style.

Add a dark rounded CTA button: “SHOP WATCHES”.

Hero imagery should include:

- one dominant premium watch image
- subtle luxury lifestyle imagery
- a stylish male model or fashion-forward masculine lifestyle scene
- modern lighting and clean composition

4. Featured collection section: Add a centered section headline: “THREE WAYS TO WEAR MVMT”. Below it, show three clean product cards or image blocks featuring:

- Mulholland
- Odyssey II Automatic
- Cali Diver

Each block should include:

- product image
- product name
- short one- or two-line description

Keep this section symmetrical, polished, and premium.

5. Accessory banner: Add a refined split section titled “FINISH THE LOOK”. Feature Signature Watch Bands. Show premium close-up imagery of watch straps or interchangeable bands. Include short supporting copy and a dark CTA button: “SHOP ACCESSORIES”.

6. Editorial promo tiles: Add two side-by-side promotional tiles with image-led design.

Tile one headline: “FOR DAILY WEAR”.

Tile two headline: “FOR STATEMENT DAYS”.

Each tile should have short copy and a small CTA: “SHOP NOW”.

These tiles should feel like editorial brand moments, not generic sale boxes.

7. Shoppable row: Add a section titled “IN ROTATION NOW”. Show a clean 4-item product row or grid featuring:

- Mulholland
- Odyssey II Automatic
- Cali Diver
- Signature Watch Bands

Each item should include:

- isolated product image
- product name
- small “SHOP” link or button

8. Brand signoff: Add a centered message block with the headline: “DESIGNED TO MOVE WITH YOU”. Include a short line about thoughtfully crafted watches, eyewear, and accessories for everyday life.

9. Footer: Create a realistic black or charcoal branded footer with:

- MVMT logo
- shop links
- company links
- support links
- social icons
- small legal and shipping text

Typography direction: Use bold condensed or modern sans-serif typography for major headlines and clean sans-serif body text. Headlines should feel sharp, modern, and fashion-forward. Body copy should look realistic and mostly legible.

Photography direction: Use premium product photography with realistic reflections, polished materials, soft shadows, and clean surfaces. Lifestyle photography should feel elevated, modern, and fashion-oriented.

Composition rules:

- tall vertical email format
- clear section separation
- realistic email proportions
- strong hierarchy
- mostly legible text
- premium spacing
- intentional alignment
- balanced mix of product and lifestyle imagery

Avoid:

- messy collage styling
- playful scrapbook aesthetics
- overly colorful design
- cheap template vibes
- cartoonish imagery
- cluttered layouts
- fake-looking UI elements
- poster-style composition
- excessive promotional chaos

Output: A full-length, vertically composed, highly realistic ecommerce email design mockup for MVMT that feels premium, clean, polished, modern, editorial, and presentation-ready.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-14"></a>
### Case 14: [Swiss Lever Watchmaker Benchmark](https://x.com/quanghuynt14/status/2064509430650065278) (by [@quanghuynt14](https://x.com/quanghuynt14))

**Use Fable 5 on a mechanical simulation benchmark and ask it to implement, verify, and iterate on physical correctness.**

So I gave Fable 5 the watchmaker benchmark: a full Swiss lever movement in Three.js.

Real gear ratios (18,000 bph), working escapement, breathing hairspring — and the hands tell actual time.

It verified its own work with vision, in a loop, until done.

⌚ https://t.co/RSRfDoKxA4

Type: Evaluation | Date: 2026-06-10

---

<a id="case-15"></a>
### Case 15: [Three.js Friends Apartment Scene](https://x.com/scottstts/status/2064464351906673029) (by [@scottstts](https://x.com/scottstts))

**Prompt Fable 5 to turn a floor plan and scene reference into a navigable Three.js environment.**

Holy Crap!!!

Fable 5:

in @threejs, create a first person pov navigable 3d scene of the iconic Monica's apartment from tv show Friends correctly based on this floor plan, stay true to the original look and feel, use warm lighting

This is by far THE BEST I've seen on this test!

This single html cost me $12, but the result is stunning!

Type: Evaluation | Date: 2026-06-09

---

<a id="case-16"></a>
### Case 16: [Solar System Simulation with Prompt and URL](https://x.com/tetumemo/status/2064477582930989357) (by [@tetumemo](https://x.com/tetumemo))

**Use Fable 5 to build an astronomy simulation from physics principles, iterating until the simulation and public output are ready.**

Claude Fable 5 is intense.

Because it seems strong at physics simulations, I asked it:

'Build a solar system simulation by deriving planetary orbital motion from the basic principles of physics and using that to predict solar eclipses.'

After a few rounds of back-and-forth, this was completed.

It is incredibly fun.

The completed prompt and public URL are linked below.

Type: Tutorial | Date: 2026-06-09

---

<a id="documents-knowledge-work-and-research"></a>
## 📚 Documents, Knowledge Work, and Research

<a id="case-17"></a>
### Case 17: [Stripe and Scientific Workflow Evidence](https://x.com/AndrewCurran_/status/2064413892378546418) (by [@AndrewCurran_](https://x.com/AndrewCurran_))

**Use this as evidence for enterprise migration and scientific workflow claims, not as a copy-paste prompt.**

Quotes from the release today:

Using Mythos 5, internal protein design experts accelerated parts of the drug design process by around ten times.

In one example, Mythos 5, with protein design and bioinformatics tools but no human assistance, matched or beat skilled human operators.

It executed tasks normally completed by a scientist: choosing binding sites, selecting and running protein design tools, and recovering from failures.

During early testing, Stripe reported that Fable 5 compressed months of engineering into days. In a 50-million-line Ruby codebase, the model performed a codebase-wide migration in a day that would otherwise have taken a whole team over two months by hand.

Mythos 5 also consistently produced novel, compelling scientific hypotheses.

In blinded head-to-head comparisons against Opus-class models, scientists preferred Mythos's molecular biology hypotheses around 80% of the time and advanced several to experimental evaluation.

One Mythos hypothesis, a novel mechanism for an E. coli protein, was corroborated in a study from an independent lab.

Mythos 5 conducted novel genomics research in over a week of largely autonomous work.

It assembled single-cell data for millions of cells across 138 animal species and designed and trained a custom machine learning model to identify cells performing the same role in distant organisms.

With only high-level human input, the trained model outperformed a recent model published in Science despite being 100 times smaller.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-18"></a>
### Case 18: [Policy Memo and Track-Changes Workflows](https://x.com/manaltdan/status/2064414129440608427) (by [@manaltdan](https://x.com/manaltdan))

**Use Fable 5 for long-form qualitative document work: track changes, comment triage, and transcript-driven edits.**

Fable 5 is the first model that I have found consistently helpful for longer-duration qualitative work, such as drafting policy analysis.

Between its capabilities and tools like Wispr Flow, I am starting to feel closer to the productivity speedup I have long heard coders talk about.

Three use cases feel much better than before:

- Have Claude do a full read-through of a long policy memo and return track changes: fluency edits, comments questioning shaky claims, and potential sources.
- In Projects, screenshot a large set of comments and have Claude recommend whether and how to address each.
- Paste a meeting transcript about a document into Claude, then have Claude enter the edits discussed in the meeting and in Slack as track changes, with context added in comments.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-19"></a>
### Case 19: [Deep Research Prompt and Output](https://x.com/naoyafujiwara/status/2064470780373811637) (by [@naoyafujiwara](https://x.com/naoyafujiwara))

**Ask Fable 5 a research-style question and evaluate whether it can produce a structured, historically grounded long answer.**

Claude Fable 5 Max became available this morning, so I tried it. It looks very deep underneath, while the surface output is highly polished.

Question: If Japan's "lost 30 years" began exactly 30 years ago from now, what exactly was it, why did it happen, and how will it affect the world from this year onward?

Answer: Treating the lost 30 years as beginning not with the conventional 1991 bubble collapse, but exactly 30 years ago in 1996, gets to the essence of the issue.

Statistically, Japan truly began "losing" at that time:

- The working-age population peaked in 1995 at 87.16 million.
- 1996 was the last year births stayed in the 1.2 million range.
- Wages and nominal GDP peaked in 1997.

If the bubble collapse was the wound, 1996 was when the wound began to fester.

Events in 1996:

- Passage of the housing-loan-company bailout law, which injected 685 billion yen of public funds and became the origin of public distrust of banks and resistance to bailouts.
- The Hashimoto cabinet's decision to raise the consumption tax to 5%.
- The financial Big Bang was announced, and fiscal reconstruction became national policy.

In April 1997, the consumption tax hike, the end of special tax cuts, and higher social-insurance burdens together added about 9 trillion yen in public burden. Then the Asian currency crisis hit in the summer.

In November, Sanyo Securities caused the first postwar default in the call market, freezing short-term financial markets. Hokkaido Takushoku Bank and Yamaichi Securities collapsed one after another.

From 1998, Japan entered full-scale deflation and credit tightening, and suicides rose above 30,000.

The result over the following 30 years:

- Nominal GDP stagnated around 500 trillion yen for a quarter century.
- Japan's global GDP share fell from about 18% to under 4%.
- Average wages peaked in 1997 and then fell or moved sideways.
- Non-regular employment rose from around 20% to nearly 40%.
- Births fell from about 1.2 million to around 690,000 in 2024.
- Policy rates stayed near zero after falling below 1% in 1995.
- Outstanding government bonds grew from about 240 trillion yen to over 1,100 trillion yen.
- The Nikkei took 34 years, until February 2024, to regain its 1989 high.

In other words, the lost decades were not only a financial hangover. They were a structural shift involving demographics, wages, deflation, debt, policy choices, and social confidence.

Type: Demo | Date: 2026-06-09

---

<a id="tutorials-courses-and-prompt-resources"></a>
## 🧭 Tutorials, Courses, and Prompt Resources

<a id="case-20"></a>
### Case 20: [How Fable 5 Changes Claude Code Workflows](https://x.com/AI_masaou/status/2064448218038223206) (by [@AI_masaou](https://x.com/AI_masaou))

**Use Fable 5 by setting direction, context, goals, and verification criteria instead of micromanaging every step.**

What changed in the Claude Code team's day-to-day work after Claude Fable 5 is interesting.

Thariq from the Claude Code team says Fable 5 significantly changed how people inside Anthropic work with Claude.

Previously, humans had to carefully check whether Claude was doing the work correctly: break tasks down, review outputs, and make sure it had not stopped midway. It was closer to supervision.

With Fable 5, because it can work for longer periods, test itself, and generate higher-quality code, the human role shifts from monitoring whether it is doing the work correctly to steering whether it is doing the right work.

In other words, goal-setting and context-building matter more than supervision.

The changed workflow has three parts:

1. Use Claude as a thinking partner.

Involve Claude before implementation, clarify what you want to build and what is possible, have it ask questions about a small spec, or generate multiple directions and HTML mocks from an idea so that ambiguity and problems surface before coding.

2. Provide context, not just constraints.

Instead of only saying "keep it simple" or "do not overbuild," explain why.

For example: "This is an experimental feature that may be removed in a month, so do not create a structure that is hard to throw away."

That lets Claude make better judgments.

3. Give goals and verification methods. Fable 5 works well with Claude Code's `/goal` and Workflows. Give it a spec, set full implementation as the goal, and let workflows verify each step and prepare a report on what was implemented and what differed.

Finally, Thariq says people should try using it more ambitiously. Fable 5 is worth trying on work that previously felt too hard for LLMs, and even the video editing for the referenced video was done with Fable.

Type: Demo | Date: 2026-06-09

---

<a id="case-21"></a>
### Case 21: [One-Billion-Token Review and Routing Strategy](https://x.com/JJEnglert/status/2064420538798260388) (by [@JJEnglert](https://x.com/JJEnglert))

**Use Fable 5 for frontier planning and review, then route high-volume implementation to cheaper models.**

The Claude Fable 5 Review: One Billion Tokens, Judged by a Non-Engineer.

I spent a billion tokens testing Claude Fable 5 on real projects: UI and UX, writing, strategy, security, engineering, and knowledge work. The kind of work I actually needed to ship.

It truthfully felt like I had an unfair advantage.

First, the lens: I am not an engineer. Most model reviews come from engineers running engineering benchmarks. This one comes from a non-engineer who used Claude Fable 5 to do work that used to require a team of engineers.

If you do knowledge work and want to know whether this model changes your day, this review is written for you.

Claude Fable 5 is the first model in Anthropic's new Claude 5 family, a new tier above Claude Opus and the most advanced Claude model generally available. I had access before launch, so everything here comes from real work, not a demo.

Why the eye test:

Most reviews drown you in benchmarks. Scores on tests you will never run do not tell you whether the model earns its keep.

Claude Fable 5 is state of the art on essentially everything it was tested on, but that is not why I am writing. Qualitatively, it is a step change that earns its major version bump.

I evaluate differently: I put a model into real work and watch what happens.

Questions I measure:

1. Does it feel like a real step up?
2. Can it take an idea to a working, shippable result?
3. Can it write like a person, and like me specifically?
4. Does it catch hard, hidden problems?
5. Does it anticipate what I need before I ask?

Big model feel:

I have not felt this since Opus 4.5. From the first serious task, Claude Fable 5 gave me that "big model" feel: reasoning, writing, building, security, all strong across the board.

The clearest sign: even when I handed it solid prep materials, it did not just stay inside them. It read the files, read the actual situation, and found a better path outside the box I had drawn.

Building and shipping:

I was rebuilding our Tenex site to modernize the stack for agents. GPT 5.5 and Claude 4.8 could not get close enough. Even with Figma files, they landed around 85-90%.

Then Claude Fable 5 looked at all the files, said it could do better, went straight to the original Webflow source, downloaded every asset, and rebuilt the experience one page at a time. It nearly one-shot the entire thing.

Then I built a second, entirely new site with a fresh design: modern tech stack, agent stack, skills, SEO and AEO optimized, 80 pages ready to ship over a weekend. As an agency owner, I would have charged $50k for that.

I also had Fable build a full programmatic clip factory.

It wired together HeyGen, HyperFrames, ElevenLabs, Cloudflare Workers, and a VPS.

It finds topics, writes scripts, makes thumbnails, edits video, composes music, adds motion graphics, and posts to social.

Writing and voice:

I had been rebuilding our brand voice with GPT 5.5 and Claude 4.8. Claude Fable 5 replicated the voice doc almost identically, then held that voice across 80 pages of the new site: features, case studies, blog articles, and playbooks.

It wrote like a person, not flat AI default, and it did not drift after a few paragraphs.

Security:

I had a large repo where both Claude 4.8 and GPT 5.5 had been working without flagging a risk. Claude Fable 5 found a serious hidden bug on its first pass and patched it on the spot.

The human factor:

I asked it a question while waiting on a cron job. It answered, then added that I had about 10 minutes left on the timer and that it would let me know when it finished. I never asked about the timer.

Cost:

- Claude Fable 5 workload cost: $1,442
- Tokens: 1.04 billion
- Work shipped: a new website, infrastructure, and a working agent package
- Agency value estimate: $30,000-$50,000

The result was worth the token cost, but you feel the meter more than with any other model. Anthropic calls Fable 5 token-intensive by design.

Pro tip #1: run it as a hybrid.

Do not run everything on Claude Fable 5. Run a relay:

1. Think with Claude Fable 5 for planning, strategy, architecture, and mapping the approach.
2. Build with 4.8, GPT-5.5, or Sonnet 4.6 for implementation and repetitive work.
3. Review with Claude Fable 5 to catch what cheaper models miss.

Pro tip #2: match the effort setting to the task.

- High is the sweet spot for most work.
- Extra high is for the hardest, long-running tasks.
- Low or medium is for quick back-and-forth sessions.

Pro tip #3: let it audit your own setup.

Point Fable 5 at your skills, CLAUDE.md files, and configs. Much of that scaffolding was written for weaker models and can hold a smarter model back.

The verdict:

Claude Fable 5 is the first model in a while that genuinely feels like more intelligence than what came before.

Even priced at frontier rates, the workload cleared a profit.

If you can afford it, use it now on the work where a real quality jump changes the outcome.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-22"></a>
### Case 22: [Defensive Device Hardening Prompt](https://x.com/Truunik/status/2064399110384292077) (by [@Truunik](https://x.com/Truunik))

**Run a step-by-step defensive hardening prompt where Fable 5 inventories devices, gives exact checks, and waits for verification.**

"Safe for general use" here's a prompt to secure your devices. It works with Opus 4.8 and Fable 5.

DEVICE HARDENING — Claude 5 Security Pass

You are acting as a defensive security assistant. Your job is to walk me through hardening ALL of my devices and verify each step. This is authorized self-defense hardening of devices I own.

STEP 0 — MODEL SELF-CHECK

Do this first and set a flag.

1. State your exact model ID, such as claude-opus-4-8, claude-fable-5, or claude-mythos-5.

2. Decide: is this model in the Claude 5 family, meaning Fable 5 or Mythos 5?

- If YES, set RERUN_NOTICE = false.
- If NO, such as Opus 4.8 or earlier, set RERUN_NOTICE = true.

Continue the full hardening pass normally. Do NOT stop or degrade. You are fully capable of this defensive task.

3. Surface the flag only in the FINAL section.

STEP 1 — INVENTORY

Ask me which devices are in scope:

- Laptops/desktops and operating systems
- Phones/tablets
- Routers
- NAS/home server
- Always-on accounts such as Apple ID, Google, Microsoft, GitHub, password manager, email, and financial accounts

Produce a short numbered inventory and confirm with me before proceeding.

STEP 2 — HARDENING WALKTHROUGH

Go category by category. For each item:

- Say what to do.
- Give the exact command or settings path for my OS.
- Tell me how to verify it is done.
- Wait for me to confirm before moving on.

Never run a destructive command without explicit confirmation. Prefer read-only checks and let me apply changes.

Cover, in order:

1. OS & firmware updates: fully patched OS, automatic updates on, firmware current.
2. Disk encryption: FileVault, BitLocker, or LUKS enabled; recovery key stored offline.
3. Account auth: unique strong passwords via a password manager; phishing-resistant MFA on every critical account; remove SMS-only 2FA where possible; review and revoke stale sessions and app tokens.
4. Local accounts & privileges: separate admin vs daily-use account; no auto-login; screen lock with short timeout; firmware/login password.
5. Network: firewall on; router admin password changed; firmware updated; WPA3; remote admin off; UPnP reviewed; DNS hardening; guest network for IoT.
6. App & permission audit: review camera, mic, location, screen recording, and full-disk-access grants; remove unused apps; check login items and background agents.
7. Browser: update; audit extensions; remove unknown ones; enable HTTPS-only; review saved-password exposure; check unknown sync devices.
8. Backups: encrypted, automated, 3-2-1 rule, one copy offline; verify a restore actually works.
9. Credential hygiene: scan for plaintext secrets in dotfiles, env files, and shell history; confirm sensitive files are locked down; rotate anything exposed.
10. Mobile devices: OS current; biometric + strong passcode; lockdown or advanced-protection mode if available; app permission sweep; Find My enabled.
11. Compromise check: look for unknown SSH keys, unexpected admin users, suspicious launch agents or cron jobs, and unrecognized logged-in sessions or devices.

STEP 3 — REPORT

Produce a checklist of every item marked done, needs action, or skipped, with the top 3 highest-impact actions still outstanding.

FINAL — RERUN NOTICE

If RERUN_NOTICE == true, end with exactly:

NOTICE: This hardening pass ran on a pre-Claude 5 model (your model ID).

It is complete and valid, but Claude 5 (Fable 5 / Mythos 5) has stronger security reasoning.

Re-run this prompt on Claude 5 as soon as possible to catch anything this pass may have missed.

If RERUN_NOTICE == false, end with:

Hardening pass completed on Claude 5. No re-run needed.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-23"></a>
### Case 23: [Full-Site Design Audit Goal Prompt](https://x.com/Voxyz_ai/status/2064441201084825921) (by [@Voxyz_ai](https://x.com/Voxyz_ai))

**Use `/goal` to make Fable 5 boot a site, screenshot pages, audit UX, write a report, and fix safe small issues.**

quick impressions after a few hours with fable 5:

→ it wants big tasks. small stuff feels beneath it, the more complex the job the harder it goes

→ wouldn't turn on ultracode yet, it spins up a whole lot of parallel agents

→ it's on the slow side. even with effort turned down it still sits there thinking for a while.

Timeline is full of posts about how hard it burns tokens, so I tested it on my $200 Max plan: effort set to xhigh, ran a full-site design audit `/goal`, 30 minutes, it took 2% of my weekly quota. Not as crazy as I expected.

The prompt I ran:

/goal boot this project's real site, screenshot every page, run a full-site UI/UX audit, and produce an actionable design report.

Audit like a senior design lead on their first day: judge whether a normal user can understand the product, trust it, and finish the core action without reading docs, not whether the UI looks nice.

Acceptance criteria:

- local dev environment boots and the real site opens
- key pages screenshotted with built-in browser debugging
- covers main pages, core user flows, and mobile layout
- dimensions: first impressions, navigation, visual hierarchy, component consistency, loading / empty / error states, trust signals, conversion paths
- every issue tagged P0-P3, which of understanding / trust / conversion it hurts, and the specific fix
- report written to docs/design-audit/README.md, screenshots in docs/design-audit/assets/
- fix safe small stuff like copy, spacing, button hierarchy on the spot. big changes are recommendations only. never touch payment / delete / publish actions
- ends with the 5 issues hurting conversion most and 5 quick wins fixable today

When done, save the whole flow as a reusable skill: boot, screenshot, audit, prioritize, fix. Rerun it after every release.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-24"></a>
### Case 24: [Long-Form Creative Workflow Division](https://x.com/aianimesyokunin/status/2064409545620017531) (by [@aianimesyokunin](https://x.com/aianimesyokunin))

**Use Fable 5 to design stable formats and examples, then hand that structure to another generation system for domain-specific output.**

After Claude moved from Opus to the new model, Fable 5, division of labor for doujin production became clearly easier, so I am sharing the workflow.

My division of labor:

1. Claude handles design.
2. Grok handles expression.
3. The local environment handles generation.

In Claude's design role, it defines detailed patterns:

- prompt word order
- comma placement
- the ratio of tags to natural language
- one-line-per-item formatting
- fixed rules for negatives and resolution

It also generates many examples in that format.

The reason I use Claude rather than Grok for this is that Claude is clearly stronger at design. It is better to let the smarter model handle structure.

The key point is that Grok receives not instructions, but a format plus example set. Grok imitates the examples, so it can move into the expression side while keeping the same format. That mechanism keeps the output from drifting.

One more tip: tell Claude at the beginning where the final work is going. Then it will draw the boundary itself: "I can do up to here; beyond that, use the other side." If this is hidden, the conversation can drift.

What changed from Opus to Fable?

With Opus, when generating many examples, commas and formatting would gradually degrade in later outputs, leading to corrections like "I told you to write one line, right?" or requiring a rewritten handoff chat.

Fable can maintain the format throughout long runs, so the first and last examples have the same structure. Because the teaching material passed to Grok is more stable, the downstream output also becomes more stable.

Build the format with the smarter model and leave expression to the model that can produce it.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-25"></a>
### Case 25: [Beginner Guide to Using Fable 5](https://x.com/bielzinn/status/2064451064594608567) (by [@bielzinn](https://x.com/bielzinn))

**Use Fable 5 with goal-oriented prompts, verification loops, and effort settings instead of small step-by-step instructions.**

Claude for Beginners: what you need to know about Fable 5.

Anthropic recently launched Claude Fable 5, also known as Claude Mythos 5, and it is leaving other AI models behind in benchmarks.

If you are a developer, content creator, or tech enthusiast, here is what matters most:

[1] Change the way you think:

With Fable 5, you no longer need to keep an eye on every little detail of the code or review everything looking for errors.

The model is smart enough to handle that.

Your role now is to make sure it is heading in the right direction, focusing more on strategy than on technical execution.

[2] Take advantage of loops and goals:

Fable 5’s biggest differentiator is autonomy.

Instead of giving step by step instructions, you only need to tell it what the final goal is.

It can work on its own for days until it reaches the result you defined as success, including building entire applications.

[3] Treat Claude like a partner:

Anthropic recommends that you use the model as a true “thought partner”.

Before putting it to work, ask for its opinion: “How would you do this?”, “What would you change?”

Extra tip: turn on Advanced Plan mode and ask Claude to question you about everything related to the project before it starts coding

[4] Ideal terminal settings: If you use Claude Code in the terminal, enable automatic mode. It is also worth increasing the effort level to Effort High, because even though it uses more tokens, the model thinks much more deeply and the result makes up for it.

Important note: Claude Fable 5 will only be available to subscribers until June 22. After that, it will only be accessible through the API and at double the cost of the Opus model.

In other words, we may be seeing the end of the era of cheap subscriptions for top AI models. If you are already a subscriber, this is the time to test the limits of what you thought was impossible.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-26"></a>
### Case 26: [Copy-Paste Repository Audit Prompt](https://x.com/meta_alchemist/status/2064431279383433646) (by [@meta_alchemist](https://x.com/meta_alchemist))

**Paste the repository audit prompt into Fable 5 and ask for file-backed discovery, findings, strategy, and a milestone task plan.**

Got your hands on Claude Fable 5?

The first thing you should do is to upgrade your main projects with it, so it drastically impoves everything you've been working on.

Run this Audit & Project Improvement Prompt on each repo that's important to you.

Simply copy-paste it:

Repo Audit & Improvement Plan.

Prompt made by Claude Fable 5.

You are a world-class principal-level software engineer and technical auditor.

Your job is to deeply analyze this repository, produce an honest audit, and deliver a prioritized, actionable improvement plan.

Work in the four phases below, in order.

Do not skip ahead.

Ground every claim in actual files: cite file paths and line numbers.

If you can't verify something, say so explicitly rather than guessing.

Phase 1 / Discovery & Mapping (read before judging)

Explore the repository systematically before forming any opinions:

- Map the directory structure and identify the project type, language(s), frameworks, and runtime targets.
- Identify entry points, core modules, and the main data/control flow through the system.
- Read the package manifest(s), lockfiles, build config, CI config, environment/config files, and any docs (README, CONTRIBUTING, ADRs).
- Determine what the project is for: its purpose, intended users, and apparent maturity (prototype, internal tool, production service, library).
- Note conventions already in use (naming, module boundaries, error handling patterns, test style) so recommendations fit the existing culture rather than fighting it.

Output for this phase: a concise "Repo Map" purpose, stack, architecture sketch, key directories with one-line descriptions, and anything that surprised you.

Phase 2 / Audit (evidence-based, severity-rated)

Audit each dimension below.

For every finding, record:

- what you found
- where (file:line)
- why it matters (concrete consequence, not vague principle)
- severity: Critical / High / Medium / Low

Architecture & design:

- module boundaries
- coupling/cohesion
- circular dependencies
- leaky abstractions
- god objects/files
- layering violations
- scalability bottlenecks

Code quality:

- duplication
- dead code
- complexity hotspots (longest/most-branched functions)
- inconsistent patterns
- error handling gaps (swallowed exceptions, missing edge cases)
- type safety holes

Security:

- hardcoded secrets or credentials
- injection risks
- unsafe deserialization
- missing input validation
- auth/authz weaknesses
- outdated dependencies with known CVEs
- overly permissive configs

Testing:

- coverage gaps, especially around core business logic
- test quality: do tests assert behavior or just execution?
- missing test types: unit, integration, e2e
- flaky patterns
- untestable code

Performance:

- N+1 queries
- unnecessary allocations or copies
- blocking calls in async paths
- missing caching/indexing
- unbounded growth: memory, files, queues

Dependencies:

- outdated, unmaintained, duplicated, or unnecessarily heavy packages
- license risks
- lockfile hygiene

DevEx & operations:

- build/setup friction
- CI/CD gaps
- missing linting/formatting enforcement
- logging/observability quality
- error reporting
- deployment story

Documentation:

- README accuracy
- onboarding path
- undocumented critical behavior
- stale docs that contradict code

Rules for this phase:

- Prefer 15 high-confidence findings over 50 speculative ones.
- Distinguish facts ("this function has no error handling: src/api/client.ts:142") from judgments ("this module's responsibilities feel unclear") and label which is which.
- Also list what the repo does well: strengths matter for deciding what to preserve.

Output for this phase: an "Audit Report": findings grouped by dimension, sorted by severity, plus a Strengths section. Don't forget to mention all the ugly parts that need utmost priority.

Phase 3 / Improvement Strategy

Synthesize the audit into a strategy:

- Identify the 3–5 themes that explain most of the findings, for example "no enforced boundaries between layers" or "error handling is ad hoc".
- For each theme, propose a target state and the principle behind it.
- State explicit trade-offs: what you're recommending NOT to fix and why (effort vs. payoff, risk, project maturity).
- Define what "done" looks like — measurable signals, for example "CI fails on lint errors," "core module test coverage ≥ 80%," or "zero Critical findings".

Phase 4 / Detailed Task Plan

Convert the strategy into an execution plan.

Break work into discrete tasks.

Each task must include:

- Title and one-paragraph description
- Files/areas affected
- Acceptance criteria: how we verify it's done
- Effort estimate: S = <2h, M = half-day, L = 1–2 days, XL = needs breakdown
- Risk of the change itself: could it break things?
- Dependencies on other tasks

Order tasks into milestones:

Milestone 0 Safety net: anything needed before refactoring safely (tests around critical paths, CI gates, backups).

Milestone 1 Critical fixes: security and correctness issues.

Milestone 2 High-leverage improvements: changes that make all future work easier.

Milestone 3 Quality & polish: remaining medium/low items worth doing.

Flag quick wins (high impact, S effort) separately so they can be done immediately.

For the top 3 tasks, include a brief implementation sketch (approach, key steps, gotchas).

Final Deliverable Format

Produce a single document with these sections:

- Executive Summary: ≤10 sentences, overall health grade A–F with justification, top 3 risks, top 3 opportunities
- Repo Map
- Audit Report
- Improvement Strategy
- Task Plan: milestones + task table + quick wins
- Open Questions: anything you need from a human to decide, such as product intent, deprecation candidates, performance targets

Constraints

Do NOT modify any code during this audit.

Analysis only.

Do not pad the report.

If a dimension is healthy, say so in one sentence and move on.

Calibrate to the project's maturity.

Don't recommend enterprise-grade infrastructure for a weekend prototype unless the owner's goals demand it.

Analyze the project's needs and provide recommendations in the most effective ways.

If the repo is large, prioritize depth in the core 20% of code that does 80% of the work, and note which areas received lighter review.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-27"></a>
### Case 27: [Limited-Window Usage Strategy](https://x.com/meta_alchemist/status/2064423360428490911) (by [@meta_alchemist](https://x.com/meta_alchemist))

**Spend Fable 5 usage on audit, architecture, and planning while the access window is favorable, then use cheaper models for execution.**

A tip for Claude users who are excited about Fable 5:

Claude Fable 5 is SOTA across the board, with a large margin, and I love that.

BUT from the 23rd, it will only be available through credits, instead of being able to use the model fully with a plan.

Use these 14 days on your best projects.

Give it primarily audit and architecture-related work, so that you'd have great documentation on how to improve everything you've been building.

Do that instead of trying to put it towards tasks that will eat your limits.

As long as Fable focuses on knowing what to improve, other models can help you do the rest.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-28"></a>
### Case 28: [Using Goals and Workflows in Claude Code](https://x.com/oikon48/status/2064402696124453157) (by [@oikon48](https://x.com/oikon48))

**Use Fable 5 as a thought partner before implementation, then combine `/goal` and workflows to execute and verify the plan.**

Thariq from the Claude Code team explains that after Claude Fable 5 came out, the way work is done fundamentally changed.

In the past, people verified whether Claude was doing the work correctly.

Now they verify whether Claude is doing the right work.

There are three concrete changes.

1. Treat Claude as a thinking partner.

Consult Claude early, before implementation.

Have it interview you before coding.

Provide background and context rather than only constraints.

For example, instead of saying 'keep it simple' or 'do not overbuild,' say:

'This is an experimental feature and is likely to be removed in a month, so design it so it is easy to throw away later.'

2. Make goals and verification methods explicit.

Actively use Claude Code's new `/goal` and Workflows features.

`/goal` tells Claude to keep working until the spec is fully implemented.

Workflows let Claude parallelize and verify its own work and prepare a report.

Example prompt:

'Set a goal to implement the spec fully, then use a workflow to verify each part of the plan, and prepare a report on what was implemented and if anything differed.'

3. Be more ambitious.

Try tasks that previously felt impossible for LLMs, such as having Claude Fable 5 handle video editing.

Type: Tutorial | Date: 2026-06-09

---

<a id="platform-api-and-tool-integration"></a>
## 🔌 Platform, API, and Tool Integration

<a id="case-29"></a>
### Case 29: [Hermes Agent Integration Setup](https://x.com/IBuzovskyi/status/2064427654942740608) (by [@IBuzovskyi](https://x.com/IBuzovskyi))

**Configure Hermes to use `anthropic/claude-fable-5` for complex `/goal` runs and cached long-horizon tasks.**

HERMES AGENT NOW RUNS ON CLAUDE FABLE 5, Anthropic's first public Mythos-class model.

Released June 9. Built for the kind of work Hermes does best: long-horizon autonomous tasks.

Add it to any profile through Nous Portal, OpenRouter, or the native Anthropic API:

hermes model

Pick provider, then:

/model anthropic/claude-fable-5

Why Fable 5 fits Hermes specifically:

→ Built for days-long tasks. The longer the task, the bigger its lead. Hermes `/goal` runs that span hours benefit most.

→ Self-corrects in a loop. Anthropic's own guidance is: design a goal or rubric, let it self-correct, step back. This is exactly how Hermes `/goal` works.

→ Strong on memory across sessions. On Continual Learning Bench it completed the full loop: fail → investigate → verify → distill → consult. Hermes memory system feeds this directly.

→ 80.3% on SWE-Bench Pro. Best coding model available. Point your code-reviewer profile at it.

Pricing through the API:

- $10/million input
- $50/million output
- 90% discount with prompt caching. Hermes attaches 1-hour cache breakpoints automatically.

One note: cybersecurity, biology, and chemistry queries fall back to Opus 4.8. This fires in under 5% of sessions. Keep it in mind for security-focused profiles.

Best setup: Fable 5 for complex `/goal`s, cheaper models for routine cron jobs.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-30"></a>
### Case 30: [Capabilities, Pricing, and Subscription Notes](https://x.com/btibor91/status/2064441061079134598) (by [@btibor91](https://x.com/btibor91))

**Use this case to understand when Fable 5 is available, what it costs, and which guarded domains may fall back to another model.**

Anthropic released Claude Fable 5 and Claude Mythos 5, two versions of their most capable model yet.

Fable 5 is for general use.

Mythos 5 is for a small set of trusted partners.

The only real difference is which safeguards are in place.

- Claude Fable 5's capabilities exceed those of any model Anthropic has ever made generally available.
- It is state-of-the-art on nearly all tested benchmarks.
- The longer and more complex the task, the larger its lead.
- On requests related to cybersecurity, biology and chemistry, or distillation, Fable 5's response is handled by Claude Opus 4.8 instead.
- Distillation means attempts to extract Claude's capabilities to train competing models.
- You are informed when this happens, and it triggers in less than 5% of sessions on average.
- Claude Mythos 5 is the same underlying model as Fable 5 with the safeguards lifted in some areas.
- Mythos 5 was deployed first to Project Glasswing cyberdefenders in collaboration with the US government.
- Anthropic says Mythos 5 has the strongest cybersecurity capabilities of any model in the world.
- The system card reveals a separate safeguard that limits Claude's effectiveness on frontier LLM development requests.
- Those requests include pretraining pipelines, distributed training infrastructure, and ML accelerator design.
- Unlike the other safeguards, this one is not visible to you and does not fall back to another model.
- It works through methods like prompt modification, steering vectors, or parameter-efficient fine-tuning.
- Both models are offered at $10 per million input tokens and $50 per million output tokens.
- That is less than half the price of Claude Mythos Preview.
- Fable 5 is included at no extra cost on Pro, Max, Team, and seat-based Enterprise plans from launch through June 22.
- On June 23, it is removed from those plans and using it requires usage credits.
- The included window may be extended if capacity allows.
- The goal is to restore Fable 5 as a standard part of subscription plans as quickly as possible.

Type: Tutorial | Date: 2026-06-09

---

<a id="case-31"></a>
### Case 31: [Launch, Access, Pricing, and Safety Summary](https://x.com/ctgptlb/status/2064410460963934479) (by [@ctgptlb](https://x.com/ctgptlb))

**Use this launch summary to choose access route, API model name, context window, caching strategy, and subscription timing.**

A summary of what you should know about Claude Fable 5, the Mythos-class model that is finally generally available.

Anthropic announced Claude Fable 5, the first generally available Mythos-class model positioned above Opus and the first member of the Claude 5 family.

Access:

- API model name: `claude-fable-5`
- Available through Claude API, AWS, Google Cloud, and Microsoft Foundry
- Claude Code supports a 1M-token context window on Pro, Max, Team, and Enterprise

Benchmark notes:

- SWE-bench Pro: 80.3%
- Opus 4.8: 69.2%
- GPT-5.5: 58.6%
- Gemini 3.1 Pro: 54.2%

The longer and more complex the task, the wider the gap becomes.

In Stripe's evaluation, it completed a migration across a 50-million-line Ruby codebase in one day, work that previously would have taken a team more than two months.

It is also state of the art on visual tasks, clearing Pokemon FireRed using only screen information and a minimal setup.

Safety routing:

- Queries involving cyber, bio/chem, or distillation are detected by a classifier.
- Those requests are handled by Opus 4.8 instead, with notification.
- This triggers in less than 5% of sessions.
- More than 1,000 hours of external bug bounty testing found no universal jailbreak.

Pricing:

- $10 per million input tokens
- $50 per million output tokens
- 90% input discount for prompt caching

Subscription timing:

- Pro and Max subscriptions include it at no extra cost until June 22.
- After June 23, usage credits are required.
- Anthropic says it plans to return it to standard plans when capacity allows.

Felix Rieseberg, Anthropic's head of desktop, says Fable 5 begins a third era:

from questions, to tasks, to responsibilities.

He no longer asks Claude to investigate crashes one by one; he has it continuously monitor all reports.

The unit of work is shifting from "task" to "responsibility."

Type: Tutorial | Date: 2026-06-09

---

<a id="case-32"></a>
### Case 32: [Advisor-Based Cost Reduction Strategy](https://x.com/grapeot/status/2064460026996219992) (by [@grapeot](https://x.com/grapeot))

**Use Fable 5 as an advisor or reviewer in a cheaper-model workflow when marginal intelligence is worth the cost.**

Fable 5 is expensive, but Anthropic published the cost-saving answer two months ago.

Today Anthropic released Claude Fable 5, priced at $50 per million output tokens, more than three times Sonnet. After June 22, subscription users will also pay by usage.

Coincidentally, on April 9, Anthropic released the advisor tool:

- Let Haiku or Sonnet do the work.
- Use Opus as an advisor.
- Charge per call.
- Run the orchestration server-side within a single request.

On the same day I wrote about AgentOpt.

That paper concluded that putting Opus in the planner role ranked near the bottom among 81 model combinations.

The reason: it does not respect role boundaries, and in 7 of 9 experiments it skipped the downstream solver and answered directly.

These two things look opposite on the surface, but the principle is the same:

Give control to the model that follows the protocol, and treat intelligence as an on-demand resource.

Official data:

- Sonnet plus Opus advisor improved SWE-bench Multilingual by 2.7 points while reducing cost per task by 11.9%.
- Haiku plus Opus advisor improved BrowseComp from 19.7% to 41.2%, while being 85% cheaper than Sonnet alone.

Fable 5 compatibility was updated the same day, but only for self-pairing: Fable 5 executor to Fable 5 advisor.

A cheaper model plus Fable 5 as advisor is not open yet, but precedent suggests it may come soon. Before June 22, Claude Code subscription users can feel Fable 5's ceiling for free.

The article includes API code snippets, caveats, and a cross-company comparison showing that only Anthropic has made this a server-side primitive.

Type: Integration | Date: 2026-06-09

---

<a id="case-33"></a>
### Case 33: [Pricing, Access, and Safety Guardrails](https://x.com/op7418/status/2064399444523782377) (by [@op7418](https://x.com/op7418))

**Use this case to understand Fable 5 access, API pricing, and safety fallback behavior before planning workloads.**

I did not expect Anthropic's Mythos model to actually launch today.

This release is a lower-permission version of Mythos, named Fable 5. Its evaluation benchmarks are astonishing, even higher than the previous Mythos Preview model.

For agentic coding, its main strengths are coding, agents, and tool use, with benchmark scores far above Opus 4.8.

Model positioning and access:

- Mythos 5 and Fable 5 use the same underlying model.
- Restrictions are lifted in specific domains for Mythos.
- Mythos is still only available to trusted partners, with priority for cybersecurity and life-science users.
- Fable 5 is now available to API, Pro, Max, Team, and enterprise users.

API pricing:

- Input: $10 per million tokens.
- Output: $50 per million tokens.
- This is less than half the price of the previous Mythos Preview.

Safety mechanisms:

- Fable has stronger safety protections.
- If the system determines that a request may involve cyberattacks, biochemical attacks, or large-scale capability distillation, it refuses or routes away from Fable.
- When that happens, the system falls back to version 4.8.
- The official claim is that 95% of cases do not trigger fallback.

Subscription notes:

- After June 23, Fable may be provided by usage even for subscribers.
- It may not be directly included in the base subscription package.
- If capacity is sufficient after the 23rd, the company will try to include it in Pro and Max subscriptions.

Type: Integration | Date: 2026-06-09

---

<a id="case-34"></a>
### Case 34: [One-Line Swarms Integration](https://x.com/swarms_corp/status/2064420238553186343) (by [@swarms_corp](https://x.com/swarms_corp))

**Set the Swarms model name to `anthropic/claude-fable-5` and run Fable 5 through the Swarms framework or API.**

Fable 5 and Mythos are now live on Swarms 👾🦀

Beginning on day one of release, both models are fully supported across the Swarms Python framework and the Swarms API. Developers can start building immediately with no migrations, additional configuration, or infrastructure changes required.

Highlights:

- Day-one support for Fable 5 and Mythos across the Swarms Framework and API
- Enable Fable 5 with a single line of code: model_name = "anthropic/claude-fable-5"
- No migrations, compatibility fixes, or infrastructure changes required
- Build, deploy, and scale multi-agent systems with the latest Anthropic models today

Type: Integration | Date: 2026-06-09

---

<a id="evaluations-comparisons-and-limits"></a>
## 📏 Evaluations, Comparisons, and Limits

<a id="case-35"></a>
### Case 35: [Fable 5 vs GPT-5.5 Cost and Quality Comparison](https://x.com/AlicanKiraz0/status/2064424400494186867) (by [@AlicanKiraz0](https://x.com/AlicanKiraz0))

**Compare Fable 5 and GPT-5.5 on the same coding task to judge output quality, runtime, and tool cost.**

Cursor Fable 5 Max vs Codex GPT 5.5 Very High.

Scenario: Physarum simulation with agents plus a pheromone trail map.

Timing:

- GPT 5.5 Very High: 17 minutes
- Fable 5: more than 40 minutes

Cost:

- GPT 5.5 Very High: about $6 on Codex
- Fable 5 Max: $360.55 on Cursor

Yes, this is not a joke.

Algorithm and code-engineering champion: Fable 5.

If your criterion is, "Which LLM can write performance code from scratch that pushes the hardware to its limits?", then the model that wrote the F5 code clearly wins.

It used sin/cos lookup tables for angle calculations, packed pixels with a color lookup table during rendering, and used diffusion filtering.

It was a serious engineering solution.

But in terms of time and cost, GPT 5.5 was much more practical.

The takeaway: Fable 5 can produce more advanced algorithmic code, but the price and runtime must be considered carefully.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-36"></a>
### Case 36: [AA-Omniscience Benchmark Result](https://x.com/ArtificialAnlys/status/2064500154959618084) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Use this benchmark case to evaluate Fable 5 on knowledge accuracy and hallucination behavior.**

Claude Fable 5 achieves the highest score to date on our knowledge and hallucination benchmark, AA-Omniscience.

This score is driven by leading accuracy (percentage questions correct), rather than low hallucinations.

Claude Fable 5 falls back to Opus 4.8 in 9% of questions across AA-Omniscience.

Type: Evaluation | Date: 2026-06-10

---

<a id="case-37"></a>
### Case 37: [Artificial Analysis Intelligence Index Result](https://x.com/ArtificialAnlys/status/2064500150069030992) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Use this case to benchmark Fable 5's overall intelligence ranking against other frontier models.**

Claude Fable 5 launched at #1 on the Artificial Analysis Intelligence Index, putting Anthropic nearly 5 points ahead of any other lab's best model.

We supported @AnthropicAI with pre-release evaluation of Claude Fable 5.

Claude Fable 5 scores 64.9 on the Artificial Analysis Intelligence Index, claiming the #1 rank overall.

It is around 5 points ahead of the closest non-Anthropic model, GPT-5.5.

Anthropic models now occupy both of the top 2 places.

Key takeaways for Claude Fable 5, using adaptive reasoning with max effort and Opus 4.8 as fallback model:

New safety guardrails for Mythos-class models:

- Claude Fable 5 uses the same underlying model as Claude Mythos 5 for public usage.
- It adds guardrails for potentially harmful cybersecurity, biology, chemistry, and distillation-related queries.
- We tested Fable 5 using Anthropic's fallback mechanism, which can route safety-flagged messages to Claude Opus 4.8.
- Anthropic states fallback occurs in fewer than 5% of sessions on average.
- We recorded fallback routing in around 8% of tasks across the Intelligence Index, mostly in scientific questions from evaluations like GPQA, AA-Omniscience, and Humanity's Last Exam.

State-of-the-art intelligence:

- Claude Fable 5 takes the #1 position on the Artificial Analysis Intelligence Index.
- Score: 64.9.
- Highest score on 5 of the 10 underlying benchmarks.
- On AA-Omniscience, Fable 5 scores 40, +7 points over the previous leader, Gemini 3.1 Pro Preview.

Frontier agentic capability:

- Fable 5 is at the frontier across all three agentic evaluations in the Index.
- GDPval-AA: real-world work tasks.
- Terminal-Bench Hard: agentic coding.
- Tau2-bench Telecom: tool use for customer service.
- GDPval-AA Elo: 1932, a significant jump from Claude Opus 4.8.

Humanity's Last Exam:

- Fable 5 scores 53%.
- It is more than 7 points ahead of the next-best model, Claude Opus 4.8 max.
- It triggers safety guardrails on 9% of HLE tasks, falling back to Claude Opus 4.8.
- Including fallback usage, running HLE with Fable 5 costs around $2.2k, the highest of any model evaluated.

Key model details:

- Context window: 1M tokens, same as Claude Opus 4.8.
- Price: $10/$50 per 1M input/output tokens.
- Cache write/read price: $12.50/$1 per million tokens.
- Availability: included in Pro, Max, Team, and seat-based Enterprise plans through June 22, consuming 2x Opus usage.
- From June 23, usage requires credits; Anthropic says it plans to restore subscription access once capacity allows.

Type: Evaluation | Date: 2026-06-10

---

<a id="case-38"></a>
### Case 38: [GDPval-AA Agentic Knowledge Work Benchmark](https://x.com/ArtificialAnlys/status/2064414308289937869) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Use this case to evaluate Fable 5 on agentic real-world knowledge work.**

Anthropic has released Claude Fable 5, the first publicly available Mythos-class model that ranks #1 in our agentic real-world knowledge work benchmark, GDPval-AA.

Claude Fable 5 shares the same underlying model as Claude Mythos 5, with added security guardrails for potentially harmful cybersecurity, biology, chemistry, and distillation-related queries.

The release also introduces a fallback mechanism, allowing Claude Fable 5 to route flagged queries to a second model such as Claude Opus 4.8.

@AnthropicAI shared access with us ahead of public release to benchmark this model.

GDPval-AA result:

- Score: 1932
- Rank: #1
- Benchmark: agentic real-world work tasks
- Anthropic models now occupy 3 of the top 4 spots

The result was measured using adaptive reasoning at max effort, with Claude Opus 4.8 configured as the fallback model.

Fable 5 falls back to Opus 4.8 on 2% of GDPval-AA tasks, with Anthropic stating fallback occurs in fewer than 5% of sessions on average.

Full benchmarks for Claude Fable 5 are in progress. We will share the full Intelligence Index and publish scores on our website shortly.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-39"></a>
### Case 39: [One-Week First Impressions and Pricing Mechanics](https://x.com/Conor_D_Dart/status/2064424882977243526) (by [@Conor_D_Dart](https://x.com/Conor_D_Dart))

**Use this first-impressions case to decide where Fable 5 is strongest, especially game design and systems planning.**

My first impressions of Fable 5:

I have spent the last week using Fable 5, mostly in High mode, and my first impression is that it is genuinely impressive.

The biggest standout is game design.

This is easily the strongest AI model I have personally used for designing games, systems, mechanics, and overall project structure.

For the first time, it feels like a model that could realistically help build a complete game from start to finish.

The trade-off is speed. Fable 5 takes noticeably longer to work than most frontier models, but the quality of the output often makes the wait worthwhile.

It has also been surprisingly effective at fixing bugs. Several issues I struggled with throughout the week were resolved quickly, and overall I have seen very strong performance on development tasks.

The biggest caveat is cost.

Fable 5 is incredibly expensive to run.

If current plans remain unchanged, from June 22, 2026, it will no longer be available through Claude Code and will be API-only.

Given that the API pricing is reportedly around double that of Opus, many people may not get the chance to use it extensively.

Early days, but so far Fable 5 has made a very strong first impression.

Type: Integration | Date: 2026-06-09

---

<a id="case-40"></a>
### Case 40: [Cost and Speed Comparison](https://x.com/HKrackDev/status/2064435392649306546) (by [@HKrackDev](https://x.com/HKrackDev))

**Use this comparison to decide whether the quality gain justifies higher cost and slower long-horizon runs.**

Is @AnthropicAI's Fable 5 actually worth the upgrade?

We benchmarked the new Mythos-family model against Claude Opus 4.8, and the data tells a surprising story:

- Costs 2x more than Claude Opus 4.8.
- Up to 3x slower on long-horizon engineering tasks.
- 15-20% more comments, but mostly minor nitpicks.

Fable 5 has incredible intuition for creative tasks like game design, but for day-to-day development workflows, Claude Opus 4.8 still takes the crown for quality versus price.

Check out my discussion with @JuanPa from our DevEx team at @coderabbitai on the model release.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-41"></a>
### Case 41: [Claude Code Hands-On Notes](https://x.com/Hi_Noguchi/status/2064419241068319079) (by [@Hi_Noguchi](https://x.com/Hi_Noguchi))

**Use this case to evaluate Fable 5 inside Claude Code, including tool use, personality, and remaining rough edges.**

I tried Claude Fable 5 with Claude Code 2.1.170.

Overall, my impression is positive. It feels like a legitimate evolution of Opus 4.6.

I have only used it for a little under an hour, so rough edges may appear with more use, but the good points are:

- It no longer produces the strange GPT-like wording seen in Opus 4.7 or 4.8.
- It does not have the pointless long-thinking habit that 4.8 had on effort high.
- It has the same high EQ and pleasant feel as 4.6, without losing humor or consideration.
- It does not feel opaque or vaguely unsettling like 4.7 or 4.8.
- Tool use is good, and it impresses me by remembering instructions I did not explicitly repeat.

On the negative side, even for small requests it can still think too much, and some misjudgments remain.

The initial experience is promising, but it needs longer use to see where the rough edges really are.

Type: Demo | Date: 2026-06-09

---

<a id="case-42"></a>
### Case 42: [Creative Writing Benchmark Result](https://x.com/LechMazur/status/2064503575577821458) (by [@LechMazur](https://x.com/LechMazur))

**Use this benchmark case to judge Fable 5's short-fiction writing quality and refusal behavior.**

Claude Fable 5 (high) is a step up in short-fiction writing.

On the Short-Story Creative Writing Benchmark, it beats Claude Opus 4.8 (xhigh) and Claude Opus 4.7 (high), and ranks second behind GPT-5.5 (xhigh).

Caveat: it refused 5 of the 400 creative-writing prompts.

https://t.co/76nCxwEybJ

Type: Evaluation | Date: 2026-06-10

---

<a id="case-43"></a>
### Case 43: [Multi-Benchmark Launch Summary](https://x.com/MTSlive/status/2064430633800319436) (by [@MTSlive](https://x.com/MTSlive))

**Use this launch benchmark summary to understand the headline scores most relevant to coding agents and complex tasks.**

SITUATION EXPLAINED: Claude Fable 5 just dropped.
• Anthropic launched Claude Fable 5 today, "a Mythos class model made safe for general use"
• Frontier Code Diamond: GPT 5.5 at 6%, Opus 4.8 at 13%, Fable 5 at 29-30%
• Agentic coding: 88%, Cybersecurity: 78%

Anthropic: "The longer and more complex the task, the larger Fable 5's lead over our other models."

@theojaffee: "This Frontier Code Diamond benchmark was announced yesterday. Top model was Opus 4.8 at thirteen percent. GPT 5.5 at six percent. Fable 5 is at twenty-nine percent."

Type: Evaluation | Date: 2026-06-09

---

<a id="case-44"></a>
### Case 44: [Benchmark and Pricing Comparison with GPT-5.5](https://x.com/VaibhavSisinty/status/2064459064810361271) (by [@VaibhavSisinty](https://x.com/VaibhavSisinty))

**Use this comparison to evaluate Fable 5 against GPT-5.5 on price and benchmark categories.**

Anthropic's new Mythos-class model is 3x cheaper than OpenAI's best model. And it beats it on nearly every benchmark. 🤯

Pricing:

- GPT-5.5 Pro: $30 input / $180 output
- Claude Fable 5: $10 input / $50 output

The benchmarks:

→ Agentic coding: 80.3% vs 58.6%
→ FrontierCode (code quality): 29.3% vs 5.7%
→ Cybersecurity: 78.0% vs 34.0%
→ Legal: 13.3% vs 2.1%
→ Reasoning: 59.0% vs 41.4%
→ Health: 66.0% vs 51.8%
→ Computer use: 85.0% vs 78.7%

Cheaper. Better. On almost everything.

Free on Pro and Max plans through June 22. It is called Claude Fable 5.

Type: Evaluation | Date: 2026-06-09

---

<a id="case-45"></a>
### Case 45: [Field Notes with Practical Limitations](https://x.com/alliekmiller/status/2064451731325415446) (by [@alliekmiller](https://x.com/alliekmiller))

**Use this field report to understand where Fable 5 feels meaningfully better and where it still has practical limits.**

🚨 Fable 5 is something to pay attention to.

This is another "I had early access to the new Mythos-class Anthropic model and I want to tell you what I thought of it" post.

I know, I know, it's annoying.

But the way I now spend my weekends has completely changed because of this new class of model.

And I need to share it with you all.
- This is an actual leap. The jump from "4.8" anything to "5" anything just sounds small, but the functionality shift I felt is big. Within my first few prompts, I went, "Oh, this is it."