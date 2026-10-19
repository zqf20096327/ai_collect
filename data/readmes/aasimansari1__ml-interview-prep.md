<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a0a2e,100:003366&height=200&section=header&text=ML%20%2F%20AI%20Interview%20Prep&fontSize=48&fontColor=00D9FF&animation=fadeIn&fontAlignY=38&desc=500%2B%20Questions%20%E2%80%A2%20Cheat%20Sheets%20%E2%80%A2%20Code%20Snippets%20%E2%80%A2%20System%20Design&descAlignY=60&descColor=BD00FF&descSize=16" width="100%"/>

[![Stars](https://img.shields.io/github/stars/aasimansari1/ml-interview-prep?style=for-the-badge&color=FFD700&labelColor=0D1117&logo=github)](https://github.com/aasimansari1/ml-interview-prep/stargazers)
[![Forks](https://img.shields.io/github/forks/aasimansari1/ml-interview-prep?style=for-the-badge&color=00D9FF&labelColor=0D1117&logo=github)](https://github.com/aasimansari1/ml-interview-prep/network)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-BD00FF?style=for-the-badge&labelColor=0D1117)](https://github.com/aasimansari1/ml-interview-prep/pulls)
[![License: MIT](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge&labelColor=0D1117)](LICENSE)

**The most complete, interview-focused ML/AI reference on GitHub.**

*Cracking interviews at Google DeepMind, OpenAI, Meta AI, Amazon, Microsoft.*

</div>

---

## 📌 What's Inside

| Section | Content |
|---|---|
| 🧠 [ML Fundamentals](#-ml-fundamentals) | Bias-variance, overfitting, regularization, loss functions |
| 🔢 [Math & Statistics](#-math--statistics) | Linear algebra, probability, calculus for ML |
| 🤖 [Deep Learning](#-deep-learning) | CNNs, RNNs, transformers, attention, training tricks |
| 🗣️ [NLP](#️-nlp) | BERT, GPT, RAG, embeddings, tokenization |
| 👁️ [Computer Vision](#️-computer-vision) | YOLO, ResNet, image augmentation, segmentation |
| 🏗️ [ML System Design](#️-ml-system-design) | Recommendation systems, search, fraud detection |
| 🐍 [Python & Libraries](#-python--libraries) | NumPy, Pandas, scikit-learn, PyTorch one-liners |
| 🧩 [Coding Patterns](#-coding-patterns) | Data preprocessing, model eval, cross-validation |
| 💼 [Behavioral](#-behavioral) | STAR answers, research discussion, project walkthrough |

---

## 🧠 ML Fundamentals

<details>
<summary><strong>Q: Explain the bias-variance tradeoff.</strong></summary>

**Bias** = error from wrong assumptions (underfitting — model too simple).
**Variance** = error from sensitivity to training data fluctuations (overfitting — model too complex).

```
Total Error = Bias² + Variance + Irreducible Noise
```

| | High Bias | High Variance |
|---|---|---|
| Training error | High | Low |
| Test error | High | High |
| Fix | More features, complex model | Regularization, more data, dropout |

**Interview tip:** Draw the U-shaped test error curve. Explain that the goal is to find the sweet spot.
</details>

<details>
<summary><strong>Q: What is regularization? Compare L1 vs L2.</strong></summary>

Regularization adds a penalty to the loss function to prevent overfitting.

| | L1 (Lasso) | L2 (Ridge) |
|---|---|---|
| Penalty | λΣ\|wᵢ\| | λΣwᵢ² |
| Effect | Produces sparse weights (zeros out features) | Shrinks weights toward zero, keeps all |
| Use when | Feature selection needed | All features relevant |
| Gradient | Sign(w) | 2w |

```python
from sklearn.linear_model import Lasso, Ridge

lasso = Lasso(alpha=0.1)   # L1
ridge = Ridge(alpha=1.0)   # L2
```
</details>

<details>
<summary><strong>Q: How do you handle imbalanced datasets?</strong></summary>

**Resampling:**
```python
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler

# Oversample minority class
X_res, y_res = SMOTE().fit_resample(X, y)

# Undersample majority class
X_res, y_res = RandomUnderSampler().fit_resample(X, y)
```

**Class weights:**
```python
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(class_weight='balanced')
```

**Metrics:** Avoid accuracy. Use:
- Precision, Recall, F1-score
- ROC-AUC
- PR-AUC (better for severe imbalance)
</details>

<details>
<summary><strong>Q: Explain cross-validation. Why use k-fold?</strong></summary>

K-fold CV splits data into k subsets. Train on k-1, test on 1. Repeat k times. Average the scores.

```python
from sklearn.model_selection import cross_val_score, StratifiedKFold

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=cv, scoring='f1')
print(f"F1: {scores.mean():.3f} ± {scores.std():.3f}")
```

**Why k-fold?** Reduces variance in evaluation vs a single train/test split. Stratified k-fold preserves class distribution in each fold.
</details>

<details>
<summary><strong>Q: What is gradient descent? Compare SGD, Mini-batch, Adam.</strong></summary>

Gradient descent minimizes loss by updating parameters in the direction of steepest descent:

```
θ = θ - α · ∇L(θ)
```

| | Batch GD | SGD | Mini-batch |
|---|---|---|---|
| Update per | Full dataset | 1 sample | Batch (32-256) |
| Speed | Slow | Fast | Fast |
| Noise | Low | High | Medium |
| Memory | High | Low | Medium |

**Adam** (Adaptive Moment Estimation) — most popular optimizer:
```python
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3, betas=(0.9, 0.999))
```
Adam combines momentum + RMSProp. Adapts learning rate per parameter.
</details>

---

## 🔢 Math & Statistics

<details>
<summary><strong>Q: What is the dot product and why does it matter in ML?</strong></summary>

```
a · b = Σ aᵢbᵢ = |a||b|cos(θ)
```

In ML: measures similarity (cosine similarity in embeddings), is the core of every linear layer:
```python
output = X @ W.T + b  # Matrix multiplication = stacked dot products
```
</details>

<details>
<summary><strong>Q: Explain PCA intuitively and mathematically.</strong></summary>

PCA finds directions (principal components) of maximum variance in data.

**Steps:**
1. Center data: `X_centered = X - mean(X)`
2. Compute covariance matrix: `C = (X_centered.T @ X_centered) / (n-1)`
3. Eigendecompose: `C = V Λ Vᵀ`
4. Project: `X_pca = X_centered @ V[:, :k]`

```python
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)
print(f"Variance explained: {pca.explained_variance_ratio_.sum():.2%}")
```
</details>

<details>
<summary><strong>Q: What is the difference between MLE and MAP?</strong></summary>

**MLE (Maximum Likelihood Estimation):**
```
θ_MLE = argmax P(data | θ)
```
Finds parameters that make observed data most probable. No prior assumption.

**MAP (Maximum A Posteriori):**
```
θ_MAP = argmax P(θ | data) = argmax P(data | θ) · P(θ)
```
Incorporates prior belief about θ. MAP with Gaussian prior = L2 regularization. MAP with Laplace prior = L1 regularization.
</details>

---

## 🤖 Deep Learning

<details>
<summary><strong>Q: How does backpropagation work?</strong></summary>

Backprop computes gradients of the loss with respect to all parameters using the chain rule.

```
Forward: x → [L1] → h → [L2] → ŷ → loss
Backward: ∂loss/∂W₂ → ∂loss/∂h → ∂loss/∂W₁
```

```python
loss = criterion(output, target)
loss.backward()       # Compute all gradients
optimizer.step()      # Update weights: W = W - lr * W.grad
optimizer.zero_grad() # Clear for next batch
```

Chain rule: `∂L/∂W₁ = (∂L/∂ŷ) · (∂ŷ/∂h) · (∂h/∂W₁)`
</details>

<details>
<summary><strong>Q: Explain the vanishing gradient problem and solutions.</strong></summary>

In deep networks, gradients shrink exponentially as they propagate backward through many sigmoid/tanh layers → early layers learn very slowly.

**Solutions:**
| Fix | How |
|---|---|
| ReLU activation | Gradient = 1 for positive inputs (no squashing) |
| Batch Normalization | Normalizes activations, keeps gradients stable |
| Residual connections | Gradient flows directly via skip connections |
| LSTM/GRU | Gating mechanisms preserve long-range gradients |
| Gradient clipping | `torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)` |
</details>

<details>
<summary><strong>Q: What is attention mechanism / self-attention?</strong></summary>

Attention lets the model focus on relevant parts of the input for each output position.

```
Attention(Q, K, V) = softmax(QKᵀ / √dₖ) · V
```

- **Q** (Query): what we're looking for
- **K** (Key): what each position offers
- **V** (Value): actual content to aggregate

```python
# Scaled dot-product attention
import torch.nn.functional as F

def attention(Q, K, V):
    d_k = Q.size(-1)
    scores = (Q @ K.transpose(-2, -1)) / (d_k ** 0.5)
    weights = F.softmax(scores, dim=-1)
    return weights @ V
```

Self-attention: Q=K=V come from same sequence. Allows each token to attend to all others.
</details>

<details>
<summary><strong>Q: Compare CNN vs RNN vs Transformer for sequence tasks.</strong></summary>

| | CNN | RNN/LSTM | Transformer |
|---|---|---|---|
| Parallelizable | ✅ Yes | ❌ Sequential | ✅ Yes |
| Long-range deps | ❌ Fixed window | ⚠️ Struggles | ✅ Global attention |
| Memory | Low | Medium | High (O(n²)) |
| Best for | Local patterns, CV | Short sequences | NLP, long sequences |
| Speed | Fast | Slow | Fast (parallelized) |
</details>

<details>
<summary><strong>Q: What is batch normalization? Why does it help?</strong></summary>

BatchNorm normalizes activations within each mini-batch to have zero mean and unit variance, then applies learnable scale/shift:

```python
# PyTorch
self.bn = nn.BatchNorm2d(num_channels)

# What it computes:
# μ = mean(x), σ² = var(x)
# x_norm = (x - μ) / √(σ² + ε)
# output = γ * x_norm + β  (γ, β are learned)
```

**Benefits:** Reduces internal covariate shift, acts as regularization, allows higher learning rates, reduces sensitivity to weight initialization.
</details>

---

## 🗣️ NLP

<details>
<summary><strong>Q: How does BERT work? What makes it different from GPT?</strong></summary>

**BERT (Bidirectional Encoder Representations from Transformers):**
- Encoder-only transformer
- Bidirectional: sees both left and right context simultaneously
- Pre-trained with: Masked Language Model (MLM) + Next Sentence Prediction (NSP)
- Best for: classification, NER, Q&A (understanding tasks)

**GPT (Generative Pre-trained Transformer):**
- Decoder-only transformer
- Unidirectional (causal): only sees left context
- Pre-trained with: Next token prediction
- Best for: text generation, summarization, chat

```
BERT: [CLS] The [MASK] sat on the mat [SEP] → predicts "cat"
GPT:  The cat sat on → predicts "the"
```
</details>

<details>
<summary><strong>Q: What is RAG (Retrieval-Augmented Generation)?</strong></summary>

RAG combines a retriever (finds relevant documents) with a generator (LLM) to answer questions grounded in external knowledge.

```
Query → [Embed] → Vector DB search → Top-k docs
                                          ↓
                   Prompt: "Using these docs: {docs}\nAnswer: {query}"
                                          ↓
                                    LLM generates answer
```

```python
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-4"),
    retriever=vectorstore.as_retriever(search_kwargs={"k": 4})
)
```

**Why RAG?** Overcomes LLM knowledge cutoff, reduces hallucination, keeps knowledge updatable without retraining.
</details>

<details>
<summary><strong>Q: Explain word embeddings. Word2Vec vs GloVe vs FastText.</strong></summary>

Embeddings map words to dense vectors where similar words are close.

| | Word2Vec | GloVe | FastText |
|---|---|---|---|
| Method | Neural (CBOW/Skip-gram) | Matrix factorization on co-occurrence | Word2Vec + subword n-grams |
| OOV handling | ❌ No | ❌ No | ✅ Yes (via n-grams) |
| Morphology | ❌ No | ❌ No | ✅ Yes |
| Best for | General NLP | General NLP | Morphologically rich languages |

```python
from gensim.models import Word2Vec, FastText
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1)
vector = model.wv['python']  # shape: (100,)
```
</details>

---

## 👁️ Computer Vision

<details>
<summary><strong>Q: How does YOLO work? What makes YOLOv8 better?</strong></summary>

YOLO (You Only Look Once) divides image into S×S grid. Each cell predicts B bounding boxes + class probabilities in a **single forward pass**.

```
Input image (640×640)
       ↓
  Backbone (feature extraction)
       ↓
  Neck (FPN/PAN — multi-scale features)
       ↓
  Head (predict boxes + classes for 3 scales)
       ↓
  NMS (remove overlapping boxes)
       ↓
  Final detections
```

**YOLOv8 improvements over v5:**
- Anchor-free detection (no pre-defined anchors)
- Decoupled head (separate classification and regression)
- C2f module replaces C3 (better gradient flow)
- New loss: Distribution Focal Loss for bounding box regression
- ~35% fewer parameters than YOLOv5 at same accuracy

```python
from ultralytics import YOLO
model = YOLO('yolov8n.pt')
results = model('image.jpg')
results[0].boxes  # bboxes, confidences, classes
```
</details>

<details>
<summary><strong>Q: What is transfer learning? When to freeze layers?</strong></summary>

Transfer learning: use a model trained on large dataset (ImageNet) as starting point for your task.

**Strategies:**

| Scenario | Approach |
|---|---|
| Small dataset, similar domain | Freeze backbone, train head only |
| Small dataset, different domain | Freeze early layers, fine-tune later layers |
| Large dataset, any domain | Fine-tune entire network |

```python
# PyTorch — freeze backbone
model = torchvision.models.resnet50(pretrained=True)
for param in model.parameters():
    param.requires_grad = False  # Freeze all

# Replace and unfreeze head
model.fc = nn.Linear(2048, num_classes)  # Only fc trains
```
</details>

---

## 🏗️ ML System Design

<details>
<summary><strong>Q: Design a real-time fraud detection system.</strong></summary>

```
Transaction → [Feature Engineering] → [ML Model] → Decision
                     ↑                              ↓
              Feature Store                    Risk Score
              (user history,              → Block / Flag / Pass
               merchant profile,
               velocity features)
```

**Key components:**
1. **Features:** amount, merchant category, location delta, time of day, velocity (5 txns in 1 min?), device fingerprint
2. **Model:** XGBoost / LightGBM (low latency), backed by deep learning for complex patterns
3. **Threshold:** p(fraud) > 0.7 → block, 0.3-0.7 → MFA challenge, < 0.3 → pass
4. **Latency:** < 100ms P99 via feature precomputation + model serving (TorchServe/TFServing)
5. **Feedback loop:** labeled outcomes → retrain weekly

**Metrics:** Precision (false positives = bad UX), Recall (false negatives = fraud loss), F1, AUC
</details>

<details>
<summary><strong>Q: Design a recommendation system (YouTube/Netflix style).</strong></summary>

**Two-stage architecture:**

```
100M items → [Retrieval (fast)] → 1000 candidates
                                      ↓
                              [Ranking (accurate)]
                                      ↓
                               Top 50 shown to user
```

**Retrieval:** Matrix factorization / two-tower neural network
```python
# Two-tower: embed user and item separately, dot product for score
user_embed = user_tower(user_features)   # (batch, 128)
item_embed = item_tower(item_features)   # (batch, 128)
scores = (user_embed * item_embed).sum(-1)
```

**Ranking:** Wide & Deep / DIN / Transformer on (user, item, context) features

**Metrics:** Click-through rate, Watch time, NDCG, Coverage, Diversity
</details>

---

## 🐍 Python & Libraries

<details>
<summary><strong>Essential NumPy one-liners</strong></summary>

```python
import numpy as np

# Shape manipulation
x = np.random.randn(100, 3)
x.reshape(50, 6)           # Reshape
x.T                         # Transpose
x[:, np.newaxis]            # Add dimension
np.squeeze(x)               # Remove size-1 dims

# Math
np.dot(A, B)                # Matrix multiply (2D)
A @ B                       # Same, cleaner syntax
np.linalg.norm(x)           # L2 norm
np.linalg.eig(A)            # Eigendecomposition
np.linalg.svd(A)            # SVD

# Stats
np.mean(x, axis=0)          # Column means
np.std(x, ddof=1)           # Sample std
np.percentile(x, 75)        # 75th percentile
np.corrcoef(x[:, 0], x[:, 1])  # Correlation

# Boolean ops
np.where(x > 0, x, 0)      # ReLU!
x[x > 0]                    # Boolean indexing
np.any(x > 5), np.all(x > 0)
```
</details>

<details>
<summary><strong>Essential Pandas one-liners</strong></summary>

```python
import pandas as pd

# Load
df = pd.read_csv('data.csv')
df.info()               # Shape, dtypes, nulls
df.describe()           # Stats summary
df.head(), df.tail()

# Missing values
df.isnull().sum()                       # Null count per col
df.fillna(df.mean(), inplace=True)      # Fill numeric
df.dropna(subset=['target'])            # Drop rows with null target
df['col'].fillna(df['col'].mode()[0])   # Fill with mode

# Feature engineering
df['log_price'] = np.log1p(df['price'])
df['age_group'] = pd.cut(df['age'], bins=[0,18,35,60,100], labels=['teen','young','mid','senior'])
pd.get_dummies(df['category'], prefix='cat', drop_first=True)  # One-hot encode

# Aggregation
df.groupby('city')['salary'].agg(['mean','median','count'])
df.pivot_table(values='sales', index='region', columns='product', aggfunc='sum')
```
</details>

<details>
<summary><strong>Scikit-learn full pipeline template</strong></summary>

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV

num_features = ['age', 'salary', 'experience']
cat_features = ['city', 'department']

num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

cat_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

preprocessor = ColumnTransformer([
    ('num', num_pipeline, num_features),
    ('cat', cat_pipeline, cat_features)
])

full_pipeline = Pipeline([
    ('prep', preprocessor),
    ('model', GradientBoostingClassifier(n_estimators=100))
])

# Cross-validate
scores = cross_val_score(full_pipeline, X_train, y_train, cv=5, scoring='roc_auc')

# Grid search
param_grid = {'model__n_estimators': [100, 200], 'model__max_depth': [3, 5]}
gs = GridSearchCV(full_pipeline, param_grid, cv=5, n_jobs=-1, scoring='roc_auc')
gs.fit(X_train, y_train)
```
</details>

<details>
<summary><strong>PyTorch training loop template</strong></summary>

```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader

def train_one_epoch(model, loader, optimizer, criterion, device):
    model.train()
    total_loss = 0
    for X, y in loader:
        X, y = X.to(device), y.to(device)
        optimizer.zero_grad()
        output = model(X)
        loss = criterion(output, y)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        optimizer.step()
        total_loss += loss.item()
    return total_loss / len(loader)

@torch.no_grad()
def evaluate(model, loader, criterion, device):
    model.eval()
    total_loss, correct = 0, 0
    for X, y in loader:
        X, y = X.to(device), y.to(device)
        output = model(X)
        total_loss += criterion(output, y).item()
        correct += (output.argmax(1) == y).sum().item()
    return total_loss / len(loader), correct / len(loader.dataset)

# Training loop with early stopping
best_val_loss, patience, wait = float('inf'), 5, 0
for epoch in range(100):
    train_loss = train_one_epoch(model, train_loader, optimizer, criterion, device)
    val_loss, val_acc = evaluate(model, val_loader, criterion, device)
    scheduler.step(val_loss)
    
    if val_loss < best_val_loss:
        best_val_loss = val_loss
        torch.save(model.state_dict(), 'best_model.pt')
        wait = 0
    else:
        wait += 1
        if wait >= patience:
            print(f'Early stopping at epoch {epoch}')
            break
    
    print(f'Epoch {epoch}: train={train_loss:.4f} val={val_loss:.4f} acc={val_acc:.4f}')
```
</details>

---

## 🧩 Coding Patterns

<details>
<summary><strong>Custom Dataset class (PyTorch)</strong></summary>

```python
from torch.utils.data import Dataset
from PIL import Image
import torchvision.transforms as T

class ImageDataset(Dataset):
    def __init__(self, df, img_dir, transform=None):
        self.df = df.reset_index(drop=True)
        self.img_dir = img_dir
        self.transform = transform or T.Compose([
            T.Resize((224, 224)),
            T.ToTensor(),
            T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        img = Image.open(f"{self.img_dir}/{self.df.loc[idx, 'filename']}").convert('RGB')
        label = self.df.loc[idx, 'label']
        return self.transform(img), torch.tensor(label, dtype=torch.long)
```
</details>

<details>
<summary><strong>Evaluation metrics from scratch</strong></summary>

```python
import numpy as np

def precision_recall_f1(y_true, y_pred):
    tp = ((y_pred == 1) & (y_true == 1)).sum()
    fp = ((y_pred == 1) & (y_true == 0)).sum()
    fn = ((y_pred == 0) & (y_true == 1)).sum()
    precision = tp / (tp + fp + 1e-8)
    recall    = tp / (tp + fn + 1e-8)
    f1        = 2 * precision * recall / (precision + recall + 1e-8)
    return precision, recall, f1

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def iou(box1, box2):
    x1 = max(box1[0], box2[0]); y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2]); y2 = min(box1[3], box2[3])
    intersection = max(0, x2-x1) * max(0, y2-y1)
    union = (box1[2]-box1[0])*(box1[3]-box1[1]) + (box2[2]-box2[0])*(box2[3]-box2[1]) - intersection
    return intersection / (union + 1e-8)
```
</details>

---

## 💼 Behavioral

<details>
<summary><strong>Project walkthrough template (STAR format)</strong></summary>

**Situation:** "At [company/university], we faced [problem] — [metric showing scale]."

**Task:** "My role was to [responsibility] — specifically [what you owned]."

**Action:** 
1. "First I [explored/analyzed] the data and found [insight]."
2. "I chose [model/approach] because [reason over alternatives]."
3. "Key challenge was [X] — I solved it by [Y]."

**Result:** "[Metric improvement] — e.g., reduced inference time by 40%, improved F1 from 0.72 to 0.89."

**Tip:** Always quantify. "Improved accuracy" < "Improved F1 from 0.72 to 0.89 on a 100K sample test set."
</details>

<details>
<summary><strong>Questions to ask the interviewer</strong></summary>

1. "What does the ML infrastructure look like — on-prem, cloud, internal tooling?"
2. "How do you handle model monitoring and drift detection in production?"
3. "What's the typical iteration cycle from idea to model in production?"
4. "What's the biggest unsolved ML challenge on the team right now?"
5. "How does the team balance research vs engineering vs product priorities?"
</details>

---

## 🗺️ Roadmap

- [ ] LLM fine-tuning section (LoRA, QLoRA, RLHF)
- [ ] MLOps questions (MLflow, DVC, Kubeflow, feature stores)
- [ ] Reinforcement Learning fundamentals
- [ ] Time series deep dive
- [ ] More system design case studies

---

## 🤝 Contributing

Found an error? Have a great question/answer pair? PRs are very welcome.

```bash
git checkout -b add/new-question
# Add your Q&A in the relevant section
git commit -m 'Add: <topic> question on <concept>'
git push origin add/new-question
```

---

## ⭐ If this helped you land an offer — please star the repo!

<div align="center">

[![Star](https://img.shields.io/badge/⭐_Star_this_repo-FFD700?style=for-the-badge&labelColor=0D1117)](https://github.com/aasimansari1/ml-interview-prep)

MIT © [Mohd Aasim Ansari](https://github.com/aasimansari1)

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:003366,50:1a0a2e,100:0d0d0d&height=100&section=footer" width="100%"/>

</div>
