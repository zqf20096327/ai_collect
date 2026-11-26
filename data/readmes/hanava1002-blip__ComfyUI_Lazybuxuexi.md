# ComfyUI_Lazybuxuexi

Lazy不学习 的 ComfyUI 自定义节点。装进 `custom_nodes` 后重启即可在节点菜单里看到 `Lazy` 开头的节点。

作者：Lazy不学习  
B站：https://space.bilibili.com/3706970246744888

这个仓库只包含节点代码和示例工作流，不含模型权重。

## 安装

用 ComfyUI Manager：

1. 打开 Manager → **Install via Git URL**
2. 粘贴下面这个地址，安装后重启 ComfyUI
3. 浏览器按 **Ctrl+F5** 强刷页面

```text
https://github.com/hanava1002-blip/ComfyUI_Lazybuxuexi
```

或者手动克隆。文件夹名请保持 `ComfyUI_Lazybuxuexi`：

```text
cd ComfyUI/custom_nodes
git clone https://github.com/hanava1002-blip/ComfyUI_Lazybuxuexi.git
```

然后重启 ComfyUI，并 Ctrl+F5。

节点本身不额外安装 Python 包，用的是 ComfyUI 自带的环境。部分功能要配合已有的模型节点，例如 MiniMax H3、Wan、Krea2、Qwen、YuE，以及超分 / RIFE 补帧。缺哪个，对应功能会在运行时提示。

## 节点

| 一组 | 做什么 |
|------|--------|
| Lazy 导演台 / 逐段生成 / 视频段拼合 | Wan2.2 Remix 时间线，每段单独 high→low |
| Lazy MinimaxH3 导演台 / H3 逐段生成 / 段拼合 | H3 分镜与多参 |
| Lazy Krea2、Qwen2.1、合并台 | 图像工作台和生成 |
| Lazy YuE 工作台 / 生成 | YuE |
| Lazy 超分+补帧、二采修脸、空间二采 | 成片后处理 |
| 多图 / 音频 / 视频加载、提示词、视频保存 | 辅助 |

更细的接法写在仓库里的说明里：

- `Lazy_使用说明.txt`：Wan 导演台
- `Lazy_H3_使用说明.txt`：Minimax H3 导演台

## 示例工作流

在 ComfyUI 里用 **Workflow → Open** 打开 `example_workflows` 下的文件：

- `Lazy_Wan_Remix_逐段生成_干净版.json`
- `Lazy_H3_导演台_逐段.json`
- `Lazy_Krea2_合并台.json`
- `Lazy_Qwen2.1_合并台.json`
- `Lazy_K2Qwen_合并台.json`
- `Lazy_合并台.json`
- `Lazy_YuE_工作台.json`

工作流里的模型路径按你自己机器上的文件改。权重不会随这个仓库下载。

## 自定义风格

节点运行后，会在 `custom_nodes/ComfyUI_Lazybuxuexi_zidingyi` 里分开保存 Krea、Qwen、合并台、YuE 的自定义风格。这是每台电脑自己的资料，不在本仓库里。

## 许可

GPL-3.0。Wan 采样相关逻辑继承 WhatDreamsCost / WanMoeKSampler。
