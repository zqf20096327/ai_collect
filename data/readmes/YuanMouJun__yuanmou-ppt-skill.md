<sub>🌐 <b>中文</b> · <a href="./README.en.md">English</a> · <a href="https://ppt.resourcehub.dpdns.org">官网预览</a></sub>

<div align="center">

# Yuanmou PPT · 渊眸

> *「打字。回车。一份能在 PowerPoint 里直接改数的成品 PPT。」*
> *"Type. Hit enter. A native editable `.pptx` lands in your lap."*

[![License](https://img.shields.io/badge/License-Apache--2.0-161514?style=flat-square)](./LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/npm%20dependencies-0-C85A32?style=flat-square)](#装上就能用)
[![Skills](https://img.shields.io/badge/skills.sh-Compatible-161514?style=flat-square)](#装上就能用)

<br>

**在你的 agent 里打一句话，拿回一份真能交付的 `.pptx`。**

<br>

不是「AI 生成的网页截图」，也不是改一个数字就得推倒重画的死图——是放进 PowerPoint / WPS 里，文字直接改、图片右键直接换、**双击柱状图直接弹出真 Excel 工作簿**的原生演示文稿。

给它一句主题，它帮你从零策划大纲并匹配 **1.6W+ 商业版式库**；丢给它一张参考截图或 PDF，它 1:1 还原为原生可编辑矢量；丢给它公司 35 MB 的老旧 `.pptx` 模板，它保留原母版骨架原地换血升级，顺手把文件瘦身 97%。

**你在下面主展厅看到的每一套 PPT，都由渊眸引擎原生生成，并直接附上 `.pptx` 源文件供你下载验真。**

```bash
npx skills add YuanMouJun/yuanmou-ppt-skill
```

跨 agent 通用——WorkBuddy、Trae、Qoder、CodeBuddy、OpenClaw、Claude Code、Cursor、Codex、Antigravity 都能装。

[作品展厅](#作品展厅) · [职场实战](#真实职场刚需) · [装上就能用](#装上就能用) · [为什么不一样](#为什么和常见-ppt-工具不一样) · [安全与数据流](./SECURITY.md)

</div>

---

<p align="center">
  <img src="https://github.com/YuanMouJun/yuanmou-ppt-skill/releases/download/media-v2/launch-yuanmou-0.2.gif" alt="Yuanmou PPT 0.2 发布片" width="100%">
</p>

<p align="center"><sub>
  ▲ 0.2 发布片 · 11 秒 · 每一页均由原生 OOXML 引擎渲染出图，内嵌真实 <code>.xlsx</code> Excel 工作簿，支持 PowerPoint / WPS 双击改数
</sub></p>

---

## 作品展厅

下面三套完整展品全部由 `@yuanmou/pptx-kit` 原生生成标准 `.pptx`，经 6 组 15 项自动门禁（0 报错 0 警告）与 LibreOffice 260 DPI 真机渲染直出。每一套都附上了真实 `.pptx` 原件——你可以直接下载，打开 PowerPoint 随便改字、换图、双击图表弹 Excel。

### PPT · 《声如建筑》渊眸声学 AURA 01 发布会

> 「给一台整块铝锭切削的空间声学音箱做一套暗场工业设计发布会 PPT，要有机械剖面引线标注和能双击改数的实测声学图表」

走的是暗场工业画册路子：封面底部一条 20Hz 到 40kHz 的细长声谱标尺压住画面重心，暗影顺着玄武岩底座沉进纯黑；第二页在纯黑背景里直接用细引线标出六处内部紫铜波导结构；第三页左右两张声学实测图内嵌了标准 `.xlsx` 工作簿，第四页切出微距质感与矿物色卡，收尾落在极克制的三段式瑞士网格。👉 [下载这套 `.pptx` 源文件验真](https://github.com/YuanMouJun/yuanmou-ppt-skill/releases/download/media-v2/yuanmou-aura-01-flagship-sample.pptx)

<p align="center"><img src="https://github.com/YuanMouJun/yuanmou-ppt-skill/releases/download/media-v2/case-aura-cover.jpg" width="100%" alt="声如建筑：渊眸声学 AURA 01 发布会封面"></p>
<p align="center"><img src="https://github.com/YuanMouJun/yuanmou-ppt-skill/releases/download/media-v2/case-aura-pages.jpg" width="100%" alt="声如建筑内页四联：硬件剖面、双真 Excel 图表、材质微距、三段式架构"></p>

### PPT · 《光影与混凝土》极简建筑美学讲演

> 「做一个关于清水混凝土与自然光影的极简建筑美学演讲 PPT，克制留白，像建筑展馆画册」

全案约束在黑、灰、暖米白和一缕哑光铜金里，把 68% 的版面主动留给光和墙。封面底部用一条 06:00 到 18:30 的日照入射角标尺定位午后 28° 的光束；第三页把十二小时墙面照度变化做成可双击改数的真 Excel 折线图，右侧只用细线分隔三个光影时刻，不画多余卡片框。👉 [下载这套 `.pptx` 源文件验真](https://github.com/YuanMouJun/yuanmou-ppt-skill/releases/download/media-v2/yuanmou-arch-monograph-sample.pptx)

<p align="center"><img src="https://github.com/YuanMouJun/yuanmou-ppt-skill/releases/download/media-v2/case-arch-cover.jpg" width="100%" alt="光影与混凝土：建筑美学讲演封面"></p>
<p align="center"><img src="https://github.com/YuanMouJun/yuanmou-ppt-skill/releases/download/media-v2/case-arch-pages.jpg" width="100%" alt="光影与混凝土内页四联：光缝留白、十二小时照度真 Excel 折线图、材料反射率、空间结语"></p>

### PPT · 《深空之眼》我们如何看见 130 亿年前的光

> 「做一套讲红外空间望远镜如何穿透星际尘埃拍下深空星云的科普演讲 PPT，纯黑底，照片做主角」

纯黑底色、照片做主角、标注直接落在光学结构上。第二页把镀金六边形铍镜悬浮在纯黑画布正中，六条细引线精准指向镀层、致动器与次镜；第三页把可见光尘埃与红外穿透并排对照，底部拉出一条 0.4–28 μm 光谱窗口；第四页用纯黑原生表格拉平两代望远镜参数。👉 [下载这套 `.pptx` 源文件验真](https://github.com/YuanMouJun/yuanmou-ppt-skill/releases/download/media-v2/yuanmou-cosmos-keynote-sample.pptx)

<p align="center"><img src="https://github.com/YuanMouJun/yuanmou-ppt-skill/releases/download/media-v2/case-cosmos-pages.jpg" width="100%" alt="深空之眼：纯黑红外空间望远镜科普演讲四联"></p>

### 品牌高定 · 跨赛道单页风格样张

> 「轻奢护肤年度规划与智能出行战役总纲——两个截然不同的行业，各自找到对味的视觉语言」

内置的 1.6W+ 商业版式库不是千篇一律的模板套壳，而是按行业气质、构图骨架与内容槽位同构匹配：轻奢护肤走香槟丝绸横幅与极简徽标，智能出行走红黑杂志风战役主视觉与三图拼贴（示例已统一脱敏为「渊眸」品牌）。

<p align="center"><img src="https://github.com/YuanMouJun/yuanmou-ppt-skill/releases/download/media-v2/case-luxury-duo.jpg" width="85%" alt="渊眸美研轻奢画册封面与渊眸智行红黑战役总纲"></p>

---

## 真实职场刚需

画册级美学之外，打工人每天最头疼的三件实战硬活——**20+ 页完整商业提案、既有公司旧模板改版、高密度咨询结构图**——才是渊眸引擎真正拉开代差的地方。

### 23 页完整商业全案 · 渊眸电视「一家一屏 100 天」

> 「给我一套 23 页的大屏电视百日全域推广方案，借用跨行业参考版式骨架，全套内容、水墨切图、菱形画框和 H5 交互表单都要原生可编辑」

整套 23 页一气呵成通过 6 组 15 项门禁（0 告警）。左侧水墨干笔飞白切片与朱砂印章由内置纯 Node 蒙版引擎实时合成，菱形九宫格每一张照片都保留独立图片槽位，在 PowerPoint 里右键就能单张换图。

<p align="center"><img src="https://github.com/YuanMouJun/yuanmou-ppt-skill/releases/download/media-v2/case-yuanmou-tv-grid.jpg" width="92%" alt="渊眸电视 23 页全套原生商业方案精选 12 页"></p>
<p align="center"><img src="https://github.com/YuanMouJun/yuanmou-ppt-skill/releases/download/media-v2/case-yuanmou-tv-craft.jpg" width="75%" alt="水墨飞白切图、45度菱形裁图与九宫格多图画廊特写"></p>

### 1.6W+ 商业版式库 · 高密度咨询结构图样张

给咨询顾问、品牌市场部和 Agency 准备的高密度策略结构页（全域增长三阶闭环矩阵、多阶投放漏斗与搜索回环图、跨行业品牌视觉页，示例统一脱敏为「渊眸」品牌），开箱免登录即可按槽位指纹毫秒级同构挑版；也支持对既有公司 `.pptx` 母本原位换字换图、注入双真 Excel 图表并自动清理冗余媒体瘦身。

<p align="center"><img src="https://github.com/YuanMouJun/yuanmou-ppt-skill/releases/download/media-v2/case-industry-highlights.jpg" width="82%" alt="多行业商业版式与高密度咨询结构图样张"></p>

---

## 装上就能用

```bash
npx skills add YuanMouJun/yuanmou-ppt-skill
```

仅需 **Node.js `>= 22.5`**（零第三方 npm 依赖，仓库约 1.2 MB）。装完直接对你的 agent 说话就行，开箱 Prompt 可直接抄 [`test-prompts.json`](./test-prompts.json)。

<details>
<summary><strong>更多安装方式（WorkBuddy 拖包导入 / 本地克隆 / 真机渲染环境 / 增量升级）</strong></summary>

<br>

**WorkBuddy / 非命令行用户零配置导入**
1. 前往 [Latest Releases](https://github.com/YuanMouJun/yuanmou-ppt-skill/releases/latest) 下载 `yuanmou-ppt-skill.zip`。
2. 打开腾讯 WorkBuddy → 左侧「专家 · 技能 · 连接器」→「上传技能」→ 拖入 `.zip` 即用。

**本地克隆多端同步**
```bash
git clone https://github.com/YuanMouJun/yuanmou-ppt-skill.git
cd yuanmou-ppt-skill
node scripts/install.mjs --target all
node skills/yuanmou-ppt/scripts/deck_cli.mjs check-env
```

**推荐安装本地渲染器（开启 260 DPI 真机审图与左右对照 PDF）**
未安装时引擎仍可零依赖完成构建与 15 项代码门禁（自动降级 `code-gates-only`），安装后解锁真机高清验收：
```bash
# macOS
brew install --cask libreoffice && brew install poppler
# Ubuntu / Debian
sudo apt update && sudo apt install -y libreoffice poppler-utils
# Windows
winget install TheDocumentFoundation.LibreOffice
```

**后续版本升级（国内直连镜像 + SHA-256 逐文件校验）**
```bash
node <SKILL_DIR>/scripts/deck_cli.mjs update
```

</details>

---

## 为什么和常见 PPT 工具不一样

| 对比维度 | 生图 / 截图流 PPT | HTML 转 PPT | 传统 `python-pptx` | **`yuanmou-ppt-skill`** |
| :--- | :--- | :--- | :--- | :--- |
| **原生可编辑性** | 整页死图，不可修改 | 导出后易错位散架 | 原生可编辑 | **100% 原生 OOXML，字/图/形/表全可改** |
| **图表双击改 Excel** | 静态图 | 静态图或前端 Canvas | 配置繁琐、易乱码 | **零依赖内嵌 `.xlsx` 工作簿，双击弹 Excel** |
| **旧 `.pptx` 无损改版** | 不支持 | 不支持 | 易炸母版与蒙版 | **五步原位手术 + 保蒙版换图 + 瘦身 97%** |
| **复杂视觉 1:1 复刻** | 仅风格近似 | 依赖前端 CSS | 缺透明渐变与蒙版 | **`<a:alpha>` 玻璃叠层 + 干笔飞白 + X-Ray 校准** |
| **依赖与体积** | 外部生图 API | 常需无头浏览器 | 50–400 MB 依赖 | **0 npm 依赖（仅 Node >=22.5），克隆 ~1.2 MB** |
| **自动化质检兜底** | 靠肉眼 | 靠肉眼 | 无内置门禁 | **6 组 15 项自动代码门禁 + 真机对照 PDF** |

---

## 能力边界、安全与开源协议

- **诚实边界**：当前聚焦商业演示最高频的 95% 图表类型（柱形 / 条形 / 折线 / 面积 / 饼 / 环图 + 合并原生表）；极冷门的 3D 透视图、双轴组合图仍在持续补齐中。无 LibreOffice 的受限沙箱自动走静态门禁模式。
- **本地优先 · 零遥测**：所有文档、文稿与 `.pptx` **100% 本地处理，绝不上传任何服务器**。全部只读外联端点与本地缓存路径已逐条公开于 **[`SECURITY.md`](./SECURITY.md)**。
- **开源协议**：代码引擎与 Skill 定义采用 **[Apache License 2.0](./LICENSE)**，个人学习、企业汇报与商业项目均免费使用（二次分发请按协议保留 [`NOTICE`](./NOTICE) 署名）。

<details>
<summary>☕ <strong>如果它帮你省下了熬夜做 PPT 的时间，欢迎请作者喝杯咖啡（微信 / 支付宝）</strong></summary>

<br>

项目核心引擎永久开源免费。你的赞赏将用于持续维护引擎迭代与 1.6W+ 免费版式库 CDN 带宽，点击前往 **[赞赏支持页](https://ppt.resourcehub.dpdns.org/sponsor.html)** 或直接扫码：

<p align="center">
  <img src="https://ppt.resourcehub.dpdns.org/assets/qr-wechat.png" width="180" alt="微信赞赏" />
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://ppt.resourcehub.dpdns.org/assets/qr-alipay.png" width="180" alt="支付宝赞赏" />
  <br>
  <sub>左：微信赞赏 · 右：支付宝赞赏</sub>
</p>

</details>
