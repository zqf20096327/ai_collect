<p align="center">
    <img alt="Transformers Explained" src="https://github.com/amitshekhariitbhu/transformers-explained/blob/main/assets/banner.png">
</p>

# Transformers Explained

**Transformer architecture explained step by step - the full architecture, every attention variant, positional embeddings, and every layer inside a Transformer.**

---

Prepared and maintained by the **Founder** of Outcome School: [Amit Shekhar](https://x.com/amitiitbhu)

---

**Note: This series will continue to grow as I write more blogs and create more videos on new topics. Keep learning.**

---

# Part 1: The Architecture

We start with the complete picture - every component of the Transformer and how data flows through it. The rest of this guide then zooms into each piece.

---

## Decoding Transformer Architecture

In this blog, we will learn about the Transformer architecture by decoding it piece by piece - understanding what each component does, how they work together, and why this architecture powers every modern Large Language Model (LLM).

We will cover the following:

* Why the Transformer was needed
* The two halves of the architecture
* Tokenization, Embedding, and Positional Encoding
* The Attention Mechanism and Multi-Head Attention
* Feed-Forward Networks, Residual Connections, and Layer Normalization
* How the Encoder and Decoder work
* How data flows through the entire architecture
* The three variants of the Transformer
* Why the Transformer is so powerful

Let's get started: [Decoding Transformer Architecture](https://outcomeschool.com/blog/decoding-transformer-architecture)

---

# Part 2: Attention

Attention is the heart of the Transformer. In this part, we go from the intuition to the exact math, and then through every attention variant used in modern models.

---

## Self Attention in Transformers

In this blog, we will learn about Self Attention in Transformers. We will understand what it is, how it works step by step, and why it is the heart of modern Large Language Models like BERT and GPT.

We will cover the following:

* What is Self Attention?
* Why do we need Self Attention?
* Query, Key, and Value vectors
* Step-by-step working of Self Attention
* A simple example walk-through
* Why Self Attention works so well
* Multi-Head Self Attention
* Where Self Attention is used

Let's get started: [Self Attention in Transformers](https://outcomeschool.com/blog/self-attention-in-transformers)

---

## Math behind Attention - Q, K, and V

In this blog, we will learn about the math behind Attention - Query(Q), Key(K), and Value(V) with a step-by-step numeric example.

We will cover the following:

* The Attention Formula
* Setting Up: From Words to Vectors
* Creating Q, K, and V Matrices
* Computing Attention Scores (Q x K^T)
* Scaling the Scores
* Applying Softmax
* Computing the Final Output (Attention Weights x V)
* Putting It All Together

Let's get started: [Math behind Attention - Q, K, and V](https://outcomeschool.com/blog/math-behind-attention-qkv)

---

## Math behind √dₖ Scaling Factor in Attention

In this blog, we will learn about why we scale the dot product attention by √dₖ in the Transformer architecture with a step-by-step numeric example.

We will cover the following:

* The Attention Formula (Quick Recap)
* What Happens Without Scaling?
* Why Do Dot Products Grow with dₖ?
* Understanding Variance of the Dot Product
* Proving It Step by Step: Variance of the Dot Product is dₖ
* What Large Dot Products Do to Softmax
* Why √dₖ is the Right Scaling Factor
* Seeing It with Real Numbers
* Putting It All Together

Let's get started: [Math behind √dₖ Scaling Factor in Attention](https://outcomeschool.com/blog/scaling-dot-product-attention)

---

## Multi-Head Attention in Transformers

In this blog, we will learn about Multi-Head Attention in Transformers. We will understand what it is, how it works step by step, and why it gives Transformers their power to understand language so well.

We will cover the following:

* What is Multi-Head Attention?
* A quick recap of Self Attention
* Why do we need Multi-Head Attention?
* Step-by-step working of Multi-Head Attention
* A simple example walk-through
* Where Multi-Head Attention is used
* Advantages of Multi-Head Attention

Let's get started: [Multi-Head Attention in Transformers](https://outcomeschool.com/blog/multi-head-attention-in-transformers)

---

## Cross Attention in Transformers

In this blog, we will learn about Cross Attention in Transformers. We will understand what it is, how it works step by step, how it is different from Self Attention, and where it is used.

We will cover the following:

* What is Cross Attention?
* Why do we need Cross Attention?
* Query, Key, and Value in Cross Attention
* Self Attention vs Cross Attention
* Step-by-step working of Cross Attention
* A simple example walk-through
* Where Cross Attention is used
* Importance of Cross Attention

Let's get started: [Cross Attention in Transformers](https://outcomeschool.com/blog/cross-attention-in-transformers)

---

## Causal Masking in Attention

In this blog, we will learn about causal masking in attention.

We will start with the introduction of causal masking, understand the problem of seeing future tokens through an example, and then walk through its implementation to see how masked attention prevents the model from accessing future tokens.

We will cover the following:

* Without Causal Masking
* With Causal Masking
* Implementation of Causal Masking
* The Causal Mask Matrix

Let's get started: [Causal Masking in Attention](https://outcomeschool.com/blog/causal-masking-in-attention)

---

## Grouped Query Attention

In this blog, we will learn about Grouped-Query Attention (GQA) and how it differs from Multi-Head Attention (MHA). We will also learn about Multi-Query Attention (MQA) along the way and see when to use which one.

We will cover the following:

* The Big Picture
* Quick Recap: Multi-Head Attention (MHA)
* The Problem with Multi-Head Attention
* What is Multi-Query Attention (MQA)?
* What is Grouped-Query Attention (GQA)?
* How Grouped-Query Attention Works
* GQA is a Generalization of MHA and MQA
* GQA vs MHA vs MQA
* Real-World Use Cases
* A Note on Terminology
* Uptraining: Converting MHA to GQA
* Quick Summary

Let's get started: [Grouped Query Attention](https://outcomeschool.com/blog/grouped-query-attention)

---

## Decoding Flash Attention in LLMs

In this blog, we will learn about Flash Attention by decoding it piece by piece - understanding why standard attention is slow, what makes Flash Attention fast, how it uses GPU memory cleverly, and why it is used in almost every modern Large Language Model (LLM).

We will cover the following:

* A quick recap of standard attention
* Why standard attention is slow
* How GPU memory actually works (HBM vs SRAM)
* The core idea behind Flash Attention
* Tiling: breaking the work into small blocks
* Online softmax: computing softmax without the full matrix
* Recomputation in the backward pass
* Flash Attention 2
* Flash Attention 3
* Advantages and impact of Flash Attention

Let's get started: [Decoding Flash Attention in LLMs](https://outcomeschool.com/blog/decoding-flash-attention)

---

# Part 3: Position

Attention by itself has no sense of order - it treats a sentence like a bag of tokens. Positional embeddings are how the Transformer knows which token came first.

---

## Positional Embeddings in LLMs

In this article, we will learn about Positional Embeddings in LLMs - how the Transformer gets the position information of every token in the sequence.

Let's get started: [Positional Embeddings in LLMs](https://outcomeschool.substack.com/p/positional-embeddings-in-llms)

---

## Math Behind RoPE (Rotary Position Embedding)

In this blog, we will learn about the math behind Rotary Position Embedding (RoPE) and why it is used in modern Large Language Models.

We will cover the following:

* The Big Picture
* Why a Transformer Needs Position Information
* Older Approaches and Their Problems
* The Core Idea Behind RoPE
* The 2D Rotation Math
* How RoPE Is Applied to Q and K
* Why the Dot Product Captures Relative Position
* A Small Numeric Example
* Real-World Use Cases
* Quick Summary

Let's get started: [Math Behind RoPE (Rotary Position Embedding)](https://outcomeschool.com/blog/math-behind-rope-rotary-position-embedding)

---

# Part 4: The Other Layers

Attention gets the fame, but a Transformer block is more than attention. The feed-forward network holds most of the parameters, and normalization keeps the whole thing trainable.

---

## Feed-Forward Networks in LLMs

In this blog, we will learn about Feed-Forward Networks in LLMs - understanding what they are, how they work inside the Transformer architecture, why every Transformer layer needs one, and what role they play in making Large Language Models so powerful.

We will cover the following:

* What is a Feed-Forward Network?
* Understanding Feed-Forward Networks with a Real-World Analogy
* Where Does the Feed-Forward Network Sit in a Transformer?
* How Does a Feed-Forward Network Work - Step by Step
* The Expand-then-Contract Pattern
* Why Does the FFN Expand and Then Contract?
* ReLU and Activation Functions
* What Does the Feed-Forward Network Actually Learn?
* How Much of the Model is the Feed-Forward Network?
* Feed-Forward Networks in Mixture of Experts
* Why Feed-Forward Networks Are So Important

Let's get started: [Feed-Forward Networks in LLMs](https://outcomeschool.com/blog/feed-forward-networks-in-llms)

---

## Batch Normalization vs Layer Normalization

In this blog, we are going to learn about Batch Normalization vs Layer Normalization. We will also see how Batch Normalization and Layer Normalization differ from each other and when to use which one.

We will cover the following:

* What is Normalization?
* Why do we need Normalization?
* What is Batch Normalization?
* What is Layer Normalization?
* Batch Normalization vs Layer Normalization
* When to use which one?

Let's get started: [Batch Normalization vs Layer Normalization](https://outcomeschool.com/blog/batch-normalization-vs-layer-normalization)

---

## RMSNorm (Root Mean Square Layer Normalization)

In this blog, we will learn about RMSNorm, a faster and simpler alternative to Layer Normalization that powers most modern Large Language Models like Llama, Mistral, Gemma, Qwen, PaLM, and DeepSeek.

We will cover the following:

* Why normalization is needed in deep networks
* A quick recap of Layer Normalization (LayerNorm)
* What RMSNorm is and how it works
* The math behind RMSNorm with a concrete numeric example
* LayerNorm vs RMSNorm - the key differences
* Why modern LLMs prefer RMSNorm
* A code example
* Where RMSNorm fits in a Transformer
* Quick Summary

Let's get started: [RMSNorm (Root Mean Square Layer Normalization)](https://outcomeschool.com/blog/rmsnorm-root-mean-square-layer-normalization)

---

# Part 5: Variants

The same core architecture stretches far beyond plain text models. Here are two variants you will meet everywhere: sparse expert models and Transformers for images.

---

## Mixture of Experts Explained

In this blog, we will learn about the Mixture of Experts (MoE) architecture - understanding what experts are, how the router picks them, why MoE makes large models faster and cheaper, and why it powers many of today's most powerful Large Language Models (LLMs).

We will cover the following:

* Why Mixture of Experts was needed
* What an "expert" really means
* The router and how it picks experts
* Where MoE sits inside a Transformer
* Sparse activation and why it saves compute
* Load balancing across experts
* Advantages and challenges of MoE
* Why MoE powers many modern LLMs

Let's get started: [Mixture of Experts Explained](https://outcomeschool.com/blog/mixture-of-experts)

---

## Decoding Vision Transformer (ViT)

In this blog, we will learn about the Vision Transformer (ViT) by decoding how it splits an image into patches, turns those patches into tokens, and processes them with a transformer to classify the image.

We will cover the following:

* The Big Picture
* Decoding Step 1: Splitting the Image into Patches
* Decoding Step 2: Patch Embedding
* Decoding Step 3: The CLS Token
* Decoding Step 4: Position Embeddings
* Decoding Step 5: The Transformer Encoder
* Decoding Step 6: The Classification Head
* Putting It All Together
* ViT vs CNN
* Quick Summary

Let's get started: [Decoding Vision Transformer (ViT)](https://outcomeschool.com/blog/decoding-vision-transformer-vit)

---

## More blogs and videos coming soon!

### License
```
   Copyright (C) 2026 Outcome School

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```
