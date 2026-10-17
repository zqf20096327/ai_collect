# Kimi K3 GGUF Structural Validation Report

Independent structural validation of UD-IQ1_M and UD-Q4_K_XL without
downloading tensor payloads.

This case study records evidence-backed structural validation of two split GGUF
variants from `unsloth/Kimi-K3-GGUF` at immutable artifact revision `3d4b61ab4b6789d401191c476cbb4567246db8f5`.
It publishes a bounded report, compact deterministic summaries, digest-linked
evidence metadata, and a verifier for this public package.

## Results

- UD-IQ1_M: `STRUCTURALLY_VALIDATED_WITH_LIMITATIONS`
- UD-Q4_K_XL: `STRUCTURALLY_VALIDATED_WITH_LIMITATIONS`
- Cross-quantization comparison:
  `STRUCTURALLY_EQUIVALENT_WITH_QUANTIZATION_DIFFERENCES`
- Both variants contain 2,573 descriptors; their normalized identities and
  shapes match. Remote inspection accepted zero tensor payload bytes.

## Evidence limitations

Artifact-specific provenance is `UNAVAILABLE`. Payload equality and integrity,
quantization fidelity, tokenizer parity, and runtime parity are `NOT_CHECKED`.
The findings do not establish numerical correctness, model quality, benchmark
performance, safety, deployment fitness, or validation of the full Kimi release.

## Contents

- [Full report](report/kimi-k3-gguf-structural-validation-report.md)
- [Evidence manifest](evidence/evidence-manifest.json)
- [Claim registry](evidence/claim-registry.json)
- [Reproducibility manifest](evidence/reproducibility-manifest.json)
- [Public artifact index](evidence/artifact-index.json)
- [IQ1_M summary](summaries/iq1m-validation-summary.json)
- [Q4 summary](summaries/q4-validation-summary.json)
- [Structural comparison](summaries/structural-comparison-summary.json)
- [Reproduction guide](reproduction/README.md)

## Relationship to OMIV

This repository contains the public case-study report, evidence summaries, and
reproducibility metadata generated from an OMIV validation run. The OMIV
validation engine is maintained separately.

## Acknowledgements

Moonshot AI developed and released the Kimi K3 architecture. Unsloth published
the compared GGUF variants. llama.cpp and GGML maintainers provide format,
conversion, and quantization infrastructure. The broader open-model community
supports review and interoperability. Acknowledgement does not imply endorsement.

## Licensing

Original report, evidence summaries, this README, reproduction documentation,
and community drafts are licensed under
[CC BY 4.0](LICENSE-CONTENT). The
[verification shell script](reproduction/verify-evidence.sh) is licensed under
the [Apache License 2.0](LICENSE-CODE).

Kimi K3, the analyzed Unsloth GGUF artifacts, llama.cpp, and GGML remain subject
to their respective upstream licenses. No model weights or tensor payloads are
distributed by this repository. No endorsement is implied. See
[Third-party notices](NOTICE-THIRD-PARTY.md).
