<!-- markdownlint-disable-file MD041 -->

<p align="center">
  <img src="docs/assets/vLLM-GR.png" alt="vLLM-GR" width="55%">
</p>

<h3 align="center">vLLM-GR brings generative recommendation models to vLLM.</h3>

<p align="center">
  <a href="https://slack.vllm.ai"><b>Developer Slack</b></a> |
  <a href="docs/assets/wechat.jpg"><b>WeChat</b></a>
</p>

## Latest News

- [2026/11] vLLM community officially released [vllm-project/vllm-gr](https://github.com/vllm-project/vllm-gr)
  in order to support generative recommendation model serving.

## About

[vLLM](https://github.com/vllm-project/vllm) was originally built to serve
large language models that generate text autoregressively. vLLM-GR extends
that foundation to recommendation, where a model uses a person's interaction
history to predict which items will interest them. vLLM-GR is an independent
extension of vLLM.

- **Recommendation inputs.** Views, clicks and other interactions describe a
  user's history. A prompt can ask the model to recommend the next item.
- **Model architectures.** The current implementation focuses on inference
  for autoregressive generative recommendation models.
- **Recommendation outputs.** Generation returns candidate item IDs, such as
  semantic IDs (SIDs), ordered by sequence likelihood. Ranking a supplied
  candidate set is planned.

![Recommendation model architecture for generating ranked item IDs, with a separate planned path for scoring supplied candidates.](docs/assets/framework-overview.svg)

### vLLM-GR is fast with

- **One submission for the entire beam search.** The frontend submits the
  request to EngineCore once. The engine drives prefill and every decode step,
  then returns the ranked candidates and their scores in one response.
- **BeamAttn and KV cache reuse.** All beams attend to the same cached prompt.
  The beam KV cache carries each selected parent's suffix into the next step.
  Across requests, vLLM's prefix cache skips prefill for matching prompt blocks.
- **Asynchronous scheduling.** While the device executes one step, the
  host can prepare and submit the next. This overlaps host preparation with
  device execution across prefill and decode.
- **On-device beam postprocessing.** Device kernels apply catalog constraints
  and select the highest-scoring valid continuations. The next decode step
  uses the selected tokens directly on the device, avoiding a host round trip
  for each beam decision.

### vLLM-GR is flexible and easy to use with

- Generate candidate SIDs with full-vocabulary or catalog-constrained Beam
  search. Set per-step candidate and beam widths and the result count.
- Reuse the same `gr` configuration for offline Python inference,
  OpenAI-compatible HTTP completions, and experimental gRPC serving.
- Roll out model weights and replace item catalogs independently. Weight updates
  pause and drain instances. Online catalog replacement requires asynchronous
  Beam execution on CUDA.
- Reuse vLLM's platform abstraction to support CUDA GPUs and Ascend NPUs with
  device-specific worker and ModelRunner optimizations, and extend support to
  other hardware backends.

### vLLM-GR supports the following models

- **Generative recommendation.** [OneRec-1.7B](https://huggingface.co/OpenOneRec/OneRec-1.7B)
  generates a ranked list of candidate SIDs for a user's history.

## Getting Started

- [Installation](docs/getting_started/installation/README.md) — Install vLLM-GR
  from source on NVIDIA GPUs or Ascend NPUs.
- [OneRec quickstart](docs/getting_started/quickstart.md) — Generate ranked
  recommendations with OneRec-1.7B offline or serve the model over HTTP.
- [Feature compatibility](docs/user_guide/feature_compatibility.md) — Check
  which beam search and serving features are supported on each platform.

## Contributing

We welcome and value any contributions and collaborations.
Please check out [Contributing to vLLM-GR](./CONTRIBUTING.md) for how to get involved.

## Join the Community

Ask questions and share feedback in `#sig-gr` on [vLLM Developer Slack](https://slack.vllm.ai),
or scan the [vLLM-GR WeChat group QR code](docs/assets/wechat.jpg) in WeChat.
If the QR code has expired, ask for a fresh one in `#sig-gr`.

## Security

See the [security policy](SECURITY.md) for reporting and deployment guidance.

## License

Apache License 2.0, as found in the [LICENSE](./LICENSE) file.
