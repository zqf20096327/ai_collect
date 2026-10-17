# Hands-On Labs for Neural Networks with PyTorch

This repository contains a series of hands-on labs for beginners in neural networks using PyTorch. The labs are designed to briefly cover various topics, including Maths basics, Python refresher, and neural network concepts.

## Getting Started

Lab 04 walks through installing Miniconda from scratch. If you already have it, this is the whole setup:

```bash
conda create -n envNeural python=3.12 -y
```

```bash
conda activate envNeural && pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu && pip install numpy matplotlib scikit-learn scipy pillow jupyter ipykernel
```

Labs 17-19 need a few extras — `onnx`, `onnxruntime` and `onnxscript` for the export section, and `transformers` for the retrieval labs:

```bash
conda activate envNeural && pip install onnx onnxruntime onnxscript transformers
```

Every lab runs on CPU. Labs 12 and 16 are noticeably faster on a GPU; if you have one, install the CUDA build of PyTorch instead of the `whl/cpu` index above. Datasets and pretrained weights download automatically on first run, into `./data` and the Hugging Face cache respectively.

## Topics Covered

### 1. Maths Basics
- Linear Algebra: Introduction to linear algebra concepts used in neural networks.
- Calculus: Exploring calculus concepts relevant to neural networks.

### 2. Python Refresher & Environment Setup
- Miniconda Installation and Environment Setup: Step-by-step guide for installing Miniconda and setting up the environment.
- Python Refresher: Implementation of Maths functions.
- PyTorch: Getting started with PyTorch library for neural networks development.

### 3. Neural Network Concepts
- Neurons and Activation Functions: Understanding the building blocks of neural networks.
- Forward and Back Propagation: Implementing forward and back propagation algorithms in neural networks.
- Dense Neural Networks: Building and training dense neural networks.
- Convolutional Neural Networks (CNN): Introduction to CNNs and their applications in computer vision tasks.
- Recurrent Neural Networks (RNN): Exploring RNNs and their ability to process sequential data.
- Long Short-Term Memory (LSTM): Understanding LSTM networks and their role in handling long-term dependencies.
- Transfer Learning: Leveraging pre-trained models for transfer learning in neural networks.

### 4. Advanced Topics
- Regularization and Optimization: Making networks generalise — dropout, weight decay, batch norm, augmentation, early stopping, optimizers and learning rate schedules.
- Attention and Transformers: The mechanism that replaced recurrence, built from scratch.
- Autoencoders and VAEs: Learning representations without labels, and generating from a latent space.
- Generative Adversarial Networks: Training two networks against each other to generate data.
- Deployment and Model Optimization: Taking a trained model out of the notebook — TorchScript, ONNX, quantization and serving.

### 5. Extra: Retrieval
- Embeddings and Semantic Search: Turning a pretrained Transformer into a search engine over your own text.
- Retrieval-Augmented Generation (RAG): Grounding a language model in your documents, with citations and refusals.

## Labs

### 1. Introduction to Neural Networks
- Overview of neural networks, their applications, and workflow.

### 2. Linear Algebra for Neural Networks
- Understanding linear algebra concepts used in neural networks.

### 3. Calculus for Neural Networks
- Exploring calculus concepts relevant to neural networks.

### 4. Miniconda Installation and Environment Setup
- Step-by-step guide for installing Miniconda and setting up the environment with needed libraries.

### 5. Python Refresher & PyTorch
- Implementing maths concepts as a Python refresher and getting started with Pytorch for neural network development.

### 6. Neurons and Activation Functions
- Understanding the building blocks of neural networks: neurons and activation functions.

### 7. Forward and Back Propagation
- Implementing forward and back propagation algorithms in neural networks.

### 8. Dense Neural Networks
- Building and training dense neural networks.

### 9. Convolutional Neural Networks (CNN)
- Introduction to CNNs and their applications in computer vision tasks.

### 10. Recurrent Neural Networks (RNN)
- Exploring RNNs and their ability to process sequential data.

### 11. Long Short-Term Memory (LSTM)
- Understanding LSTM networks and their role in handling long-term dependencies.

### 12. Transfer Learning
- Leveraging pre-trained models for transfer learning in neural networks.

### 13. Regularization and Optimization
- Diagnosing overfitting, and the toolkit that fixes it: weight decay, dropout, batch normalization, data augmentation and early stopping. How optimizers move through the loss landscape, and why the learning rate schedule matters.

### 14. Attention and Transformers
- Queries, keys and values; scaled dot-product and multi-head attention built from scratch; positional encoding; the encoder block; and reading a trained model's attention maps.

### 15. Autoencoders and Variational Autoencoders
- Learning with no labels at all. Bottlenecks, latent spaces, denoising, the reparameterization trick, and generating new samples from a learned distribution.

### 16. Generative Adversarial Networks (GANs)
- Two networks playing a minimax game. Training loop, the diagnostics that actually mean something, mode collapse, and the stability tricks that make it work.

### 17. Deployment and Model Optimization
- Saving and loading without the traps, TorchScript and ONNX export, quantization, honest benchmarking, and wrapping a model in a serving interface.

### 18. Embeddings and Semantic Search
- Why keyword search breaks, mean pooling a Transformer into a sentence vector, cosine similarity, building and scaling a vector index, chunking, and measuring retrieval with recall@k and MRR.

### 19. Retrieval-Augmented Generation (RAG)
- The full pipeline — chunk, embed, index, retrieve, prompt, generate — with a local model. Closed-book versus grounded answers, refusing to answer, citations, and tuning chunk size and top-k.

## Conclusion

The labs build in five stages:

1. **Foundations (Labs 1-5).** The linear algebra and calculus that neural networks are made of, a working Python environment, and the PyTorch basics — tensors, autograd, and the training loop.
2. **Core architectures (Labs 6-12).** A single neuron and its activation function, forward and back propagation done by hand, then dense networks, convolutional networks for images, recurrent networks and LSTMs for sequences, and transfer learning to reuse what others have trained.
3. **Advanced topics (Labs 13-16).** The techniques that decide whether a network generalises, the attention mechanism that replaced recurrence, and two families of generative model.
4. **Production (Lab 17).** Everything that happens after the accuracy prints.
5. **Retrieval (Labs 18-19).** Reusing the Transformer as a search engine, and grounding a language model in your own documents.

A few ideas recur throughout, and they are worth naming:

- **Additive paths preserve gradients.** It is the same trick in the LSTM's cell state, in ResNet's skip connections, and in the Transformer's residual connections.
- **Gating is just a sigmoid used as a valve** — a learned decision about how much information passes.
- **Regularization is deliberate difficulty.** Every technique in Lab 13 makes training harder on purpose, in exchange for generalisation.
- **`model.train()` and `model.eval()` are not cosmetic.** Dropout and batch norm behave differently in each, and forgetting the switch fails silently.
- **Build it by hand once, then use the library.** Every lab implements the mechanism from scratch, verifies it against PyTorch's version, and then uses PyTorch's.

Each lab ends with an experiment section. Those are the point — the code is meant to be broken and rebuilt.

## References

- [1] [PyTorch Documentation](https://pytorch.org/docs/stable/index.html): Official documentation for PyTorch.
- [2] Machine Learning Knowledge (`machinelearningknowledge.ai`): the original source of several diagrams in Labs 01 and 06-09. The site no longer resolves, so those diagrams have been redrawn and now live in `Misc/`.
- [3] [Miniconda Documentation](https://docs.conda.io/en/latest/miniconda.html): Official documentation for Miniconda.
- [4] [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/): Christopher Olah's explanation of LSTMs, and the source of the LSTM diagrams in Lab 11.
- [5] [Attention Is All You Need](https://arxiv.org/abs/1706.03762): The original Transformer paper.
- [6] [Auto-Encoding Variational Bayes](https://arxiv.org/abs/1312.6114): The paper that introduced the VAE and the reparameterization trick.
- [7] [Generative Adversarial Networks](https://arxiv.org/abs/1406.2661): The original GAN paper.
- [8] [Dive into Deep Learning](https://d2l.ai/): A free interactive book covering most of these topics in greater depth.

## Additional Resources

- [3Blue1Brown](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi): Visual tutorials for Neural Networks & Maths.
- [Deep Learning with PyTorch: A 60 Minute Blitz](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html): A beginner-friendly tutorial on deep learning with PyTorch.
- [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/): Online book by Michael Nielsen covering neural networks and deep learning concepts.
- [PyTorch Tutorials](https://www.youtube.com/playlist?list=PLqnslRFeH2UrcDBWF5mfPGpqQDSta6VK4): Complete beginner course.
- [Programming with Mosh](https://www.youtube.com/@programmingwithmosh): Python for beginners.

## Projects to implement (Optional)

<details>
<summary>Project 1: Image Classification</summary>

- Description: Build a neural network model that can classify images into different categories, such as cats and dogs.
- Steps:
    1. Collect a dataset of labeled images.
    2. Preprocess the images by resizing and normalizing them.
    3. Design and train a convolutional neural network (CNN) model using PyTorch.
    4. Evaluate the model's performance on a test set.
    5. Fine-tune the model to improve its accuracy.
    6. Test the model on new, unseen images.

</details>

<details>
<summary>Project 2: Sentiment Analysis</summary>

- Description: Develop a neural network model that can analyze the sentiment of text data, classifying it as positive, negative, or neutral.
- Steps:
    1. Gather a dataset of labeled text data with corresponding sentiment labels.
    2. Preprocess the text data by tokenizing, removing stopwords, and converting it into numerical representations.
    3. Build and train a recurrent neural network (RNN) model using PyTorch.
    4. Evaluate the model's performance on a validation set.
    5. Fine-tune the model by adjusting hyperparameters and architecture.
    6. Test the model on new, unseen text data.

</details>

<details>
<summary>Project 3: Stock Price Prediction</summary>

- Description: Create a neural network model that can predict future stock prices based on historical price data.
- Steps:
    1. Collect a dataset of historical stock prices, including features such as opening price, closing price, volume, etc.
    2. Preprocess the data by normalizing and splitting it into training and testing sets.
    3. Design and train a recurrent neural network (RNN) or long short-term memory (LSTM) model using PyTorch.
    4. Evaluate the model's performance by comparing predicted prices with actual prices.
    5. Fine-tune the model by adjusting hyperparameters and architecture.
    6. Use the model to make predictions on future stock price data.

</details>