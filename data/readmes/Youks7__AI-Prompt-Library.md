<h1 align="center">KeRo AI Prompt Library</h1>

<p align="center"><strong>面向电商内容与视觉生产的结构化 Prompt、真实案例和 Agent 工作流库</strong></p>

<p align="center">Prompt · Visual Cases · Workflow Packs · Agent Skill</p>

<p align="center">
  <a href="README.md">简体中文</a> ·
  <a href="README_EN.md">English</a> ·
  <a href="README_ZH-TW.md">繁體中文</a>
</p>

<p align="center">
  <a href="https://youks7.github.io/AI-Prompt-Library/"><strong>可视化网站</strong></a> ·
  <a href="prompts/README.md">Prompt 目录</a> ·
  <a href="data/case-index.json">案例索引</a> ·
  <a href="agents/skills/kero-prompt-router/SKILL.md">Agent Skill</a>
</p>

---

## 项目数据

<!-- catalog-stats:start -->
| 结构化 Prompt | 复杂工作流 | 主题分类 | 关联视觉示例 |
|---:|---:|---:|---:|
| 88 | 11 | 9 | 36 |
<!-- catalog-stats:end -->

这些数字由内容生成器核对。运行 `npm run build` 可以重新生成网站目录、Prompt 索引、案例索引和 Skill 引用数据。

## 这不是随机提示词合集

本项目把真实内容生产中使用的 Prompt 按任务、输入、模型、案例和执行阶段整理。你可以直接复制一条 Prompt，也可以使用多阶段 Workflow Pack 完成分析、方向选择、生成、迭代和验收。

核心原则：

- **真实输入优先**：商品结构、材质、颜色、Logo、尺寸、价格和认证以用户资料为准。
- **结构化控制**：明确任务、变量、平台、受众、语言、风格和输出格式。
- **视觉示例与 Prompt 关联**：先看结果，再进入对应 Prompt；历史图片不等于完整案例研究，来源与许可状态以索引为准。
- **复杂任务分阶段**：不强行用一条超长 Prompt 解决所有问题。
- **同一数据源**：网站、索引和 Agent Skill 从同一个结构化目录生成。

## 快速开始

### 普通用户

1. 打开[可视化网站](https://youks7.github.io/AI-Prompt-Library/)。
2. 搜索任务或按分类、模型筛选。
3. 查看案例和 Prompt 详情。
4. 复制 Prompt，并替换为真实产品、受众、平台和素材信息。
5. 发布前核对事实、版权、价格、认证和平台要求。

### GitHub 用户

- [完整 Prompt 目录](prompts/README.md)
- [结构化 Prompt 数据](data/prompt-index.json)
- [复杂 Workflow Packs](prompt-packs/)
- [视觉案例索引](data/case-index.json)
- [使用示例](examples/)


### Agent 用户

仓库包含 [`kero-prompt-router`](agents/skills/kero-prompt-router/SKILL.md)。它会根据任务类型选择合适的 Prompt 或 Workflow，识别缺失资料并生成可直接使用的版本。

示例：

```text
使用 $kero-prompt-router，为泰国 TikTok 墨镜视频选择合适的脚本 Prompt。
```

```text
使用 $kero-prompt-router，根据我的产品图选择商业海报工作流，并提醒需要确认的材质与表面工艺。
```

## 按任务进入

| 你要完成的任务 | 推荐入口 |
|---|---|
| 商品详情页、卖点和广告文案 | [文案、电商与广告](prompts/03-copywriting.md) |
| TikTok 和短视频脚本 | [短视频与 TikTok](prompts/04-short-video-and-tiktok.md) |
| AI 图片、图生视频和分镜 | [AI 生图、视频与分镜](prompts/05-image-and-video-generation.md) |
| 主图、详情页和电商视觉 | [电商视觉设计](prompts/06-ecommerce-visual-design.md) |
| 人像、写真和照片修复 | [人像、写真与修复](prompts/08-banana-portrait-and-restoration.md) |
| 产品 KV、海报和精修 | [电商、海报与社交视觉](prompts/09-banana-ecommerce-and-poster.md) |
| 翻译、字幕和中泰本地化 | [翻译、音频与文本润色](prompts/02-translation-and-polishing.md) |
| 市场日报和自动化报告 | [市场分析与自动化](prompts/01-market-automation.md) |

## 代表性 Workflow Packs

- [工业级 AIGC 电商详情页 Prompt Gem V4.0](prompt-packs/industrial-aigc-ecommerce-v4.md)
- [Seedance 2.0 平台 / API 双模式](prompt-packs/seedance-platform-api-v4.md)
- [视频复刻拆解 v2.1](prompt-packs/video-remake-analysis-v2.1.md)
- [高端香水广告两步式导演](prompt-packs/luxury-perfume-director.md)
- [双语 MJ 摄影 Prompt 导演](prompt-packs/bilingual-mj-photo-director.md)
- [美股收盘日报完整版](prompt-packs/us-market-daily-report.md)

## 项目结构

```text
content/                 独立 Prompt 与 Workflow 内容条目
data/                    网站和工具使用的结构化索引
prompts/                 保留旧链接的分类阅读入口
prompt-packs/            原始复杂工作流入口
assets/images/           案例图片
agents/skills/           可分发的 Agent Skill
website/                 数据驱动静态网站
scripts/                 迁移、构建和校验工具
tests/                   内容合同测试
docs/                    内容规范、使用和许可文档
```

`content/` 是结构化内容层；`data/` 和 `website/data/` 是自动生成结果，不应手工编辑。旧的 `prompts/` 和 `prompt-packs/` 链接继续保留，避免公开链接立即失效。

## 本地构建与验证

需要 Node.js 20 或更高版本，不依赖第三方 npm 包。

```powershell
npm run build
npm test
npm run validate
```

首次从旧版分类文件重新迁移时：

```powershell
npm run migrate:legacy
```

此命令会重新生成 `content/prompts/` 和 `content/workflows/`，不要在存在未同步的结构化内容修改时运行。

## 新增内容

新增或修改 Prompt 前，请阅读：

- [贡献指南](CONTRIBUTING.md)
- [内容结构规范](docs/CONTENT_SCHEMA.md)
- [Prompt 标准模板](docs/PROMPT_TEMPLATE.md)

提交前必须运行测试和内容校验。Pull Request 会自动检查重复 ID、缺失文件、无效分类、图片路径和旧链接锚点。

## 使用边界

- Prompt 不保证不同模型产生完全相同的结果。
- 产品功效、材质、认证、价格、库存和平台规则必须使用真实、当前、可验证的信息。
- 涉及产品视觉时，应明确材质和表面工艺，例如金属拉丝、镜面金属、哑光塑料、透明玻璃、织物纹理或木纹。
- 只上传和使用你有权处理的图片、视频、字体、商标和人物素材。
- 第三方品牌、平台和模型名称归各自权利人所有。

## 许可证

本仓库采用双许可：

- Prompt、文档和原创内容默认使用 [CC BY-NC 4.0](LICENSE)。
- 网站代码、自动化脚本和 Agent Skill 使用 [MIT License](LICENSE-CODE)。
- 第三方图片、商标和案例不自动包含在上述授权中，详见 [NOTICE.md](NOTICE.md) 和[许可证说明](docs/LICENSING.md)。

由于内容许可证包含非商业限制，本项目应准确描述为“公开的非商业内容库 + MIT 开源工具代码”，而不是把所有内容笼统称为无限制开源。

## 支持项目

如果 Prompt Library 对你有帮助，欢迎支持项目维护。

<p align="center">
  <img src="assets/sponsor.jpg" alt="项目赞赏码" width="240">
</p>

---

作者：秋水 Kero · X：[@Isonlyonenice](https://x.com/Isonlyonenice)
