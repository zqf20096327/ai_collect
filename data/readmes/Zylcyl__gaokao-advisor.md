# gaokao-advisor

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/Zylcyl/gaokao-advisor?style=social)](https://github.com/Zylcyl/gaokao-advisor/stargazers)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/Zylcyl/gaokao-advisor)](https://github.com/Zylcyl/gaokao-advisor/commits)
[![GitHub Issues](https://img.shields.io/github/issues/Zylcyl/gaokao-advisor)](https://github.com/Zylcyl/gaokao-advisor/issues)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/Zylcyl/gaokao-advisor)](https://github.com/Zylcyl/gaokao-advisor)

高考志愿填报智能顾问 —— 基于多 Skill 协调架构的 AI 志愿填报系统。

不只是给信息，更是帮考生看清路、想清楚。

如果喜欢，可以考虑给我一个star~

## 特点

- **政策优先**：先搜索当年最新政策再做决策，避免基于过时规则给建议
- **场景自适应**：自动识别 12 种考生场景（迷茫/纠结/冲突/紧急/艺体/军警/低分段/复读/残疾等），走不同交互路径
- **数据驱动**：所有推荐基于可验证的公开数据，位次为锚点，选科刚性核验
- **决策辅助**：帮考生看清选项、缩小范围、建立信心
- **多 Skill 协调**：主调度 + 分数线检索 + ADI 评估 + 报告生成，模块化设计
- **年度通用**：每年只需更新 `config.json` 中的年份即可使用
- **覆盖全流程**：从出分到填报到出结果，含填报当天操作指南和填报后心理支持

## 架构

```
gaokao-advisor/
├── SKILL.md                              主调度中心（323行）
├── config.json                           年度配置（每年更新一次）
├── README.md                             本文件
├── LICENSE                               MIT 许可证
└── skills/
    ├── province-score-line/
    │   └── SKILL.md                      录取数据搜索策略（135行）
    ├── adi-assessment/
    │   ├── SKILL.md                      ADI 四维评估引擎（59行）
    │   ├── baseline_adi.json             标杆数据
    │   └── question_bank.json            素质问卷题库
    └── report-generator/
        └── SKILL.md                      报告格式规范（94行）
```

**调用关系：**

```
考生输入
  ↓
主 SKILL.md（调度中心）
  ├── 读取 config.json（获取年份、政策配置）
  ├── Read → province-score-line/SKILL.md
  │         └── 按策略执行 WebSearch 查询录取数据
  ├── Read → adi-assessment/SKILL.md
  │         └── 按问卷和评分规则执行 ADI 评估
  └── Read → report-generator/SKILL.md
            └── 按格式规范输出推荐报告
```

## 安装

### 方式一：手动安装

将整个 `gaokao-advisor` 文件夹复制到你的 AI agent 的 skills 目录：

| Agent | 安装路径 |
|-------|----------|
| Claude Code | `~/.claude/skills/gaokao-advisor/` |
| Cowork | Cowork skills 目录 |
| Cursor | `~/.cursor/skills/gaokao-advisor/` |
| 其他 | 任何支持 Skills 的 agent 的 skills 目录 |

```bash
git clone https://github.com/Zylcyl/gaokao-advisor.git ~/.claude/skills/gaokao-advisor
```

### 方式二：直接使用

即使不安装为 skill，你也可以把 `SKILL.md` 的内容粘贴进对话——它本质就是一份指令。

## 使用

安装后，对你的 AI agent 说：

```
我是湖南考生，物理类，568分，位次28000，帮我填志愿
```

或：

```
用高考报考顾问帮我分析一下我的志愿选择
```

### 测试场景

| 场景 | 示例输入 |
|------|----------|
| 常规填报 | "我是广东考生，历史类，520分，帮我看看能上什么学校" |
| 迷茫型 | "我不知道学什么专业，能帮帮我吗" |
| 冲突型 | "我爸非要我学医，我想学计算机" |
| 紧急型 | "明天就截止了，快来不及了" |
| 艺术类 | "我是美术生，统考240分，文化课380分" |
| 低分段 | "我只考了350分，还有什么好选择吗" |

## 年度维护

每年高考季前（5-6月），只需做一件事：

打开 `config.json`，把 `current_year` 更新为当年年份：

```json
{
  "current_year": 2027,        // ← 改这里
  "recent_data_years": [2026, 2025, 2024],  // ← 和这里
  ...
}
```

其他字段（改革时间线、政策搜索关键词等）通常不需要改动。

## 内置能力

### 决策框架（AI 内功，不直接暴露给考生）

- **就业倒推法**：从中间 50% 毕业生的真实去向倒推专业选择
- **ADI 四维评估**：路径宽度 × 成功可达性 × 纠偏能力 × 损失可控性（1-625分）
- **不可替代性检验**：AI 时代哪些能力不容易被替代
- **10 年后压迫测试**：帮纠结的考生做最终判断
- **家庭背景分流**：不同家庭条件给出不同策略

### 特殊场景覆盖

- 艺术类/体育类考生（统考/校考/综合分）
- 军校/公安类（政审/体检/体测）
- 低分段与三二分段（专科+本科通道）
- 复读生（更保守策略，更多心理支持）
- 残疾考生（无障碍设施/体检限制核查）
- 定向招生（公费师范/免费医学/服务期分析）
- 特殊类型线附近（一本线上下 20 分的精细策略）

### 全流程覆盖

- 出分前：估分阶段支持
- 出分后：政策研究 → 数据检索 → 推荐方案
- 填报当天：系统操作指南（代码核对/截图保存/提前提交）
- 填报后：等待期心理支持 → 收到录取后行动指南

## 数据声明

- 所有推荐基于公开数据，AI 不编造录取信息
- 概率估算是基于往年位次的粗略参考，非精确预测
- 建议将推荐结果与高中老师、学长学姐的意见做交叉验证
- 最终以省考试院和院校官网发布的信息为准

## 许可证

[MIT](LICENSE) — 随便用，随便改，随便分发。

## 致谢

本项目融合了以下方法论、模型和开源项目：

### 张雪峰决策框架

就业倒推法、中位数原则、阶层现实主义、家庭背景分流等决策框架，来源于对张雪峰公开言论的系统性提炼。

- 原始 Skill 仓库：[alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill)
- 由 [女娲.skill](https://github.com/alchaincyf/nuwa-skill) 自动生成，作者 [花叔 Huashu](https://github.com/alchaincyf)
- 许可证：MIT

### ADI 专业路径评估模型

ADI（Action Domain Index）四维评估模型——路径宽度、成功可达性、纠偏能力、损失可控性——用于评估专业选择的"可走通性"。

- 原始 Skill 仓库：[xiapuyang/gaokao-adi](https://github.com/xiapuyang/gaokao-adi)
- 模型理论来源：**风灵之声**（风灵）于 2026 年 3 月发布的三篇系列文章
- 本项目使用的是从公开案例和标杆值反推的工程化实现
- 许可证：MIT

### province-score-line 录取数据检索策略

结构化录取数据检索方法论，包括省份匹配、选科自动纠错、新老高考模式识别等。

- 原始 Skill 定义由本项目作者设计
- 参考了各省教育考试院公开数据的查询模式

### 其他参考

- [阳光高考平台](https://gaokao.chsi.com.cn)（教育部官方）
- 各省教育考试院公开数据
- Agent Skills 开放协议（[agentskills.io](https://agentskills.io)）


捐款渠道：
<img width="203.7" height="203.7" alt="e91e35013fc1c12eab07dfcfd9a42168" src="https://github.com/user-attachments/assets/e7ee8212-5844-4c65-8331-6473a25d914f" />

