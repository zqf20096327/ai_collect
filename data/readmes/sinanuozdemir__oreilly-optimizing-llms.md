![oreilly-logo](images/oreilly.png)

# Optimizing LLMs with Fine-Tuning and Prompt Engineering


This repository contains code for the [O'Reilly Live Online Training for Optimizing LLMs with Fine-Tuning and Prompt Engineering](https://www.oreilly.com/live-events/optimizing-llms-with-fine-tuning-and-prompt-engineering/0642572011351)

<p align="center">
  <a href="https://www.amazon.com/Quick-Start-Guide-Language-Models-dp-0135346568/dp/0135346568">Check out my book</a> for even more examples and fleshed out case studies. The code for the book is free forever on my Github
</p>

<p align="center" href="https://www.amazon.com/Quick-Start-Guide-Language-Models-dp-0135346568/dp/0135346568">
  <img src="images/qsllm2e.jpg" href="https://www.amazon.com/Quick-Start-Guide-Language-Models-dp-0135346568/dp/0135346568" alt="Quick Start Guide to Large Language Models" width="200">
</p>

This advanced course is designed for machine learning engineers and software developers looking to elevate the performance and precision of large language models (LLMs). This course focuses on two critical aspects of LLM optimization: fine-tuning models on specific datasets to tailor their capabilities and mastering the craft of prompt engineering to generate accurate and contextually relevant outputs.

Over the course of this training, you will explore the intricacies of fine-tuning LLMs like GPT, learning how to adapt pre-trained models to specific tasks and use cases. Additionally, you will delve into the nuances of prompt engineering, discovering how to design and refine prompts that effectively guide LLM behavior. By the end of the course, you will have a deep understanding of how to maximize the potential of LLMs, making them more responsive and valuable in a variety of applications. This course is essential for anyone aiming to push the boundaries of what LLMs can achieve in real-world scenarios.

### Notebooks

#### Comparing Fine-tuned OpenAI + BERT

  - [`bert_app_review.ipynb`](https://colab.research.google.com/drive/1z2sMZ_A05_VGYqpHBgabvcV0V4INYhQ4#scrollTo=QQAdv6RBNees): Fine-tuning a BERT model for app review classification.
  - [`openai_app_review_fine_tuning.ipynb`](notebooks/openai_app_review_fine_tuning.ipynb): Fine-tuning OpenAI models for app review classification.

#### Fine-tuning embeddings

- [Fine-tuning Embeddings For Rec Engines](https://colab.research.google.com/drive/1JfxyxdGCDjYeO52Bk1JzW4Af94xndTws?usp=sharing): Fine-tuning embedding engines using custom preference data

- [Fine-tuning Embeddings  with Synthetic Data](https://colab.research.google.com/drive/1FOr9hgMEcTa8UJJSuKjoHpohVb-Qz-FJ?usp=sharing) - Using GPT-4o to create synthetic queries for a corpus to increase the quality of open-source embedding models

#### Working with FLAN-T5 models using Reinforcement Learning
  - Colab Version: [![Using SAWYER](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1wG8lv6drn872HNZHrT7V9kl6JIF1SXpr?usp=sharing)

#### Domain Adaptation - Fine-tune Qwen on domain-specific documents
  - Colab: [Google Colab](https://colab.research.google.com/drive/1eZzTJ5dNtbeh2RZS-kV7DD7jDHFqS4qG#scrollTo=yqxqAZ7KJ4oL)

#### Matryoshka Embeddings - Train embeddings that work at multiple dimensions.
  - Colab: [Google Colab](https://colab.research.google.com/drive/1N9ROhCmrOTnXMkpIc9SukVeSwFr5Xxkx#scrollTo=UbG2yyJxv_JW)


#### SAWYER - Training a chat model with RLF

  - [`SAWYER_LLAMA_SFT.ipynb`](notebooks/SAWYER_LLAMA_SFT.ipynb): Fine-tuning the Llama-3 model to create the SAWYER bot.
    - [colab version](https://colab.research.google.com/drive/1gN7jsUFQTPAj5uFrq06HcSLQSZzT7hZz?usp=sharing) 
  - [`SAWYER_Reward_Model.ipynb`](notebooks/SAWYER_Reward_Model.ipynb): Training a reward model from human preferences for the SAWYER bot.
    - [colab version](https://colab.research.google.com/drive/1bVjTzOjXCOM8J6tzgt3LK-D0K-yGWzyI?usp=sharing) 
  - [`SAWYER_RLF.ipynb`](notebooks/SAWYER_RLF.ipynb): Applying Reinforcement Learning from Human Feedback (RLHF) to align the SAWYER bot.
    - [colab version](https://colab.research.google.com/drive/1QR_Xf1GsOyChYzReg_JHxsBTrMZ0Vwz6?usp=sharing) 
  - [`SAWYER_USE_SAWYER.ipynb`](notebooks/SAWYER_USE_SAWYER.ipynb): Using the SAWYER bot.
    - [colab version](https://colab.research.google.com/drive/1xUrIbqyKoEjxNyjNI6iuYuSNMyksypEO?usp=sharing)
  - [Adapting SAWYER to know more about ML](https://colab.research.google.com/drive/12JeS96SVLIyY06bzJs96B5PdTt1Pga06?usp=sharing)

#### Distillation + Quantization

  - [`distillation_example_1.ipynb`](notebooks/distillation_example_1.ipynb): Exploring knowledge distillation techniques for transformer models.
  - [`distillation_example_2.ipynb`](notebooks/distillation_example_2.ipynb): Advanced distillation methods and applications.
  - [`llama_quantization.ipynb`](notebooks/llama_quantization.ipynb): Quantizing Llama models for efficient deployment.
  - [`Llama.cpp`](https://colab.research.google.com/drive/1D6k-BeuF8YRTR8BGi2YYJrSOAZ6cYX8Y?usp=sharing) - Using LLMs with llama.cpp


## Instructor

<div style="text-align: center;">
  <img src="images/square_headshot_small.jpg" alt="Headshot" width="300">
</div>

**Sinan Ozdemir** is the Founder and CTO of UseCrucible.ai where he uses State of the art AI to help people create custom AI models. Sinan is a former lecturer of Data Science at Johns Hopkins University and the author of multiple textbooks on data science and machine learning. Additionally, he is the founder of the recently acquired Kylie.ai, an enterprise-grade conversational AI platform with RPA capabilities. He holds a master’s degree in Pure Mathematics from Johns Hopkins University and is based in San Francisco, CA.

