<div align="center">

# echarts-bigscreen-skill

**领导要的数据大屏,一句话生成。**

AI 数据可视化大屏生成技能(Claude Code Skill)· 一句话生成 ECharts 可视化大屏 / 监控大屏 / 数据驾驶舱 / 一张图,单文件 HTML 双击即用,支持政务内网离线部署。

[English](./README.en.md) · 简体中文

</div>

---

![大屏效果预览](./assets/preview.png)

> 🖼️ 上图即本技能生成的成品:双击 [`examples/traffic-monitor.html`](./examples/traffic-monitor.html) 本地直接体验(交通监控大屏,含地图、流光折线、玫瑰图、仪表盘、警情轮播)。

## 这是什么

给 Claude Code / Codex / Cursor 等 AI 编程工具装上的一个**大屏专业技能**。装好之后,对 AI 说:

> "给我做一个工厂能耗监控大屏"

它会按照资深可视化工程师的路数(选主题配色、定三栏布局、套 ECharts 成品配方、做 1920×1080 等比缩放)产出一个**单文件 HTML 大屏**,双击就能全屏投到 LED 大屏上,不用搭工程也不用 npm。

**为什么需要这个技能?** 直接让 AI 写大屏,它会给你白底的"报表网页":配色随机、没有科技感边框、分辨率一缩放就乱、CDN 用国内打不开的 unpkg、内网一部署就白屏。这个技能把大屏行业的实战经验(配色体系、布局网格、图表配方、**中国网络环境和政务内网的部署坑**)全部写成了 AI 能执行的规范。

## 快速开始

**Claude Code:**

```bash
# 克隆到技能目录(个人级,所有项目可用)
git clone https://github.com/xiaofuqing13/echarts-bigscreen-skill.git ~/.claude/skills/echarts-bigscreen
```

然后在 Claude Code 里直接说需求:

```
做一个高速公路收费站运营监测大屏,深色科技风
```

**Cursor / Codex / Windsurf 等其他工具:** 把本仓库文件夹放进项目,在对话里说"按照 echarts-bigscreen-skill/SKILL.md 的规范,给我做一个 ×× 大屏"。技能本体是纯 Markdown,任何能读文件的 AI 编程工具都能用。

## 特性

- 🎨 **6 套实战主题**:深海蓝(政务/交通)、翡翠青(环保/能源)、暗夜紫(科技)、曜石红金(应急)、墨黑鎏金(金融)、中国红(党建),每套都是完整的 CSS 变量 + ECharts 色板
- 📐 **4 种布局模式**:三栏经典 / 主视觉侧重 / 上下汇报型 / 田字格,自带科技感四角边框卡片规范
- 📊 **7 类图表成品配方**:流光渐变折线、渐变柱状、玫瑰图轮播高亮、迷你仪表盘、双轴柱线、地图飞点、警情无缝轮播表
- 🖥️ **1920×1080 等比缩放**:一套代码适配 1080p 显示器、4K 大屏、LED 拼接屏,不写媒体查询
- 🇨🇳 **中国环境适配**(做过政务项目的都懂这些坑):
  - CDN 用国内稳定源(npmmirror)+ 自动 fallback,不用国内打不开的 unpkg
  - 地图数据走阿里 DataV GeoAtlas,全国省市区县全覆盖
  - **政务/公安内网离线部署方案**:本地化 echarts.min.js 与 GeoJSON、file:// 协议 CORS 规避
  - 老旧浏览器(360 兼容模式、信创环境)语法安全清单
  - 7×24 长期运行的内存与定时器管理红线
- 📦 **单文件交付**:产物是一个 .html,微信/钉钉发给领导,双击就能看

## 支持的场景

交通指挥 · 公安情指 · 政务综合治理一张图 · 智慧园区 · 工厂生产监控 · 能耗双碳 · 环保监测 · 应急消防 · 校园安防 · 电力调度 · 商业经营分析 · 医院运营 · 乡村振兴 · 文旅客流

## 目录结构

```
echarts-bigscreen-skill/
├── SKILL.md                      # 技能入口(AI 读这个)
├── references/
│   ├── color-themes.md           # 6 套大屏配色主题
│   ├── layout-patterns.md        # 布局网格与卡片规范
│   ├── echarts-recipes.md        # ECharts 高频图表配方
│   └── china-deploy.md           # 中国环境部署专项(内网/信创/LED屏)
├── examples/
│   └── traffic-monitor.html      # 完整示例:交通监控大屏(双击可看)
└── assets/
    └── preview.png               # 示例大屏效果截图
```

## 常见问题

**Q:生成的大屏能对接真实数据吗?**
所有 mock 数据集中在文件顶部 `MOCK` 区,每个字段都注释了对应的接口格式(`// TODO: GET /api/...`),把 fetch 换成你的接口即可。也可以直接让 AI:"把车流量图表对接到我的接口 /api/flow"。

**Q:政务内网用不了外网 CDN 怎么办?**
对 AI 说"内网环境"即可,它会读取 `references/china-deploy.md`,改为本地 `lib/echarts.min.js` 引用并告诉你去哪里下载文件。

**Q:我们的屏是 3×2 拼接的 LED 屏,分辨率很怪。**
说出物理分辨率(如 5760×2160),技能会按目标比例出设计稿并调整布局,而不是硬套 16:9。

**Q:必须用 Claude Code 吗?**
不是。技能本体是 Markdown 规范,Cursor、Codex、Windsurf、Copilot 等能读取项目文件的 AI 工具都能按此规范生成。

## 关键词

ECharts 大屏 · 数据可视化大屏 · 可视化大屏模板 · 监控大屏 · 数据驾驶舱 · 智慧大屏 · 一张图 · 大屏自适应 · AI 生成大屏 · Claude Code Skill · data visualization · big screen dashboard

## License

[MIT](./LICENSE) © xiaofuqing13

如果这个技能帮你交付了大屏,点个 ⭐ Star 让更多人看到它。
