# Strix Halo Guide: AMD Ryzen AI MAX+ 395 Local LLM Setup & Benchmarks

**Maintenance update: October 21, 2026.** Beginner-route evidence, model-answer corrections, current release observations and 495 dispatch status: [MAINTENANCE_REVIEW_2026-10-21.md](MAINTENANCE_REVIEW_2026-10-21.md). Historical measurements and the broad October 1 evidence review keep their original dates.

Get a local AI model running on your AMD Strix Halo / Ryzen AI MAX+ 395 (Radeon 8060S) under Ubuntu 24.04, with settings measured on real hardware and a check that it really runs on the GPU. Then pick the right model for your work and make it faster.

**Start here → [Get local AI running, step by step](LOCAL_CHAT_START.md)** · Ubuntu 24.04 · 128GB-class systems · from BIOS to your first answer and a GPU check, then chat in your browser if you want it.

Built on [real-world results from 10 Strix Halo systems plus 3 independent sources](SYSTEM_EVIDENCE_MATRIX.md), with measured settings, model comparisons and documented fixes.

**Setup status:** GPU answers and browser chat passed an isolated hardware check on October 15. A complete run on a freshly installed Strix Halo is not yet verified; [see what has been checked](LOCAL_CHAT_START.md#version-and-security-status).

## What This Gives You

- **A clear setup route.** The settings that matter on this chip, from the BIOS memory option to the one Ollama setting without which measured builds quietly run on the CPU, in one [step-by-step start route](LOCAL_CHAT_START.md) that shows the expected result of every step.
- **A model that fits your work.** Which model to run for chat, coding, images or long context, with the speed each one reached here: [Best Known Profiles](BEST_KNOWN_PROFILES.md).
- **Know what's tested.** See which settings have been tested, what is still experimental, and which [known failures you can avoid](#things-that-dont-work-dont-waste-your-time). If something goes wrong, use the [troubleshooting steps](#troubleshooting). Every headline number links to its [raw evidence](#headline-evidence) or carries an explicit caveat.

## Start Here

| I want to… | Start here |
|---|---|
| Get local AI running | [Install, get an answer and check the GPU](LOCAL_CHAT_START.md) |
| Choose a model or make it faster | [Best Known Profiles](BEST_KNOWN_PROFILES.md) and [Current Models](CURRENT_MODELS.md) |
| Fix something that is not working | [Troubleshooting](#troubleshooting) |
| Decide what to buy | [Buyer Use Cases](BUYER_USE_CASES.md) and [Buying Guide](#buying-guide) |

Also: [website](https://strixhaloguide.com/) · [Qwen3.8](QWEN38_STRIX_HALO.md) · [reproduce a result](REPRODUCIBILITY.md) · [vendor/reviewer brief](ONE_PAGE_BRIEF.md).

## Quick Start (6 Steps)

New here? Use the [complete start route](LOCAL_CHAT_START.md): it has the
commands, what each one should print, and what to do when it does not. The six
points below are the short overview for anyone who wants to do, or understand,
each step by hand:

1. **BIOS:** use UMA 512MB if available, or the vendor minimum such as 2GB. Leave IOMMU enabled/default; the desktop benchmark alternative has [suspend/NPU caveats](#step-12-choose-the-iommu-policy).
2. **OS:** install Ubuntu 24.04 LTS. X11 is needed only by desktop tools that require it.
3. **Memory:** the recorded 128GB profile uses `amdgpu.gttsize=131072 ttm.pages_limit=31457280 amdgpu.cwsr_enable=0`. Do not reuse these limits on 64/96/192GB systems; see [the manual memory section](#step-32-configure-grub-boot-parameters).
4. **Drivers:** use Mesa/RADV and preserve the existing power policy by default. `tuned` is an opt-in reproduction profile.
5. **Ollama:** the setup script does steps 3–5 for you on the 128GB-class profile. It sets `OLLAMA_VULKAN=1`, `OLLAMA_IGPU_ENABLE=1` and `HIP_VISIBLE_DEVICES=-1`; reboot first if it asks you to.
6. **Check:** chat with the model using `ollama run qwen3.6:35b-a3b`, then run the [known-answer, GPU and loopback-listener checks](LOCAL_CHAT_START.md#step-5-get-your-first-answer-and-check-a-known-task) from the start route. The historical 0.31.2 row reached about 60 generation t/s; that is an indication, not a promise for today's model tag. Single-digit t/s on this model is a reason to check for [CPU fallback](#troubleshooting).

Further down, the phases explain each change in detail for anyone who wants to
inspect or reproduce it by hand. For another model, use
[Best Known Profiles](BEST_KNOWN_PROFILES.md); the
[Qwen3.8 decision](QWEN38_STRIX_HALO.md) has its own runtime and context boundaries.

## Setup Script

**Scope before running:** this automatic route is for 128GB-class systems with
at least 120GiB visible RAM on Ubuntu 24.04. It is not a general 64GB/96GB
installer, and it stops above about 136GiB visible RAM: 192GB-class systems
(for example Ryzen AI Max+ PRO 495) are not qualified, so do not reuse the 128GB
values there. The check reads OS-visible RAM only, so a 192GB system with a
large BIOS UMA reserve can still pass it; confirm your installed memory first.
Ubuntu 26.04 is **not qualified** by this guide; the script stops on any OS
other than Ubuntu 24.04 unless you deliberately pass
`STRIX_HALO_ALLOW_UNQUALIFIED_OS=1` to it (for example
`STRIX_HALO_ALLOW_UNQUALIFIED_OS=1 bash setup.sh`). Configuration
handling has offline fixture coverage; the revised script's fresh-install and
upgrade paths still need hardware qualification. Review the script and existing
configuration first: a later conflict can stop a partially completed run; this
is not a transactional installer with a complete automatic rollback.

If `/etc/default/grub.d/` contains any `*.cfg` files, the script stops before
changing the system and asks for manual review. These files can override the
boot settings it writes. This conservative check also stops for harmless
fragments; keep them and use the [manual boot-settings reference](#step-32-configure-grub-boot-parameters).

**Existing-user result, September 19:** [the scoped qualification](RUNTIME_QUALIFICATION_2026-09-19.md)
passed text, separate-model image, executed tools and pinned WebUI on the
existing Ollama 0.32.15 service after restart. The historical fresh-install
reboot pin stays 0.31.2; isolated 0.34.2 is useful but not default. These tests
are not a new clean-install or full-host-reboot qualification.

Fresh installations request **Ollama 0.31.2**, the reboot-qualified runtime.
An existing installation is retained, with its version reported; it is not
automatically downgraded. Set `OLLAMA_VERSION` explicitly to test another
release. This pins only the requested runtime: model tags, Mesa and other
packages can change, so record the actual stack and complete the reboot/GPU
checks before comparing with a measured profile. See
[Ollama version selection](https://docs.ollama.com/linux#installing-specific-versions).

**Before you change anything:** the [complete start route](LOCAL_CHAT_START.md)
walks through the prerequisites, disk checks, the expected output of each step
and help when something fails. The script edits GRUB, adds the kisak Mesa PPA
and runs a full `apt upgrade -y`; the [manual undo table](#undo-the-setup-script)
is untested on hardware. Ollama has no password, so keep its API on loopback.
Published advisories include the historical 0.31.2 pin; read the
[security status](SECURITY.md#security-status-of-pinned-components). If you
already have a working setup, back it up and test the restore before running
the script.

If you've already set your BIOS (UMA = 512MB if available, or 2GB if that is your vendor minimum; leave IOMMU enabled/default unless you deliberately choose the desktop benchmark profile) and installed Ubuntu 24.04:

```bash
git clone https://github.com/hogeheer499-commits/strix-halo-guide
cd strix-halo-guide
bash setup.sh
```

Both the `git clone` route above and the `curl | bash` route below run the
unpinned `main` branch, which has not been fresh-install qualified on hardware.
For a reproducible run, review the script and pin it to a tag or commit you have
reviewed (`git checkout <tag-or-commit>` before `bash setup.sh`, or replace
`main` in the raw URL with that commit). No tag is currently marked as
fresh-install qualified for the revised script.

Inspect the script first with `less setup.sh` before running it: it edits GRUB boot parameters, adds the kisak Mesa PPA, and runs a full `apt upgrade`.

For unattended copy/paste installs, the same script can also be run as:

```bash
curl -fsSL https://raw.githubusercontent.com/hogeheer499-commits/strix-halo-guide/main/setup.sh | bash
```

This also adds the kisak Mesa PPA and runs a full `apt upgrade -y`, and it
fetches unpinned `main` (see the pinning note above).

This installs the Linux-side Vulkan/RADV + Ollama path, configures Ollama for Vulkan, pulls a model, and prepares a verification benchmark. If the script changes boot parameters, reboot first and then run `bash ~/bench-ollama.sh`.

### Undo the setup script

> **Untested on hardware:** these manual reversal steps have not been run on the
> test system. Review each one against your own configuration first, and only
> undo what the script actually changed on your machine.

| Change made by `setup.sh` | Manual reversal |
|---|---|
| Added `amdgpu.gttsize=131072 ttm.pages_limit=31457280 amdgpu.cwsr_enable=0` to `GRUB_CMDLINE_LINUX_DEFAULT` | `sudoedit /etc/default/grub`, remove only those parameters, run `sudo update-grub`, reboot and check `/proc/cmdline` |
| Installed `/etc/systemd/system/ollama.service.d/60-strix-halo-guide.conf` | `sudo rm /etc/systemd/system/ollama.service.d/60-strix-halo-guide.conf`, then `sudo systemctl daemon-reload` and `sudo systemctl restart ollama` |
| Added `ppa:kisak/kisak-mesa` and ran `apt upgrade -y` | `sudo apt install ppa-purge && sudo ppa-purge ppa:kisak/kisak-mesa` (downgrades the PPA packages to Ubuntu's versions); other packages upgraded by `apt upgrade` are not reverted |
| Added your user to `render` and/or `video` | Only if the script added them: `sudo gpasswd -d "$USER" render` / `video`, then log out and back in |
| Wrote `~/bench-ollama.sh` | `rm ~/bench-ollama.sh` |
| Pulled `qwen3.6:35b-a3b` | `ollama rm qwen3.6:35b-a3b` |
| Installed Ollama (fresh installs only) and `vulkan-tools` if missing | Follow [Ollama's Linux uninstall steps](https://docs.ollama.com/linux#uninstall); `sudo apt remove vulkan-tools` |
| With `POWER_POLICY=tuned` only: installed/enabled `tuned` | `sudo systemctl disable --now tuned`, then restore your previous power manager |

![AMD](https://img.shields.io/badge/AMD-Ryzen_AI_MAX+_395-ED1C24?style=for-the-badge&logo=amd&logoColor=white)
![Speed](https://img.shields.io/badge/direct_30B_Qwen-100.0_t/s-brightgreen?style=for-the-badge)
![Small MoE](https://img.shields.io/badge/small_MoE-170.0_t/s-brightgreen?style=for-the-badge)
![284B](https://img.shields.io/badge/direct_284B_GGUF-13.3_t/s-0ea5e9?style=for-the-badge)
![MTP](https://img.shields.io/badge/MTP_server-101--141_t/s_experimental-7c3aed?style=for-the-badge)
[![Community](https://img.shields.io/badge/community-10_benchmark_contributors_13_systems%2Fsources-success?style=for-the-badge)](COMMUNITY_RESULTS.md)
![RAM](https://img.shields.io/badge/128GB_unified-blue?style=for-the-badge)
![GitHub stars](https://img.shields.io/github/stars/hogeheer499-commits/strix-halo-guide?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
[![Validate](https://img.shields.io/github/actions/workflow/status/hogeheer499-commits/strix-halo-guide/validate.yml?branch=main&label=validate&style=for-the-badge)](https://github.com/hogeheer499-commits/strix-halo-guide/actions/workflows/validate.yml)

## Use This Guide If

- You own, ordered, review, sell, or are evaluating a Strix Halo / Ryzen AI MAX system for local AI.
- You want a working route and the evidence needed to understand where it transfers—or fails to transfer—to another system.
- You need independent buyer guidance that can coexist with future disclosed vendor or affiliate relationships.

A complete, practical guide to running large language models locally on AMD Strix Halo / Ryzen AI MAX+ 395 systems with Radeon 8060S (`gfx1151`) and 96GB/128GB unified memory.

Covers BIOS config, Ubuntu 24.04/kernel setup, Ollama, `llama.cpp` Vulkan/RADV, ROCm/HIP experiments, vLLM notes, 70B/120B and selected 284B GGUF capacity evidence, benchmarks, raw logs, and reproducibility checks.

AMD now publicly frames Ryzen AI Halo-class systems as a local-AI and developer-platform direction. This repository is the independent practical layer: copyable setup, measured rows, raw evidence, failures, and community reproductions. It is not official AMD or OEM endorsement. See [`RYZEN_AI_HALO_CONTEXT.md`](RYZEN_AI_HALO_CONTEXT.md).

Project website: <https://strixhaloguide.com/>. This GitHub repository remains the source of truth for setup commands, benchmark claims, and raw evidence.

Maintainer credibility is public and reviewable: 15 merged engineering PRs across 10 upstream projects, including [`llama.cpp`](https://github.com/ggml-org/llama.cpp/pull/25643), the AMD-sponsored open-source Lemonade local-AI server, a Strix Halo detection fix in llmfit, OpenAI's official .NET SDK, and Kubernetes SIG inference-perf, plus 3 merged listing/docs PRs (counts reconciled 2026-09-13). See [`UPSTREAM_CONTRIBUTIONS.md`](UPSTREAM_CONTRIBUTIONS.md) for every PR link, its scope, and honest boundaries. Upstream acceptance strengthens confidence in the engineering process; it does not replace the raw evidence required for each benchmark claim.

**Current evidence state — October 1, 2026 review (observations of September 30):** Qwen3.8 27B is
measured through the official Ollama route, labelled as Ollama-default MTP drafting; a matched
control on Ollama 0.32.15 (2026-09-26) measured 12.89 t/s without drafting versus 22.71 t/s with
default MTP. See [the active-evidence review](ACTIVE_EVIDENCE_REVIEW_2026-10-01.md); the
[September 26 review](ACTIVE_EVIDENCE_REVIEW_2026-09-26.md) keeps its original wording. The August 30 b10687 Vulkan sentinel and Flash-Next
scout are indexed with their own stack and caveats; see
[the measured update](BENCHMARKS.md#2026-08-30-vulkan-sentinel-and-flash-next-scout).
The [September 30 availability check](ROCM_VLLM_BUGWATCH.md#2026-09-30-upstream-recheck)
lists newer candidates without promoting them: Ollama 0.34.4 (the latest stable release that day),
`llama.cpp` v0.5.0 (the same commit as build b11146, which the 2026-09-26 routine scouts used) and
the numbered build b11265 (the newest numbered build when that check was made, published 2026-09-29 23:24 UTC; newer builds followed within hours; not measured here). The
machine-readable freshness record is [`data/public_state.json`](data/public_state.json).

What you get:

- A copyable Ubuntu + Vulkan/RADV setup for Ollama and `llama.cpp`.
- Workload-to-model/backend recommendations instead of one undifferentiated leaderboard.
- Direct, API/server, MTP/speculative, concurrency, capacity, power, NPU, RPC, first-party, and community claims kept separate.
- Headline rows linked to CSVs, raw logs, charts or explicit `n/a`, plus preserved failures and corrections.
- Cross-OEM evidence covering 13 systems or independent sources from 10 credited community benchmark contributors.

> Measured primarily on one Beelink GTR9 Pro. Community results are kept separate from local headline claims. This repository ships docs, scripts, data, and charts only; no `.exe`, binary `.zip`, browser extensions, or model weights. Raw evidence, commands, caveats, and corrections are linked so results can be checked instead of taken on trust.

[Quick Start](#quick-start-6-steps) | [Qwen3.8](QWEN38_STRIX_HALO.md) | [Profiles](BEST_KNOWN_PROFILES.md) | [Current Models](CURRENT_MODELS.md) | [Evidence](#headline-evidence) | [Community](COMMUNITY_RESULTS.md) | [Reproduce](#reproduce-one-headline-result) | [Contribute](CONTRIBUTING.md)

If this guide saves you setup or research time, a GitHub star helps other Strix
Halo owners find it; a reproducible result or correction helps even more.

| Need | Source of truth |
| --- | --- |
| Full beginner route | [Install, check the result and fix errors](LOCAL_CHAT_START.md); [manual reference](#quick-start-6-steps) |
| Current Qwen3.8 decision | [`QWEN38_STRIX_HALO.md`](QWEN38_STRIX_HALO.md) and [`data/qwen38_route_matrix.csv`](data/qwen38_route_matrix.csv) |
| Known-good workload profiles | [`BEST_KNOWN_PROFILES.md`](BEST_KNOWN_PROFILES.md) and [`data/best_known_profiles.csv`](data/best_known_profiles.csv) |
| Auditable benchmark claims | [Headline Evidence](#headline-evidence), [`data/headline_claims.csv`](data/headline_claims.csv), and [`data/raw/`](data/raw/) |
| Cross-OEM buyer evidence | [`SYSTEM_EVIDENCE_MATRIX.md`](SYSTEM_EVIDENCE_MATRIX.md), [`COMMUNITY_RESULTS.md`](COMMUNITY_RESULTS.md), and [`BUYER_PATH_VALIDATION.md`](BUYER_PATH_VALIDATION.md) |
| Current blockers and test priorities | [`CURRENT_MODELS.md`](CURRENT_MODELS.md), [`ROCM_VLLM_BUGWATCH.md`](ROCM_VLLM_BUGWATCH.md), and [`data/current_test_queue.csv`](data/current_test_queue.csv) |

## 20-Second Summary

| Question | Current answer |
| --- | --- |
| Best beginner route | Ollama with Vulkan/RADV. The fully reboot-qualified general baseline remains 0.31.2; Qwen3.8 is separately measured on 0.32.13. Available Ollama 0.34.4 (September 30 check; GitHub lists the then pre-release 0.35.0 as the latest release on October 1, not qualified; 0.34.2 passed isolated controls on September 19) still needs the controlled upgrade/reboot matrix; the revised installer itself is not yet fresh-install/upgrade qualified. |
| Current Qwen3.8 route | Official Qwen3.8 27B `Q4_K_M` measured 292.49 prompt t/s and 20.42 generation t/s through the Ollama API with Ollama-default MTP drafting (`draft_num_predict 4`; not a no-draft result); a separate matched control on Ollama 0.32.15 (2026-09-26) measured 12.89 t/s without drafting versus 22.71 t/s with default MTP; image, tools, thinking, and exact retrieval through 50,059 prompt tokens passed. [Read the route comparison.](QWEN38_STRIX_HALO.md) |
| Fast direct 30B-class route | Qwen3-Coder 30B-A3B `Q4_K_S` reached 100.99 tg128 on official b9851; it is a speed-first quant, not the balanced default. |
| Largest direct GGUF tested | DeepSeek V4 Flash 284B `UD-IQ2_XXS` loaded as a 90.86GB low-bit artifact and measured 13.27 tg128; capacity proof, not broad quality. |
| Experimental server frontier | Repeat-confirmed local MTP/server profiles reach 101-141 t/s, but prompt shape, draft acceptance, runtime, and quant are part of each claim. |
| Cross-system confidence | 13 systems or independent sources and 10 credited community benchmark contributors, with community data separated from first-party Beelink rows. |
| Trust model | Every headline maps to structured/raw evidence or an explicit caveat; failed paths and negative results remain public. |
| Commercial independence | No affiliate links are present as of September 19, 2026. Future affiliate/vendor support must be disclosed and cannot buy ranking, positive conclusions, or removal of accurate negative findings. |

## What You Can Run: Quick Snapshot

This is the quick "what can I actually run on my AI PC?" view. It is not the full benchmark list; see [What You Can Run](#what-you-can-run) for more models and [Headline Evidence](#headline-evidence) for the audit trail.

| What you want to do | Measured local result | Practical takeaway | Evidence |
|---------------------|-----------------------|--------------------|----------|
| Fastest direct 30B-class Qwen MoE row | Qwen3-30B-A3B-Instruct-2507 IQ4_XS: 100.04 t/s direct llama.cpp Vulkan/RADV on b9467; b9544 control measured 103.18 tg128 r10 | First local direct `llama-bench` row above 100 t/s. Treat it as a separate general-instruct Qwen route, not as a Qwen3-Coder replacement or balanced-default claim. | [`headline claims`](data/headline_claims.csv), [`raw r50`](data/raw/2026-06-02/qwen3-30b-a3b-2507-direct-scout/qwen3-30b-2507-iq4xs-b9467-r50.csv), [`b9544 control`](data/raw/2026-06-07/latest-llamacpp-b9544-regression/) |
| Fastest current small-MoE scout | LFM2.5 8B-A1B Q4_K_M: 168.96 tg128 in pp512/tg128, 170.02 t/s generation-only, b9544 control at 176.48 tg128 r10 | Shows how fast newer small active-parameter MoE routes can be on Strix Halo. Do not compare it as a 30B-class coding/reasoning replacement. | [`headline claims`](data/headline_claims.csv), [`raw latest/int-dot`](data/raw/2026-06-05/latest-llamacpp-intdot-regression/), [`b9544 control`](data/raw/2026-06-07/latest-llamacpp-b9544-regression/) |
| Fastest local coding speed | Qwen3-Coder 30B-A3B Q4_K_S: 100.99 t/s direct llama.cpp Vulkan/RADV on the official b9851 release binary; older strict-clean b9179 row measured 98.51 t/s | Speed-first quant candidate. Use it when raw t/s matters and you accept the quality tradeoff. This is direct `llama-bench`, not MTP/server speculation. | [`headline claims`](data/headline_claims.csv), [`b9851 raw r50`](data/raw/2026-06-30/latest-llamacpp-b9851-vulkan-sentinel/qwen3-coder-q4ks-b9851-p512-n128-r50.csv), [`older strict-clean raw r50`](data/raw/2026-05-16/break-97-24-strict-noise-settings/b9179-q4-k-s-r50.csv) |
| Fast balanced local coding model | Qwen3-Coder 30B-A3B UD-Q4_K_XL: 96.76 t/s direct llama.cpp Vulkan/RADV on current b9049 | Coding-speed row for the balanced quant: a speed measurement, not a coding-quality ranking. Third-party quality signals and public scores are in [`docs/models.md`](docs/models.md). | [`headline claims`](data/headline_claims.csv), [`raw run`](data/raw/2026-05-07/max-performance-campaign/benchmarks/qwen3-coder-top-confirm-r20/guide.csv) |
| Newer Qwen coding model | Qwen3-Coder-Next 80B-A3B IQ4_XS: 61.91 t/s direct llama.cpp Vulkan/RADV on b9467 | Modern coding-model row for people who want current Qwen Coder-Next rather than the older 30B speed headline. Use it for capability/currentness, not maximum raw t/s. | [`benchmarks CSV`](data/benchmarks.csv), [`raw run`](data/raw/2026-06-02/modern-model-clean-followup/) |
| Easy local chat setup | Qwen3.6 35B-A3B Q4_K_M: 60.57 t/s warm API generation through the normal Ollama 0.31.2 system service with `OLLAMA_IGPU_ENABLE=1`; vision, service restart, and full-host reboot persistence passed | This is the copyable default for model pulling, Open WebUI, vision, and simple local chat. A later controlled local-binary comparison measured 0.31.1/0.31.2/0.32.0 at 72.55/73.19/73.20 t/s, so do not treat the earlier 60.57-versus-71.82 gap as a version-wide regression. | [`headline claims`](data/headline_claims.csv), [`raw service run`](data/raw/2026-07-10/ollama-0312-buyer-path/), [`raw controlled comparison`](data/raw/2026-07-16/ollama-0311-0312-0320-controlled/) |
| Fine-tune, export, and reload a local model | Pinned ROCm 7.2 Unsloth route: Radeon GPU gate, one SFT step, checkpoint inference, `Q4_K_M` GGUF export, ROCm `llama.cpp` inference, and post-restart artifact load all passed | End-to-end developer workflow evidence on a retail box. The Qwen3 0.6B one-step run is a plumbing smoke, not a quality or performance headline. | [`Unsloth guide`](UNSLOTH_STRIX_HALO.md), [`raw evidence`](data/raw/2026-07-21/unsloth-rocm72-train-export-smoke/) |
| Fast all-rounder direct path | Qwen3.6 35B-A3B UD-Q4_K_M: 62.56 t/s direct llama.cpp Vulkan/RADV on current b9049 | Use this when you care more about speed and control than the easiest UI. | [`headline claims`](data/headline_claims.csv), [`raw run`](data/raw/2026-05-07/latest-stack-rerun/clean-b9049-rerun/qwen36-35b-b9049-clean-r20.csv) |
| Fastest Qwen3.6 direct path | Qwen3.6 35B-A3B Q4_0: 81.30 t/s direct llama.cpp Vulkan/RADV on current b9049 | Speed-first option. Use the default/balanced quant if quality matters more than raw t/s. | [`max campaign`](data/max_performance_campaign.csv), [`raw run`](data/raw/2026-05-07/max-performance-campaign/benchmarks/qwen36-top-confirm-r20/q4-0-ub2048.csv) |
| Qwen3.6 27B dense control | Official Qwen3.6 27B MTP Q8_0: 7.61-7.74 t/s without MTP, 14.59-14.69 t/s with the best MTP setting; a direct b9467 `llama-bench` follow-up measured 7.70 t/s tg128 | Useful practical row for people comparing 27B versus 35B-A3B. It runs, but this dense Q8 route is much slower than the 35B-A3B MoE paths and is not a speed candidate. | [`Performance notes`](PERFORMANCE_NOTES.md#qwen36-27b-mtp-q8_0-status), [`MTP CSV`](data/mtp_speculative.csv), [`raw b9235`](data/raw/2026-05-19/qwen36-27b-mtp-q8-llamacpp-9235/), [`raw latest`](data/raw/2026-06-01/qwen36-27b-mtp-latest-de6f727/), [`raw b9467`](data/raw/2026-06-02/reddit-look-int-dot-reproduction/) |
| Experimental Qwen3.6 MTP server path | Qwen3.6 35B-A3B MTP IQ4_XS-Q8nextn: 101.16 t/s best local Beelink six-prompt average on b9360, with t16 repeats at 101.15 / 101.10 / 101.06 t/s; first GMKtec community reproduction reached 93.29 t/s on b9235 | Advanced speculative-decoding route. Useful if you are testing a local API server; keep separate from direct `llama-bench`. | [`MTP notes`](MTP_SPECULATIVE_DECODING.md), [`MTP CSV`](data/mtp_speculative.csv), [`local raw`](data/raw/2026-05-27/latest-llamacpp-b9360/), [`GMKtec raw`](data/raw/2026-05-19/community-gmktec-mtp-issue18/) |
| Experimental Gemma 4 QAT MTP server path | Gemma 4 26B-A4B QAT UD-Q4_K_XL + matched Q4_0 MTP head: 110.00 t/s best repeat, 107.42 t/s T3-only repeat, 102.69 t/s cold repeat, 73.96 t/s no-spec baseline on ac4cddeb0 | Historical server throughput, not a practical recommendation: six sampled saved coding answers failed their tasks in both no-spec and MTP records; see the [saved-output review](BEST_KNOWN_PROFILES.md#historical-throughput-sampled-coding-outputs-failed). These are server/speculative results, separate from direct `llama-bench`. | [`headline claims`](data/headline_claims.csv), [`MTP CSV`](data/mtp_speculative.csv), [`warm raw`](data/raw/2026-06-11/gemma4-26b-qat-mtp-sixprompt-ac4cddeb/), [`cold raw`](data/raw/2026-06-12/gemma4-26b-qat-mtp-cold-repeat-ac4cddeb/), [`T3-only raw`](data/raw/2026-06-12/gemma4-26b-qat-mtp-t3-only-repeat-ac4cddeb/) |
| Official Gemma 4 31B QAT multimodal route | Official Q4_0 GGUF: 308.28 pp512 / 11.38 tg128 direct on b10066; narrow text, `STRIX 395` vision, and native calculator tool-call smokes passed | Current dense Google-model compatibility route for buyers who value text, vision, and tools over maximum decode speed. The matched Q8_0 DFlash sidecar loaded but was slower on the measured 5.5K/21.9K synthetic prompt shapes because acceptance stayed low. | [`benchmarks CSV`](data/benchmarks.csv), [`MTP CSV`](data/mtp_speculative.csv), [`raw evidence`](data/raw/2026-07-18/gemma4-31b-qat-dflash-b10066/) |
| Experimental CHADROCK ROCmFP4 MTP server path | CHADROCK ACE/SABER 35B ROCmFP4 through `ciru-ai/ROCmFPX`: 141.37 t/s mean across three repeats on the exact 3946-token reference profile, with 100% mean draft acceptance | Fastest repeat-confirmed server/speculative reference profile in the guide, but not a universal speed. Separate 1K/8K/16K profiles measured 78.00/83.85/107.23 t/s as acceptance changed. Treat as advanced ROCmFPX/CHADROCK evidence, not a direct `llama-bench` replacement. | [`ROCMFP4_CHADROCK.md`](ROCMFP4_CHADROCK.md), [`raw stability profile`](data/raw/2026-07-16/rocmfpx-chadrock-stability-profile/), [`MTP CSV`](data/mtp_speculative.csv) |
| Frontier-size agent server | Step 3.7 Flash 198B-A11B ROCmFPX Q3 plus Q8 MTP draft: 23.84 t/s matched 4K no-spec baseline, 34.50 t/s 4K MTP, 33.83 t/s 16K MTP, native tool-call pass, and 256K allocation | Shows the capacity and agent value of 128GB unified memory rather than chasing the fastest small-model row. Advanced pinned runtime; server/MTP result, and the 48K row has one repeat. | [`ROCmFPX guide`](ROCMFP4_CHADROCK.md#step-37-q3-qualityplus-first-party-reproduction), [`raw evidence`](data/raw/2026-07-16/step37-rocmfpx-q3-qualityplus/), [`MTP CSV`](data/mtp_speculative.csv) |
| 80B MoE coding/reasoning experiments | Qwen3-Next 80B-A3B UD-Q4_K_XL: 59.06 t/s direct llama.cpp Vulkan/RADV on b9172 | Historical May 80B Qwen-family path measured here; use when model size and 256K context matter more than smallest footprint. | [`headline claims`](data/headline_claims.csv), [`raw r20`](data/raw/2026-05-16/latest-stack-b9172/qwen3-next-confirm-r20/qwen3-next-80b-b9172-ub1024-r20.csv) |
| Open-weight 120B reasoning model | gpt-oss-120b MXFP4: 55.57 t/s direct llama.cpp Vulkan/RADV on current b9049 | 128GB unified memory can run a 117B-parameter MoE locally; this is speed evidence, not a model-quality eval. | [`headline claims`](data/headline_claims.csv), [`raw run`](data/raw/2026-05-07/max-performance-campaign/benchmarks/gpt-oss-120b-long-context-vulkan/) |
| Current 120B-class GGUF capacity route | Nemotron 3 Super 120B-A12B UD-IQ4_XS: 18.43 t/s direct llama.cpp Vulkan/RADV, b9544 control at 18.93 tg128 r3 | Answers a different buyer question: yes, a current 120B-class MoE GGUF route can run directly on one 128GB Strix Halo box. | [`headline claims`](data/headline_claims.csv), [`raw latest/int-dot`](data/raw/2026-06-05/latest-llamacpp-intdot-regression/), [`b9544 control`](data/raw/2026-06-07/latest-llamacpp-b9544-regression/) |
| Current NVIDIA Omni/FP4 route | The same Nemotron 3 Nano Omni MXFP4 artifact improved from 56.56 tg128 on b9747 to 64.26 on b10034; a separate NVFP4 + F16 projector route measured 53.21 tg128 and correctly read `STRIX 395` from an image | Shows both current runtime maintenance and a first-party image-capable Nemotron route. The OCR check is not broad vision/audio/video validation and neither row replaces the Qwen speed headlines. | [`benchmarks CSV`](data/benchmarks.csv), [`raw MXFP4 sentinel`](data/raw/2026-07-16/nemotron-omni-mxfp4-b10034-sentinel/), [`raw multimodal scout`](data/raw/2026-07-16/nemotron-omni-nvfp4-multimodal/) |
| Current agent/reasoning scouts | Nemotron Cascade 2 30B-A3B `IQ4_XS`: 78.95 tg128; Qwen AgentWorld 35B-A3B `UD-IQ4_XS`: rate withheld pending retained-run provenance with a correct terminal-world smoke and 128K allocation pass | These answer current-model and agent-use-case questions without pretending every new model is a speed headline. Cascade's forced no-think prefix did not hide reasoning; AgentWorld's 128K result is an allocation smoke, not a filled-context quality claim. | [`CURRENT_MODELS.md`](CURRENT_MODELS.md), [`Cascade evidence`](data/raw/2026-07-16/nemotron-cascade2-iq4xs/), [`AgentWorld evidence`](data/raw/2026-07-16/agentworld-iq4xs/) [Curator: exact retained-run disagreement](EVIDENCE_CORRECTIONS.md#agentworld-retained-run-disagreement); rate provenance pending. |
| Local API for tools or several clients | Qwen3-Coder 30B-A3B b9979: 228.18 aggregate t/s stock at np8; opt-in density+dense16 reached 234.12 at np9, while density alone reached 266.07 at np16 | A software dispatch cliff, not memory capacity, can limit multi-user value. Keep stock for low concurrency; advanced users should compare density Vulkan and ROCm at their exact target. | [`MOE_CONCURRENCY.md`](MOE_CONCURRENCY.md), [`summary CSV`](data/moe_density_gate_summary.csv), [`30B chart`](charts/moe_density_gate_30b.svg) |
| FP16 vLLM at 8-16 concurrent requests | Official ROCm 7.14 image, PyTorch 2.11, Qwen3-0.6B: `TORCH_BLAS_PREFER_HIPBLASLT=1` improved aggregate throughput by 40.50% / 38.96% / 41.54% at concurrency 8/9/16 | This reproduces AMD's Ryzen AI batch-8+ workaround without changing the host. It is a small-model FP16 server A/B, not a direct GGUF or 27B/35B claim; concurrency 4 was slightly slower. | [`ROCm/vLLM notes`](ROCM_VLLM_BUGWATCH.md), [`processed A/B`](data/rocm_714_hipblaslt_ab.csv), [`raw evidence`](data/raw/2026-07-16/rocm-714-vllm-hipblaslt-ab/) |
| Historical ROCm/HIP `llama.cpp` allocation smoke | Official b10046, Qwen3-0.6B Q8_0: 4666.05 pp512 / 208.73 tg128; full 120,124 MiB free UMA detected and `ROCm_Host` buffers allocated | Reproduced full-UMA discovery without `HSA_OVERRIDE_GFX_VERSION`, but open issue #26209 and the model-scoped [v0.4.1 mitigation controls](RUNTIME_QUALIFICATION_2026-09-19.md) do not make the tiny smoke qualify long-context, multimodal, multi-slot, or practical-model correctness. | [`ROCm/HIP notes`](ROCM_VLLM_BUGWATCH.md), [`raw evidence`](data/raw/2026-07-16/llamacpp-b10046-rocm-integrated-host-buffer/) |
| Long documents or codebase context | Qwen3.6 35B-A3B: 32.23 t/s decode after a filled 128K KV cache | Long-context use is possible, but prompt ingestion cost matters. | [`filled KV CSV`](data/filled_kv_decode.csv), [`chart`](charts/filled_kv_decode.svg) |
| Large-model proof point | MiniMax M2.7 230B-class MoE loaded and generated locally; Llama 4 Scout 109B measured 18.32 t/s historically | 128GB unified memory makes very large local models practical on one compact PC, but capacity and speed are different wins. | [`CURRENT_MODELS.md`](CURRENT_MODELS.md), [`benchmarks CSV`](data/benchmarks.csv) |

## Use This If You Want

| Goal | Start with | Why | Evidence |
|------|------------|-----|----------|
| Easiest local chat | Ollama 0.31.2 system service with Vulkan/RADV | normal install path; model pulling, vision, restart/reboot persistence, and Open WebUI compatibility. Local is not automatically private: prompts can end up in logs and caches, see [`SECURE_LOCAL_AI.md`](SECURE_LOCAL_AI.md#the-short-version) | 60.57 t/s fully qualified service run; controlled isolated 0.31.1/0.31.2/0.32.0 binaries later measured 72.55-73.20 t/s, [`data/benchmarks.csv`](data/benchmarks.csv) |
| Fast coding or scripts on one machine | `llama-server` Vulkan/RADV | fastest measured Qwen3.6 path at 1-4 parallel requests | [`SERVER_SHOOTOUT.md`](SERVER_SHOOTOUT.md) |
| Speculative decoding experiments | `llama-server` MTP on current master / ROCmFPX | measured server speedups on Qwen3.6 MTP GGUFs, Gemma 4 QAT matched MTP heads, and CHADROCK ROCmFP4; Qwen3.6 reached about 101.1 t/s on b9360, Gemma 4 26B-A4B QAT reached 110.0 t/s best-repeat, and the exact CHADROCK reference profile averaged 141.37 t/s over three repeats at 100% draft acceptance | [`MTP_SPECULATIVE_DECODING.md`](MTP_SPECULATIVE_DECODING.md), [`ROCMFP4_CHADROCK.md`](ROCMFP4_CHADROCK.md), [`data/mtp_speculative.csv`](data/mtp_speculative.csv) |
| Several local tools or users hitting one API | Start with stock Vulkan up to 8; above that, compare opt-in density Vulkan and Lemonade ROCm on the exact model | b9979 repeats show density recovers the Vulkan np9 cliff, but the backend winner differs between the tested 30B and 80B models | [`MOE_CONCURRENCY.md`](MOE_CONCURRENCY.md), [`data/moe_density_gate_summary.csv`](data/moe_density_gate_summary.csv) |
| Long local documents or codebase context | `llama-server` Vulkan/RADV first, test ROCm/HIP for prompt-heavy ingestion | 128K prompt plus generation completed; HIP can win prompt processing | [`data/filled_kv_decode.csv`](data/filled_kv_decode.csv), [`BACKEND_CROSSOVER.md`](BACKEND_CROSSOVER.md) |
| Prompt-heavy ROCm experiments | Keep a reproducible ROCm/HIP + ZenDNN path available, but do not treat it as a decode-speed headline. | A community Beelink GTR9 Pro on CachyOS / kernel 7.0.11 / ROCm 7.2.4 / ZenDNN measured Qwen3.6 27B MTP `UD-Q6_K_XL` at 303.20 pp5000 on ROCm versus 155.89 pp5000 on Vulkan, while decode stayed around 8 t/s on both backends. | [`BACKEND_CROSSOVER.md`](BACKEND_CROSSOVER.md#community-beelink-cachyos-rocmzendnn-crossover), [`COMMUNITY_RESULTS.md`](COMMUNITY_RESULTS.md#beelink-gtr9-pro-cachyos-rocmzendnn-crossover) |
| NPU sidecar work | Treat the NPU as a possible low-overhead sidecar, not as a replacement for the main iGPU LLM path. | A ciru-ai GMKtec EVO-X2 NixOS artifact kept IOMMU enabled and measured only +3.29% main 64k iGPU workload latency with concurrent NPU load, versus +68.96% with a comparable iGPU auxiliary load. The same package reports FastFlowLM-NPU LFM2.5 1.2B at 32k around 1646 prompt tok/s, 38.18 decode tok/s, and about 2.09GiB RSS. | [`COMMUNITY_RESULTS.md#gmktec-evo-x2-nixos--npu--rocmfp4-evidence-package`](COMMUNITY_RESULTS.md#gmktec-evo-x2-nixos--npu--rocmfp4-evidence-package), [`data/community_ciru_evox2_metrics.csv`](data/community_ciru_evox2_metrics.csv) |
| vLLM-style serving experiments | Start with isolated ROCm containers; for ROCm 7.14 plus PyTorch before 2.14, A/B `TORCH_BLAS_PREFER_HIPBLASLT=1` at batch 8+ | The local Qwen3-0.6B FP16 A/B measured about 39-42% more aggregate throughput at concurrency 8/9/16. This validates the setting and container path, but no practical 27B/35B vLLM throughput claim exists yet. | [`processed A/B`](data/rocm_714_hipblaslt_ab.csv), [`ROCM_VLLM_BUGWATCH.md`](ROCM_VLLM_BUGWATCH.md) |
| Sustained inference on a Corsair/Sixunited AXB35 system | Verify the expected EC/fan module and dependent services after every kernel update before applying a clock cap. | A strict three-system campaign found a useful 2400 MHz fleet tradeoff, but historical journals also showed missing `ec_su_axb35` modules and failed fan services after updates. The root cause remains unresolved and the cap is not universal. | [`THERMAL_STABILITY.md`](THERMAL_STABILITY.md), [`data/community_thermal_sclk.csv`](data/community_thermal_sclk.csv) |

## Community-Tested Rules Of Thumb

These are the practical decisions extracted from the primary Beelink runs plus community reports from Corsair, GMKtec, MS-S1-Max, Nimo, a second Beelink owner stack, and a ciru-ai GMKtec EVO-X2 NixOS/NPU artifact. Use them to avoid retesting dead ends first; follow the evidence links if your setup differs.

| Situation | Do this first | Why | Evidence |
|-----------|---------------|-----|----------|
| One Strix Halo AI PC | Use Vulkan/RADV for GGUF chat, coding, and generation-heavy inference. | It is the fastest measured practical path for the main Qwen MoE rows. | [`headline claims`](data/headline_claims.csv), [`COMMUNITY_RESULTS.md`](COMMUNITY_RESULTS.md) |
| Native Linux on another Strix Halo vendor | Expect the same performance class if backend, model, quant, and command match. | GMKtec EVO-X2 96GB on Ubuntu 26.04, Mesa RADV 26.0.3, and llama.cpp b9156 reproduced the guide's Qwen3.6 UD-Q4_K_M row within -0.8% pp512 and -1.7% tg128. | [`COMMUNITY_RESULTS.md`](COMMUNITY_RESULTS.md), [#16](https://github.com/hogeheer499-commits/strix-halo-guide/issues/16) |
| Comparing Qwen3-Coder rows | Preserve the exact model hash, build and command flags before calling one system faster. | The August 26 GMKtec follow-up supplies hashes and direct rows of 99.08 tg128 for `Q4_K_S` and 96.75 for `UD-Q4_K_XL`. It strengthens portability evidence; runtime, model and batch differences still prevent an OEM ranking. | [Community follow-up](COMMUNITY_RESULTS.md#gmktec-evo-x2-four-model-follow-up--august-26), [raw bundle](data/raw/2026-08-26/community-gmktec-issue4/README.md) |
| Handling "older model" criticism | Add current-model rows, but keep speed and capability separate. | Qwen3-Coder-Next IQ4_XS runs locally at 61.91 t/s on the Beelink with b9467. That is a useful modern coding-model result, but it does not replace the older Qwen3-Coder 30B Q4_K_S speed-first headline. | [`raw Qwen3-Coder-Next run`](data/raw/2026-06-02/modern-model-clean-followup/), [`data/benchmarks.csv`](data/benchmarks.csv) |
| Tuning `llama.cpp` batch flags | Check that `-ub` is not larger than `-b` before any other tuning. | `-ub` above `-b` is silently clamped to `min(n_batch, n_ubatch)` with no warning. A community GTR9 Pro report measured +28.9% pp512 from correcting `-b 256 -ub 1024` to `-b 2048 -ub 512`, and a further +16.9% pp512 / +3.1% tg128 from upgrading stock Mesa 25.2.8 to kisak 26.1.7 (no reboot needed; RADV is userspace). | [`COMMUNITY_RESULTS.md`](COMMUNITY_RESULTS.md), [`raw note`](data/raw/2026-08-21/community-reddit-ornery-ub-clamp/) |
| Seeing a direct 100 t/s 30B-class Qwen result | Check the exact model, quant, build, and claim category before comparing. | There are now two separate first-party direct 100-class Qwen rows: Qwen3-Coder 30B-A3B `Q4_K_S` at 100.99 t/s on official b9851, and Qwen3-30B-A3B-Instruct-2507 `IQ4_XS` at 100.04 t/s on b9467 with a b9544 control at 103.18 t/s. The Qwen3-Coder row is speed-first, not the balanced default; the 2507 row is a separate general-instruct model. | [`b9851 Qwen3-Coder raw`](data/raw/2026-06-30/latest-llamacpp-b9851-vulkan-sentinel/), [`2507 raw scout`](data/raw/2026-06-02/qwen3-30b-a3b-2507-direct-scout/), [`headline claims`](data/headline_claims.csv) |
| Seeing Qwen3-Coder around 100 t/s on another Strix Halo box | Treat it as a tuned-system clue, not a default claim. Capture thermals, power policy, Vulkan device line, `glslc --version`, driver/toolchain details, and exact command. | A Reddit GMKtec EVO-X2 report saw most `Q4_K_S -p 0 -n 128` runs around 99.90 t/s and a best 100.0 t/s after repasting, reseating memory pads, and using GPU `high` plus CPU EPP `performance`. Local Beelink b9467 follow-ups stayed around 95.27-96.72 t/s, so thermals/power/toolchain still need to be separated before calling this generally reproducible. | [`COMMUNITY_RESULTS.md#reddit-gmktec-evo-x2-tuned-100-ts-report`](COMMUNITY_RESULTS.md#reddit-gmktec-evo-x2-tuned-100-ts-report), [`PERFORMANCE_NOTES.md#vulkan-integer-dot-and-100-ts-reproduction-status`](PERFORMANCE_NOTES.md#vulkan-integer-dot-and-100-ts-reproduction-status), [`raw reproduction`](data/raw/2026-06-02/reddit-look-int-dot-reproduction/) |
| Starting on Windows | LM Studio Vulkan is now a documented Windows path, but keep it separate from Linux `llama-bench`. | The first Windows MS-S1-Max report measured a 89.49 tok/s script average through LM Studio with `n_parallel=4` and 262K context; the long 512-token prompt rows were around 69-70 tok/s. This is useful Windows buyer evidence, not a same-machine Windows-vs-Linux comparison. | [`COMMUNITY_RESULTS.md#windows-lm-studio-ms-s1-max-report`](COMMUNITY_RESULTS.md#windows-lm-studio-ms-s1-max-report), [`raw Windows report`](data/raw/2026-06-02/community-windows-lmstudio-issue3/) |
| Evaluating a compact non-Beelink chassis | Look for setup metadata, thermal context, and large-model feasibility, not only headline t/s. | The Nimo AI Mini PC issue #4 bundle adds Ubuntu 25.04 / Mesa 25.2.8 / ROCm rows, Qwen 122B-class serving, StepFun 198B-class serving, Qwen3-Coder-Next server rows, DFlash negative/control evidence, Gemma 4 QAT/MTP assistant-head follow-up data, and supplemental fan/power/temperature telemetry. | [`COMMUNITY_NIMO.md`](COMMUNITY_NIMO.md), [`data/community_nimo_issue4.csv`](data/community_nimo_issue4.csv), [`raw Nimo bundle`](data/raw/2026-06-03/community-nimo-issue4/), [`Gemma QAT follow-up`](data/raw/2026-06-06/community-nimo-gemma4-qat-issue4/) |
| Choosing an IOMMU policy | Keep IOMMU enabled/default for normal systems, NPU work, and mobile suspend. Use `amd_iommu=off` only for the optional always-on desktop benchmark profile. | The Beelink headline profile preserves the measured performance route, while the safer general default avoids silently losing the NPU or deep laptop/tablet sleep. ciru-ai's GMKtec EVO-X2 NixOS artifact also shows an IOMMU-on stack where the NPU can run sidecar work with low measured main-workload impact. | [setup policy](#step-12-choose-the-iommu-policy), [`COMMUNITY_RESULTS.md#gmktec-evo-x2-nixos--npu--rocmfp4-evidence-package`](COMMUNITY_RESULTS.md#gmktec-evo-x2-nixos--npu--rocmfp4-evidence-package) |
| Testing MTP/speculative decoding | Treat MTP as an advanced server route, not a direct benchmark replacement. | The Qwen3.6 MTP IQ4_XS-Q8nextn route has a local b9360 rerun at 101.16 t/s and a GMKtec b9235 reproduction at 93.29 t/s. The Gemma 4 26B-A4B QAT route adds a current Google-model matched-head example at 102.69-110.00 t/s. The exact CHADROCK ACE/SABER reference profile averaged 141.37 t/s over three repeats at 100% acceptance, while lower-acceptance shapes were much slower. | [`MTP_SPECULATIVE_DECODING.md`](MTP_SPECULATIVE_DECODING.md), [`ROCMFP4_CHADROCK.md`](ROCMFP4_CHADROCK.md), [`data/mtp_speculative.csv`](data/mtp_speculative.csv), [#18](https://github.com/hogeheer499-commits/strix-halo-guide/issues/18) |
| The model fits on one Strix Halo box | Do not use `llama.cpp` RPC for raw single-stream speed. | 2-node RPC lost about 14-22% tg128 on fits-on-one models; 3-node was slower again. | [`COMMUNITY_RPC.md`](COMMUNITY_RPC.md), [`data/community_rpc.csv`](data/community_rpc.csv) |
| A huge GGUF does not fit on one box | Try ROCm RPC first, starting with the smallest node count that fits. | In the tested MiniMax-M2.7 140.8GB case, one box failed, 2-node ROCm worked, and 3-node ROCm was slower. This is a capacity rule from that case, not a universal speedup rule. | [`COMMUNITY_RPC.md`](COMMUNITY_RPC.md) |
| Testing huge MoE capacity on one box | Separate "loads and processes prompts" from "fast generation". | A Corsair AI Workstation 300 `ai-2` community row loaded MiMo-V2.5 `UD-IQ2_M`, a 310B-total / 15B-active GGUF route, and measured 30.65 pp512 with wall-power/GPU telemetry. The pasted CSV row has `n_gen=0`, so it is capacity/telemetry evidence, not a tg128 speed claim. | [`COMMUNITY_RESULTS.md#corsair-ai-workstation-300-mimo-v25-capacity-row`](COMMUNITY_RESULTS.md#corsair-ai-workstation-300-mimo-v25-capacity-row), [#26](https://github.com/hogeheer499-commits/strix-halo-guide/issues/26) |
| Building a USB4 Strix Halo cluster | Start with MTU 9000 and `pm_qos_resume_latency_us=100`. | MTU 9000 beat 1500 and 65520; `pm_qos` added about +2% tg128 with only about 1.5 W idle cost per toggled box in the community report. | [`USB4_CLUSTER_TUNING.md`](USB4_CLUSTER_TUNING.md) |
| Choosing Qwen3.6 quantization | Use Q4_K_M/UD-Q4_K_M for balanced defaults; use Q4_0 only when speed matters more than quality. | Q4_0 was faster locally and in the Corsair report, but this guide has not made a model-quality claim for it. | [`COMMUNITY_RESULTS.md`](COMMUNITY_RESULTS.md), [`data/community_results.csv`](data/community_results.csv) |
| Serving an interactive local API | Prefer single-box `llama-server` when the model fits. | Community `llama-server` TTFT was about 201 ms on 1 node versus about 301 ms on 2-node RPC, with higher RPC variance. | [`COMMUNITY_RPC.md`](COMMUNITY_RPC.md), [`data/community_rpc_server.csv`](data/community_rpc_server.csv) |
| Comparing your t/s to this guide | Treat about 2% tg128 spread as normal between well-matched Strix Halo systems. | Three matched Corsair boxes showed 0.11% pp512 spread and 2.05% tg128 spread; the GMKtec native Qwen3.6 row landed within 2% of the Beelink row. | [`COMMUNITY_RESULTS.md`](COMMUNITY_RESULTS.md) |
| Estimating electricity and heat | Use wall-power rows as workload-specific context, not universal TDP. | Community wall-power data measured about 150 W / 1.6 J/token for Qwen3-Coder, 148 W / 2.0 J/token for Qwen3.6, 174 W / 3.1 J/token for gpt-oss-120b, and 137 W / 3.4 J/token for Qwen3-Coder-Next. | [`COMMUNITY_RESULTS.md#whole-system-power`](COMMUNITY_RESULTS.md#whole-system-power), [`data/community_power.csv`](data/community_power.csv) |
| Seeing a Vulkan/RADV failure on a huge MoE | Check for per-buffer allocation limits, not only total memory. | MiniMax-M2.7 hit the same 830472192-byte RADV allocation failure on 1-node and RPC follower paths. | [`data/community_rpc_failures.csv`](data/community_rpc_failures.csv), [`COMMUNITY_RPC.md`](COMMUNITY_RPC.md) |

## Results Wanted

Have a Strix Halo / Ryzen AI MAX system? Please share results, even if they are slower, failed, or contradict this guide.

- Open a [benchmark report](https://github.com/hogeheer499-commits/strix-halo-guide/issues/new?template=benchmark-report.md) with your system, BIOS UMA setting, kernel, Mesa/ROCm versions, backend, model, command, CSV/raw output, and notes.
- Open a [power / efficiency report](https://github.com/hogeheer499-commits/strix-halo-guide/issues/new?template=power-report.md) if you can measure wall power, UPS power, or validated board power during the same benchmark command.
- Open a [model request](https://github.com/hogeheer499-commits/strix-halo-guide/issues/new?template=model-request.md) if there is a model/backend combination that should be tested.
- Use [Discussions](https://github.com/hogeheer499-commits/strix-halo-guide/discussions) for setup questions, comparisons, and early results that are not ready for a benchmark issue yet.
- Power telemetry is useful if you have reliable wall-power data; it helps turn raw tokens/sec into tokens-per-watt context for buying, cooling, and always-on server decisions.
- Current community reports live in [`COMMUNITY_RESULTS.md`](COMMUNITY_RESULTS.md), [`COMMUNITY_NIMO.md`](COMMUNITY_NIMO.md), [`COMMUNITY_RPC.md`](COMMUNITY_RPC.md), [`USB4_CLUSTER_TUNING.md`](USB4_CLUSTER_TUNING.md), and the `community_*` CSVs listed in [`data/README.md`](data/README.md).
- See [`SHARE.md`](SHARE.md) for short Reddit/HN/forum text and the current social preview image if you want to share the guide.

## For Vendors, Partners, And Reviewers

This guide is primarily a technical resource for AMD Strix Halo local-AI users. For vendors, reviewers, and partners, it also documents a reproducible way to reduce buyer setup friction and validate real-world local-AI use cases without weakening independent benchmark discipline.

Start with the public [vendor and reviewer overview](https://strixhaloguide.com/partners/), then inspect the linked GitHub evidence, raw artifacts, negative results, disclosure policy, and upstream contribution record here.

Start with [`ONE_PAGE_BRIEF.md`](ONE_PAGE_BRIEF.md) and [`PARTNERSHIP.md`](PARTNERSHIP.md). Supporting docs cover [`SPONSORSHIP.md`](SPONSORSHIP.md), [`VENDOR_DISCLOSURE.md`](VENDOR_DISCLOSURE.md), [`BUYER_USE_CASES.md`](BUYER_USE_CASES.md), [`SPONSOR_ROADMAP.md`](SPONSOR_ROADMAP.md), and [`TRACTION.md`](TRACTION.md). How vendors can report a factual error, how vendor responses are recorded and how hardware provenance is disclosed: [How We Work With Vendors](VENDOR_DISCLOSURE.md#how-we-work-with-vendors).

No affiliate links are present as of September 19, 2026. The links added on October 1, 2026
were checked by URL pattern for tracking parameters and affiliate-network domains and none was
found (the destinations themselves were not inspected). If monetized product
links are added later, each relevant link will be labeled and recorded in the
public [`affiliate link registry`](data/affiliate_link_registry.csv). Affiliate
commission does not determine benchmark conclusions, product inclusion, or
ranking.

## Best Current Setup Tested Here

These are the AMD Strix Halo / Ryzen AI MAX+ 395 configurations behind this guide's measured results. Pick the starting point that matches what you want to do; each result applies to the exact versions it was recorded with.

New to local AI? Follow the [complete start route](LOCAL_CHAT_START.md). It
keeps installation, the first answer, the GPU check and help with errors on one
page, and treats a browser interface as the next step for daily use. The
measured profiles below were recorded on an existing setup; they are not proof
that a fresh run of the revised installer works.

Choose the backend by what you are trying to do:

| Use case | Do this first | Why |
|----------|---------------|-----|
| You want to get local AI running | Follow [the complete start route](LOCAL_CHAT_START.md). | Installation, a visible answer, a GPU check and help with errors on one page. |
| You want to reproduce the headline speed rows | Use [Reproduce One Headline Result](#reproduce-one-headline-result). | Exact model, quant, build, and command matter for benchmark comparisons. |
| You want a local API server or MTP tests | Read [MTP/speculative decoding](MTP_SPECULATIVE_DECODING.md) and use `llama-server`. | Supports serving, batching, long-context tests, and speculative decoding. |
| You have many parallel local requests | Read [SERVER_SHOOTOUT.md](SERVER_SHOOTOUT.md) for the measured Lemonade `llamacpp-rocm` b1259 profile before planning a new comparison. | The 8-16 parallel advice was measured on 2026-05-05. [Lemonade v11.9.0](https://github.com/lemonade-sdk/lemonade/releases/tag/v11.9.0), checked September 19, is available but unqualified here and has not inherited that result. |
| You are testing prompt-heavy, vLLM, or future server paths | Read [BACKEND_CROSSOVER.md](BACKEND_CROSSOVER.md) and [VLLM_BASELINE.md](VLLM_BASELINE.md). | Useful for prompt processing, batching, vLLM, and long-context experiments. |

Once your first answer has passed its checks, choose a model and an interface for your daily work from [the start route](LOCAL_CHAT_START.md). To compare numbers, use the exact commands and evidence links in [Reproduce One Headline Result](#reproduce-one-headline-result), the [AI/search setup summary](STRIX_HALO_LOCAL_LLM_SETUP.md), [headline claim index](data/headline_claims.csv), and raw evidence under [`data/raw/`](data/raw/).

## Headline Evidence

The machine-readable index for these rows is [`data/headline_claims.csv`](data/headline_claims.csv).

Dates below are measurement dates. A row being from May does not mean it is stale; it means later checks did not produce a stronger replacement headline. The latest controls and current-model rows are documented in [`CURRENT_MODELS.md`](CURRENT_MODELS.md), [`BENCHMARKS.md`](BENCHMARKS.md), [`PERFORMANCE_NOTES.md`](PERFORMANCE_NOTES.md), and the raw evidence links below.

| Claim | Date | Backend | Model | Result | CSV | Raw | Chart | Notes |
|-------|------|---------|-------|--------|-----|-----|-------|-------|
| Fastest direct 30B-class Qwen MoE route | 2026-06-02; b9544 control 2026-06-07 | llama.cpp Vulkan/RADV b9467; b9544 | Qwen3-30B-A3B-Instruct-2507 IQ4_XS | 100.04 tg128 r50, 1416.03 pp512; b9544 control 103.18 tg128 r10 | [`benchmarks`](data/benchmarks.csv) | [`raw r50`](data/raw/2026-06-02/qwen3-30b-a3b-2507-direct-scout/qwen3-30b-2507-iq4xs-b9467-r50.csv), [`b9544 control`](data/raw/2026-06-07/latest-llamacpp-b9544-regression/) | n/a | first local direct `llama-bench` row above 100 t/s; separate general-instruct Qwen route; not the Qwen3-Coder headline or balanced default |
| Fastest current small-MoE scout | 2026-06-05; b9544 control 2026-06-07 | llama.cpp Vulkan/RADV 2016bf2; b9544 | LFM2.5 8B-A1B Q4_K_M | 168.96 tg128, 3414.61 pp512; generation-only 170.02 tg128; b9544 control 176.48 tg128 r10 | [`benchmarks`](data/benchmarks.csv) | [`raw latest/int-dot`](data/raw/2026-06-05/latest-llamacpp-intdot-regression/), [`b9544 control`](data/raw/2026-06-07/latest-llamacpp-b9544-regression/) | n/a | small active-parameter MoE speed/currentness row; not a 30B-class model replacement |
| Largest current direct GGUF capacity route | 2026-07-16 | llama.cpp Vulkan/RADV b10034 | DeepSeek V4 Flash 284B UD-IQ2_XXS | 155.64 pp512 / 13.27 tg128 r3; deterministic answer `9` | [`benchmarks`](data/benchmarks.csv) | [`raw direct pass`](data/raw/2026-07-16/deepseek-v4-flash-ud-iq2-xxs/) | n/a | pinned 90.86GB ordinary GGUF; direct load/basic-correctness capacity proof, not a speed or broad quality recommendation |
| Current 120B-class direct GGUF route | 2026-06-05; b9544 control 2026-06-07 | llama.cpp Vulkan/RADV 2016bf2; b9544 | Nemotron 3 Super 120B-A12B UD-IQ4_XS | 18.43 tg128, 294.99 pp512; b9544 control 18.93 tg128 r3 | [`benchmarks`](data/benchmarks.csv) | [`raw latest/int-dot`](data/raw/2026-06-05/latest-llamacpp-intdot-regression/), [`b9544 control`](data/raw/2026-06-07/latest-llamacpp-b9544-regression/) | n/a | direct 120B-class MoE route on one 128GB Strix Halo system; capacity/current-model proof, not a speed headline |
| Fastest measured short-context coding MoE speed-first quant | 2026-06-30 | llama.cpp Vulkan/RADV b9851 official release binary | Qwen3-Coder 30B-A3B Q4_K_S | 100.99 tg128 r50, 1423.05 pp512 | [`benchmarks`](data/benchmarks.csv) | [`raw r50`](data/raw/2026-06-30/latest-llamacpp-b9851-vulkan-sentinel/qwen3-coder-q4ks-b9851-p512-n128-r50.csv) | n/a | speed-first lower-quality quant; not the balanced UD default; older b9179 strict-clean row remains preserved at 98.51 t/s |
| Fast balanced short-context coding MoE | 2026-05-07 | llama.cpp Vulkan/RADV b9049 | Qwen3-Coder 30B-A3B UD-Q4_K_XL | 96.76 tg128, 1320.52 pp512 | [`max campaign`](data/max_performance_campaign.csv) | [`raw run`](data/raw/2026-05-07/max-performance-campaign/benchmarks/qwen3-coder-top-confirm-r20/guide.csv) | n/a | max-performance r20 confirmation; previous b9010 peak was 97.24 t/s |
| Default Qwen3.6 direct path | 2026-05-07 | llama.cpp Vulkan/RADV b9049 | Qwen3.6 35B-A3B UD-Q4_K_M | 62.56 tg128, 1059.45 pp512 | [`benchmarks`](data/benchmarks.csv) | [`raw run`](data/raw/2026-05-07/latest-stack-rerun/clean-b9049-rerun/qwen36-35b-b9049-clean-r20.csv) | [`chart`](charts/backend_spot_check.svg) | clean latest-stack r20 rerun; rounds to 63 t/s |
| Fastest measured Qwen3.6 speed-first quant | 2026-05-07 | llama.cpp Vulkan/RADV b9049 | Qwen3.6 35B-A3B Q4_0 | 81.30 tg128, 1243.51 pp512 | [`max campaign`](data/max_performance_campaign.csv) | [`raw run`](data/raw/2026-05-07/max-performance-campaign/benchmarks/qwen36-top-confirm-r20/q4-0-ub2048.csv) | n/a | speed-first lower-quality quant; not the default all-round recommendation without a quality sanity check |
| Current normal Ollama buyer path | 2026-07-10 | Ollama 0.31.2 system service Vulkan/RADV | Qwen3.6 35B-A3B Q4_K_M | 60.57 t/s warm API generation average | [`benchmarks`](data/benchmarks.csv) | [`raw service run`](data/raw/2026-07-10/ollama-0312-buyer-path/) | n/a | normal service-upgrade path; iGPU, vision, service restart, and full-host reboot persistence passed; later controlled local binaries did not reproduce a version-wide slowdown |
| Experimental Qwen3.6 MTP server path | 2026-05-27 | `llama-server` Vulkan/RADV b9360 | Qwen3.6 35B-A3B MTP IQ4_XS-Q8nextn | 101.16 t/s best local average over six prompts; t16 repeats at 101.15 / 101.10 / 101.06 t/s; 93.29 t/s GMKtec community average on b9235 | [`MTP CSV`](data/mtp_speculative.csv) | [`local raw`](data/raw/2026-05-27/latest-llamacpp-b9360/), [`GMKtec raw`](data/raw/2026-05-19/community-gmktec-mtp-issue18/) | n/a | server/speculative result; localweights Q8-next-token-head quant; not the direct `llama-bench` headline |
| Experimental Gemma 4 QAT MTP server path | 2026-06-12 | `llama-server` Vulkan/RADV ac4cddeb0 | Gemma 4 26B-A4B IT QAT UD-Q4_K_XL + Q4_0 MTP head | 102.69 t/s cold repeat; 107.42 t/s T3-only repeat; 110.00 t/s best repeat; 73.96 t/s no-spec baseline | [`MTP CSV`](data/mtp_speculative.csv) | [`cold raw`](data/raw/2026-06-12/gemma4-26b-qat-mtp-cold-repeat-ac4cddeb/), [`T3-only raw`](data/raw/2026-06-12/gemma4-26b-qat-mtp-t3-only-repeat-ac4cddeb/), [`warm raw`](data/raw/2026-06-11/gemma4-26b-qat-mtp-sixprompt-ac4cddeb/) | n/a | historical server/speculative result with matched QAT MTP head; sampled coding outputs failed and profile is not recommended (see the [saved-output review](BEST_KNOWN_PROFILES.md#historical-throughput-sampled-coding-outputs-failed)); host-workload sensitive; not direct `llama-bench` |
| Experimental CHADROCK ROCmFP4 MTP server path | 2026-06-21 | `llama-server` ROCmFPX/RADV helper route | CHADROCK ACE/SABER 35B ROCmFP4 | 140.40 and 139.93 t/s gen512 high-acceptance repeats; 127.77 t/s gen2048 check | [`MTP CSV`](data/mtp_speculative.csv) | [`raw helper repro`](data/raw/2026-06-21/rocmfpx-chadrock-ace-saber-helper-repro/) | n/a | server/speculative result with `ciru-ai/ROCmFPX`; prompt/acceptance-sensitive; not direct `llama-bench` |
| Historical May 80B Qwen-family path | 2026-05-16 | llama.cpp Vulkan/RADV b9172 | Qwen3-Next 80B-A3B UD-Q4_K_XL | 59.06 tg128, 751.70 pp512 | [`benchmarks`](data/benchmarks.csv) | [`raw r20`](data/raw/2026-05-16/latest-stack-b9172/qwen3-next-confirm-r20/qwen3-next-80b-b9172-ub1024-r20.csv) | n/a | b9172 improved this 80B MoE path versus the older 54.92 t/s b8933 row |
| gpt-oss-120b loaded locally | 2026-05-07 | llama.cpp Vulkan/RADV b9049 | gpt-oss-120b MXFP4 split GGUF | 55.57 tg128, 726.99 pp512, 293.73 pp65536 r1 | [`max campaign`](data/max_performance_campaign.csv) | [`raw run`](data/raw/2026-05-07/max-performance-campaign/benchmarks/gpt-oss-120b-long-context-vulkan/) | n/a | performance evidence only; no model-quality eval; pp65536 is one repeat |
| User-local Ollama comparator | 2026-07-02 | Ollama 0.31.1 local binary Vulkan/RADV | Qwen3.6 35B-A3B Q4_K_M | 71.82 t/s warm API generation average | [`benchmarks`](data/benchmarks.csv) | [`raw API run`](data/raw/2026-07-02/ollama-0311-qwen36-buyer-path/) | n/a | 9 warm API runs after one cold run; required `OLLAMA_IGPU_ENABLE=1`; faster than the earlier normal-service check, but a later controlled comparison found no version-wide 0.31.2 regression |
| Best measured Qwen3.6 server split | 2026-05-05 | Vulkan/RADV and Lemonade ROCm | Qwen3.6 35B-A3B UD-Q4_K_M | Vulkan wins 1-4 parallel; Lemonade ROCm wins 8-16 | [`server data`](data/server_shootout.csv) | [`raw sweep`](data/raw/2026-05-05/server-shootout/full-sweep-qwen36-workstation-baseline/summary.csv) | n/a | 5 reps per concurrency, 0 errors |
| HIP/Vulkan workload split | 2026-05-07 | Vulkan/RADV and ROCm/HIP from b9049 source | Qwen3.6 35B-A3B, Qwen3-Coder 30B-A3B | HIP won pp16384; Vulkan won tg128 on both local Qwen rows | [`max campaign`](data/max_performance_campaign.csv) | [`same-source matrix`](data/raw/2026-05-07/max-performance-campaign/benchmarks/same-build-hip-vulkan-b9049/) | n/a | HIP binary reports unknown build id due container git safe-directory, but source checkout was b9049 |
| Best measured Qwen3-Coder local API point | 2026-05-03 | `llama-server` Vulkan/RADV b9010 | Qwen3-Coder 30B-A3B UD-Q4_K_XL | 173.16 aggregate t/s at `-np 8` | [`multi-user`](data/multi_user.csv) | [`raw summary`](data/raw/2026-05-03/multi-user-coder/qwen3-coder-30b-ud-llama-server-multi-user-summary.csv) | [`chart`](charts/multi_user_aggregate.svg) | `-np 16` regressed |
| 128K filled-context Qwen3.6 decode completed | 2026-05-03 | `llama-server` Vulkan/RADV b9010 | Qwen3.6 35B-A3B UD-Q4_K_M | 32.23 t/s decode after 128K fill, no truncation | [`filled KV`](data/filled_kv_decode.csv) | [`raw 128K summary`](data/raw/2026-05-03/filled-kv-decode-128k/filled-kv-decode-128k-summary.csv) | [`chart`](charts/filled_kv_decode.svg) | f16 KV, synthetic long prompt |
| Real documents are slower than synthetic repeated prompts | 2026-05-03 | `llama-server` Vulkan/RADV b9010 | Qwen3.6 35B-A3B and Qwen3-Next 80B-A3B | real 64K prompt ingest was 24-33% slower; decode barely changed | [`filled KV`](data/filled_kv_decode.csv) | [`real-corpus summary`](data/raw/2026-05-03/filled-kv-decode-real-corpus/filled-kv-decode-real-corpus-summary.csv) | [`chart`](charts/real_vs_synthetic.svg) | avoids overclaiming synthetic prompt speed |

## Reproduce One Headline Result

Pick the row that matches what you want to verify. The balanced coding row is the best first reproduction target for most users. The direct 100 t/s row is useful if you specifically want to verify the fastest measured 30B-class Qwen speed scout. Keep them separate: they use different model files, quants, builds, and quality tradeoffs.

### Balanced Qwen3-Coder Row

```bash
AMD_VULKAN_ICD=RADV \
VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/radeon_icd.json \
~/llama-cpp-upstream-2026-05-07/build-vulkan/bin/llama-bench \
  -m ~/models/Qwen3-Coder-30B-A3B-Instruct-UD-Q4_K_XL.gguf \
  -fa 1 -ngl 999 -mmp 0 -p 0 -n 128 -r 20 -o csv
```

Measured local result: 96.76 tg128 in the max-performance b9049 campaign: [`raw CSV`](data/raw/2026-05-07/max-performance-campaign/benchmarks/qwen3-coder-top-confirm-r20/guide.csv). This is the practical balanced Qwen3-Coder row. The fastest first-party Qwen3-Coder row is now 100.99 tg128 with Q4_K_S on the official b9851 Vulkan release binary, but that is a speed-first quant rather than the balanced default: [`raw b9851 r50`](data/raw/2026-06-30/latest-llamacpp-b9851-vulkan-sentinel/qwen3-coder-q4ks-b9851-p512-n128-r50.csv). The older b9179 strict-clean 98.51 t/s row remains preserved for historical host-state context: [`raw b9179 r50`](data/raw/2026-05-16/break-97-24-strict-noise-settings/b9179-q4-k-s-r50.csv).

### Direct 100 t/s Qwen3 30B Speed Scout

Use this only if you have the exact `Qwen3-30B-A3B-Instruct-2507` `IQ4_XS-3.63bpw` GGUF and a comparable b9467 Vulkan/RADV build. Adjust the binary and model paths to your checkout; the flags, model hash, build, and raw CSV are the reproducibility anchors. This is a direct `llama-bench` result, but it is not Qwen3-Coder and not the balanced default.

```bash
AMD_VULKAN_ICD=RADV \
VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/radeon_icd.json \
~/llama-cpp-b9467/build-vulkan/bin/llama-bench \
  -m ~/models/Qwen3-30B-A3B-Instruct-2507-IQ4_XS-3.63bpw.gguf \
  -fa 1 -ngl 999 -mmp 0 -b 2048 -ub 512 -t 16 --poll 50 -p 512 -n 128 -r 50 -o csv
```

Measured local result: 100.04 tg128 and 1416.03 pp512 on the r50 confirmation: [`raw r50`](data/raw/2026-06-02/qwen3-30b-a3b-2507-direct-scout/qwen3-30b-2507-iq4xs-b9467-r50.csv), [`model hash`](data/raw/2026-06-02/qwen3-30b-a3b-2507-direct-scout/model-iq4xs.sha256), [`scout notes`](data/raw/2026-06-02/qwen3-30b-a3b-2507-direct-scout/README.md).

## Not Yet Proven Here

- A first-party Beelink wall-power tokens-per-watt claim. Local amdgpu `PPT` telemetry exists, and community Corsair wall-power rows exist, but the guide still needs a Beelink wall-meter run before publishing Beelink J/token claims.
- Same-machine Windows versus Linux performance. Windows LM Studio and WSL2/HIP community rows now exist, but they are not same-machine, same-model, same-shape comparisons against native Linux Vulkan/RADV.
- A default or balanced first-party 100 t/s Qwen3-Coder claim. The first-party Qwen3-Coder `Q4_K_S` speed-first row now reaches 100.99 t/s on b9851, but the practical balanced `UD-Q4_K_XL` row remains in the 96-99.6 t/s class depending on build/repeat length. A tuned community GMKtec report touched 100.0 t/s on Qwen3-Coder, and a separate first-party Qwen3-30B-A3B-Instruct-2507 IQ4_XS route reached 100.04 t/s, but those are separate evidence categories.
- Production-ready NPU/FastFlowLM inference. In the May 16 preflight the kernel saw `amdxdna` and `/dev/accel/accel0`, but XRT/FastFlowLM user-space is not installed and no local NPU LLM row is published yet.
- A broadly useful DFlash/PFlash speedup on Strix Halo. The official Gemma 4 31B QAT target and matched DFlash sidecar now load and serve on b10066, but DFlash `n_max=8` was 5.54% slower at 5,471 prompt tokens and 20.42% slower at 21,855 on the measured synthetic shapes because acceptance stayed low. Representative chat, coding, and reasoning prompts still need separate profiling.
- A vLLM/DFlash server path that competes with `llama-server` or Ollama for a real 35B Strix Halo use case. Plain AWQ without the gated DFlash drafter was only a smoke test here at about 25 t/s.
- A pinned current-HIP long-context comparison against the current Vulkan/RADV path. Historical external rocWMMA evidence exists, but upstream removed that kernel in 2026 and the older local lhl branch failed to load the current Qwen3.6 GGUFs.
- Multi-machine clustering numbers from this guide's own hardware. Community RPC and USB4 tuning data exists in [`COMMUNITY_RPC.md`](COMMUNITY_RPC.md) and [`USB4_CLUSTER_TUNING.md`](USB4_CLUSTER_TUNING.md), but it is not a local Beelink headline claim.

## Do Not Copy These Claims Without Matching Setup

These numbers are local measurements from one primary machine: a Beelink GTR9 Pro with Ryzen AI MAX+ 395 and 128GB LPDDR5X-8000. Treat the headline results as directional unless your setup matches the measured run closely.

Performance depends on the exact hardware SKU, RAM configuration, BIOS UMA setting, IOMMU setting, firmware, kernel, Mesa/RADV version, ROCm version, Vulkan ICD selection, power profile, GPU clocks, thermal state, backend commit/build flags/container image, model file, quant type, model hash/path, context length, prompt length, generated token count, batch size, parallel slots, request concurrency, API endpoint, environment variables, and background system load.

If your setup differs, rerun the benchmark scripts and cite the date, command, CSV, raw log, chart, model file, and backend version with any copied claim.

## Reuse And Citing The Numbers

Other projects and sites already read the data in this repository (see [`TRACTION.md`](TRACTION.md#where-the-data-is-reused-checked-2026-09-30)), and a number copied without its qualification can say more than the measurement shows. The repository license stays MIT (see [`LICENSE`](LICENSE)). When you cite a headline, keep its qualification next to it, and give the date, the commit or release you read, and the source file.

| Headline | Keep this qualification with it | Source |
| --- | --- | --- |
| 20.42 generation t/s, Qwen3.8 27B | Ollama API with Ollama-default MTP drafting (`draft_num_predict 4`), Ollama 0.32.13, one 128GB Beelink; not a no-draft result. A matched control on 2026-09-26 (Ollama 0.32.15, same blob and harness, routine background load) measured 12.89 t/s without drafting and 22.71 t/s with MTP. | [`QWEN38_STRIX_HALO.md`](QWEN38_STRIX_HALO.md), [raw control](data/raw/2026-09-26/qwen38-27b-ollama-03215-mtp-vs-nodraft/) |
| 141.37 t/s, CHADROCK ROCmFP4 | `llama-server` speculative decoding on the exact 3946-token reference prompt at 100% mean draft acceptance (three repeats, 140.84-141.79 range); not `llama-bench`. The 1K and 8K profiles measured 78.00 and 83.85 t/s as acceptance fell. | [`MTP_SPECULATIVE_DECODING.md`](MTP_SPECULATIVE_DECODING.md), [`data/best_known_profiles.csv`](data/best_known_profiles.csv) |
| 60.57 t/s, Qwen3.6 35B-A3B on Ollama | Ollama 0.31.2 system service, measured 2026-07-10 on the tag's earlier manifest `07d35212591f`; the current tag is an MTP build. A matched check on 2026-09-26 (Ollama 0.32.15, different harness: compare its arms with each other, not with 60.57) measured 70.25 t/s on the old manifest, 74.51 t/s on the current MTP manifest, and 70.35 t/s on the same blob without drafting. | [raw bundle](data/raw/2026-09-26/qwen36-35b-a3b-ollama-03215-manifest-mtp-check/) |
| 101.16 t/s (Qwen3.6 MTP) and 110.00 t/s (Gemma 4 QAT MTP) | `llama-server` speculative decoding with a matched MTP head; prompt shape and host workload change the result (Gemma 4: 102.69 t/s cold repeat, 73.96 t/s no-spec baseline). | [`MTP_SPECULATIVE_DECODING.md`](MTP_SPECULATIVE_DECODING.md), [`data/mtp_speculative.csv`](data/mtp_speculative.csv) |
| 100.99 and 100.04 t/s | Direct `llama-bench` tg128 at short context on one machine: a speed-first quant (Qwen3-Coder `Q4_K_S`) and a separate general-instruct model. Not server or MTP results. | [`data/headline_claims.csv`](data/headline_claims.csv) |

All first-party numbers come from one Beelink GTR9 Pro with 128GB; community rows are labeled as such. The notes for each headline claim are in [`data/headline_claims.csv`](data/headline_claims.csv). To cite this repository, use [`CITATION.cff`](CITATION.cff) and add the commit hash or release tag you used and the date you read it.

## Documentation Map

| File | Purpose |
|------|---------|
| [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) | Exact machine, BIOS/software state, commands, raw data paths, and chart generation. |
| [`SERVER_SHOOTOUT.md`](SERVER_SHOOTOUT.md) | Practical local-AI-server comparison: Ollama, `llama-server`, Lemonade ROCm, and vLLM candidates. |
| [`ENGINES.md`](ENGINES.md) | Inference engines for Strix Halo (Gufo, Halogen, forks, Lemonade, LM Studio, Ollama, `llama.cpp`): licence, claim class of each headline, what this guide verified (only its own `llama.cpp` and Ollama routes), questions to ask before running a community engine, and Ollama compared with other servers. |
| [`WINDOWS_START.md`](WINDOWS_START.md) | Starting on Windows: Variable Graphics Memory and the open large-model loading reports, AMD's official Windows routes, LM Studio versions and open issues, display-off throttling. Community and vendor sources, not measured by this guide. |
| [`LAPTOPS_AND_HOMELAB.md`](LAPTOPS_AND_HOMELAB.md) | Laptops and tablets, Proxmox/LXC and VMs, clusters (RPC, Ray), one 192GB box against two 128GB boxes, extra GPUs and the NAS form. Community sources, not measured by this guide. |
| [`BACKEND_CROSSOVER.md`](BACKEND_CROSSOVER.md) | HIP versus Vulkan workload split: prompt processing versus token generation. |
| [`POWER_BASELINE.md`](POWER_BASELINE.md) | Local amdgpu `PPT` telemetry status and Beelink power-sampling caveats. |
| [`PERFORMANCE_NOTES.md`](PERFORMANCE_NOTES.md) | Narrow notes on strict-stack reruns, failed headline reproduction attempts, and useful negative model results. |
| [`CURRENT_MODELS.md`](CURRENT_MODELS.md) | Current-model triage: latest model scouts, speed versus capability framing, and practical next-test value. |
| [`UNSLOTH_STRIX_HALO.md`](UNSLOTH_STRIX_HALO.md) | Measured local fine-tuning, GGUF export, ROCm deployment, persistence, and troubleshooting path. |
| [`data/current_test_queue.csv`](data/current_test_queue.csv) | Machine-readable current test priorities, readiness, artifact size, blockers, and evidence questions. |
| [`ROCM_VLLM_BUGWATCH.md`](ROCM_VLLM_BUGWATCH.md) | Fast-moving ROCm/vLLM upstream issue and release watchlist. |
| [`BENCHMARKS.md`](BENCHMARKS.md) | Compact benchmark source-of-truth for current README numbers. |
| [`COMMUNITY_RESULTS.md`](COMMUNITY_RESULTS.md) | Independent benchmark reports from other Strix Halo systems, kept separate from headline claims. |
| [`COMMUNITY_FEEDBACK.md`](COMMUNITY_FEEDBACK.md) | Community feedback loop: trust friction, public corrections, and how criticism turns into reproducible evidence. |
| [`COMMUNITY_NIMO.md`](COMMUNITY_NIMO.md) | Nimo AI Mini PC community bundle with large-model, MTP, StepFun, Qwen 122B, Gemma 4 QAT/MTP assistant-head, and thermal context. |
| [`COMMUNITY_RPC.md`](COMMUNITY_RPC.md) | Community multi-node `llama.cpp` RPC over USB4 results, kept separate from single-machine headline claims. |
| [`USB4_CLUSTER_TUNING.md`](USB4_CLUSTER_TUNING.md) | Community USB4 latency tuning for active Strix Halo cluster nodes. |
| [`THERMAL_STABILITY.md`](THERMAL_STABILITY.md) | Scoped Corsair/Sixunited sustained-inference evidence: SCLK tradeoffs, bounded stock controls, fan-module/service checks, raw telemetry, and upstream safety work. |
| [`ROCMFP4_CHADROCK.md`](ROCMFP4_CHADROCK.md) | Advanced ROCmFP4 / CHADROCK tuned-GGUF route tracking. The exact first-party reference profile averaged 141.37 t/s across three repeats at 100% acceptance, but other prompt shapes were much slower; it is not the beginner/default setup path or a direct `llama-bench` replacement. |
| [`UPSTREAM_CONTRIBUTIONS.md`](UPSTREAM_CONTRIBUTIONS.md) | Accepted upstream engineering work in `llama.cpp`, LocalAI, Qwen Code, OpenTelemetry GenAI, NVIDIA AICR, and vLLM GGUF tooling, with direct review links and claim boundaries. |
| [`CONTRIBUTORS.md`](CONTRIBUTORS.md) | Community benchmark contributor credits and contribution path. |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | What data is most useful, which issue template to use, and how community reports become structured evidence. |
| [`data/headline_claims.csv`](data/headline_claims.csv) | Machine-readable map from public headline claims to data, raw evidence, charts, and notes. |
| [`data/README.md`](data/README.md) | Structured CSV schema and raw-data conventions. |
| [`charts/README.md`](charts/README.md) | Generated chart inventory and regeneration command. |
| [`SHARE.md`](SHARE.md) | Copyable Reddit/HN/forum/Discord text and share links. |
| [`SECURE_LOCAL_AI.md`](SECURE_LOCAL_AI.md) | Checklist for securing a local AI box: network exposure, shared servers, community recipes, containers, clusters, SSH, RAG and agents, firmware, with dated public sources and what is not tested here. |
| [`SECURITY.md`](SECURITY.md) | Official-source and impersonation reporting policy, plus the dated advisory status of the pinned components. |
| [`SUPPORT.md`](SUPPORT.md), [`SERVICES.md`](SERVICES.md) | How to support ongoing testing, or request scoped professional help, without changing the evidence-first benchmark policy. |
| [`ONE_PAGE_BRIEF.md`](ONE_PAGE_BRIEF.md), [`PARTNERSHIP.md`](PARTNERSHIP.md), [`SPONSORSHIP.md`](SPONSORSHIP.md), [`VENDOR_DISCLOSURE.md`](VENDOR_DISCLOSURE.md) | Vendor/partner-facing explanation of how the technical proof layer reduces buyer adoption friction while preserving independence, including how vendors can report factual corrections. |
| [`BUYER_USE_CASES.md`](BUYER_USE_CASES.md), [`SPONSOR_ROADMAP.md`](SPONSOR_ROADMAP.md), [`TRACTION.md`](TRACTION.md) | Buyer-use-case, roadmap, and public-evidence docs, including where this repository's data is reused by other projects. |

## Table of Contents

- [20-Second Summary](#20-second-summary)
- [Use This Guide If](#use-this-guide-if)
- [Quick Start (6 Steps)](#quick-start-6-steps)
- [Qwen3.8 On Strix Halo](QWEN38_STRIX_HALO.md)
- [Setup Script](#setup-script)
- [What You Can Run: Quick Snapshot](#what-you-can-run-quick-snapshot)
- [Use This If You Want](#use-this-if-you-want)
- [Community-Tested Rules Of Thumb](#community-tested-rules-of-thumb)
- [Results Wanted](#results-wanted)
- [Community Results](COMMUNITY_RESULTS.md)
- [Best Current Setup Tested Here](#best-current-setup-tested-here)
- [Headline Evidence](#headline-evidence)
- [Reproduce One Headline Result](#reproduce-one-headline-result)
- [Not Yet Proven Here](#not-yet-proven-here)
- [Do Not Copy These Claims Without Matching Setup](#do-not-copy-these-claims-without-matching-setup)
- [Reuse And Citing The Numbers](#reuse-and-citing-the-numbers)
- [Documentation Map](#documentation-map)
- [Hardware](#hardware)
- [What You Can Run](#what-you-can-run)
- [Benchmark Results](#benchmark-results)
  - [Benchmark Charts](#benchmark-charts)
  - [Ollama Vulkan (RADV)](#ollama-vulkan-radv)
  - [llama-server Multi-User Serving](#llama-server-multi-user-serving-b9010)
  - [ROCm HIP (llama.cpp)](#rocm-hip-llamacpp)
  - [Backend Comparison](#backend-comparison-table)
  - [Hardware Comparison](#hardware-comparison)
  - [Long Context Performance](#long-context-performance)
- [Backend Decision Guide](#backend-decision-guide)
- [Server Shootout](SERVER_SHOOTOUT.md)
- [Phase 1: BIOS Configuration](#phase-1-bios-configuration)
- [Phase 2: Ubuntu 24.04 Installation](#phase-2-ubuntu-2404-installation)
- [Phase 3: Kernel Configuration](#phase-3-kernel-configuration)
- [Phase 4: Performance Tuning](#phase-4-performance-tuning)
- [Phase 5: Ollama Setup (Vulkan)](#phase-5-ollama-setup-vulkan)
- [Phase 6: Benchmarking](#phase-6-benchmarking)
- [Phase 7: ROCm with llama.cpp (Containers)](#phase-7-rocm-with-llamacpp-containers)
- [Phase 8: vLLM Serving](#phase-8-vllm-serving)
- [Phase 9: Multi-Node Clustering (RDMA)](#phase-9-multi-node-clustering-rdma)
- [Phase 10: SSH and Remote Access](#phase-10-ssh-and-remote-access)
- [Vulkan Driver Comparison](#vulkan-driver-comparison)
- [Key Findings and Corrections](#key-findings-and-corrections)
- [Known Issues](#known-issues)
- [Troubleshooting](#troubleshooting)
- [Kernel and ROCm Compatibility](#kernel-and-rocm-compatibility)
- [Power Measurement Status](#power-measurement-status)
- [Testing Checklist](#testing-checklist)
- [Model Recommendation Guide](#model-recommendation-guide)
- [Cost: Local vs Cloud](#cost-local-vs-cloud)
- [Buying Guide](#buying-guide)
- [Glossary](#glossary)
- [FAQ](#faq)
- [Community Resources](#community-resources)
- [Credits and References](#credits-and-references)
- [Contributing](#contributing)
- [Changelog](#changelog)
- [License](#license)

---

## Hardware

### Evidence Coverage: 13 Systems Or Independent Sources

The count is **10 described owner systems plus 3 independently attributable
external evidence sources**. One physical owner system counts once regardless
of how many results it contributes; separate physical machines count
separately even when they are the same product or belong to the same
contributor. External packages whose unique hardware identity cannot be safely
proved remain labelled as sources. This makes the public `13 systems/sources`
claim auditable without treating every row as an equal-quality benchmark.

For a reviewer-friendly cross-OEM view of what each source proves, how the evidence classes differ, and which validation is still missing, see the [`AMD Strix Halo System Evidence Matrix`](SYSTEM_EVIDENCE_MATRIX.md). A machine-readable version is available at [`data/system_evidence_matrix.csv`](data/system_evidence_matrix.csv).

| Evidence source | Systems/sources counted | Running total | Evidence |
|-----------------|------------------------:|--------------:|----------|
| Primary Beelink GTR9 Pro | 1 | 1 | First-party raw evidence throughout this repository |
| Corsair AI Workstation 300 fleet | 3 | 4 | [`COMMUNITY_RESULTS.md`](COMMUNITY_RESULTS.md), [`THERMAL_STABILITY.md`](THERMAL_STABILITY.md), [`data/community_results.csv`](data/community_results.csv) |
| GMKtec EVO-X2 native contributor system | 1 | 5 | [`COMMUNITY_RESULTS.md`](COMMUNITY_RESULTS.md), [`data/raw/2026-05-14/community-gmktec-native-issue16/`](data/raw/2026-05-14/community-gmktec-native-issue16/) |
| GMKtec EVO-X2 tuned Reddit report | 1 | 6 | [`COMMUNITY_RESULTS.md`](COMMUNITY_RESULTS.md), [`raw note`](data/raw/2026-06-02/community-reddit-look-qwen-coder/) |
| Minisforum MS-S1-Max | 1 | 7 | [`COMMUNITY_RESULTS.md`](COMMUNITY_RESULTS.md), [`raw report`](data/raw/2026-06-02/community-windows-lmstudio-issue3/) |
| Nimo AI Mini PC | 1 | 8 | [`COMMUNITY_NIMO.md`](COMMUNITY_NIMO.md) |
| Second Beelink GTR9 Pro owner stack | 1 | 9 | [`COMMUNITY_RESULTS.md`](COMMUNITY_RESULTS.md), [`raw report`](data/raw/2026-06-12/community-devoidfury-cachyos-rocm-zendnn/) |
| ciru-ai GMKtec EVO-X2 NixOS/NPU artifact | 1 | 10 | [`COMMUNITY_RESULTS.md`](COMMUNITY_RESULTS.md), [`source artifact`](https://github.com/ciru-ai/strix-halo-evo-x2-evidence) |
| Minix Elite ER939 Ai | 1 | **11** | [`COMMUNITY_RESULTS.md`](COMMUNITY_RESULTS.md), [`raw report`](data/raw/2026-06-24/community-minix-er939-ollama-issue27/) |
| Third independent Beelink GTR9 Pro unit | 1 | 12 | [`COMMUNITY_RESULTS.md`](COMMUNITY_RESULTS.md), [`raw report`](data/raw/2026-08-21/community-reddit-ornery-ub-clamp/) |
| Kyanite Labs GMKtec EVO-X2 Qwen3.8 package | 1 | **13** | [`COMMUNITY_RESULTS.md`](COMMUNITY_RESULTS.md), [`scope note`](data/raw/2026-08-25/qwen38-community-runtime-update/), [source artifact](https://github.com/KyaniteLabs/qwen38-27b-strix-halo) |

### Hardware Context

This table is a product/context map, not an endorsement list or the source of the thirteen-source count above. Rows without linked community evidence are useful hardware context only.

| System | CPU | GPU | RAM | Notes |
|--------|-----|-----|-----|-------|
| **Beelink GTR9 Pro** | Ryzen AI MAX+ 395 | Radeon 8060S (40 CU) | 128GB LPDDR5X-8000 | This guide's primary test system |
| Corsair AI Workstation 300 | Ryzen AI MAX+ 395 | Radeon 8060S (40 CU) | 128GB LPDDR5X-8000 | Three community systems reproduced the Qwen3-Coder path |
| Framework Desktop | Ryzen AI MAX+ 395 | Radeon 8060S (40 CU) | 128GB LPDDR5X-8000 | Used by kyuz0, lhl |
| GMKtec EVO-X2 | Ryzen AI MAX+ 395 | Radeon 8060S (40 CU) | 96GB or 128GB LPDDR5X-8000 | Native 96GB community rows reproduce Qwen3.6 and add a stock Gemma 4 direct control; a separate corrected 96GB Kyanite package reaches 262K-class Qwen3.8 retrieval on a patched HIP route; a tuned Reddit report touched 100.0 t/s on Qwen3-Coder `Q4_K_S`; [pablo-ross guide](https://github.com/pablo-ross/strix-halo-gmktec-evo-x2) |
| Minisforum MS-S1-Max | Ryzen AI MAX+ 395 | Radeon 8060S (40 CU) | 128GB LPDDR5X | Windows LM Studio community serving report imported; not a same-shape Linux comparison |
| Nimo AI Mini PC | Ryzen AI MAX+ 395 | Radeon 8060S (40 CU) | 128GB LPDDR5X | Community issue #4 bundle imported; adds compact-chassis large-model serving, MTP, StepFun/Qwen 122B, Gemma 4 QAT/MTP assistant-head follow-up data, and thermal context |
| HP ZBook Ultra G1a | Ryzen AI MAX+ 395 | Radeon 8060S (40 CU) | 128GB LPDDR5X-8000 | Workstation laptop |

### Strix Halo Specs

| Component | Spec |
|-----------|------|
| CPU | AMD Ryzen AI MAX+ 395 (16 cores / 32 threads, Zen 5) |
| GPU | Radeon 8060S (gfx1151, RDNA 3.5, 40 CUs) |
| RAM | 96GB or 128GB unified LPDDR5X-8000 depending on vendor; primary measured system is 128GB (~215 GB/s measured, 256 GB/s theoretical) |
| NPU | RyzenAI-npu5 (XDNA 2) |

> **Why this hardware?** 96GB/128GB unified memory shared between CPU and GPU means you can run **70B+ models entirely on the GPU** -- something an RTX 4090 (24GB VRAM) cannot do. You trade raw bandwidth (~215 GB/s vs ~1 TB/s on this Beelink) for the ability to run larger model artifacts (not automatically higher task quality) on one compact machine. Price changes quickly by vendor; check the [Buying Guide](#buying-guide) before making a purchase decision.

---

## What You Can Run

Real-world generation speeds measured on the Beelink GTR9 Pro, primarily with Vulkan/RADV. Speeds marked with * are via `llama-bench` direct; others are via Ollama unless noted. Use this table to choose a first model, then follow the evidence links above before copying a benchmark claim.

| Model | Size | Type | Generation Speed | Use Case |
|-------|------|------|------------------|----------|
| Qwen3-0.6B (Q8_0) | 0.8 GB | Dense | 266 t/s * | Ultra-fast tiny model |
| Llama 2 7B | 3.8 GB | Dense | 48-52 t/s | Testing, lightweight tasks |
| Qwen2.5-VL 7B | 6.0 GB | Vision | 21.4 t/s | Image understanding |
| LFM2.5-VL 1.6B (Q4_0) | 1.19 GB with projector | Vision | functional local pass | Lightweight official-GGUF image route; one-image smoke, not a speed/quality headline |
| Qwen3-ASR 0.6B (Q8_0) | 0.95 GB with projector | Speech | functional local pass | Short offline English transcription; experimental audio path |
| LFM2.5 8B-A1B (Q4_K_M) | 5.1 GB | MoE | **170.0 t/s** * | Fastest current small-MoE scout; not a 30B-class replacement |
| Gemma 4 26B-A4B IT QAT (UD-Q4_K_XL) | 14.2 GB | MoE | **74.8 t/s** direct; **102.7-110.0 t/s** MTP server | Historical throughput; sampled server coding answers failed and this profile is not recommended (see the [saved-output review](BEST_KNOWN_PROFILES.md#historical-throughput-sampled-coding-outputs-failed)). Direct `llama-bench` is separate and does not establish task quality |
| Qwen3-30B-A3B-Instruct-2507 (IQ4_XS) | 13.9 GB | MoE | **100.0 t/s** * | Fastest direct 30B-class Qwen row; general-instruct route, not Qwen3-Coder |
| Qwen3-Coder 30B-A3B (Q4_K_S) | 17.5 GB | MoE | **101.0 t/s** * | Fastest measured coding speed; speed-first quant, not the balanced default |
| Qwen3-Coder 30B-A3B (UD-Q4_K_XL) | 17.7 GB | MoE | **97 t/s** * | Measured balanced-quant candidate; no matched quality score; current b9049 measured 96.76 t/s and previous b9010 peak was 97.24 t/s |
| Qwen3.6 35B-A3B (Q4_0) | 19.7 GB | MoE | **81 t/s** * | Fastest measured Qwen3.6 speed-first quant; use a balanced quant if quality matters more than raw speed |
| Qwen3.6 35B-A3B (Q4_K_M / UD-Q4_K_M) | 20-22 GB | MoE | **63 t/s** * | Balanced direct path; separate speed-first/alternate quants reach higher but need quality sanity |
| Qwen3.5 35B-A3B | 23 GB | MoE | 48-**65 t/s** | General purpose, coding (65 with measured direct llama.cpp builds) |
| Qwen3-Coder 30B-A3B (Q8_0) | 32 GB | MoE | 51 t/s | Coding (higher-bit quant; no matched quality evaluation) |
| Qwen3-Coder-Next | 51 GB | MoE (80B total / 3B active) | 38-39 t/s | Coding MoE; size is the measured artifact, not parameter count |
| Llama 3.1 70B (Q4_K_M) | 42 GB | Dense | **4.7-4.9 t/s** | Dense 70B capacity; artifact exceeds 24GB VRAM without offload |
| Llama 4 Scout 109B (Q4_K_M) | 61 GB | MoE | **18.3 t/s** * | 109B artifact on a mini PC; exceeds 24GB VRAM without offload |
| Nemotron 3 Nano 30B-A3B (IQ4_XS) | 18.2 GB | MoE | **76.0 t/s** * | Measured NVIDIA Nemotron 30B-class route (June 2026); the newer Nemotron 3.5 Lightning was measured on 2026-09-26 as a routine direct scout ([66.80 tg128 on b11146](CURRENT_MODELS.md#2026-09-26-30b-class-scout-b11146-routine)); no recommendation between the two |
| DeepSeek V4 Flash 284B (UD-IQ2_XXS) | 90.9 GB | MoE | **13.3 t/s** * | Largest current direct ordinary-GGUF capacity proof; low-bit quant, not a quality recommendation |
| Nemotron 3 Super 120B-A12B (UD-IQ4_XS) | 64.5 GB | MoE | **18.4 t/s** * | Current 120B-class GGUF route on one 128GB Strix Halo |
| gpt-oss-120b MXFP4 | 63.4 GB | MoE | **55.6 t/s** * | 117B-parameter open-weight model; local load and long-context speed check |
| Qwen3-Next 80B-A3B (UD-Q4_K_XL) | 42.90 GiB | MoE | **59 t/s** * | 80B model, 256K context -- a separate 80B MoE route |
| Kimi K2.5 1T (4-node cluster) | 375 GB artifact; 512GB aggregate RAM | MoE | distributed | [AMD technical article](https://www.amd.com/en/developer/resources/technical-articles/2026/how-to-run-a-one-trillion-parameter-llm-locally-an-amd.html) |

---

## Benchmark Results

Benchmarks below were run on 2026-03-20, 2026-03-21, 2026-04-26, 2026-05-03, 2026-05-07, 2026-05-16, 2026-05-26, 2026-05-27, 2026-05-31, 2026-06-01, 2026-06-02, 2026-06-05, 2026-06-07, 2026-06-11, 2026-06-12, 2026-06-21, 2026-06-30, and 2026-07-02. Primary benchmark system: Beelink GTR9 Pro. Recorded local runs used kernel 6.19.4, Mesa RADV 26.0.2-26.1.3 where captured, AMDVLK removed, and `tuned` `accelerator-performance` where captured; individual raw directories and CSV rows are the source of truth for exact run metadata, and some older or scout rows intentionally record missing metadata as `not recorded`. Before new benchmarks, record and verify the selected power/background policy; require tuned only for a tuned-profile reproduction.

These rows are included because they answer practical setup questions: which model to try first, which backend removes the most friction, which paths are only experimental, and which results are strong enough to cite.

### Benchmark Charts

These generated SVGs summarize the current structured benchmark data. The CSV files in `data/` and raw logs in `data/raw/` remain the source of truth; regenerate charts with `python3 scripts/generate_charts.py`.

| Multi-user serving | Long-context prompt scaling |
|--------------------|-----------------------------|
| <img src="charts/multi_user_aggregate.svg" alt="llama-server multi-user aggregate throughput chart" width="455"> | <img src="charts/long_context_prompt.svg" alt="long-context prompt processing chart" width="455"> |

| Filled-KV decode | KV-cache quantization tradeoff |
|------------------|-------------------------------|
| <img src="charts/filled_kv_decode.svg" alt="decode speed after filled KV cache chart" width="455"> | <img src="charts/kv_cache_tradeoff.svg" alt="Qwen3.6 KV-cache quantization tradeoff chart" width="455"> |

| Real versus synthetic prompts | Backend spot check |
|-------------------------------|--------------------|
| <img src="charts/real_vs_synthetic.svg" alt="real documentation corpus versus synthetic prompt chart" width="455"> | <img src="charts/backend_spot_check.svg" alt="Vulkan RADV versus ROCm HIP spot check chart" width="455"> |

### Ollama Vulkan (RADV)

**Qwen3.6-35B-A3B** (Q4_K_M, ~20-23GB, MoE):

| Prompt Tokens | Prompt Eval | Generation | Notes |
|---------------|-------------|------------|-------|
| 25 | 944 t/s | **71.8 t/s** | 2026-07-02 user-local Ollama 0.31.1 binary sanity check; required `OLLAMA_IGPU_ENABLE=1`; 9-run warm average after one cold run |
| 19 | 158 t/s | **50.5 t/s** | Controlled 2026-05-07 API warm average across 10 runs; matches 0.21.2 |
| 20 | 163 t/s | 45.6 t/s | Older result, superseded by controlled API run |
| 22 | 174 t/s | 45.4 t/s | Older result, superseded by controlled API run |

**Qwen3.5-35B-A3B** (Q4_K_M, ~23GB, MoE -- Ollama 0.20.4):

| Prompt Tokens | Prompt Eval | Generation | vs Previous (Mesa 26.0.1) |
|---------------|-------------|------------|---------------------------|
| 14 | 121.3 t/s | **48.0 t/s** | tg +4.8% |
| 23 | 182.3 t/s | **47.5 t/s** | tg +4.4% |
| 122 | 456.7 t/s | **47.4 t/s** | tg +4.2% |

**Qwen3-Coder 30B-A3B** (Q8_0, ~32GB, MoE):

| Prompt Tokens | Prompt Eval | Generation | Notes |
|---------------|-------------|------------|-------|
| 12 | 118.3 t/s | **51.4 t/s** | Fastest via Ollama |
| 21 | 205.2 t/s | **51.3 t/s** | Higher-bit quant than Q4_K_M; quality not evaluated here |

**Qwen3-Coder-Next** (~51GB artifact, 80B total / 3B active MoE):

| Prompt Tokens | Prompt Eval | Generation | vs Previous |
|---------------|-------------|------------|-------------|
| 12 | 90.7 t/s | **39.1 t/s** | tg +2.9% |
| 21 | 129.5 t/s | **38.4 t/s** | tg +3.8% |
| 120 | 301.2 t/s | **37.9 t/s** | NEW |

**Other Models:**

| Model | Size | Prompt Tokens | pp (t/s) | tg (t/s) |
|-------|------|---------------|----------|----------|
| Llama 2 7B | 3.8 GB | 24 | 384.6 | 52.0 |
| Qwen2.5-VL 7B | 6.0 GB | 23 | 81.7 | 21.4 |
| Qwen3.5 35B (no-think) | 23 GB | 14 | 127.1 | 47.4 |

**Llama 3.1 70B** (Q4_K_M, 42GB, Dense -- the "doesn't fit on RTX 4090" showcase):

| Prompt Tokens | Prompt Eval | Generation | Notes |
|---------------|-------------|------------|-------|
| 14 | 22.1 t/s | 4.9 t/s | Cold start |
| 23 | 36.8 t/s | 4.8 t/s | Realistic chat |
| 122 | 79.6 t/s | 4.7 t/s | Long prompt |

> A rough weight-streaming estimate is 215 GB/s divided by 42 GB, or about 5.1 t/s, compared with the observed 4.8 t/s. This simplified model omits compute, KV/cache traffic and implementation effects; it is not a proven ceiling or evidence that optimization cannot help. The artifact cannot fit wholly in an RTX 4090's 24GB VRAM; partial CPU offload is a separate memory/latency tradeoff.

> The historical combined Mesa/power-profile change was reported alongside higher generation rates. It does not isolate a tuned-only effect or establish a universal percentage across models.

### llama-server Multi-User Serving (b9010)

Single-user `llama-bench` tells you the ceiling for one stream. For a real local API box, the more practical question is what happens when multiple tools or users hit `llama-server` at the same time.

**Qwen3.6-35B-A3B** (UD-Q4_K_M, Vulkan RADV, llama.cpp b9010, continuous batching, 4096 context tokens per slot):

| `-np` | Concurrent Requests | Aggregate Generation | Avg per Request | Mean TTFT | Mean request decode interval | Notes |
|-------|---------------------|----------------------|-----------------|-----------|----------|-------|
| 1 | 1 | 59.21 t/s | 59.21 t/s | 0.117 s | 16.1 ms | Server/API baseline |
| 2 | 2 | 92.21 t/s | 46.11 t/s | 0.198 s | 20.3 ms | Good scaling |
| 4 | 4 | 130.81 t/s | 32.71 t/s | 0.237 s | 29.0 ms | Strong batching gain |
| 8 | 8 | **161.98 t/s** | 20.25 t/s | 0.307 s | 47.4 ms | Practical sweet spot |
| 16 | 16 | 165.98 t/s | 10.38 t/s | 0.547 s | 92.9 ms | Throughput plateau |

> **Takeaway:** continuous batching makes Strix Halo look much stronger as a local API server than single-user tg numbers suggest. `-np 8` delivers about **2.7x** the `-np 1` aggregate throughput while keeping TTFT around 0.3 seconds. `-np 16` works with no errors in this test, but aggregate throughput barely improves while per-user speed drops sharply.

**Qwen3-Coder 30B-A3B** (UD-Q4_K_XL, Vulkan RADV, llama.cpp b9010, continuous batching, 4096 context tokens per slot):

| `-np` | Concurrent Requests | Aggregate Generation | Avg per Request | Mean TTFT | Mean request decode interval | Notes |
|-------|---------------------|----------------------|-----------------|-----------|----------|-------|
| 1 | 1 | 90.20 t/s | 90.20 t/s | 0.079 s | 10.6 ms | Server/API baseline |
| 2 | 2 | 121.65 t/s | 60.83 t/s | 0.133 s | 15.5 ms | Good scaling |
| 4 | 4 | 157.41 t/s | 39.36 t/s | 0.207 s | 24.0 ms | Strong batching gain |
| 8 | 8 | **173.16 t/s** | 21.65 t/s | 0.382 s | 43.5 ms | Practical sweet spot |
| 16 | 16 | 129.56 t/s | 8.10 t/s | 0.571 s | 119.9 ms | Regression |

> **Coding server takeaway:** `-np 8` is also the best measured setting for Qwen3-Coder, but here `-np 16` is actively worse. More parallel slots are not automatically better.

Raw data: `data/multi_user.csv`, `data/raw/2026-05-03/multi-user/`, and `data/raw/2026-05-03/multi-user-coder/`.

<a id="llama-bench-direct-key-llamacpp-builds-b9049-b9010-and-b8460-vs-kyuz0-containers-b8298"></a>

### llama-bench Direct -- Key llama.cpp Builds (b9049, b9010, and b8460) vs kyuz0 Containers (b8298)

> **Historical Qwen3.5-35B-A3B comparison (2026-03-21):** b8298 to b8460 improved pp512 by about 24% and tg128 by about 25% on the recorded Vulkan pair. The build includes changes such as [PR #19625](https://github.com/ggml-org/llama.cpp/pull/19625), [PR #20551](https://github.com/ggml-org/llama.cpp/pull/20551) and [PR #20334](https://github.com/ggml-org/llama.cpp/pull/20334), but this endpoint comparison does not isolate their individual contributions.
>
> **Important caveats:**
> - The 25% observation is scoped to that Qwen3.5 pair. Qwen3-Coder's recorded 86.81→87.11 t/s pair did not show that gain. Small changes on dense models do not prove a bandwidth ceiling.
> - For [kyuz0's containers](https://github.com/kyuz0/amd-strix-halo-toolboxes), inspect the actual binary revision and image digest. A tag or rebuild policy does not prove an already-installed container contains a particular update.
> - **WARNING: AMDVLK silently overrides RADV.** If AMDVLK is installed, its `/etc/vulkan/icd.d/amd_icd64.json` takes priority over RADV. This reduced pp speed by about 39% in the recorded pair (1080 -> 660 pp512) without any visible error. Always set `AMD_VULKAN_ICD=RADV` or uninstall AMDVLK entirely: `sudo dpkg -r amdvlk && sudo rm -f /etc/vulkan/icd.d/amd_icd64.json`. Check your driver: RADV shows `(RADV STRIX_HALO) (radv)` with `shared memory: 65536` in llama-bench output. AMDVLK shows `(AMD open-source driver)` with `shared memory: 32768`. We [originally reported this as a llama.cpp regression](https://github.com/ggml-org/llama.cpp/issues/22375) -- it wasn't.

**Qwen3.5-35B-A3B** (Q4_K_M, 19.9GB, MoE) -- the biggest improvement:

| Build | Driver | pp128 | pp512 | tg128 | vs old RADV |
|-------|--------|-------|-------|-------|-------------|
| **b8460 (newer March build)** | **RADV** | **623** | **1080** | **64.85** | **pp +24%, tg +25%** |
| b8460 (newer March build) | AMDVLK | 521 | 663 | 64.10 | pp -24%, tg +23% |
| b8298 (kyuz0) | RADV | 583 | 868 | 52.06 | baseline |
| b8298 (kyuz0) | AMDVLK | 479 | 576 | 56.08 | |

> **Beginner rule: use RADV for Vulkan. Do not install AMDVLK.** In the newer b8460 Vulkan comparison, RADV is faster than AMDVLK on both pp (+63%) and tg (+1.2%), and AMDVLK can silently hijack your Vulkan driver. Advanced note: ROCm/HIP is a different backend, not a Vulkan driver. HIP can still be worth testing for long prompts, RAG ingest, and other prompt-processing-heavy workloads.

Extended context scaling (b8460 RADV):

| pp512 | pp2048 | pp4096 | pp8192 | Drop at 8K |
|-------|--------|--------|--------|------------|
| **1080** | **1057** | **1049** | **1049** | **-3%** |

> pp is virtually flat from 512 to 8192 tokens. Only 3% drop at 8K context.

**Qwen3-Coder 30B-A3B** (Q4_K_S speed-first and UD-Q4_K_XL balanced, MoE):

| Build | Driver | pp512 | tg128 | Notes |
|-------|--------|-------|-------|-------|
| **b9851** | **RADV** | **1423** | **100.99** | Official release binary; Q4_K_S speed-first quant; not the balanced default |
| **b9179** | **RADV** | **1396** | **98.51** | Q4_K_S speed-first quant, strict-clean r50 confirmation |
| **b9049** | **RADV** | **1321** | **96.76** | 2026-05-07 max-performance guide-flags r20 confirmation |
| **b9010** | **RADV** | **1346** | **97.24** | Controlled 2026-05-03 two-run r20 average |
| b8460 | RADV | 1342 | 87.11 | Previous headline |
| b8298 (kyuz0) | RADV | 1350 | 86.81 | ~same (model was already at ceiling) |

> A controlled May 2026 rerun moved the balanced Qwen3-Coder 30B headline from 87 t/s to 97 t/s on b9010 Vulkan RADV. The 2026-05-07 b9049 max-performance campaign measured 96.76 t/s on UD-Q4_K_XL. A later strict-clean b9179 run measured 98.51 t/s with Q4_K_S, and the official b9851 Vulkan release binary lifted the same speed-first quant to 100.99 t/s. This is still not the default balanced row.

**Gemma 4 26B-A4B historical non-QAT baseline** (UD-Q4_K_M, 15.7GB, MoE) -- tested on b8933 (earliest build with Gemma 4 support):

| Build | Driver | pp512 | tg128 | Notes |
|-------|--------|-------|-------|-------|
| **b8933** | **RADV** | **1142** | **48.46** | early non-QAT Gemma 4 MoE baseline |

> This row is historical and non-QAT. The separate **Gemma 4 26B-A4B IT QAT UD-Q4_K_XL** route measured **74.80 t/s direct** and **102.69 cold / 107.42 T3-only / 110.00 best-repeat t/s** through a matched MTP `llama-server` route. Sampled saved server coding answers failed in both no-spec and MTP records, so this QAT server profile is not a practical recommendation; see the [saved-output review](BEST_KNOWN_PROFILES.md#historical-throughput-sampled-coding-outputs-failed). Keep direct and server/speculative speed evidence separate from task correctness.
>
> The older non-QAT Gemma row was slower than the recorded Qwen MoE routes. Attention dimensions, mixed attention and active-parameter traffic are possible contributors, alongside runtime implementation. These unmatched rows do not isolate a cause or rule out llama.cpp improvements; the later non-QAT b9851 result reached 55.45 t/s.
>
> **KV precision caveat:** an [external KL experiment](https://localbench.substack.com/p/kv-cache-quantization-benchmark) reported q8_0 KV KL 0.377 for Gemma 26B-A4B versus 0.108 for **Gemma 31B**, about 3.49×. It compared output distributions against an f16-KV reference; this is not a factor of downstream task-quality loss and not a comparison with Qwen. Keep f16 KV as this guide's conservative tested profile; lower-precision KV needs artifact/workload-specific qualification.

**Llama 4 Scout 109B** (Q4_K_M, 60.9GB, MoE -- 109B total params, 17B active):

| Build | Driver | pp512 | tg128 | Notes |
|-------|--------|-------