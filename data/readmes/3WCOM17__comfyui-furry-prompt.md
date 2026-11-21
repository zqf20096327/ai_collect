# comfyui-furry-prompt

本地 Furry 提示词工作流插件，面向 ComfyUI。

它把 **参考图识图、e621 标签导入、中英对照、词典、自选搭配和 WD14 参数写回** 放在同一个侧边面板里，所有处理都在本机完成。

> 非官方项目，与 ComfyUI、e621 或任何模型作者无关联。  
> 当前为 alpha 版本，接口和界面仍可能变化。

![ComfyUI panel](docs/panel.png)

## 功能

- 右侧中英对照面板，不占用画布节点。
- 三类提示词：
  - 参考图释义：只读，可单独删除；
  - e621 导入：从 Edge 扩展或本地接口进入；
  - 我的新增：手动输入、编辑和追加。
- 词典 / 纠错：搜索、修改中文、写回本地用户词典。
- 自选搭配：把词典、用户词条、AI 译文和 e621 标签放在同一张表里，点 `＋` 加入“我的新增”。
- WD14 识图：
  - 提示词 + 参数；
  - 只填提示词；
  - 只调参数。
- e621 导入：
  - 自动中文；
  - 自动负向；
  - 替换 / 追加；
  - 词条 + 调参 / 只填词条 / 只调参数。
- 不自动 Queue，不覆盖画布上未保存的工作流文件。

## 安装

把仓库放进 ComfyUI 的 `custom_nodes`：

```bash
cd <ComfyUI>/custom_nodes
git clone https://github.com/3WCOM17/comfyui-furry-prompt.git
```

重启 ComfyUI，并强制刷新浏览器页面（`Ctrl+F5`）。

面板应该出现在画布右侧。如果没出现，检查：

- `custom_nodes/comfyui-furry-prompt/__init__.py` 是否存在；
- ComfyUI 启动日志是否出现 `[comfyui-furry-prompt] 路由注册失败`；
- 浏览器 Console 是否有 `[furry-prompt]` 报错。

## 依赖

基础依赖：

```bash
pip install -r requirements.txt
```

说明：

- `torch` 不写入 requirements，使用 ComfyUI 自己的 PyTorch；
- WD14 需要 `onnxruntime` 和对应的 ONNX 模型 / CSV；
- 本地翻译需要 `transformers` 和模型文件，二者都是可选项。

### WD14 模型

默认会查找：

```text
<ComfyUI>/custom_nodes/comfyui-wd14-tagger/models/<model>.onnx
<ComfyUI>/custom_nodes/comfyui-wd14-tagger/models/<model>.csv
```

也可以用环境变量指定：

```bash
set FURRY_WD14_MODEL_DIR=<path-to>\wd14\models
```

## 可选：本地翻译模型

翻译默认不启用。模型不随仓库分发。

默认目录：

```text
comfyui-furry-prompt/models/translation/
├─ opus-mt-zh-en/
├─ opus-mt-en-zh/
├─ m2m100-418M/
└─ qwen2.5-1.5b-instruct/
```

也可以用环境变量覆盖：

```bash
set FURRY_TRANSLATE_MODEL_DIR=<path-to>\translation
set FURRY_TRANSLATE_DEVICE=cpu
```

没有模型时，词典、e621 标签和手动编辑仍然可用，只是 AI 翻译按钮不可用。

## 可选：e621 本地词库

仓库 **不包含** 完整 e621 标签数据，原因见 [docs/e621-tags.md](docs/e621-tags.md)。

如果需要 e621 页签的本地搜索，请自己准备：

```text
comfyui-furry-prompt/e621_tags.json
```

格式：

```json
[
  {"t": "anthro", "c": 0, "n": 123456, "a": ["anthromorph"]},
  {"t": "wolf", "c": 5, "n": 654321, "a": []}
]
```

字段：

- `t`：标签；
- `c`：分类编号；
- `n`：使用次数；
- `a`：别名数组。

没有这个文件时，插件不会崩溃，e621 页签会为空。

## 用户词典

第一次保存词典时，插件会创建：

```text
comfyui-furry-prompt/user_dictionary.json
```

这个文件属于用户本地数据，已在 `.gitignore` 中排除，不应提交。

## 隐私

- 不上传图片到第三方。
- 不包含遥测。
- 默认只监听本机 ComfyUI。
- Edge 扩展只访问 e621 页面和 `127.0.0.1:8188`。
- e621 sample 的本地读取只发生在启用 WD14 参数分析时。

## 使用边界

- e621 是 18+ 站点，项目中只使用 SFW 示例。
- 不把 e621 图片当作训练数据。
- 不声称训练或拥有画师作品。
- 不传播原图，不商用。
- 本项目不包含模型权重、e621 完整数据、角色语音或用户词典。

## CORS

Edge 扩展向本地 ComfyUI 发请求时，需要允许本地跨域。例如：

```bash
python main.py --enable-cors-header "*"
```

只建议在本机使用，不要把 8188 暴露到公网。

## 目录

```text
comfyui-furry-prompt/
├─ __init__.py
├─ furry_prompt_core.py
├─ routes.py
├─ translation.py
├─ web/
│  ├─ js/furry_prompt.js
│  └─ tag_dict.json
├─ docs/
│  ├─ panel.png
│  └─ e621-tags.md
├─ requirements.txt
├─ pyproject.toml
├─ PRIVACY.md
├─ SECURITY.md
└─ LICENSE
```

## 状态

alpha。当前重点是本地工作流和面板交互，API、界面、数据格式都可能调整。

## License

MIT。第三方模型、e621 数据、图片和角色语音不适用 MIT，且不随本仓库分发。

