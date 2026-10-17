# Article Image Gen

Article Image Gen 是一个本机运行的 Markdown 文章配图工作台。上传文章后，它会先分析结构并给出可编辑的配图计划；用户在规划步骤统一确认首图与章节图尺寸、位置、风格和来源，确认后直接开始生成，最后导出包含新 Markdown 与 `images/` 的 ZIP。

## 当前里程碑

`v0.4.0` 已作为 **Local-first Web MVP** 冻结。当前方向是本机 Web 工作台、规划先行、AI 生成与本地上传并存；不再维护 Codex 插件形态，也不提供互联网图片搜索。完整决策与后续边界见 [MILESTONE_V0.4.0.md](./MILESTONE_V0.4.0.md)。

## 已实现

- 上传 UTF-8 `.md`，保留原文并生成稳定的段落锚点
- 以确定性规则识别 H2 主章节、连续 H1 分章和无标题文章的插图锚点；章节图默认紧跟标题，再由 LLM 完善摘要、用途和 alt 文本
- 严格分离规划与 AI 执行：确认方案前不会调用图片生成服务；本地图片只在用户主动选择后上传
- 实时显示结构判断、分析阶段和公开推理摘要
- 在右侧图片位点击“定位”，跳转并高亮左侧文章对应位置
- 可新增、移动和删除正文图片位
- 四步工作流：上传 → 规划 → 生成 → 导出
- 规划时分别设置文章顶部首图和章节图统一尺寸；可选 7 种预设风格，也可仅填写自定义要求，并逐图选择 AI / 本地上传 / 跳过
- 使用兼容 Images API 的服务真实生成图片，多张图片并行执行
- 每张结果可独立重新生成或上传本地图片替换，不影响其他图片
- 首页最近项目可删除；删除会同时移除该项目的文章快照和图片文件
- 导出不覆盖原文，生成带图片引用的 Markdown ZIP

## 模型与服务

右上角“设置”使用一套通用的 OpenAI-compatible 连接：

- 用户填写服务名称、HTTPS Base URL 和一个 API Key。
- 文本分析和图片生成共享这套连接，但分别配置模型 ID；本地图片上传不使用模型服务。
- 适用于实现 `/v1/responses`、`/v1/images/generations` 和 `/v1/models` 的兼容服务，例如 AIHubMix、OpenAI 兼容网关及同类服务。
- 接口协议完全不同的供应商需要单独增加适配器，不能仅靠更换 Base URL 接入。
- 连接检测会验证当前 Key 能否访问两个模型 ID。

API Key 只保存在本机服务的 `data/private-settings.json`，不会写入浏览器、文章任务或导出文件。也可以通过 `MODEL_API_KEY`、`MODEL_API_BASE_URL` 和 `MODEL_SERVICE_NAME` 环境变量提供。

## 提示词与模型调用

- 文章分析先由本地规则确定图片位，再把文章纯文本、标题和既有图片位发送给文本模型；结构化输出只允许更新摘要、表达目标和 alt 文本。
- 图片生成按图片位单独组合“文章标题、图片类型、表达目标、风格、目标尺寸和构图约束”，再调用 Images API。
- 风格按预设、全局自定义要求和图片位单独要求合并；生成画布根据横版、方形或竖版选择，结果再裁切到精确尺寸。
- 实际图片提示词会写入任务快照；重新生成会使用最新配置重新组合。本地图片上传不使用提示词或模型服务。

完整输入结构、固定提示词、画布映射和输出处理见 [TECHNICAL_DESIGN.md 的提示词处理章节](./TECHNICAL_DESIGN.md#62-提示词处理)。

## 本机开发

需要 Node.js 22+。

```bash
cp .env.example .env
npm install
npm run dev
```

打开 [http://127.0.0.1:5173](http://127.0.0.1:5173)。Vite 开发服务器会把 API 和图片请求转发到本机 Fastify 服务。

## 生产式本机运行

```bash
npm run check
npm start
```

打开 [http://127.0.0.1:3000](http://127.0.0.1:3000)。

## 本地文件

运行数据默认写入项目下的 `data/`：

```text
data/
├── article-images.db          # 任务状态与文章快照
├── private-settings.json      # 本机服务设置与可选 API Key
└── sessions/<task-id>/
    ├── source/article.md      # 上传后保存的原文副本
    ├── assets/                # 生成或选中的图片
    └── exports/               # 导出的 ZIP
```

因此文件并非只在生成 ZIP 时落盘：上传、分析和每次任务更新都会持久化，图片成功后也会立即保存；导出阶段只是把现有副本和图片打包。

## 验证

```bash
npm run typecheck
npm test
npm run build
npm audit
```

里程碑决策见 [MILESTONE_V0.4.0.md](./MILESTONE_V0.4.0.md)，产品边界见 [PRODUCT_REQUIREMENTS.md](./PRODUCT_REQUIREMENTS.md)，实现结构见 [TECHNICAL_DESIGN.md](./TECHNICAL_DESIGN.md)。
