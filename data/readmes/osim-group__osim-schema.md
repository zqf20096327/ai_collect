# OSIM

## 项目简介

OSIM （Open Security Information Model）是 面向 AI 的开源安全数据标准化 项目，通过定义规范统一的安全数据 schema 语义层，破解行业数据碎片化难题，使安全团队、工具和 AI 系统能够在不同的数据源之间进行一致性推理和分析。致力于实现跨厂商、跨产品的安全数据无缝对接，为安全智能化升级与建立协同防御的核心数据打基础！

![OSIM Framework](pictures/homepage-image-2.png)

## 项目背景

随着网络安全形势日益复杂，各类安全产品和系统产生了海量的安全数据。然而，由于缺乏统一的数据标准，不同厂商、不同产品之间的数据格式各异，导致：

- 数据孤岛现象严重
- 跨系统数据分析困难
- 安全运维效率低下
- 威胁情报共享受阻

OSIM项目希望通过建立行业公认的数据标准，解决这些痛点，促进安全生态的健康发展。

## 战略意义

- **标准化：统一安全数据，筑牢流转根基**

  确立统一的安全数据 schema 标准，将异构原始安全数据转化为AI 可理解的结构化格式，为数据规范流转奠定基础，从源头规避 “垃圾输入 = 垃圾输出” 的无效分析，保障数据质量。

- **开放性：开放共享数据，破解孤岛难题**

  秉持开源开放理念，主动推动安全数据的合规开放与高效共享，打破数据孤岛，释放安全数据的协同价值。

- **互联互通：跨域无缝对接，提升交互效能**

  实现跨厂商、跨产品的安全数据无缝对接，消除脆弱的点对点集成模式与技术差异，为安全工具、厂商及平台提供统一语义语言，提升数据交互效率与准确性。

- **生态建设：共建安全生态，赋能产业创新**

  构建健康有序、协同共赢的安全开发生态，汇聚多方力量，助力安全产业持续创新发展。

## 数据 Schema 范围

项目目前涵盖以下安全数据类型的 schema 定义：

- 日志信息（Log）
- 告警信息（Alert）
- 资产信息（Asset）
- 安全事件 (Security Incident)

## 项目结构

```
osim-schema/
├── schemas/                     # Schema 定义文件
│   ├── asset/           
│   ├── log/
│   ├── alert/
│   └── incident/
├── faqs/
│   └── README.md
├── examples/                   # 数据样例
├── pictures/                   # 图片内容
├── CHANGELOG.md             	# 更改日志
├── CONTRIBUTING.md             # 贡献指南
├── CODE_OF_CONDUCT.md          # 行为准则
├── dictionaries.json           # 数据字典
├── valid.json        			# 数据校验
├── README.md          			# 项目说明
├── version.json          		# 版本文件
└── LICENSE                     # 开源协议
```

## 使用场景

- 数据解析：把原始数据转化为符合OSIM标准的json格式

  ![image-20260617100806398](pictures/image-20260617100806398.png)

- 数据质量校验：为你解析数据质量，提供数据质量报告并改进说明

  ![image-20260617100336899](pictures/image-20260617100336899.png)

- 自然语言查询：自然语言转查询语句，支持SQL/ES/SPL 多种格式

  ![image-20260617100503524](pictures/image-20260617100503524.png)

- 安全场景建设：围绕安全场景需求，梳理网络/终端安全事件的内在联系

  ![image-20260617100720663](pictures/image-20260617100720663.png)

## 如何贡献

我们欢迎所有形式的贡献！请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详细的贡献指南。

### 贡献方式

1. **报告问题**: 提交 Issue 反馈 bug 或建议新功能
2. **完善文档**: 帮助改进项目文档和示例
3. **提交代码**: 实现新功能或修复 bug
4. **扩展 Schema**: 添加新的安全数据 schema 定义
5. **推广项目**: 在社区中分享和推广 OSIM

### 开发流程

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 许可证

本项目采用 Apache License 2.0 开源协议，详见 [LICENSE](LICENSE) 文件。

## 联系我们

- OSIM官网：[OSIM Website URL](https://www.osim.space)
- 项目主页：[GitHub Repository URL](https://github.com/osim-group/osim-schema)
- 问题反馈: [GitHub Issues](https://github.com/osim-group/osim-schema/issues)
- 讨论区: [GitHub Discussions](https://github.com/osim-group/osim-schema/discussions)

## 致谢

感谢所有为这个项目做出贡献的开发者、安全专家和组织！

---

**让我们一起推动中国安全行业的数据标准化和开放共享！**

欢迎 Star ⭐ 和 Fork 本项目，参与建设中国安全开源生态！

