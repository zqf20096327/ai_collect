# Remotion Skills - Remotion 最佳实践技能库

这是一个为 AI 代理提供的 Remotion 最佳实践技能库,包含了使用 Remotion 进行视频创作的详细指南和代码示例。

## 关于 Remotion

Remotion 是一个使用 React 创建视频的强大框架。通过编程方式创建视频,您可以实现精确的控制、动态内容生成和可重复的视频制作流程。

## 技能内容

本仓库包含了 Remotion 开发的核心技能和最佳实践,涵盖以下主题:

### 核心概念
- **[动画](skills/remotion/rules/animations.md)** - Remotion 的基础动画技巧
- **[组合](skills/remotion/rules/compositions.md)** - 定义组合、静态图像、文件夹、默认属性和动态元数据
- **[时序控制](skills/remotion/rules/timing.md)** - Remotion 中的插值曲线 - 线性、缓动、弹簧动画
- **[序列编排](skills/remotion/rules/sequencing.md)** - Remotion 的序列模式 - 延迟、修剪、限制项目持续时间

### 媒体处理
- **[图像](skills/remotion/rules/images.md)** - 使用 Img 组件在 Remotion 中嵌入图像
- **[视频](skills/remotion/rules/videos.md)** - 在 Remotion 中嵌入视频 - 修剪、音量、速度、循环、音调
- **[音频](skills/remotion/rules/audio.md)** - 在 Remotion 中使用音频和声音 - 导入、修剪、音量、速度、音调
- **[GIF 动画](skills/remotion/rules/gifs.md)** - 显示与 Remotion 时间轴同步的 GIF
- **[资源管理](skills/remotion/rules/assets.md)** - 将图像、视频、音频和字体导入 Remotion

### 高级功能
- **[3D 内容](skills/remotion/rules/3d.md)** - 使用 Three.js 和 React Three Fiber 在 Remotion 中创建 3D 内容
- **[字幕显示](skills/remotion/rules/display-captions.md)** - 在 Remotion 中显示字幕,支持 TikTok 风格的分页和单词高亮
- **[字幕导入](skills/remotion/rules/import-srt-captions.md)** - 使用 @remotion/captions 将 .srt 字幕文件导入 Remotion
- **[字幕转录](skills/remotion/rules/transcribe-captions.md)** - 转录音频以在 Remotion 中生成字幕
- **[Lottie 动画](skills/remotion/rules/lottie.md)** - 在 Remotion 中嵌入 Lottie 动画
- **[图表可视化](skills/remotion/rules/charts.md)** - Remotion 的图表和数据可视化模式
- **[地图动画](skills/remotion/rules/maps.md)** - 使用 Mapbox 添加地图并进行动画处理

### 文本和排版
- **[字体加载](skills/remotion/rules/fonts.md)** - 在 Remotion 中加载 Google 字体和本地字体
- **[文本动画](skills/remotion/rules/text-animations.md)** - Remotion 的排版和文本动画模式
- **[文本测量](skills/remotion/rules/measuring-text.md)** - 测量文本尺寸、使文本适应容器以及检查溢出
- **[DOM 节点测量](skills/remotion/rules/measuring-dom-nodes.md)** - 在 Remotion 中测量 DOM 元素尺寸

### 视频处理工具
- **[提取帧](skills/remotion/rules/extract-frames.md)** - 使用 Mediabunny 在特定时间戳从视频中提取帧
- **[获取视频时长](skills/remotion/rules/get-video-duration.md)** - 使用 Mediabunny 获取视频文件的时长(秒)
- **[获取视频尺寸](skills/remotion/rules/get-video-dimensions.md)** - 使用 Mediabunny 获取视频文件的宽度和高度
- **[获取音频时长](skills/remotion/rules/get-audio-duration.md)** - 使用 Mediabunny 获取音频文件的时长(秒)
- **[视频解码检查](skills/remotion/rules/can-decode.md)** - 使用 Mediabunny 检查浏览器是否可以解码视频

### 配置和优化
- **[参数化](skills/remotion/rules/parameters.md)** - 通过添加 Zod 模式使视频可参数化
- **[计算元数据](skills/remotion/rules/calculate-metadata.md)** - 动态设置组合持续时间、尺寸和属性
- **[TailwindCSS](skills/remotion/rules/tailwind.md)** - 在 Remotion 中使用 TailwindCSS
- **[透明视频](skills/remotion/rules/transparent-videos.md)** - 渲染带有透明度的视频
- **[修剪](skills/remotion/rules/trimming.md)** - Remotion 的修剪模式 - 剪切动画的开头或结尾
- **[场景转场](skills/remotion/rules/transitions.md)** - Remotion 的场景转场模式

## 如何使用

这个技能库是为 AI 代理设计的,但也可以作为开发者的参考资料。每个规则文件都包含:

1. **概念说明** - 清晰的功能描述
2. **代码示例** - 可直接使用的代码片段
3. **最佳实践** - 推荐的使用方法和注意事项

## 技能结构

```
remotion-skills/
├── README.md                          # 本文件
└── skills/
    └── remotion/
        ├── SKILL.md                   # 技能元数据和索引
        └── rules/                     # 具体规则文件
            ├── 3d.md
            ├── animations.md
            ├── assets.md
            └── ...
```

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个技能库!

## 许可证

本项目基于原始 [remotion-dev/skills](https://github.com/remotion-dev/skills) 仓库创建,遵循相同的开源许可证。

## 相关链接

- [Remotion 官方网站](https://www.remotion.dev/)
- [Remotion 文档](https://www.remotion.dev/docs)
- [原始技能库](https://github.com/remotion-dev/skills)
