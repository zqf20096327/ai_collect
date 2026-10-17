<div align="center">
  <h1>ReT-2: Recurrence Meets Transformers for <br>Universal Multimodal Retrieval </h1>
</div>

<div align="center">
  
  [![Paper](https://img.shields.io/badge/Paper-arxiv.2509.08897-B31B1B.svg)](https://arxiv.org/abs/2509.08897)
  [![ReT-2](https://img.shields.io/badge/Checkpoints-🤗%20ReT--2-blue)](https://huggingface.co/collections/aimagelab/ret-2-68b5b0aec72c48fa72ff4290)
  [![Dataset](https://img.shields.io/badge/Dataset-🤗%20ReT--M2KR-blue)](https://huggingface.co/datasets/aimagelab/ReT-M2KR)


</div>

<p align="center">
  <img src="assets/ret2.png" alt="ReT2" width="840" />
</p> 


## Table of Contents

1. [Installation](#installation)
2. [Usage](#use-with-s-transformers)
3. [Evaluation - M2KR](#m2kr)
4. [Evaluation - M-BEIR](#m-beir)
5. [Evaluation - RAG VQA](#rag-vqa)
6. [Citation](#citation)


## Installation
1. Create the Python environment.
```
conda create -n ret2 -y --no-default-packages python==3.10.16
conda activate ret2
```
2. Install Pytorch.
```
pip install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cu118
```
3. Install faiss.
```
conda install -n ret2 -y -c conda-forge faiss-gpu==1.7.4
```
4. Clone the repo and install other dependencies.
```
git clone https://github.com/aimagelab/ReT-2.git
cd ReT-2
pip install -r requirements.txt
```

## Use with 🤗's Transformers
```python
from src.models import Ret2Model
import requests
from PIL import Image
from io import BytesIO
import torch
import torch.nn.functional as F

device = 'cuda' if torch.cuda.is_available() else 'cpu'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

query_img_url = 'https://upload.wikimedia.org/wikipedia/commons/8/84/Ghirlandina_%28Modena%29.jpg'
response = requests.get(query_img_url, headers=headers)
query_image = Image.open(BytesIO(response.content)).convert('RGB')
query_text = 'Where is this building located?'

passage_img_url = 'https://upload.wikimedia.org/wikipedia/commons/0/09/Absidi_e_Ghirlandina.jpg'
response = requests.get(query_img_url, headers=headers)
passage_image = Image.open(BytesIO(response.content)).convert('RGB')
passage_text = (
    "The Ghirlandina is the bell tower of the Cathedral of Modena, in Modena, Italy. "
    "It is 86.12 metres (282.7 ft) high and is the symbol of the city. "
    "It was built in Romanesque style in the 12th century and is part of a UNESCO World Heritage Site."
)

model = Ret2Model.from_pretrained('aimagelab/ReT2-M2KR-ColBERT-SigLIP2-ViT-L', device_map=device)

query_txt_inputs = model.tokenizer([query_text], return_tensors='pt').to(device)
query_img_inputs = model.image_processor([query_image], return_tensors='pt').to(device)
passage_txt_inputs = model.tokenizer([passage_text], return_tensors='pt').to(device)
passage_img_inputs = model.image_processor([passage_image], return_tensors='pt').to(device)

with torch.inference_mode():
    query_feats = model.get_ret_features(
        input_ids=query_txt_inputs.input_ids,
        attention_mask=query_txt_inputs.attention_mask,
        pixel_values=query_img_inputs.pixel_values
    )

    passage_feats = model.get_ret_features(
        input_ids=passage_txt_inputs.input_ids,
        attention_mask=passage_txt_inputs.attention_mask,
        pixel_values=passage_img_inputs.pixel_values
    )

    sim = F.normalize(query_feats, p=2, dim=-1) @ F.normalize(passage_feats, p=2, dim=-1).T

print(f"query-passage similarity: {sim.item():.3f}")
```

## Evaluation
The core script to reproduce the results shown in the paper is [evaluate.py](src/evaluate.py). The evaluation is split into three stages:
1. `index`: typically the longest stage, extracts embeddings from multimodal passages and saves them to file system.
2. `create_index`: reads embeddings and index them as a `faiss.IndexFlatIP` for efficient inner-product similarity search. This stage outputs two files: **(1)** `knn.index`, that is the actual Faiss index; **(2)** `knn.json`, that is a JSON list of 2-uple, where the first item is the (unique) passage ID (*i.e.* `pid`), and the second item is the textual content associated with that passages.
3. `search`: queries the index and computes metrics. The output is: **(1)** `metrics.json`, a JSON dict containing the retrieval metrics; **(2)** `metrics.txt`, containing the metrics written in Markdown for pretty-printing; **(3)** `ranking.tsv`, a .tsv file where each row has 4 fields: 
    - `qid`: a unique identifier of a query.
    - `pidx`: the 0-index value of the retrieved passage in the JSONL file used to create the index in stage 1.
    - `rank`: the rank of the retrived passage. Note that the top-1 retrieved passage has rank equal to 0. 
    - `score`: the query-passage cosine similarity.

Both the multimodal passages to be indexed and the multimodal queries are supposed to be in JSONL format. To index and search through custom data collections, please refer to our Hugging Face's dataset for examples on how to prepare your data for [indexing](https://huggingface.co/datasets/aimagelab/ReT-M2KR/tree/main/jsonl/m2kr/passages) and [search](https://huggingface.co/datasets/aimagelab/ReT-M2KR/tree/main/jsonl/m2kr/test).

Our experiments have been run on the [Leonardo](https://www.hpc.cineca.it/systems/hardware/leonardo/) HPC cluster, which features [SLURM](https://slurm.schedmd.com/documentation.html) as the resource manager. Inside the [scripts](scripts) folder, we provide SLURM sbatch scripts to reproduce the paper results. As the `index` stage can last very long, depending on the amount of passages to be indexed, [evaluate.py](src/evaluate.py) does support single-node multi-GPU acceleration to speed up the process. Conversely, the `search` stage currently only works with a single GPU.

### M2KR
To reproduce the results on the **LLaVA**, **KVQA**, **OVEN**, and **IGLUE** tasks of M2KR, run [eval_m2kr_single_gpu.sh](scripts/eval_m2kr_single_gpu.sh). <br>
For **OKVQA**, **InfoSeek**, **E-VQA**, and **WIT**, run [eval_m2kr_multi_gpu.sh](scripts/eval_m2kr_multi_gpu.sh). <br>
Before running either script, you have to set two variables:
1. `IMAGE_ROOT_PATH`: the path where [M2KR images](https://huggingface.co/datasets/aimagelab/ReT-M2KR#download-images) have been downloaded.
2. `JSONL_ROOT_PATH` the path where [JSONL annotations](https://huggingface.co/datasets/aimagelab/ReT-M2KR/tree/main/jsonl) have been downloaded.

### M-BEIR
To reproduce the results on M-BEIR, run [eval_mbeir_multi_gpu.sh](scripts/eval_mbeir_multi_gpu.sh). Similarly to M2KR, you have to set
1. `IMAGE_ROOT_PATH`: the path where M-BEIR images have been downloaded. Please refer to the [official repository](https://huggingface.co/datasets/TIGER-Lab/M-BEIR#downloading-the-m-beir-dataset) to download them.
2. `JSONL_ROOT_PATH` the path where [JSONL annotations](https://huggingface.co/datasets/aimagelab/ReT-M2KR/tree/main/jsonl) have been downloaded.

### RAG VQA
For the best VQA performance, we recommend using ReT-2 paired with [ColBERT + SigLIP2](https://huggingface.co/aimagelab/ReT2-M2KR-ColBERT-SigLIP2-ViT-L) as the retrieval engine. <br>
The first step is to index the Wikipedia knowledge base (KB) and retrieve the top-k passages for each visual question. This step is built on the same [evaluate.py](src/evaluate.py) script used for M2KR and M-BEIR, but you have to set some additional variables according to the chosen VQA benchmark: either [InfoSeek](#infoseek) or [Encyclopedic-VQA (E-VQA)](#encyclopedic-vqa).

Next is the answer generation stage, where the generator is a Multimodal Large Language Model (MLLM), whose prompt for each question is enriched with the top-k retrieved passages from the previous stage.

#### InfoSeek
##### Retrieval
Modify [infoseek_index_and_search.sh](scripts/rag/infoseek/infoseek_index_and_search.sh) as follows:
- `dataset_path_index`: a JSONL file containing the multimodal passages of your KB. For InfoSeek, this is a collection of 1M (image)-text pairs from Wikipedia pages. You can download it from [here](https://huggingface.co/datasets/aimagelab/ReT-M2KR/blob/main/jsonl/rag/kb_infoseek1M.jsonl).<br>**Note**: we also release a smaller KB of [525k passages](https://huggingface.co/datasets/aimagelab/ReT-M2KR/blob/main/jsonl/rag/kb_infoseek525k.jsonl), that is the KB used in our previous work, [ReT](https://www.arxiv.org/abs/2503.01980).
- `image_root_index`: the path to which image paths in `dataset_path_index` are relative to. InfoSeek shares the same KB as OVEN, and the images can be downloaded as a tarfile from [here](https://huggingface.co/datasets/ychenNLP/oven/blob/main/all_wikipedia_images.tar
).
- `dataset_path_query`: a JSONL file containing the retrieval queries. You can download it from [here](https://huggingface.co/datasets/aimagelab/ReT-M2KR/blob/main/jsonl/rag/infoseek_val.jsonl).
- `image_root_query`: the path to which image paths in `dataset_path_query` are relative to. The images can be downloaded by following the official OVEN [guidelines](https://github.com/edchengg/oven_eval/tree/main/image_downloads#oven-images).

This script outputs `ranking.jsonl`, which is similar to the [ranking.tsv](#evaluation) file produced after searching throug an index, with the addition of the textual content associated to each retrieved passage.

##### Generation
Run [infoseek_rag_llava_more.sh](scripts/rag/infoseek/infoseek_rag_llava_more.sh) to generate answers with [LLaVA-MORE-8B](https://github.com/aimagelab/LLaVA-MORE), or [infoseek_rag_qwen.sh](scripts/rag/infoseek/infoseek_rag_qwen.sh) to generate with [Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct). In either case, modify the scripts as follows:
- `dataset_path_query`: same as [above](#retrieval).
- `image_root_query`: same as [above](#retrieval).
- `ranking_path`: path to the `ranking.jsonl` file generatedy by [infoseek_index_and_search.sh](scripts/rag/infoseek/infoseek_index_and_search.sh).
- `output_path`: the JSONL file that stores the answer to each visual question.

To compute the evaluation metrics, run the following:
```
python src/rag/metrics/infoseek_compute_metrics.py \
--prediction_paths /path/to/my_predictions.jsonl \
--experiment_names my_experiment \
--reference_path infoseek_val.jsonl \
--reference_qtype_path infoseek_val_qtype.jsonl
```
where `infoseek_val.jsonl` and `infoseek_val_qtype.jsonl` can be downloaded from the official InfoSeek [repository](https://github.com/edchengg/infoseek_eval/tree/main/infoseek#infoseek-annotations).


#### Encyclopedic-VQA
##### Retrieval
Modify [evqa_index_and_search.sh](scripts/rag/evqa/evqa_index_and_search.sh) as follows:
- `dataset_path_index`: a JSONL file containing the multimodal passages of your KB. For E-VQA, this is a collection of 15.9M (image)-text pairs from Wikipedia pages. Indexing can take a lot, depending on the capability of your GPUs. You can download it from [here](https://huggingface.co/datasets/aimagelab/ReT-M2KR/blob/main/jsonl/rag/kb_evqa15M.jsonl).
- `image_root_index`: the path to which image paths in `dataset_path_index` are relative to. Images for E-VQA KB have been sampled from WikiWeb2M and can be downloaded accordingly to the official E-VQA [repository](https://github.com/google-research/google-research/tree/master/encyclopedic_vqa#controlled-knowledge-base). Because E-VQA uses only a subset of 2.4M images from the original 11M, we have packed them as tarfiles for convenience. You can download them from [here](https://huggingface.co/datasets/aimagelab/ReT-M2KR#download-images).
- `dataset_path_query`: a JSONL file containing the retrieval queries. You can download it from [here](https://huggingface.co/datasets/aimagelab/ReT-M2KR/blob/main/jsonl/rag/evqa_test.jsonl).
- `image_root_query`: the path to which image paths in `dataset_path_query` are relative to. According to the official E-VQA [repository](https://github.com/google-research/google-research/tree/master/encyclopedic_vqa#vqa-questions), query images come from two datasets: *iNaturalist 2021* and *Google Landmarks Dataset v2*. After downloading them, your `image_root_query` should look like this:
```
.
└── image_root_query/
    ├── iNaturalist/
    │   ├── train/
    │   │   ├── 03248_Animalia_Chordata_Aves_Anseriformes_Anatidae_Dendrocygna_viduata/
    │   │   │   ├── 90af92cc-254a-43c9-90bd-cb894fc8613e.jpg
    │   │   │   ├── 2f2a2358-3429-492c-a90e-63d59dc2dfe3.jpg
    │   │   │   ├── fbbbe163-5e0f-4b90-a948-33373aff2e24.jpg
    │   │   │   └── ...
    │   │   └── ...
    │   ├── val
    │   └── test
    └── Google_Landmarks_v2/
        ├── 0/
        │   ├── 0/
        │   │   ├── 0/
        │   │   │   ├── 0000059611c7d079.jpg
        │   │   │   ├── 0000070506c174cc.jpg
        │   │   │   ├── 000008ae30de967e.jpg
        │   │   │   └── ...
        │   │   ├── 1
        │   │   ├── 2
        │   │   └── ...
        │   └── ...
        └── ...
```

##### Generation
Run [evqa_rag_llava_more.sh](scripts/rag/evqa/evqa_rag_llava_more.sh) to generate answers with [LLaVA-MORE-8B](https://github.com/aimagelab/LLaVA-MORE), or [evqa_rag_qwen.sh](scripts/rag/evqa/evqa_rag_qwen.sh) to generate with [Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct). In either case, modify the scripts as follows:
- `dataset_path_query`: same as [above](#retrieval-1).
- `image_root_query`: same as [above](#retrieval-1).
- `ranking_path`: path to the `ranking.jsonl` file generatedy by [evqa_index_and_search.sh](scripts/rag/evqa/evqa_index_and_search.sh).
- `output_path`: the JSONL file that stores the answer to each visual question.

In E-VQA, the [evaluation metric](https://github.com/google-research/google-research/tree/master/encyclopedic_vqa#evaluation) is the accuracy, where an answer is deemed as correct if its BEM score with the reference is greater than 0.5. To compute it, run the following:
```
python src/rag/metrics/evqa_compute_metrics.py --input_path /path/to/my_predictions.jsonl
```
#### Known issue
[evqa_compute_metrics.py](src/rag/metrics/evqa_compute_metrics.py) requires tensorflow to run. The offical python dependencies can be found [here](https://github.com/google-research/google-research/blob/master/encyclopedic_vqa/requirements.txt). Unfortunately, we did not succeed in installing tensorflow in our environment due to some conflicts, so you may require a dedicated environment for that.

## Citation
If you happen to use our works, please cite them with the following BibTeX:
```
@inproceedings{caffagni2025recurrence,
  title={{Recurrence-Enhanced Vision-and-Language Transformers for Robust Multimodal Document Retrieval}},
  author={Caffagni, Davide and Sarto, Sara and Cornia, Marcella and Baraldi, Lorenzo and Cucchiara, Rita},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  year={2025}
}
```
```
@article{caffagni2025recurrencemeetstransformers,
      title={{Recurrence Meets Transformers for Universal Multimodal Retrieval}}, 
      author={Davide Caffagni and Sara Sarto and Marcella Cornia and Lorenzo Baraldi and Rita Cucchiara},
      journal={arXiv preprint arXiv:2509.08897},
      year={2025}
}
```