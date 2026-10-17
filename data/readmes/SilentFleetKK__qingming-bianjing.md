<p align="center">
  <a href="https://silentfleetkk.github.io/qingming-bianjing/"><img src="assets/banner.jpg" alt="清明上河 · 汴京：黄昏时分的汴河与虹桥" width="100%"></a>
</p>

<h1 align="center"><img src="assets/logo-512.png" width="40" alt=""> 清明上河 · 汴京</h1>

<p align="center">
  <b>同一份提示词，两座汴京。</b><br>
  让两个大模型各自从零写出《清明上河图》里的北宋汴京——一座可以在浏览器里走进去的实时三维城市。
</p>

<p align="center">
  <a href="https://silentfleetkk.github.io/qingming-bianjing/"><b>在线预览</b></a> ·
  <a href="https://silentfleetkk.github.io/qingming-bianjing/opus-5.5/qingming-bianjing.html">Opus 5.5 版</a> ·
  <a href="https://silentfleetkk.github.io/qingming-bianjing/gpt-6-sol/qingming-bianjing.html">GPT 6 Sol 版</a> ·
  <a href="%E6%B8%85%E6%98%8E%E4%B8%8A%E6%B2%B3%E5%9B%BE-%E6%B1%B4%E4%BA%AC-%E6%8F%90%E7%A4%BA%E8%AF%8D.md">测评提示词</a> ·
  <a href="#english">English</a>
</p>

---

## 两座汴京

<p align="center"><img src="assets/compare.jpg" alt="同一份提示词下两个模型的默认全景对比" width="100%"></p>

九百年前，张择端把北宋汴京的汴河、虹桥和城门内外的街市，画进了一幅五米多长的绢本长卷。
这个仓库把**同一份约五千字的提示词**分别交给 **Claude Opus 5.5** 和 **GPT 6 Sol**，让它们各自从零写出一座可以走进去的汴京。

两个版本都是**单个 HTML 文件**，没有一张外部图片、一个现成模型：屋瓦、木拱桥、漕船、树木与人群全部由代码程序化生成，在浏览器里实时运行。上图是两者打开时的默认视角，都在 1280×800 下截取、不含界面。

## 看点 · Opus 5.5 版

<table>
<tr>
<td width="50%" valign="top"><img src="opus-5.5/screenshots/02-%E8%99%B9%E6%A1%A5%E6%B2%B3%E5%B2%B8-%E6%B8%85%E6%98%8E%E4%B8%8A%E5%8D%88.jpg" alt="大船过虹桥"><br><b>大船过虹桥</b><br>原画最著名的一幕：漕船放倒人字桅，船工撑篙抵住桥身，桥上的人探身张望，岸上有人挥手呼喊。虹桥按《东京梦华录》“其桥无柱，皆以巨木虚架”做成单跨编木拱，河中没有一根桥墩。</td>
<td width="50%" valign="top"><img src="opus-5.5/screenshots/03-%E8%99%B9%E6%A1%A5%E6%A1%A5%E4%B8%8A-%E6%B8%85%E6%98%8E%E4%B8%8A%E5%8D%88.jpg" alt="虹桥桥上的人群"><br><b>走上桥头</b><br>挑担的、推车的、倚着栏杆看船的——六百多个行人与车马沿街往来。人物不画五官，靠幞头、斗笠、长衫、短褐和姿态区分身份，四肢动作全在着色器里计算。</td>
</tr>
<tr>
<td width="50%" valign="top"><img src="opus-5.5/screenshots/04-%E5%9F%8E%E9%97%A8%E8%A1%97%E5%B8%82-%E6%B8%85%E6%98%8E%E4%B8%8A%E5%8D%88.jpg" alt="城门街市"><br><b>宋式城门</b><br>门洞是两侧排叉柱承托的梯形木构门道，不是明清的半圆砖券；出城的驼队正从门洞里走出来。</td>
<td width="50%" valign="top"><img src="opus-5.5/screenshots/05-%E5%B1%95%E5%8D%B7%E7%BB%88%E7%82%B9-%E5%AD%99%E7%BE%8A%E6%AD%A3%E5%BA%97.jpg" alt="孙羊正店的彩楼欢门"><br><b>展卷巡游</b><br>一键“展卷”，镜头按长卷的顺序从郊野沿汴河经过码头与虹桥，穿过城门，停在孙羊正店的彩楼欢门前。</td>
</tr>
</table>

### 三种氛围

| 清明上午 | 黄昏华灯 | 清明春雨 |
|:---:|:---:|:---:|
| <img src="opus-5.5/screenshots/01-%E6%B1%B4%E6%B2%B3%E5%85%A8%E6%99%AF-%E6%B8%85%E6%98%8E%E4%B8%8A%E5%8D%88.jpg" alt="清明上午"> | <img src="opus-5.5/screenshots/06-%E6%B1%B4%E6%B2%B3%E5%85%A8%E6%99%AF-%E9%BB%84%E6%98%8F%E5%8D%8E%E7%81%AF.jpg" alt="黄昏华灯"> | <img src="opus-5.5/screenshots/08-%E6%B1%B4%E6%B2%B3%E5%85%A8%E6%99%AF-%E6%B8%85%E6%98%8E%E6%98%A5%E9%9B%A8.jpg" alt="清明春雨"> |
| <img src="opus-5.5/screenshots/02-%E8%99%B9%E6%A1%A5%E6%B2%B3%E5%B2%B8-%E6%B8%85%E6%98%8E%E4%B8%8A%E5%8D%88.jpg" alt="清明上午的虹桥"> | <img src="opus-5.5/screenshots/07-%E8%99%B9%E6%A1%A5%E6%B2%B3%E5%B2%B8-%E9%BB%84%E6%98%8F%E5%8D%8E%E7%81%AF.jpg" alt="黄昏的虹桥"> | <img src="opus-5.5/screenshots/09-%E8%99%B9%E6%A1%A5%E6%B2%B3%E5%B2%B8-%E6%B8%85%E6%98%8E%E6%98%A5%E9%9B%A8.jpg" alt="春雨中的虹桥"> |

切换时天空、日光、雾气、水色、地面湿度与窗里的灯火一起平滑过渡：黄昏时大约一半人家点起灯，春雨里行人撑起伞。

## 在线预览

- 首页：<https://silentfleetkk.github.io/qingming-bianjing/>
- Opus 5.5 版：<https://silentfleetkk.github.io/qingming-bianjing/opus-5.5/qingming-bianjing.html>（加 `?lang=en` 为英文界面）
- GPT 6 Sol 版：<https://silentfleetkk.github.io/qingming-bianjing/gpt-6-sol/qingming-bianjing.html>

需要支持 WebGL 2 的现代浏览器（Chrome、Edge、Safari、Firefox 的新版本）。手机会自动切到轻量画质。

## 本地运行

页面以 ES 模块方式加载 `vendor/` 里的 Three.js，直接双击 HTML 时浏览器会拦截本地模块脚本，所以要通过网页服务器访问：

```bash
cd 本仓库所在目录
python3 -m http.server 8000 --bind 127.0.0.1
```

然后打开 <http://127.0.0.1:8000/>。

> `--bind 127.0.0.1` 让服务只对本机开放。不加这个参数，服务会监听所有网卡，同一网络下的其他设备都能浏览你启动服务的那个目录。

## 操作（Opus 5.5 版）

| 操作 | 方式 |
|---|---|
| 环视 / 平移 / 推近 | 拖动 / 右键拖动或双指 / 滚轮或双指捏合 |
| 漫步 | `W` `A` `S` `D` 移动，`Q` `E` 升降 |
| 镜头 | `1` 汴河全景 · `2` 虹桥河岸 · `3` 虹桥桥上 · `4` 城门街市 |
| 展卷巡游 | `空格`，巡游中任意操作即可接管镜头 |
| 其他 | `H` 隐藏界面 · `R` 重置视角 · `L` 中文 / English |

右上角还可以切换氛围、画质（高 / 轻量）、环境音（默认关闭，用 Web Audio 实时合成）和保存当前画面。

## 技术要点（Opus 5.5 版）

- **单文件**：约 2,700 行 HTML / CSS / JavaScript，唯一的依赖是 Three.js r160（只收录页面用到的 14 个模块）。
- **程序化城市**：宋式屋顶生成器（悬山、庑殿、歇山，屋面举折内凹、翼角柔和起翘），六百多栋建筑按街道性质自动排布，再按材质合并成少量绘制调用。
- **人群**：实例化渲染 + 着色器骨骼动画，行走、挑担、撑篙、摇橹、坐饮、呼喊、拉纤、倚栏八种动作。
- **水面**：平面实时反射、浑黄偏绿的河水、船行 V 形尾浪与雨点涟漪。
- **大气与性能**：解析积分的高度雾、静态阴影缓存；帧率不足时自动降低渲染分辨率。
- **体验**：中英双语、手机适配、尊重系统的“减少动态效果”设置；运行时不请求任何第三方服务器。

## 测评说明

- 两个版本使用同一份提示词：[清明上河图-汴京-提示词.md](%E6%B8%85%E6%98%8E%E4%B8%8A%E6%B2%B3%E5%9B%BE-%E6%B1%B4%E4%BA%AC-%E6%8F%90%E7%A4%BA%E8%AF%8D.md)。
- Opus 5.5 版在 Claude Code 中完成：按提示词的验收要求用浏览器截图自检并修正；之后应作者要求，又补充了中英文切换、依赖本地化和发布前的安全检查。
- GPT 6 Sol 版是作者在 Codex 中用同一份提示词得到的结果；发布时只把 Three.js 的加载地址改成了仓库内的本地文件，并删去一行 CDN 预连接，其余代码未动。

## 目录结构

```text
├── index.html                    首页（分享链接用这个）
├── opus-5.5/
│   ├── qingming-bianjing.html    Claude Opus 5.5 的作品
│   └── screenshots/              9 张浏览器实际渲染截图
├── gpt-6-sol/
│   ├── qingming-bianjing.html    GPT 6 Sol 的作品
│   └── github-pages/index.html   同一文件的副本
├── 清明上河图-汴京-提示词.md        测评使用的提示词
├── assets/                       标题图、分享卡、印章 logo、图标、对比图
└── vendor/                       Three.js 与字体子集（各附许可证）
```

## 致谢与出处

- **画面依据**：张择端《清明上河图》；虹桥“其桥无柱，皆以巨木虚架”、酒店“门首皆缚彩楼欢门”等描述出自孟元老《东京梦华录》。两者均为公有领域作品。场景是为实时浏览所做的艺术化复原，不是考古意义上的精确还原。
- **测评形式**：参考了宝玉（[@dotey](https://x.com/dotey)）公开发布的 Opus 5.5 与 GPT 6 Astra“日式樱花山谷”三维网页对比测评及其提示词。
- **代码出处说明**：`opus-5.5/qingming-bianjing.html` 中的高度雾实现（替换 three.js 雾效着色器片段的写法）与雨天潮湿材质的写法，共约 13 行，是参考宝玉公开的 Opus 5.5 樱花谷页面（<https://s.baoyu.io/files/sakura-valley-opus-5-5.html>）的实现思路后改写的，写法相近，特此注明。
- **第三方组件**：
  - [Three.js](https://threejs.org/)（MIT）：`vendor/three-0.160.0/`、`vendor/three-0.167.1/`，各附 `LICENSE`；只收录了页面实际用到的模块，文件未作修改。
  - 字体 Ma Shan Zheng、Noto Serif SC、Cormorant Garamond（SIL Open Font License 1.1）：`vendor/fonts/`，附各自的 `OFL-*.txt`；为按页面实际用字生成的子集。

## 许可证

本项目代码与文档的公开署名和许可证待确定；确定后再补充项目 `LICENSE`。`vendor/` 中的第三方组件遵循各自附带的许可证。

---

## English

<p align="center"><img src="assets/og-cover.jpg" alt="Along the River · Bianjing" width="80%"></p>

**Same prompt, two cities.** Two language models — **Claude Opus 5.5** and **GPT 6 Sol** — were each given the same ~5,000-character prompt and asked to write, from scratch, a real-time 3D web page recreating Northern Song Bianjing as painted in *Along the River During the Qingming Festival*. Both results are single HTML files with no external images or 3D models: every roof, the woven timber Rainbow Bridge, the grain boats, trees and crowds are generated procedurally and run live in the browser.

- **Live**: <https://silentfleetkk.github.io/qingming-bianjing/> · [Opus 5.5 version](https://silentfleetkk.github.io/qingming-bianjing/opus-5.5/qingming-bianjing.html?lang=en) · [GPT 6 Sol version](https://silentfleetkk.github.io/qingming-bianjing/gpt-6-sol/qingming-bianjing.html)
- **Highlights of the Opus 5.5 version**: the famous boat lowering its mast to pass under the pier-less Rainbow Bridge; 600+ animated townspeople, carts and camels; a Song-dynasty city gate and festooned tavern gateways; four camera views plus an "unroll the scroll" tour; morning, dusk and spring-rain atmospheres; Chinese / English interface.
- **Run locally**: from the repository root, run `python3 -m http.server 8000 --bind 127.0.0.1` and open <http://127.0.0.1:8000/>. Browsers block ES modules when an HTML file is opened directly.
- **How the versions were made**: the Opus 5.5 version was built in Claude Code, self-checking with browser screenshots as the prompt requires, then prepared for release (bilingual UI, vendored dependencies, security review) at the author's request. The GPT 6 Sol version is the author's result from the same prompt, generated in Codex; only its Three.js import URLs were pointed to the vendored copy (and one CDN preconnect line removed); nothing else was changed.
- **Credits**: based on Zhang Zeduan's painting and Meng Yuanlao's *Dongjing Menghua Lu* (both public domain). The test format follows Bao Yu's ([@dotey](https://x.com/dotey)) public Opus 5.5 vs GPT 6 Astra "sakura valley" comparison. About 13 lines of the Opus 5.5 version (the height-fog shader chunk override and the wet-surface material) were written after studying his published Opus 5.5 sakura-valley page (<https://s.baoyu.io/files/sakura-valley-opus-5-5.html>) and follow a similar approach. Three.js is MIT-licensed; the fonts are SIL OFL 1.1 subsets. Licenses are included in `vendor/`.
- **License**: The project's public attribution and license are pending. Third-party components keep their own licenses.
