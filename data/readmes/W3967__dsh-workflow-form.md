# ComfyUI 工作台 · DSH 插件

[![test](https://github.com/W3967/dsh-workflow-form/actions/workflows/test.yml/badge.svg)](https://github.com/W3967/dsh-workflow-form/actions/workflows/test.yml)

中文 | [English](README.en.md)

把本机 **ComfyUI** 接进 DeepSeek Harness：导入任意 API 格式工作流，自动生成参数表单，侧栏里直接出图。

本地跑 ComfyUI 出图，通常得切到浏览器、在节点图里改参数、再切回来。这个插件把这一整套收进 DSH 的侧栏——参数面板常驻，生成的图和对话并排，不用离开工作流。

内置 **Krea 2** 两个预设（文生图 / 风格参考），开箱即用；其它模型只要在 ComfyUI 里能跑，导进来就有表单。

![面板](docs/panel.png)

---

## 它是通用的，不是 Krea 2 专用

插件的核心不是某一套模型，而是**参数发现**：拿 ComfyUI 自己的 `/object_info` 当元数据，把任意工作流图翻译成表单。

| 信息来自 | 决定了什么 |
|---|---|
| `/object_info` | 每个输入该用下拉、滑块、数字框还是文本框；取值范围；下拉候选项 |
| 工作流的连线 | 哪两个 `CLIPTextEncode` 分别是正面和负面提示词 |
| 一张 60 行的语义规则表 | 「画面描述」「步数」「主模型」这类好读的标签和分组 |
| 同值合并 | `EmptyLatentImage` 和 `ModelSamplingFlux` 都有的 `width`，合成一个控件 |

规则不认识的节点不会报错，只会退化成「Class · field」的通用控件。所以你装什么自定义节点都不影响它工作。

## 特性

- **导入任意工作流**：ComfyUI 里「Save (API Format)」导出的 JSON，粘进来就有表单。
- **内置 Krea 2 预设**：文生图、风格参考，装好就能出图。
- **两种输入**：面板点着用，或者让模型通过 agent 工具调用，两者共用同一条任务队列。
- **参数自动识别**：正负提示词、种子、步数、CFG、尺寸、模型、LoRA 强度、图片输入。
- **任务式生成**：提交即返回，面板轮询进度，支持取消，可看大图、复制路径。
- **队列**：看 ComfyUI 队列里的**所有**任务（不只插件提交的），可移除等待项、清空等待。
- **历史图片**：浏览 `output/` 目录里的全部生成图；点开看大图，可**恢复当时的参数**、在资源管理器里定位、删除。
- **参数预设**：把当前这套参数存成命名预设，下次一键套用。
- **启动与关闭**：ComfyUI 没开时在面板上直接启动；用完了点一下关闭——先卸载模型释放显存，再停进程。
- **跟随宿主主题**：只用 `--dsw-alias-*` 设计令牌，亮色/暗色自动适配。

## 前置条件

1. **ComfyUI** 在跑（默认 `http://127.0.0.1:8188`），版本建议 ≥ 0.26.0。
2. **显卡**：取决于你要跑的工作流。内置 Krea 2 预设用 Q2_K 量化，8 GB 显存可跑（1024² / 8 步约 70 秒）。
3. **工作流能跑通**：先在 ComfyUI 网页里确认这套图能出图，再导进来。

## 可选：让 ComfyUI 后台运行

> 只在 DSH 里用的话，面板上的**启动按钮**就够了（ComfyUI 没开时它会出现）。这一节是给「不想开面板 / 想让 ComfyUI 独立常驻」的情况。

便携版 ComfyUI 双击 `run_nvidia_gpu.bat` 会弹出一个命令行窗口，**关掉窗口服务就停了** —— 很多人第一次用时都踩过这个坑。

[docs/comfyui/](docs/comfyui/) 里有两个小脚本，复制到 ComfyUI 便携版根目录（和 `run_nvidia_gpu.bat` 同级）就能用，不需要改路径：

| 文件 | 作用 |
|---|---|
| `start-silent.vbs` | 双击启动，完全不出现窗口 |
| `stop.bat` | 双击停止，只杀 ComfyUI 进程，别的 Python 不受影响 |

启动后的输出写到同目录的 `comfyui.log`。原来的 `run_nvidia_gpu.bat` 留着 —— 需要实时看日志时用它。

两个脚本都只有十几行，做的事就是：用 `python.exe` 起 `ComfyUI\main.py` 并把窗口隐藏、输出重定向到文件。用之前可以自己读一遍。

## 安装

### 方式一：本地目录（开发用）

```bash
git clone https://github.com/W3967/dsh-workflow-form.git
```

在 Harness 里用 `plugin_manager` 的 `install_bundle`，目标填这个目录的绝对路径。

### 方式二：挂到 profile

把包放进 profile 的 `node_modules`，并在 `cordis.patch.yml` 里加一行：

```yaml
- insert:
    - id: krea2
      name: dsh-workflow-form
      config:
        comfyUrl: 'http://127.0.0.1:8188'
        comfyRoot: 'D:\AI\ComfyUI\ComfyUI_windows_portable\ComfyUI'
```

`config` 只是**初始种子**：面板里保存过的值优先。

## 配置

装好后侧栏出现 ✦ 图标。展开底部「设置」：

| 项 | 说明 |
|---|---|
| ComfyUI 地址 | 默认 `http://127.0.0.1:8188`，反代路径（如 `http://host/comfy`）也支持。 |
| ComfyUI 目录 | 含 `models/`、`input/`、`output/` 的那一层。**必填**，否则读不到生成的图，也复制不了输入图片。 |

## 快速开始

1. 左上角工作流下拉选 **Krea 2 · 文生图**
2. 在「提示词」里写画面描述（英文效果最好）
3. 确认主模型下拉选到了文件
4. 点「生成」（或 `Ctrl/Cmd + Enter`）
5. 结果出现在右侧；点图看大图，缩略图条回看本次会话

参数改动会自动保存，下次打开还是这套值。

## 导入自己的工作流

### 1. 在 ComfyUI 里导出

搭好图、确认能出图之后，用菜单 **Workflow → Save (API Format)** 导出 JSON。

> 只认 **API Format**。UI 格式那个带 `nodes` / `links` 数组的文件是给浏览器用的，这里解析不了。

### 2. 粘进面板

点工作流下拉右边的 **+**，填个名字，把整个 JSON 粘进去，点「导入」。

### 3. 表单自己就出来了

导入后会立刻发现参数。以 Krea 2 文生图为例，18 个参数被分成四组：

```
提示词    画面描述 · 负面提示词
尺寸      宽 · 高 · 张数          （宽和高各自合并了两个节点）
采样      种子 · 步数 · CFG · 采样器 · 调度器 · 降噪强度 · 位移上限/基准
模型      主模型 · 文本编码器 · CLIP 类型 · VAE · LoRA
```

图片输入（`LoadImage`）会变成路径框，旁边有「用最近结果」按钮，可以把刚才生成的图直接填进去。

### 4. 认不出的参数怎么办

落在「其他」组，标签形如 `SomeNode · some_field`，控件仍然可用。想让它好看，两种办法：

- 在 [lib/workflows.js](lib/workflows.js) 的 `RULES` 里加一条匹配规则（一行）
- 或者就这么用，功能不受影响

## 参数是怎么来的

发现算法按顺序做四件事，全部在 [lib/workflows.js](lib/workflows.js) 的 `discoverParams()` 里：

1. **跳过连线**：`inputs: { model: ["7", 0] }` 是引用另一个节点，不是参数。
2. **查声明**：`/object_info` 里这个输入的 `[type, options]`，决定控件、范围、下拉项。
3. **贴语义**：按「class + 字段名」匹配规则表，比如 `KSampler.steps` → 步数。
4. **同值合并**：语义相同且值相同的输入合到一个控件，写回时同时更新所有节点。

正负提示词不靠猜：算法会找采样器的 `positive` / `negative` 输入连到哪个节点，那两个节点的文本就是对应提示词。

## 给模型用

注册了两个 agent 工具：

| 工具 | 作用 |
|---|---|
| `krea2_workflows` | 列出工作流和它们的参数（id、标签、控件、当前值、可选项） |
| `krea2_generate` | 提交一次生成并等待图片，返回绝对路径 |

模型先用 `krea2_workflows` 看清参数名，再用 `krea2_generate` 提交：

```json
{
  "workflow": "krea2-txt2img",
  "values": { "4.text": "a red fox in snow", "8.steps": 12, "6.width": 768 }
}
```

参数 key 就是 `krea2_workflows` 返回的 `params[].id`。

和面板的关系：

- **同一套校验和钳制**，不存在两套逻辑。
- **串行执行**（`isConcurrencySafe: false`）：并发会抢显存，而 ComfyUI 的 `/interrupt` 是全局的。
- **可取消**：模型侧中断时通过 `exec.signal` 松开等待。
- **工具超时 11 分钟**，比任务的 10 分钟上限略长，保证先拿到「任务失败」而不是「工具超时」。

## 和 krea2-mcp 的关系

同一套后端有两个前端，**只需要装一个**：

- **本插件** —— DSH 专属，面板 + 工具。
- **`krea2-mcp`** —— 纯 MCP server，只有工具，任何 MCP 客户端都能用。

两个都装会在工具列表里留下两个几乎相同的能力，模型随机挑，还会同时抢显存。在 DSH 里用插件就够了。

## 架构

```
workflow-form/
├── index.js              Host 半：组装设置、预设存储、路由、工具
├── lib/
│   ├── comfy.js          ComfyUI HTTP 客户端（不含任何节点图）
│   ├── workflows.js      参数发现、图合并、内置预设、用户预设存储
│   ├── settings.js       连接信息 + 当前工作流 + 各工作流的参数值
│   ├── presets.js        参数预设（一组值，不是一张图）
│   ├── jobs.js           任务状态机（连工作流一起提交、轮询、取消）
│   ├── routes.js         /krea2/* HTTP 接口、object_info 缓存、图片路径校验
│   ├── recover.js        读 PNG 里的工作流元数据，还原参数
│   ├── launch.js         没启动时拉起本机 ComfyUI
│   └── tool.js           krea2_workflows / krea2_generate
├── client.js             侧栏图标 + 主面板（动态表单）
├── cordis.patch.yml      bundle 补丁
├── locale/{en,zh}.json   Plugin Manager 里显示的标题与描述
├── docs/panel.png        截图
└── icon.svg
```

**唯一含"图"的地方**是 `workflows.js` 里的 `BUILTIN_PRESETS`，那是两个 Krea 2 的静态 JSON。除此之外没有任何模型或架构知识。

**接口**：

| 方法 | 路径 | 作用 |
|---|---|---|
| GET | `/krea2/status` | ComfyUI 状态、预设列表、当前设置 |
| POST | `/krea2/start` | 启动本机 ComfyUI（便携版） |
| POST | `/krea2/stop` | 卸载模型并关闭本机 ComfyUI |
| GET | `/krea2/workflow?id=` | 某个工作流的参数发现结果 + 保存的值 |
| POST | `/krea2/workflow` | 新增/覆盖用户预设 |
| DELETE | `/krea2/workflow?id=` | 删除用户预设 |
| GET/POST | `/krea2/settings` | 读 / 局部更新设置 |
| POST | `/krea2/generate` | 提交一次生成，立刻返回 job |
| GET | `/krea2/job?id=` | 单个任务状态 |
| GET | `/krea2/jobs` | 最近任务 |
| POST | `/krea2/cancel` | 取消任务 |
| GET | `/krea2/queue` | ComfyUI 队列（运行中 + 等待中） |
| POST | `/krea2/queue` | 移除等待项或清空队列 |
| GET | `/krea2/history?limit=` | 扫描 `output/` 目录的图片 |
| GET | `/krea2/recover?path=` | 从 PNG 元数据恢复当时的参数 |
| POST | `/krea2/reveal` | 在资源管理器里定位文件 |
| DELETE | `/krea2/image?path=` | 删除一张生成图 |
| GET/POST | `/krea2/presets` | 读 / 保存参数预设 |
| DELETE | `/krea2/presets?id=` | 删除参数预设 |
| GET | `/krea2/image?path=` | 生成图字节流 |

`?path=` 会重新解析并校验落在 ComfyUI 的 `output` / `temp` 之内，`..` 穿越与外部路径一律 404。

浏览器用相对路径 `fetch('krea2/...', { credentials: 'same-origin' })` 调这些接口，图片也由 Host 代理，浏览器不直连 ComfyUI。

## 开发

```bash
npm run check   # node --check 所有入口（8 个文件）
npm test        # 25 个测试：参数发现、图合并、路径安全、工具参数
```

没有构建步骤：`client.js` 是浏览器直接加载的普通 JS（`window.__ModuleLoader__` 格式），改完刷新页面即可。

Host 侧改了 `index.js` 或 `lib/` 之后，用 `plugin_manager` 把插件禁用再启用一次，新模块才会加载。

### CI

GitHub Actions 在每次 push 和 PR 时跑 `npm run check` + `npm test`（Node 22，约 15 秒），徽章在页面顶部。

### 发布

```bash
git init
git add -A
git commit -m "feat: generic ComfyUI front end for DeepSeek Harness"

git remote add origin https://github.com/W3967/dsh-workflow-form.git
git branch -M main
git push -u origin main
```

## 已知限制

- **只支持 API 格式**的工作流 JSON。UI 格式（带 `nodes` / `links`）不解析。
- **复杂工作流表单可能不好看**：多段采样、遮罩、条件分支这类图，自动表单会退化成一堆「Class · field」。功能能用，界面不优雅。
- **单次生成取第一个输出节点**的图片；一个工作流有多个 `SaveImage` 时只显示第一个的产物。
- **取消是尽力而为**：ComfyUI 的 `/interrupt` 是全局的，已进入采样的任务可能仍会跑完，面板会立刻标为已取消。
- 单次生成上限 10 分钟。
- 图片输入只接受本机绝对路径，暂不支持拖拽上传。
- **ComfyUI 会缓存执行结果**：参数完全相同的第二次提交会复用上次的输出，可能一两秒就返回（截图里那个「1.5s」就是这么来的）。这是 ComfyUI 自身的行为——换一个种子或改一个字就会重新计算。
- 历史图片管理只覆盖 `output/` 目录：能删除、能在资源管理器里定位，但不能重命名或移动。
- **启动/关闭只在本机有效**：启动还要求便携版（目录旁有 `python_embeded/`）；源码安装、conda 环境和远程 ComfyUI 需要自己管理进程。
- 关闭前会检查队列：插件自己的任务、或 ComfyUI 队列里的任何任务在跑，都会被拒绝（HTTP 409），避免杀掉正在生成的图。

## 注意事项

- **模型权重适用各自的许可证**。内置 Krea 2 预设对应 Krea 2 Community License（商用有条件、有内容过滤义务）。本插件不附带任何模型权重。

## License

MIT（插件代码）。见 [LICENSE](./LICENSE)。
