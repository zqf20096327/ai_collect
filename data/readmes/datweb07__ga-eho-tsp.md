# GA-EHO-TSP

**Genetic Algorithm and Elephant Herding Optimization for the Traveling Salesman Problem**

## Overview

This repository contains a university Artificial Intelligence course project focused on solving the **Traveling Salesman Problem (TSP)** using two metaheuristic optimization algorithms:

- **Genetic Algorithm (GA)**
- **Elephant Herding Optimization (EHO)**

The project aims to implement, visualize, and experimentally evaluate both algorithms across different TSP instances.

## Project Objectives

The primary objectives of this project are:

1. Implement the Genetic Algorithm for solving TSP.
2. Implement Elephant Herding Optimization for solving TSP.
3. Develop an interactive application for visualizing TSP solutions.
4. Evaluate solution quality, convergence behavior, and computational performance.
5. Conduct experiments using multiple TSP benchmark datasets.

## Technologies

- Python 3.11 or newer
- Tkinter and ttk for the desktop interface
- Matplotlib for charts and route visualization
- Jupyter Notebook and IPython kernel for experiments
- Python standard library for the GA core

## Installation

Run these commands from the repository root in PowerShell:

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If PowerShell does not allow environment activation, use `\.venv\Scripts\python.exe` in place of `python` for the installation and project commands. On Windows, Tkinter is included with most standard Python installations; if it is unavailable, install Python with the Tcl/Tk component enabled.
