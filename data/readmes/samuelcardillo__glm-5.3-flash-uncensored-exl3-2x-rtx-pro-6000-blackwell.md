# GLM-5.3 Flash Uncensored EXL3 on 2× RTX PRO 6000 Blackwell

Revision-pinned **v0.8** recipe based on a live implementation tested on two NVIDIA RTX PRO 6000 Blackwell 96 GB GPUs (one Max-Q Workstation Edition at 300 W and one Workstation Edition at 600 W). The sanitized public launcher is CPU-tested, not freshly GPU-launched: publication did not interrupt the running model. Historical r19 results below are a separate lineage.

- `neko-legends/GLM-5.3-Flash-Uncensored-EXL3@1fac3dbe6269a399ce5378261cdf250fde706180`
- EXL3/TR3 4 bpw routed experts, BF16 remainder
- TP2, DCP1, expert parallel off; MLA ownership `split:25`, embedding split `0.17`
- DFlash2 K3, BF16 draft KV, draft slot sharing; baseline rollback (not ReplaySSM)
- 1,048,576-token configured context; 1,040,000-token retrieval tested before the template repair
- Compact FP8 MLA KV cache; prefix caching enabled, Mamba cache `align`
- Up to 16 still images per request tested separately; native video disabled
- OpenAI-compatible text, reasoning, and native tool calls

This is the uncensored/abliterated checkpoint, not the aligned GLM-5.3 Flash checkpoint and not full GLM-5.3.

## License warning

This is a source-available deployment stack, not an all-MIT/open-source bundle:

- the checkpoint includes ShapleyMCG-licensed calibration artifacts and requires attribution;
- the uncensored checkpoint is gated and has additional model-card terms;
- the DFlash2 drafter is **CC BY-NC-ND 4.0**, for non-commercial research/evaluation unless separately licensed;
- the v0.8 recipe/runtime image declares Apache-2.0, but that label does not replace model, ShapleyMCG, NVIDIA foundation or dependency terms; the image is not redistributed here.

Review [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md), [ATTRIBUTIONS.md](ATTRIBUTIONS.md), and all upstream terms before use.

> This work includes or was produced using ShapleyMcg, created by Brandon M. Music
> (https://github.com/brandonmmusic-max/shapleymcg). ShapleyMcg is licensed under the
> ShapleyMcg License v1.0, an attribution-required license that grants no rights to
> the person known as "0xSero." Use of ShapleyMcg without this attribution is unlicensed.

## Qualified hardware and software

- 1× NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition, 96 GB, 300 W power limit
- 1× NVIDIA RTX PRO 6000 Blackwell Workstation Edition, 96 GB, 600 W power limit
- This is a mixed-power pair, not a power-matched upstream benchmark configuration.
- both cards selected explicitly; an RTX 5090 in the test workstation was excluded
- NVIDIA driver 590.48.01
- Docker 29.1.3 with NVIDIA Container Toolkit
- Ubuntu 24.04 host
- pinned runtime image digest in [PROVENANCE.md](PROVENANCE.md)

Other GPUs, driver branches, container engines, lower-VRAM cards, and topology combinations are unqualified.

## Quick start

Prerequisites:

1. Docker Engine and NVIDIA Container Toolkit working for an unprivileged user.
2. Exactly two free RTX PRO 6000 Blackwell 96 GB GPUs.
3. About 180 GB for the target checkpoint, 2.4 GB for the drafter, and additional cache space.
4. An authenticated Hugging Face account approved for the gated target checkpoint.
5. Hugging Face `hf` CLI (tested with 1.9.0).

```bash
git clone https://github.com/samuelcardillo/glm-5.3-flash-uncensored-exl3-2x-rtx-pro-6000-blackwell.git
cd glm-5.3-flash-uncensored-exl3-2x-rtx-pro-6000-blackwell
cp config/example.env .env
$EDITOR .env
```

Authenticate with Hugging Face, review the three licenses/terms, then download exact revisions:

```bash
hf auth login
I_ACCEPT_SHAPLEYMCG_LICENSE=yes \
I_ACCEPT_UNCENSORED_MODEL_TERMS=yes \
I_ACCEPT_DFLASH2_CC_BY_NC_ND_4_0=yes \
  ./scripts/download-model.sh
```

The acceptance variables are deliberately not stored in `.env`. The downloader checks all three before creating download directories.

Run full preflight and launch:

```bash
./scripts/preflight.sh        # hashes every pinned file; expect a full ~178 GB read
./scripts/serve.sh
```

In another terminal:

```bash
./scripts/verify.py
./scripts/verify-long-context.py   # historical 261,875-token smoke only, NOT a near-1M qualification
```

Stop:

```bash
./scripts/stop.sh
```

## User systemd service

```bash
./scripts/install-user-service.sh
systemctl --user daemon-reload
systemctl --user enable --now glm53-uncensored-exl3.service
journalctl --user -u glm53-uncensored-exl3.service -f
```

The installer writes and validates files only; it does not reload, enable, start, restart, or replace a running service. Explicit activation is your decision. The user manager starts after login. For deliberate pre-login startup, review `loginctl enable-linger` and its security implications. Do not activate this alongside another model using the same GPUs/port. Startup waits up to 5,400 seconds for Docker release-warmup health plus HTTP health/model identity; inspect progress with `docker logs -f` using your configured container name. Stop refuses foreign containers, including containers from the previous launcher lacking this recipe's ownership label.

## API example

```bash
curl http://127.0.0.1:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model":"glm-5.3-flash-uncensored-exl3",
    "messages":[{"role":"user","content":"Reply with exactly READY"}],
    "chat_template_kwargs":{"enable_thinking":false},
    "temperature":0,
    "max_tokens":64
  }'
```

The API has no built-in authentication. It binds to loopback by default. Do not set `BIND_ADDRESS=0.0.0.0`; use a specific trusted LAN/Tailnet address and an authenticated gateway such as LiteLLM when remote access is required.

## v0.8 historical live evidence and publication boundary

- Near-1M: 1,040,000 prompt tokens, six needles retrieved (6/6), TTFT 278.466 s **before** the template-only repair; not rerun afterward.
- After repair: randomized 16-image strict JSON passed with no reasoning leakage; 10 protocol probes and 8 sandboxed code checks passed; tool failure/recovery/final-answer sequence passed.
- Warm pre-repair prose: 115–119 tok/s; tested code: 165–188 tok/s. Post-repair long output: 4,096 tokens at 116.46 tok/s, `finish_reason=length`: a capped repetition check, **not** a completed-manual quality pass.
- No matched comparison with the old aligned service; no v0.8 K5 trial; no combined near-1M-plus-16-images request. K3 is usable, not proven globally optimal.

See [docs/V08.md](docs/V08.md) and the [sanitized summary](benchmarks/v08-summary.json). No private raw prompts/logs are published. The public lifecycle, loopback binding and installer are safety adaptations, not claims about the historical live launcher. No fresh inference or restart was performed for publication.

### Thinking controls

The launcher derives a hash-pinned template outside the immutable checkpoint and mounts it read-only. Thinking defaults on. Either true `thinking` or `enable_thinking` enables it; false disables it when neither alias is true, matching the pinned parser's OR semantics. Default/low/high/max enabled-mode rendered bytes remain unchanged. There is no parser patch and no answer stripping.

### Local CPU-only validation (no GitHub Actions)

Install Python 3, Jinja2 (tested 3.1.2), ShellCheck (or the pinned `uvx` fallback), and systemd's `systemd-analyze`; run `./scripts/ci.sh`. Tests use temporary files and mocked Docker/HTTP calls; the installer test validates a real rendered unit without activating it. The repository contains no active workflows.

## Historical r19 results — not v0.8 measurements

The initial K=7 profile admitted only one active request because its hybrid recurrent/speculative cache reservation consumed about 60% of the available KV pool per short request. The qualified K=3 profile admits three active requests and preserves single-stream performance:

- concurrency 1: 117.82 → 123.19 output tok/s (+4.56%);
- concurrency 2: 127.31 → 205.40 output tok/s (+61.33%);
- concurrency 4: 131.66 → 212.90 output tok/s (+61.70%);
- slowest of four 512-token requests: 15.55 → 9.62 seconds (-38.16%);
- near-262K TTFT: 60.456 → 59.850 seconds.

A sequential matched-checkpoint A/B under the same K=3 runtime found the uncensored checkpoint within about 4% of the aligned checkpoint on the isolated regressions and faster on most measured workloads. This does not reconstruct the former aligned native-MTP/ReplaySSM service. HumanEval+ pass@1 remains 92.7% from the original qualification. See [docs/OPTIMIZATION.md](docs/OPTIMIZATION.md) and [docs/BENCHMARKS.md](docs/BENCHMARKS.md) for methods, provenance, rejected candidates, and limitations.

## Important limitations

- Historical K-depth sweep, aligned A/B, HumanEval+ and five-image results do not qualify v0.8. Existing benchmark scripts/documents are retained as historical tools, not a new v0.8 campaign.
- Public recipe changes have not been GPU-launched; local CPU tests cannot establish clean-machine GPU reproducibility.
- Native video is disabled and unqualified. Sixteen-image and near-1M capabilities were tested separately in the live implementation.
- DFlash2 at the pinned revision is non-commercial under CC BY-NC-ND 4.0.
- Uncensored weights reduce refusal behavior; operators are responsible for authorization, safeguards, and legal use.
- The recipe pulls, but does not mirror, the composed runtime image. Its embedded provenance is preserved under `manifests/`; review the upstream image/source boundary.

## Documentation

- [PROVENANCE.md](PROVENANCE.md) — immutable model, drafter, image, and runtime identities
- [ATTRIBUTIONS.md](ATTRIBUTIONS.md) — people, organizations, projects, citations
- [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) — license boundaries and restrictions
- [docs/BENCHMARKS.md](docs/BENCHMARKS.md) — measured performance and capability
- [docs/OPTIMIZATION.md](docs/OPTIMIZATION.md) — K=7 bottleneck, tuning sweep, matched aligned A/B, and production decision
- [benchmarks/README.md](benchmarks/README.md) — exact performance, EvalPlus, and BFCL reproduction steps
- [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) — startup and memory diagnostics

The recipe's own scripts and documentation are Apache-2.0 licensed. Model weights, drafter weights, container layers, and upstream software retain their own licenses.
