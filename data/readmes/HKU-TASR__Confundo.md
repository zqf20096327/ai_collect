# **Confundo: Learning to Generate Robust Poison for Practical RAG Systems**

![](assets/overview.png)
**Abstract**: Retrieval-augmented generation (RAG) is increasingly deployed in real-world applications, where its reference-grounded design makes outputs appear trustworthy. This trust has spurred research on poisoning attacks that craft malicious content, inject it into knowledge sources, and manipulate RAG responses. However, when evaluated in practical RAG systems, existing attacks suffer from severely degraded effectiveness. This gap stems from two overlooked realities: (i) content is often processed before use, which can fragment the poison and weaken its effect, and (ii) users often do not issue the exact queries anticipated during attack design. These factors can lead practitioners to underestimate risks and develop a false sense of security. To better characterize the threat to practical systems, we present Confundo, a learning-to-poison framework that fine-tunes a large language model as a poison generator to achieve high effectiveness, robustness, and stealthiness. Confundo provides a unified framework supporting multiple attack objectives, demonstrated by manipulating factual correctness, inducing biased opinions, and triggering hallucinations. By addressing these overlooked challenges, Confundo consistently outperforms a wide range of purpose-built attacks across datasets and RAG configurations by large margins, even in the presence of defenses. Beyond exposing vulnerabilities, we also present a defensive use case that protects web content from unauthorized incorporation into RAG systems via scraping, with no impact on user experience.

---
For more technical details and experimental results, we invite you to check out our paper [[here]](https://arxiv.org/abs/2602.06616):  
**Haoyang Hu, Zhejun Jiang, Yueming Lyu, Junyuan Zhang, Yi Liu and Ka-Ho Chow,** *"Confundo: Learning to Generate Robust Poison for Practical RAG Systems,"* USENIX Security Symposium, Baltimore, MD, USA, Aug. 12-14, 2026.

```
@inproceedings{hu2026confundo,
  title={Confundo: Learning to Generate Robust Poison for Practical RAG Systems},
  author={Hu, Haoyang and Jiang, Zhejun and Lyu, Yueming and Zhang, Junyuan and Liu, Yi and Chow, Ka-Ho},
  booktitle={35th USENIX Security Symposium (USENIX Security 26)},
  year={2026}
}
```
---
## 🚀 Quick Start

🛠️ **Clone this repository and install the required dependencies:**

```
git clone https://github.com/HKU-TASR/Confundo.git
cd Confundo
pip install -r requirements.txt
```

⚔️ Poisoning for Multiple Attack Objectives

Confundo provides a unified framework capable of supporting multiple adversarial objectives. We provide interactive notebooks for rapid deployment, along with pre-configured attack demonstrations across three core objectives:

* **Factual Correctness Manipulation**: Manipulate RAG systems to produce incorrect responses.

  👉 Run the interactive demo: [`./factual_correctness_manipulation.ipynb`](./factual_correctness_manipulation.ipynb)

* **Opinion Manipulation**: Manipulate RAG systems to generate responses with subjective bias.

  👉 Run the interactive demo: [`./opinion_manipulation.ipynb`](./opinion_manipulation.ipynb)

* **Hallucination Induction**: Induce hallucinations in RAG systems.

  👉 Run the interactive demo: [`./hallucination_induction.ipynb`](./hallucination_induction.ipynb)

**🤗 We open-sourced our fine-tuned poison generators on HuggingFace: [confundo-correctness](https://huggingface.co/AlienHu/confundo-correctness), [confundo-opinion](https://huggingface.co/AlienHu/confundo-opinion), [confundo-hallucination](https://huggingface.co/AlienHu/confundo-hallucination).**

---

## 🔄 Cross-Pipeline Transferability

As our default RAG pipeline is built with LangChain, you can also evaluate the effectiveness of Confundo across other popular RAG frameworks:

- **LlamaIndex Pipeline Evaluation:**
  ```
  python ./generalization/pipeline/llamaindex.py
  ```

- **Haystack Pipeline Evaluation:**
  
  ```
  python ./generalization/pipeline/haystack.py
  ```
  
---

## 🛡️ Survivability Under Defenses

Evaluate the resilience of generated poison against various defensive mechanisms.

### Heuristic Filtering

Assess how well the adversarial content bypasses automated document preprocessing and statistical filters:

- **Perplexity Filtering:**
  ```
  python ./defenses/filter/filtering_perplexity.py
  ```

- **Duplicate-Text Filtering:**
  ```
  python ./defenses/filter/filtering_duplicate.py
  ```

- **Keyword Density Filtering:**
  ```
  python ./defenses/filter/filtering_keyword.py
  ```

### LLM-Based Intent Detection

Evaluate survival rates when commercial LLM judges act as intent monitors to detect adversarial content injection:
```
python ./defenses/intent.py
```

### Reranking

Analyze performance degradation when a reranking model alters the position and priority of poisoned entries:

```
python ./defenses/rerank.py
```

### Paraphrasing

Measure robustness when queries or retrieved documents undergo rewriting across three levels:

- **Level I — Paraphrase Question:** Rewrite user queries.
  ```
  python ./defenses/paraphrase/paraphrase-1.py
  ```

- **Level II — Paraphrase Retrieved Entry:** Rewrite retrieved documents.
  ```
  python ./defenses/paraphrase/paraphrase-2.py
  ```
- **Level III — Paraphrase Both Question and Entry:** Rewrite both queries and retrieved documents.
  ```
  python ./defenses/paraphrase/paraphrase-3.py
  ```
  
---

## 🥷 Lexical Generalization

Confundo can maintain good performance even if the user paraphrases the target query:

**👉 Run the interactive demo:** [`./generalization/lexical_generalization.ipynb`](./generalization/lexical_generalization.ipynb)

---

## 🏋️ Training the Poison Generator

### 1. Data Preparation

To fine-tune the generator, you must first prepare target answers and semantic variants. You can generate these customized assets using our notebook or bootstrap directly from our pre-packaged examples:

- **Target Answer Generation:** Generate incorrect target responses using the interactive notebook `./tools/gen.ipynb`, or use our ready-made example at: `./examples/input_harry_potter.json`.

- **Paraphrased Variant Generation:** Synthesize diverse query and entry variations via `./tools/gen.ipynb`, or directly load our optimization dataset from: `./train/RL_train_harry_potter.json`.

### 2. Fine-Tuning

* **Factual Correctness Manipulation**
```
python ./train/train_correctness.py
```

* **Opinion Manipulation**
```
python ./train/train_opinion.py
```

* **Hallucination Induction**
```
python ./train/train_hallucination.py
```

> 💡 **Note on Computation Time & Hardware:** A full training run typically requires a GPU with at least 48GB VRAM and takes 10+ hours, depending on your hardware configuration. Training parameters or configurations may require adjustment based on your experimental environment (e.g., hardware or package versions). For a rapid preview, we also provide a simplified training pipeline at `./train/train_sim.py`. 

---

📬 If you encounter any issues, feel free to contact: haoyanghu@connect.hku.hk.
