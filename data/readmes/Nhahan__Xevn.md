# Xevn

**English** | [한국어](README.ko.md)

Xevn is a 4B decision model built for Korean. It starts from the general-purpose [Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B) and is further trained for Korean understanding, knowledge, and judgment.

Xevn follows the [Jev](https://benchmarkheaven.com/jev-models) decision format. It reads a question and its options once and returns the answer together with a probability for every option. There is no text generation, so a request costs one forward pass.

## Tasks

| Type | Input | Output |
|---|---|---|
| `choice` | A question and up to 26 options | Probability for each option |
| `noul` | A yes/no question with criteria | Probability of yes |
| `score` | An item and a graded scale | Probability for each level |

## Benchmarks

<p align="center"><img src="assets/acc_en.svg" alt="Korean benchmarks: accuracy" width="100%"></p>

**Accuracy (%)**

| Benchmark | Measures | **Xevn** | JevK5 | Plumb | Decider | Mica | Tev1 |
|---|---|:-:|:-:|:-:|:-:|:-:|:-:|
| KoBEST | Reasoning and commonsense | **89.7** | 69.7 | 84.2 | 74.6 | 72.7 | 67.7 |
| KorMedMCQA | Korean medical licensing exams | **69.4** | 65.5 | 65.5 | 64.3 | 65.8 | 59.7 |
| HAE-RAE | Korean knowledge | **58.3** | 56.5 | 54.9 | 53.7 | 54.6 | 53.2 |
| Belebele | Reading comprehension | **89.0** | 87.4 | 86.6 | 87.2 | 86.3 | 87.6 |
| KMMLU | Expert knowledge across subjects | **56.3** | 52.8 | 55.1 | 54.1 | 54.4 | 47.5 |
| CSAT-QA | Korean SAT reading | **68.8** | 69.4 | 67.7 | 66.2 | 60.5 | 65.1 |
| CLIcK | Korean culture and language | **66.5** | 67.3 | 67.2 | 64.9 | 64.3 | 62.9 |
| KMMLU-1035 | Expert knowledge, second set | **50.1** | 48.0 | 48.3 | 51.0 | 48.2 | 43.6 |

<p align="center"><img src="assets/h_en.svg" alt="Korean benchmarks: Headline" width="100%"></p>

**Headline** = (Intelligence + Calibration) / 2, the JevBench score that combines accuracy and calibration.

| Benchmark | **Xevn** | JevK5 | Plumb | Decider | Mica | Tev1 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| KoBEST | **92.0** | 83.7 | 84.2 | 82.0 | 85.3 | 87.1 |
| KorMedMCQA | **78.7** | 76.7 | 74.0 | 73.1 | 70.4 | 67.1 |
| HAE-RAE | **70.2** | 69.3 | 68.2 | 63.9 | 62.1 | 61.0 |
| Belebele | **90.3** | 89.7 | 87.7 | 89.3 | 86.4 | 89.2 |
| KMMLU | **68.5** | 63.3 | 67.8 | 58.1 | 58.5 | 55.3 |
| CSAT-QA | **76.4** | 76.6 | 77.3 | 72.3 | 65.7 | 74.4 |
| CLIcK | **72.5** | 74.8 | 73.1 | 68.5 | 68.1 | 68.6 |
| KMMLU-1035 | **60.1** | 55.7 | 57.8 | 53.3 | 49.5 | 49.3 |

**Setup.** Every model was run in 16-bit (bf16; Decider in its official FP16) with the same prompts and the same scoring, on an Apple M4 Max.

## Speed

Latency of a single request over HTTP, bf16, Apple M4 Max, 3,000 requests.

| Input length | p50 | p95 |
|---|:-:|:-:|
| up to 64 tokens | 56 ms | 64 ms |
| 65 to 128 tokens | 88 ms | 103 ms |
| 129 to 256 tokens | 156 ms | 188 ms |

## Models

| Precision | Size | Accuracy | Headline | Speed (p50) | Download |
|---|:-:|:-:|:-:|:-:|:-:|
| 16-bit | 8.4 GB | 68.5 | 76.1 | 88 ms | [MLX](https://huggingface.co/quevirus/Xevn-4B-MLX-bf16) |
| 8-bit | 4.5 GB | 68.3 | 76.0 | 83 ms | [MLX](https://huggingface.co/quevirus/Xevn-4B-MLX-8bit) |
| 6-bit | 3.4 GB | 68.2 | 75.8 | 82 ms | [MLX](https://huggingface.co/quevirus/Xevn-4B-MLX-6bit) |
| 5-bit | 2.9 GB | 68.4 | 75.6 | 80 ms | [MLX](https://huggingface.co/quevirus/Xevn-4B-MLX-5bit) |
| 4-bit | 2.4 GB | 67.0 | 75.4 | 78 ms | [MLX](https://huggingface.co/quevirus/Xevn-4B-MLX-4bit) |
| 3-bit | 1.8 GB | 55.3 | 65.7 | 77 ms | [MLX](https://huggingface.co/quevirus/Xevn-4B-MLX-3bit) |

16-bit is the bf16 format. Accuracy and Headline are the mean over the eight Korean benchmarks above. Speed is the p50 over an equal mix of the three input lengths, measured in the same session as the Speed table. 8-bit to 4-bit stay within 1.5 points of 16-bit. 3-bit loses substantial accuracy and is provided for experimentation.

PyTorch (Transformers) 16-bit weights: [Xevn-4B](https://huggingface.co/quevirus/Xevn-4B).

### By benchmark

<p align="center"><img src="assets/quant_en.svg" alt="Xevn by precision: accuracy" width="100%"></p>

**Accuracy (%)**

| Benchmark | 16-bit | 8-bit | 6-bit | 5-bit | 4-bit | 3-bit |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| KoBEST | 89.7 | 89.7 | 89.6 | 89.5 | 87.4 | 79.7 |
| KorMedMCQA | 69.4 | 69.1 | 69.6 | 68.5 | 66.4 | 50.8 |
| HAE-RAE | 58.3 | 58.3 | 56.5 | 57.5 | 56.3 | 40.2 |
| Belebele | 89.0 | 88.8 | 89.0 | 88.7 | 87.8 | 80.8 |
| KMMLU | 56.3 | 56.1 | 55.8 | 56.8 | 55.3 | 42.3 |
| CSAT-QA | 68.8 | 68.3 | 67.7 | 69.4 | 66.8 | 48.3 |
| CLIcK | 66.5 | 66.2 | 66.9 | 65.9 | 65.8 | 58.8 |
| KMMLU-1035 | 50.1 | 49.9 | 50.5 | 50.9 | 50.1 | 41.5 |

**Headline**

| Benchmark | 16-bit | 8-bit | 6-bit | 5-bit | 4-bit | 3-bit |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| KoBEST | 92.0 | 91.9 | 92.4 | 91.4 | 90.8 | 80.6 |
| KorMedMCQA | 78.7 | 78.7 | 79.0 | 77.8 | 75.5 | 65.9 |
| HAE-RAE | 70.2 | 69.9 | 68.9 | 68.2 | 68.1 | 56.9 |
| Belebele | 90.3 | 90.0 | 89.6 | 89.2 | 89.6 | 82.8 |
| KMMLU | 68.5 | 68.7 | 68.1 | 69.7 | 69.1 | 55.8 |
| CSAT-QA | 76.4 | 76.4 | 74.7 | 74.5 | 74.5 | 61.8 |
| CLIcK | 72.5 | 72.2 | 72.6 | 73.1 | 74.5 | 68.0 |
| KMMLU-1035 | 60.1 | 59.9 | 60.8 | 61.3 | 61.1 | 53.4 |

## Intended use

Xevn is built for decisions: classification, multiple choice, yes/no judgments, and rating. It is not a chat or text-generation model. It is tuned for Korean; English input works but is not the focus.

## License

[Apache 2.0](LICENSE). Built on [Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B).
