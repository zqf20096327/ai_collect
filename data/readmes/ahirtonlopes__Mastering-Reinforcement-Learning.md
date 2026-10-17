# Mastering Reinforcement Learning

Hands-on notebooks covering classical and modern Reinforcement Learning algorithms, from the foundations of decision-making to Deep RL with neural networks.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Gymnasium](https://img.shields.io/badge/Gymnasium-0.29+-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## What you'll learn

- Model sequential decision problems as **Markov Decision Processes (MDPs)**
- Understand and apply the **Bellman Equation** for value estimation
- Implement **Q-Learning** from scratch in discrete environments
- Explore the exploration vs. exploitation trade-off
- Scale to complex environments using **Deep Q-Networks (DQN)**
- Interpret learning curves and agent performance

## Prerequisites

| Topic | Level |
|---|---|
| Python | Intermediate |
| NumPy & Matplotlib | Basic |
| Neural Networks | Basic (for Lesson 3) |

---

## Contents

### Lesson 1 — Q-Learning
> `Aula1_Q_Learning_Taxi.ipynb`

Introduction to Q-Learning in a discrete environment. The agent learns to navigate the Taxi grid by maximizing cumulative reward.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ahirtonlopes/Mastering-Reinforcement-Learning/blob/main/Aula1_Q_Learning_Taxi.ipynb)

---

### Lesson 2 — Bellman Equation & FrozenLake
> `Aula2_Bellman.ipynb` · `Aula2_Grid_movements_RL.ipynb` · `Aula2_Q_Learning_FrozenLakev1.ipynb`

From the Bellman recurrence to a full Q-Learning implementation in the stochastic FrozenLake environment.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ahirtonlopes/Mastering-Reinforcement-Learning/blob/main/Aula2_Bellman.ipynb)

---

### Lesson 3 — Deep Reinforcement Learning (DQN)
> `Aula3_DQN_Breakout.ipynb` · `Aula3_DQN_LunarLander.ipynb`

Moving from Q-tables to neural network function approximation. Trains DQN agents on Breakout and LunarLander.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ahirtonlopes/Mastering-Reinforcement-Learning/blob/main/Aula3_DQN_LunarLander.ipynb)

---

## Getting Started

**Option 1 — Google Colab (recommended)**

Click any "Open in Colab" badge above to run directly in your browser, no setup required.

**Option 2 — Local**

```bash
git clone https://github.com/ahirtonlopes/Mastering-Reinforcement-Learning.git
cd Mastering-Reinforcement-Learning
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

**Dependencies**
```
gymnasium
numpy
matplotlib
tensorflow  # Lesson 3
```

---

## Study Tips

Run notebooks in order. After each lesson, try modifying the key hyperparameters:

- `alpha` — learning rate
- `gamma` — discount factor
- `epsilon` — exploration rate

Observe how each change affects the reward curve and ask: *is the agent actually learning, or just getting lucky?*

---

## Author

**Prof. Dr. Ahirton Lopes** · [LinkedIn](https://linkedin.com/in/ahirtonlopes) · [Google Scholar](https://scholar.google.com/citations?user=1SQDVrwAAAAJ)

Contributions are welcome — open an issue or submit a pull request.

## License

[MIT](LICENSE)
