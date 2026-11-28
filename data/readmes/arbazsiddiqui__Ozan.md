# Ozan

**A 12B creative-writing model tuned to write long-form fiction that *doesn't sound like an LLM.***

![Ozan, the storyteller](./ozan_banner.png)

*Ozan* means **"storyteller / bard"** in Turkish. The model is a fine-tune of **Mistral-Nemo-Instruct-2407** built around one goal: **low slop.** "Slop" is the family of over-used LLM tells: *"barely above a whisper," "a testament to," "couldn't help but,"* the reflexive *"not just X, but Y."* It comes mostly from training on GPT-style synthetic data, and it's the single biggest reason machine prose reads as machine prose. Ozan is trained, and *measured*, to avoid it.

This repo holds the training recipe. The weights, quants and sample stories live on Hugging Face:

| | link |
|---|---|
| Full-precision (BF16) | [huggingface.co/arbazsiddiqui/Ozan-v1-12B](https://huggingface.co/arbazsiddiqui/Ozan-v1-12B) |
| GGUF quants (Q4/Q5/Q6/Q8) | [huggingface.co/arbazsiddiqui/Ozan-v1-12B-GGUF](https://huggingface.co/arbazsiddiqui/Ozan-v1-12B-GGUF) |
| Hosted, no download (Featherless) | [featherless.ai/models/arbazsiddiqui/Ozan-v1-12B](https://featherless.ai/models/arbazsiddiqui/Ozan-v1-12B) |

## Why this model exists

Instruct models tell a decent story but write sloppily: base Mistral-Nemo-Instruct scores **9.47** on the EQ-Bench Creative Writing v3 slop metric. Two steps fix that:

1. **SFT (QLoRA)** on ~17k curated, *low-slop* examples: prose distilled from strong **non-GPT** models (the Claude-Opus and Gemini-3-Pro families) plus filtered human Reddit WritingPrompts for range. This teaches voice and roughly halves the slop.
2. **Gutenberg anti-slop DPO**: preference-tuned toward real public-domain book prose over AI prose. This removes the slop that's left without hurting fluency.

## Results: lowest-slop runnable 12B

Slop and repetition are computed **directly from the generated text** (no LLM grading involved) by the [EQ-Bench Creative Writing v3](https://github.com/EQ-bench/creative-writing-bench) harness (by Sam Paech), run identically on every model's 96 generations (32 prompts × 3). **Lower is better.**

![Slop comparison](./ozan_slop_chart.png)

| model | size | slop ↓ | repetition ↓ |
|---|---|---|---|
| gemma-2-9b-it | 9B | 11.92 | 6.30 |
| Mistral-Nemo-Instruct (our base) | 12B | 9.47 | 3.93 |
| Magnum-v4-12b | 12B | 8.57 | 8.99 |
| Gemma-3-Glitter-12B | 12B | 7.68 | 3.63 |
| Gemma-3-Starshine-12B | 12B | 7.52 | 3.59 |
| gemma-3-27b-it | 27B | 7.03 | 3.62 |
| **Ozan-v1-12B** | **12B** | **5.30** | **3.21** |
| QwQ-32B | 32B | 4.90 | 3.56 |
| Mistral-Small-Creative-24B | 24B | 4.25 | 3.36 |

**Lowest slop of any same-size 12B tested**, beating the popular community fine-tunes and a 27B, with the **cleanest repetition in the whole field** and zero degenerate loops across 96 stories.

### Craft (LLM-judged rubric)

Low slop isn't the same as good writing, so craft is checked too, on the EQ-Bench Creative Writing v3 21-dimension rubric (voice, imagery, prose, characterisation, coherence and the rest; judged by **Claude-Sonnet-4**, n=32):

- **Ozan ≈ 58.8 / 100**, a gain of **+11.8 over its own base** (Mistral-Nemo-Instruct ≈ 47) and competitive with the strongest low-slop 12B fine-tunes (60–73). Larger 24–32B models score higher (71–77).
- Strongest on **voice and tone, coherence, instruction-adherence and imagery**; weaker, like most 12Bs, on emotional complexity and surprise.

Three unedited sample stories are on the [model card](https://huggingface.co/arbazsiddiqui/Ozan-v1-12B#samples).

## Use it

Quickest, with [Ollama](https://ollama.com):

```bash
ollama run hf.co/arbazsiddiqui/Ozan-v1-12B-GGUF:Q4_K_M
```

Or load a GGUF in **LM Studio, llama.cpp or koboldcpp**:

| quant | size | notes |
|---|---|---|
| `Q4_K_M` | 7.5 GB | recommended default, best size/quality |
| `Q5_K_M` | 8.7 GB | higher quality |
| `Q6_K` | 10.1 GB | near-lossless |
| `Q8_0` | 13.0 GB | effectively lossless |

No CUDA needed: on an Apple Silicon Mac, `Q4_K_M` wants 16 GB of unified memory or more, and `Q8_0` is comfortable from 32 GB.

**Recommended sampler** (matters for this model):

```
temperature      0.7
min_p            0.1
DRY: multiplier  0.8   base 1.75   allowed_length 2
```

DRY (a repetition control, on by default in modern llama.cpp and koboldcpp) keeps long outputs clean and trims residual repeated phrasing, which lowers both repetition and slop at no quality cost. Ozan writes ~1000-word completions on its own, so there's no need to force length.

**Chat template:** native Mistral `[INST] … [/INST]`.

### Python (full precision, transformers)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "arbazsiddiqui/Ozan-v1-12B"
tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", torch_dtype="bfloat16")

messages = [{"role": "user", "content": "Write a 1000-word story about a lighthouse keeper who collects forgotten sounds."}]
ids = tok.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)
out = model.generate(ids, max_new_tokens=1200, do_sample=True, temperature=0.7, min_p=0.1)
print(tok.decode(out[0][ids.shape[1]:], skip_special_tokens=True))
```

DRY is a llama.cpp/koboldcpp sampler, so the DRY settings apply to the GGUF builds; `transformers` supports the `temperature` and `min_p` part.

## Recipe

```
Mistral-Nemo-Instruct-2407
  -> QLoRA SFT  (~17k curated low-slop examples)
  -> Gutenberg anti-slop DPO
  -> merge to BF16  ->  GGUF (imatrix quants)
```

Trained on a single **NVIDIA A100** spot instance (GCP).

1. **SFT (QLoRA).** `train/sft_instruct.py` (TRL), rank 32, lr 5e-5 cosine, seq 4096, native Mistral `[INST]` format with completion-only loss, early-stopped once the slop metric plateaued.
2. **Gutenberg anti-slop DPO.** `train/dpo_gutenberg.py`: a LoRA DPO pass (rank 64, β 0.1, 200 steps) over [sam-paech/gutenbergs_1_2_3_4-antislop-dpo](https://huggingface.co/datasets/sam-paech/gutenbergs_1_2_3_4-antislop-dpo) (chosen = real public-domain book prose, rejected = AI prose), via TRL `DPOTrainer`. Trained to the point where the slop metric bottomed out; pushing it further only put slop back.
3. **Merge and quantize.** Merge the adapters to BF16, convert to GGUF with `llama.cpp`, compute an importance matrix (imatrix) on the Q8_0 model with bartowski's standard `calibration_datav3.txt`, then `llama-quantize --imatrix` for each level.

### Training data

- **Low-slop distilled prose:** [Crownelius/Gemini-3-Pro](https://huggingface.co/datasets/Crownelius/Creative-Writing-Gemini3Pro-2700x), [Crownelius/Opus-4.5-WritingStyle](https://huggingface.co/datasets/Crownelius/Opus-4.5-WritingStyle-1000x-formatted-fixed), [Gryphe/Opus-WritingPrompts](https://huggingface.co/datasets/Gryphe/Opus-WritingPrompts), [Kalomaze Opus-Instruct (no-refusal)](https://huggingface.co/datasets/anthracite-org/kalo-opus-instruct-22k-no-refusal)
- **Human voice:** [euclaise/writingprompts](https://huggingface.co/datasets/euclaise/writingprompts)
- **Anti-slop DPO:** [sam-paech/gutenbergs_1_2_3_4-antislop-dpo](https://huggingface.co/datasets/sam-paech/gutenbergs_1_2_3_4-antislop-dpo) (Gutenberg corpora 1–4)

All eval prompts were decontaminated (minhash) against the training data before any run.

## Reproduce

```bash
pip install -r train/requirements-train.txt
export HF_TOKEN=...                                        # for the base-model pull (gated)
# 1) SFT our data into Mistral-Nemo-Instruct-2407:
DATA=./data/train.jsonl OUT=./ozan_sft python train/sft_instruct.py
# 2) merge the SFT adapter to 16-bit, then the Gutenberg anti-slop DPO pass:
python train/dpo_gutenberg.py --model ./ozan_sft_merged --out ./ozan_dpo
```

Records are ChatML-native (`{"messages":[{role,content}], ...}`); `sft_instruct.py` formats them to Mistral `[INST]`, filters any example that would lose its eos to truncation, and preflights the masking before any GPU spend. Slop, repetition and the craft rubric are all measured with the upstream [EQ-Bench Creative Writing v3](https://github.com/EQ-bench/creative-writing-bench) harness: slop and repetition at n=96, the craft rubric at n=32.

## Notes

- **"Slop"** measures how often over-represented LLM phrases show up. It's one axis of quality, so read the samples and judge for yourself.
- **Content:** trained on creative-writing data including some uncensored/NSFW sources; it will write mature fiction. Use responsibly.

## License

Apache-2.0 (see [LICENSE](./LICENSE)), matching the base model. Training data carries its own per-source licenses (see the dataset cards linked above).

## Acknowledgements

The slop/repetition metric and the EQ-Bench Creative Writing benchmark are by **Sam Paech** ([eqbench.com](https://eqbench.com)). Base model by **Mistral AI**. Gutenberg-DPO data by the community.
