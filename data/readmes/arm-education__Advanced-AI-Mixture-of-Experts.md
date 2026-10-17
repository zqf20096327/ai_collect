![arm-education-logo](./Education_horizontal_violet.png)

# **Mixture of Experts: A Practical Course**

This course provides a hands-on introduction to Mixture of Experts (MoE) models through four progressive notebooks. Each notebook builds on the previous ones, taking you from theoretical understanding to practical implementation of advanced MoE concepts.



## Intended Audience


This course is designed for industry ML engineers who wish to gain hands-on experience with Mixture of Experts (MoE) models. It is also well-suited for ML researchers interested in exploring and experimenting with cutting‑edge methods for model compression and performance optimization.

Learners should be comfortable with the following

- **Deep learning architectures** — transformers, attention mechanisms, and feed-forward networks  
- **Training and optimization** — gradient descent variants, regularization, and overfitting control  
- **Practical skills** — Python programming experience and intermediate understanding of PyTorch  

Those who want to build or refresh these fundamentals can first complete introductory and intermediate material such as the [Intro to AI](https://www.edx.org/learn/computer-science/arm-education-introduction-to-ai) or [Optimizing Generative AI on Arm](https://www.edx.org/learn/computer-science/arm-education-ai-on-arm) course.


## Course Progression

1. **Theory to Practice** — start with computational benefits, end with advanced optimization  
2. **Building Blocks** — each notebook provides necessary components for the next  
3. **Progressive Complexity** — simple concepts build to sophisticated implementations  


## Requirements

- Python 3.8 or newer  
- PyTorch
- Transformers
- PyTorch backend to accelerate training (e.g., Google Colab T4 or A100) is **strongly recommended**


We recommend running these labs on Google Colab with T4 GPUs. All computations can be completed using the GPUs available in Colab.

You are expected to be familiar with configuring software across different operating systems, and you may need to install additional packages depending on your setup. Several commands in the labs reference tools specific to the Colab environment, so you may need to adapt them if you are working on another system, such as your own PC.

**We also provide links to saved checkpoints** for each training epoch, along with code examples for loading model weights from these checkpoints.

Finally, there are options to speed up computation. The dataset created in Part Two is quite large and contributes significantly to training and evaluation time. Using a smaller subset of the dataset can greatly reduce this overhead and may also offer an interesting comparative analysis of model accuracy.

---

## [Part One: MoE vs Dense Inference Comparison](https://colab.research.google.com/drive/12eg4PF_FBU9-RRkwO5eS2_rHE3x267lq?usp=sharing)

### Overview
The first notebook explores the computational advantages of MoE architectures compared to traditional dense models, with a focus on theoretical and practical efficiency metrics.

### Key Concepts
- **Conditional Computation**: MoE models only activate a subset of parameters for each input
- **Expert Specialization**: Different experts learn to handle different aspects of the input space
- **Computational Efficiency**:
  - Theoretical FLOP analysis based on model architecture
  - Impact of expert count and batch size on speedup
  - Memory efficiency through parameter sharing

### Implementation Highlights
```python
# Theoretical FLOP calculation
dense_flops = batch_size * seq_len * d_model * d_ff
moe_flops = batch_size * seq_len * (d_model * num_experts + d_ff)
speedup = dense_flops / moe_flops
```

### Performance Analysis
- **Architecture Impact**:
  - Varying fully connected layer sizes
  - Different expert counts
  - Batch size effects on throughput
- **Theoretical vs Actual Speedup**:
  - FLOP count comparison
  - Memory bandwidth considerations
  - Practical implementation overheads

### Learning Outcomes
- Understanding the computational benefits of MoE
- Measuring inference speed and memory usage
- Analyzing the impact of architectural choices
- Comparing theoretical and practical speedups

## [Part Two: Designing a Sentiment Detection Data Set for MoE](https://colab.research.google.com/drive/1qu8HFrgofMBgGMOEcZtrG6pQ2DuI7R_8?usp=drive_link)

### Key Components
- **Data Sources**:
  - Amazon product reviews
  - Yelp business reviews
  - IMDB movie reviews
- **Data Collection**: Gathering text from multiple domains
- **Preprocessing**: Tokenization and formatting
- **Domain Labeling**: Tracking data source for routing analysis


### Implementation Highlights
```python
# Combining multiple datasets
amazon_data = load_dataset("amazon_reviews_multi")
yelp_data = load_dataset("yelp_review_full")
imdb_data = load_dataset("imdb")

# Creating unified dataset with domain labels
combined_data = {
    "text": [...],
    "label": [...],
    "domain": ["amazon", "yelp", "imdb", ...]
}
```
```python
# Dataset structure
{
    "input_ids": tokenized_text,
    "attention_mask": padding_mask,
    "label": sentiment_class,
    "domain": data_source
}
```

### Learning Outcomes
- Creating domain-diverse datasets
- Implementing proper data preprocessing
- Understanding the importance of domain information

## [Part Three: Sentiment Detection Training](https://colab.research.google.com/drive/1PCDVnA-RfuhuqnCUuzRqdjVhM9LLu6Or?usp=sharing)

### Overview
We implement and train a transformer-based MoE model for sentiment analysis, focusing on the core architecture and training process.

### Key Components
- **Transformer Architecture**: Multi-head attention and feed-forward layers
- **MoE Implementation**: Expert routing and processing
- **Training Pipeline**: Optimization and evaluation

### Implementation Highlights
```python
class TransformerEncoder(nn.Module):
    def __init__(self, vocab_size, d_model=128, num_heads=4,
                 num_layers=2, num_experts=4):
        # Transformer with MoE layers
        self.layers = nn.ModuleList([
            TransformerBlock(use_moe=True, num_experts=num_experts)
            for _ in range(num_layers)
        ])
```

### Learning Outcomes
- Implementing transformer-based MoE
- Training and evaluating MoE models
- Understanding model architecture choices

## [Part Four: Routing and Load Balancing](https://colab.research.google.com/drive/1MoVqen8pbfRXIq3zqWMEaEtKJRM4s1Yi?usp=sharing)

### Overview
In this notebook we move to explore advanced MoE concepts, focusing on routing behavior and load balancing optimization.

### Key Investigations
1. **Gating Function Analysis**
   - Comparing learned vs. random routing
   - Measuring routing effectiveness

2. **Expert Specialization**
   - Computing expert similarity
   - Analyzing expert diversity

3. **Load Distribution**
   - Tracking expert utilization
   - Identifying routing imbalances

4. **Load Balancing Implementation**
   - Adding balancing loss
   - Fine-tuning for balanced routing

### Implementation Highlights
```python
class MoEFeedForwardBucketedWithLoadBalancing(nn.Module):
    def load_balancing_loss(self, gate_probs, expert_indices):
        expert_fraction = torch.bincount(expert_indices).float()
        expert_fraction = expert_fraction / expert_fraction.sum()
        mean_gate_probs = gate_probs.mean(dim=0)
        return torch.sum(expert_fraction * mean_gate_probs)
```

### Learning Outcomes
- Understanding routing behavior
- Implementing load balancing
- Optimizing expert utilization
- Maintaining accuracy while improving balance

## [Part Five: EM-Inspired Alternating Optimization for MoE](https://colab.research.google.com/drive/1D2-RlKNsIyhiEYJ6nSXX3JQAHbisL1mN?usp=sharing)

In our previous attempts, we faced a fundamental challenge: achieving both high accuracy and balanced expert utilization seemed mutually exclusive. Traditional approaches that tried to optimize both objectives simultaneously often led to suboptimal results, with the model either achieving good accuracy at the cost of imbalanced expert utilization, or vice versa.

### The EM-Inspired Solution

Drawing inspiration from the Expectation-Maximization (EM) algorithm, we developed a novel alternating optimization strategy that separates the training into two distinct phases:

1. **Expert Training Phase (E-step)**:
   - Freeze the routing mechanism (gate)
   - Allow experts to specialize in their assigned tokens
   - Focus solely on maximizing classification accuracy
   - This phase enables experts to develop deep, specialized knowledge

2. **Gate Training Phase (M-step)**:
   - Freeze the expert parameters
   - Train the routing mechanism to distribute tokens more evenly
   - Incorporate a sophisticated load balancing loss
   - This phase ensures fair utilization of all experts

### Key Innovations

1. **Alternating Training**:
   - Experts and gate are trained in alternating epochs
   - Each component gets dedicated time to optimize its specific objective
   - Prevents interference between accuracy and balancing goals

2. **Enhanced Load Balancing**:
   - KL divergence loss for uniform distribution
   - Stricter capacity constraints (0.8-1.2 of uniform)
   - Entropy regularization for gate probabilities
   - Multiple balancing terms work together synergistically

3. **Sophisticated Loss Function**:
   - Classification loss for accuracy
   - Load balancing loss only during gate training
   - Capacity constraints to prevent over/under utilization
   - Entropy regularization to encourage uniform routing

### Results and Analysis

The EM-inspired approach has shown remarkable success:
- Classification accuracy comparable to non-MoE models
- Even distribution of tokens across experts
- Stable training without the previous trade-offs
- Clear specialization of experts (as shown by low cosine similarities)

### Implementation Details

The implementation includes:
- Selective parameter freezing for alternating phases
- Comprehensive monitoring of both accuracy and balancing metrics
- Enhanced routing information tracking
- Sophisticated visualization tools for analysis

This approach represents a significant advancement in MoE training, demonstrating that it's possible to achieve both high accuracy and balanced expert utilization through careful architectural design and training strategy.

---

## Course Progression
1. **Theory to Practice**: Start with computational benefits, end with advanced optimization
2. **Building Blocks**: Each notebook provides necessary components for the next
3. **Progressive Complexity**: Simple concepts build to sophisticated implementations



## Getting Started
1. Install required packages
2. Follow notebooks in sequence
3. Experiment with different configurations
4. Analyze results and modify approaches

This course provides both theoretical understanding and practical implementation skills for working with MoE models in modern deep learning applications.

---


The original content was produced by [Professor Constantine Caramanis](http://users.ece.utexas.edu/~cmcaram/) at the University of Texas at Austin, in collaboration with Kieran Hejmadi from Arm Education.



---

## License
You are free to fork or clone this material. See `LICENSE.md` for the complete license.

## Inclusive Language Commitment
Arm is committed to making the language we use inclusive, meaningful, and respectful. Our goal is to remove and replace non-inclusive language from our vocabulary to reflect our values and represent our global ecosystem.
 
Arm is working actively with our partners, standards bodies, and the wider ecosystem to adopt a consistent approach to the use of inclusive language and to eradicate and replace offensive terms. We recognise that this will take time. This course may contain references to non-inclusive language; it will be updated with newer terms as those terms are agreed and ratified with the wider community. 
 
Contact us at education@arm.com with questions or comments about this course. You can also report non-inclusive and offensive terminology usage in Arm content at terms@arm.com.

---