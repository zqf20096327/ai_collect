# Credit-Card-Fraud-Detection

### Abstract
Due to a rapid advancement in the electronic commerce technology, the use of credit cards has dramatically increased. As credit card becomes the most popular mode of payment for both online as well as regular purchase, cases of fraud associated with it are also rising. A fraudulent purchase, however, rarely looks wrong on its own: what gives it away is that it does not fit the way that particular cardholder usually spends. Detection is therefore better posed as a question about the sequence of a cardholder's transactions than about any single amount, and it has to be learned without labelled examples of fraud, which are rare and tend to arrive too late to be of use. In [this paper](https://ieeexplore.ieee.org/document/4358713), authors model the sequence of operations in credit card transaction processing using a hidden Markov model (HMM) and show how it can be used for the detection of frauds. An HMM is initially trained with the normal behavior of a cardholder. If an incoming credit card transaction is not accepted by the trained HMM with sufficiently high probability, it is considered to be fraudulent. At the same time, they try to ensure that genuine transactions are not rejected, and they report detailed experimental results comparing the approach with other techniques available in the literature.

This repository is a Python implementation of that technique, working from one cardholder's history as a sequence of purchase amounts. Since a hidden Markov model observes symbols rather than raw numbers, the amounts are first clustered so that each transaction becomes a spending level such as low, medium or high; k-means is used by default, and DBSCAN along with single, complete and average linkage clustering are provided as alternatives. The resulting sequence of symbols trains an HMM with a small number of hidden states, starting from uniform initial, transition and emission probabilities that the Baum-Welch algorithm then re-estimates over repeated forward-backward passes. A new transaction is judged by mapping its amount to a cluster, appending the symbol to the recent observation window in place of the oldest one, and comparing the probability the trained model gives the new sequence against the probability of the old one: a relative drop beyond a configurable threshold marks the transaction as fraudulent, and anything smaller as normal. Amounts are read interactively, and a verdict is printed for each.

#### To use this work on your researches or projects you need:
* Python 3.7.0
* Python packages:
	* hidden_markov
	* numpy
	* pandas
	* scikit_learn

#

#### To install Python:
_First, check if you already have it installed or not_.
~~~~
python3 --version
~~~~
_If you don't have python 3 in your computer you can use the code below_:
~~~~
sudo apt-get update
sudo apt-get install python3
~~~~
#

#### To install packages via pip install:
~~~~
sudo pip3 install hidden_markov numpy pandas scikit_learn
~~~~
_If you haven't installed pip, you can use the codes below in your terminal_:
~~~~
sudo apt-get update
sudo apt install python3-pip
~~~~
_You should check and update your pip_:
~~~~
pip3 install --upgrade pip
~~~~
#