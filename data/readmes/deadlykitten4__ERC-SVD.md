<div align="center">
      <h2><b> ERC-SVD: Error-Controlled SVD for Large Language Model Compression </b></h2>
</div>

<div align="center">

</div>

<div align="center">

**Haolei Bai<sup>1,2</sup>, Siyong Jian<sup>1,4</sup>, Tuo Liang<sup>3</sup>, Yu Yin<sup>3</sup>, Huan Wang<sup>1,*</sup>**  

*<sup>1</sup>Westlake University, <sup>2</sup>Nanyang Technological University, <sup>3</sup>Case Western Reserve University, <sup>4</sup>Nanjing University*


[![arXiv](https://img.shields.io/badge/arXiv-2602.11715-b31b1b.svg)](https://arxiv.org/abs/2505.20112)

[//]: # ([![GitHub Repo stars]&#40;https://img.shields.io/github/stars/deadlykitten4/ERC-SVD?style=social&#41;]&#40;https://github.com/deadlykitten4/ERC-SVD&#41;)

</div>

<!-- LOGO -->
<div align="center" style="margin-top: 20px;">
  <img src="image/img.png" height="150" alt="Westlake University Logo" style="margin-right: 20px; display: inline-block;">
</div>

##  🚀 Usage
### 1. Install dependencies
```bash
conda create -n erc-svd python=3.10
conda activate erc-svd
pip install -r requirements.txt
```

### 2. Perform SVD compression

```bash
# loss analysis (compression ratio=20% for example)
python ERC-SVD_compression.py --model /yout/path/to/llama-2-7b-hf/ --step 0 --ratio 0.2 --whitening_nsamples 256 --dataset wikitext2 --seed 3 --model_seq_len 2048 --layer_num 16

python ERC-SVD_compression.py --model /yout/path/to/llama-2-7b-hf/ --step 1 --ratio 0.2 --whitening_nsamples 256 --dataset wikitext2 --seed 3 --model_seq_len 2048 --layer_num 16 --save_path /your/save/path/
```

### 3. Evaluation
#### 3.1 Perplexity
```bash
python ERC-SVD_compression.py --step 2 --model_path /your/path/to/compressed_model.pt
```

#### 3.2 Zero-shot accuracy
```bash
python evaluation_zero_acc.py --model_id /your/path/to/compressed_model.pt --pt_flag
```

## 🙌 Acknowledgement

We are grateful to the [ASVD](https://github.com/hahnyuan/ASVD4LLM?tab=readme-ov-file) and [SVD-LLM](https://github.com/AIoT-MLSys-Lab/SVD-LLM) for releasing their code publicly, which greatly facilitated our work. 


## 📖 Citation

If you find **ERC-SVD** useful for your research or projects, please consider citing our work:

```bibtex
@inproceedings{bai2026ercsvd,
  title={ERC-SVD: Error-Controlled SVD for Large Language Model Compression},
  author={Bai, Haolei and Jian, Siyong and Liang, Tuo and Yin, Yu and Wang, Huan},
  booktitle={CPAL},
  year={2026}
}
@article{bai2025ressvd,
  title={Ressvd: Residual compensated svd for large language model compression},
  author={Bai, Haolei and Jian, Siyong and Liang, Tuo and Yin, Yu and Wang, Huan},
  journal={arXiv preprint arXiv:2505.20112},
  year={2025}
}
```