# Rethinking Intelligence: Brain-like Neuron Network

![image-20260124220740036](.assets/image-20260124220740036.png)

> Since their inception, artificial neural networks have relied on manually designed architectures and inductive biases to better adapt to data and tasks. With the rise of deep learning and the expansion of parameter spaces, they have begun to exhibit brain-like functional behaviors. Nevertheless, artificial neural networks remain fundamentally different from biological neural systems in structural organization, learning mechanisms, and evolutionary pathways.
>
> From the perspective of neuroscience, we rethink the formation and evolution of intelligence and proposes a new neural network paradigm, Brain-like Neural Network (BNN). We further present the first instantiation of a BNN termed LuminaNet that operates without convolutions or self-attention and is capable of autonomously modifying its architecture. We conduct extensive experiments demonstrating that LuminaNet can achieve self-evolution through dynamic architectural changes. On the CIFAR-10, LuminaNet achieves top-1 accuracy improvements of 11.19%, 5.46% over LeNet-5 and AlexNet, respectively, outperforming MLP-Mixer, ResMLP, and DeiT-Tiny among MLP/ViT architectures. On the TinyStories text generation task, LuminaNet attains a perplexity of 8.4, comparable to a single-layer GPT-2-style Transformer, while reducing computational cost by approximately 25% and peak memory usage by nearly 50%.

![image-20260124221015948](.assets/image-20260124221015948.png)



## ✧ Structure Visualization

We provide several interactive structures of the LuminaNet mentioned in the paper.

1. Image Recognition Task (CIFAR-10)
    
    | d_hidden | structure                                                    |
    | -------- | ------------------------------------------------------------ |
    | 10       | [link](https://aaroncomo.github.io/LuminaNet/structure/cifar-10/cifar10-10.html) |
    | 32       | [link](https://aaroncomo.github.io/LuminaNet/structure/cifar-10/cifar10-32.html) |
    | 64       | [link](https://aaroncomo.github.io/LuminaNet/structure/cifar-10/cifar10-64.html) |
    | 84       | [link](https://aaroncomo.github.io/LuminaNet/structure/cifar-10/cifar10-84.html) |
    | 128      | [link](https://aaroncomo.github.io/LuminaNet/structure/cifar-10/cifar10-128.html) |
2. Text Generation Task (TinyStories)
    
    | d_hidden | structure                                                    |
    | -------- | ------------------------------------------------------------ |
    | 128      | [link](https://aaroncomo.github.io/LuminaNet/structure/tinystories/tinystories-128.html) |
    | 256      | [link](https://aaroncomo.github.io/LuminaNet/structure/tinystories/tinystories-256.html) |
    | 384      | [link](https://aaroncomo.github.io/LuminaNet/structure/tinystories/tinystories-384.html) |



## ✧ Requirements

```bash
conda create -n LuminaNet python=3.10.16
conda activate LuminaNet
pip install -r requirments.txt
```



## ✧ Testing

```bash
python test_<cifar10/tinystories>.py
```



## ✧ Training

> Training code will be released soon.



## ✧ License

This repository is licensed for research and non-commercial use only.

Commercial use requires a separate license from the author.

Please refer to [LISENCE](https://github.com/AaronComo/LuminaNet/blob/main/LICENSE) for more information.

Contact: 

- contact@vistazenith.com
- weifeng.liu@vistazenith.com

