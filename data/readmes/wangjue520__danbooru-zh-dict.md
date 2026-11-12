# danbooru-zh-dict

Danbooru 标签**中英字典**：收录 Danbooru 图数 ≥50 的 **125,778** 个标签（2026-10 数据），每个标签都有中文译名、中文同义词、英文/日文别名和一句说明。

适合用来：
- 中文查标签（例如「黑丝」可以查到 `black_thighhighs`、`black_pantyhose`）
- 英文标签看中文含义
- 做 AI 绘画提示词工具、打标器的中文显示、自动补全插件

配套 WebUI 插件：[sd-webui-zh-tag-autocomplete](https://github.com/wangjue520/sd-webui-zh-tag-autocomplete)（输入中文自动补全标签、一键中译英）。

| 分类 | 数量 | 平均中文同义词数 |
| --- | --- | --- |
| 通用 | 31,089 | 5.2 |
| 元标签 | 537 | 5.3 |
| 角色 | 36,422 | 2.1 |
| 作品 | 8,660 | 2.2 |
| 画师 | 49,070 | 只收录原名与别名，不翻译 |

---

## 使用指南

### 文件

| 文件 | 大小 | 用途 |
| --- | --- | --- |
| `dist/danbooru_zh_dict.csv` | 17MB | 一行一个标签，UTF-8 BOM，**Excel 可以直接双击打开**；多个值用 `\|` 分隔 |
| `dist/danbooru_zh_dict.json` | 40MB | 以标签为键的字典，方便程序调用 |
| `dist/zh_index.json` | 16MB | **中文 → 标签**的反查表，共 30.6 万个中文词，每个词下的标签按图数排序 |

### 字段

| CSV 列名 | JSON 字段 | 说明 | 示例（black_pantyhose） |
| --- | --- | --- | --- |
| 标签 | （键） | Danbooru 原始标签 | `black_pantyhose` |
| 提示词写法 | `prompt` | 可直接写进 SD 提示词（下划线转空格、括号转义） | `black pantyhose` |
| 分类 | `category` | 通用 / 角色 / 作品 / 画师 / 元标签 | 通用 |
| 图数 | `count` | Danbooru 上使用该标签的图片数 | 302108 |
| 中文名 | `zh` | 主译名 | 黑色连裤袜 |
| 中文同义词 | `zh_synonyms` | 其他中文叫法 | 黑丝 \| 黑色丝袜 \| 黑色裤袜 \| 黑连裤袜 \| 黑裤袜 \| 黑丝袜 \| 黑色打底裤袜 |
| 英文别名 | `en_aliases` | Danbooru 官方别名及常见写法 | |
| 日文/其他别名 | `other_aliases` | 日文名、其他语言叫法 | 黒スト \| 黒ストッキング \| 黒タイツ |
| 说明 | `note` | 一句话说明标签含义 | 连裆包裹双腿的黑色连裤袜，常称黑丝。 |

### 示例：用 Excel 查

双击打开 `danbooru_zh_dict.csv`，按 Ctrl+F 搜索中文，例如「双马尾」，就能找到 `twintails`；「提示词写法」一列可以直接复制使用。

### 示例：用 Python 查

```python
import json

d = json.load(open("dist/danbooru_zh_dict.json", encoding="utf-8"))
idx = json.load(open("dist/zh_index.json", encoding="utf-8"))

# 英文 → 中文
print(d["cowboy_shot"]["zh"], d["cowboy_shot"]["zh_synonyms"])
# 七分身构图 ['大腿以上构图', '牛仔镜头', '七分身', '七分身镜头']

# 中文 → 标签（按常用程度排序）
print(idx["黑丝"])   # ['black_thighhighs', 'black_pantyhose']
print(idx["吾王"])   # ['artoria_pendragon_(fate)', 'saber_(fate)']

# 把中文提示词转成标签
words = ["黑丝", "双马尾", "初音"]
print(", ".join(d[idx[w][0]]["prompt"] for w in words if w in idx))
# black thighhighs, twintails, hatsune miku
```

---

## 质量说明

- 中文底稿来自 [amenorira/danbooru-tags-data-zh](https://github.com/amenorira/danbooru-tags-data-zh)，在此基础上用大模型纠正误译、扩展同义词。例如 `cowboy_shot` 原译「牛仔像」改为「七分身构图」，`censored` 原译「送审的」改为「打码」
- 通用、元标签：DeepSeek V4-Pro 翻译
- 角色、作品：图数 ≥500 的用 grok-4.7 翻译，其余用 DeepSeek Flash
- 热门标签抽查准确；**冷门角色、作品可能有误**，少数同义词会混入下位词（如「手套」下出现「皮手套」）
- 包含成人内容标签的翻译

发现错误欢迎提 issue 或 PR。

---

## 自己重新生成

```bash
# 0. 准备：Python 3.10+，pip install openai pandas
#    设置环境变量 DEEPSEEK_API_KEY、XAI_API_KEY
#    把原始数据下载到 raw/（来源见下文「数据来源」，路径见 scripts/build_base.py 顶部）

python scripts/build_base.py          # 合并数据源 → data/base.jsonl
python scripts/translate.py --cats general,meta --provider deepseek
python scripts/translate.py --cats character,copyright --provider xai --reasoning-effort low --min-count 500 --batch 30
python scripts/translate.py --cats character,copyright --provider deepseek-flash --max-count 500 --out character_copyright_ds --batch 30
python scripts/export.py              # 导出 → dist/
python scripts/build_plugin_data.py   # 生成插件数据（需要插件目录在同级）
```

- `translate.py` 支持断点续跑，中断后重新运行同一条命令即可
- 手动修正可以写进 `data/out_fix.jsonl`，每行一条，格式为 `{"tag": "...", "zh": "...", "syn": [...], "note": "..."}`；导出时它的优先级最高
- 成本参考：grok-4.7 默认推理档的隐藏推理 token 约为输出的 10 倍，务必加 `--reasoning-effort low`

---

## 数据来源与许可

- 标签全集与图数：[licyk/danbooru_tags](https://huggingface.co/datasets/licyk/danbooru_tags)
- 官方别名：[NSFW-API/DanBooruTagsAndWikiDumpSept2025](https://huggingface.co/datasets/NSFW-API/DanBooruTagsAndWikiDumpSept2025)
- 英文别名：[DominikDoom/a1111-sd-webui-tagcomplete](https://github.com/DominikDoom/a1111-sd-webui-tagcomplete)
- 多语言别名：[newtextdoc1111/danbooru-tag-csv](https://huggingface.co/datasets/newtextdoc1111/danbooru-tag-csv)
- 中文底稿：[amenorira/danbooru-tags-data-zh](https://github.com/amenorira/danbooru-tags-data-zh)（MIT）

本仓库以 MIT License 发布，第三方版权声明见 [LICENSE](LICENSE)。
