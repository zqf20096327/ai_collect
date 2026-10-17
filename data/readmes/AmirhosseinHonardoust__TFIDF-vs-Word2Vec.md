# TF-IDF vs Word2Vec: Understanding Text Vectorization in NLP

Natural Language Processing (NLP) is at the core of how machines understand human language.  
However, computers cannot process text directly, they need **numerical representations**.  
This article explains two of the most widely used vectorization methods in NLP:  
**TF-IDF (Term Frequency - Inverse Document Frequency)** and **Word2Vec**.

---

## Overview

Text vectorization transforms text data into numerical vectors, enabling machine learning models to process and analyze it.  
In this article, we’ll explore the fundamental concepts, formulas, differences, and practical Python implementations of TF-IDF and Word2Vec.  
You’ll also learn when to use each approach in real-world NLP projects.

---

## What Is TF-IDF?

TF-IDF is a statistical technique that measures how important a word is within a document relative to an entire corpus.  
It balances **term frequency (TF)**, how often a word appears in a document against **inverse document frequency (IDF)**, how rare it is across documents.

### Formula
\[
\text{TF-IDF}(w, d) = TF(w, d) \times \log\left(\frac{N}{DF(w)}\right)
\]

Where:
- **TF(w, d):** Frequency of word *w* in document *d*  
- **DF(w):** Number of documents containing *w*  
- **N:** Total number of documents

TF-IDF assigns **higher weights** to rare, informative words and **lower weights** to common words like “the” or “and”.

---

### Example in Python

```python
from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
    "I love data science and machine learning",
    "Deep learning is a part of machine learning",
    "Python is great for data analysis"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs)

print("Feature Names:", vectorizer.get_feature_names_out())
print("TF-IDF Matrix:\n", X.toarray())
```

**TF-IDF is great for:**  
- Simple text classification models  
- Keyword extraction  
- Search engines and ranking tasks  

---

## What Is Word2Vec?

Unlike TF-IDF, **Word2Vec** is a neural embedding model that learns **semantic meaning** of words.  
It represents words as dense vectors where **similar words** have **similar vector representations**.

Word2Vec uses shallow neural networks and two main architectures:
- **CBOW (Continuous Bag of Words):** Predicts a word based on its surrounding context.  
- **Skip-Gram:** Predicts context words based on a target word.

---

### Example in Python

```python
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize

docs = [
    "I love data science and machine learning",
    "Deep learning is a part of machine learning",
    "Python is great for data analysis"
]

tokenized_docs = [word_tokenize(doc.lower()) for doc in docs]

model = Word2Vec(sentences=tokenized_docs, vector_size=50, window=3, min_count=1, workers=4)
print("Vector for 'data':", model.wv["data"])
```

**Word2Vec is great for:**  
- Semantic similarity and clustering  
- Chatbots and recommendation systems  
- Context-aware applications  

---

## Key Differences

| Feature | TF-IDF | Word2Vec |
|----------|--------|----------|
| Type | Statistical | Neural embedding |
| Captures meaning | ❌ No | ✅ Yes |
| Handles synonyms | ❌ No | ✅ Yes |
| Output | Sparse vector | Dense vector |
| Model type | Non-trainable | Trainable |
| Ideal for | Traditional ML | Deep learning, semantic tasks |

---

## When to Use Which

**Use TF-IDF when:**
- You have limited data  
- You need interpretable features  
- You’re building simple ML models (SVM, Logistic Regression)

**Use Word2Vec when:**
- You have large text data  
- You want to capture contextual relationships  
- You’re building chatbots or deep NLP systems  

---

## Visualization Example

You can visualize Word2Vec embeddings using **t-SNE**:

```python
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

words = list(model.wv.index_to_key)
vectors = [model.wv[w] for w in words]

tsne = TSNE(n_components=2, random_state=42)
reduced = tsne.fit_transform(vectors)

plt.figure(figsize=(8,6))
plt.scatter(reduced[:,0], reduced[:,1])
for i, word in enumerate(words):
    plt.annotate(word, xy=(reduced[i,0], reduced[i,1]))
plt.title("Word2Vec Embeddings Visualization")
plt.show()
```

---

## Summary

| Aspect | TF-IDF | Word2Vec |
|--------|--------|----------|
| Speed | Faster | Slower |
| Accuracy (semantic) | Moderate | High |
| Interpretability | Easy | Harder |
| Use Case | Text analysis | Deep NLP, recommendation |
| Data requirement | Low | High |

> **In short:**  
> Start with TF-IDF for smaller tasks.  
> Switch to Word2Vec when context and meaning matter.

---

## Real-World Applications

- Sentiment analysis  
- Text classification  
- Document similarity  
- Recommendation engines  
- Search and information retrieval  
