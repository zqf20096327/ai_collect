<p align="center">
  <img src="./assets/nex-logo.svg" alt="Nex-AGI" width="160" />
</p>

<h1 align="center">Nex-N2.6</h1>

<p align="center">
  <strong>API</strong> 👉 <a href="https://openrouter.ai/nex-agi/nex-n2.6"><strong>OpenRouter</strong></a> · <a href="https://platform.moss.cn/docs/models/nex-n2-6"><strong>MOSS</strong></a>
</p>

<p align="center">
  <a href="https://huggingface.co/nex-agi/Nex-N2.6"><img src="./assets/hf-link.svg" alt="Hugging Face: https://huggingface.co/nex-agi/Nex-N2.6" width="360" /></a>
</p>

Nex-N2.6 is a multimodal agentic model from Nex-AGI, built on [GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash-BF16). It is designed for computer use, coding, and long-horizon tasks involving tools. This repository contains the FP8-quantized weights of Nex-N2.6, with approximately 321B parameters.

Following [Nex-N2.5-Pro](https://huggingface.co/nex-agi/Nex-N2.5-Pro), this release focuses on reducing repetitive reasoning and improving adherence to the tools available in the current environment.

## Highlights

- 🔥 **Less repetitive reasoning:** Reasoning repetition fell from 16.0% to 1.6% compared with Nex-N2.5-Pro in our internal checkpoint-replay evaluation—a 90% relative reduction.
- 🛠️ **Improved tool-list adherence:** Nex-N2.6 achieved 100% tool-list adherence among responses making tool calls in our internal evaluation.
- 🖥️ **Stronger computer use:** Nex-N2.6 scored 83.0 on OSWorld, up from 82.2 for Nex-N2.5-Pro and 78.0 for the base model, GLM-5.3-Flash.

## Performance

The following results are reported by the Nex-AGI team for this release. Scores depend on the evaluation harness and settings. These are model-level results, not a separate evaluation of this FP8 export.

| Benchmark ↑ | GLM-5.3-Flash | DeepSeek-V4.1-Flash | Nex-N2.5-Pro | Nex-N2.6 |
| --- | ---: | ---: | ---: | ---: |
| OSWorld | 78.0 | 71.7 | 82.2 | **83.0** |
| Terminal-Bench 2.1 | 84.3 | 82.7 | 82.7 | 84.1 |
| AutomationBench | 48.8 | 54.8 | 44.2 | 45.7 |

### Internal reliability evaluations

These evaluations are built from issues encountered in real tasks by our team and partner teams. Known-issue replay fixes the preceding conversation and tool outputs, then tests the model's next response. Tool-list adherence checks whether generated calls use only the tools declared in the request.

| Metric | Nex-N2.5-Pro | GLM-5.3-Flash | Nex-N2.6 |
| --- | ---: | ---: | ---: |
| Reasoning Repetition Rate ↓ | 16.0% | 6.0% | **1.6%** |
| Overall Non-Repetition Rate ↑ | 91.0% | 96.2% | **97.8%** |
| Valid Tool Selection Rate (Overall) ↑ | 82.2% | 85.3% | **100.0%** |
| Valid Tool Selection Rate (When with Tools) ↑ | 80.5% | 84.1% | **100.0%** |

## Usage

Use an inference runtime with GLM-5.3-Flash support. For self-hosting, follow the [official SGLang deployment guide](https://github.com/sgl-project/sglang/blob/main/docs/cookbook/autoregressive/GLM/GLM-5.3-Flash.mdx) and select an **FP8-compatible** configuration for your hardware. Replace the model path with the downloaded Nex-N2.6 directory and set `--served-model-name Nex-N2.6`. Keep the tokenizer, processor, and chat template shipped with these weights.

Once the OpenAI-compatible server is listening on port 8000:

```bash
curl -N http://localhost:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "Nex-N2.6",
    "messages": [
      {"role": "user", "content": "Write a Python function that checks whether a string is a palindrome."}
    ],
    "reasoning_effort": "max",
    "max_tokens": 8192,
    "stream": true
  }'
```

The bundled chat template supports `reasoning_effort` values `low`, `high`, and `max`, defaulting to `max`. For image inputs, use image content blocks supported by your serving runtime. For tool use, supply the available tools with each request; the client or agent framework executes tool calls and returns their results.

## Community

Scan a QR code to join the Nex-AGI community group and connect with the team.

<table align="center">
  <tr>
    <td align="center"><img src="./assets/feishu-group.jpeg" alt="Feishu community group QR code" width="200" /></td>
    <td align="center"><img src="./assets/wechat-group.png" alt="WeChat community group QR code" width="200" /></td>
  </tr>
  <tr>
    <td align="center">Feishu Group (飞书社区群)</td>
    <td align="center">WeChat Group (微信社区群)</td>
  </tr>
</table>
