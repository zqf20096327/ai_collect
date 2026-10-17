# ios-reverse-skills

> Multi-LLM iOS reverse-engineering toolkit. Drives the same **14-phase**
> workflow (Phase 0 → Phase 13: triage → decryption → static analysis →
> dynamic instrumentation → vulnerability audit → patching) from
> **Claude Opus / Code**, **Cursor**, **Qwen Coder**, **MiniMax**,
> **OpenAI Codex / GPT-5**, **Aider**, **Cline** — or any LLM with a shell
> tool.

A **fork, generalization and significant expansion** of
[`incogbyte/iOS-reverse-engineering-claude-skill`](https://github.com/incogbyte/iOS-reverse-engineering-claude-skill)
(public domain). The original ships as a Claude-Code-only skill with a
10-phase pipeline; this repo:

- Refactors the workflow into a model-agnostic
  [`skill/METHODOLOGY.md`](skill/METHODOLOGY.md) and **adds 4 new phases**
  (decryption, dynamic instrumentation, vulnerability-class audit, binary
  patching).
- Keeps every original script and reference doc intact; **adds 6 new bash
  scripts, 2 new Ghidra scripts and 21 new reference docs** based on:
  - the classical book *iOS App Reverse Engineering*
    ([`iosre/iOSAppReverseEngineering`](https://github.com/iosre/iOSAppReverseEngineering))
  - the Mach-O / Ghidra / Frida primer
    ([`GhidraEnjoyr/iOS-Reverse-Engineering`](https://github.com/GhidraEnjoyr/iOS-Reverse-Engineering))
  - the 5-module course
    ([`ivRodriguezCA/RE-iOS-Apps`](https://github.com/ivRodriguezCA/RE-iOS-Apps))
  - the obfuscation / swizzling reference
    ([`LaurieWired/iOS_Reverse_Engineering`](https://github.com/LaurieWired/iOS_Reverse_Engineering))
  - the OWASP Mobile Application Security Testing Guide
    ([`OWASP/mastg`](https://github.com/OWASP/mastg))
  - kernel-adjacent notes from [`kpwn/iOSRE`](https://github.com/kpwn/iOSRE)
    and [`hack-different/apple-knowledge`](https://github.com/hack-different/apple-knowledge)
  - tooling integrations for [`tobefuturer/restore-symbol`](https://github.com/tobefuturer/restore-symbol),
    [`tobefuturer/app2dylib`](https://github.com/tobefuturer/app2dylib),
    [`4ch12dy/xia0LLDB`](https://github.com/4ch12dy/xia0LLDB),
    [`facebook/chisel`](https://github.com/facebook/chisel),
    [`0xdea/frida-scripts`](https://github.com/0xdea/frida-scripts),
    [`suifei/fridare`](https://github.com/suifei/fridare),
    and others
- Adds adapters for every major LLM coding agent.

Full attribution and licensing in [`NOTICE.md`](NOTICE.md).

## What it does

Process IPA archives, `.app` bundles, Mach-O binaries, dynamic libraries, and
frameworks — produce structured documentation of APIs, security findings,
embedded secrets, SDK inventories, protection assessments **and** a
vulnerability-class audit ready for a pentest report.

- **Initial triage (Phase 0)** — five-pass probe (symbols, strings, libs,
  entitlements, Mach-O facts) + FairPlay encryption detection + decryption
  driver (`ipadecrypt`, `bagbak`, `frida-ios-dump`, `Clutch`) + automatic
  App Store download by bundle-id via `ipadecrypt`
- **IPA / app extraction (Phase 2)** — unpack, dump Objective-C / Swift
  class headers via `ipsw class-dump`, extract `Info.plist`, entitlements,
  embedded frameworks, string constants
- **API endpoint discovery (Phase 5)** — URLSession, Alamofire, Moya,
  AFNetworking, GraphQL, WebSocket
- **Call-flow tracing (Phase 4)** — ViewController → ViewModel/Presenter →
  Service → API client → networking layer
- **Security audit (Phase 6)** — ATS exceptions, cert pinning, weak crypto,
  keychain misuse, jailbreak detection, debug artifacts
- **Cloud credential scan (Phase 7)** — Firebase, AWS, GCP, Azure, Stripe,
  Twilio, SendGrid + LLM-assisted classification, blast-radius assessment
- **Deep binary reversing (Phase 8)** — radare2 / rizin / Ghidra headless,
  with seven bundled Java analysis scripts (incl. Swift demangler and
  Objective-C swizzling detector)
- **SDK fingerprinting (Phase 9)** — embedded third-party SDKs, version
  detection, CVE cross-reference
- **Protection detection (Phase 10)** — obfuscation, anti-debug,
  dylib-injection prevention, integrity checks, jailbreak detection,
  FairPlay DRM (0–20 protection score)
- **Dynamic instrumentation (Phase 11)** — drop-in Frida script bundle for
  jailbreak bypass, SSL pinning bypass, Keychain / URLSession / pasteboard
  / crypto hooking
- **Vulnerability-class audit (Phase 12)** — URL-scheme injection, WebView
  misuse, hard-coded secrets, broken transport security, insecure storage,
  sensitive logging, deep-link abuse, plus a written attack-chain narrative
- **Binary patching (Phase 13)** — AArch64 / armv7 patch idioms, re-sign
  loop, FridaGadget injection (only against software you own / are
  authorised to modify)

The full 14-phase workflow lives in
[`skill/METHODOLOGY.md`](skill/METHODOLOGY.md).

## Repository layout

```
ios-reverse-skills/
├── skill/                              # The model-agnostic toolkit
│   ├── METHODOLOGY.md                  # 14-phase workflow (source of truth)
│   ├── scripts/
│   │   ├── check-deps.sh               # Dep verification
│   │   ├── install-dep.sh              # Auto-installer
│   │   ├── initial-probe.sh            # ★ Five-pass triage (Phase 0)
│   │   ├── check-encryption.sh         # ★ FairPlay detection (Phase 0)
│   │   ├── decrypt-helper.sh           # ★ Decryption driver  (Phase 0)
│   │   ├── extract-ipa.sh              # Extract + class-dump (Phase 2)
│   │   ├── find-api-calls.sh           # API endpoint discovery (Phase 5)
│   │   ├── deep-secret-scan.sh         # Cloud credential scanner (Phase 7)
│   │   ├── reversing-analyze.sh        # r2 / rizin / Ghidra driver (Phase 8)
│   │   ├── detect-sdks.sh              # SDK fingerprinting + CVE (Phase 9)
│   │   ├── detect-protections.sh       # Anti-tamper detection (Phase 10)
│   │   ├── frida-toolbox.sh            # ★ Frida script generator (Phase 11)
│   │   ├── audit-vulnerabilities.sh    # ★ Vuln-class audit (Phase 12)
│   │   ├── restore-symbols.sh          # ★ ObjC symbol restoration wrapper
│   │   └── ghidra/                     # Ghidra headless Java scripts
│   │       ├── DecompileAllFunctions.java
│   │       ├── FindSecrets.java
│   │       ├── ExportAPICalls.java
│   │       ├── ExportCryptoUsage.java
│   │       ├── ExportStringXrefs.java
│   │       ├── SwiftDemangler.java     # ★ Swift name beautifier
│   │       └── DetectSwizzling.java    # ★ ObjC swizzling locator
│   └── references/                     # Per-phase reference guides
│       ├── setup-guide.md
│       ├── initial-probe.md            # ★ Five-pass triage walk-through
│       ├── macho-internals.md          # ★ Mach-O headers / load cmds / sections
│       ├── arm-assembly-primer.md      # ★ AArch64 + armv7 idioms
│       ├── ios-app-lifecycle.md        # ★ Entrypoints to start reversing from
│       ├── swift-reversing.md          # ★ Mangling, dispatch, metadata
│       ├── ipc-mechanisms.md           # ★ Mach IPC / MIG / XPC fingerprints
│       ├── dyld-shared-cache.md        # ★ DSC extraction
│       ├── decryption-workflow.md      # ★ FairPlay & decrypters (incl. mremap_encrypted)
│       ├── ipadecrypt-integration.md  # ★ ipadecrypt setup & usage guide
│       ├── dynamic-instrumentation.md  # ★ Frida / Cycript / lldb primer
│       ├── binary-patching.md          # ★ Patch idioms + re-signing
│       ├── common-vulnerabilities.md   # ★ Vuln class catalogue + template
│       ├── obfuscation-patterns.md     # ★ Strip / swizzle / CFF / strings
│       ├── owasp-mastg-crosswalk.md    # ★ MASVS/MSTG mapping + report template
│       ├── tooling-index.md            # ★ Tool catalogue beyond ipsw/Ghidra/Frida
│       ├── lldb-cheatsheet.md          # ★ LLDB + chisel + xia0LLDB
│       ├── restore-symbol-workflow.md  # ★ Rebuild stripped ObjC symtab
│       ├── app2dylib-workflow.md       # ★ App → dylib for partial dynamic
│       ├── xnu-mach-iokit-primer.md    # ★ Kernel-adjacent primer
│       ├── private-framework-headers.md# ★ Lookup mirrors for PrivateFrameworks
│       ├── frida-toolkit-index.md      # ★ 0xdea/Fridare/Brida/objection
│       ├── external-reading.md         # ★ Canonical Mach-O/ARM/XNU bibliography
│       ├── class-dump-usage.md
│       ├── api-extraction-patterns.md
│       ├── call-flow-analysis.md
│       ├── cloud-secrets-patterns.md
│       ├── reversing-tools-guide.md
│       ├── sdk-fingerprinting.md
│       └── anti-tampering-patterns.md
│   #  ★ = added by anatoly505/ios-reverse-skills (see NOTICE.md)
├── agents/                             # Per-LLM adapter configs
│   ├── claude-code/                    # SKILL.md + /extract-ipa command
│   ├── cursor/                         # .cursor/rules/*.mdc + commands
│   ├── qwen-coder/                     # QWEN.md + AGENTS.md
│   ├── minimax/                        # System prompt
│   ├── openai-codex/                   # AGENTS.md
│   ├── aider/                          # CONVENTIONS.md + .aider.conf.yml
│   ├── cline/                          # .clinerules
│   └── generic/                        # Universal system prompt
├── install.sh                          # One-shot installer
├── LICENSE                             # Unlicense (public domain)
├── NOTICE.md                           # Upstream attribution
└── README.md                           # This file
```

## Quick start

### 1. Clone

```bash
git clone https://github.com/anatoly505/ios-reverse-skills.git
cd ios-reverse-skills
```

### 2. Install for your agent

| Agent             | One-liner                                                                  |
| ----------------- | -------------------------------------------------------------------------- |
| Claude Opus / Code| `bash install.sh --for claude-code  --target /path/to/project`             |
| Cursor (any model)| `bash install.sh --for cursor       --target /path/to/workspace`           |
| Qwen Coder        | `bash install.sh --for qwen-coder   --target /path/to/project`             |
| MiniMax           | `bash install.sh --for minimax      --target /path/to/workspace`           |
| OpenAI Codex / GPT-5 | `bash install.sh --for openai-codex --target /path/to/project`          |
| Aider             | `bash install.sh --for aider        --target /path/to/project`             |
| Cline             | `bash install.sh --for cline        --target /path/to/project`             |
| Any LLM (manual)  | `bash install.sh --for generic      --target /path/to/workspace`           |
| Everything        | `bash install.sh --for all          --target /path/to/playground`          |

The installer drops the right config files into your project (e.g.
`.cursor/rules/`, `.claude/skills/`, `QWEN.md`, `AGENTS.md`, `.clinerules`,
…) and copies the actual scripts under `tools/ios-re-skill/` (or
`.claude/skills/ios-reverse-engineering/` for Claude Code).

### 3. Verify dependencies

```bash
export IOS_RE_SKILL_ROOT="/path/to/project/tools/ios-re-skill"  # or .claude/skills/...
bash "$IOS_RE_SKILL_ROOT/scripts/check-deps.sh"
```

Required: `ipsw` (`brew install blacktop/tap/ipsw`), `otool`, `strings`,
`unzip`. Recommended: `radare2`/`rizin`, `Ghidra` (set `GHIDRA_INSTALL_DIR`),
`plutil`, `codesign`. macOS gives you most via Xcode CLI tools. Linux is
static-analysis-only.

### 4. Drive it from your agent

Examples:

```text
Claude Code:    /extract-ipa /work/MyApp.ipa
Cursor:         /extract-ipa /work/MyApp.ipa
Qwen Coder:     "Extract /work/MyApp.ipa, run all 10 phases, write a report."
MiniMax:        Same — system prompt is preloaded with the workflow.
Codex CLI:      Same — AGENTS.md takes care of the contract.
Aider:          /run bash $IOS_RE_SKILL_ROOT/scripts/extract-ipa.sh /work/MyApp.ipa
Cline:          "Extract /work/MyApp.ipa and produce a security report."
```

Every agent then runs the same 14 phases, calls the same bash scripts, and
produces the same `*-report.md` deliverables.

## Supported input formats

| Format         | Description                                                  |
| -------------- | ------------------------------------------------------------ |
| `.ipa`         | iOS App Store package (ZIP archive containing `Payload/*.app`) |
| `.app`         | Application bundle directory                                  |
| Mach-O binary  | Raw executable                                                |
| `.dylib`       | Dynamic library                                               |
| `.framework`   | Framework bundle                                              |

## The 14 phases

| # | Phase                                          | Driver script                  |
|---|------------------------------------------------|--------------------------------|
| 0 | Triage + (if needed) decryption                | `initial-probe.sh`, `check-encryption.sh`, `decrypt-helper.sh` |
| 1 | Verify & install dependencies                  | `check-deps.sh`, `install-dep.sh` |
| 2 | Extract & class-dump                           | `extract-ipa.sh`               |
| 3 | Analyze structure (Info.plist, entitlements)   | (manual)                       |
| 4 | Trace call flows (UI → ViewModel → network)    | (manual)                       |
| 5 | Extract & document APIs                        | `find-api-calls.sh`            |
| 6 | Security audit (ATS, pinning, crypto)          | `find-api-calls.sh --security` |
| 7 | Deep secret & credential scan                  | `deep-secret-scan.sh`          |
| 8 | Deep binary reversing                          | `reversing-analyze.sh`         |
| 9 | SDK & framework fingerprinting                 | `detect-sdks.sh`               |
|10 | Protection & anti-tampering detection (0-20)   | `detect-protections.sh`        |
|11 | Dynamic instrumentation (Frida)                | `frida-toolbox.sh`             |
|12 | Vulnerability-class audit                      | `audit-vulnerabilities.sh`     |
|13 | Binary patching (only when authorised)         | `references/binary-patching.md` |

Read the full spec in [`skill/METHODOLOGY.md`](skill/METHODOLOGY.md).

## Use cases

- **Security research** — pre-disclosure auditing of iOS apps
- **Pentesting** — attack-surface mapping under authorized engagements
- **CTF** — fast triage of iOS challenge binaries
- **Competitive analysis** — SDK / API / architecture intelligence
- **Compliance** — verify ATS, cert pinning, keychain usage, data encryption
- **Incident response** — rapid assessment of suspicious IPAs

## Contributing

PRs welcome — adapters for additional agents, new SDK fingerprints, refined
secret patterns, more Ghidra scripts. Keep the scripts model-agnostic; put
agent-specific glue under `agents/<name>/`.

## License

Public domain — [Unlicense](LICENSE). See [`NOTICE.md`](NOTICE.md) for
upstream attribution.
