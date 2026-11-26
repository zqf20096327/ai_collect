<a href="https://www.doji-tech.com/">
  <img src="https://www.doji-tech.com/assets/favicon.ico" alt="doji logo" title="Doji" align="right" height="70" />
</a>

# Transformers
A Unity package to run pretrained transformer models with Unity Inference Engine

[OpenUPM] · [Documentation (coming soon)] · [Feedback/Questions]

## About

This is essentially a C# port of Hugging Face’s [transformers] library.

There are two use cases for this package right now:
- It's used by the [tools.doji.diffusers] package to run Stable Diffusion models in Unity (most SD models use a CLIPTokenizer for prompting, newer pipelines require additional ones like T5Tokenizer)
- To run small LLMs like [SmolLM2](https://huggingface.co/julienkay/SmolLM2-135M-Instruct-sentis-float16) in Unity

### Installation

<details>
  <summary> via OpenUPM </summary>
  
 1. In `Edit -> Project Settings -> Package Manager`, add a new scoped registry:

        Name: Doji
        URL: https://package.openupm.com
        Scope(s): com.doji
 
  4. In the Package Manager install `tools.doji.transformers` either by name or select it in the list under `Package Manager -> My Registries`

</details>

### Usage

Models come through [AI Model Hub] (`tools.doji.model-hub`). List them in the project's AI Model Hub manifest (`Project Settings > Doji > AI > AI Model Hub`).

```csharp
using Doji.AI.Transformers;

var tokenizer = await AutoTokenizer.FromPretrainedAsync("julienkay/SmolLM2-135M-Instruct-sentis-float16");
var model = await AutoModelForCausalLM.FromPretrainedAsync("julienkay/SmolLM2-135M-Instruct-sentis-float16");

string prompt = tokenizer.ApplyChatTemplate(new[] { ChatMessage.User("What is the capital of France?") });
int[] inputIds = tokenizer.Encode(prompt, addSpecialTokens: false).InputIds.ToArray();
var streamer = new TextStreamer(tokenizer, text => Debug.Log(text), skipPrompt: true);
int[] outputIds = await model.GenerateAsync(inputIds, new GenerationConfig { MaxNewTokens = 64 }, streamer);
```

To try it, import the **Text Generation Sample** from the Package Manager and open its scene. The sample lists its model in a Model Hub manifest asset, so Model Hub downloads the model after the import.

`FromPretrained` and `Generate` (without `Async`) run without waiting. They work in the Editor and for bundled or already downloaded models on Windows, macOS, Linux and iOS.

The models are plain ONNX exports with the input and output names of optimum (`input_ids`, `attention_mask`, `position_ids`, `past_key_values.*`). `tools/causal_lm/make_models.py` exports a transformers model this way.

#### GGUF files

`AutoModelForCausalLM.FromGguf` loads a model from a GGUF file of llama.cpp, for example one of [ggml-org/Qwen3.5-0.8B-GGUF](https://huggingface.co/ggml-org/Qwen3.5-0.8B-GGUF). Supported architectures: `llama` (for example SmolLM2), `qwen3`, `phi3` (Phi-3 with a context of 4k) and `qwen35` (Qwen3.5). Q8_0, Q4_K, Q5_K and Q6_K weights stay quantized on the GPU, which covers Q8_0 and Q4_K_M files. F32 tensors stay float32, other types become float16. `AutoTokenizer.FromGguf` loads the tokenizer and the chat template from the metadata of the same file.

```csharp
var model = AutoModelForCausalLM.FromGguf("Models/Qwen3.5-0.8B-Q8_0.gguf");
var tokenizer = AutoTokenizer.FromGguf("Models/Qwen3.5-0.8B-Q8_0.gguf");
```

### Performance

Rough numbers for greedy generation in Play mode with one frame after each token, as the sample runs. Each model generates 64 tokens after a short chat prompt.

| Model | Tokens/s<br>D3D12 / D3D11 | Peak VRAM<br>D3D12 / D3D11 | Peak RAM<br>D3D12 / D3D11 |
|---|---|---|---|
| [SmolLM2-135M-Instruct-sentis-float16](https://huggingface.co/julienkay/SmolLM2-135M-Instruct-sentis-float16) | 13.2 / 21.8 | 0.5 / 0.5 GB | +0.3 / +0.3 GB |
| [SmolLM2-360M-Instruct-sentis-float16](https://huggingface.co/julienkay/SmolLM2-360M-Instruct-sentis-float16) | 11.2 / 19.0 | 1.1 / 1.0 GB | +0.4 / +0.3 GB |
| [SmolLM2-1.7B-Instruct-sentis-float16](https://huggingface.co/julienkay/SmolLM2-1.7B-Instruct-sentis-float16) | 10.2 / 11.0 | 4.0 / 4.0 GB | +0.5 / +0.6 GB |
| [Phi-3-mini-4k-instruct-sentis-uint8](https://huggingface.co/julienkay/Phi-3-mini-4k-instruct-sentis-uint8) | 6.7 / 7.4 | 4.4 / 4.5 GB | +0.3 / +0.4 GB |
| [Phi-3-mini-4k-instruct-sentis-float16](https://huggingface.co/julienkay/Phi-3-mini-4k-instruct-sentis-float16) | 6.0 / 6.5 | 7.8 / 7.7 GB | +0.5 / +0.6 GB |

In a release Player (vSync on), `GenerateAsync` picks the tokens on the GPU and takes about one frame per token. 64 tokens after a short prompt, the second of two runs:

| Model | Greedy, tokens/s<br>D3D12 / D3D11 | Sampling, tokens/s<br>D3D12 / D3D11 |
|---|---|---|
| SmolLM2-135M-Instruct-sentis-float16 | 46.6 / 49.7 | 37.7 / 37.9 |
| SmolLM2-1.7B-Instruct-sentis-float16 | 16.0 / 12.1 | 14.5 / 11.3 |

Sampling uses temperature 0.7, top-k 50, top-p 0.9 and repetition penalty 1.1. The Play mode table above was measured before the sampling moved to the GPU, when each token took about 3 frames.

A small model runs several steps per frame. `PreTrainedModel.Pacing` caps the main-thread time that `GenerateAsync` spends on scheduling steps per frame (`MaxMillisecondsPerFrame`, 4 ms by default). julienkay/tiny-random-LlamaForCausalLM-onnx (2 layers), 512 greedy tokens in a release Player with vSync on:

| `MaxMillisecondsPerFrame` | D3D12 | D3D11 |
|---|---|---|
| 1 | 60 tokens/s, 16.7 ms/frame | 60 tokens/s, 16.7 ms/frame |
| 4 | 110 tokens/s, 16.7 ms/frame | 79 tokens/s, 16.7 ms/frame |
| 8 | 153 tokens/s, 16.7 ms/frame | 170 tokens/s, 16.7 ms/frame |
| 16 | 181 tokens/s, 18.2 ms/frame | 353 tokens/s, 17.5 ms/frame |

With `SpreadStepsOverFrames`, a step that takes longer than a frame goes on in the next frames. 64 greedy tokens, vSync on, mean frame time:

| Model | Default pacing<br>D3D12 / D3D11 | Spread, 4 ms<br>D3D12 / D3D11 | Spread, 8 ms<br>D3D12 / D3D11 |
|---|---|---|---|
| SmolLM2-135M-Instruct-sentis-float16 | 48 / 49 tokens/s, 21 / 20 ms/frame | 11.1 / 10.8 tokens/s, 17.0 / 16.8 ms/frame | 23.9 / 22.7 tokens/s, 17.1 / 16.9 ms/frame |
| SmolLM2-1.7B-Instruct-sentis-float16 | 15.9 / 12.0 tokens/s, 63 / 83 ms/frame | 14.6 / 11.8 tokens/s, 20.1 / 21.7 ms/frame | 15.5 / 12.1 tokens/s, 32.4 / 39.4 ms/frame |

The budget is main-thread time. SmolLM2-1.7B does much more GPU work per step than CPU work, so its parts of 8 ms carry more GPU work than a frame. Single frames take longer than the mean: with SmolLM2-1.7B, the longest frame of a run was 83 / 129 ms at 4 ms and 136 / 162 ms at 8 ms. With SmolLM2-135M, it was 106 / 42 ms at 4 ms and 68 / 34 ms at 8 ms.

Long prompts with Phi-3-mini-4k-instruct-sentis-float16, 4 new tokens after the prompt:

| Prompt | D3D12 | D3D11 |
|---|---|---|
| 1024 tokens | 3.6 tokens/s, 10.3 GB VRAM | 4.2 tokens/s, 9.4 GB VRAM |
| 2048 tokens | 2.1 tokens/s, 11.6 GB VRAM (at the limit of the GPU) | 3.0 tokens/s, 9.7 GB VRAM |
| 3072 tokens | not run: 2048 tokens already fill the GPU | 2.2 tokens/s, 10.3 GB VRAM (11.5 GB peak) |

Loading Qwen3.5-0.8B with `BackendType.GPUCompute` in a headless Editor (PlayMode test), D3D12, warm file cache, 3 runs each. Load is the time to a model ready to generate. 32 greedy tokens after a short chat prompt, the second of two runs, compared with the tokens of transformers (float32):

| Source | Load | RAM after load | VRAM after load | 32 tokens | Same tokens as transformers |
|---|---|---|---|---|---|
| `model.sentis`, float16 (`ModelFile`) | 1.9–2.0 s | +1.5 GB | 1.9 GB | 2.1 s | 32 of 32 |
| [Qwen3.5-0.8B-BF16.gguf](https://huggingface.co/ggml-org/Qwen3.5-0.8B-GGUF) (`FromGguf`, float16 on the GPU) | 3.1 s (4.3 s first run) | +1.5 GB | 1.9 GB | 1.7–1.9 s | 32 of 32 |
| [Qwen3.5-0.8B-Q8_0.gguf](https://huggingface.co/ggml-org/Qwen3.5-0.8B-GGUF) (`FromGguf`, Q8_0 on the GPU) | 1.6–1.7 s | +0.6 GB | 0.8 GB | 0.8 s | 32 of 32 |
| [Qwen3.5-0.8B-Q4_K_M.gguf](https://huggingface.co/unsloth/Qwen3.5-0.8B-GGUF) (`FromGguf`, Q4_K, Q5_K, Q6_K and Q8_0 on the GPU) | 1.5–1.9 s | +0.5 GB | 0.5 GB | 0.7–0.8 s | first 25 of 32 |

- Peak VRAM is the GPU memory that the model adds, from `nvidia-smi`. In the long-prompt table, VRAM is the memory of the whole GPU while the model holds its cache.
- Peak RAM is the resident memory (working set) that the Editor process adds while it loads and runs the model.
- D3D12 is the default graphics API of Unity 6 on Windows. On D3D12, GPU memory that a model frees during a long prompt can't be reused in the same frame, so long prompts need more VRAM. To use D3D11, turn off *Auto Graphics API for Windows* in the Player settings and put Direct3D11 first, or start the Editor with `-force-d3d11`.
- Measured on 2026-11-24 (the release Player tables of SmolLM2 and the Qwen3.5 load table on 2026-11-25) with `BackendType.GPUCompute`, Unity 6000.6.4f1, an NVIDIA GeForce RTX 3060 (12 GB) and an Intel Core i7-4790K. The D3D11 numbers come from one run per model.

## Roadmap:

Tokenizers
- [x] TokenizersBackend (any `tokenizer.json`, as in transformers v5)
- [x] CLIPTokenizer
- [x] LlamaTokenizer
- [x] GPT2Tokenizer
- [x] Qwen2Tokenizer

LLMs
- [x] Llama (SmolLM2)
- [x] Phi-3
- [x] Qwen3 (from GGUF files)
- [x] Qwen3.5 (text)
- [x] GGUF files of llama.cpp (`llama`, `qwen3`, `phi3`, `qwen35`)

### Dependencies
- [AI Model Hub] (`tools.doji.model-hub`)
- GGUF Format (`tools.doji.formats.gguf`)
- [Tokenizers] (`tools.doji.tokenizers`)

[OpenUPM]: https://openupm.com/packages/tools.doji.transformers
[Documentation (coming soon)]: https://github.com/julienkay/tools.doji.transformers
[Feedback/Questions]: https://discussions.unity.com/t/stable-diffusion-diffusers-transformers-package/332701?u=julienkay
[transformers]: https://github.com/huggingface/transformers
[tools.doji.diffusers]: https://github.com/julienkay/tools.doji.diffusers
[AI Model Hub]: https://docs.doji-tech.com/tools.doji.model-hub
[Tokenizers]: https://github.com/julienkay/tools.doji.tokenizers
