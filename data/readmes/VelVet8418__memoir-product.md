<div align="center">

# 📖 忆声 · Memoir

**让人用说话的方式，留下一本"还是本人在说"的书。**

[![License: MIT](https://img.shields.io/badge/License-MIT-D4845A.svg?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](https://github.com/VelVet8418/memoir-product/pulls)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-❤️-red?style=for-the-badge)](#)
[![Platform](https://img.shields.io/badge/Platform-Web-blue?style=for-the-badge)](#)

---

*一个 AI 采访者：陪老人用说话的方式回忆人生，*
*只做"去赘词、顺语序、断句"三层轻整理，*
*产出一本**还是本人在说**的回忆录。*

</div>

---

## 🎯 解决什么问题

72 岁的退休教师王秀英，心里装着 1971 年黑龙江知青点的四年——雪地里送战友小韩返城、半个窝头的情分。她想讲，子女想留，但：

| 现有方案 | 痛点 |
|---------|------|
| 🏠 子女回家录音 | 坚持不过三次，整理时忍不住"润色"，老人读后说"这不像我说的" |
| 💰 请传记代笔 | 起价三万，写出来"像新闻稿" |
| ✍️ 老人自己写 | 握笔半小时手就抖 |
| 🤖 AI 代写工具 | 辞藻华丽，通篇虚构 |

> **结果是：全中国每天有成千上万个"王秀英的故事"随葬礼一起被埋掉。**
>
> 忆声要接住这些故事——不是替她说，而是让她说，并且一个字不改样地留下。

---

## 🕐 为什么是现在

- **📊 人口窗口**：中国 60 岁及以上人口约 3.1 亿（占 22%），50 年代生人的口述史是不可再生资源，记录窗口只剩 **10-15 年**
- **🔧 技术拐点**：方言语音识别 + 长对话记忆大模型 + 老照片理解视觉模型，在 2025-2026 年**首次同时达到**"老人无感可用"的水平
- **🏳️ 市场空白**：没有产品占据"保真"这个位置，而"像本人说的"恰恰是家庭愿意为之心动的唯一理由

---

## ✨ 产品特性

### 两种运行模式

| 模式 | 说明 | 适用场景 |
|------|------|---------|
| 🎭 **演示模式**（默认） | 预置 12 轮对话 + 预置成稿，断网也能完整走通 | 快速体验完整产品闭环 |
| 🟢 **AI 模式** | 接入 SiliconFlow 真实模型，对话与成稿走 AI | 真实用户访谈场景 |

> **🔒 隐私承诺**：API Key 仅保存在内存（`window.MEMOIR_API_KEY`），刷新即失效，不硬编码、不持久化、不上传任何第三方。

### 五大功能模块

| Tab | 名称 | 说明 |
|:---:|------|------|
| 📋 | **产品界定** | 为谁做、是什么/不是什么、什么程度算完成（5 张可折叠卡片） |
| 🗺️ | **推进路线** | 三阶段时间线 + AI/用户分工矩阵 + 7 角色 + 11 题自查清单 |
| ⭐💬 | **对话 Demo** | **核心**：12 轮访谈 → 整理成稿 → 逐句确认的完整可玩闭环 |
| 📊 | **用户漏斗** | 7 层漏斗可视化，滑块拖动实时演算，L4 最危险层警示 |
| 👨‍👩‍👧 | **子女视角** | 自发 vs 代发起 8 维对比 + 3 个被推翻的判断 + 2×2 矩阵 |

---

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/VelVet8418/memoir-product.git
cd memoir-product
```

### 2. 启动本地服务

ES Module 需要 HTTP 环境，任选其一：

```bash
# 方式一：Python（无需安装额外依赖）
python3 -m http.server 8000

# 方式二：Node http-server
npx http-server -p 8000
```

### 3. 打开浏览器

访问 `http://localhost:8000`，默认进入 ⭐ 对话 Demo。

### 4. （可选）启用 AI 模式

1. 注册 [SiliconFlow](https://siliconflow.cn)（官网 → 注册 → 控制台 → API 密钥 → 新建密钥）
2. 复制 `sk-` 开头的密钥，粘贴到页面右上角输入框
3. 点击"启用 AI"按钮

---

## 📱 手机测试（局域网）

1. 电脑与手机连接同一 Wi-Fi
2. 查电脑局域网 IP（`ipconfig` / `ifconfig`）
3. 启动服务：`python3 -m http.server 8000 --bind 0.0.0.0`
4. 手机浏览器访问 `http://<电脑IP>:8000`
5. 重点验证：375px 竖屏无横向滚动、语音按钮可触达、成稿区从底部滑入

---

## 🏗️ 项目结构

```
memoir-product/
├── index.html           # 入口页面
├── main.js              # 应用主逻辑（Tab 切换、API Key 管理）
├── config/
│   ├── constants.js     # 全局配置常量
│   └── prompts.js       # AI Prompt 模板
├── core/
│   ├── ai.js            # AI 调用层（双模型分工）
│   ├── memory.js        # 记忆管理（多版本并存）
│   ├── speech.js        # 语音识别（长停顿自动重启）
│   └── stats.js         # 漏斗统计引擎
├── components/
│   ├── chat-bubble.js   # 对话气泡组件
│   ├── manuscript.js    # 成稿组件（含版本差异弹窗）
│   └── state-panel.js   # 状态面板组件
├── views/
│   ├── tab1.js          # 📋 产品界定
│   ├── tab2.js          # 🗺️ 推进路线
│   ├── tab3.js          # 💬 对话 Demo（核心）
│   ├── tab4.js          # 📊 用户漏斗
│   └── tab5.js          # 👨‍👩‍👧 子女视角
├── styles/
│   └── main.css         # 设计系统（30+ token，温暖系银发适配）
└── docs/                # 设计原则 + 产品文档 + 验收矩阵
    ├── 00_principles.md
    ├── 00_executive_summary.md
    ├── 01_product_definition.md
    ├── 02_roadmap_and_team.md
    ├── 03_demo_script.md
    ├── 04_funnel_analysis.md
    ├── 05_children_initiated.md
    └── acceptance_checklist.md
```

---

## 🛡️ 保真原则（设计红线）

> **判据**：老人本人看到后会认为"这还是我说的、我做的主"吗？答案为否，一律否决。

三条铁律：

- 🔴 **保真** — 老人的话是史料，不是素材
- 🔴 **不替代** — AI 没有创作权
- 🔴 **尊严** — 老人是作者，不是数据源

保真在产品每一层都有拦截器：Prompt 铁律 → `[AI补充]` 标记硬拦截 → 多版本不合并数据结构 → 成稿保真率盲测。

> 📄 完整原则文档：[docs/00_principles.md](docs/00_principles.md)

---

## 🔬 核心验证假设

| # | 假设 | 指标 | 否决条件 |
|---|------|------|---------|
| 1 | **有人愿意讲** | 10 名 A 类用户，2 周内 ≥6 人无激励说完第一段（>30s） | 证伪即停止 |
| 2 | **成稿像本人** | 20 份成稿句子级盲测，"像我说的"标注率 ≥80% | <70% 不扩量 |
| 3 | **会回来讲** | 30 名用户 4 周，次周自发复访率 ≥35% | 持续低于则调整策略 |

---

## ⚠️ 已知局限（诚实五条）

1. 真实 AI 模式未经真机联调验证（演示模式可完整体验全部机制）
2. 语音识别仅 Chrome/Edge 完整支持，其他浏览器自动降级为文字输入
3. 照片理解（vision 模式）配置已就绪但 UI 上传入口未实现，下一版本接入
4. 差异弹窗当前展示首组差异事件，多组差异并存时的逐句定位待完善
5. 数据存于浏览器 localStorage，清缓存即丢失——正式版需账号体系与云端备份

---

## 📋 核心风险

| 风险 | 说明 | 对策 |
|------|------|------|
| 🧠 认知可塑性 | AI 追问可能植入暗示，让老人混淆 AI 提示与自身记忆 | AI 只追问用户已说内容、版本差异绝不仲裁、伦理顾问审查 |
| 📉 银发留存 | "聊完一次就满足"的一次性使用是大概率事件 | 章节化悬念 + 子女端递话头，但绝不用推送骚扰老人 |
| 📝 成稿保真（L4） | 成稿一处"不像本人说的"，信任当场崩塌且不可修复 | 保真率盲测 <70% 前不扩量，写进扩张边界的硬约束 |

---

## 🤝 参与贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建你的特性分支（`git checkout -b feature/AmazingFeature`）
3. 提交你的修改（`git commit -m 'Add some AmazingFeature'`）
4. 推送到分支（`git push origin feature/AmazingFeature`）
5. 打开一个 Pull Request

---

## 📜 开源协议

本项目采用 [MIT License](LICENSE) 开源协议。

---

<div align="center">

**忆声 · 让每段经历，都被好好听见。**

*Made with ❤️ for every story that deserves to be heard.*

</div>
