# 白板遮罩动画 Skill

将中文文章或分镜中的静态线稿，制作成可编辑、可预览的白板手绘遮罩动画，并在确认后导出 MP4。

它不是简单地把整张图渐显：动画会按故事事件的语义顺序逐个揭示区域，手部笔尖贴着遮罩边缘移动；尚未开始的元素保持完全隐藏，因此特别适合文章配图、知识讲解、故事分镜和口播视频。

## 效果示例

**场景：猴子山抢香蕉** —— 依次呈现假山场景、小猴与香蕉、大猴抢夺、围观小朋友的反应。

![猴子山抢香蕉：白板遮罩动画演示](assets/examples/scene-01-monkey-mountain-banana-whiteboard.gif)

原始线稿：[查看 PNG](assets/examples/scene-01-monkey-mountain-banana.png)；高清版本：[查看 MP4](assets/examples/scene-01-monkey-mountain-banana-whiteboard.mp4)。

## 能做什么

- 从文章或分镜拆解出单一核心画面的配图策略
- 为 16:9 暖米黄色线稿图建立像素级的 `annotation.json`
- 依据叙事顺序控制元素的绘制顺序，而不是机械按画面位置排序
- 提供本地预览台：播放、拖动时间轴、编辑区域、方向和时序
- 让手部素材的笔尖随遮罩边缘匀速移动，并加入可复现的轻微抖动
- 对重叠对象使用保护区，避免后续内容提前露出
- 在用户确认后输出 MP4

## 视觉规范

源图采用统一的极简素描风格：暖米黄色纸张背景（建议 `#F5EBD7`）、深灰线条，以及少量橙色（`#FFA500`）点缀。画面应留白充足、构图简洁；不使用文字、标签、写实摄影感、3D 效果或复杂背景。

## 安装与依赖

需要 Python 3，以及以下包：

```bash
pip install pillow numpy opencv-python
```

将此目录放入你的 Agent Skills 目录，或在 Codex 中直接引用 `whiteboard-mask-animation`。

## 素材目录

为每个项目使用如下结构。图片和标注文件必须同名：`foo.png` 对应 `foo.annotation.json`。

```text
assets/whiteboard/<项目名>/
├── scene-01-<名称>.png
├── scene-01-<名称>.annotation.json
└── scene-01-<名称>-whiteboard.mp4
```

## 工作流程

1. 先读取文章或分镜，输出配图策略；每幕只表达一个核心意思，建议承载 25–35 秒口播。
2. 用户确认策略后，生成符合视觉规范的 16:9 线稿源图。
3. 结合文章事件和实际画面，创建同名 `.annotation.json`。绘制顺序应遵循“场景铺垫 → 关键人物/物体 → 动作或变化 → 反应/结果”。
4. 生成区域预览，并在预览台中调整区域、方向和时序。
5. 用户确认预览后，渲染 MP4，并检查开场、中段和结尾帧。

## 标注文件

每个元素使用源图的整数像素坐标，并包含叙事角色、揭示方向、时间和手部轨迹。默认绘制速度为 `150 像素/秒`：横向按区域宽度计算，纵向按区域高度计算。

```json
{
  "sceneId": "scene-01",
  "canvas": { "width": 1920, "height": 1080 },
  "storyBasis": "猴子山上，小猴拿着香蕉，大猴冲来抢夺，孩子们在旁观看。",
  "sceneDurationMs": 8000,
  "elements": [
    {
      "id": "rockery",
      "label": "猴子山场景",
      "sequence": 1,
      "narrativeRole": "故事的场景铺垫",
      "type": "structure",
      "region": { "x": 40, "y": 260, "width": 720, "height": 600 },
      "reveal": {
        "direction": "top_to_bottom",
        "startMs": 400,
        "durationMs": 4000,
        "maskPaddingPx": 22
      },
      "handPath": { "start": [400, 270], "end": [400, 850], "easing": "easeInOut" }
    }
  ]
}
```

当早期区域与后续对象重叠时，在早期元素的 `reveal.protectedRegions` 中列出需要延后显示的矩形区域。这样可以防止矩形遮罩过大而泄露后续线条。

## 本地预览与导出

生成带编号、方向和手部轨迹的检查图：

```bash
python scripts/render_annotation_preview.py <图片路径> <标注路径> <预览图输出路径>
```

启动本地预览台（默认地址为 `http://127.0.0.1:8766`）：

```bash
python scripts/preview_server.py
```

渲染单幕 MP4：

```bash
python scripts/render_mask_whiteboard.py <图片路径> <标注路径> <输出视频路径> assets/drawing-hand.png
```

预览台与渲染器采用相同的遮罩规则：当前模块按进度显示，所有后续区域与保护区都会从遮罩中扣除。未开始模块不会出现在画面中，最终完整画面会至少停留 0.5 秒。

## 质量检查

- 首帧为干净的纸张底色，没有提前露出的线条
- `canvas` 与原图像素尺寸完全一致，所有区域为整数像素坐标且处于画布内
- `sequence` 和 `startMs` 与文章事件顺序一致
- 对重叠模块检查中段帧，确认不存在提前揭示
- 手部笔尖始终贴近当前遮罩边缘
- 结尾帧显示完整源图，并至少停留 0.5 秒

## 仓库内容

```text
whiteboard-mask-animation/
├── SKILL.md                          # Agent 使用说明与完整规范
├── README.md                         # 本文档
├── LICENSE                           # MIT
├── .gitignore
├── assets/
│   ├── drawing-hand.png              # 手部素材
│   ├── preview.html                  # 本地预览界面
│   └── examples/                     # README 示例图片与视频
├── scripts/
│   ├── render_annotation_preview.py  # 标注区域预览图
│   ├── render_mask_whiteboard.py     # MP4 渲染器
│   ├── preview_server.py             # 本地预览服务
│   └── start_preview_server.py       # 后台启动预览服务（Windows）
└── agents/openai.yaml                # Codex 元数据
```

## 贡献

欢迎提交 Issue 或 Pull Request。新增功能请保持预览与渲染规则一致，并使用真实场景验证遮罩、保护区和最终视频效果。

## 许可证

本项目基于 [MIT License](LICENSE) 开源，可自由使用、修改和分发。

## 关于作者

一个爱养鱼的老登 / AI Builder / 用 AI 团队打造一人公司。

抖音、B站、公众号：江哥是老登啊
