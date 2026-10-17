# Dreamy Motion Editorial

把普通随手拍照片，变成高级、朦胧、梦幻、具有动态模糊氛围的视觉图像。

Turn casual snapshots into premium, hazy, dreamlike motion-editorial visuals — preserving the semantic hero while dissolving the environment into directional cinematic motion.

## 这是什么 / What is this

这是一个面向 AI 图生图的**视觉风格分析与提示词生成 Skill**。

它不会简单地对照片加雾、加光晕或整图虚化，而是：

- 提取照片中真正重要的主体、动作、情绪和色彩记忆
- 决定哪些内容保持清晰（Keep）、哪些淡化成运动残影（Fade）、哪些直接删除（Remove）
- 用真实的慢门拖影、风动、光影流动、玻璃反射、蒸汽、飞鸟或交通掠影构建**动态留白**
- 输出完整的中英文图生图提示词、负面提示词、保真约束、构图与参数建议

It is not a filter. It is an art-direction workflow:

- Keep one semantic hero (face, gesture, object, silhouette, or relationship)
- Fade secondary content into large directional motion veils
- Remove clutter, text, and competing detail
- Build **kinetic negative space** instead of blank empty backgrounds

## 核心理念 / Core ideas

| 理念 | 说明 |
| --- | --- |
| Semantic-core | 默认不是完整还原场景，而是提取语义核心 |
| Kinetic negative space | 留白是动态运动场，不是静态纯色背景 |
| Three depth layers | 近镜掠影、中景拖影、背景光色流 |
| Physical motion | 模糊必须来自真实的慢门、风、交通、蒸汽或反射 |
| Sharpness hierarchy | 主体清晰，环境逐步溶解，绝不整图均匀模糊 |

## 适用场景 / Use cases

- 人物街拍 → 高级艺术写真
- 城市与老街 → 电影感动态海报
- 情侣 / 婚纱照 → 朦胧梦幻关系肖像
- 动物照片 → 艺术摄影风格
- 风景 / 旅行照 → 梦幻动态自然影像
- 日常随手拍 → 杂志 / Pinterest / 小红书封面视觉

## 目录结构 / Repository structure

```text
dreamy-motion-editorial/
├── SKILL.md                        # Skill 主文件与工作流
├── agents/
│   └── openai.yaml                 # Agent 界面配置
├── assets/
│   └── dreamy-motion-editorial-icon.svg
├── references/
│   ├── style-system.md             # 诊断、机制、色彩与强度逻辑
│   ├── prompt-recipes.md           # 双语提示词模板与机制模块
│   └── quality-rubric.md           # 质量评分与修复规则
├── scripts/
│   └── analyze_photo.py            # 照片特征 → 方向建议的结构化工具
└── tests/
    ├── test_analyze_photo.py
    └── test_skill_contract.py
```

## 安装 / Installation

### 作为 Codex Skill

把本仓库克隆或复制到 Codex 的 skills 目录：

```powershell
git clone https://github.com/<your-username>/dreamy-motion-editorial.git "$HOME\.codex\skills\dreamy-motion-editorial"
```

然后在对话中直接使用：

```text
使用 $dreamy-motion-editorial 分析这张照片，输出高级朦胧梦幻风格的中英文图生图提示词
```

### 作为 Claude / 其他 Agent Skill

将 `SKILL.md` 与 `references/`、`scripts/`、`assets/` 一起放入对应 Agent 的 skill 目录即可。

## 使用方法 / Usage

### 1. 自然语言调用

向 Agent 提供一张照片，并要求：

```text
使用 $dreamy-motion-editorial 分析这张照片，输出高级朦胧梦幻风格的中文图生图提示词
```

Skill 会输出：

- 照片视觉诊断
- Keep / Fade / Remove 内容分层
- 动态留白与构图建议
- 完整中文图生图提示词
- 负面提示词
- 保真约束与推荐参数

### 2. 结构化方向建议（可选）

用 `analyze_photo.py` 将观察到的照片特征转换为方向建议：

```powershell
python scripts/analyze_photo.py `
  --subject portrait `
  --light hard-sun `
  --motion still `
  --depth layered `
  --background street `
  --risks face,hands,geometry,text `
  --strength dream-haze `
  --fidelity semantic-core `
  --json
```

参数说明：

| 参数 | 可选值 | 说明 |
| --- | --- | --- |
| `--subject` | `portrait` / `group` / `product` / `scene` / `animal` | 主体类型 |
| `--light` | `flat` / `window` / `hard-sun` / `backlit` / `mixed` / `night` | 光线条件 |
| `--motion` | `still` / `walking` / `turning` / `reaching` / `wind` / `traffic` | 画面中已有的动势 |
| `--depth` | `shallow` / `layered` / `deep` | 空间层次 |
| `--background` | `indoor` / `street` / `nature` / `architecture` / `studio` | 背景类型 |
| `--reflection` | flag | 画面是否有玻璃 / 镜面反射 |
| `--flora` | flag | 画面是否有花叶等植物元素 |
| `--risks` | `face` / `faces` / `hands` / `geometry` / `text` | 需要保护的易错结构 |
| `--strength` | `restrained-premium` / `dream-haze` / `experimental-memory` | 风格强度 |
| `--fidelity` | `semantic-core` / `identity-lock` / `experimental-abstraction` | 保真策略 |
| `--json` | flag | 输出结构化 JSON |

### 3. 运行测试

```powershell
python -m unittest discover -s tests -v
```

## 风格机制 / Mechanisms

- `crowd-drift` — 人群慢门漂移
- `floral-diffusion` — 花叶扩散与风动
- `glass-memory` — 玻璃反射与记忆叠影
- `backlit-halation` — 逆光晕染
- `low-angle-color-field` — 低角度色场
- `passing-gesture` — 动作经过的瞬间拖影

每次只选择一个主机制，最多一个辅助机制。

## 输出示例 / Example output

```markdown
## 照片诊断
- 主体：……
- 必须保留：……
## 构图提炼
- Keep / Fade / Remove：……
- 动态覆盖：40–55%
## 中文图生图提示词
……
## 负面提示词
……
## 建议参数
- 比例：4:5
- 重绘强度：0.50–0.62
```

完整示例见 `references/prompt-recipes.md`。

## 许可证 / License

[MIT](LICENSE)

## 致谢 / Credits

本 Skill 的视觉方法论参考了 Pinterest / 杂志 / 独立电影中的高级动态编辑摄影原则；不模仿任何在世艺术家或单一创作者。
