# 面向深度学习的 Python 面向对象编程

**Python OOP for Deep Learning: from Instance to Engineering（从实例到工程）**

> 一本专门写给深度学习学习者的 Python 面向对象教材——填补《动手学深度学习》与《Fluent Python》之间的空白。

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)]()

- 📖 **在线阅读**：直接浏览 [`chapters/`](chapters/) 目录下的 Markdown 章节
- 📕 **PDF 完整版**：[`Python-OOP面向对象编程-教材.pdf`](Python-OOP面向对象编程-教材.pdf)
- 🗺️ **课程总纲**：[`docs/OOP课程总纲.md`](docs/OOP课程总纲.md)（含每章学习目标、易错点、题型的完整表格）
- 🌳 **知识树**：[`docs/OOP知识树.md`](docs/OOP知识树.md)

---

## 为什么需要这本教材？

如果你学过深度学习，很可能遇到过这样的困境：

**理论看懂了，代码看不懂。**

读完《动手学深度学习》（Dive into Deep Learning）、《深度学习》（花书）这类专业教材，反向传播、卷积、注意力机制的数学推导都明白了，可打开一份真实的 PyTorch 项目代码，面对 `nn.Module`、`Dataset`、`DataLoader`、Trainer 这些类的设计时，仍然一头雾水：

- 为什么每个模型都要写 `super().__init__()`？不写会怎样？
- 为什么把层赋值给 `self.conv1` 之后，`model.parameters()` 就能自动找到它？
- `Dataset` 只实现了 `__getitem__` 和 `__len__`，为什么 DataLoader 就能批量取数据？
- `model.train()` 和 `model.eval()` 背后到底改了什么？

**原因很简单：现代深度学习框架是高度面向对象的工程，而这些教材几乎不讲面向对象。**

于是你转向传统的 Python OOP 书籍——《Fluent Python》、《Python编程：从入门到实践》……但很快发现另一个问题：**它们是写给软件工程师的**。案例是 `Animal`/`Dog`、银行账户、图形界面组件，讲的是通用软件工程实践。学完之后，你依然不知道：

- `__getitem__` 这个特殊方法和 PyTorch 的 `Dataset` 有什么关系？
- MRO（方法解析顺序）在真实的神经网络代码里什么时候会用到？
- 描述符协议和 `model.training` 属性有什么联系？

**深度学习教材不讲 OOP，OOP 教材不讲深度学习——这就是本书要填补的空白。**

## 本书的创新

### 1. 每个 OOP 知识点都锚定在深度学习场景上

全书 16 章，每一章都有一个"**AI 迁移点**"板块，把当章知识直接映射到 PyTorch 真实源码：

| OOP 概念 | 深度学习中的对应 |
|---|---|
| 继承 | 自定义模型继承 `nn.Module` |
| `__init__` + 组合 | 在模型中注册子模块（`self.conv1 = nn.Conv2d(...)`） |
| `__getitem__` / `__len__` | 自定义 `Dataset` |
| 特殊方法 `__call__` | `model(x)` 自动调用 `forward`；`torch.no_grad()` |
| 属性查找链与 `__dict__` | `nn.Module` 的参数自动注册机制、`state_dict()` |
| property / 描述符 | `model.training` 属性、`train()` / `eval()` 切换 |
| 装饰器 | `@torch.no_grad()`、`@torch.inference_mode()` |
| 抽象基类（ABC） | 为什么 `Dataset` 被设计成抽象基类 |
| 类方法 / 工厂模式 | `from_pretrained()` 风格的构造接口 |
| 策略模式 / 模板方法 | Trainer 训练框架的组织方式 |
| Mixin | 模块化设计可复用的模型组件 |

### 2. 王道考研式写法：不铺垫、直击要害

本书借鉴考研教辅的写法（每章固定栏目：知识框架图 → 极简解释 → 底层原理 → 最小代码示例 → 常见错误/误区 → 基础题 → 综合题 → AI 场景题 → 与前章联系 → 完成标准），**不从 "Hello World class Animal" 开始铺垫**，基础概念用极小例子讲清，练习尽快进入工程场景。

### 3. 终点是你能独立写出训练框架和 Transformer

全书设计为一条完整的能力阶梯：

```
看懂任何 Python 类的骨架
  → 读懂 Dataset、装饰器、property 等真实设计
    → 能设计接口、写带类型注解的代码
      → 独立实现 nn.Module / Dataset / Trainer
        → 从零手写一个可训练的 Transformer
```

综合项目（Part V）分 6 个阶段：MLP → CNN → VGG → ResNet → Self-Attention → Transformer + Trainer，每一步都标注了它综合运用了前面哪些章节的哪些 OOP 知识点。

## 目录

**Part I — 基础机制**（15h）：看懂任何 Python 类的基本骨架

| 章节 | 内容 | AI 迁移点 |
|---|---|---|
| [第1章 类与实例](chapters/第1章-类与实例.md) | `class`、`__init__`、`self` 的本质 | `nn.Module.__init__`、`Dataset.__init__` |
| [第2章 方法体系](chapters/第2章-方法体系.md) | 实例方法、`@classmethod`、`@staticmethod` | 工厂模式（`from_pretrained()`） |
| [第3章 封装与访问控制](chapters/第3章-封装与访问控制.md) | `_protected`、`__private`、名称改写 | `model._modules`、参数私有化 |
| [第4章 继承与多态](chapters/第4章-继承与多态.md) | 继承、方法重写、duck typing | 自定义模型继承 `nn.Module` |
| [第5章 组合 vs 继承](chapters/第5章-组合vs继承.md) | is-a / has-a 的选择标准 | `nn.Sequential`、模型包含子模块 |

**Part II — Python 对象模型**（17h）：读懂 `Dataset`、装饰器、`property` 等真实设计

| 章节 | 内容 | AI 迁移点 |
|---|---|---|
| [第6章 super() 与 MRO](chapters/第6章-super与MRO.md) | `super()` 的本质、多继承、C3 线性化 | ResNet 残差块中的 `super().__init__()` |
| [第7章 特殊方法](chapters/第7章-特殊方法.md) | `__repr__`、`__len__`、`__getitem__`、`__call__`…… | `Dataset` 协议、`torch.no_grad()` |
| [第8章 property 与描述符](chapters/第8章-property与描述符.md) | `@property`、描述符协议 | `model.training` 的设计原理 |
| [第9章 装饰器](chapters/第9章-装饰器.md) | 函数装饰器、带参装饰器、叠加顺序 | `@torch.no_grad()`、`@torch.inference_mode()` |
| [第10章 属性查找链与 `__dict__`](chapters/第10章-属性查找链与dict.md) | 查找顺序、`__getattr__`、`setattr` | `nn.Module` 参数注册机制、`state_dict()` |

**Part III — 工程化能力**（8h）：读带类型注解的代码，能设计接口

| 章节 | 内容 | AI 迁移点 |
|---|---|---|
| [第11章 抽象基类与协议](chapters/第11章-抽象基类与协议.md) | `abc.ABC`、`@abstractmethod`、`Protocol` | 为什么 `Dataset` 是 ABC |
| [第12章 类型提示](chapters/第12章-类型提示.md) | 注解、`Optional`/`Union`、`TypeVar` | 阅读现代 PyTorch 源码 |
| [第13章 常见设计模式](chapters/第13章-常见设计模式.md) | 策略模式、模板方法、Mixin、工厂 | Trainer 设计、`nn.Module`（模板方法） |

**Part IV — PyTorch 实战**（12h）：独立写训练框架

| 章节 | 内容 |
|---|---|
| [第14章 nn.Module 深度剖析](chapters/第14章-nn.Module深度剖析.md) | 参数/子模块自动注册、`state_dict()`、`train()`/`eval()` |
| [第15章 Dataset + DataLoader](chapters/第15章-Dataset与DataLoader.md) | 自定义 Dataset、`collate_fn`、DataLoader 配置 |
| [第16章 Trainer 框架设计](chapters/第16章-Trainer框架设计.md) | 训练/验证循环、Checkpoint、Early Stopping、Logger |

**Part V — 综合项目**（8h）：从零手写 Transformer

| 阶段 | 内容 | 综合的 OOP 知识点 |
|---|---|---|
| [P1](chapters/PartV-综合项目.md) | MLP + Dataset + 训练 | `__init__`、`forward`、`__getitem__`、`__len__` |
| P2 | CNN + ConvBlock | 组合、`nn.Sequential`、子模块 |
| P3 | VGG + VGGBlock | 继承复用、配置化构建 |
| P4 | ResNet + 残差块 | `forward` 中的 add、继承层次 |
| P5 | Self-Attention | 矩阵运算 + OOP 封装 |
| P6 | Transformer + Trainer | 综合全部 16 章 |

**总学习时间约 60 小时**。完整的章节规划（学习目标、核心知识点、重点易错、题型、AI 迁移点的逐章表格）见 [docs/OOP课程总纲.md](docs/OOP课程总纲.md)。

## 适合谁读

✅ **你**，如果：

- 学过深度学习理论（D2L、吴恩达课程、花书等），但读不懂 PyTorch 代码的类设计
- 正在学习 PyTorch，想搞清楚 `nn.Module` / `Dataset` 背后的机制而不只是照抄模板
- 有 Python 基础语法（变量、循环、函数、字典），OOP 从零开始
- 准备 AI/Machine Learning 方向的面试或科研，需要能独立搭建训练管线

❌ **可能不适合**，如果：

- 你想系统学习软件工程级的 Python（请直接读《Fluent Python》）
- 你想学深度学习理论本身（请先读《动手学深度学习》，再来读本书）

## 使用建议

1. **按顺序学习**：章节之间有明确的前置关系（总纲中每章都标注了前置章节）
2. **动手做题**：每章末尾有基础题、综合题和 AI 场景题，AI 场景题通常是"实现一个简化版的 PyTorch 组件"
3. **对照源码**：学到 Part II 之后，建议打开 PyTorch 源码（如 `torch/utils/data/dataset.py`）对照阅读
4. **完成标准自查**：每章末尾都有"学习完成标准"，达不到就回头补

## 致谢

本书的写作动机和部分场景设计受以下优秀作品的启发：

- 《动手学深度学习》（Dive into Deep Learning）— 李沐 et al.
- 《Fluent Python》— Luciano Ramalho
- 王道考研系列教辅（本书的栏目式写法借鉴于此）

## License

本书内容采用 [MIT License](LICENSE) 开源，欢迎学习、分享、引用。欢迎通过 Issue / PR 反馈错误或贡献改进！
