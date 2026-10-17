<div align="center">

# 🕸️ Solving 14 Common RAG Failures with Knowledge Graphs

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-🦜️🔗-green?style=for-the-badge)](https://langchain.com)
[![NetworkX](https://img.shields.io/badge/NetworkX-Graph-red?style=for-the-badge)](https://networkx.org)
[![TinyLlama](https://img.shields.io/badge/Model-TinyLlama-purple?style=for-the-badge)](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)

**A practical cookbook demonstrating why Vector Search fails at reasoning and how Graph RAG solves it.**

[📖 Read the Full Blog Post on Medium](https://medium.com/@fareedkhandev/solving-14-common-rag-failures-through-knowledge-graphs-7125a8837a17)

</div>

---

## 🧐 The Problem
Standard RAG (Retrieval Augmented Generation) relies on **Vector Similarity**. It retrieves documents based on how semantically close words are. While powerful, it struggles with:
- **Reasoning:** Connecting dot A to dot C via dot B.
- **Structure:** Understanding hierarchy, sequence, and direction.
- **Negation:** Finding what is *missing*.

## 💡 The Solution: Graph RAG
This repository contains **14 Python Notebooks** that simulate specific edge cases where standard RAG fails. Each notebook implements a **Knowledge Graph (NetworkX)** solution to demonstrate how structured data and graph traversal can solve these complex reasoning problems.

---

## 📂 The 14 Failure Modes

| # | Failure Mode | The Vector Trap ❌ | The Graph Solution ✅ |
|:-:|:---|:---|:---|
| **01** | [**Multi-Hop Reasoning**](./01_multi_hop.ipynb) | Retrieves disjointed facts (A->B, B->C) but fails to connect A to C. | **Graph Traversal:** Walks the edges `(A)-[connected_to]->(B)-[connected_to]->(C)` to return the full path. |
| **02** | [**Causal Synthesis**](./02_cascual_synthesis.ipynb) | Sees positive sentiment ("Safe", "Eco-friendly") and ignores hidden chemical conflicts. | **Rule Checking:** Maps properties (`Oxidizer`, `Flammable`) and runs strict compatibility logic. |
| **03** | [**Entity Ambiguity**](./03_entity_ambiguity.ipynb) | Confuses "Jaguar" (Car) with "Jaguar" (Animal) due to keyword overlap. | **Entity Resolution:** Creates distinct nodes `Jaguar(Company)` and `Jaguar(Animal)` and filters by intent. |
| **04** | [**Contradictory Facts**](./04_entity_ambiguity.ipynb) | Retrieves old (2021) and new (2024) policies equally, confusing the LLM. | **Temporal Graphs:** Edges have `timestamp` metadata. The logic sorts by date to find the *latest* truth. |
| **05** | [**Implicit Hallucination**](./05_implicit_hallucination.ipynb) | Assumes a relationship exists because two entities appear in the same paragraph. | **Edge Verification:** If no explicit edge `(A)-[PARTNERS_WITH]->(B)` exists, the answer is "No". |
| **06** | [**Aggregation (Counting)**](./06_aggregation.ipynb) | Fails to count items scattered across multiple documents (or double counts synonyms). | **Node Aggregation:** Normalizes entities to IDs and runs `len(graph.neighbors(node))` for exact counts. |
| **07** | [**Scattered Evidence**](./07_scattered_evidence.ipynb) | Misses details because `top_k=3` cuts off documents containing the 4th, 5th, and 6th features. | **Neighborhood Search:** Retrieves the central node and *all* connected attribute nodes, regardless of document count. |
| **08** | [**Structural Hierarchy**](./08_hierarchy.ipynb) | Loses context of parent systems when retrieving leaf nodes (The "Russian Doll" effect). | **Recursive Traversal:** Traces the lineage `(Leaf)->(Parent)->(Root)` to provide full context. |
| **09** | [**Directionality**](./09_directionality.ipynb) | Confuses "A owns B" with "B owns A" because vector space is symmetric. | **Directed Edges:** Strictly defines `(Parent)-[OWNS]->(Child)`. The arrow direction is immutable. |
| **10** | [**Intersection (Common Neighbors)**](./10_intersection.ipynb) | Sees explicit mentions but misses implicit connections (e.g., Drug Interaction via common protein). | **Intersection Query:** Finds common neighbors between Node A and Node B to detect hidden risks. |
| **11** | [**Negation & Absence**](./11_negation.ipynb) | Struggles to find "What is safe?" because it retrieves documents mentioning the danger. | **Set Difference:** Calculates `All_Products - Unsafe_Products` to mathematically prove safety. |
| **12** | [**Synonymy & Jargon**](./12_synonymy.ipynb) | Fails to link "Project X" logs to "Billing Service" queries. | **Ontology Mapping:** Maps technical IDs to business concepts (`ID` --[IMPLEMENTS]--> `Concept`). |
| **13** | [**Centrality & Influence**](./13_centrality.ipynb) | Biases towards job titles (VP, CEO) rather than actual communication flow. | **Graph Topology:** Uses `Betweenness Centrality` algorithms to mathematically identify influencers/bottlenecks. |
| **14** | [**Temporal Sequence**](./14_temporal_sequence.ipynb) | Scrambles cause and effect because documents are ranked by relevance, not time. | **Linked Lists:** Creates a causal chain `(Event A)-[NEXT]->(Event B)` and strictly follows the sequence. |

---

## 🚀 Getting Started

### Prerequisites
This project uses **TinyLlama-1.1B** (via HuggingFace) to ensure the code runs efficiently on most machines (including Google Colab free tier) without needing massive GPUs.

### Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/FareedKhan-dev/14-rag-failures.git
   cd 14-rag-failures
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install langchain langchain-community langchain-huggingface faiss-cpu networkx transformers sentence-transformers accelerate bitsandbytes dateparser
   ```

### Running the Notebooks
You can run any notebook directly. Each notebook is self-contained:
1. It simulates a dataset.
2. It runs a **Naive RAG** (Vector Search) to show the failure.
3. It runs a **Knowledge Graph** approach to show the solution.

```bash
# Example: Run the Multi-Hop reasoning demo
jupyter notebook 01_multi_hop.ipynb
```

---

## 🛠️ Tech Stack

*   **LLM:** `TinyLlama/TinyLlama-1.1B-Chat-v1.0` (Local inference via HuggingFacePipeline)
*   **Orchestration:** `LangChain`
*   **Vector Store:** `FAISS` (Facebook AI Similarity Search)
*   **Graph Store:** `NetworkX` (In-memory Python graph library)
*   **Embeddings:** `sentence-transformers/all-MiniLM-L6-v2`

---

## 🤝 Contributing

Contributions are welcome! If you find a 15th failure mode or want to improve the graph extraction prompts:
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<div align="center">

**[🌟 Star this repo if you found it useful!]**

Created by [Fareed Khan](https://github.com/FareedKhan-dev)

</div>