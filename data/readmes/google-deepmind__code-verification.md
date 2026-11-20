**Reviewers' site: [google-deepmind.github.io/code-verification](https://google-deepmind.github.io/code-verification/)**: browse the specifications, proofs and checks.

## License

Copyright 2026 Google LLC

All code is licensed under the Apache License, Version 2.0 (the "Apache 2.0"); you may not use this file except in compliance with the Apache 2.0 license. You may obtain a copy of the License at https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and
limitations under the License.

# Formal Verification of Signal's Security in Lean

We present two AI-generated proofs of security for compiled AArch64 machine code of
`libsignal` (the official Rust implementation of the Signal protocol) in a CLI harness
(including its linked cryptographic primitives, formatting, and I/O, with no external hooks other
than mapping 18 Rust panic entry points to `SIGABRT`, DEV-E7).
These provide independent arguments for security, one under the symbolic model and one under the
computational model.

**Scope and headline caveats.** Every non-panic instruction executes directly from plain loaded ELF
memory (`ElfImage.loadState` with zero initial memory patches and pinned auxiliary vector
`AT_HWCAP = 0x1b`, `AT_HWCAP2 = 0`, DEV-CLI10); the `.symtab` trust point is that the pinned ELF
accurately labels the 18 intercepted Rust panic entry points (DEV-E7) and the 5 `libcrux_ml_kem`
`SampleNTT` entry points (DEV-CLI22). Because `libcrux_ml_kem`'s compiled `SampleNTT`
(`sample_from_xof`) rejection loop executes directly rather than behind a total hook, runs that
reach one of those 5 entry points with a SHAKE-128 matrix seed for which `SampleNTT` never yields
256 coefficients `< 3329` are excused from termination in binary correctness (`CliPqxdhElfCorrect`)
and symbolic progress (`CliElfProgress` / `CliElfProgressReal`), and add a `2 · CliPqxdhFlagProb`
term to both clauses of the computational security bound (`CliPqxdhElfSecure`; probability `0` under
an idealized random XOF, but not further bounded in Lean since an adversary can influence the seeds,
DEV-CLI22). Binary correctness (`CliPqxdhElfCorrect`) also excuses `.OutOfMemory` (DEV-CLI15),
whereas computational security (`CliPqxdhElfSecure`) carries no `.OutOfMemory` premise or term
under the modelled 1 GiB memory budget. The computational main theorem
(`libsignal_cli_pq_secure_elf_binary`) instantiates Kyber-1024 at `kyber1024KemKeyGen` with
`δ_kem = ε + 2^-112` under the CBD-noise idealization hypothesis `KyberNoiseGap ε` and public-key
collision premise `_hKemColl ≤ 2^-255` (DEV-PQ21), and Clause 2 adds `2 · ε_ro` under the HKDF
random-oracle gap `KeyIndRoGap` (DEV-CLI16). On the symbolic side, `signal_session_secure_real` and
`comp_refines_cli_real` (via `real_prims_admissible`) fix the primitives to the real linked ones
(`realCliHooks`, via `RealPrimsMatch`) over the unfiltered ELF run `elfRelReal`, alongside the
hook-parametric `signal_session_secure` and `comp_refines_cli`. See
[`Computational/docs/DEVIATIONS.md`](Computational/docs/DEVIATIONS.md) and
[`Computational/docs/TRUSTED_BASE.md`](Computational/docs/TRUSTED_BASE.md) for the full deviation
catalogue and trusted base.

For more information, please see the associated paper.
The file [`docs/PAPER_MAP.md`](docs/PAPER_MAP.md) provides links from sections in the paper,
such as descriptions of theorems, to the Lean code that formalizes it. A detailed overview of the
computational development is in [`Computational/docs/README.md`](Computational/docs/README.md);
the symbolic theorems are in [`Symbolic/Theorems/`](Symbolic/Theorems/).

```text
├── Computational/     # Computational (game-based) security specs, proofs, and headline theorems
├── Symbolic/          # Symbolic (Dolev–Yao) model, binary refinement, proofs, and theorems
├── LibsignalBinary/   # Shared AArch64 binary specs, hook models, and function proofs
├── arm64-semantics/   # Formal AArch64 ISA/process semantics, separation logic, and rust-obj2lean
├── third_party/       # Official libsignal crates (v0.105.4 + spqr v1.6.0) and libsignal-cli CLI
├── scripts/           # Stock ld.lld CLI ELF builder (cli-elf-stock), trusted-closure, and axiom audit scripts
└── docs/              # Paper-to-code map (docs/PAPER_MAP.md) and symbolic paper differences
```

## Building and Verifying

### Prerequisites

- **Lean 4** via [`elan`](https://github.com/leanprover/elan) (`lean-toolchain` pins `leanprover/lean4:v4.35.0`).
- **Rust `1.98.1`** (pinned in [`rust-toolchain.toml`](rust-toolchain.toml); `.GeneratedLean/` depends on the exact `rustc` output, so do not override the pin) with cross-compilation targets, `rust-src`, and LLVM tools:
  ```bash
  rustup toolchain install 1.98.1 \
    --target aarch64-unknown-linux-gnu,aarch64-unknown-linux-musl \
    --component rust-src,llvm-tools-preview
  ```
- **`protoc`** (Protocol Buffers compiler, used by `libsignal`'s `prost-build` scripts), **LLVM `ld.lld` `22.1.8`**, and **[Zig `0.16.0`](https://ziglang.org/)** on `PATH`.

### Build and Kernel-Check All Proofs

```bash
# 1. Fetch prebuilt Mathlib:
lake exe cache get

# 2. Raise the soft stack limit (needed by `leantar` on large modules), materialize cached
#    `.olean` files into `.lake/`, and bound parallel Lean workers (use about 1 thread per
#    4 GiB of free RAM, plus some headroom), then compile libsignal, extract it to Lean, and
#    check all default Lean proofs (several hours, ~15–34 GiB peak RAM):
ulimit -S -s 524288
export LAKE_RESTORE_ARTIFACTS=true
export LEAN_NUM_THREADS=8   # ~1 per 4 GiB of free RAM; Lake has no -j flag
lake build

# 3. Build the SHA-256-pinned `libsignal-cli` AArch64 ELF from source with stock `ld.lld`, verify
#    its pin, and check the binary-level headline theorems in `CliElfLib`
#    (`Computational/Theorems/Main.lean` and `Symbolic/Theorems/{Security,Refinement}.lean`):
./scripts/cli-elf-stock --stdbin --build
./scripts/cli-elf-stock --stdbin --verify-pin --lean-mod LibsignalBinary/Specifications/SignalSession/CliElf.lean
lake build CliElfLib
lake script run checkCliElfOwner
```

### Verify Headline Theorems with Comparator

[`leanprover/comparator`](https://github.com/leanprover/comparator) verifies that each headline
theorem matches its trusted challenge statement (including all transitive definitions), uses only
standard Lean axioms (`propext`, `Quot.sound`, `Classical.choice`), and replays in a fresh Lean
kernel from `lean4export` output rather than `.olean` files.

Running this check (`comparator/install-tools.sh` and `comparator/run.sh`) is only supported on
Linux, as `leanprover/comparator` sandboxes its builds and exports with
[`landrun`](https://github.com/Zouuup/landrun) (which uses Linux's Landlock LSM).

```bash
# 1. Build the pinned comparator, lean4export, and landrun tools and export their paths:
comparator/install-tools.sh /tmp/comparator-tools
set -a; source /tmp/comparator-tools/env; set +a

# 2. Build the challenge and solution libraries (`comparator/`), then check both
#    `comparator/computational.json` and `comparator/symbolic.json` (or pass one config):
lake build ComparatorChallenge ComparatorSolution
comparator/run.sh
```

### Audit Axioms and the Trusted Base

After building (`lake build` and, for the binary-level `CliElfLib` headlines, Step 3 above),
[`scripts/trusted-closure.sh`](scripts/trusted-closure.sh) runs
[`scripts/TrustedClosure.lean`](scripts/TrustedClosure.lean) to compute the per-theorem transitive
declaration closure (`trusted_closure.csv`, `trusted_closure.md`, and per-module
`trusted_banners.csv`), enforce Rule 5 (no proof-tree definition unfolded in a headline's
statement closure), and report each headline theorem's kernel axioms (`## Axioms` in
`trusted_closure.md`) for inspection, while [`comparator/run.sh`](comparator/run.sh) (above)
fail-closed enforces `std3`-only axioms (`propext`, `Classical.choice`, `Quot.sound`). For the
tiered breakdown, line counts, and reading guide, see
[`Computational/docs/TRUSTED_BASE.md`](Computational/docs/TRUSTED_BASE.md).

```bash
# Default computational lemmas (`L1`, `L2`, `L3`, and `KyberDelta` in `Computational/Theorems/Lemmas.lean`):
./scripts/trusted-closure.sh --out-dir /tmp/closure-default

# All 8 computational and ELF-direct symbolic binary headlines (`scripts/trust_banner_headlines.txt`):
./scripts/trusted-closure.sh --headlines-file scripts/trust_banner_headlines.txt --out-dir /tmp/closure-banners

# The 14 `symbolicHeadlines` (`Symbolic/Theorems/` and `Symbolic/Tests/ExternWitness.lean`;
# 3 additional real-primitive headlines are listed in `Computational/docs/TRUSTED_BASE.md` §7):
./scripts/trusted-closure.sh --symbolic --out-dir /tmp/closure-symbolic
```

## License and disclaimer

Copyright 2026 Google LLC

Unless a file states otherwise, the software in this repository is licensed under the license
described in [`LICENSE`](LICENSE). Third-party material, including code copied from
Signal's `libsignal` (AGPL-3.0-only), keeps its own license. The libsignal crates live in
[`third_party/libsignal/`](third_party/libsignal/), with the upstream
[`LICENSE`](third_party/libsignal/LICENSE) and a [`README.md`](third_party/libsignal/README.md)
that lists what is copied from libsignal; each file states its license in its header comment. To
contribute, see [`CONTRIBUTING.md`](CONTRIBUTING.md).

Unless required by applicable law or agreed to in writing, all software distributed here is
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
implied. See the licenses for the specific language governing permissions and limitations under
those licenses.

This is not an official Google product.

Eligibility for the [Google Open Source Software Vulnerability Rewards
Program](https://bughunters.google.com/open-source-security) is determined by the [Google Open Source Software Vulnerability Reward Program Rules](https://bughunters.google.com/about/rules/open-source/google-open-source-software-vulnerability-reward-program-rules).
