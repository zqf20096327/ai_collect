# news-summarization-id

Indonesian news summarization: headline + 2-3 sentence paragraph summary.
Fine-tunes IndoBART (or `google/mt5-small`) on IndoNLG / Liputan6.

## Install

```bash
pip install -r requirements.txt
```

## Data

```bash
python prepare_data.py --dataset liputan6 --out data/
# or
python prepare_data.py --dataset indosum --out data/
```

Sources: [IndoNLG](https://github.com/IndoNLP/indonlg) · [Liputan6](https://huggingface.co/datasets/id_liputan6) · [IndoSum](https://github.com/kata-ai/indosum).

## Train

```bash
python train.py \
  --model indobenchmark/indobart-v2 \
  --data  data/ \
  --epochs 4 \
  --bs 8 \
  --lr 3e-5 \
  --out ckpt/
```

Models: [indobart-v2](https://huggingface.co/indobenchmark/indobart-v2) · [mt5-small](https://huggingface.co/google/mt5-small).

## Eval

```bash
python eval.py --ckpt ckpt/ --data data/ --split test
```

Outputs ROUGE-1 / ROUGE-2 / ROUGE-L.

## Infer

```bash
python infer.py --ckpt ckpt/ --text "Jakarta — Presiden hari ini ..."
# both modes:
python infer.py --ckpt ckpt/ --text "..." --mode headline
python infer.py --ckpt ckpt/ --text "..." --mode summary
```

## Why ROCm

IndoBART-v2 fine-tune fits on a single MI210 in fp16; the IndoNLG paragraph
summary task at seq-len 512→128 needs ~24 GB activation memory at batch 16.
ROCm 6.x + PyTorch wheel covers everything in `requirements.txt` (transformers,
datasets, evaluate, sentencepiece) — no CUDA-only ops. MI300 cuts our epoch
time roughly in half versus the consumer card we currently rent.

## License

MIT.
