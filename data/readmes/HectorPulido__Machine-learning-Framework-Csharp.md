# 🧠 TAS · Machine Learning Framework for C#

**TAS (Training Autograd System)** is a minimalist pytorch-like machine learning framework made with C#, built on top of **[SimpleLinearAlgebra](SimpleLinearAlgebra)**, a dependency-free matrix library that also lives in this repo — together with the whole family of from-scratch neural networks that grew around them.

![CI](https://github.com/HectorPulido/Machine-learning-Framework-Csharp/actions/workflows/ci.yml/badge.svg)
![Language](https://img.shields.io/badge/Language-C%23-178600)
![Target](https://img.shields.io/badge/Target-netstandard2.0-blue)
![Unity](https://img.shields.io/badge/Unity-compatible-222c37?logo=unity&logoColor=white)
![License](https://img.shields.io/github/license/HectorPulido/Machine-learning-Framework-Csharp?color=orange)

This project was made using as reference the work of [@iamtrask](https://twitter.com/iamtrask) and his book [Grokking Deep Learning](https://github.com/iamtrask/grokking-deep-learning).

## Repo map

| Folder | What it is |
|---|---|
| [`src/DLFramework`](src/DLFramework) | The TAS framework: tensors, autograd operations, layers, losses and optimizers |
| [`SimpleLinearAlgebra`](SimpleLinearAlgebra) | The matrix + rank-4 tensor library everything is built on — zero dependencies, works anywhere (including Unity) |
| [`SimpleLinearAlgebra/examples`](SimpleLinearAlgebra/examples) | Three from-scratch neural networks written directly with matrices: mono-layer, multi-layer and a convolutional network trained end-to-end |
| [`examples/TasXor`](examples/TasXor) | XOR trained with TAS, from raw tensors up to `Sequential` + `SGD` |
| [`examples/AutogradDemo`](examples/AutogradDemo) | Guided tour of the autograd engine — every gradient checked against the derivative by hand |
| [`examples/SinRegression`](examples/SinRegression) | An MLP fits y = sin(x) end-to-end and plots the result as ASCII art |
| [`tests/`](tests) · [`SimpleLinearAlgebra/tests`](SimpleLinearAlgebra/tests) | xUnit suites for the framework and the library |

Everything targets **netstandard2.0** with C# 7.3 and **zero external dependencies**, so both libraries work in modern .NET, .NET Framework, Mono and **Unity** — you can even copy the sources straight into an `Assets/` folder.

> Until 2026 these lived as five separate repos (`Simple_Linear_Algebra`, `Simple-vectorized-mono-layer-perceptron`, `Vectorized-multilayer-neural-network`, `Convolutional-Neural-Network-From-Scratch` and this one); they were merged, modernized and tested here.

## Quick start

```bash
dotnet build TAS.sln     # build everything
dotnet test TAS.sln      # run the test suites
dotnet run --project examples/TasXor                                         # XOR with TAS
dotnet run --project examples/AutogradDemo                                   # guided tour of the autograd engine
dotnet run --project examples/SinRegression                                  # fit sin(x), plotted in the terminal
dotnet run --project SimpleLinearAlgebra/examples/MonoLayerPerceptron        # logic gates, by hand
dotnet run --project SimpleLinearAlgebra/examples/MultiLayerPerceptron       # XOR, generalized
dotnet run --project SimpleLinearAlgebra/examples/ConvolutionalNeuralNetwork # Fashion-MNIST (auto-downloads)
```

## How TAS works

TAS is an automatic differentiation framework inspired by pytorch. It uses a dynamic computational graph that allows changes at runtime, which makes it perfect for experimentation at the expense of performance. The core of TAS are the Tensors, a generalization of the concept of matrix for superior dimensions — TAS currently supports tensors of up to 2 dimensions, which is enough for text analysis, reinforcement learning and classic dense networks.

### Creating tensors

```csharp
using LinearAlgebra;
using DLFramework;
using DLFramework.Operations;

var data = new Tensor((Matrix) new double[,] { { 0, 0 }, { 0, 1 }, { 1, 0 }, { 1, 1 } }, true);
```

The first argument is the Matrix that will be converted into a tensor; the second marks the tensor as autograd, which lets gradients flow through it.

Math operations chain naturally, and if the operands are autograd the result will be too:

```csharp
var multiplication = data.MatMul(weights);
```

Backpropagate a gradient through the graph with `Backward`:

```csharp
loss.Backward(new Tensor(Matrix.Ones(loss.Data.X, loss.Data.Y)));

weight.Data -= weight.Gradient.Data * 0.1;
weight.Gradient.Data *= 0;
```

### Layers, losses and optimizers

The manual process above is wrapped by familiar abstractions — `Sequential`, `Linear`, `SigmoidLayer`/`ReLuLayer`, `MeanSquaredError` and `StochasticGradientDescent`:

```csharp
var seq = new Sequential();
seq.Layers.Add(new Linear(2, 5, r));
seq.Layers.Add(new SigmoidLayer());
seq.Layers.Add(new Linear(5, 1, r));
seq.Layers.Add(new SigmoidLayer());

var sgd = new StochasticGradientDescent(seq.Parameters, 1);
var mse = new MeanSquaredError();

for (var i = 0; i < 300; i++)
{
    var pred = seq.Forward(data);
    var loss = mse.Forward(pred, target);
    loss.Backward(new Tensor(Matrix.Ones(loss.Data.X, loss.Data.Y)));
    sgd.Step();
}
```

[`examples/TasXor`](examples/TasXor) walks through five versions of the same XOR network, from raw tensors and manual gradient descent (`FirstNN`) to the full `Sequential` + `SGD` + `MSE` stack (`FifthNN`) — that progression is the best tour of the framework.

### Features

- **Autograd operations:** Add, Sub, Neg, Mul (element-wise), MatMul, Transpose, Expand, Sum
- **Layers:** Linear, Sigmoid, ReLu, Sequential
- **Loss:** Mean Squared Error
- **Optimizer:** Stochastic Gradient Descent
- **Initializators:** Gaussian and Uniform random

### TODO

- Support for real tensors, not just matrices
- Performance adjustments
- More layers, loss functions and activation functions

## More interesting projects

- [Evolutionary-Neural-Networks-on-unity-for-bots](https://github.com/HectorPulido/Evolutionary-Neural-Networks-on-unity-for-bots)
- [Chatbot-seq2seq-C-](https://github.com/HectorPulido/Chatbot-seq2seq-C-)
- [Multi-layer-perceptron](https://github.com/HectorPulido/Multi-layer-perceptron)
- [AwesomeUnityProjects](https://github.com/HectorPulido/AwesomeUnityProjects)

## License

This project was totally handcrafted, so the license is MIT — use it as you want.

<div align="center">
<h3 align="center">Let's connect 😋</h3>
</div>
<p align="center">
<a href="https://www.linkedin.com/in/hector-pulido-17547369/" target="blank">
<img align="center" width="30px" alt="Hector's LinkedIn" src="https://www.vectorlogo.zone/logos/linkedin/linkedin-icon.svg"/></a> &nbsp; &nbsp;
<a href="https://twitter.com/Hector_Pulido_" target="blank">
<img align="center" width="30px" alt="Hector's Twitter" src="https://www.vectorlogo.zone/logos/twitter/twitter-official.svg"/></a> &nbsp; &nbsp;
<a href="https://www.twitch.tv/hector_pulido_" target="blank">
<img align="center" width="30px" alt="Hector's Twitch" src="https://www.vectorlogo.zone/logos/twitch/twitch-icon.svg"/></a> &nbsp; &nbsp;
<a href="https://www.youtube.com/channel/UCS_iMeH0P0nsIDPvBaJckOw" target="blank">
<img align="center" width="30px" alt="Hector's Youtube" src="https://www.vectorlogo.zone/logos/youtube/youtube-icon.svg"/></a>
</p>
