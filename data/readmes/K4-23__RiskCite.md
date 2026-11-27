# 📌 项目介绍

上传企业材料，输出对应的风险清单，每条结论均包含材料原文出处与相关法条作为证据支撑。

## 📚 知识库

知识库需要自己上传建立，本项目建立了法规和案例两个知识库，参考模板在`docs`文件夹。

## 🚀 快速开始

环境要求：Python 3.12+、Node 18+。

**1. 配置**

```bash
cp env.example env
```

`env` 里填模型配置：`LLM_API_KEY`、`LLM_BASE_URL`、`LLM_MODEL`，任意 OpenAI 兼容接口即可。`EMBEDDING_*` 和 `RERANKER_*` 可选。

**2. 启动后端**

```bash
cd backend
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python run.py
```

macOS 和 Linux 把 `.venv\Scripts\python` 换成 `.venv/bin/python`。

**3. 启动前端**

```bash
cd frontend
npm install
npm run dev
```

**4. 使用**

打开 <http://localhost:5173>，点击「新建评估」上传企业材料自动分析。

## 📄 许可证

[Apache-2.0](LICENSE)
