<p align="center">
  <img src="assets/orbitlm_banner.webp" alt="OrbitLM" width="100%">
</p>

<p align="center">
  <a href="https://arxiv.org/abs/2610.00673"><img alt="arXiv: 2610.00673" src="https://img.shields.io/badge/arXiv-2610.00673-b31b1b"></a>
  <a href="https://huggingface.co/ai-forever/OrbitLM-1.8B-Thinking"><img alt="Hugging Face: OrbitLM-1.8B-Thinking" src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-OrbitLM--1.8B--Thinking-ffc107"></a>
  <a href="https://habr.com/ru/companies/sberbank/articles/1111372/"><img alt="Как сделать looped LLM: от архитектуры до обучения с подкреплением" src="https://img.shields.io/badge/Habr-article%20%28RU%29-65a3be?logo=habr&logoColor=white"></a>
  <a href="LICENSE"><img alt="Лицензия: Apache 2.0" src="https://img.shields.io/badge/license-Apache%202.0-2f6fde"></a>
  <img alt="Python 3.12+" src="https://img.shields.io/badge/python-3.12%2B-2f6fde">
</p>

<p align="center"><b>Русский</b> · <a href="README_en.md">English</a></p>

# OrbitLM-1.8B

OrbitLM-1.8B представляет собой зацикленную языковую модель. Она построена на архитектуре Ouro-1.4B
с токенизатором Qwen3: один стек из 24 слоёв трансформера (hidden_size 2048, 16 attn_heads)
прогоняется четыре раза на каждый токен, а после каждого прохода гейт выхода даёт токену
вероятность остановиться. В модели 1,86 млрд параметров: 1,23 млрд в слоях и 0,62 млрд в
несвязанных матрицах эмбеддингов и выхода.

Статья: [Closing the Loop: Practical Training Recipes for Looped Language Models](https://arxiv.org/abs/2610.00673).

В репозитории лежит полный пайплайн обучения модели с нуля и скрипты инференса с budget forcing,
FP8 KV-кэшем и спекулятивным декодированием. Пакеты называются `orbit` (трейнер) и `orbit_verl`
(дистилляция и RL), переменные окружения начинаются с `ORBIT_`. Команды запускаются из корня
репозитория.

## Веса модели

Обученная модель лежит на Hugging Face:
[ai-forever/OrbitLM-1.8B-Thinking](https://huggingface.co/ai-forever/OrbitLM-1.8B-Thinking). В её
карточке есть результаты на бенчмарках и примеры запуска в transformers и vLLM, в том числе с
self-speculative decoding. Код модели лежит вместе с весами, поэтому при загрузке нужен
`trust_remote_code=True`:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

repo = "ai-forever/OrbitLM-1.8B-Thinking"
tokenizer = AutoTokenizer.from_pretrained(repo, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    repo, dtype=torch.bfloat16, trust_remote_code=True, early_exit_threshold=None
).to("cuda")
# На некоторых связках CUDA ядро внимания cuDNN из PyTorch падает на длинных контекстах. Без него
# SDPA берёт ядро flash или memory-efficient, которое считает то же самое внимание.
torch.backends.cuda.enable_cudnn_sdp(False)

messages = [{"role": "user", "content": "Сколько будет 17 умножить на 23?"}]
prompt = "<|endoftext|>" + tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True, enable_thinking=True
)
inputs = tokenizer(prompt, return_tensors="pt", add_special_tokens=False).to(model.device)
output = model.generate(**inputs, max_new_tokens=8192)
print(tokenizer.decode(output[0, inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

Промпт начинается с `<|endoftext|>`, как при обучении. С `enable_thinking=False` модель отвечает
без рассуждения.

## Пайплайн

| # | Стадия | Конфиг | Старт | Рецепт |
|---|---|---|---|---|
| 1 | Претрейн 4K | `configs/train/pretrain/stage1_4k.yaml` | случайная инициализация | 100 000 шагов по 4,19 млн токенов, lr 3e-4, RoPE 4e4 |
| 2 | Претрейн 4K, продолжение | `configs/train/pretrain/stage2_4k.yaml` | стадия 1, шаг 100000 | 200 000 шагов, lr 1e-4 |
| 3 | Контекст 16K | `configs/train/pretrain/stage3_16k.yaml` | стадия 2, шаг 200000 | 47 684 шага (200 млрд токенов), RoPE 1e6, маскирование документов |
| 4 | Контекст 32K | `configs/train/pretrain/stage4_32k.yaml` | стадия 3, шаг 47684 | 4769 шагов (20 млрд токенов), RoPE 4e6 |
| 5 | SFT | `configs/train/sft/sft_v5.yaml` | стадия 4, шаг 4769 | 7000 шагов по 2,1 млн токенов, lr 1e-5 с косинусом до 1e-6 |
| 6 | RL | `configs/verl/rl_sft_mix.yaml` | стадия 5, шаг 7000 | плечо `mix` (математика и код), лосс на всех проходах с весами гейта выхода (`rltt_exit`), lr 1e-6, до 150 шагов |
| 7 | Инференс | `inference/` | любой чат-экспорт | vLLM, FP8 KV-кэш, спекулятивное декодирование, budget forcing |

Стадии с 1 по 5 выполняет трейнер (`src/orbit`), стадия 6 работает на verl 0.9.1 (`src/orbit_verl`).
Релизная модель получена на шаге 90 стадии 6. В коде есть и on-policy дистилляция, о ней в разделе RL.

## Установка

| Окружение | Откуда ставить | Для чего |
|---|---|---|
| Обучение | `requirements/train.txt` (torch 2.9, CUDA 12.8) | стадии с 1 по 5, экспорт, `inference/generate_hf.py` |
| Оценка | `requirements/eval.txt` (vLLM 0.22) | оценка, которую стадии 4 и 5 запускают во время обучения |
| verl | `requirements/verl/build_env.sh` (torch 2.11, CUDA 13, vLLM 0.26) | стадия 6, дистилляция, `inference/generate_vllm.py` |
| Данные | `requirements/data_prep.txt` | сборка данных |

```bash
python -m pip install -r requirements/train.txt --extra-index-url https://download.pytorch.org/whl/cu128
python -m pip install -e . --no-deps
bash requirements/verl/build_env.sh /path/to/envs/orbit-verl /path/to/flash_attn-2.8.3-<torch2.11-cu13-cp312>.whl
```

Каждое окружение, которое импортирует `orbit` или `orbit_verl`, ставится в репозиторий командой
`pip install -e . --no-deps`; в окружение verl это делает `build_env.sh`. Его второй аргумент: сборка
flash-attn 2.8.3, которую один раз собирают с nvcc, без неё RL и дистилляция не загрузят модель. vLLM в
окружении verl нужен версии 0.26: с ней запускались и проверялись RL и дистилляция. Для одного инференса
подойдёт и более новый vLLM. Модель Ouro из него убрали после 0.26, и её возвращает плагин `orbit_vllm`,
который ставится той же командой (проверено на vLLM 0.34). Окружение оценки настраивается один раз, как
показано в `eval/in_training/README.md`.

| Переменная | Что хранит |
|---|---|
| `ORBIT_RAW` | исходные данные и данные, которые вы готовите сами |
| `ORBIT_DATA` | токенизированные обучающие данные |
| `ORBIT_TOKENIZERS` | три подготовленных токенизатора |
| `ORBIT_RUNS` | прогоны трейнера и логи TensorBoard |
| `ORBIT_EXPORTS` | HF-экспорты между стадиями |
| `ORBIT_EVAL_PYTHON`, `ORBIT_LM_EVAL`, `ORBIT_EVAL_CACHE` | интерпретатор оценки, папка lm-eval и офлайн-кэш |
| `ORBIT_ATTN_KERNEL_PATH` | необязательная локальная сборка ядра FA3 |
| `ORBIT_VERL_RUNS` | подготовленные модели, датасеты и прогоны verl |
| `VERL_PYTHON` | python окружения verl |

## Данные

```bash
python data_prep/tokenizer/prepare_tokenizers.py --out-dir "$ORBIT_TOKENIZERS"
```

Затем нужно собрать данные каждой стадии, как описано в `docs/DATA.md`. Несколько входов готовятся
вручную: русский текст, русские чаты и математические задачи.

## Обучение: стадии с 1 по 5

```bash
scripts/train/run_local.sh configs/train/pretrain/stage1_4k.yaml        # все GPU одной машины
torchrun --nnodes N --node_rank R --nproc_per_node 8 --rdzv_endpoint HOST:PORT \
    -m orbit.train --config configs/train/pretrain/stage1_4k.yaml       # несколько машин
```

`$ORBIT_RUNS` должен лежать на общей для всех узлов файловой системе. Число GPU должно быть кратно 64,
иначе шаги станут больше и номеров шагов из таблицы ниже не будет; релиз обучался на 64 GPU на
стадиях с 1 по 4 и на 32 GPU на стадии 5. Перезапущенный прогон продолжает с `latest.txt`. Стадии 4
и 5 запускают оценку во время обучения, поэтому сначала настройте её.

Последний чекпоинт каждой стадии экспортируется на CPU. Экспорту SFT нужен `--chat-export`.

```bash
python -m orbit.export $ORBIT_RUNS/orbit_stage1_4k $ORBIT_EXPORTS/stage1_4k_step100000 \
    --model-config src/orbit/ouro_1.4b_qwen3_config.json --tokenizer $ORBIT_TOKENIZERS/tokenizer_qwen3_orbit
```

| Стадия | Шаг экспорта | Имя | Токенизатор |
|---|---|---|---|
| 1 | 100000 | `stage1_4k_step100000` | `tokenizer_qwen3_orbit` |
| 2 | 200000 | `stage2_4k_step200000` | `tokenizer_qwen3_orbit` |
| 3 | 47684 | `stage3_16k_step47684` | `tokenizer_qwen3_orbit` |
| 4 | 4769 | `stage4_32k_step4769` | `tokenizer_qwen3_orbit` |
| 5 | 7000 | `sft_v5_step7000` | `tokenizer_qwen3_4b_qwen35_tools`, с `--chat-export` |

Подробнее о трейнере в `src/orbit/README.md`.

## RL: стадия 6

```bash
RECIPE_TAG=lr1e6_fp8tis_rlttexit bash scripts/verl/run_rl.sh mix \
    --export $ORBIT_EXPORTS/sft_v5_step7000 --model-name sft_v5_step7000 --data /path/to/verl_data -- \
    actor_rollout_ref.actor.policy_loss.loss_mode=rltt_exit trainer.total_training_steps=150
$VERL_PYTHON scripts/verl/watch.py $ORBIT_VERL_RUNS/runs/rl_mix__lr1e6_fp8tis_rlttexit --rl --val-dir /path/to/verl_data --follow 600
$VERL_PYTHON scripts/verl/export_hf_fp32.py --ckpt $ORBIT_VERL_RUNS/runs/rl_mix__lr1e6_fp8tis_rlttexit/ckpt/global_step_90/actor \
    --base-export $ORBIT_EXPORTS/sft_v5_step7000 --out $ORBIT_EXPORTS/orbitlm_1.8b
```

Прогон идёт на плече `mix` на одном узле с 8 GPU, лосс на всех проходах с весами гейта выхода
(`rltt_exit`), не больше 150 шагов. Релизная модель взята с шага 90 по валидационным метрикам, более
поздние шаги лучше не были. RL может развалиться ближе к концу прогона, поэтому держите вотчер
запущенным. На GPU с 80 ГБ добавьте `--gpu-mem 0.7` перед `--`. Плечи `math`, `code` и `mix_ru`
остаются вариантами, которые релизная модель не использовала.

В `--data` лежат пул промптов, gold-строки математики и кода и валидационные наборы, которые
собираются по `scripts/verl/data/README.md`. Награда за код запускает программы в песочнице, которой
нужен Linux на x86_64 с user namespaces, Landlock и seccomp. На нескольких узлах сначала один раз
запустите скрипт с `--prepare-only`, потом с `--no-prepare` на каждом узле с заданными `RANK`,
`WORLD_SIZE` и `MASTER_ADDR`; подробности в `docs/verl/README.md`.

В коде есть и on-policy дистилляция из Qwen3-8B (`configs/verl/distill_rl_sft_16k.yaml`,
`scripts/verl/run_distill.sh`), и она тоже неплохо работает. Она идёт на одном узле с 8 GPU: шесть
обучают студента, две отведены под учителя. RL может стартовать с её экспорта в fp32 вместо экспорта
SFT. Команды в `docs/verl/README.md`.

## Инференс

```bash
$VERL_PYTHON inference/generate_vllm.py $MODEL --prompts prompts.jsonl --output answers.jsonl \
    --speculative --budget-forcing --think-budget 14336 --answer-budget 2048
```

FP8 KV-кэш включён по умолчанию и вмещает в 2,1 раза больше токенов, чем bf16. `--speculative`
предлагает четыре черновых токена за один проход модели; вместе с FP8-кэшем декодирование идёт
от 1,7 до 2,2 раза быстрее, чем bf16 без спекуляции.
`--budget-forcing` закрывает рассуждение после `--think-budget` токенов, для русских промптов
по-русски. Остальное в `inference/README.md`.

## Тесты

```bash
python -m pytest -q tests/train data_prep tests/inference                           # обучение + dev.txt + data_prep.txt
CUDA_VISIBLE_DEVICES= $VERL_PYTHON -m pytest -q tests/verl tests/inference          # окружение verl
```

Короткие проверки на GPU: конфиги на одну GPU в `configs/train/smoke/` и
`bash scripts/verl/smoke.sh rl|distill`.

## Цитирование

```bibtex
@article{marchenko2026closing,
  title   = {Closing the Loop: Practical Training Recipes for Looped Language Models},
  author  = {Marchenko, Andrei and Bezrukov, Viacheslav and Kashurin, Oleg and Fedorova, Inessa and Bocharov, Dmitry and Shakhvalieva, Yuliana and Tikhonova, Maria and Ternovskii, Valerii},
  journal = {arXiv preprint arXiv:2610.00673},
  year    = {2026}
}
```

## Лицензия

Apache License 2.0 (`LICENSE`). Файлы со своим уведомлением об авторских правах сохраняют его.
