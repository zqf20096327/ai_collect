# cn-humanizer

让 AI 写的中文不再有 AI 味。

一个 agent skill，干两件事：

1. **去 AI 味** — 把 AI 生成的中文改成人话
2. **翻译去腔** — 把英文翻成地道中文，不是"翻译体"中文

识别 18 种中文 AI 写作模式，覆盖 100+ 高频 AI 词汇，附带 12 种翻译腔修正规则。

---

## 起源

英文 AI 腔有自己的一套特征：em dash 满天飞、"delve" 出现八百次、"It's important to note that" 当万能开头。这些特征被研究得很透了，GitHub 上也有不少检测和改写工具（比如 Brandon Wise 的 [ai-humanizer](https://github.com/brandonwise/humanizer)）。

但中文的 AI 痕迹完全是另一回事：

- 英文 AI 爱用 "delve"，中文 AI 爱用"赋能"
- 英文 AI 结尾 "The future looks bright"，中文 AI 结尾"让我们拭目以待"
- 英文 AI 用 em dash 当万能标点，中文 AI 用排比句当万能结构
- 中文还有一个英文没有的问题：翻译腔——大量被动句、"的"字连珠、英文语序残留

搜了一圈，没找到一个专门处理中文 AI 痕迹的工具。

所以自己做了一个。

参考了英文 humanizer 的方法论（模式检测 + 词汇分级 + 统计分析），但所有检测规则、词汇库、改写指南都是从零写的，针对的是中文特有的 AI 写作模式。同时加了翻译模式——把英文翻成中文的时候直接输出"人话"，而不是先翻出翻译腔再改。

---

## 安装

### 让 Agent 安装

直接把这句 prompt 给你的 agent: 

```
帮我安装这个skill: https://github.com/0xtresser/cn-humanizer
```

### 手动安装

复制这行命令，粘贴到终端里回车：

```bash
curl -fsSL https://raw.githubusercontent.com/0xtresser/cn-humanizer/main/install.sh | bash
```

脚本会自动检测你的环境（Claude Code 或 OpenCode），把 skill 安装到对应目录。没有任何依赖——纯 Markdown 文件，不需要 npm、pip 或其他包管理器。

安装完成后重启你的 AI 编码工具即可使用。

### Claude Code 手动安装

```bash
git clone https://github.com/0xtresser/cn-humanizer.git ~/.claude/skills/cn-humanizer
```

### OpenCode 手动安装

```bash
# 克隆到 OpenCode skill 目录
git clone https://github.com/0xtresser/cn-humanizer.git ~/.config/opencode/skills/cn-humanizer
```

### 自定义路径安装

如果你的环境不同，可以指定路径：

```bash
curl -fsSL https://raw.githubusercontent.com/0xtresser/cn-humanizer/main/install.sh | bash -s -- /your/custom/path
```

### 更新

```bash
# Claude Code
cd ~/.claude/skills/cn-humanizer && git pull

# OpenCode
cd ~/.config/opencode/skills/cn-humanizer && git pull
```

### 卸载

```bash
# Claude Code
rm -rf ~/.claude/skills/cn-humanizer

# OpenCode
rm -rf ~/.config/opencode/skills/cn-humanizer
```

---

## 效果对比

### 去 AI 味

改写前：

> 随着人工智能技术的不断发展，大语言模型在各个领域展现出了巨大的潜力。值得注意的是，这一技术不仅赋能了传统行业的数字化转型，更为创新型企业打造了全方位的智能化解决方案。综上所述，人工智能的未来发展前景广阔，让我们拭目以待。

改写后：

> 大语言模型这两年确实火。写代码、做客服、翻译文档，能干的事越来越多。不过说实话，真正用好的公司没几家，多数还在"买了个锤子找钉子"的阶段。最头疼的是幻觉问题——模型编起东西来一本正经的，不懂的人根本分不出真假。

### 翻译去腔

原文：

> The system, which was developed by a team at Google, utilizes a transformer-based architecture that has been specifically designed to handle multilingual tasks.

翻译腔：

> 该系统由谷歌的一个团队所开发，利用了一种基于 Transformer 的架构，该架构被专门设计用于处理多语言任务。

人话：

> Google 一个团队做了个多语言系统，底层用的 Transformer。

---

## 检测的 18 种模式

| # | 模式 | 举例 |
|---|------|------|
| 1 | 意义拔高 | "具有里程碑式的意义" |
| 2 | 空洞归纳 | "综上所述...具有重要意义" |
| 3 | 排比堆砌 | "不仅 A，而且 B，更 C" |
| 4 | 宣传腔 | "亮眼成绩"、"蓬勃发展" |
| 5 | 虚假引用 | "专家指出"、"业内人士认为" |
| 6 | 万能挑战 | "尽管面临挑战...但仍然..." |
| 7 | AI 高频词 | "赋能"、"深耕"、"打造" |
| 8 | 过度连接 | "此外"、"值得一提的是" |
| 9 | "的"字连珠 | 超过 3 个"的"的修饰链 |
| 10 | 四字格滥用 | "齐心协力、攻坚克难、砥砺前行" |
| 11 | 同义替换 | "该技术...这一方案...此项创新..." |
| 12 | 总分总结构 | 开头总述→分点→结尾重复 |
| 13 | 句式均匀 | 每句话长度差不多 |
| 14 | Markdown 滥用 | 过度加粗和列表 |
| 15 | 机器人开场 | "以下是关于...的介绍" |
| 16 | 客服收尾 | "希望以上信息对您有所帮助" |
| 17 | 过度谦虚 | "仅供参考"、"不当之处敬请指正" |
| 18 | 鸡汤收尾 | "让我们拭目以待"、"未来可期" |

---

## 项目结构

```
cn-humanizer/
├── README.md                             # 你正在看的这个
├── install.sh                            # 一键安装脚本
├── SKILL.md                              # 核心指令和模式速查
└── references/
    ├── cn-ai-patterns.md                 # 18 种模式详细说明 + 改写示例
    ├── cn-ai-vocabulary.md               # AI 高频词汇分级表（100+ 词）
    ├── cn-style-guide.md                 # 中文拟人化写作指南
    └── translation-guide.md              # 英中翻译去腔指南（12 种翻译腔）
```

## 支持的环境

| 环境 | 安装方式 |
|------|---------|
| Claude Code | `~/.claude/skills/cn-humanizer/` |
| OpenCode | `~/.config/opencode/skills/cn-humanizer/` |
| Cursor | 复制到项目 `.cursor/skills/` 目录 |
| 其他 | 复制到对应 skill 目录即可 |

纯 Markdown 文件，零依赖。能读 `.md` 文件的 AI 编码环境都能用。

## 致谢

方法论参考了 Brandon Wise 的 [ai-humanizer](https://github.com/brandonwise/humanizer)。所有中文检测规则、词汇库、改写指南为独立编写。

## License

MIT
