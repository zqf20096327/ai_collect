# 百度地图 HarmonyOS NEXT Skills

本仓库提供一组面向 **HarmonyOS NEXT 百度地图** 平台的 AI Coding Agent Skills，帮助开发者在智能研发工具（如 Cursor / Claude Code等）中高效完成鸿蒙应用的创建、地图 SDK 集成与 ArkTS 代码开发。

## Skills 概览

本仓库包含以下三个 Skill：

| Skill | 说明 |
| --- | --- |
| [baidu-map-harmonyos-sdk](skills/baidu-map-harmonyos-sdk/) | 百度地图鸿蒙 SDK 开发助手 |
| [harmony-arkts-dev-assistant](skills/harmony-arkts-dev-assistant/) | HarmonyOS ArkTS 开发规范助手 |
| [harmony-empty-project](skills/harmony-empty-project/) | HarmonyOS NEXT 空工程模板生成器 |

---

### baidu-map-harmonyos-sdk

百度地图 HarmonyOS NEXT SDK 的完整开发辅助 Skill，覆盖以下核心能力：

- **地图展示与交互** — 地图组件初始化、手势控件、地图类型切换、个性化地图、室内图、离线地图等
- **覆盖物绘制** — Marker、折线、多边形、圆、气泡信息窗、点聚合、3D 模型、轨迹动画等
- **检索能力** — POI/AOI 检索、地理编码/逆地理编码、建筑物/行政区/天气/公交线路检索、推荐上车点等
- **路线规划** — 驾车、步行、骑行、公交、跨城公交路线规划
- **步骑行导航** — 导航引擎初始化、路线规划、导航控制与状态监听、默认导航 UI、模拟导航、语音播报
- **定位能力** — 前台/后台连续定位、单次定位、经纬度/地址/POI 获取
- **工具类** — 距离/面积计算、坐标转换、空间关系判断、调起百度地图客户端

支持独立包（`@bdmap/base`、`@bdmap/map`、`@bdmap/search`、`@bdmap/util`）和组合包（`@bdmap/map_walkride_search`、`@bdmap/navi_map`），以及定位 SDK（`@bdmap/locsdk`）。

### harmony-arkts-dev-assistant

HarmonyOS ArkTS 综合开发与类型安全最佳实践助手，在生成或重构 ArkTS/ArkUI 代码时提供规范约束，包括：

- 组件装饰器与状态管理（`@State`/`@Prop`/`@Link`/`@Provide`/`@Consume` 等）
- 生命周期规范与资源清理
- 样式布局链式调用顺序
- 类型安全与空值安全（通过 ArkTSCheck）
- 性能优化（对象缓存复用、LazyForEach、状态拆分、异步线程化）
- 错误处理、日志规范与代码审查清单

### harmony-empty-project

HarmonyOS NEXT 空工程模板生成器，可从零创建标准的 Stage 模型 + ArkTS 最小可运行工程，包括：

- 完整的工程目录结构（`AppScope`、`entry` 模块、`hvigor` 配置等）
- 标准配置文件（`oh-package.json5`、`build-profile.json5`、`module.json5` 等）
- 入口能力（`EntryAbility`）与首页（`Index.ets`）
- 资源文件与 SVG 图标占位
- 依赖管理与构建自检流程

---

## 适用环境

- **平台**：HarmonyOS NEXT Developer Preview1 及以上
- **开发工具**：DevEco Studio NEXT Developer Preview1 及以上
- **SDK 版本**：HarmonyOS NEXT Developer Preview1 SDK 及以上
- **设备**：标准系统，华为手机
- **ArkTS 版本**：API 12+

## 目录结构

```
harmony-sdk-skills/
├── CHANGELOG.md              # 变更日志
├── README.md                 # 本文件（中文）
├── README_EN.md              # English README
└── skills/
    ├── baidu-map-harmonyos-sdk/
    │   ├── SKILL.md          # Skill 定义文件
    │   └── references/       # API 文档、开发指南、资源文件
    ├── harmony-arkts-dev-assistant/
    │   └── SKILL.md          # Skill 定义文件
    └── harmony-empty-project/
        └── SKILL.md          # Skill 定义文件
```

## 使用方式

### 1. 克隆本仓库

```bash
git clone <本仓库地址>
cd harmony-sdk-skills
```

### 1. 从 Release 下载（可选）

你也可以直接从 Release 下载附件 `harmony-sdk-skills.zip`，然后解压使用：

```bash
unzip harmony-sdk-skills.zip
cd skills
```

### 2. 将 Skill 注册到你的 AI 助手

把 `skills/` 目录下的 `baidu-map-harmonyos-sdk`、`harmony-arkts-dev-assistant`、`harmony-empty-project` 链接或复制到当前环境对应的 skills 目录，这样 AI 在对话时会自动读取这些文档。

**Claude Code（本地）**

- Skills 目录一般为：`~/.claude/skills/`
- 注册（软链，推荐）：
  ```bash
  ln -sfn "$(pwd)/skills/baidu-map-harmonyos-sdk" ~/.claude/skills/baidu-map-harmonyos-sdk
  ln -sfn "$(pwd)/skills/harmony-arkts-dev-assistant" ~/.claude/skills/harmony-arkts-dev-assistant
  ln -sfn "$(pwd)/skills/harmony-empty-project" ~/.claude/skills/harmony-empty-project
  ```
- 或直接把 `skills/` 下的文件夹复制到 `~/.claude/skills/` 下。

**Cursor**

- Skills 目录一般为：`~/.cursor/skills-cursor/`
- 注册（软链，推荐）：
  ```bash
  ln -sfn "$(pwd)/skills/baidu-map-harmonyos-sdk" ~/.cursor/skills-cursor/baidu-map-harmonyos-sdk
  ln -sfn "$(pwd)/skills/harmony-arkts-dev-assistant" ~/.cursor/skills-cursor/harmony-arkts-dev-assistant
  ln -sfn "$(pwd)/skills/harmony-empty-project" ~/.cursor/skills-cursor/harmony-empty-project
  ```
- 或直接把 `skills/` 下的文件夹复制到 `~/.cursor/skills-cursor/` 下。

### 3. 在对话中使用

在支持 Skills 的客户端里，当你的问题涉及「百度地图」「鸿蒙百度地图 SDK」「HarmonyOS NEXT」「ArkTS 开发规范」「鸿蒙空工程」等关键词时，助手会优先参考本仓库中对应 Skill 的文档来回答，从而给出更贴合百度地图 HarmonyOS NEXT SDK 的代码与用法。

## 变更日志

详见 [CHANGELOG.md](CHANGELOG.md)。

## 许可证

本项目为百度内部项目，仅供授权使用。
