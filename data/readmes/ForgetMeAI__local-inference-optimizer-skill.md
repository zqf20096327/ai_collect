<p align="center">
  <img src="https://img.shields.io/badge/Hermes%20Skill-local--inference--optimizer-7c3aed?style=for-the-badge" alt="Hermes Skill" />
  <img src="https://img.shields.io/badge/LLM-Inference-0ea5e9?style=for-the-badge" alt="LLM Inference" />
  <img src="https://img.shields.io/badge/License-MIT-10b981?style=for-the-badge" alt="MIT" />
</p>

# Local Inference Optimizer Skill

**Источник идеи:** [Ahmad Osman's LLM inference engine decision guide](https://x.com/TheAhmadOsman/status/2057183854444843202)

**Языки:** [🇷🇺 Русский — основная документация](#-русский) · [🇬🇧 English](#-english) · [🇨🇳 中文](#-中文)

---

## 🇷🇺 Русский

**Local Inference Optimizer** — skill для Hermes / Claude Code / Codex-агентов, который помогает агенту не гадать, а реально подобрать и настроить LLM inference stack под железо, модель и сценарий.

Агент должен:

- определить железо: Apple Silicon, NVIDIA CUDA, AMD ROCm, Intel, CPU-only;
- выбрать inference engine: MLX, llama.cpp, ExLlama, vLLM, SGLang, TensorRT-LLM, OpenVINO/ONNX Runtime;
- создать проект через `uv` + `.venv`;
- подобрать kernels, quantization, context, batching, KV cache, prefix cache, tensor parallel;
- запустить сервер и проверить его через health check + OpenAI-compatible smoke test.

### Быстрая установка в Hermes

```bash
curl -fsSL https://raw.githubusercontent.com/ForgetMeAI/local-inference-optimizer-skill/main/install.sh | bash
```

Затем в новой сессии:

```bash
hermes -s local-inference-optimizer
```

или внутри Hermes-чата:

```text
/skill local-inference-optimizer
```

### Ручная установка

```bash
git clone https://github.com/ForgetMeAI/local-inference-optimizer-skill.git
cd local-inference-optimizer-skill
./install.sh
```

### Использование с Claude Code / Codex

```bash
./scripts/export-agent-instructions.sh
```

Скрипт создаст:

- `AGENTS.md` — для Codex-style агентов;
- `CLAUDE.md` — для Claude Code.

Или просто скопируйте `SKILL.md` в project instructions.

### Готовый prompt

```text
Используй local-inference-optimizer skill.
Определи лучший inference engine под моё железо, настрой проект через uv + venv, подбери kernels/quantization, подкрути flags, batching, KV cache и оптимизируй запуск под мою модель и машину.

Модель: <HF repo или локальный путь>
Цель: <локальный чат / OpenAI API / production / long context / throughput / latency>
```

### Карта выбора engine

| Железо / сценарий | Стартовый engine |
|---|---|
| MacBook / Mac Studio | MLX, fallback llama.cpp |
| Laptop / edge / GGUF / странное железо | llama.cpp |
| Один consumer RTX | ExLlamaV2 или llama.cpp/vLLM |
| 2–4 NVIDIA GPU | ExLlamaV3, vLLM или SGLang |
| Production OpenAI-compatible API | vLLM |
| Long context / MoE / structured output | SGLang |
| NVIDIA H100/B200 max performance | TensorRT-LLM benchmark path |
| AMD ROCm | vLLM или SGLang |
| Intel CPU/GPU | OpenVINO или ONNX Runtime GenAI |

### Структура репозитория

```text
.
├── SKILL.md                         # основной Hermes skill
├── install.sh                       # установка в ~/.hermes/skills/mlops/
├── scripts/
│   ├── validate-skill.py            # проверка skill-файла
│   └── export-agent-instructions.sh # генерация AGENTS.md + CLAUDE.md
├── templates/
│   ├── AGENTS.md
│   └── CLAUDE.md
└── README.md
```

### Проверка

```bash
python3 scripts/validate-skill.py
```

Ожидаемый результат:

```text
OK local-inference-optimizer skill is valid
```

---

## 🇬🇧 English

**Local Inference Optimizer** is a skill for Hermes / Claude Code / Codex-style agents. It helps the agent inspect real hardware, choose the right LLM inference engine, create a `uv` + `.venv` project, tune runtime flags, and verify the server with a real smoke test.

### Install

```bash
curl -fsSL https://raw.githubusercontent.com/ForgetMeAI/local-inference-optimizer-skill/main/install.sh | bash
hermes -s local-inference-optimizer
```

### Use with Claude Code / Codex

```bash
./scripts/export-agent-instructions.sh
```

This generates `AGENTS.md` and `CLAUDE.md` from `SKILL.md`.

### Prompt

```text
Use the local-inference-optimizer skill.
Determine the best inference engine for my hardware, set up the project with uv + venv, choose kernels/quantization, tune flags, batching, KV cache, and optimize launch for my model and machine.

Model: <HF repo or local path>
Goal: <local chat / OpenAI API / production / long context / throughput / latency>
```

### Engine map

- Apple Silicon: MLX first, llama.cpp fallback.
- GGUF / edge / unusual hardware: llama.cpp.
- Single consumer RTX: ExLlamaV2 or llama.cpp/vLLM.
- Multi-GPU NVIDIA: ExLlamaV3, vLLM, or SGLang.
- Production API: vLLM.
- Long context / MoE / structured output: SGLang.
- NVIDIA datacenter max performance: TensorRT-LLM benchmark path.

---

## 🇨🇳 中文

**Local Inference Optimizer** 是一个适用于 Hermes / Claude Code / Codex 类代理的 skill。它让代理先检查真实硬件，再选择合适的 LLM 推理引擎，创建 `uv` + `.venv` 项目，调整 kernels、量化、batching、KV cache，并通过真实 smoke test 验证服务。

### 安装

```bash
curl -fsSL https://raw.githubusercontent.com/ForgetMeAI/local-inference-optimizer-skill/main/install.sh | bash
hermes -s local-inference-optimizer
```

### 用于 Claude Code / Codex

```bash
./scripts/export-agent-instructions.sh
```

该脚本会根据 `SKILL.md` 生成 `AGENTS.md` 和 `CLAUDE.md`。

### Prompt 示例

```text
Use the local-inference-optimizer skill.
Determine the best inference engine for my hardware, set up the project with uv + venv, choose kernels/quantization, tune flags, batching, KV cache, and optimize launch for my model and machine.

Model: <HF repo or local path>
Goal: <local chat / OpenAI API / production / long context / throughput / latency>
```

### 引擎选择速览

- Apple Silicon：优先 MLX，备用 llama.cpp。
- GGUF / 边缘设备 / 特殊硬件：llama.cpp。
- 单张消费级 RTX：ExLlamaV2 或 llama.cpp/vLLM。
- 多张 NVIDIA GPU：ExLlamaV3、vLLM 或 SGLang。
- 生产级 OpenAI-compatible API：vLLM。
- 长上下文 / MoE / 结构化输出：SGLang。
- NVIDIA 数据中心极致性能：TensorRT-LLM benchmark path。

---

## License

MIT. Use it, fork it, improve it.
