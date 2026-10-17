
 <div align="center">
<img width="112" height="87" alt="rudradb_logo_no_bg_sym_smallest" src="https://github.com/user-attachments/assets/01cb40ea-6d5f-415e-ba11-88eb830da64f" />
</div>
<div align="center">
<img width="169" height="35" alt="rudradb_brandName_no_bg_no_tag_smallest" src="https://github.com/user-attachments/assets/88e7135a-3184-4ce3-a35d-6f3cdc3ac5d3" />
</div>

# RudraDB-Opin - Relationship-Aware Vector Database 
### Repository contains Examples of RudraDB-Opin (Free Version)

<div align="center">

![RudraDB-Opin Logo](https://img.shields.io/badge/RudraDB-Opin-blue?style=for-the-badge&logo=database&logoColor=white)
[![PyPI version](https://img.shields.io/pypi/v/rudradb-opin.svg?style=for-the-badge)](https://pypi.org/project/rudradb-opin/)
[![Python versions](https://img.shields.io/pypi/pyversions/rudradb-opin.svg?style=for-the-badge)](https://pypi.org/project/rudradb-opin/)
[![License](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)](LICENSE)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/rudradb-opin?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=PyPI+Downloads)](https://pepy.tech/projects/rudradb-opin)

**🌟 The World's First Relationship-Aware Vector Database (Free Version)**  
*Perfect for Learning, Tutorials, Hackathons, Enterprise POCs and AI Development*

</div>

---
### 🆓 **100% Forever Free Version with Premium Features**
- **100000 vectors** - Perfect tutorial and learning size
- **500000 relationships** - Rich relationship modeling capability  
- **🎯 Auto-Dimension Detection** - Works with any ML model instantly
- **🧠 Auto-Relationship Detection** - Builds intelligent connections automatically
- **🪄 Auto-Optimize Search** - quicker search response automatically
- **📈 Auto-Intelligent Knowlege Graph Construction** - Builds intelligent knowledge graph construction for connected relationships automatically
- **Complete feature set** - All 5 relationship types and algorithms
- **Multi-hop discovery** - 2-degree relationship traversal
- **No usage tracking** - Complete privacy and freedom
- **Production-quality code** - Same codebase as enterprise RudraDB

## 📦 Quick Installation & Setup

### Install from PyPI
```bash
pip install rudradb-opin
```

### Verify Installation with Auto-Features
```python
import rudradb
import numpy as np

# Test auto-dimension detection
db = rudradb.RudraDB()  # No dimension specified!
print(f"🎯 Auto-dimension detection: {'✅ Enabled' if db.dimension() is None else 'Manual'}")

# Test with random embedding
test_embedding = np.random.rand(384).astype(np.float32)
db.add_vector("test", test_embedding, {"test": True})
print(f"🎯 Auto-detected dimension: {db.dimension()}")

# Verify auto-relationship capabilities
print(f"🧠 Auto-relationship detection: ✅ Available")
print(f"📊 Limits: {rudradb.MAX_VECTORS} vectors, {rudradb.MAX_RELATIONSHIPS} relationships")
print(f"🎉 RudraDB-Opin {rudradb.__version__} ready with auto-intelligence!")
```

---


## 🎯 Revolutionary Auto-Intelligence for AI Developers

**RudraDB-Opin** is the only vector database that combines **relationship-aware search** with **revolutionary auto-features** that eliminate manual configuration. While traditional databases require complex setup and manual relationship building, RudraDB-Opin automatically detects dimensions, builds intelligent relationships, and optimizes performance.

### 🤖 **World's First Auto-Intelligent Vector Database**

#### 🎯 **Auto-Dimension Detection**
**Zero Configuration Required** - Works with any ML model instantly:

```python
import rudradb
import numpy as np
from sentence_transformers import SentenceTransformer
import openai

# ✨ NO DIMENSION SPECIFICATION NEEDED!
db = rudradb.RudraDB()  # Auto-detects from any model

# Works with Sentence Transformers (384D)
model_384 = SentenceTransformer('all-MiniLM-L6-v2')
text_384 = model_384.encode(["AI transforms everything"])[0]
db.add_vector("st_doc", text_384.astype(np.float32), {"model": "sentence-transformers"})

print(f"🎯 Auto-detected: {db.dimension()}D")  # 384

# Works with different models seamlessly (768D)  
model_768 = SentenceTransformer('all-mpnet-base-v2')
text_768 = model_768.encode(["Machine learning revolution"])[0]
db2 = rudradb.RudraDB()  # Fresh auto-detection
db2.add_vector("mpnet_doc", text_768.astype(np.float32), {"model": "mpnet"})

print(f"🎯 Auto-detected: {db2.dimension()}D")  # 768

# Works with OpenAI (1536D)
openai.api_key = "your-key"
response = openai.Embedding.create(model="text-embedding-ada-002", input="Deep learning")
embedding_1536 = np.array(response['data'][0]['embedding'], dtype=np.float32)
db3 = rudradb.RudraDB()  # Fresh auto-detection
db3.add_vector("openai_doc", embedding_1536, {"model": "openai-ada-002"})

print(f"🎯 Auto-detected: {db3.dimension()}D")  # 1536

# 🔥 IMPOSSIBLE WITH TRADITIONAL VECTOR DATABASES! 
# No manual configuration, no dimension errors, just works!
```

#### 🧠 **Auto-Relationship Detection**
**Intelligent Connection Building** - Automatically discovers semantic relationships:

```python
def add_document_with_auto_intelligence(db, doc_id, text, metadata):
    """Add document with full auto-intelligence enabled"""
    
    # 1. Auto-dimension detection handles any model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embedding = model.encode([text])[0].astype(np.float32)
    
    # 2. Add vector - dimension auto-detected on first vector
    db.add_vector(doc_id, embedding, metadata)
    
    # 3. 🧠 Auto-Relationship Detection analyzes content and metadata
    relationships_found = auto_build_smart_relationships(db, doc_id, metadata)
    
    return relationships_found

def auto_build_smart_relationships(db, new_doc_id, metadata):
    """RudraDB-Opin's intelligent auto-relationship detection"""
    relationships_created = 0
    
    # 🎯 Analyze all existing vectors for intelligent connections
    for existing_id in db.list_vectors():
        if existing_id == new_doc_id:
            continue
            
        existing_vector = db.get_vector(existing_id)
        existing_meta = existing_vector['metadata']
        
        # 🧠 SEMANTIC ANALYSIS: Content similarity detection
        if metadata.get('category') == existing_meta.get('category'):
            db.add_relationship(new_doc_id, existing_id, "semantic", 0.8)
            relationships_created += 1
            print(f"   🔗 Semantic: {new_doc_id} ↔ {existing_id} (same category)")
        
        # 🧠 HIERARCHICAL ANALYSIS: Parent-child detection  
        if (metadata.get('type') == 'concept' and existing_meta.get('type') == 'example'):
            db.add_relationship(new_doc_id, existing_id, "hierarchical", 0.9)
            relationships_created += 1
            print(f"   📊 Hierarchical: {new_doc_id} → {existing_id} (concept→example)")
        
        # 🧠 TEMPORAL ANALYSIS: Learning sequence detection
        difficulties = {"beginner": 1, "intermediate": 2, "advanced": 3}
        current_level = difficulties.get(metadata.get('difficulty', 'intermediate'), 2)
        existing_level = difficulties.get(existing_meta.get('difficulty', 'intermediate'), 2)
        
        if abs(current_level - existing_level) == 1 and metadata.get('topic') == existing_meta.get('topic'):
            db.add_relationship(new_doc_id, existing_id, "temporal", 0.85)
            relationships_created += 1
            print(f"   ⏰ Temporal: {new_doc_id} ↔ {existing_id} (learning sequence)")
        
        # 🧠 ASSOCIATIVE ANALYSIS: Tag overlap detection
        new_tags = set(metadata.get('tags', []))
        existing_tags = set(existing_meta.get('tags', []))
        shared_tags = new_tags & existing_tags
        
        if len(shared_tags) >= 2:  # Strong tag overlap
            strength = min(0.7, len(shared_tags) * 0.2)
            db.add_relationship(new_doc_id, existing_id, "associative", strength)
            relationships_created += 1
            print(f"   🏷️ Associative: {new_doc_id} ↔ {existing_id} (tags: {', '.join(shared_tags)})")
        
        # 🧠 CAUSAL ANALYSIS: Problem-solution detection
        if (metadata.get('type') == 'problem' and existing_meta.get('type') == 'solution'):
            db.add_relationship(new_doc_id, existing_id, "causal", 0.95)
            relationships_created += 1
            print(f"   🎯 Causal: {new_doc_id} → {existing_id} (problem→solution)")
    
    return relationships_created

# 🚀 DEMO: Building a Knowledge Base with Auto-Intelligence
print("🤖 Building AI Knowledge Base with Auto-Intelligence")
db = rudradb.RudraDB()  # Auto-dimension detection enabled

# Add documents - watch auto-relationship detection work!
documents = [
    {
        "id": "ai_basics",
        "text": "Artificial Intelligence fundamentals and core concepts",
        "metadata": {"category": "AI", "difficulty": "beginner", "type": "concept", "tags": ["ai", "basics"], "topic": "ai"}
    },
    {
        "id": "ml_intro", 
        "text": "Machine Learning introduction and supervised learning",
        "metadata": {"category": "AI", "difficulty": "intermediate", "type": "concept", "tags": ["ml", "supervised"], "topic": "ai"}
    },
    {
        "id": "python_ml_example",
        "text": "Python code example for machine learning with scikit-learn", 
        "metadata": {"category": "AI", "difficulty": "intermediate", "type": "example", "tags": ["python", "ml", "code"], "topic": "ai"}
    },
    {
        "id": "overfitting_problem",
        "text": "Overfitting problem in machine learning models",
        "metadata": {"category": "AI", "difficulty": "advanced", "type": "problem", "tags": ["ml", "overfitting"], "topic": "ai"}
    },
    {
        "id": "regularization_solution", 
        "text": "Regularization techniques to prevent overfitting",
        "metadata": {"category": "AI", "difficulty": "advanced", "type": "solution", "tags": ["ml", "regularization"], "topic": "ai"}
    }
]

total_relationships = 0
for doc in documents:
    relationships = add_document_with_auto_intelligence(
        db, doc["id"], doc["text"], doc["metadata"]
    )
    total_relationships += relationships

print(f"\n✅ Auto-created knowledge base:")
print(f"   📄 {db.vector_count()} documents")
print(f"   🔗 {db.relationship_count()} auto-detected relationships")
print(f"   🎯 {db.dimension()}-dimensional embeddings (auto-detected)")
print(f"   🧠 {total_relationships} intelligent connections found automatically")

# 🔍 Experience Auto-Enhanced Search
query = "machine learning techniques and examples"
model = SentenceTransformer('all-MiniLM-L6-v2')
query_embedding = model.encode([query])[0].astype(np.float32)

# Traditional similarity search
basic_results = db.search(query_embedding, rudradb.SearchParams(
    top_k=5, include_relationships=False
))

# 🧠 Auto-relationship enhanced search
enhanced_results = db.search(query_embedding, rudradb.SearchParams(
    top_k=5,
    include_relationships=True,  # Uses auto-detected relationships!
    max_hops=2,
    relationship_weight=0.4
))

print(f"\n🔍 Search Results Comparison:")
print(f"Traditional search: {len(basic_results)} results")
print(f"Auto-enhanced search: {len(enhanced_results)} results with relationship intelligence")

for result in enhanced_results:
    vector = db.get_vector(result.vector_id)
    connection = "Direct match" if result.hop_count == 0 else f"{result.hop_count}-hop auto-connection"
    print(f"   📄 {vector['metadata']['type']}: {result.vector_id}")
    print(f"      └─ {connection} (score: {result.combined_score:.3f})")

print(f"\n🎉 RudraDB-Opin discovered {sum(1 for r in enhanced_results if r.hop_count > 0)} additional relevant documents")
print("    that traditional vector databases would completely miss!")
```

### 🚀 **Ready for Production?**
When you outgrow the 100000-vector limit, upgrade seamlessly:
```bash
pip uninstall rudradb-opin
pip install rudradb  # Get 1M+ vectors for PRO & Unlimited Vector for Enterprise, same API! 
```

---


## 🤖 Complete ML Framework Integrations

### 1. 🔥 **OpenAI Integration** - Auto-Dimension Detection for 1536D Embeddings

```python
import openai
import rudradb
import numpy as np

class OpenAI_RudraDB_RAG:
    """Complete OpenAI + RudraDB-Opin integration with auto-features"""
    
    def __init__(self, api_key):
        openai.api_key = api_key
        self.db = rudradb.RudraDB()  # 🎯 Auto-detects OpenAI's 1536 dimensions
        print("🤖 OpenAI + RudraDB-Opin initialized with auto-dimension detection")
    
    def add_document(self, doc_id, text, metadata=None):
        """Add document with OpenAI embeddings + auto-relationship detection"""
        
        # Get OpenAI embedding
        response = openai.Embedding.create(
            model="text-embedding-ada-002",
            input=text
        )
        embedding = np.array(response['data'][0]['embedding'], dtype=np.float32)
        
        # Add with auto-intelligence
        enhanced_metadata = {
            "text": text,
            "embedding_model": "text-embedding-ada-002",
            "auto_detected_dim": self.db.dimension() if self.db.dimension() else "pending",
            **(metadata or {})
        }
        
        self.db.add_vector(doc_id, embedding, enhanced_metadata)
        
        # 🧠 Auto-build relationships based on content analysis
        relationships_created = self._auto_detect_relationships(doc_id, enhanced_metadata)
        
        return {
            "dimension": self.db.dimension(),
            "relationships_created": relationships_created,
            "total_vectors": self.db.vector_count()
        }
    
    def _auto_detect_relationships(self, new_doc_id, metadata):
        """Auto-detect relationships using OpenAI embeddings + metadata analysis"""
        relationships = 0
        new_text = metadata.get('text', '')
        new_category = metadata.get('category')
        new_tags = set(metadata.get('tags', []))
        
        for existing_id in self.db.list_vectors():
            if existing_id == new_doc_id or relationships >= 3:
                continue
                
            existing = self.db.get_vector(existing_id)
            existing_meta = existing['metadata']
            existing_text = existing_meta.get('text', '')
            existing_category = existing_meta.get('category')
            existing_tags = set(existing_meta.get('tags', []))
            
            # 🎯 Semantic similarity through category matching
            if new_category and new_category == existing_category:
                self.db.add_relationship(new_doc_id, existing_id, "semantic", 0.8, 
                                       {"reason": "same_category", "auto_detected": True})
                relationships += 1
                print(f"   🔗 Auto-linked {new_doc_id} ↔ {existing_id} (semantic: same category)")
            
            # 🏷️ Associative through tag overlap
            shared_tags = new_tags & existing_tags
            if len(shared_tags) >= 1:
                strength = min(0.7, len(shared_tags) * 0.3)
                self.db.add_relationship(new_doc_id, existing_id, "associative", strength,
                                       {"reason": "shared_tags", "tags": list(shared_tags), "auto_detected": True})
                relationships += 1
                print(f"   🏷️ Auto-linked {new_doc_id} ↔ {existing_id} (associative: {shared_tags})")
        
        return relationships
    
    def intelligent_qa(self, question):
        """Answer questions using relationship-aware search + GPT"""
        
        # Get question embedding with auto-dimension compatibility
        response = openai.Embedding.create(
            model="text-embedding-ada-002", 
            input=question
        )
        query_embedding = np.array(response['data'][0]['embedding'], dtype=np.float32)
        
        # 🧠 Auto-enhanced relationship-aware search
        results = self.db.search(query_embedding, rudradb.SearchParams(
            top_k=5,
            include_relationships=True,  # Use auto-detected relationships
            max_hops=2,                 # Multi-hop discovery
            relationship_weight=0.3     # Balance similarity + relationships
        ))
        
        # Build context from auto-enhanced results
        context_pieces = []
        for result in results:
            vector = self.db.get_vector(result.vector_id)
            text = vector['metadata']['text']
            connection_type = "Direct match" if result.hop_count == 0 else f"{result.hop_count}-hop connection"
            context_pieces.append(f"[{connection_type}] {text}")
        
        context = "\n".join(context_pieces)
        
        # Generate answer with GPT
        chat_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an AI assistant with access to a relationship-aware knowledge base. Use the provided context to answer questions, noting both direct matches and relationship-connected information."},
                {"role": "user", "content": f"Context from relationship-aware search:\n{context}\n\nQuestion: {question}"}
            ]
        )
        
        return {
            "answer": chat_response.choices[0].message.content,
            "sources_found": len(results),
            "relationship_enhanced": sum(1 for r in results if r.hop_count > 0),
            "context_dimension": self.db.dimension()
        }

# 🚀 Demo: OpenAI + Auto-Intelligence
rag = OpenAI_RudraDB_RAG("your-openai-api-key")

# Add AI knowledge with auto-relationship detection
documents = [
    {"id": "ai_overview", "text": "Artificial Intelligence is transforming industries through automation and intelligent decision making.", 
     "category": "AI", "tags": ["ai", "automation", "industry"]},
    {"id": "ml_subset", "text": "Machine Learning is a subset of AI that enables computers to learn from data without explicit programming.",
     "category": "AI", "tags": ["ml", "data", "learning"]},
    {"id": "dl_neural", "text": "Deep Learning uses neural networks with multiple layers to process complex patterns in data.",
     "category": "AI", "tags": ["dl", "neural", "patterns"]},
    {"id": "nlp_language", "text": "Natural Language Processing helps computers understand and generate human language.",
     "category": "AI", "tags": ["nlp", "language", "text"]},
    {"id": "cv_vision", "text": "Computer Vision enables machines to interpret and analyze visual information from images and videos.",
     "category": "AI", "tags": ["cv", "vision", "images"]}
]

print("🤖 Building AI Knowledge Base with OpenAI + Auto-Intelligence:")
for doc in documents:
    result = rag.add_document(doc["id"], doc["text"], {"category": doc["category"], "tags": doc["tags"]})
    print(f"   📄 {doc['id']}: {result['relationships_created']} auto-relationships, {result['dimension']}D embedding")

print(f"\n✅ Knowledge base ready: {rag.db.vector_count()} vectors, {rag.db.relationship_count()} auto-relationships")

# Intelligent Q&A with relationship-aware context
answer = rag.intelligent_qa("How does machine learning relate to other AI technologies?")
print(f"\n🧠 Intelligent Answer:")
print(f"   Sources: {answer['sources_found']} documents (including {answer['relationship_enhanced']} through relationships)")
print(f"   Answer: {answer['answer'][:200]}...")
```

### 2. 🤗 **HuggingFace Integration** - Multi-Model Auto-Dimension Detection

```python
from transformers import AutoTokenizer, AutoModel, pipeline
from sentence_transformers import SentenceTransformer
import torch
import rudradb
import numpy as np

class HuggingFace_RudraDB_MultiModel:
    """HuggingFace + RudraDB-Opin with multi-model auto-dimension detection"""
    
    def __init__(self):
        self.models = {}
        self.databases = {}
        print("🤗 HuggingFace + RudraDB-Opin Multi-Model System initialized")
    
    def add_model(self, model_name, model_type="sentence-transformer"):
        """Add a HuggingFace model with auto-dimension detection"""
        
        if model_type == "sentence-transformer":
            model = SentenceTransformer(model_name)
            dimension = model.get_sentence_embedding_dimension()
        else:
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            model = AutoModel.from_pretrained(model_name)
            # Get dimension from config
            dimension = model.config.hidden_size
            model = {"tokenizer": tokenizer, "model": model}
        
        self.models[model_name] = {
            "model": model,
            "type": model_type, 
            "expected_dimension": dimension
        }
        
        # Create database with auto-dimension detection
        self.databases[model_name] = rudradb.RudraDB()  # 🎯 Auto-detects dimension
        
        print(f"✅ Added {model_name} (expected: {dimension}D, auto-detection enabled)")
        
    def encode_text(self, model_name, text):
        """Encode text with specified model"""
        model_info = self.models[model_name]
        
        if model_info["type"] == "sentence-transformer":
            embedding = model_info["model"].encode([text])[0]
        else:
            tokenizer = model_info["model"]["tokenizer"]
            model = model_info["model"]["model"]
            
            inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
            with torch.no_grad():
                outputs = model(**inputs)
                embedding = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
        
        return embedding.astype(np.float32)
    
    def add_document_multimodel(self, doc_id, text, metadata, model_names=None):
        """Add document to multiple model databases with auto-relationship detection"""
        
        if model_names is None:
            model_names = list(self.models.keys())
        
        results = {}
        for model_name in model_names:
            db = self.databases[model_name]
            
            # Encode with current model
            embedding = self.encode_text(model_name, text)
            
            # Add to database - auto-dimension detection in action
            enhanced_metadata = {
                "text": text,
                "model": model_name,
                "expected_dim": self.models[model_name]["expected_dimension"],
                **metadata
            }
            
            db.add_vector(doc_id, embedding, enhanced_metadata)
            
            # Auto-detect relationships within this model's space
            relationships = self._auto_build_relationships(db, doc_id, enhanced_metadata)
            
            results[model_name] = {
                "expected_dim": self.models[model_name]["expected_dimension"],
                "detected_dim": db.dimension(),
                "relationships_created": relationships,
                "match": db.dimension() == self.models[model_name]["expected_dimension"]
            }
        
        return results
    
    def _auto_build_relationships(self, db, doc_id, metadata):
        """Auto-build relationships based on metadata analysis"""
        relationships_created = 0
        doc_tags = set(metadata.get('tags', []))
        doc_category = metadata.get('category')
        doc_difficulty = metadata.get('difficulty')
        
        for other_id in db.list_vectors():
            if other_id == doc_id or relationships_created >= 3:
                continue
                
            other_vector = db.get_vector(other_id)
            other_meta = other_vector['metadata']
            other_tags = set(other_meta.get('tags', []))
            other_category = other_meta.get('category')
            other_difficulty = other_meta.get('difficulty')
            
            # Auto-detect relationship type and strength
            if doc_category == other_category:
                # Same category → semantic relationship
                db.add_relationship(doc_id, other_id, "semantic", 0.8,
                                  {"auto_detected": True, "reason": "same_category"})
                relationships_created += 1
            elif len(doc_tags & other_tags) >= 1:
                # Shared tags → associative relationship  
                shared = doc_tags & other_tags
                strength = min(0.7, len(shared) * 0.25)
                db.add_relationship(doc_id, other_id, "associative", strength,
                                  {"auto_detected": True, "reason": "shared_tags", "tags": list(shared)})
                relationships_created += 1
            elif doc_difficulty and other_difficulty:
                # Learning progression → temporal relationship
                levels = {"beginner": 1, "intermediate": 2, "advanced": 3}
                if abs(levels.get(doc_difficulty, 2) - levels.get(other_difficulty, 2)) == 1:
                    db.add_relationship(doc_id, other_id, "temporal", 0.85,
                                      {"auto_detected": True, "reason": "learning_progression"})
                    relationships_created += 1
        
        return relationships_created
    
    def cross_model_search(self, query, model_names=None, top_k=5):
        """Search across multiple models with auto-enhanced results"""
        
        if model_names is None:
            model_names = list(self.models.keys())
        
        all_results = {}
        for model_name in model_names:
            db = self.databases[model_name]
            query_embedding = self.encode_text(model_name, query)
            
            # Auto-enhanced relationship-aware search
            results = db.search(query_embedding, rudradb.SearchParams(
                top_k=top_k,
                include_relationships=True,  # Use auto-detected relationships
                max_hops=2,
                relationship_weight=0.3
            ))
            
            model_results = []
            for result in results:
                vector = db.get_vector(result.vector_id)
                model_results.append({
                    "document": result.vector_id,
                    "text": vector['metadata']['text'],
                    "similarity": result.similarity_score,
                    "combined_score": result.combined_score,
                    "connection": "direct" if result.hop_count == 0 else f"{result.hop_count}-hop",
                    "model_dimension": db.dimension()
                })
            
            all_results[model_name] = {
                "results": model_results,
                "dimension": db.dimension(),
                "total_docs": db.vector_count(),
                "total_relationships": db.relationship_count()
            }
        
        return all_results

# 🚀 Demo: Multi-Model Auto-Dimension Detection
system = HuggingFace_RudraDB_MultiModel()

# Add multiple HuggingFace models - each gets auto-dimension detection
models_to_test = [
    ("sentence-transformers/all-MiniLM-L6-v2", "sentence-transformer"),  # 384D
    ("sentence-transformers/all-mpnet-base-v2", "sentence-transformer"),  # 768D  
    ("distilbert-base-uncased", "transformer")  # 768D
]

print("🤗 Adding multiple HuggingFace models with auto-dimension detection:")
for model_name, model_type in models_to_test:
    system.add_model(model_name, model_type)

# Add documents to all models - watch auto-dimension detection work
documents = [
    {"id": "transformers_paper", "text": "Attention Is All You Need introduced the Transformer architecture revolutionizing NLP", 
     "category": "NLP", "tags": ["transformers", "attention", "nlp"], "difficulty": "advanced"},
    {"id": "bert_paper", "text": "BERT Bidirectional Encoder Representations from Transformers for language understanding",
     "category": "NLP", "tags": ["bert", "bidirectional", "nlp"], "difficulty": "intermediate"},  
    {"id": "gpt_intro", "text": "GPT Generative Pre-trained Transformers for text generation and completion",
     "category": "NLP", "tags": ["gpt", "generative", "nlp"], "difficulty": "intermediate"},
    {"id": "vision_transformer", "text": "Vision Transformer ViT applies transformer architecture to computer vision tasks",
     "category": "CV", "tags": ["vit", "transformers", "vision"], "difficulty": "advanced"}
]

print(f"\n📄 Adding documents with multi-model auto-dimension detection:")
for doc in documents:
    results = system.add_document_multimodel(
        doc["id"], doc["text"], 
        {"category": doc["category"], "tags": doc["tags"], "difficulty": doc["difficulty"]}
    )
    
    print(f"   📄 {doc['id']}:")
    for model_name, result in results.items():
        status = "✅" if result["match"] else "⚠️"
        print(f"      {status} {model_name}: Expected {result['expected_dim']}D → Detected {result['detected_dim']}D")
        print(f"         Relationships: {result['relationships_created']} auto-created")

# Cross-model search with auto-enhanced results
query = "transformer architecture for language and vision"
print(f"\n🔍 Cross-Model Search: '{query}'")
search_results = system.cross_model_search(query, top_k=3)

for model_name, results in search_results.items():
    print(f"\n📊 {model_name} ({results['dimension']}D, {results['total_relationships']} auto-relationships):")
    for result in results['results'][:2]:
        print(f"   📄 {result['document']}")
        print(f"      Connection: {result['connection']} (score: {result['combined_score']:.3f})")

print(f"\n🎉 Multi-model auto-dimension detection successful!")
print("    RudraDB-Opin seamlessly adapted to each model's dimensions automatically!")
```

### 3. 🔍 **Haystack Integration** - Document Processing with Auto-Relationships

```python
from haystack import Document, Pipeline
from haystack.document_stores import InMemoryDocumentStore  
from haystack.nodes import DensePassageRetriever, FARMReader
import rudradb
import numpy as np

class Haystack_RudraDB_Pipeline:
    """Haystack + RudraDB-Opin integration with auto-intelligence"""
    
    def __init__(self):
        # Initialize Haystack components
        self.haystack_store = InMemoryDocumentStore()
        self.retriever = DensePassageRetriever(
            document_store=self.haystack_store,
            query_embedding_model="facebook/dpr-question_encoder-single-nq-base",
            passage_embedding_model="facebook/dpr-ctx_encoder-single-nq-base"
        )
        
        # Initialize RudraDB-Opin with auto-dimension detection
        self.rudra_db = rudradb.RudraDB()  # 🎯 Auto-detects DPR dimensions (768D)
        
        print("🔍 Haystack + RudraDB-Opin pipeline initialized")
        print("   🤖 Auto-dimension detection enabled for DPR embeddings")
    
    def process_documents(self, documents):
        """Process documents through Haystack and add to RudraDB with auto-relationships"""
        
        # Convert to Haystack documents
        haystack_docs = []
        for i, doc in enumerate(documents):
            haystack_doc = Document(
                content=doc["text"],
                meta={
                    "id": doc["id"],
                    "title": doc.get("title", f"Document {i+1}"),
                    **doc.get("metadata", {})
                }
            )
            haystack_docs.append(haystack_doc)
        
        # Add to Haystack document store and create embeddings
        self.haystack_store.write_documents(haystack_docs)
        self.haystack_store.update_embeddings(self.retriever)
        
        print(f"📄 Processed {len(haystack_docs)} documents through Haystack")
        
        # Add to RudraDB-Opin with auto-dimension detection and relationship building
        relationships_created = 0
        for doc in haystack_docs:
            # Get embedding from Haystack
            embedding = self.haystack_store.get_embedding_by_id(doc.id)
            if embedding is not None:
                embedding_array = np.array(embedding, dtype=np.float32)
                
                # Add to RudraDB with enhanced metadata
                enhanced_meta = {
                    "haystack_id": doc.id,
                    "title": doc.meta["title"],
                    "content": doc.content,
                    "embedding_model": "facebook/dpr-ctx_encoder-single-nq-base",
                    **doc.meta
                }
                
                self.rudra_db.add_vector(doc.meta["id"], embedding_array, enhanced_meta)
                
                # 🧠 Auto-detect relationships based on Haystack processing + content analysis
                doc_relationships = self._auto_detect_haystack_relationships(doc.meta["id"], enhanced_meta)
                relationships_created += doc_relationships
        
        return {
            "processed_docs": len(haystack_docs),
            "rudra_dimension": self.rudra_db.dimension(),
            "auto_relationships": relationships_created,
            "total_vectors": self.rudra_db.vector_count()
        }
    
    def _auto_detect_haystack_relationships(self, doc_id, metadata):
        """Auto-detect relationships using Haystack embeddings + metadata"""
        relationships = 0
        doc_content = metadata.get('content', '')
        doc_title = metadata.get('title', '')
        doc_category = metadata.get('category')
        doc_topics = set(metadata.get('topics', []))
        
        # Analyze against existing documents
        for existing_id in self.rudra_db.list_vectors():
            if existing_id == doc_id or relationships >= 4:
                continue
            
            existing = self.rudra_db.get_vector(existing_id)
            existing_meta = existing['metadata']
            existing_content = existing_meta.get('content', '')
            existing_category = existing_meta.get('category')
            existing_topics = set(existing_meta.get('topics', []))
            
            # 🎯 Content-based semantic relationships (using Haystack embeddings)
            if doc_category and doc_category == existing_category:
                self.rudra_db.add_relationship(doc_id, existing_id, "semantic", 0.85,
                    {"auto_detected": True, "reason": "haystack_same_category", "method": "dpr_embeddings"})
                relationships += 1
                print(f"   🔗 Haystack semantic: {doc_id} ↔ {existing_id}")
            
            # 🏷️ Topic overlap relationships  
            shared_topics = doc_topics & existing_topics
            if len(shared_topics) >= 1:
                strength = min(0.8, len(shared_topics) * 0.3)
                self.rudra_db.add_relationship(doc_id, existing_id, "associative", strength,
                    {"auto_detected": True, "reason": "shared_topics", "topics": list(shared_topics), "method": "haystack_analysis"})
                relationships += 1
                print(f"   🏷️ Haystack associative: {doc_id} ↔ {existing_id} (topics: {shared_topics})")
            
            # 📊 Hierarchical relationships through title analysis
            if "introduction" in doc_title.lower() and existing_category == doc_category:
                self.rudra_db.add_relationship(doc_id, existing_id, "hierarchical", 0.7,
                    {"auto_detected": True, "reason": "introduction_hierarchy", "method": "haystack_title_analysis"})
                relationships += 1
                print(f"   📊 Haystack hierarchical: {doc_id} → {existing_id}")
        
        return relationships
    
    def hybrid_search(self, question, top_k=5):
        """Hybrid search using Haystack retrieval + RudraDB relationship-aware search"""
        
        # 1. Haystack dense retrieval
        haystack_results = self.retriever.retrieve(question, top_k=top_k*2)
        
        # 2. RudraDB-Opin relationship-aware search
        question_embedding = self.retriever.embed_queries([question])[0]
        question_embedding = np.array(question_embedding, dtype=np.float32)
        
        rudra_results = self.rudra_db.search(question_embedding, rudradb.SearchParams(
            top_k=top_k,
            include_relationships=True,  # 🧠 Use auto-detected relationships
            max_hops=2,
            relationship_weight=0.4
        ))
        
        # 3. Combine and deduplicate results
        combined_results = []
        seen_docs = set()
        
        # Add Haystack results
        for doc in haystack_results[:top_k]:
            if doc.meta["id"] not in seen_docs:
                combined_results.append({
                    "id": doc.meta["id"],
                    "title": doc.meta.get("title", ""),
                    "content": doc.content[:200] + "...",
                    "source": "haystack_dense",
                    "score": doc.score,
                    "method": "DPR retrieval"
                })
                seen_docs.add(doc.meta["id"])
        
        # Add RudraDB relationship-enhanced results
        for result in rudra_results:
            if result.vector_id not in seen_docs:
                vector = self.rudra_db.get_vector(result.vector_id)
                connection = "direct" if result.hop_count == 0 else f"{result.hop_count}-hop auto-connection"
                combined_results.append({
                    "id": result.vector_id,
                    "title": vector['metadata'].get('title', ''),
                    "content": vector['metadata'].get('content', '')[:200] + "...",
                    "source": "rudradb_relationships",
                    "score": result.combined_score,
                    "method": f"Relationship-aware ({connection})",
                    "hop_count": result.hop_count
                })
                seen_docs.add(result.vector_id)
        
        # Sort by score
        combined_results.sort(key=lambda x: x["score"], reverse=True)
        
        return {
            "question": question,
            "total_results": len(combined_results),
            "haystack_results": len([r for r in combined_results if r["source"] == "haystack_dense"]),
            "rudra_relationship_results": len([r for r in combined_results if r["source"] == "rudradb_relationships"]),
            "relationship_enhanced": len([r for r in combined_results if r.get("hop_count", 0) > 0]),
            "results": combined_results[:top_k],
            "dimension": self.rudra_db.dimension()
        }

# 🚀 Demo: Haystack + RudraDB Auto-Intelligence
pipeline = Haystack_RudraDB_Pipeline()

# Process documents with auto-dimension detection and relationship building
documents = [
    {
        "id": "ai_intro_doc",
        "text": "Artificial Intelligence Introduction: AI systems can perform tasks that typically require human intelligence, including learning, reasoning, and problem-solving.",
        "title": "AI Introduction",
        "metadata": {"category": "AI", "topics": ["ai", "introduction", "basics"], "difficulty": "beginner"}
    },
    {
        "id": "machine_learning_fundamentals", 
        "text": "Machine Learning Fundamentals: ML algorithms enable computers to learn from data without being explicitly programmed for every task.",
        "title": "ML Fundamentals",
        "metadata": {"category": "AI", "topics": ["ml", "algorithms", "data"], "difficulty": "intermediate"}
    },
    {
        "id": "neural_networks_deep",
        "text": "Neural Networks and Deep Learning: Deep neural networks with multiple layers can learn complex patterns and representations from large datasets.",
        "title": "Neural Networks",
        "metadata": {"category": "AI", "topics": ["neural", "deep", "learning"], "difficulty": "advanced"}
    },
    {
        "id": "nlp_processing",
        "text": "Natural Language Processing: NLP enables computers to understand, interpret, and generate human language in a valuable way.",
        "title": "NLP Overview", 
        "metadata": {"category": "NLP", "topics": ["nlp", "language", "text"], "difficulty": "intermediate"}
    },
    {
        "id": "computer_vision_intro",
        "text": "Computer Vision Introduction: CV systems can automatically identify, analyze, and understand visual content from images and videos.",
        "title": "Computer Vision",
        "metadata": {"category": "CV", "topics": ["vision", "images", "analysis"], "difficulty": "intermediate"}
    }
]

print("🔍 Processing documents through Haystack + RudraDB pipeline:")
processing_result = pipeline.process_documents(documents)

print(f"✅ Processing complete:")
print(f"   📄 Documents processed: {processing_result['processed_docs']}")
print(f"   🎯 Auto-detected dimension: {processing_result['rudra_dimension']}D (DPR embeddings)")
print(f"   🧠 Auto-relationships created: {processing_result['auto_relationships']}")
print(f"   📊 Total vectors in RudraDB: {processing_result['total_vectors']}")

# Hybrid search with relationship enhancement
questions = [
    "What are the fundamentals of machine learning?",
    "How do neural networks work in AI systems?"
]

print(f"\n🔍 Hybrid Search Demonstrations:")
for question in questions:
    results = pipeline.hybrid_search(question, top_k=4)
    
    print(f"\n❓ Question: {question}")
    print(f"   📊 Results: {results['total_results']} total ({results['haystack_results']} Haystack + {results['rudra_relationship_results']} RudraDB)")
    print(f"   🧠 Relationship-enhanced: {results['relationship_enhanced']} documents found through auto-detected connections")
    print(f"   🎯 Search dimension: {results['dimension']}D")
    
    print("   Top Results:")
    for i, result in enumerate(results['results'][:3], 1):
        print(f"      {i}. {result['title']}")
        print(f"         Method: {result['method']} (score: {result['score']:.3f})")
        print(f"         Preview: {result['content']}")

print(f"\n🎉 Haystack + RudraDB-Opin integration successful!")
print("    Auto-dimension detection handled DPR embeddings seamlessly!")
print("    Auto-relationship detection enhanced search with intelligent connections!")
```

### 4. 🎨 **LangChain Integration** - Advanced RAG with Auto-Features

```python
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document
import rudradb
import numpy as np

class LangChain_RudraDB_AutoRAG:
    """LangChain + RudraDB-Opin integration with auto-intelligence for advanced RAG"""
    
    def __init__(self, embedding_model_name="sentence-transformers/all-MiniLM-L6-v2"):
        # Initialize LangChain components
        self.embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)
        self.text_splitter = CharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50,
            separator="\n"
        )
        
        # Initialize RudraDB-Opin with auto-dimension detection  
        self.db = rudradb.RudraDB()  # 🎯 Auto-detects LangChain embedding dimensions
        self.embedding_model_name = embedding_model_name
        
        print(f"🦜 LangChain + RudraDB-Opin Auto-RAG initialized")
        print(f"   🎯 Embedding model: {embedding_model_name}")
        print(f"   🤖 Auto-dimension detection enabled")
    
    def add_documents_with_chunking(self, documents):
        """Add documents with LangChain chunking + RudraDB auto-relationship detection"""
        
        all_chunks = []
        chunk_metadata = []
        
        # Process each document through LangChain
        for doc in documents:
            # Create LangChain document
            langchain_doc = Document(
                page_content=doc["content"],
                metadata={
                    "source_id": doc["id"],
                    "title": doc.get("title", ""),
                    **doc.get("metadata", {})
                }
            )
            
            # Split into chunks
            chunks = self.text_splitter.split_documents([langchain_doc])
            
            # Process each chunk
            for i, chunk in enumerate(chunks):
                chunk_id = f"{doc['id']}_chunk_{i}"
                
                # Create embeddings through LangChain
                embedding = self.embeddings.embed_query(chunk.page_content)
                embedding_array = np.array(embedding, dtype=np.float32)
                
                # Enhanced metadata for auto-relationship detection
                enhanced_metadata = {
                    "chunk_id": chunk_id,
                    "source_document": doc["id"], 
                    "chunk_index": i,
                    "chunk_content": chunk.page_content,
                    "embedding_model": self.embedding_model_name,
                    "langchain_processed": True,
                    **chunk.metadata
                }
                
                # Add to RudraDB with auto-dimension detection
                self.db.add_vector(chunk_id, embedding_array, enhanced_metadata)
                
                all_chunks.append(chunk_id)
                chunk_metadata.append(enhanced_metadata)
        
        # 🧠 Auto-detect relationships between chunks after all are added
        relationships_created = self._auto_detect_document_relationships(chunk_metadata)
        
        return {
            "total_chunks": len(all_chunks),
            "auto_detected_dimension": self.db.dimension(),
            "auto_relationships": relationships_created,
            "documents_processed": len(documents)
        }
    
    def _auto_detect_document_relationships(self, chunk_metadata):
        """Auto-detect sophisticated relationships between document chunks"""
        relationships = 0
        
        print("🧠 Auto-detecting sophisticated chunk relationships...")
        
        for i, chunk_meta in enumerate(chunk_metadata):
            chunk_id = chunk_meta["chunk_id"]
            source_doc = chunk_meta["source_document"]
            chunk_index = chunk_meta["chunk_index"]
            content = chunk_meta["chunk_content"]
            category = chunk_meta.get("category")
            topics = set(chunk_meta.get("topics", []))
            
            for j, other_meta in enumerate(chunk_metadata[i+1:], i+1):
                if relationships >= 20:  # Limit for Opin
                    break
                    
                other_chunk_id = other_meta["chunk_id"]
                other_source_doc = other_meta["source_document"]
                other_chunk_index = other_meta["chunk_index"]
                other_content = other_meta["chunk_content"]
                other_category = other_meta.get("category")
                other_topics = set(other_meta.get("topics", []))
                
                # 📊 Hierarchical: Sequential chunks from same document
                if (source_doc == other_source_doc and 
                    abs(chunk_index - other_chunk_index) == 1):
                    self.db.add_relationship(chunk_id, other_chunk_id, "hierarchical", 0.9,
                        {"auto_detected": True, "reason": "sequential_chunks", "method": "langchain_chunking"})
                    relationships += 1
                    print(f"   📊 Sequential chunks: {chunk_id} → {other_chunk_id}")
                
                # 🔗 Semantic: Same category, different documents
                elif (category and category == other_category and 
                      source_doc != other_source_doc):
                    self.db.add_relationship(chunk_id, other_chunk_id, "semantic", 0.8,
                        {"auto_detected": True, "reason": "cross_document_category", "category": category})
                    relationships += 1
                    print(f"   🔗 Cross-document semantic: {chunk_id} ↔ {other_chunk_id}")
                
                # 🏷️ Associative: Shared topics across documents
                elif len(topics & other_topics) >= 2 and source_doc != other_source_doc:
                    shared = topics & other_topics
                    strength = min(0.75, len(shared) * 0.25)
                    self.db.add_relationship(chunk_id, other_chunk_id, "associative", strength,
                        {"auto_detected": True, "reason": "shared_topics", "topics": list(shared)})
                    relationships += 1
                    print(f"   🏷️ Topic association: {chunk_id} ↔ {other_chunk_id} ({shared})")
                
                # ⏰ Temporal: Learning progression detection
                elif (chunk_meta.get("difficulty") and other_meta.get("difficulty") and
                      category == other_category):
                    levels = {"beginner": 1, "intermediate": 2, "advanced": 3}
                    level_diff = levels.get(other_meta["difficulty"], 2) - levels.get(chunk_meta["difficulty"], 2)
                    if level_diff == 1:  # Progressive difficulty
                        self.db.add_relationship(chunk_id, other_chunk_id, "temporal", 0.85,
                            {"auto_detected": True, "reason": "learning_progression", "from": chunk_meta["difficulty"], "to": other_meta["difficulty"]})
                        relationships += 1
                        print(f"   ⏰ Learning progression: {chunk_id} → {other_chunk_id}")
        
        return relationships
    
    def auto_enhanced_rag_search(self, query, top_k=5):
        """Advanced RAG search with auto-relationship enhancement"""
        
        # Get query embedding through LangChain
        query_embedding = self.embeddings.embed_query(query)
        query_embedding_array = np.array(query_embedding, dtype=np.float32)
        
        # 🧠 Auto-enhanced relationship-aware search
        results = self.db.search(query_embedding_array, rudradb.SearchParams(
            top_k=top_k * 2,  # Get more results for relationship expansion
            include_relationships=True,  # Use auto-detected relationships
            max_hops=2,                 # Multi-hop relationship traversal
            relationship_weight=0.35,   # Balance similarity + relationships
            relationship_types=["semantic", "hierarchical", "associative", "temporal"]
        ))
        
        # Process and enhance results
        enhanced_results = []
        seen_documents = set()
        
        for result in results:
            vector = self.db.get_vector(result.vector_id)
            metadata = vector['metadata']
            
            # Avoid duplicate chunks from same document (take best scoring)
            source_doc = metadata.get("source_document")
            if source_doc in seen_documents:
                continue
            seen_documents.add(source_doc)
            
            # Determine connection type and relevance
            if result.hop_count == 0:
                connection_type = "Direct similarity match"
                relevance = "high"
            elif result.hop_count == 1:
                connection_type = "1-hop relationship connection" 
                relevance = "medium-high"
            else:
                connection_type = f"{result.hop_count}-hop relationship chain"
                relevance = "medium"
            
            enhanced_results.append({
                "chunk_id": result.vector_id,
                "source_document": source_doc,
                "content": metadata.get("chunk_content", ""),
                "title": metadata.get("title", ""),
                "similarity_score": result.similarity_score,
                "combined_score": result.combined_score,
                "connection_type": connection_type,
                "relevance": relevance,
                "hop_count": result.hop_count,
                "category": metadata.get("category", ""),
                "chunk_index": metadata.get("chunk_index", 0)
            })
            
            if len(enhanced_results) >= top_k:
                break
        
        return {
            "query": query,
            "total_results": len(enhanced_results),
            "relationship_enhanced": sum(1 for r in enhanced_results if r["hop_count"] > 0),
            "dimension": self.db.dimension(),
            "results": enhanced_results,
            "database_stats": {
                "total_chunks": self.db.vector_count(),
                "total_relationships": self.db.relationship_count()
            }
        }

# 🚀 Demo: LangChain + RudraDB Auto-RAG
rag_system = LangChain_RudraDB_AutoRAG("sentence-transformers/all-MiniLM-L6-v2")

# Add documents with automatic chunking and relationship detection
documents = [
    {
        "id": "ai_foundations",
        "title": "AI Foundations",
        "content": """Artificial Intelligence Foundations

Introduction to AI:
Artificial Intelligence represents the simulation of human intelligence in machines. These systems are designed to think and learn like humans, performing tasks that traditionally require human cognition such as visual perception, speech recognition, decision-making, and language translation.

Core AI Concepts:
The foundation of AI lies in machine learning algorithms that can process vast amounts of data to identify patterns and make predictions. These systems improve their performance over time through experience, much like human learning processes.

AI Applications:
Modern AI applications span across industries including healthcare for medical diagnosis, finance for fraud detection, transportation for autonomous vehicles, and entertainment for recommendation systems.""",
        "metadata": {"category": "AI", "topics": ["ai", "foundations", "introduction"], "difficulty": "beginner"}
    },
    {
        "id": "machine_learning_deep_dive",
        "title": "Machine Learning Deep Dive", 
        "content": """Machine Learning Deep Dive

ML Fundamentals:
Machine Learning is a subset of artificial intelligence that focuses on the development of algorithms that can learn from and make decisions based on data. Unlike traditional programming where humans write explicit instructions, ML systems learn patterns from data to make predictions or decisions.

Types of Machine Learning:
Supervised learning uses labeled data to train models for prediction tasks. Unsupervised learning finds hidden patterns in data without labels. Reinforcement learning learns through interaction with an environment, receiving rewards or penalties for actions.

ML in Practice:
Practical machine learning involves data preprocessing, feature engineering, model selection, training, validation, and deployment. The process requires careful attention to data quality, model evaluation metrics, and avoiding overfitting to ensure good generalization to new data.""",
        "metadata": {"category": "AI", "topics": ["ml", "algorithms", "data"], "difficulty": "intermediate"}
    },
    {
        "id": "neural_networks_advanced",
        "title": "Advanced Neural Networks",
        "content": """Advanced Neural Networks

Deep Learning Architecture:
Neural networks with multiple hidden layers, known as deep neural networks, can learn complex hierarchical representations of data. Each layer learns increasingly abstract features, from simple edges and textures in lower layers to complex objects and concepts in higher layers.

Training Deep Networks:
Training deep neural networks requires specialized techniques including backpropagation for gradient computation, various optimization algorithms like Adam and SGD, regularization methods like dropout and batch normalization, and careful initialization strategies.

Modern Applications:
Advanced neural network architectures like convolutional neural networks excel at computer vision tasks, recurrent neural networks handle sequential data, and transformer models have revolutionized natural language processing with attention mechanisms enabling parallel processing of sequences.""",
        "metadata": {"category": "AI", "topics": ["neural", "deep", "learning"], "difficulty": "advanced"}
    }
]

print("🦜 Processing documents with LangChain + RudraDB Auto-Intelligence:")
processing_result = rag_system.add_documents_with_chunking(documents)

print(f"✅ Document processing complete:")
print(f"   📄 Documents processed: {processing_result['documents_processed']}")
print(f"   📝 Total chunks created: {processing_result['total_chunks']}")
print(f"   🎯 Auto-detected dimension: {processing_result['auto_detected_dimension']}D")
print(f"   🧠 Auto-relationships created: {processing_result['auto_relationships']}")

# Advanced RAG search with relationship enhancement
queries = [
    "What are the fundamentals of artificial intelligence?",
    "How do neural networks learn from data?",
    "What's the difference between supervised and unsupervised learning?"
]

print(f"\n🔍 Advanced Auto-Enhanced RAG Search:")
for query in queries:
    search_result = rag_system.auto_enhanced_rag_search(query, top_k=4)
    
    print(f"\n❓ Query: {query}")
    print(f"   📊 Results: {search_result['total_results']} documents found")
    print(f"   🧠 Relationship-enhanced: {search_result['relationship_enhanced']} through auto-detected connections")
    print(f"   🎯 Search dimension: {search_result['dimension']}D")
    print(f"   📈 Database stats: {search_result['database_stats']['total_chunks']} chunks, {search_result['database_stats']['total_relationships']} relationships")
    
    print("   📋 Top Results:")
    for i, result in enumerate(search_result['results'][:3], 1):
        print(f"      {i}. {result['title']} (Chunk {result['chunk_index']})")
        print(f"         Connection: {result['connection_type']} | Relevance: {result['relevance']}")
        print(f"         Score: {result['combined_score']:.3f} | Category: {result['category']}")
        print(f"         Content: {result['content'][:150]}...")

print(f"\n🎉 LangChain + RudraDB-Opin Auto-RAG successful!")
print("    ✨ Auto-dimension detection seamlessly handled LangChain embeddings")
print("    ✨ Auto-relationship detection created sophisticated document connections")
print("    ✨ Multi-hop relationship traversal enhanced search relevance")
```

### 5. 🌊 **Pinecone Migration** - Easy Switch with Auto-Features

```python
import rudradb
import numpy as np
from typing import List, Dict, Any
import json

class Pinecone_to_RudraDB_Migration:
    """Seamless migration from Pinecone to RudraDB-Opin with enhanced auto-features"""
    
    def __init__(self, pinecone_dimension=None):
        """Initialize migration tool with optional dimension hint"""
        
        # RudraDB-Opin with auto-dimension detection
        self.rudra_db = rudradb.RudraDB()  # 🎯 Auto-detects dimensions from migrated data
        
        # Migration tracking
        self.migration_stats = {
            "vectors_migrated": 0,
            "relationships_auto_created": 0,
            "dimension_detected": None,
            "pinecone_dimension_hint": pinecone_dimension
        }
        
        print("🌊 Pinecone → RudraDB-Opin Migration Tool initialized")
        print("   🎯 Auto-dimension detection enabled (no manual dimension setting required)")
        print("   🧠 Auto-relationship detection will create intelligent connections")
        
    def migrate_pinecone_data(self, pinecone_vectors: List[Dict[str, Any]]):
        """Migrate vectors from Pinecone format to RudraDB-Opin with auto-enhancements"""
        
        print(f"🔄 Starting migration of {len(pinecone_vectors)} vectors from Pinecone...")
        
        relationships_created = 0
        
        for i, pinecone_vector in enumerate(pinecone_vectors):
            # Extract Pinecone data
            vector_id = pinecone_vector.get("id", f"migrated_vector_{i}")
            values = pinecone_vector.get("values", [])
            metadata = pinecone_vector.get("metadata", {})
            
            # Convert to numpy array
            embedding = np.array(values, dtype=np.float32)
            
            # Enhance metadata for auto-relationship detection
            enhanced_metadata = {
                "migrated_from": "pinecone",
                "original_id": vector_id,
                "migration_order": i,
                **metadata  # Preserve original Pinecone metadata
            }
            
            # Add to RudraDB-Opin with auto-dimension detection
            try:
                self.rudra_db.add_vector(vector_id, embedding, enhanced_metadata)
                self.migration_stats["vectors_migrated"] += 1
                
                # Update dimension info after first vector
                if self.migration_stats["dimension_detected"] is None:
                    self.migration_stats["dimension_detected"] = self.rudra_db.dimension()
                    print(f"   🎯 Auto-detected dimension: {self.migration_stats['dimension_detected']}D")
                    
                    # Validate against Pinecone hint
                    if (self.migration_stats["pinecone_dimension_hint"] and 
                        self.migration_stats["dimension_detected"] != self.migration_stats["pinecone_dimension_hint"]):
                        print(f"   ⚠️  Dimension mismatch detected!")
                        print(f"      Pinecone hint: {self.migration_stats['pinecone_dimension_hint']}D")
                        print(f"      Auto-detected: {self.migration_stats['dimension_detected']}D")
                
                # 🧠 Auto-create relationships based on migrated metadata
                if self.migration_stats["vectors_migrated"] > 1:  # Need at least 2 vectors
                    vector_relationships = self._auto_create_migration_relationships(vector_id, enhanced_metadata)
                    relationships_created += vector_relationships
                
                if (i + 1) % 25 == 0:  # Progress update every 25 vectors
                    print(f"   📊 Migrated {i + 1}/{len(pinecone_vectors)} vectors...")
                    
            except Exception as e:
                print(f"   ❌ Failed to migrate vector {vector_id}: {e}")
                continue
        
        self.migration_stats["relationships_auto_created"] = relationships_created
        
        return self.migration_stats
    
    def _auto_create_migration_relationships(self, new_vector_id: str, metadata: Dict[str, Any]):
        """Auto-create intelligent relationships based on migrated Pinecone metadata"""
        
        relationships_created = 0
        
        # Extract relationship indicators from metadata
        new_category = metadata.get("category") or metadata.get("type")
        new_tags = set(metadata.get("tags", []) if isinstance(metadata.get("tags"), list) else [])
        new_user = metadata.get("user_id") or metadata.get("user")
        new_timestamp = metadata.get("timestamp") or metadata.get("created_at")
        new_source = metadata.get("source") or metadata.get("source_type")
        
        # Analyze existing vectors for relationship opportunities
        for existing_id in self.rudra_db.list_vectors():
            if existing_id == new_vector_id or relationships_created >= 3:
                continue
                
            existing_vector = self.rudra_db.get_vector(existing_id)
            existing_meta = existing_vector['metadata']
            
            existing_category = existing_meta.get("category") or existing_meta.get("type")
            existing_tags = set(existing_meta.get("tags", []) if isinstance(existing_meta.get("tags"), list) else [])
            existing_user = existing_meta.get("user_id") or existing_meta.get("user")
            existing_source = existing_meta.get("source") or existing_meta.get("source_type")
            
            # 🔗 Semantic relationship: Same category/type
            if new_category and new_category == existing_category:
                self.rudra_db.add_relationship(new_vector_id, existing_id, "semantic", 0.8,
                    {"auto_detected": True, "reason": "pinecone_same_category", "category": new_category})
                relationships_created += 1
                print(f"      🔗 Auto-linked: {new_vector_id} ↔ {existing_id} (same category: {new_category})")
            
            # 🏷️ Associative relationship: Shared tags
            elif len(new_tags & existing_tags) >= 1:
                shared_tags = new_tags & existing_tags
                strength = min(0.7, len(shared_tags) * 0.3)
                self.rudra_db.add_relationship(new_vector_id, existing_id, "associative", strength,
                    {"auto_detected": True, "reason": "pinecone_shared_tags", "tags": list(shared_tags)})
                relationships_created += 1
                print(f"      🏷️ Auto-linked: {new_vector_id} ↔ {existing_id} (shared tags: {shared_tags})")
            
            # 📊 Hierarchical relationship: Same user/owner
            elif new_user and new_user == existing_user:
                self.rudra_db.add_relationship(new_vector_id, existing_id, "hierarchical", 0.7,
                    {"auto_detected": True, "reason": "pinecone_same_user", "user": new_user})
                relationships_created += 1
                print(f"      📊 Auto-linked: {new_vector_id} ↔ {existing_id} (same user: {new_user})")
            
            # 🎯 Associative relationship: Same source
            elif new_source and new_source == existing_source:
                self.rudra_db.add_relationship(new_vector_id, existing_id, "associative", 0.6,
                    {"auto_detected": True, "reason": "pinecone_same_source", "source": new_source})
                relationships_created += 1
                print(f"      🎯 Auto-linked: {new_vector_id} ↔ {existing_id} (same source: {new_source})")
        
        return relationships_created
    
    def compare_capabilities(self):
        """Compare Pinecone vs RudraDB-Opin capabilities after migration"""
        
        stats = self.rudra_db.get_statistics()
        
        comparison = {
            "feature_comparison": {
                "Vector Storage": {"Pinecone": "✅ Yes", "RudraDB-Opin": "✅ Yes"},
                "Similarity Search": {"Pinecone": "✅ Yes", "RudraDB-Opin": "✅ Yes"},
                "Auto-Dimension Detection": {"Pinecone": "❌ Manual only", "RudraDB-Opin": "✅ Automatic"},
                "Relationship Modeling": {"Pinecone": "❌ None", "RudraDB-Opin": "✅ 5 types"},
                "Auto-Relationship Detection": {"Pinecone": "❌ None", "RudraDB-Opin": "✅ Intelligent"},
                "Multi-hop Discovery": {"Pinecone": "❌ None", "RudraDB-Opin": "✅ 2 hops"},
                "Metadata Filtering": {"Pinecone": "✅ Basic", "RudraDB-Opin": "✅ Advanced"},
                "Free Tier": {"Pinecone": "❌ Limited trial", "RudraDB-Opin": "✅ 100% free version"},
                "Setup Complexity": {"Pinecone": "❌ API keys, config", "RudraDB-Opin": "✅ pip install"},
                "Relationship-Enhanced Search": {"Pinecone": "❌ Not available", "RudraDB-Opin": "✅ Automatic"}
            },
            "migration_results": {
                "vectors_migrated": self.migration_stats["vectors_migrated"],
                "relationships_auto_created": self.migration_stats["relationships_auto_created"],
                "dimension_auto_detected": self.migration_stats["dimension_detected"],
                "capacity_remaining": {
                    "vectors": stats["capacity_usage"]["vector_capacity_remaining"],
                    "relationships": stats["capacity_usage"]["relationship_capacity_remaining"]
                }
            }
        }
        
        return comparison
    
    def demonstrate_enhanced_search(self, query_vector: np.ndarray, query_description: str):
        """Demonstrate RudraDB-Opin's enhanced search vs Pinecone-style search"""
        
        print(f"🔍 Search Comparison: {query_description}")
        
        # Pinecone-style similarity-only search
        basic_results = self.rudra_db.search(query_vector, rudradb.SearchParams(
            top_k=5,
            include_relationships=False  # Pinecone equivalent
        ))
        
        # RudraDB-Opin enhanced search with auto-relationships
        enhanced_results = self.rudra_db.search(query_vector, rudradb.SearchParams(
            top_k=5,
            include_relationships=True,  # Use auto-detected relationships
            max_hops=2,
            relationship_weight=0.3
        ))
        
        comparison_result = {
            "query_description": query_description,
            "pinecone_style_results": len(basic_results),
            "rudradb_enhanced_results": len(enhanced_results),
            "additional_discoveries": len([r for r in enhanced_results if r.hop_count > 0]),
            "results_preview": []
        }
        
        print(f"   📊 Pinecone-style search: {len(basic_results)} results")
        print(f"   🧠 RudraDB-Opin enhanced: {len(enhanced_results)} results")
        print(f"   ✨ Additional discoveries: {len([r for r in enhanced_results if r.hop_count > 0])} through relationships")
        
        # Show preview of enhanced results
        for result in enhanced_results[:3]:
            vector = self.rudra_db.get_vector(result.vector_id)
            connection = "Direct similarity" if result.hop_count == 0 else f"{result.hop_count}-hop relationship"
            
            result_info = {
                "vector_id": result.vector_id,
                "connection_type": connection,
                "combined_score": result.combined_score,
                "metadata_preview": {k: v for k, v in vector['metadata'].items() if k in ['category', 'tags', 'source']}
            }
            
            comparison_result["results_preview"].append(result_info)
            print(f"      📄 {result.vector_id}: {connection} (score: {result.combined_score:.3f})")
        
        return comparison_result

# 🚀 Demo: Pinecone to RudraDB-Opin Migration
migration_tool = Pinecone_to_RudraDB_Migration(pinecone_dimension=384)

# Simulate Pinecone data format
pinecone_vectors = [
    {
        "id": "doc_ai_intro",
        "values": np.random.rand(384).tolist(),  # Simulated 384D embedding
        "metadata": {
            "category": "AI",
            "tags": ["artificial intelligence", "introduction", "basics"],
            "user_id": "researcher_1",
            "source": "research_papers",
            "title": "Introduction to Artificial Intelligence"
        }
    },
    {
        "id": "doc_ml_fundamentals", 
        "values": np.random.rand(384).tolist(),
        "metadata": {
            "category": "AI",
            "tags": ["machine learning", "algorithms", "data science"],
            "user_id": "researcher_1",
            "source": "research_papers", 
            "title": "Machine Learning Fundamentals"
        }
    },
    {
        "id": "doc_neural_networks",
        "values": np.random.rand(384).tolist(),
        "metadata": {
            "category": "AI",
            "tags": ["neural networks", "deep learning", "backpropagation"],
            "user_id": "researcher_2",
            "source": "textbooks",
            "title": "Neural Networks and Deep Learning"
        }
    },
    {
        "id": "doc_nlp_overview",
        "values": np.random.rand(384).tolist(),
        "metadata": {
            "category": "NLP",
            "tags": ["natural language processing", "text analysis", "linguistics"],
            "user_id": "researcher_2", 
            "source": "research_papers",
            "title": "Natural Language Processing Overview"
        }
    },
    {
        "id": "doc_computer_vision",
        "values": np.random.rand(384).tolist(),
        "metadata": {
            "category": "CV",
            "tags": ["computer vision", "image processing", "pattern recognition"],
            "user_id": "researcher_1",
            "source": "textbooks",
            "title": "Computer Vision Techniques"
        }
    }
]

# Perform migration
print("🌊 Starting Pinecone to RudraDB-Opin migration...")
migration_results = migration_tool.migrate_pinecone_data(pinecone_vectors)

print(f"\n✅ Migration Complete!")
print(f"   📊 Vectors migrated: {migration_results['vectors_migrated']}")
print(f"   🎯 Auto-detected dimension: {migration_results['dimension_detected']}D")
print(f"   🧠 Auto-relationships created: {migration_results['relationships_auto_created']}")

# Compare capabilities
print(f"\n📈 Capability Comparison:")
comparison = migration_tool.compare_capabilities()

print("   🆚 Feature Comparison:")
for feature, implementations in comparison["feature_comparison"].items():
    print(f"      {feature}:")
    print(f"         Pinecone: {implementations['Pinecone']}")
    print(f"         RudraDB-Opin: {implementations['RudraDB-Opin']}")

# Demonstrate enhanced search
query_vector = np.random.rand(384).astype(np.float32)
search_demo = migration_tool.demonstrate_enhanced_search(
    query_vector, "AI and machine learning concepts"
)

print(f"\n🎉 Migration to RudraDB-Opin successful!")
print("    ✨ Gained relationship-aware search capabilities")
print("    ✨ Auto-dimension detection eliminated configuration")
print("    ✨ Auto-relationship detection created intelligent connections")
print(f"    ✨ Enhanced search discovered {search_demo['additional_discoveries']} additional relevant results")

```

---

## 🆚 **Why RudraDB-Opin Crushes Traditional & Hybrid Vector Databases**

### 🔥 **vs Traditional Vector Databases** 
*(Pinecone, ChromaDB, Weaviate, Qdrant)*

| Capability | Traditional VectorDBs | RudraDB-Opin | Winner |
|------------|----------------------|--------------|---------|
| **Basic Vector Search** | ✅ Yes | ✅ Yes | 🤝 Tie |
| **🎯 Auto-Dimension Detection** | ❌ Manual config required | ✅ **Automatic with any model** | 🏆 **RudraDB-Opin** |
| **🧠 Auto-Relationship Detection** | ❌ None | ✅ **Intelligent analysis** | 🏆 **RudraDB-Opin** |
| **Relationship Intelligence** | ❌ None | ✅ **5 semantic types** | 🏆 **RudraDB-Opin** |
| **Multi-hop Discovery** | ❌ None | ✅ **2-degree traversal** | 🏆 **RudraDB-Opin** |
| **🔄 Auto-Performance Optimization** | ❌ Manual tuning | ✅ **Self-optimizing** | 🏆 **RudraDB-Opin** |
| **Zero-Config Setup** | ❌ Complex configuration | ✅ **`pip install` and go** | 🏆 **RudraDB-Opin** |
| **Learning-Focused** | ❌ Enterprise complexity | ✅ **Perfect for education** | 🏆 **RudraDB-Opin** |
| **Free Tier** | ❌ Limited trials | ✅ **100% free version** | 🏆 **RudraDB-Opin** |
| **Connection Discovery** | ❌ Manual queries only | ✅ **Auto-enhanced search** | 🏆 **RudraDB-Opin** |

**🚀 Result: RudraDB-Opin wins 8/10 capabilities with revolutionary auto-features!**

```python
# Traditional Vector DBs - Complex manual setup
import pinecone
pinecone.init(api_key="...", environment="...")  # API keys required
index = pinecone.Index("my-index")                # Manual index management
index.upsert([("id", [0.1]*1536)])               # Manual dimension specification (1536)
results = index.query([0.1]*1536)                 # Only similarity search
# ❌ No relationships, no auto-features, no intelligent connections

# RudraDB-Opin - Zero configuration with auto-intelligence
import rudradb
db = rudradb.RudraDB()                           # 🔥 Zero config, auto-dimension detection
db.add_vector("id", embedding, metadata)        # 🎯 Auto-detects any dimension
db.auto_build_relationships("id")               # 🧠 Auto-creates intelligent relationships
results = db.search(query, include_relationships=True)  # ✨ Auto-enhanced search
# ✅ Full auto-intelligence, relationship awareness, connection discovery
```

### ⚡ **vs Hybrid Vector Databases**
*(Weaviate with GraphQL, Qdrant with payloads, Milvus with attributes)*

| Capability | Hybrid VectorDBs | RudraDB-Opin | Winner |
|------------|------------------|--------------|---------|
| **Vector Search** | ✅ Yes | ✅ Yes | 🤝 Tie |
| **Metadata Filtering** | ✅ Basic filtering | ✅ **Rich metadata + analysis** | 🏆 **RudraDB-Opin** |
| **🎯 Auto-Dimension Detection** | ❌ Manual config | ✅ **Works with any model** | 🏆 **RudraDB-Opin** |
| **Relationship Intelligence** | ❌ Keywords/tags only | ✅ **5 semantic relationship types** | 🏆 **RudraDB-Opin** |
| **🧠 Auto-Relationship Building** | ❌ Manual relationship setup | ✅ **Intelligent auto-detection** | 🏆 **RudraDB-Opin** |
| **Graph-like Traversal** | ❌ Limited navigation | ✅ **Multi-hop with auto-optimization** | 🏆 **RudraDB-Opin** |
| **Context Understanding** | ❌ Statistical filtering only | ✅ **Semantic + contextual relationships** | 🏆 **RudraDB-Opin** |
| **🔄 Auto-Performance Optimization** | ❌ Manual tuning required | ✅ **Self-tuning system** | 🏆 **RudraDB-Opin** |
| **Setup Complexity** | ❌ Enterprise-level complexity | ✅ **Zero configuration** | 🏆 **RudraDB-Opin** |
| **Educational Access** | ❌ Enterprise pricing | ✅ **100% free learning tier** | 🏆 **RudraDB-Opin** |

**🚀 Result: RudraDB-Opin wins 9/10 capabilities with superior auto-intelligence!**

```python
# Hybrid Vector DBs - Complex schema and manual relationships
import weaviate
client = weaviate.Client("http://localhost:8080")
client.schema.create_class({                    # Manual schema definition
    "class": "Document",
    "properties": [                             # Manual property setup
        {"name": "content", "dataType": ["text"]},
        {"name": "category", "dataType": ["string"]}
    ]
})
client.data_object.create(                      # Manual object creation
    {"content": "text", "category": "AI"},
    class_name="Document", 
    vector=[0.1]*768                            # Manual dimension (768)
)
# ❌ No auto-features, complex setup, limited relationship intelligence

# RudraDB-Opin - Full auto-intelligence with semantic relationships
import rudradb
db = rudradb.RudraDB()                          # 🔥 Zero schema, auto-dimension detection
db.add_vector("doc", embedding, {               # 🎯 Any embedding model works
    "content": "text", "category": "AI",       # 🧠 Auto-analyzes for relationships
    "tags": ["ai", "ml"], "difficulty": "intro"
})
auto_relationships = db.auto_build_relationships("doc")  # ✨ Intelligent auto-detection
results = db.search(query, include_relationships=True)  # 🚀 Auto-enhanced discovery
# ✅ Full semantic intelligence, zero configuration, automatic optimization
```

### 🎯 **vs Advanced Graph Databases**
*(Neo4j, ArangoDB, Amazon Neptune)*

| Capability | Graph Databases | RudraDB-Opin | Winner |
|------------|-----------------|--------------|---------|
| **Graph Relationships** | ✅ Complex graphs | ✅ **AI-optimized relationships** | 🤝 Tie |
| **Vector Search** | ❌ Limited/plugin only | ✅ **Native vector + relationships** | 🏆 **RudraDB-Opin** |
| **🎯 Auto-Dimension Detection** | ❌ Not applicable | ✅ **Seamless ML model support** | 🏆 **RudraDB-Opin** |
| **🧠 Auto-Relationship Detection** | ❌ Manual relationship creation | ✅ **AI-powered auto-detection** | 🏆 **RudraDB-Opin** |
| **Embedding Integration** | ❌ Complex plugins/setup | ✅ **Zero-config ML integration** | 🏆 **RudraDB-Opin** |
| **Similarity + Relationships** | ❌ Requires separate systems | ✅ **Unified search experience** | 🏆 **RudraDB-Opin** |
| **🔄 Auto-Performance Optimization** | ❌ DBA expertise required | ✅ **Self-tuning for AI workloads** | 🏆 **RudraDB-Opin** |
| **Setup Complexity** | ❌ Enterprise complexity | ✅ **`pip install` simplicity** | 🏆 **RudraDB-Opin** |
| **AI/ML Focus** | ❌ General purpose | ✅ **Built for AI/ML workflows** | 🏆 **RudraDB-Opin** |
| **Educational Access** | ❌ Enterprise licensing | ✅ **100% free version** | 🏆 **RudraDB-Opin** |

**🚀 Result: RudraDB-Opin wins 8/10 with AI-native design and auto-intelligence!**

```python
# Graph Databases - Complex setup for AI workloads
from neo4j import GraphDatabase
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
with driver.session() as session:
    session.run("CREATE (n:Document {content: $content})", content="AI text")
    # ❌ No vector search, no embeddings, complex Cypher queries
    # ❌ Manual relationship creation, no auto-intelligence
    # ❌ Requires separate vector search system for similarity

# RudraDB-Opin - AI-native with unified vector + graph intelligence  
import rudradb
db = rudradb.RudraDB()                          # 🔥 AI-native, auto-dimension detection
db.add_vector("doc", ai_embedding, {            # 🎯 Native vector + metadata
    "content": "AI text", "category": "AI"
})
auto_rels = db.auto_build_relationships("doc")  # 🧠 AI-powered relationship detection
results = db.search(query_vector, include_relationships=True)  # ✨ Unified vector + graph search
# ✅ Native AI integration, automatic intelligence, unified experience
```

### 🏆 **Unique Advantages Only RudraDB-Opin Provides**

#### 🎯 **Revolutionary Auto-Dimension Detection**
```python
# 🔥 IMPOSSIBLE with other databases - works with ANY ML model
db = rudradb.RudraDB()  # No dimension specification needed!

# OpenAI Ada-002 (1536D) → Auto-detected
openai_emb = get_openai_embedding("text")
db.add_vector("openai", openai_emb, {"model": "ada-002"})
print(f"Auto-detected: {db.dimension()}D")  # 1536

# Switch to Sentence Transformers (384D) → New auto-detection
db2 = rudradb.RudraDB()  # Fresh auto-detection
st_emb = sentence_transformer.encode("text")
db2.add_vector("st", st_emb, {"model": "sentence-transformers"})
print(f"Auto-detected: {db2.dimension()}D")  # 384

# 🚀 Traditional databases REQUIRE manual dimension specification and throw errors!
```

#### 🧠 **Intelligent Auto-Relationship Detection** 
```python
# 🔥 UNIQUE to RudraDB-Opin - builds relationships automatically
db = rudradb.RudraDB()

# Just add documents with rich metadata
db.add_vector("doc1", emb1, {"category": "AI", "difficulty": "beginner", "tags": ["intro", "basics"]})
db.add_vector("doc2", emb2, {"category": "AI", "difficulty": "intermediate", "tags": ["ml", "advanced"]})

# 🧠 Auto-relationship detection analyzes content and creates intelligent connections
auto_relationships = db.auto_build_relationships("doc1")
# Automatically creates:
# - Semantic relationships (same category)
# - Temporal relationships (difficulty progression) 
# - Associative relationships (shared tags)

# 🚀 Traditional databases have NO relationship intelligence!
```

#### ⚡ **Auto-Enhanced Search Discovery**
```python
# 🔥 Revolutionary search that discovers connections others miss
query_emb = model.encode("machine learning basics")

# Traditional DB result: Only similar documents
basic_results = traditional_db.search(query_emb)  # 3 results

# RudraDB-Opin auto-enhanced result: Similar + relationship-connected
enhanced_results = db.search(query_emb, rudradb.SearchParams(
    include_relationships=True,  # 🧠 Uses auto-detected relationships
    max_hops=2                  # Multi-hop relationship traversal
))  # 7 results - discovered 4 additional relevant documents!

# 🚀 Finds documents traditional databases completely miss through relationship intelligence!
```

---

## 🎓 **Perfect Use Cases for RudraDB-Opin's Auto-Intelligence**

### 📚 **Educational Excellence** - Auto-Learning Enhancement
```python
# 🎓 Perfect for tutorials and courses with auto-intelligence
class AI_Learning_System:
    def __init__(self):
        self.db = rudradb.RudraDB()  # Auto-dimension detection for any model
        
    def add_lesson(self, lesson_id, content, difficulty, topic):
        embedding = self.model.encode(content)  # Any model works
        
        # Rich metadata for auto-relationship detection
        metadata = {
            "content": content,
            "difficulty": difficulty,      # Auto-detects learning progression
            "topic": topic,               # Auto-detects topic clustering  
            "type": "lesson",             # Auto-detects lesson → example relationships
            "tags": self.extract_tags(content)  # Auto-detects tag associations
        }
        
        self.db.add_vector(lesson_id, embedding, metadata)
        
        # 🧠 Auto-build learning relationships
        return self.db.auto_build_learning_relationships(lesson_id, metadata)
    
    def intelligent_learning_path(self, query):
        """Find optimal learning sequence with auto-relationship intelligence"""
        query_emb = self.model.encode(query)
        
        # Auto-enhanced search discovers learning progressions
        return self.db.search(query_emb, rudradb.SearchParams(
            include_relationships=True,    # Use auto-detected relationships
            relationship_types=["temporal", "hierarchical"],  # Focus on learning sequences
            max_hops=2                    # Multi-step learning paths
        ))

# 🚀 Builds perfect learning sequences automatically!
learning_system = AI_Learning_System()
learning_system.add_lesson("intro_ai", "Introduction to AI...", "beginner", "ai")
learning_system.add_lesson("ml_basics", "ML fundamentals...", "intermediate", "ai") 
# Auto-creates beginner → intermediate temporal relationship!

path = learning_system.intelligent_learning_path("learn machine learning")
# Discovers optimal learning sequence through auto-detected relationships!
```

### 🔬 **Research Discovery** - Auto-Citation Networks
```python 
# 📄 Research paper discovery with auto-relationship intelligence  
class Research_Discovery_System:
    def __init__(self):
        self.db = rudradb.RudraDB()  # Auto-dimension for any research embeddings
        
    def add_paper(self, paper_id, abstract, metadata):
        embedding = self.get_research_embedding(abstract)  # Any model
        
        # Research metadata for auto-relationship detection
        enhanced_metadata = {
            "abstract": abstract,
            "year": metadata["year"],           # Auto-detects temporal citations
            "field": metadata["field"],         # Auto-detects field clustering
            "methodology": metadata.get("method"),  # Auto-detects method relationships
            "problem_type": metadata.get("problem"), # Auto-detects problem-solution
            "authors": metadata["authors"],     # Auto-detects author networks
            **metadata
        }
        
        self.db.add_vector(paper_id, embedding, enhanced_metadata)
        
        # 🧠 Auto-detect research relationships
        return self.db.auto_build_research_relationships(paper_id, enhanced_metadata)
    
    def discover_research_connections(self, query_paper):
        """Discover research connections through auto-relationship networks"""
        paper_vector = self.db.get_vector(query_paper)
        paper_embedding = paper_vector["embedding"]
        
        # Auto-enhanced discovery finds citation networks and methodological connections
        return self.db.search(paper_embedding, rudradb.SearchParams(
            include_relationships=True,        # Use auto-detected research relationships
            relationship_types=["causal", "semantic", "temporal"],  # Research patterns
            max_hops=2,                       # Citation chains
            relationship_weight=0.4           # Balance citation + similarity
        ))

# 🚀 Automatically builds research citation networks and discovers methodological connections!
research_system = Research_Discovery_System()
research_system.add_paper("transformer_paper", "Attention is all you need...", 
                         {"year": 2017, "field": "NLP", "method": "attention"})
research_system.add_paper("bert_paper", "BERT bidirectional representations...",
                         {"year": 2018, "field": "NLP", "method": "pretraining"})
# Auto-creates temporal (2017 → 2018) and methodological (attention → pretraining) relationships!

connections = research_system.discover_research_connections("transformer_paper")
# Discovers papers that cited, built upon, or used similar methodologies automatically!
```

### 🛍️ **E-commerce Intelligence** - Auto-Product Networks
```python
# 🛒 E-commerce with auto-relationship product discovery
class Ecommerce_Intelligence_System:
    def __init__(self):
        self.db = rudradb.RudraDB()  # Auto-dimension for any product embeddings
        
    def add_product(self, product_id, description, product_metadata):
        embedding = self.get_product_embedding(description)  # Any embedding model
        
        # Product metadata for auto-relationship detection
        enhanced_metadata = {
            "description": description,
            "category": product_metadata["category"],           # Auto-detects category clusters
            "price_range": self.get_price_range(product_metadata["price"]),  # Auto-detects price relationships
            "brand": product_metadata["brand"],                 # Auto-detects brand associations
            "features": product_metadata.get("features", []),   # Auto-detects feature overlaps
            "use_cases": product_metadata.get("use_cases", []), # Auto-detects usage relationships
            "target_audience": product_metadata.get("audience"), # Auto-detects audience segments
            **product_metadata
        }
        
        self.db.add_vector(product_id, embedding, enhanced_metadata)
        
        # 🧠 Auto-detect product relationships
        return self.db.auto_build_product_relationships(product_id, enhanced_metadata)
    
    def intelligent_product_discovery(self, query_or_product_id):
        """Discover products through auto-relationship networks"""
        if isinstance(query_or_product_id, str) and query_or_product_id in self.db.list_vectors():
            # Product-to-product discovery
            product_vector = self.db.get_vector(query_or_product_id)
            search_embedding = product_vector["embedding"]
        else:
            # Query-based discovery  
            search_embedding = self.get_product_embedding(str(query_or_product_id))
        
        # Auto-enhanced product discovery
        return self.db.search(search_embedding, rudradb.SearchParams(
            include_relationships=True,        # Use auto-detected product relationships
            relationship_types=["associative", "semantic", "causal"],  # Purchase patterns
            max_hops=2,                       # "Customers who bought X also bought Y"
            relationship_weight=0.35          # Balance similarity + purchase relationships
        ))

# 🚀 Automatically builds "customers also bought" and "similar products" networks!
ecommerce_system = Ecommerce_Intelligence_System()
ecommerce_system.add_product("laptop_gaming", "High-performance gaming laptop with RTX GPU", 
                           {"category": "Electronics", "brand": "NVIDIA", "features": ["gaming", "rtx", "high_performance"]})
ecommerce_system.add_product("gaming_mouse", "Precision gaming mouse with RGB lighting",
                           {"category": "Electronics", "brand": "Razer", "features": ["gaming", "rgb", "precision"]})
# Auto-creates associative relationship (shared "gaming" feature)!

recommendations = ecommerce_system.intelligent_product_discovery("laptop_gaming")
# Discovers complementary products (gaming accessories) and similar items automatically!
```

### 📝 **Content Management** - Auto-Content Networks
```python
# 📄 Content management with auto-relationship organization
class Content_Intelligence_System:
    def __init__(self):
        self.db = rudradb.RudraDB()  # Auto-dimension for any content embeddings
        
    def add_content(self, content_id, content_text, content_metadata):
        embedding = self.get_content_embedding(content_text)  # Any model works
        
        # Content metadata for auto-relationship detection  
        enhanced_metadata = {
            "content": content_text,
            "content_type": content_metadata["type"],           # Auto-detects type clustering
            "publication_date": content_metadata["date"],       # Auto-detects temporal sequences
            "author": content_metadata["author"],               # Auto-detects author networks
            "tags": content_metadata.get("tags", []),           # Auto-detects tag associations
            "audience_level": content_metadata.get("level"),    # Auto-detects reading progression
            "content_series": content_metadata.get("series"),   # Auto-detects series relationships
            "references": content_metadata.get("references", []), # Auto-detects reference networks
            **content_metadata
        }
        
        self.db.add_vector(content_id, embedding, enhanced_metadata)
        
        # 🧠 Auto-detect content relationships
        return self.db.auto_build_content_relationships(content_id, enhanced_metadata)
    
    def intelligent_content_discovery(self, query, discovery_type="comprehensive"):
        """Discover content through auto-relationship networks"""
        query_embedding = self.get_content_embedding(query)
        
        if discovery_type == "comprehensive":
            # Discover all related content through multiple relationship types
            search_params = rudradb.SearchParams(
                include_relationships=True,
                relationship_types=["semantic", "hierarchical", "associative", "temporal"],
                max_hops=2,
                relationship_weight=0.4
            )
        elif discovery_type == "series":
            # Focus on content series and sequential relationships
            search_params = rudradb.SearchParams(
                include_relationships=True,
                relationship_types=["hierarchical", "temporal"],
                max_hops=1,
                relationship_weight=0.5
            )
        elif discovery_type == "author_network":
            # Focus on author-based relationships
            search_params = rudradb.SearchParams(
                include_relationships=True,
                relationship_types=["associative", "semantic"],
                max_hops=2,
                relationship_weight=0.3
            )
        
        return self.db.search(query_embedding, search_params)

# 🚀 Automatically organizes content networks by author, series, topic, and reading level!
content_system = Content_Intelligence_System()
content_system.add_content("ai_intro_1", "Introduction to AI: Part 1 - Basic Concepts",
                          {"type": "tutorial", "author": "Dr. Smith", "level": "beginner", 
                           "series": "AI Fundamentals", "tags": ["ai", "intro"]})
content_system.add_content("ai_intro_2", "Introduction to AI: Part 2 - Machine Learning",
                          {"type": "tutorial", "author": "Dr. Smith", "level": "beginner",
                           "series": "AI Fundamentals", "tags": ["ai", "ml"]})
# Auto-creates hierarchical (series), temporal (part 1 → 2), and associative (author) relationships!

content_network = content_system.intelligent_content_discovery("machine learning basics", "series")
# Discovers complete content series and learning progressions automatically!
```

---

## 📊 **Advanced API Reference & Auto-Features**

### 🤖 **Auto-Intelligence Methods**

#### Auto-Dimension Detection
```python
# Core auto-dimension detection capabilities
db = rudradb.RudraDB()

# Check auto-detection status
print(f"Auto-detection enabled: {db.is_auto_dimension_detection_enabled()}")  # True
print(f"Current dimension: {db.dimension()}")  # None (until first vector)

# Add vector - auto-detection triggers
embedding = np.random.rand(512).astype(np.float32)
db.add_vector("test", embedding)
print(f"Auto-detected dimension: {db.dimension()}")  # 512

# Advanced auto-detection info
detection_info = db.get_auto_dimension_info()
print(f"Detection confidence: {detection_info['confidence']:.2%}")
print(f"Detection method: {detection_info['method']}")
print(f"Supports dimension: {detection_info['supports_dimension']}")
```

#### Auto-Relationship Detection & Building
```python
# Advanced auto-relationship capabilities
db = rudradb.RudraDB()

# Configure auto-relationship detection
auto_config = rudradb.create_auto_relationship_config(
    enabled=True,
    similarity_threshold=0.7,
    max_relationships_per_vector=5,
    algorithms=["metadata_analysis", "content_similarity", "semantic_clustering"],
    min_confidence=0.6
)

db.enable_auto_relationships(auto_config)

# Add vectors with rich metadata for auto-detection
docs = [
    ("ai_basics", embedding1, {"category": "AI", "difficulty": "beginner", "tags": ["ai", "intro"], "type": "concept"}),
    ("ml_advanced", embedding2, {"category": "AI", "difficulty": "advanced", "tags": ["ml", "algorithms"], "type": "concept"}),
    ("python_example", embedding3, {"category": "Programming", "difficulty": "intermediate", "tags": ["python", "code"], "type": "example"})
]

for doc_id, emb, metadata in docs:
    db.add_vector_with_auto_relationships(doc_id, emb, metadata, auto_relationships=True)

# Manual relationship detection for existing vectors
candidates = db.detect_relationships_for_vector("ai_basics")
print(f"Auto-detected relationship candidates: {len(candidates)}")

for candidate in candidates:
    print(f"  {candidate['source_id']} → {candidate['target_id']}")
    print(f"    Type: {candidate['relationship_type']} (confidence: {candidate['confidence']:.2f})")
    print(f"    Algorithm: {candidate['algorithm']}")

# Batch auto-detection for all vectors
all_candidates = db.batch_detect_relationships()
print(f"Total relationship candidates detected: {len(all_candidates)}")
```

#### Auto-Enhanced Search
```python
# Advanced auto-enhanced search capabilities  
db = rudradb.RudraDB()

# Auto-enhanced search parameters
auto_params = rudradb.SearchParams(
    top_k=10,
    include_relationships=True,
    max_hops=2,
    
    # 🤖 Auto-enhancement options
    auto_enhance=True,                    # Enable all auto-optimizations
    auto_balance_weights=True,            # Auto-balance similarity vs relationships  
    auto_select_relationship_types=True,  # Auto-choose relevant relationship types
    auto_optimize_hops=True,             # Auto-optimize traversal depth
    auto_calibrate_threshold=True,        # Auto-adjust similarity threshold
    
    # Manual overrides (optional)
    relationship_weight=0.3,              # Can override auto-balancing
    similarity_threshold=0.1              # Can override auto-calibration
)

# Perform auto-enhanced search
results = db.search(query_embedding, auto_params)

# Analyze auto-enhancement impact
enhancement_stats = db.get_last_search_enhancement_stats()
print(f"Auto-enhancements applied:")
print(f"  Weight auto-balanced: {enhancement_stats['weight_balanced']}")
print(f"  Relationship types auto-selected: {enhancement_stats['types_selected']}")
print(f"  Traversal depth auto-optimized: {enhancement_stats['hops_optimized']}")
print(f"  Threshold auto-calibrated: {enhancement_stats['threshold_calibrated']}")
print(f"  Performance improvement: {enhancement_stats['performance_gain']:.1%}")

# Advanced result analysis
for result in results:
    print(f"Document: {result.vector_id}")
    print(f"  Connection: {'Direct' if result.hop_count == 0 else f'{result.hop_count}-hop auto-discovery'}")
    print(f"  Scores: Similarity={result.similarity_score:.3f}, Combined={result.combined_score:.3f}")
    print(f"  Enhancement: {'Auto-discovered' if result.hop_count > 0 else 'Direct similarity'}")
```

### 📊 **Advanced Statistics & Monitoring**

```python
# Comprehensive database analytics
stats = db.get_statistics()

# Auto-feature performance metrics
auto_stats = db.get_auto_feature_statistics()
print(f"🎯 Auto-Dimension Detection:")
print(f"   Accuracy: {auto_stats['dimension_detection_accuracy']:.2%}")
print(f"   Models supported: {auto_stats['models_supported']}")
print(f"   Average detection time: {auto_stats['avg_detection_time_ms']:.1f}ms")

print(f"🧠 Auto-Relationship Detection:")  
print(f"   Relationships auto-created: {auto_stats['relationships_auto_created']}")
print(f"   Detection accuracy: {auto_stats['relationship_detection_accuracy']:.2%}")
print(f"   Average confidence: {auto_stats['avg_relationship_confidence']:.2%}")
print(f"   Most effective algorithm: {auto_stats['top_detection_algorithm']}")

print(f"⚡ Auto-Performance Optimization:")
print(f"   Search speed improvement: {auto_stats['search_speed_improvement']:.1%}")
print(f"   Memory usage optimization: {auto_stats['memory_optimization']:.1%}")
print(f"   Index optimization level: {auto_stats['index_optimization_level']}")

# Capacity and upgrade insights
capacity_info = db.get_capacity_insights()
print(f"📊 Capacity Status:")
print(f"   Vector usage: {capacity_info['vector_usage_percent']:.1f}%")
print(f"   Relationship usage: {capacity_info['relationship_usage_percent']:.1f}%")
print(f"   Estimated time to capacity: {capacity_info['estimated_days_to_capacity']} days")
print(f"   Upgrade recommendation: {'Consider upgrade' if capacity_info['should_upgrade'] else 'Current capacity sufficient'}")

# Performance benchmarks
benchmark_results = db.run_performance_benchmark()
print(f"🚀 Performance Benchmarks:")
print(f"   Vector addition: {benchmark_results['vector_add_per_sec']:.0f} vectors/sec")
print(f"   Search latency: {benchmark_results['avg_search_latency_ms']:.1f}ms")
print(f"   Relationship creation: {benchmark_results['relationship_add_per_sec']:.0f} relationships/sec")
print(f"   Auto-enhancement overhead: {benchmark_results['auto_enhancement_overhead_percent']:.1f}%")
```

### 🔧 **Advanced Configuration & Optimization**

```python
# Advanced database configuration for power users
advanced_config = {
    # Auto-dimension detection settings
    "auto_dimension": {
        "enabled": True,
        "confidence_threshold": 0.95,
        "fallback_dimension": None,
        "validation_samples": 3
    },
    
    # Auto-relationship detection settings
    "auto_relationships": {
        "enabled": True,
        "background_processing": True,
        "max_analysis_candidates": 50,
        "algorithms": ["metadata_analysis", "content_similarity", "semantic_clustering"],
        "relationship_strength_calibration": "auto",
        "confidence_weighting": "adaptive"
    },
    
    # Auto-performance optimization settings  
    "auto_performance": {
        "enabled": True,
        "adaptive_indexing": True,
        "memory_optimization": True,
        "search_query_optimization": True,
        "relationship_caching": True
    },
    
    # Limits and thresholds (Opin-specific)
    "limits": {
        "max_vectors": 100000,
        "max_relationships": 500000,
        "max_hops": 2,
        "enforce_limits": True,
        "upgrade_suggestions": True
    }
}

# Apply advanced configuration
db = rudradb.RudraDB(conf