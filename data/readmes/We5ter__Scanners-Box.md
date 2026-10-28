English | [简体中文](./README_CN.md) | [Español](./README_ES.md)

<p align="center">
<img src="./logo.png" width="300px">
 </p>

<p align="center">
  <img src="./badges/version.svg" alt="version">
  <img src="./badges/license.svg" alt="license">
 <img src="./badges/scanners-count.svg" alt="scanners">
 <a href="https://we5ter.github.io/ai-tools/"><img src="./badges/daily-ai-picks.svg" alt="Daily AI Tool Picks"></a>
 <a href="https://github.com/We5ter/ScanCodex"><img src="./badges/scancodex.svg" alt="ScanCodex MCP Server"></a>
 <a href="https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2FWe5ter%2FScanners-Box"><img src="./badges/x-share.svg" alt="Share on X"></a>
 </p>

## Introduction

- **EN** The Ultimate Open-Source Security Arsenal for Hackers, Enterprises, and AI Agents
- **中文** 面向极客、企业与 AI 智能体的全域开源网络安全工具矩阵
- **ES** El arsenal definitivo de seguridad de código abierto para hackers, empresas y agentes de IA

> [!TIP]
> **📅 Tired of hunting all over the place for AI agent tools? → [Scanners-Box Daily AI Tool Picks](https://we5ter.github.io/ai-tools/)**

## Sponsors

| Sponsor | About |
|:---:|---|
| <a href="https://www.aiwts.com/" target="_blank"><img src="https://www.aiwts.com/vitas/vitas-logo-transparent.webp" alt="维塔斯AI聚合"></a> | <a href="https://www.aiwts.com/" target="_blank"><b>维塔斯AI聚合</b></a> 是企业级 AI 大模型 API 聚合服务：开发者只需一个 Key，即可统一调用 GPT、Claude、DeepSeek、Gemini 等 200+ 模型（文本/生图/视频），完全兼容 OpenAI 协议，无需海外账号与信用卡 [https://www.aiwts.com/](https://www.aiwts.com/) |

> [!NOTE]
> **Want to become the next sponsor?** Open a [GitHub Issue](https://github.com/We5ter/Scanners-Box/issues) or email [wester0x01@qq.com](mailto:wester0x01@qq.com). Individual tips are welcome too.

<p align="center">
  <a href="https://www.paypal.com/paypalme/zhiyangzeng" target="_blank"><img src="badges/blue.svg" width="200" alt="Donate with PayPal"></a>
  <br><br>
  <img src="badges/wechat-donate.jpg" width="200" alt="WeChat reward code">
</p>

## Contents

> [!IMPORTANT]
> **🤖 Security For AI & AI For Security**
>
> - [AI Red Teaming Frameworks & Agents](#ai-red-teaming-frameworks--agents)
> - [LLM-Powered Vulnerability Scanners](#llm-powered-vulnerability-scanners)
> - [Security Auditing for AI Agents & Apps](#security-auditing-for-ai-agents--apps)
> - [AI Agent Runtime Controls](#ai-agent-runtime-controls)
> - [Security Auditing for Agent Skills](#security-auditing-for-agent-skills)
> - [Agent Skills for Vulnerability Discovery & Remediation](#agent-skills-for-vulnerability-discovery--remediation)
> - [Security Toolkits for Agentic Workflows](#security-toolkits-for-agentic-workflows)
> - [AI Security Verification Standards](#ai-security-verification-standards)

- [Scanners for Smart Contracts](#scanners-for-smart-contracts)
- [Red Team vs Blue Team](#red-team-vs-blue-team)
- [Mobile App Packages Analysis](#mobile-apps-packages-analysis)
- [Binary Executables Analysis](#binary-executables-analysis)
- [Privacy Compliance](#privacy-compliance)
- [Subdomain Enumeration or Takeover](#subdomain-enumeration-or-takeover)
- [Database SQL Injection Vulnerability or Brute Force](#database-sql-injection-vulnerability-or-brute-force)
- [Weak Usernames or Passwords Enumeration For Web](#weak-usernames-or-passwords-enumeration-for-web)
- [IoT Hardware Automated Audit](#iot-hardware-automated-audit)
- [Mutiple types of Cross-site scripting Detection](#mutiple-types-of-cross-site-scripting-detection)
- [Enterprise sensitive information Leak Scan](#enterprise-sensitive-information-leak-scan)
- [Malware Detection](#malware-detection)
- [Vulnerability Assessment for Middleware](#vulnerability-assessment-for-middleware)
- [Special Vulnerability Categories Scannners for Web](#special-vulnerability-categories-scanners-for-web)
- [Dynamic or Static Code Analysis](#dynamic-or-static-code-analysis)
- [Modular Design Scanners or Vulnerability Detecting Framework](#modular-design-scanners-or-vulnerability-detecting-framework)
- [Advanced Persistent Threat Detect](#advanced-persistent-threat-detect)

***

### AI Red Teaming Frameworks & Agents

*Mature autonomous agents, plus foundational frameworks to build your own.*

- https://github.com/confident-ai/deepteam - **Open-source red teaming framework for LLM systems — "penetration testing, but for LLMs": 50+ ready-to-use vulnerabilities with local LLM-as-a-Judge scoring, simulating jailbreaks, prompt injection and multi-turn exploitation across AI agents, RAG pipelines and chatbots, plus guardrails for production**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/confident-ai/deepteam?style=for-the-badge)  ![GitHub stars](https://img.shields.io/github/stars/confident-ai/deepteam.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/confident-ai/deepteam?style=for-the-badge)

- https://github.com/vxcontrol/pentagi - **Fully autonomous multi-agent pentesting system in Go — runs whole engagements inside an isolated Docker sandbox with 20+ built-in tools (nmap, metasploit, sqlmap), long-term memory, optional Neo4j knowledge graph, and a web console for human-in-the-loop monitoring**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/vxcontrol/pentagi?style=for-the-badge)  ![GitHub stars](https://img.shields.io/github/stars/vxcontrol/pentagi.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/vxcontrol/pentagi?style=for-the-badge)

- https://github.com/oritera/Cairn - **A general-purpose state-space search engine validated on autonomous penetration testing — no predefined roles or workflows, purely goal-driven pathfinding**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/oritera/Cairn?style=for-the-badge)  ![GitHub stars](https://img.shields.io/github/stars/oritera/Cairn.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/oritera/Cairn?style=for-the-badge)

- https://github.com/KeygraphHQ/shannon - **Autonomous white-box AI pentester for web apps & APIs — analyzes source code, identifies attack vectors, and executes real exploits pre-production**

> ![](https://img.shields.io/badge/MainLanguage-TypeScript-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/KeygraphHQ/shannon?style=for-the-badge)  ![GitHub stars](https://img.shields.io/github/stars/KeygraphHQ/shannon.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/KeygraphHQ/shannon?style=for-the-badge)

- https://github.com/SickHackPark/SickHackShark - **Multi-agent AI platform for CTF automation — covers recon, scanning, exploitation, and flag capture end-to-end**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/SickHackPark/SickHackShark?style=for-the-badge)  ![GitHub stars](https://img.shields.io/github/stars/SickHackPark/SickHackShark.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/SickHackPark/SickHackShark?style=for-the-badge)

- https://github.com/SanMuzZzZz/LuaN1aoAgent - **LuaN1ao (鸾鸟) - A next-generation Autonomous Penetration Testing Agent powered by LLMs, integrating P-E-R Agent Collaboration with Causal Graph Reasoning to simulate security expert thinking patterns**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/SanMuzZzZz/LuaN1aoAgent?style=for-the-badge)  ![GitHub stars](https://img.shields.io/github/stars/SanMuzZzZz/LuaN1aoAgent.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/SanMuzZzZz/LuaN1aoAgent?style=for-the-badge)

- https://github.com/Ed1s0nZ/CyberStrikeAI - **An AI-native security testing platform in Go, integrating 100+ tools, intelligent orchestration, role-based testing, skills system, full lifecycle management, and a built-in lightweight C2 framework for authorized engagements**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/Ed1s0nZ/CyberStrikeAI?style=for-the-badge)  ![GitHub stars](https://img.shields.io/github/stars/Ed1s0nZ/CyberStrikeAI.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/Ed1s0nZ/CyberStrikeAI?style=for-the-badge)

- https://github.com/ASCIT31/Dark-Moon - **Autonomous AI pentesting engine performing continuous offensive security across web, cloud, AD and Kubernetes. Uses agentic reasoning, real exploit execution and attack path analysis to deliver proof-based vulnerabilities.**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/ASCIT31/Dark-Moon?style=for-the-badge)  ![GitHub stars](https://img.shields.io/github/stars/ASCIT31/Dark-Moon.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/ASCIT31/Dark-Moon?style=for-the-badge)


### LLM-Powered Vulnerability Scanners
*Scanners where the LLM does the hunting — beyond signature matching.*


- https://github.com/weareaisle/nano-analyzer - **A minimal LLM-powered zero-day vulnerability scanner by AISLE**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/weareaisle/nano-analyzer?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/weareaisle/nano-analyzer.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/weareaisle/nano-analyzer?style=for-the-badge)

- https://github.com/vercel-labs/deepsec - **An agent-powered vulnerability scanner for on-demand review of all code in existing large-scale repos, surfacing hard-to-find issues that have been lurking in applications for a long time**

> ![](https://img.shields.io/badge/MainLanguage-Node.js-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/vercel-labs/deepsec?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/vercel-labs/deepsec.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/vercel-labs/deepsec?style=for-the-badge)

- https://github.com/vigolium/vigolium - **High-fidelity vulnerability scanner fusing agentic AI with native speed, modularity, and precision**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/vigolium/vigolium?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/vigolium/vigolium.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/vigolium/vigolium?style=for-the-badge)


### Security Auditing for AI Agents & Apps
*Security scanners aimed at the AI systems themselves: LLMs, agents and their infrastructure.*


- https://github.com/leondz/garak - **LLM vulnerability scanner for hallucination, data leakage, promp injection, misinformation, toxicity generation, jailbreaks, and many other weaknesses**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/leondz/garak?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/leondz/garak.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/leondz/garak?style=for-the-badge)

- https://github.com/protectai/rebuff - **Designed to protect AI applications from prompt injection (PI) attacks**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/protectai/rebuff?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/protectai/rebuff.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/protectai/rebuff?style=for-the-badge)

- https://github.com/mnns/LLMFuzzer - **Fuzzing Framework for Large Language Models**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/mnns/LLMFuzzer?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/mnns/LLMFuzzer.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/mnns/LLMFuzzer?style=for-the-badge)

- https://github.com/Tencent/AI-Infra-Guard - **A.I.G (AI-Infra-Guard) integrates capabilities such as AI infrastructure vulnerability scanning, MCP Server risk detection, and LLM security assessments**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/Tencent/AI-Infra-Guard?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/Tencent/AI-Infra-Guard.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/Tencent/AI-Infra-Guard?style=for-the-badge)

- https://github.com/affaan-m/agentshield - **Security auditor for AI agent configurations — scans Claude Code setups for hardcoded secrets, permission misconfigs, hook injection, MCP server risks and prompt injection vectors; 268 rules across 15 modules, scored 0-100, with auto-fix, CI gating and compliance mapping (SOC 2 / PCI DSS / ISO 27001)**

> ![](https://img.shields.io/badge/MainLanguage-TypeScript-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/affaan-m/agentshield?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/affaan-m/agentshield.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/affaan-m/agentshield?style=for-the-badge)

- https://github.com/cisco-ai-defense/mcp-scanner - **Security scanner for Model Context Protocol (MCP) servers — combines YARA rules, LLM-based analysis and Cisco AI Defense detections to flag malicious MCP tools, tool poisoning, prompt injection and other threats across the MCP ecosystem**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/cisco-ai-defense/mcp-scanner?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/cisco-ai-defense/mcp-scanner.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/cisco-ai-defense/mcp-scanner?style=for-the-badge)


### AI Agent Runtime Controls
*Sandboxes, policy engines and approval gates that bound what agents can do.*


- https://github.com/NVIDIA/OpenShell - **Sandboxed runtime for autonomous AI agents — declarative YAML policies enforce boundaries across filesystem, network, process and provider access, block data exfiltration and unauthorized egress, and inject credentials only into policy-admitted endpoints; runs Claude Code, Codex, OpenCode and Copilot CLI in isolated containers on Docker, Podman, MicroVM or Kubernetes**

> ![](https://img.shields.io/badge/MainLanguage-Rust-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/NVIDIA/OpenShell?style=for-the-badge)  ![GitHub stars](https://img.shields.io/github/stars/NVIDIA/OpenShell.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/NVIDIA/OpenShell?style=for-the-badge)

- https://github.com/microsoft/agent-governance-toolkit - **Microsoft's governance toolkit for autonomous AI agents — a policy engine authorizing tools and actions, zero-trust agent identity with short-lived scoped credentials, OS-level execution sandboxing, plus reliability engineering (circuit breakers, budget caps, audit trails); ships reference policy packs mapped to all 10 OWASP Agentic Top 10 categories**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/microsoft/agent-governance-toolkit?style=for-the-badge)  ![GitHub stars](https://img.shields.io/github/stars/microsoft/agent-governance-toolkit.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/microsoft/agent-governance-toolkit?style=for-the-badge)

- https://github.com/agentkitai/agentgate - **Approval workflow engine for AI agents — define policies to auto-approve safe actions, auto-deny dangerous ones, and route the rest to a human via dashboard, Slack, Discord, or email**

> ![](https://img.shields.io/badge/MainLanguage-TypeScript-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/agentkitai/agentgate?style=for-the-badge)  ![GitHub stars](https://img.shields.io/github/stars/agentkitai/agentgate.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/agentkitai/agentgate?style=for-the-badge)

- https://github.com/kubernetes-sigs/agent-sandbox - **Kubernetes-native sandbox for AI agent workloads — the Sandbox CRD manages isolated, stateful, singleton pods with stable identity and persistent storage, supports gVisor/Kata secure runtimes, deep hibernation and auto-resume, plus SandboxTemplate/SandboxClaim/SandboxWarmPool extensions and Go/Python SDKs**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/kubernetes-sigs/agent-sandbox?style=for-the-badge)  ![GitHub stars](https://img.shields.io/github/stars/kubernetes-sigs/agent-sandbox.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/kubernetes-sigs/agent-sandbox?style=for-the-badge)


### Security Auditing for Agent Skills
*Scan agent skill packages for malicious patterns before you install them.*


- https://github.com/NVIDIA/SkillSpector - **Security scanner for AI agent skills — detect vulnerabilities, malicious patterns, and security risks before installing agent skills (Claude Code, Codex CLI, Gemini CLI, etc.)**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/NVIDIA/SkillSpector?style=for-the-badge)  ![GitHub stars](https://img.shields.io/github/stars/NVIDIA/SkillSpector.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/NVIDIA/SkillSpector?style=for-the-badge)

- https://github.com/cisco-ai-defense/skill-scanner - **A best-effort security scanner for AI Agent Skills — detects prompt injection, data exfiltration, and malicious code patterns via pattern-based detection (YAML+YARA), LLM-as-a-judge, and behavioral dataflow analysis. Supports OpenAI Codex Skills, Cursor Agent Skills, and Claude Code commands.**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/cisco-ai-defense/skill-scanner?style=for-the-badge)  ![GitHub stars](https://img.shields.io/github/stars/cisco-ai-defense/skill-scanner.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/cisco-ai-defense/skill-scanner?style=for-the-badge)


### Agent Skills for Vulnerability Discovery & Remediation
*Skill packs that teach coding agents to find and fix vulnerabilities end to end.*


- https://github.com/anthropics/defending-code-reference-harness - **Skills for threat modeling, scanning, triage, patching, plus an autonomous scanning harness you can customize for end-to-end vulnerability management**

> ![](https://img.shields.io/badge/MainLanguage-Markdown-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/anthropics/defending-code-reference-harness?style=for-the-badge)  ![GitHub stars](https://img.shields.io/github/stars/anthropics/defending-code-reference-harness.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/anthropics/defending-code-reference-harness?style=for-the-badge)

- https://github.com/cloudflare/security-audit-skill - **A coding-agent skill for multi-phase security audits — recon, hunting, adversarial validation, reporting, structured output, and independent verification — with machine-readable findings**

> ![](https://img.shields.io/badge/MainLanguage-Markdown-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/cloudflare/security-audit-skill?style=for-the-badge)  ![GitHub stars](https://img.shields.io/github/stars/cloudflare/security-audit-skill.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/cloudflare/security-audit-skill?style=for-the-badge)


### Security Toolkits for Agentic Workflows
*Unified tooling that equips agents for professional security work.*


- https://github.com/h5i-dev/h5i - **Agent-native web security workspace — hands AI agents a unified toolkit (browser automation, HTTP traffic capture / tamper / replay, recon crawling) to red-team web apps inside a configurable sandbox, replays confirmed attack flows in CI/CD as security regression checks, and formally verifies Rust application logic against Lean 4**

> ![](https://img.shields.io/badge/MainLanguage-Rust-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/h5i-dev/h5i?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/h5i-dev/h5i.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/h5i-dev/h5i?style=for-the-badge)


### AI Security Verification Standards
*Testable standards and checklists that define verifiable AI security.*


- https://github.com/OWASP/AISVS - **OWASP Artificial Intelligence Security Verification Standard — 213 testable requirements ("Verify that...") across 12 control families and 44 sections, graded L1/L2/L3, covering training data, model supply chain, RAG memory, agent and MCP security; designed to be verified in parallel with ASVS at the matching level**

> ![](https://img.shields.io/badge/MainLanguage-Markdown-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/OWASP/AISVS?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/OWASP/AISVS.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/OWASP/AISVS?style=for-the-badge)


### Scanners for Smart Contracts

- https://github.com/ConsenSys/mythril - **Security analysis tool for EVM bytecode. Supports smart contracts built for Ethereum, Hedera etc.**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/ConsenSys/mythril?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/ConsenSys/mythril.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/ConsenSys/mythril?style=for-the-badge)

- https://github.com/enzymefinance/oyente - **An Analysis Tool for Smart Contracts**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/enzymefinance/oyente?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/enzymefinance/oyente.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/enzymefinance/oyente?style=for-the-badge)

- https://github.com/eth-sri/securify2 - **Official security scanner for Ethereum smart contracts supported by the Ethereum Foundation**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/eth-sri/securify2?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/eth-sri/securify2.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/eth-sri/securify2?style=for-the-badge)

- https://github.com/smartdec/smartcheck - **Static analysis tool that detects vulnerabilities and bugs in Solidity programs**

> ![](https://img.shields.io/badge/MainLanguage-Java--or--Node-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/smartdec/smartcheck?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/smartdec/smartcheck.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/smartdec/smartcheck?style=for-the-badge)

- https://github.com/ivicanikolicsg/MAIAN - **Automatic tool for finding trace vulnerabilities in Ethereum smart contracts**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/ivicanikolicsg/MAIAN?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/ivicanikolicsg/MAIAN.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/ivicanikolicsg/MAIAN?style=for-the-badge)


### Red Team vs Blue Team

#### Supply Chain Analysis(SCA)

- https://github.com/murphysecurity/murphysec - **Open source tool for software supply chain security**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/murphysecurity/murphysec?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/murphysecurity/murphysec.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/murphysecurity/murphysec?style=for-the-badge)

#### Container and Cluster

- https://github.com/cdk-team/CDK - **A tool to gather information inside container/cluster and exploit them**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/cdk-team/CDK?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/cdk-team/CDK.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/cdk-team/CDK?style=for-the-badge)

- https://github.com/cr0hn/dockerscan - **Docker security analysis & hacking tools**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/cr0hn/dockerscan?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/cr0hn/dockerscan?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/cr0hn/dockerscan?style=for-the-badge)

- https://github.com/armosec/kubescape - **The first tool for testing if Kubernetes is deployed securely as defined in Kubernetes Hardening Guidance by to NSA and CISA**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/armosec/kubescape?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/armosec/kubescape?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/armosec/kubescape?style=for-the-badge)

- https://github.com/chaitin/veinmind-tools - **Container security scanner for backdoor, malicious, weak pass and sensitive and the like.**

> ![](https://img.shields.io/badge/MainLanguage-Go/Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/chaitin/veinmind-tools?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/chaitin/veinmind-tools?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/chaitin/veinmind-tools?style=for-the-badge)

- https://github.com/deepfence/ThreatMapper - **Scan for in-production vulnerabilities and exposed secrets, and identify attack paths to reach them remotely**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge) ![GitHub last commit](https://img.shields.io/github/last-commit/deepfence/ThreatMapper?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/deepfence/ThreatMapper?style=for-the-badge) ![GitHub](https://img.shields.io/github/license/deepfence/ThreatMapper?style=for-the-badge)

- https://github.com/deepfence/SecretScanner - **Scan containers and host filesystems for unprotected keys, API tokens and passwords**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/deepfence/SecretScanner?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/deepfence/SecretScanner?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/deepfence/SecretScanner?style=for-the-badge)

- https://github.com/cyberark/KubiScan - **A tool to scan Kubernetes cluster for risky permissions**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/cyberark/KubiScan?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/cyberark/KubiScan?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/cyberark/KubiScan?style=for-the-badge)

- https://github.com/kvesta/vesta - **A static analysis of vulnerabilities, Docker and Kubernetes cluster configuration detect toolkit**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/kvesta/vesta?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/kvesta/vesta?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/kvesta/vesta?style=for-the-badge)

- https://github.com/anchore/grype - **A vulnerability scanner for container images and filesystems**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/anchore/grype?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/anchore/grype?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/anchore/grype?style=for-the-badge)


#### Services fingerprint detection

- https://github.com/EdgeSecurityTeam/EHole - **Core system fingerprint detection tool for Red team**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/EdgeSecurityTeam/EHole?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/EdgeSecurityTeam/EHole.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/EdgeSecurityTeam/EHole?style=for-the-badge)

- https://github.com/opabravo/mass-bruter - **Mass bruteforce network protocols and default credentials for ports**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/opabravo/mass-bruter?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/opabravo/mass-bruter.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/opabravo/mass-bruter?style=for-the-badge)

#### Man-In-The-Middle

- https://github.com/niloofarkheirkhah/nili - **Tool for Network Scan, Man in the Middle, Protocol Reverse Engineering and Fuzzing**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/niloofarkheirkhah/nili?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/niloofarkheirkhah/nili.svg?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/niloofarkheirkhah/nili?style=for-the-badge)

#### The framework

- https://github.com/m4n3dw0lf/PytheM - **Multi-purpose network pentest framework**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/m4n3dw0lf/PytheM?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/m4n3dw0lf/PytheM?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/m4n3dw0lf/PytheM?style=for-the-badge)

- https://github.com/FunnyWolf/Viper  - **Graphical, Modularization and weaponization intranet penetration tool**

> ![](https://img.shields.io/badge/MainLanguage-Ruby-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/FunnyWolf/Viper?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/FunnyWolf/Viper?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/FunnyWolf/Viper?style=for-the-badge)

- https://github.com/P1-Team/AlliN  - **Mostly used for asset collection before penetration and lateral movement of intranet**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/P1-Team/AlliN?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/P1-Team/AlliN?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/P1-Team/AlliN?style=for-the-badge)

- https://github.com/k8gege/LadonGo  - **Pentest framework for Windows/Linux/Mac intranet networks**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/k8gege/LadonGo?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/k8gege/LadonGo?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/k8gege/LadonGo?style=for-the-badge)

- https://github.com/shmilylty/netspy  - **Quickly scan the reachable network segmentation of the intranet**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/shmilylty/netspy?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/shmilylty/netspy?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/shmilylty/netspy?style=for-the-badge)

- https://github.com/byt3bl33d3r/CrackMapExec  - **Swiss army knife for pentesting Windows/Active Directory environments**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/byt3bl33d3r/CrackMapExec?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/byt3bl33d3r/CrackMapExec?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/byt3bl33d3r/CrackMapExec?style=for-the-badge)

- https://github.com/u21h2/nacs  - **Event-driven intranet pentest scanner**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/u21h2/nacs?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/u21h2/nacs?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/u21h2/nacs?style=for-the-badge)


- https://github.com/h4wkst3r/SCMKit  - **Source Code Management Attack Toolkit,such as GitHub Enterprise, GitLab Enterprise and Bitbucket Server**

> ![](https://img.shields.io/badge/MainLanguage-CSharp-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/h4wkst3r/SCMKit?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/h4wkst3r/SCMKit?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/h4wkst3r/SCMKit?style=for-the-badge)

- https://github.com/lijiejie/MisConfig_HTTP_Proxy_Scanner  - **Helps to scan misconfigured reverse proxy servers and misconfigured forward proxy servers**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/lijiejie/MisConfig_HTTP_Proxy_Scanner?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/lijiejie/MisConfig_HTTP_Proxy_Scanner?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/lijiejie/MisConfig_HTTP_Proxy_Scanner?style=for-the-badge)

- https://github.com/chainreactors/gogo  - **A highly controllable and scalable automation engine for red teams**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/chainreactors/gogo?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/chainreactors/gogo?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/chainreactors/gogo?style=for-the-badge)

- https://github.com/freelabz/secator  - **secator - the pentester's swiss knife**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/freelabz/secator?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/freelabz/secator?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/freelabz/secator?style=for-the-badge)


#### Wireless Pentest

- https://github.com/savio-code/fern-wifi-cracker - **Testing and discovering flaws in ones own network**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/savio-code/fern-wifi-cracker?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/savio-code/fern-wifi-cracker?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/savio-code/fern-wifi-cracker?style=for-the-badge)

- https://github.com/P0cL4bs/WiFi-Pumpkin - **Framework for Rogue Wi-Fi Access Point Attack**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/P0cL4bs/WiFi-Pumpkin?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/P0cL4bs/WiFi-Pumpkin?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/P0cL4bs/WiFi-Pumpkin?style=for-the-badge)

- https://github.com/MisterBianco/BoopSuite - **A Suite of Tools written in Python for wireless auditing and security testing**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/MisterBianco/BoopSuite?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/MisterBianco/BoopSuite?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/MisterBianco/BoopSuite?style=for-the-badge)

- https://github.com/besimaltnok/PiFinger - **Searches for wifi-pineapple traces and calculate wireless network security score**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/besimaltnok/PiFinger?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/besimaltnok/PiFinger?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/besimaltnok/PiFinger?style=for-the-badge)

- https://github.com/derv82/wifite2 - **A complete re-write of Wifite,Automated Wireless Attack Tool**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/derv82/wifite2?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/derv82/wifite2?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/derv82/wifite2?style=for-the-badge)

- https://github.com/D3Ext/WEF - **Wi-Fi Exploitation Framework for 2.4 and 5 Ghz both attacks**

> ![](https://img.shields.io/badge/MainLanguage-Bash-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/D3Ext/WEF?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/D3Ext/WEF?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/D3Ext/WEF?style=for-the-badge)

- https://github.com/pinecone-wifi/pinecone - **A WLAN red team framework**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/pinecone-wifi/pinecone?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/pinecone-wifi/pinecone?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/pinecone-wifi/pinecone?style=for-the-badge)


### Mobile Apps Packages Analysis

- https://github.com/dwisiswant0/apkleaks - **Scanning APK file for URIs, endpoints & secrets**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/dwisiswant0/apkleaks?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/dwisiswant0/apkleaks?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/dwisiswant0/apkleaks?style=for-the-badge)

- https://github.com/kelvinBen/AppInfoScanner - **Collecting information from APK file, support self-defined rules**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/kelvinBen/AppInfoScanner?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/kelvinBen/AppInfoScanner?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/kelvinBen/AppInfoScanner?style=for-the-badge)

- https://github.com/maaaaz/androwarn - **Yet another static code analyzer for malicious Android applications**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/maaaaz/androwarn?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/maaaaz/androwarn?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/maaaaz/androwarn?style=for-the-badge)

- https://github.com/quark-engine/quark-engine - **Android Malware (Analysis | Scoring) System**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/quark-engine/quark-engine?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/quark-engine/quark-engine?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/quark-engine/quark-engine?style=for-the-badge)

- https://github.com/droidefense/engine - **Advance Android malware analysis framework**

> ![](https://img.shields.io/badge/MainLanguage-Java-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/droidefense/engine?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/droidefense/engine?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/droidefense/engine?style=for-the-badge)

- https://github.com/abhi-r3v0/Adhrit - **Android Security Suite for in-depth reconnaissance and static bytecode analysis based on Ghera benchmarks**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/abhi-r3v0/Adhrit?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/abhi-r3v0/Adhrit?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/abhi-r3v0/Adhrit?style=for-the-badge) <img alt="BlacHatUSA-arsenal-2022" src="./badges/BlackHatUSA--arsenal-2022-blue.svg">

- https://github.com/pascal-lab/Tai-e - **An easy-to-learn/use static analysis framework for Java, especially for Android**

> ![](https://img.shields.io/badge/MainLanguage-Java-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/pascal-lab/Tai-e?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/pascal-lab/Tai-e?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/pascal-lab/Tai-e?style=for-the-badge)

- https://github.com/Cyber-Buddy/APKHunt - **A comprehensive static code analysis tool for Android apps that is based on the OWASP MASVS framework**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/Cyber-Buddy/APKHunt?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/Cyber-Buddy/APKHunt?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/Cyber-Buddy/APKHunt?style=for-the-badge)

- https://github.com/cryptax/droidlysis - **A pre-analysis tool for Android apps: it performs repetitive and boring tasks we'd typically do at the beginning of any reverse engineering**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/cryptax/droidlysis?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/cryptax/droidlysis?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/cryptax/droidlysis?style=for-the-badge)


### Binary Executables Analysis

- https://github.com/m4rco-/dorothy2 - **A malware/botnet analysis framework written in Ruby**

> ![](https://img.shields.io/badge/MainLanguage-Ruby-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/m4rco-/dorothy2?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/m4rco-/dorothy2?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/m4rco-/dorothy2?style=for-the-badge)

- https://github.com/Tencent/HaboMalHunter  - **Used for automated malware analysis and security assessment on the Linux system**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/Tencent/HaboMalHunter?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/Tencent/HaboMalHunter?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/Tencent/HaboMalHunter?style=for-the-badge)

- https://github.com/KeenSecurityLab/BinAbsInspector  - **Static analyzer for automated reverse engineering and scanning vulnerabilities in binaries**

> ![](https://img.shields.io/badge/MainLanguage-Java-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/KeenSecurityLab/BinAbsInspector?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/KeenSecurityLab/BinAbsInspector?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/KeenSecurityLab/BinAbsInspector?style=for-the-badge)

- https://github.com/fkie-cad/cwe_checker  - **Static analyzer for detecting common bug classes such as buffer overflows in binaries**

> ![](https://img.shields.io/badge/MainLanguage-Rust-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/fkie-cad/cwe_checker?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/fkie-cad/cwe_checker?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/fkie-cad/cwe_checker?style=for-the-badge)

- https://github.com/airbus-seclab/bincat  - **Binary code static analyser, with IDA integration. Performs value and taint analysis**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/airbus-seclab/bincat?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/airbus-seclab/bincat?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/airbus-seclab/bincat?style=for-the-badge)


### Privacy Compliance

- https://github.com/riskscanner/riskscanner - **Multi-cloud privacy compliance scanning platform, through Cloud Custodian's YAML DSL to define scanning rules**

> ![](https://img.shields.io/badge/MainLanguage-Java-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/riskscanner/riskscanner?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/riskscanner/riskscanner?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/riskscanner/riskscanner?style=for-the-badge)

- https://github.com/momosecurity/bombus - **Enterprise security and privacy compliance platform**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/momosecurity/bombus?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/momosecurity/bombus?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/momosecurity/bombus?style=for-the-badge)


### Subdomain Enumeration or Takeover

- https://github.com/lijiejie/subDomainsBrute - **A classical subdomain enumeration Tool by lijiejie**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/lijiejie/subDomainsBrute?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/lijiejie/subDomainsBrute?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/lijiejie/subDomainsBrute?style=for-the-badge)

- https://github.com/ring04h/wydomain - **A Speed and Precision subdomain enumeration Tool by ringzero**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/ring04h/wydomain?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/ring04h/wydomain?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/ring04h/wydomain?style=for-the-badge)

- https://github.com/le4f/dnsmaper - **Subdomain enumeration tool with map record**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/le4f/dnsmaper?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/le4f/dnsmaper?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/le4f/dnsmaper?style=for-the-badge)

- https://github.com/TheRook/subbrute - **A DNS meta-query spider that enumerates DNS records, and subdomains,supported API**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/TheRook/subbrute?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/TheRook/subbrute?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/TheRook/subbrute?style=for-the-badge)

- https://github.com/We5ter/GSDF - **Subdomain enumeration via Google certificate transparency**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/We5ter/GSDF?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/We5ter/GSDF?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/We5ter/GSDF?style=for-the-badge)

- https://github.com/mandatoryprogrammer/cloudflare_enum  - **Subdomain enumeration via CloudFlare**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/mandatoryprogrammer/cloudflare_enum?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/mandatoryprogrammer/cloudflare_enum?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/mandatoryprogrammer/cloudflare_enum?style=for-the-badge)

- https://github.com/guelfoweb/knock - **Knock subdomain scan**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/guelfoweb/knock?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/guelfoweb/knock?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/guelfoweb/knock?style=for-the-badge)

- https://github.com/exp-db/PythonPool/tree/master/Tools/DomainSeeker - **An intergratd Python subdomain enumeration tool**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/exp-db/PythonPool?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/exp-db/PythonPool?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/exp-db/PythonPool?style=for-the-badge)

- https://github.com/code-scan/BroDomain - **Find brother domain**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/code-scan/BroDomain?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/code-scan/BroDomain?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/code-scan/BroDomain?style=for-the-badge)

- https://github.com/chuhades/dnsbrute - **A fast domain brute tool**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/chuhades/dnsbrute?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/chuhades/dnsbrute?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/chuhades/dnsbrute?style=for-the-badge)

- https://github.com/yanxiu0614/subdomain3 - **A simple and fast tool for bruting subdomains**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/yanxiu0614/subdomain3?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/yanxiu0614/subdomain3?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/yanxiu0614/subdomain3?style=for-the-badge)

- https://github.com/michenriksen/aquatone - **A powerful subdomain tool and domain takeovers finding tools**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/michenriksen/aquatone?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/michenriksen/aquatone?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/michenriksen/aquatone?style=for-the-badge)

- https://github.com/evilsocket/dnssearch - **A subdomain enumeration tool**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/evilsocket/dnssearch?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/evilsocket/dnssearch?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/evilsocket/dnssearch?style=for-the-badge)

- https://github.com/reconned/domained - **Subdomain enumeration tools for bug hunting**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/reconned/domained?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/reconned/domained?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/reconned/domained?style=for-the-badge)

- https://github.com/bit4woo/Teemo - **A domain name & Email address collection tool**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/bit4woo/Teemo?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/bit4woo/Teemo?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/bit4woo/Teemo?style=for-the-badge)

- https://github.com/laramies/theHarvester - **E-mail, subdomain and people names harvester**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/laramies/theHarvester?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/laramies/theHarvester?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/laramies/theHarvester?style=for-the-badge)

- https://github.com/nmalcolm/Inventus - **A spider designed to find subdomains of a specific domain by crawling it**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/nmalcolm/Inventus?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/nmalcolm/Inventus?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/nmalcolm/Inventus?style=for-the-badge)

- https://github.com/aboul3la/Sublist3r - **Fast subdomains enumeration tool for penetration testers**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/aboul3la/Sublist3r?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/aboul3la/Sublist3r?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/aboul3la/Sublist3r?style=for-the-badge)

- https://github.com/jonluca/Anubis - **Subdomain enumeration and information gathering tool**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/jonluca/Anubis?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/jonluca/Anubis?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/jonluca/Anubis?style=for-the-badge)

- https://github.com/n4xh4ck5/N4xD0rk - **Listing subdomains about a main domain**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/n4xh4ck5/N4xD0rk?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/n4xh4ck5/N4xD0rk?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/n4xh4ck5/N4xD0rk?style=for-the-badge)

- https://github.com/infosec-au/altdns - **Subdomain discovery through alterations and permutations**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/infosec-au/altdns?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/infosec-au/altdns?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/infosec-au/altdns?style=for-the-badge)

- https://github.com/FeeiCN/ESD - **Enumeration sub domains tool,based on AsyncIO and non-repeating dict**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/FeeiCN/ESD?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/FeeiCN/ESD?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/FeeiCN/ESD?style=for-the-badge)

- https://github.com/UnaPibaGeek/ctfr - **Abusing certificate transparency logs for getting HTTPS websites subdomains**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/UnaPibaGeek/ctfr?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/UnaPibaGeek/ctfr?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/UnaPibaGeek/ctfr?style=for-the-badge)

- https://github.com/giovanifss/Dumb - **Dumain Bruteforcer, a fast and flexible domain bruteforcer**

> ![](https://img.shields.io/badge/MainLanguage-Haskell-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/giovanifss/Dumb?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/giovanifss/Dumb?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/giovanifss/Dumb?style=for-the-badge)

- https://github.com/OWASP/Amass - **In-depth Attack Surface Mapping and Asset Discovery**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/OWASP/Amass?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/OWASP/Amass?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/OWASP/Amass?style=for-the-badge)

- https://github.com/Ice3man543/subfinder - **A subdomain discovery tool which has a simple modular architecture and has been aimed as a successor to sublist3r project**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/Ice3man543/subfinder?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/Ice3man543/subfinder?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/Ice3man543/subfinder?style=for-the-badge)

- https://github.com/Ice3man543/SubOver - **A powerful subdomain takeover tool**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/Ice3man543/SubOver?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/Ice3man543/SubOver?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/Ice3man543/SubOver?style=for-the-badge)

- https://github.com/janniskirschner/horn3t - **Powerful Visual Subdomain Enumeration**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/janniskirschner/horn3t?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/janniskirschner/horn3t?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/janniskirschner/horn3t?style=for-the-badge)

- https://github.com/yunxu1/dnsub - **A high concurrency and cross platform subdomain scanner based on Golang**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/yunxu1/dnsub?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/yunxu1/dnsub?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/yunxu1/dnsub?style=for-the-badge)

- https://github.com/shmilylty/OneForAll - **An ultimate subdomains scanner integrated multiple subdomain scanning tools**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/shmilylty/OneForAll?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/shmilylty/OneForAll?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/shmilylty/OneForAll?style=for-the-badge)

- https://github.com/knownsec/ksubdomain - **A stateless and cross-platform subdomain enumeration tool, speed up to 30w/s on Mac and Windows, and 160w/s on Linux**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/knownsec/ksubdomain?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/knownsec/ksubdomain?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/knownsec/ksubdomain?style=for-the-badge)

- https://github.com/gwen001/github-subdomains - **Find subdomains on GitHub**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/gwen001/github-subdomains?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/gwen001/github-subdomains?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/gwen001/github-subdomains?style=for-the-badge)

- https://github.com/bit4woo/domain_hunter_pro - **Domain finder and Targets management, automated information collection, integrated with burpsuite**

> ![](https://img.shields.io/badge/MainLanguage-Java-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/bit4woo/domain_hunter_pro?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/bit4woo/domain_hunter_pro?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/bit4woo/domain_hunter_pro?style=for-the-badge)

- https://github.com/m4ll0k/takeover - **Sub-Domain TakeOver Vulnerability Scanner**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/m4ll0k/takeover?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/m4ll0k/takeover?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/m4ll0k/takeover?style=for-the-badge)

- https://github.com/v4d1/Dome - **Active and/or passive scan to obtain subdomains and search for open port**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/v4d1/Dome?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/v4d1/Dome?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/v4d1/Dome?style=for-the-badge)

- https://github.com/cramppet/regulator - **Automated subdomain enumeration tool by learning of regexes for DNS discovery**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/cramppet/regulator?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/cramppet/regulator?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/cramppet/regulator?style=for-the-badge)

- https://github.com/hadriansecurity/subwiz - **A lightweight GPT model, trained to discover subdomains.**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/hadriansecurity/subwiz?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/hadriansecurity/subwiz?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/hadriansecurity/subwiz?style=for-the-badge)


### Database SQL Injection Vulnerability or Brute Force

- https://github.com/0xbug/SQLiScanner - **A SQLi vulnerability scanner via SQLMAP and Charles**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/0xbug/SQLiScanner?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/0xbug/SQLiScanner?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/0xbug/SQLiScanner?style=for-the-badge)

- https://github.com/stamparm/DSSS - **A SQLi vulnerability scanner with 99 lines of code**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/stamparm/DSSS?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/stamparm/DSSS?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/stamparm/DSSS?style=for-the-badge)

- https://github.com/youngyangyang04/NoSQLAttack  - **A SQLi vulnerability scanner for mongoDB**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/youngyangyang04/NoSQLAttack?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/youngyangyang04/NoSQLAttack?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/youngyangyang04/NoSQLAttack?style=for-the-badge)

- https://github.com/Neohapsis/bbqsql - **A blind SQLi vulnerability scanner**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/Neohapsis/bbqsql?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/Neohapsis/bbqsql?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/Neohapsis/bbqsql?style=for-the-badge)

- https://github.com/NetSPI/PowerUpSQL - **A SQLi vulnerability scanner with Powershell script**

> ![](https://img.shields.io/badge/MainLanguage-PowerShell-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/NetSPI/PowerUpSQL?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/NetSPI/PowerUpSQL?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/NetSPI/PowerUpSQL?style=for-the-badge)

- https://github.com/WhitewidowScanner/whitewidow - **Another SQL vulnerability scanner**

> ![](https://img.shields.io/badge/MainLanguage-Ruby-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/WhitewidowScanner/whitewidow?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/WhitewidowScanner/whitewidow?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/WhitewidowScanner/whitewidow?style=for-the-badge)

- https://github.com/stampery/mongoaudit - **A powerful MongoDB auditing and pentesting tool**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/stampery/mongoaudit?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/stampery/mongoaudit?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/stampery/mongoaudit?style=for-the-badge)

- https://github.com/torque59/Nosql-Exploitation-Framework - **A Python framework For NoSQL scanning and exploitation**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/stampery/mongoaudit?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/stampery/mongoaudit?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/stampery/mongoaudit?style=for-the-badge)

- https://github.com/missDronio/blindy - **Simple script to automate brutforcing blind sql injection vulnerabilities**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/missDronio/blindy?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/missDronio/blindy?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/missDronio/blindy?style=for-the-badge)

- https://github.com/fengxuangit/Fox-scan - **A initiative and passive SQL injection vulnerable test tools**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/fengxuangit/Fox-scan?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/fengxuangit/Fox-scan?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/fengxuangit/Fox-scan?style=for-the-badge)

- https://github.com/JohnTroony/Blisqy - **Exploit time-based blind-SQL injection in HTTP-Headers**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/JohnTroony/Blisqy?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/JohnTroony/Blisqy?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/JohnTroony/Blisqy?style=for-the-badge)

- https://github.com/ron190/jsql-injection - **A lightweight application used to find database information from a distant server**

> ![](https://img.shields.io/badge/MainLanguage-Java-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/ron190/jsql-injection?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/ron190/jsql-injection?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/ron190/jsql-injection?style=for-the-badge)

- https://github.com/Hadesy2k/sqliv - **Massive SQL injection vulnerability scanner**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/Hadesy2k/sqliv?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/Hadesy2k/sqliv?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/Hadesy2k/sqliv?style=for-the-badge)

- https://github.com/s0md3v/sqlmate - **A friend of SQLmap which will do what you always expected from SQLmap**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/s0md3v/sqlmate?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/s0md3v/sqlmate?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/s0md3v/sqlmate?style=for-the-badge)

- https://github.com/m8r0wn/enumdb  - **MySQL and MSSQL brute force and post exploitation tool**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/m8r0wn/enumdb?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/m8r0wn/enumdb?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/m8r0wn/enumdb?style=for-the-badge)

- https://github.com/tariqhawis/injectbot  - **A web-based, easy-to-use, SQL injection scanner and exploiter tool**

> ![](https://img.shields.io/badge/MainLanguage-PHP-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/tariqhawis/injectbot?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/tariqhawis/injectbot?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/tariqhawis/injectbot?style=for-the-badge)


### Weak Usernames or Passwords Enumeration For Web

- https://github.com/lijiejie/htpwdScan  - **A python HTTP weak pass scanner**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/lijiejie/htpwdScan?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/lijiejie/htpwdScan?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/lijiejie/htpwdScan?style=for-the-badge)

- https://github.com/netxfly/crack_ssh - **SSH, Redis, mongoDB weak password bruteforcer**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/netxfly/crack_ssh?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/netxfly/crack_ssh?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/netxfly/crack_ssh?style=for-the-badge)

- https://github.com/shengqi158/weak_password_detect - **A python HTTP weak password scanner**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/shengqi158/weak_password_detect?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/shengqi158/weak_password_detect?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/shengqi158/weak_password_detect?style=for-the-badge)

- https://github.com/s0md3v/Blazy - **a modern login bruteforcer which also tests for CSRF, Clickjacking, Cloudflare and WAF**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/s0md3v/Blazy?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/s0md3v/Blazy?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/s0md3v/Blazy?style=for-the-badge)

- https://github.com/MooseDojo/myBFF - **Web application brute force framework,supports Citrix Gateway,CiscoVPN and so on**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/MooseDojo/myBFF?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/MooseDojo/myBFF?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/MooseDojo/myBFF?style=for-the-badge)

- https://github.com/TideSec/web_pwd_common_crack - **A common web weak_password cracking script,can detect batches of management backgrounds without verification codes**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/TideSec/web_pwd_common_crack?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/TideSec/web_pwd_common_crack?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/TideSec/web_pwd_common_crack?style=for-the-badge)


### IoT Hardware Automated Audit

- https://github.com/rapid7/IoTSeeker - **Weak-password IoT devices scanner**

> ![](https://img.shields.io/badge/MainLanguage-Perl-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/rapid7/IoTSeeker?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/rapid7/IoTSeeker?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/rapid7/IoTSeeker?style=for-the-badge)

- https://github.com/shodan-labs/iotdb - **IoT Devices scanner via nmap**

> ![](https://img.shields.io/badge/MainLanguage-XML-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/shodan-labs/iotdb?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/shodan-labs/iotdb?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/shodan-labs/iotdb?style=for-the-badge)

- https://github.com/googleinurl/RouterHunterBR - **Testing vulnerabilities in devices and routers connected to the Internet**

> ![](https://img.shields.io/badge/MainLanguage-PHP-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/googleinurl/RouterHunterBR?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/googleinurl/RouterHunterBR?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/googleinurl/RouterHunterBR?style=for-the-badge)

- https://github.com/scu-igroup/telnet-scanner - **Weak telnet password scanner based on password enumeration**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/scu-igroup/telnet-scanner?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/scu-igroup/telnet-scanner?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/scu-igroup/telnet-scanner?style=for-the-badge)

- https://github.com/viraintel/OWASP-Nettacker - **Network information gathering vulnerability scanner,most useful to scan IoT**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/viraintel/OWASP-Nettacker?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/viraintel/OWASP-Nettacker?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/viraintel/OWASP-Nettacker?style=for-the-badge)

- https://github.com/threat9/routersploit - **Exploitation Framework for embedded Devices,such as router**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/threat9/routersploit?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/threat9/routersploit?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/threat9/routersploit?style=for-the-badge)

- https://github.com/w3h/icsmaster/tree/master/nse - **Digital bond's ICS enumeration tools**

> ![](https://img.shields.io/badge/MainLanguage-NSE-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/w3h/icsmaster?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/w3h/icsmaster?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/w3h/icsmaster?style=for-the-badge)

- https://github.com/firmianay/firmeye - **An IDA plug-in, based on sensitive function parameter backtracking to assist in vulnerability mining**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/firmianay/firmeye?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/firmianay/firmeye?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/firmianay/firmeye?style=for-the-badge)

- https://github.com/bahaabdelwahed/st - **An advanced security tool engineered specifically to scrutinize and detect threats within the intricate protocols utilized by IoT (Internet of Things) devices**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/bahaabdelwahed/st?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/bahaabdelwahed/st?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/bahaabdelwahed/st?style=for-the-badge)

- https://github.com/0x4D31/salt-scanner - **Linux vulnerability scanner based on Salt Open and vulners audit API, with Slack notifications and JIRA integration**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/0x4D31/salt-scanner?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/0x4D31/salt-scanner?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/0x4D31/salt-scanner?style=for-the-badge)

- https://github.com/vulmon/Vulmap - **Local vulnerability scanning programs for Windows and Linux operating systems**

> ![](https://img.shields.io/badge/MainLanguage-PowerShell-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/vulmon/Vulmap?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/vulmon/Vulmap?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/vulmon/Vulmap?style=for-the-badge)


### Mutiple types of Cross-site scripting Detection

- https://github.com/0x584A/fuzzXssPHP - **A very simple reflected XSS scanner supports GET/POST**

> ![](https://img.shields.io/badge/MainLanguage-PHP-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/0x584A/fuzzXssPHP?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/0x584A/fuzzXssPHP?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/0x584A/fuzzXssPHP?style=for-the-badge)

- https://github.com/chuhades/xss_scan - **Reflected XSS scanner**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/chuhades/xss_scan?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/chuhades/xss_scan?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/chuhades/xss_scan?style=for-the-badge)

- https://github.com/BlackHole1/autoFindXssAndCsrf - **A plugin for browser that checks automatically whether a page haves XSS and CSRF vulnerabilities**

> ![](https://img.shields.io/badge/MainLanguage-JavaScript-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/BlackHole1/autoFindXssAndCsrf?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/BlackHole1/autoFindXssAndCsrf?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/BlackHole1/autoFindXssAndCsrf?style=for-the-badge)

- https://github.com/shogunlab/shuriken - **XSS command line tool for testing lists of XSS payloads on web apps**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/shogunlab/shuriken?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/shogunlab/shuriken?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/shogunlab/shuriken?style=for-the-badge)

- https://github.com/s0md3v/XSStrike - **Fuzz and bruteforce parameters for XSS, WAFs detect and bypass**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/s0md3v/XSStrike?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/s0md3v/XSStrike?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/s0md3v/XSStrike?style=for-the-badge)

- https://github.com/stamparm/DSXS - **A fully functional cross-site scripting vulnerability scanner,supporting GET and POST parameters,and written in under 100 lines of code**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/stamparm/DSXS?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/stamparm/DSXS?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/stamparm/DSXS?style=for-the-badge)

- https://github.com/fcavallarin/domdig - **DOM XSS scanner for Single Page Applications**

> ![](https://img.shields.io/badge/MainLanguage-Node.js-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/fcavallarin/domdig?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/fcavallarin/domdig?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/fcavallarin/domdig?style=for-the-badge)

- https://github.com/lwzSoviet/NoXss - **Faster reflected-xss and dom-xss scanner based on Phantomjs**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/lwzSoviet/NoXss?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/lwzSoviet/NoXss?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/lwzSoviet/NoXss?style=for-the-badge)

- https://github.com/pwn0sec/PwnXSS - **A powerful XSS scanner made in python 3.7**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/pwn0sec/PwnXSS?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/pwn0sec/PwnXSS?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/pwn0sec/PwnXSS?style=for-the-badge)

- https://github.com/hahwul/dalfox - **Parameter Analysis and XSS Scanning tool based on golang**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/hahwul/dalfox?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/hahwul/dalfox?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/hahwul/dalfox?style=for-the-badge)


### Enterprise sensitive information Leak Scan

- https://github.com/x0day/Multisearch-v2 - **Enterprise assets collector based on search engine**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/x0day/Multisearch-v2?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/x0day/Multisearch-v2?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/x0day/Multisearch-v2?style=for-the-badge)

- https://github.com/Ekultek/Zeus-Scanner - **An advanced dork searching tool that is capable of finding IP address /URL blocked by search engine,and can run sqlmap and nmap scans on the URL's**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/Ekultek/Zeus-Scanner?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/Ekultek/Zeus-Scanner?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/Ekultek/Zeus-Scanner?style=for-the-badge)

- https://github.com/metac0rtex/GitHarvester - **Used for harvesting information from GitHub**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/metac0rtex/GitHarvester?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/metac0rtex/GitHarvester?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/metac0rtex/GitHarvester?style=for-the-badge)

- https://github.com/repoog/GitPrey - **Searching sensitive files and contents in GitHub**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/repoog/GitPrey?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/repoog/GitPrey?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/repoog/GitPrey?style=for-the-badge)

- https://github.com/0xbug/Hawkeye - **Github leak scan for enterprise**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/0xbug/Hawkeye?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/0xbug/Hawkeye?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/0xbug/Hawkeye?style=for-the-badge)

- https://github.com/UnkL4b/GitMiner - **Advanced search tool and automation in Github**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/UnkL4b/GitMiner?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/UnkL4b/GitMiner?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/UnkL4b/GitMiner?style=for-the-badge)

- https://github.com/dxa4481/truffleHog - **Searches high entropy strings through git repositories**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/dxa4481/truffleHog?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/dxa4481/truffleHog?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/dxa4481/truffleHog?style=for-the-badge)

- https://github.com/1N3/Goohak - **Automatically launch Google hacking queries against a target domain**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/1N3/Goohak?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/1N3/Goohak?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/1N3/Goohak?style=for-the-badge)

- https://github.com/UKHomeOffice/repo-security-scanner - **CLI tool that finds secrets accidentally committed to a git repo, eg passwords, private keys**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/UKHomeOffice/repo-security-scanner?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/UKHomeOffice/repo-security-scanner?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/UKHomeOffice/repo-security-scanner?style=for-the-badge)

- https://github.com/FeeiCN/GSIL - **Github sensitive information leakage scan**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/FeeiCN/GSIL?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/FeeiCN/GSIL?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/FeeiCN/GSIL?style=for-the-badge)

- https://github.com/MiSecurity/x-patrol - **Github leaked patrol**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/MiSecurity/x-patrol?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/MiSecurity/x-patrol?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/MiSecurity/x-patrol?style=for-the-badge)

- https://github.com/anshumanbh/git-all-secrets - **A tool to capture all the git secrets by leveraging multiple open source git searching tools**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/anshumanbh/git-all-secrets?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/anshumanbh/git-all-secrets?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/anshumanbh/git-all-secrets?style=for-the-badge)

- https://github.com/VKSRC/Github-Monitor - **Github sensitive information leakage monitor by vipkid SRC**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/FeeiCN/GSIL?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/FeeiCN/GSIL?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/FeeiCN/GSIL?style=for-the-badge)

- https://github.com/eth0izzle/shhgit - **A docker and web based monitor for finding secrets and sensitive files across GitHub**

> ![](https://img.shields.io/badge/MainLanguage-Go-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/eth0izzle/shhgit?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/eth0izzle/shhgit?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/eth0izzle/shhgit?style=for-the-badge)

- https://github.com/SAP/credential-digger - **A GitHub scanning tool that identifies hardcoded credentials, filtering the false positive data through machine learning models**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/SAP/credential-digger?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/SAP/credential-digger?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/SAP/credential-digger?style=for-the-badge)

- https://github.com/sdushantha/dora - **Find exposed API keys based on RegEx and get exploitation methods for some of keys that are found**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/sdushantha/dora?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/sdushantha/dora?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/sdushantha/dora?style=for-the-badge)


### Malware Detection

- https://github.com/he1m4n6a/findWebshell  - **Simple webshell detector**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/he1m4n6a/findWebshell?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/he1m4n6a/findWebshell?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/he1m4n6a/findWebshell?style=for-the-badge)

- https://github.com/nbs-system/php-malware-finder - **An awesome tool to detect potentially malicious PHP files**

> ![](https://img.shields.io/badge/MainLanguage-PHP-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/nbs-system/php-malware-finder?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/nbs-system/php-malware-finder?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/nbs-system/php-malware-finder?style=for-the-badge)

- https://github.com/emposha/PHP-Shell-Detector - **Helps you find and identify PHP/Perl/Asp/Aspx shells**

> ![](https://img.shields.io/badge/MainLanguage-PHP-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/emposha/PHP-Shell-Detector?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/emposha/PHP-Shell-Detector?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/emposha/PHP-Shell-Detector?style=for-the-badge)

- https://github.com/erevus-cn/scan_webshell - **Simple webshell detector**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/erevus-cn/scan_webshell?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/erevus-cn/scan_webshell?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/erevus-cn/scan_webshell?style=for-the-badge)

- https://github.com/emposha/Shell-Detector - **A application that helps you find and identify PHP/Perl/Asp/Aspx shells**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/emposha/Shell-Detector?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/emposha/Shell-Detector?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/emposha/Shell-Detector?style=for-the-badge)


### Vulnerability Assessment for Middleware

- https://github.com/ring04h/wyportmap - **Target port scanning + system service fingerprint recognition**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/ring04h/wyportmap?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/ring04h/wyportmap?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/ring04h/wyportmap?style=for-the-badge)

- https://github.com/ring04h/weakfilescan - **Dynamic multi - thread sensitive information leak detection tool**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/ring04h/wyportmap?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/ring04h/wyportmap?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/ring04h/wyportmap?style=for-the-badge)

- https://github.com/EnableSecurity/wafw00f - **Identify and fingerprint Web Application Firewall**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/ring04h/weakfilescan?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/ring04h/weakfilescan?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/ring04h/weakfilescan?style=for-the-badge)

- https://github.com/rbsec/sslscan - **Tests SSL/TLS enabled services to discover supported cipher suites**

> ![](https://img.shields.io/badge/MainLanguage-C-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/rbsec/sslscan?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/rbsec/sslscan?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/rbsec/sslscan?style=for-the-badge)

- https://github.com/TideSec/TideFinger - **Web fingerprint identification tool, more fingerprint database, more detection methods**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/TideSec/TideFinger?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/TideSec/TideFinger?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/TideSec/TideFinger?style=for-the-badge)

- https://github.com/TideSec/FuzzScanner - **Comprehensive web information collection platform, easy to deploy, versatile and practical**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/TideSec/FuzzScanner?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/TideSec/FuzzScanner?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/TideSec/FuzzScanner?style=for-the-badge)

- https://github.com/urbanadventurer/whatweb - **Website fingerprinter**

> ![](https://img.shields.io/badge/MainLanguage-Ruby-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/urbanadventurer/whatweb?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/urbanadventurer/whatweb?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/urbanadventurer/whatweb?style=for-the-badge)

- https://github.com/tanjiti/FingerPrint - **Another website fingerprinter**

> ![](https://img.shields.io/badge/MainLanguage-Perl-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/tanjiti/FingerPrint?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/tanjiti/FingerPrint?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/tanjiti/FingerPrint?style=for-the-badge)

- https://github.com/nanshihui/Scan-T - **A new spider based on Python with more function including Network fingerprint search**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/nanshihui/Scan-T?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/nanshihui/Scan-T?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/nanshihui/Scan-T?style=for-the-badge)

- https://github.com/OffensivePython/Nscan - **Fast internet-wide scanner**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/OffensivePython/Nscan?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/OffensivePython/Nscan?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/OffensivePython/Nscan?style=for-the-badge)

- https://github.com/ywolf/F-NAScan - **Scanning a network asset information script**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/ywolf/F-NAScan?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/ywolf/F-NAScan?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/ywolf/F-NAScan?style=for-the-badge)

- https://github.com/maurosoria/dirsearch - **Web path scanner**

> ![](https://img.shields.io/badge/MainLanguage-Python-blue?style=for-the-badge)  ![GitHub last commit](https://img.shields.io/github/last-commit/maurosoria/dirsearch?style=for-the-badge) ![GitHub stars](https://img.shields.io/github/stars/maurosoria/dirsearch?style=for-the-badge)  ![GitHub](https://img.shields.io/github/license/mau