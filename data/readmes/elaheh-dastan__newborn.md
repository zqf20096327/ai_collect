[![CI](https://github.com/elaheh-dastan/newborn/actions/workflows/ci.yml/badge.svg)](https://github.com/elaheh-dastan/newborn/actions/workflows/ci.yml)
[![Go Reference](https://pkg.go.dev/badge/github.com/elaheh-dastan/newborn.svg)](https://pkg.go.dev/github.com/elaheh-dastan/newborn)
[![Go Version](https://img.shields.io/github/go-mod/go-version/elaheh-dastan/newborn)](go.mod)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
# Introduction
This repository is really simple and small I tried to put only basic and most frequently ML algorithms in it, I'm going
to explain all the algorithms implemented in this repository, how you can use them and even the math calculation behind
them for those who are interesting.

Requires Go 1.27+. The algorithms are implemented with generics: numeric data can be `float32` or `float64`
(anywhere a `numeric.Float` constraint is used), and `knn.KNN` can classify into any `comparable` label type,
not just `int`.

| Package         | What's in it                                   | Task                        |
|-----------------|-------------------------------------------------|------------------------------|
| `data`          | CSV reading, column parsing, scatter plotting    | I/O & visualization          |
| `knn`           | K-Nearest Neighbours                             | classification               |
| `regression`    | Polynomial, Linear, Logistic regression          | regression & classification  |
| `cluster`       | K-Means                                          | clustering                   |
| `bayes`         | Gaussian Naive Bayes                             | classification               |
| `preprocessing` | Train/test split, k-fold, standardization, min-max scale | data prep            |
| `metrics`       | Accuracy, MSE, confusion matrix                  | evaluation                   |
| `tree`          | Decision Tree (CART, Gini impurity)              | classification                |
| `stats`         | Mean, variance, median, covariance, correlation  | descriptive statistics       |
| `linalg`        | Vector/matrix ops: dot, norm, transpose, matmul  | linear algebra                |
| `distance`      | Euclidean, Manhattan, Cosine                     | shared by knn/cluster         |

# Development
```sh
go build ./...
go vet ./...
go test ./... -race -cover
golangci-lint run ./...
```
CI (`.github/workflows/ci.yml`) runs the same build/vet/test and lint steps on every push and pull request.

# Reading Data And Picturing It
One of the most basic capabilities you'll need for sure is to read data from a dataset and plot it if possible, most of 
the times the dataset is a CSVDataset here is a sample of how to use this library
```go
package main

import (
	"fmt"

	"github.com/elaheh-dastan/newborn/data"
)

func main() {
	headers, content := data.ReadCSVData("./data/dataset_test.csv")
	fmt.Println(headers)

	x, _ := data.ParseColumn[float64](content[headers[0]])
	y, _ := data.ParseColumn[float64](content[headers[1]])

	data.ScatterPlot(x, y, headers[0], headers[1], "example")
}
```
```
[x y]
```
![](images/example.png)

# Regression
One of the basic things everybody has to learn to study ML is linear regression, logistic regression and
nonlinear regression, regression is used in both predicting a value and classification.<br/>
Let's talk a little deeper about regression, we want to fit a line or curve to a set of data.I'm going to show the math
calculations of what is happening.

[check here if you are interested in the math calculations](https://elaheh-dastan.github.io/newborn/)

Linear regression is really just polynomial regression with degree equal to 1 and lambda equal to 0, so
`Polynomial` covers it, but `regression.Linear` is also provided as a small, dedicated type for the common
case (deterministic zero-initialized weights instead of `Polynomial`'s random init).

## Linear Regression
```go
package main

import (
	"fmt"

	"github.com/elaheh-dastan/newborn/regression"
)

func main() {
	// y = 2x + 1
	features := [][]float64{{1}, {2}, {3}, {4}, {5}}
	values := []float64{3, 5, 7, 9, 11}

	l := regression.NewLinear[float64]()
	l.Train(features, values, 0.01, 10000, 0) // last arg is the Ridge (L2) regularization strength

	fmt.Println(l.Predict([]float64{6}))
}
```
```
13.00000001230778
```

## Logistic Regression
Logistic regression is used for binary classification: it fits `sigmoid(bias + weights . x)` as an
estimate of `P(y=1|x)`, trained by gradient descent on cross-entropy loss.
```go
package main

import (
	"fmt"

	"github.com/elaheh-dastan/newborn/regression"
)

func main() {
	features := [][]float64{{-3}, {-2}, {-1}, {1}, {2}, {3}}
	labels := []float64{0, 0, 0, 1, 1, 1}

	l := regression.NewLogistic[float64]()
	l.Train(features, labels, 0.1, 5000)

	fmt.Println(l.Predict([]float64{5}))
	fmt.Println(l.Predict([]float64{-5}))
}
```
```
1
0
```

# K Nearest Neighbour
This algorithm is used for classification, to choose a label for a new data the algorithm finds the k nearest data to it
and finds the most repeated label among them, different methods can be used to calculate the distance between the new data 
and the old ones in this repository I use one of the easiest approaches called Euclidean Distance.<br/>
```go
package main

import (
	"fmt"
	"github.com/elaheh-dastan/newborn/data"
	"github.com/elaheh-dastan/newborn/knn"
	"strconv"
)

func main() {
	headers, content := data.ReadCSVData("./knn/dataset_test.csv")
	currentData := make([][]float64, len(content[headers[0]]))
	for i := range currentData {
		f := make([]float64, len(headers)-1)
		for j := range f {
			f[j], _ = strconv.ParseFloat(content[headers[j]][i], 64)
		}
		currentData[i] = f
	}

	labels := make([]int, len(content[headers[0]]))
	for i := range labels {
		labels[i], _ = strconv.Atoi(content[headers[len(headers)-1]][i])
	}

	newData := []float64{57.0,1.0,4.0,140.0,192.0,0.0,0.0,148.0,0.0,0.4,2.0,0.0,6.0}
    
        // k = 3
	label := knn.KNN(currentData, labels, newData, 3)
	fmt.Println(label)
}
```
```
0
```

# K-Means Clustering
K-Means is an unsupervised algorithm: given data with no labels, it partitions it into K groups by
repeatedly assigning each point to its nearest centroid and then recomputing centroids as the mean of
their assigned points (Lloyd's algorithm).
```go
package main

import (
	"fmt"

	"github.com/elaheh-dastan/newborn/cluster"
)

func main() {
	data := [][]float64{
		{0, 0}, {0.5, -0.5}, {-0.5, 0.5}, {0.2, 0.1},
		{10, 10}, {10.5, 9.5}, {9.5, 10.5}, {10.2, 10.1},
	}

	m := cluster.New[float64](2)
	assignments := m.Fit(data, 100)

	fmt.Println(assignments)
}
```
```
[1 1 1 1 0 0 0 0]
```
(centroids are initialized from random data points, so which cluster id ends up `0` vs `1` varies
between runs — the two groups will still end up in separate clusters)

# Naive Bayes
Gaussian Naive Bayes is a simple probabilistic classifier: it assumes each feature is normally
distributed within a class and independent of the other features (the "naive" assumption), then
classifies a new point as whichever class has the highest posterior probability.
```go
package main

import (
	"fmt"

	"github.com/elaheh-dastan/newborn/bayes"
)

func main() {
	features := [][]float64{
		{-1}, {0}, {1}, {-0.5}, {0.5},
		{9}, {10}, {11}, {9.5}, {10.5},
	}
	labels := []string{
		"low", "low", "low", "low", "low",
		"high", "high", "high", "high", "high",
	}

	nb := bayes.New[float64, string]()
	nb.Fit(features, labels)

	fmt.Println(nb.Predict([]float64{0.2}))
	fmt.Println(nb.Predict([]float64{9.8}))
}
```
```
low
high
```

# Decision Tree
A decision tree classifies by asking a sequence of "is feature j <= threshold?" questions, each one
chosen (greedily, via Gini impurity) to best separate the classes seen so far. `maxDepth` bounds how
many questions deep the tree can go.
```go
package main

import (
	"fmt"

	"github.com/elaheh-dastan/newborn/tree"
)

func main() {
	features := [][]float64{{1}, {2}, {3}, {8}, {9}, {10}}
	labels := []string{"low", "low", "low", "high", "high", "high"}

	dt := tree.New[float64, string](3)
	dt.Fit(features, labels)

	fmt.Println(dt.Predict([]float64{2.5}))
	fmt.Println(dt.Predict([]float64{9.5}))
}
```
```
low
high
```

# Metrics
The `metrics` package has a few small helpers for evaluating a trained model: `Accuracy` for
classification, `MSE` for regression, and `ConfusionMatrix` for a per-class breakdown of a
classifier's predictions.
```go
package main

import (
	"fmt"

	"github.com/elaheh-dastan/newborn/metrics"
)

func main() {
	predicted := []int{1, 0, 1, 1, 0}
	actual := []int{1, 0, 0, 1, 1}

	fmt.Println(metrics.Accuracy(predicted, actual))
	fmt.Println(metrics.ConfusionMatrix(predicted, actual))
}
```
```
0.6
map[0:map[0:1 1:1] 1:map[0:1 1:2]]
```

# Preprocessing
The `preprocessing` package helps prepare data before training: `TrainTestSplit` shuffles and
splits features/labels into a train and a test set (deterministically, given a seed), and
`Standardize`/`MinMaxScale` rescale features column by column.
```go
package main

import (
	"fmt"

	"github.com/elaheh-dastan/newborn/preprocessing"
)

func main() {
	features := [][]float64{{1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}}
	labels := []int{0, 0, 0, 0, 0, 1, 1, 1, 1, 1}

	trainX, trainY, testX, testY := preprocessing.TrainTestSplit(features, labels, 0.3, 42)
	fmt.Println(len(trainX), len(trainY), len(testX), len(testY))

	fmt.Println(preprocessing.MinMaxScale(features))
}
```
```
7 7 3 3
[[0] [0.1111111111111111] [0.2222222222222222] [0.3333333333333333] [0.4444444444444444] [0.5555555555555556] [0.6666666666666666] [0.7777777777777778] [0.8888888888888888] [1]]
```
`preprocessing.KFold(n, k, seed)` is also available for k-fold cross-validation: it returns, for each of
the k folds, the training indices and the held-out validation indices into your own features/labels slices.

# Statistics
The `stats` package has the descriptive statistics you'd reach for before modeling anything: `Mean`,
`Variance`, `StdDev`, `Median`, `Covariance` and `Correlation`.
```go
package main

import (
	"fmt"

	"github.com/elaheh-dastan/newborn/stats"
)

func main() {
	data := []float64{2, 4, 4, 4, 5, 5, 7, 9}

	fmt.Println(stats.Mean(data))
	fmt.Println(stats.StdDev(data))
	fmt.Println(stats.Median(data))
}
```
```
5
2
4.5
```

# Linear Algebra
The `linalg` package has the vector/matrix operations the other packages (and your own code) build on:
`Dot`, `Norm`, `Add`, `Sub`, `Scale` for vectors, and `Transpose`, `MatMul` for matrices.
```go
package main

import (
	"fmt"

	"github.com/elaheh-dastan/newborn/linalg"
)

func main() {
	a := []float64{1, 2, 3}
	b := []float64{4, 5, 6}

	fmt.Println(linalg.Dot(a, b))
	fmt.Println(linalg.Norm(a))
	fmt.Println(linalg.MatMul([][]float64{{1, 2}, {3, 4}}, [][]float64{{5, 6}, {7, 8}}))
}
```
```
32
3.7416573867739413
[[19 22] [43 50]]
```

# Distance Metrics
The `distance` package has the metrics `knn` and `cluster` use internally, exposed for your own use:
`Euclidean`, `Manhattan` and `Cosine`.
```go
package main

import (
	"fmt"

	"github.com/elaheh-dastan/newborn/distance"
)

func main() {
	a := []float64{0, 0}
	b := []float64{3, 4}

	fmt.Println(distance.Euclidean(a, b))
	fmt.Println(distance.Manhattan(a, b))
}
```
```
5
7
```