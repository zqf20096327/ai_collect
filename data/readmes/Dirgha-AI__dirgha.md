<h1 align="center">Dirgha</h1>

<p align="center"><strong>Open-source local coding agent, governance gate, and open GPU compute router for developers, enterprises, and robotics teams.</strong></p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-blue.svg" alt="License: Apache-2.0"></a>
  <a href="https://github.com/Dirgha-AI/dirgha/actions/workflows/ci.yml"><img src="https://github.com/Dirgha-AI/dirgha/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://www.npmjs.com/package/@dirgha/code"><img src="https://img.shields.io/npm/dt/@dirgha/code.svg?label=npm%20downloads" alt="npm downloads"></a>
  <a href="https://modelcontextprotocol.io"><img src="https://img.shields.io/badge/protocol-MCP-purple.svg" alt="Protocol: MCP"></a>
</p>

Dirgha is an Apache-2.0 agent harness that runs on your own machine with any model provider or local Ollama model. Solo developers get a fast terminal coding agent with zero governance overhead. Security and platform teams can turn on signed policy rules, secret scanning, data-residency GPU routing, and human approvals from the same binary.

```bash
git clone https://github.com/Dirgha-AI/dirgha.git && cd dirgha
npm ci && npm run build
node bin/dirgha.mjs
```

---

## Why Dirgha exists

Teams adopting AI coding and automation agents keep hitting the same walls:

- **Single-vendor lock-in.** Most hosted coding tools tie you to one model provider, store transcripts on third-party servers, and break when you want local or air-gapped models.
- **All-or-nothing security.** Solo builders abandon tools that nag them on every edit, while enterprises cannot approve agents that run unchecked shell commands or leak credentials into commits.
- **Fragmented GPU and web tooling.** Moving from coding to GPU training or live web research usually means bolting on ad-hoc scripts with no spend cap or jurisdiction check.
- **No path from simulation to physical hardware.** Robotics teams end up maintaining separate stacks for code generation, MuJoCo testing, and hardware sign-off.

Dirgha puts these pieces behind one open-source CLI, one local memory store, and one modular safety boundary.

## Progressive governance: fast for solo builders, lockable for enterprises

Governance in Dirgha is strictly opt-in for individuals and lockable for organizations.

| Profile | LOKAHI Policy Gate | Arniko Secret & Code Scan | Open GPU Cloud Market | Best for |
|---|---|---|---|---|
| `developer` *(default)* | Off | Off | On | Solo developers who want zero friction |
| `safe-dev` | Advisory (log only) | Off | On | Developers who want visibility without blocks |
| `team` | Enforced (fail-closed) | Pre-commit scan | On | Engineering teams guarding shared repositories |
| `enterprise` | Enforced + signed manifests | Pre-commit & file-write guard | Residency & budget capped | Regulated organizations needing audit evidence |
| `robotics` | Enforced + S2 human approvals | On | Residency & budget capped | Physical-AI and MuJoCo simulation pipelines |

Switch profiles per run (`--profile team`, `--lokahi`, `--arniko`), turn modules off (`--no-lokahi`, `--no-arniko`, `--no-gpu`), or deploy a read-only organization policy lock at `/etc/dirgha/policy.json` (or `DIRGHA_ORG_POLICY`) so managed machines fail closed and reject bypass flags.

## What you can do with Dirgha

### For developers
- **Code with any model:** Connect your own API keys (Anthropic, OpenAI, Gemini, OpenRouter, DeepSeek, Groq, Mistral, NVIDIA NIM, and any OpenAI-compatible server) or run completely offline with Ollama and llama.cpp.
- **Work locally with real tools:** Read and edit files, run shell commands, search code with grep/glob and LSP lookups, manage git branches, run parallel agents in isolated git worktrees (`dirgha fleet`), and keep searchable session memory in SQLite under `~/.dirgha/`.
- **Search the web cleanly via Exa MCP:** Official Exa MCP (`web_search_exa`, `web_fetch_exa`) is registered in `.mcp.json` out of the box—keyless at Exa's free tier, with no wrapper code to maintain. See [docs/exa-search.md](docs/exa-search.md).
- **Connect any MCP server:** Load local stdio or remote Streamable HTTP/SSE MCP servers, and expose Dirgha's own 24-tool Rust kernel over MCP (`dirgha-native-host --mcp`).

### For enterprises and security teams
- **Enforce signed tool boundaries (LOKAHI):** Sign tool and argument policies with RFC-8785 canonical JSON and Ed25519 keys (`dirgha policy keygen|init|sign|verify`), require dual-control S2 approvals for irreversible actions (`dirgha policy approve`), and export auditor-ready compliance evidence packs (`dirgha policy evidence`).
- **Catch leaked secrets before they land (Arniko):** Run `dirgha scan --builtin --sarif` offline or orchestrate locally installed `gitleaks`, `semgrep`, and `trivy` binaries to emit OASIS SARIF v2.1.0 reports for GitHub, GitLab, and Azure DevOps. Missing scanner CLIs are reported honestly—never faked.
- **Route GPU jobs across an Open GPU Cloud Market:** Find the cheapest compliant GPU across RunPod, Vast.ai, Spheron, Akash, and certified third-party clouds (`dirgha gpu find`), enforce data-residency jurisdictions and hourly caps, onboard new cloud providers via `specs/GPU_PROVIDER_SCHEMA.json`, and export RFC-4180 finance chargeback CSVs (`dirgha gpu chargeback --csv`).
- **Deploy as a private sovereign stack:** Run the multi-tab Governance, GPU Market, Arniko SARIF, and Physical AI Control Plane locally (`npm run dev`), on Docker Compose (`docker-compose.private-stack.yml`), or on Kubernetes (`deploy/k8s/dirgha-enterprise.yaml`).

### For robotics and physical-AI teams
- **Evaluate in MuJoCo:** Run seeded rollouts (`dirgha eval-robot`) with confidence intervals, failure categorization, and HTML replays, or drive simulations step by step over MCP.
- **Gate physical actions:** Actions marked S2 require an explicit Ed25519 human approval within a 45-second window; silence is treated as a refusal.

## Quick start

**Requirements:** Node.js 22 or later. Rust stable is optional and only needed if you compile the native kernel from source.

### 1. Install and build
```bash
git clone https://github.com/Dirgha-AI/dirgha.git
cd dirgha
npm ci
npm run build
node bin/dirgha.mjs doctor
```

### 2. Configure a model key or local Ollama
```bash
# Bring your own API key (stored locally in ~/.dirgha/keys.json)
node bin/dirgha.mjs keys set OPENROUTER_API_KEY sk-or-...

# Or run offline with Ollama
ollama pull qwen2.5-coder:7b
node bin/dirgha.mjs -m ollama/qwen2.5-coder:7b
```

### 3. Run everyday workflows
```bash
# Interactive coding session (zero governance friction)
node bin/dirgha.mjs

# One-shot task or scripted pipe
node bin/dirgha.mjs "explain src/kernel/agent-loop.ts"
echo "summarise the last 5 commits" | node bin/dirgha.mjs --print

# Verify a change only succeeds when tests pass
node bin/dirgha.mjs verify "fix parser edge case" --accept "npm test"

# Run with strict policy enforcement and secret scanning
node bin/dirgha.mjs --profile enterprise "audit deployment scripts"
node bin/dirgha.mjs scan --builtin --sarif > arniko.sarif

# Find compliant GPUs or scaffold a third-party GPU provider manifest
node bin/dirgha.mjs gpu find --min-vram=24 --jurisdiction=EU --compliance=soc2,gdpr
node bin/dirgha.mjs gpu init-manifest --id=my-cloud --name="My Sovereign GPU" --endpoint=https://gpu.example/v1

# Verify live Exa MCP web search connectivity
npm run verify:exa

# Launch the local Enterprise Control Plane (http://localhost:3000)
npm run dev
```

## Architecture at a glance

```text
             you · CI scripts · external MCP clients
                               │
                  ┌────────────▼────────────┐
                  │  dirgha (bin/dirgha.mjs) │
                  └──────┬───────────┬──────┘
                         │           │
         ┌───────────────▼──┐     ┌──▼────────────────────────┐
         │ TypeScript agent │     │ Rust native kernel        │
         │ loop, tools, TUI │     │ 24 MCP tools, ledger,     │
         │ GPU router, scan │     │ MuJoCo harness, cockpit   │
         └───────┬──────────┘     └──┬────────────────────────┘
                 │                   │
                 └─────────┬─────────┘
                           ▼
         Modular Governance Layer (opt-in or org-locked)
         LOKAHI WASM gate · signed policies · Arniko hooks
                           │
                           ▼
   files · shell · git · Exa MCP · GPU clouds · MuJoCo simulation
```

## Honest scope and current limitations

We would rather tell you what is production-ready and what is still a demo than waste your time:

- **Core shipping wedge:** The TypeScript coding agent, multi-provider BYOK/Ollama routing, git-worktree fleet runs, the TypeScript policy gateway, LOKAHI policy signing/conformance/evidence tools, Arniko built-in secret scanner + SARIF export, and Exa MCP integration.
- **Gateway engines:** `dirgha gateway` and `dirgha proxy` always use the TypeScript gateway. The native Rust gateway is an experimental R&D prototype that does not proxy upstream LLM traffic; it requires an explicit opt-in flag.
- **Experimental preview / simulation tracks:** The Open GPU Cloud Market router/certifier, enterprise Control Plane/cockpit, Docker/Kubernetes private-stack templates, and physical-AI/robotics tooling are available for evaluation but are not part of the core production support claim.
- **Simulated demo tools (clearly labeled):** Six robotics/hardware MCP tools—`dirgha_policy_infer`, `physical_ai_vla_infer`, `hf_lerobot_dataset_sync`, `hardware_cad_pcb_generate`, `hardware_vendor_quote_order`, and `robotics_skill_invoke`—demonstrate the interface without calling external hardware vendors and always return `"simulated": true`.
- **Independent audit pending:** Dirgha has not yet undergone a third-party penetration test. Treat it as defense-in-depth alongside your OS, container, and network isolation.

## Common questions

**Does Dirgha force LOKAHI or security gates on solo developers?**
No. The default `developer` profile starts with LOKAHI and Arniko turned off. Governance only activates when you pass a profile/flag or when an organization installs `/etc/dirgha/policy.json`.

**Where do my API keys, code, and logs go?**
Keys live in `~/.dirgha/keys.json` or environment variables and are sent only to the model or GPU provider you choose. Session history and audit logs stay on disk under `~/.dirgha/`. Usage telemetry is off by default.

**How can a new GPU cloud provider join the Open GPU Cloud Market?**
Implement the lightweight HTTPS contract in `specs/GPU_PROVIDER_SCHEMA.json` (or adapt the starter server in `examples/gpu-provider-starter/`), generate a manifest with `dirgha gpu init-manifest`, and certify it with `dirgha gpu certify <manifest.json> --probe`.

**How do enterprises align Dirgha with EU AI Act, ISO/IEC 42001, NIST AI RMF, or DPDP/GDPR?**
Use the `enterprise` profile with a read-only `/etc/dirgha/policy.json` lock, sign tool/argument manifests with `dirgha policy sign`, restrict GPU jurisdictions via `allowedJurisdictions`, export SARIF findings via `dirgha scan`, and generate signed auditor packs with `dirgha policy evidence`.

## Documentation

| Guide | What it covers |
|---|---|
| [Getting started](docs/getting-started.md) | Installation, model setup, first tasks |
| [Enterprise stack](docs/ENTERPRISE_STACK.md) | Profiles, Org Policy Lock, compliance alignment, commercial tiers |
| [Open GPU Cloud Market](docs/gpu-cloud-market.md) | Multi-cloud routing, chargeback CSVs, partner provider certification |
| [Exa search](docs/exa-search.md) | Keyless web search and clean page fetch via Exa MCP |
| [Safety model](docs/safety.md) | Fail-closed WASM gate, S2 approvals, signed ledger |
| [MCP tools](docs/mcp-tools.md) | Reference for all 24 kernel MCP tools |
| [Kubernetes deployment](deploy/k8s/README.md) | Hardened private-stack deployment for EKS, GKE, AKS, and on-prem |
| [Robotics](docs/robotics.md) | MuJoCo evaluation and simulation workflows |
| [Local models](docs/local-models.md) | Running offline with Ollama and llama.cpp |
| [Fleet](docs/tutorials/fleet.md) and [Sub-agents](docs/tutorials/subagents.md) | Parallel git-worktree agents and task delegation |
| [Extensions](docs/extensions.md) | Skills and ESM plugin API |

## For AI agents and crawlers

- **[llms.txt](llms.txt):** Canonical plain-text index of Dirgha's architecture, CLI commands, and docs for LLM retrieval.
- **[AGENTS.md](AGENTS.md):** Exact build, test, and fail-closed safety rules for coding agents contributing to this repository.
- **MCP interface:** Run `dirgha-native-host --mcp` (stdio) and send `initialize` followed by `tools/list`. Respect `"simulated": true` on demo tool responses.

## The Dirgha AI open stack

Each layer works standalone or together:

| Role | Project | Purpose | Licence |
|---|---|---|---|
| **Run** | **Dirgha** | Local agent harness, Open GPU Cloud Market, MCP kernel | Apache-2.0 |
| **Enforce** | [LOKAHI](https://github.com/Dirgha-AI/lokahi) | Signed boundary manifests, fail-closed capability gate, conformance suite | Apache-2.0 |
| **Scan** | [Arniko](https://github.com/Dirgha-AI/arniko) | Secret, SAST, and dependency scanning merged into SARIF v2.1.0 | Apache-2.0 |
| **Assess** | [Ahimsa AI](https://github.com/Dirgha-AI/ahimsa-ai) | Harm/benefit risk assessment that compiles into LOKAHI rules | MIT |

## Contributing, security and licence

- **Enterprise pilots & support:** Open an [issue](https://github.com/Dirgha-AI/dirgha/issues/new) titled `"Pilot"` to discuss custom rule packs, private-stack rollouts, or GPU partner certification.
- **Contributing:** Pull requests are welcome. Sign off commits (`git commit -s`) under the [Developer Certificate of Origin](https://developercertificate.org/). See [CONTRIBUTORS.md](CONTRIBUTORS.md).
- **Security:** Report vulnerabilities privately to `security@dirgha.ai`. See [SECURITY.md](SECURITY.md).
- **Licence:** Apache-2.0 ([LICENSE](LICENSE), [NOTICE](NOTICE)). Copyright 2026 [Salik Shah](https://salikshah.com) / Dirgha AI. Third-party attributions live in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
