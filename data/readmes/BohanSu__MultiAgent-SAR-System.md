# 多智能体集群协作搜救系统 (Multi-Agent SAR System)
Multi-Agent Cooperative Search and Rescue System

这是一个面向复杂非结构化环境的无人机集群协作搜救仿真系统。
This is a UAV swarm cooperative search and rescue simulation system designed for complex unstructured environments.

本项目深度集成了机器人控制理论、信息论以及多智能体系统 (MAS) 领域的多种前沿算法，构建了一个具备自主感知、动态决策、路径规划和分布式协作能力的智能体集群仿真平台。
This project deeply integrates cutting-edge algorithms from robot control theory, information theory, and Multi-Agent Systems (MAS) to build an agent swarm simulation platform with autonomous perception, dynamic decision-making, path planning, and distributed collaboration capabilities.

## 核心特性
## Core Features

*   **先进避障算法**: 采用 **涡旋势场 (Vortex Potential Field)** 算法，有效解决了传统人工势场法 (APF) 的局部极小值问题，实现密集障碍物环境下的平滑绕行。
    
    **Advanced Obstacle Avoidance**: Adopts the **Vortex Potential Field** algorithm, effectively solving the local minima problem of the traditional Artificial Potential Field (APF) method and achieving smooth navigation in dense obstacle environments.

*   **信息驱动覆盖**: 实现基于 **分布式 Voronoi 覆盖控制** 与 **信息熵地图** 的结合，引导集群优先探索高不确定性区域。
    
    **Information-Driven Coverage**: Implements a combination of **Distributed Voronoi Coverage Control** and **Information Entropy Maps** to guide the swarm to prioritize exploration of high-uncertainty areas.

*   **高效搜索策略**: 引入 **Lévy Flight (莱维飞行)** 机制，利用重尾分布的随机游走策略，平衡局部搜索与广域探索，显著提升稀疏目标环境下的搜索效率。
    
    **Efficient Search Strategy**: Introduces the **Lévy Flight** mechanism, utilizing a heavy-tailed random walk strategy to balance local search and wide-area exploration, significantly improving search efficiency in sparse target environments.

*   **异构角色协作**: 支持 **侦察者 (Scout)**、**确认者 (Verifier)** 和 **支援者 (Support)** 等角色的动态分配与调度。
    
    **Heterogeneous Role Collaboration**: Supports dynamic assignment and scheduling of roles such as **Scout**, **Verifier**, and **Support**.

*   **高保真感知模型**: 摒弃简单的二元感知，构建了包含视场角 (FOV)、距离衰减和视线遮挡 (Occlusion) 的 **概率感知模型**。
    
    **High-Fidelity Perception Model**: Discards simple binary perception and builds a **probabilistic perception model** incorporating Field of View (FOV), distance attenuation, and Line of Sight (Occlusion).

## 系统架构
## System Architecture

系统遵循 **OODA (Observe-Orient-Decide-Act)** 循环架构：
The system follows the **OODA (Observe-Orient-Decide-Act)** loop architecture:

1.  **环境层**: 维护地图数据、障碍物分布及全局信息素。
    **Environment Layer**: Maintains map data, obstacle distribution, and global pheromones.
2.  **感知层**: 模拟传感器特性，处理视线遮挡与概率检测。
    **Perception Layer**: Simulates sensor characteristics, handling occlusion and probabilistic detection.
3.  **决策层**:
    **Decision Layer**:
    *   **指挥中心**: 基于拍卖算法 (Auction Algorithm) 进行全局任务分配。
        **Command Center**: Performs global task allocation based on the Auction Algorithm.
    *   **智能体**: 基于有限状态机 (FSM) 进行局部决策与控制。
        **Agents**: Perform local decision-making and control based on Finite State Machines (FSM).
4.  **执行层**: 处理动力学约束与电量管理。
    **Execution Layer**: Handles dynamic constraints and battery management.

## 项目结构
## Project Structure

```
.
├── src/                          # 源代码目录 (Source Code Directory)
│   ├── vortex_field.py           # 涡旋势场算法 (Vortex Potential Field Algorithm)
│   ├── drone_agent.py            # 无人机智能体逻辑 (Drone Agent Logic)
│   ├── coordinator_agent.py      # 指挥中心逻辑 (Coordinator Logic)
│   ├── environment.py            # 环境与物理规则 (Environment & Physics)
│   └── ...
├── figures/                      # 结果图表目录 (Results & Figures)
├── simulation.py                 # 仿真主程序 (Simulation Main Entry - GUI/Text)
├── visualization.py              # 可视化渲染模块 (Visualization Module)
├── run_experiments.py            # 批量实验脚本 (Batch Experiment Script)
├── plot_results.py               # 数据绘图脚本 (Data Plotting Script)
├── requirements.txt              # 项目依赖 (Project Dependencies)
└── README.md                     # 说明文档 (Readme)
```

## 快速开始
## Quick Start

### 1. 环境安装
### 1. Installation

本项目基于 Python 3.8+ 开发。
This project is developed based on Python 3.8+.

```bash
pip install -r requirements.txt
```

### 2. 运行仿真
### 2. Running Simulation

**启动 GUI 可视化模式**:
**Launch GUI Visualization Mode**:

```bash
# 基础场景 (Basic Scenario)
python simulation.py --scenario medium

# 密集障碍物场景 (观察涡旋避障)
# Dense Obstacle Scenario (Observe Vortex Avoidance)
python simulation.py --scenario hard --drones 4

# 城市覆盖场景 (观察 Voronoi 覆盖)
# City Coverage Scenario (Observe Voronoi Coverage)
python simulation.py --scenario city --drones 6
```

**启动无界面文本模式**:
**Launch Text-Only Mode**:

```bash
python simulation.py --text --scenario medium
```

### 3. 实验数据生成
### 3. Generating Experiment Data

如需复现性能分析图表（避障对比、覆盖率分析等）：
To reproduce performance analysis charts (obstacle avoidance comparison, coverage analysis, etc.):

```bash
# 运行批量实验 (耗时较长)
# Run batch experiments (Time consuming)
python run_experiments.py

# 生成统计图表
# Generate statistical charts
python plot_results.py
python generate_trajectory_plots.py
```
