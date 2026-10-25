# 董先生的中医AI诊疗室

> Mr. Dong's TCM AI Clinic — 基于六经辨证的多模态中医临床诊疗辅助数据系统

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

## ⚠️ 重要免责声明

**本项目仅供学习、研究与技术交流，不构成任何医疗建议。**

- 本项目输出的所有辨证结论、处方建议、用药方案，**均不可直接用于临床**。
- 中医诊断与用药必须在**执业中医师**的指导下进行。
- 本项目作者不对因使用本项目内容而产生的任何后果承担责任。
- 若您正在寻求医疗帮助，请立即咨询有资质的医疗专业人员。

---

## 项目简介

「董先生的中医AI诊疗室」是一套以《伤寒论》《金匮要略》**六经辨证**为核心框架的开源中医诊疗辅助系统，实现了从"四诊信息"到"辨证结论 + 经方处方"的完整可解释证据链：

- **六经辨证推理引擎** —— 逐经分析 + 条文对照 + 脉诊修正 + 双源印证
- **经方推导** —— 从六经诊断到具体处方，每味药可追溯到条文依据
- **古籍 RAG** —— ChromaDB + BM25 混合检索，覆盖约 700 本中医古籍
- **处方级统一风险引擎** —— 十八反/十九畏/剂量/妊娠/中西药/体质 一次评估
- **名医医案一致性评分** —— 处方与名医决策的一致性量化
- **GraphRAG 辨证推理** —— 症状→经方→证候的多跳可解释证据链
- **多模态四诊** —— 化验单 OCR、舌象视觉分析、脉象信号客观化
- **自我进化** —— 模式挖掘 + 疗效反馈 + 知识沉淀

## 系统架构（五层）

```
应用层    HTTP API (8787) + TUI + Flask Web
决策层    四步诊断管线 + RAG 预加载 + 证据链
知识层    知识图谱 + ChromaDB + BM25 + GraphRAG
多模态    OCR 流水线 + 舌象视觉 + 脉象信号
数据层    JSON Lines + SQLite + 统一 Schema
```

## 快速开始

### 环境要求

- Python 3.11+
- 可选：ChromaDB（向量检索）、多模态 LLM（舌象视觉）

### 安装

```bash
pip install -r requirements_minimal.txt   # 最小依赖
# 或
pip install -r requirements_full.txt      # 完整依赖（含 OCR / 向量检索）
```

### 配置

```bash
cp .env.example .env   # 填入你的 LLM API Key（见 .env.example）
```

### 运行

```bash
# 启动 HTTP API 服务（端口 8787）
python -m tcm_clinic.main serve

# 古籍语义搜索
python -m tcm_clinic.main search "手指屈而不伸 筋挛"

# 舌象视觉分析（需多模态模型）
python -m tcm_clinic.main tongue 舌头照片.jpg

# 交互式 TUI
python -m tcm_clinic.main
```

## 数据说明

**本仓库只分发「代码 + 手写本体 + 公有领域经典条文」。**

因隐私与版权原因，以下数据**不随仓库分发**，详见 [data/README.md](data/README.md)：

- 🔴 患者隐私数据（真实姓名、病历、医学影像）
- 🟡 来源/版权不确定的数据（爬虫数据、名医医案、古籍数字化文本、方剂大库）

## 项目结构

```
src/tcm_clinic/
├── reasoning/      六经辨证引擎 + 经方推导 + GraphRAG + 一致性评分
├── knowledge/      知识图谱 + ChromaDB + BM25 + RAG
├── multimodal/     OCR + 舌象视觉 + 舌象规则 + 脉象信号 + 脉象规则
├── tools/          药材/方剂/条文查询 + 配伍禁忌 + 统一风险引擎
├── agents/         四步诊断管线
├── evolution/      模式挖掘 + 疗效反馈
└── diagnosis/      Pydantic 领域模型
```

## 许可证

[Apache License 2.0](LICENSE)

- 允许商用、修改、再分发，但须保留版权声明与免责声明。
- 本项目不提供任何医疗担保，使用风险自负。

## 联系方式

- 📧 邮箱：[315096373@qq.com](mailto:315096373@qq.com)
