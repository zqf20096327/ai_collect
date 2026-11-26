<p align="center"><img src="assets/omnicad-banner.svg" alt="OmniCAD — editable 2D CAD and evidence-led verification" width="100%"></p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-1683b8?style=flat-square" alt="MIT"></a>
  <a href="pyproject.toml"><img src="https://img.shields.io/badge/Python-3.10%2B-1683b8?style=flat-square" alt="Python 3.10+"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Agent-Codex-1683b8?style=flat-square" alt="Codex"></a>
  <a href="https://github.com/Haruhi764/OmniCAD-Skill/stargazers"><img src="https://img.shields.io/github/stars/Haruhi764/OmniCAD-Skill?style=flat-square" alt="Stars"></a>
  <a href="https://github.com/Haruhi764/OmniCAD-Skill/forks"><img src="https://img.shields.io/github/forks/Haruhi764/OmniCAD-Skill?style=flat-square" alt="Forks"></a>
</p>

<h1 align="center">OmniCAD-Skill — AI CAD 自动绘图与 AutoCAD 自动化</h1>

<p align="center"><strong>让 AI 参与可编辑工程制图，让每一次交付都有据可查。</strong></p>

<p align="center"><a href="README_EN.md">English</a> · <a href="SKILL.md">Agent Skill</a> · <a href="references/v11.md">工作流</a> · <a href="references/validation.md">验收记录</a> · <a href="CHANGELOG.md">更新日志</a></p>

OmniCAD 是我为 Codex 开发的开源 CAD 自动绘图 Skill。它可以根据明确的尺寸和绘图要求生成可编辑 DXF，并在支持的 AutoCAD 环境中输出 DWG 和 PDF。

[快速安装](#安装与快速开始) · [使用说明](SKILL.md) · [更新日志](CHANGELOG.md)

## 自动绘图演示

<p align="center"><img src="assets/OmniCAD-light(1).gif" alt="OmniCAD 自动绘制法兰工程图演示" width="100%"></p>

<p align="center"><sub>真实 OmniCAD 生成的 DXF 几何动画回放与 OQA 验收展示，非 AutoCAD 实时录屏。</sub></p>

## 实际制图案例

真实 AutoCAD 2023 出图，使用仓库中的合成参数，可复现而非概念渲染。

| 阶梯传动轴 | 带凸台法兰 |
| :---: | :---: |
| ![阶梯轴](examples/previews/shaft-c.png) | ![法兰](examples/previews/flange-b.png) |
| [复现参数](examples/shaft-c.json) | [复现参数](examples/flange-b.json) |

其他实践方向：工业车间布置、工艺流程图、建筑屋面排水图。客户图纸暂不公开。

## 目前支持

- 建筑、土木二维制图：轴网、墙线、门窗、构件及标注。
- 机械制图：阶梯轴、法兰、剖面、键槽、倒角及公差标注。
- DXF 局部修改、差异检查与 OQA 验收。
- Windows AutoCAD 原生 DWG 保存与 PDF 出图。

## 安装与快速开始

需要 Python 3.10+。建议使用独立虚拟环境。纯 DXF 使用基础包即可。PDF、图片预检使用 `intake` 附加依赖。原生 DWG/PDF 依赖 Windows、已授权 AutoCAD、可用的出图设置和字体。Poppler 用于 PDF 渲染。

```bash
git clone https://github.com/Haruhi764/OmniCAD-Skill.git
cd OmniCAD-Skill
python -m pip install ".[intake,autocad]"
omnicad mechanical examples/shaft-c.json work-c.json
omnicad build work-c.json work-c.dxf
omnicad oqa work-c.dxf --job work-c.json --domain mechanical --mode standard
omnicad publish work-c.json work-c.dxf native-c --verify-native
```

在 Codex 中使用 Skill 时，将含 [SKILL.md](SKILL.md) 的目录安装到受支持的本地技能目录。CLI 与 Skill 可以分别使用。复用已验证的 [通用支架示例](examples/bracket.json) 时，从 `build` 开始。验收包含人工项目，`publish` 会为缺失的必填视觉证据保留待复核状态。

## 开发计划

- [x] AutoCAD 二维绘图与验收
- [ ] AutoCAD LT 兼容
- [ ] SolidWorks 建模与装配
- [ ] Revit BIM 建模

后续功能尚未集成，具体支持范围见 [验证记录](references/validation.md)。

## 反馈与贡献

欢迎提交 [Issue](https://github.com/Haruhi764/OmniCAD-Skill/issues)，附软件版本及脱敏复现。详细工作流见 [V1.1 文档](references/v11.md)，贡献方式见 [CONTRIBUTING.md](CONTRIBUTING.md)。目前不支持任意 DWG 自动修改、图片自动矢量化或三维建模；工程设计仍需人工复核。

项目采用 [MIT 许可证](LICENSE)，第三方许可见 [来源说明](references/provenance.md)。如果这个项目对你有帮助，欢迎 Star。

---

<p align="center"><img src="assets/omnicad-logo.svg" width="48" alt="OmniCAD logo"></p>
<p align="center"><strong>OmniCAD · Draft / Verify / Deliver</strong></p>
<p align="center"><a href="CONTRIBUTING.md">参与贡献</a> · <a href="https://github.com/Haruhi764/OmniCAD-Skill/issues">问题反馈</a> · <a href="https://github.com/Haruhi764/OmniCAD-Skill/releases">版本下载</a></p>
