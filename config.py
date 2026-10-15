# -*- coding: utf-8 -*-
"""ai_collect 配置(声明式 · 单一事实源)。

宇宙口径:stars>=STAR_MIN + PUSHED_DAYS 天内有 push + 非 fork + 未归档。
黑名单改这里;通道由 config 自动推导,无需改脚本。
"""

# ---------- 宇宙口径 ----------
STAR_MIN = 10          # 星线:信噪比,不是编辑性排除
PUSHED_DAYS = 360      # 活跃线:360 天内有 push(宇宙边界)
NEW_STAR_MIN = 3       # 新项目窗口:低星线
NEW_DAYS = 45          # 新项目窗口:创建天数

# ---------- 分片红线 ----------
N_SHARDS = 8           # 池活文件分片数(repo_id % N)
SHARD_MAX_MB = 20      # 单文件红线:超过必须扩片
README_MAX_BYTES = 100 * 1024

# ---------- topic 通道(20 个,2026-10-15 实测验证) ----------
TOPICS = [
    "ai", "artificial-intelligence", "llm", "machine-learning",
    "deep-learning", "transformers", "llm-agent", "ai-agent", "rag",
    "text-generation", "stable-diffusion", "diffusion-model", "comfyui",
    "langchain", "openai-api", "ollama", "local-llm", "inference-engine",
    "vector-database", "mlops",
]

# ---------- org 通道(2026-10-15 API 核验存在) ----------
# dedicated: org 即 AI 产品,过滤线只有 星线+活跃线+fork/archived
# superset : 大厂综合 org,额外要求 挂任一 topic 或 描述命中 AI 关键词
ORG_DEDICATED = [
    # 模型厂商/实验室(国际)
    "openai", "anthropics", "google-deepmind", "meta-llama", "mistralai",
    "xai-org", "cohere-ai", "AI21Labs", "Stability-AI",
    # 模型厂商(国产)
    "QwenLM", "deepseek-ai", "zai-org", "MoonshotAI", "01-ai",
    "Tencent-Hunyuan", "MiniMax-AI", "stepfun-ai", "baichuan-inc",
    # 深度学习框架
    "pytorch", "tensorflow", "PaddlePaddle", "mindspore-ai",
    # 推理/部署
    "vllm-project", "ollama", "ggml-org", "sgl-project",
    # Agent / 应用框架
    "langchain-ai", "llama-index", "crewAIInc",
    # 本地 LLM 应用
    "open-webui", "lobehub",
    # 微调/训练
    "unslothai", "hpcaitech",
    # 网关/可观测
    "BerriAI", "langfuse",
    # RAG / 向量
    "unstructured-io", "qdrant", "chroma-core", "weaviate", "milvus-io", "lancedb",
    # 训练/服务基础设施
    "huggingface", "ray-project", "mlflow", "bentoml", "modelscope",
    # 多模态/开放算法
    "open-mmlab", "InternLM",
]
ORG_SUPERSET = ["microsoft", "nvidia", "bytedance", "intel", "google"]

# superset org 的二级过滤:描述/名称命中任一关键词(不区分大小写)
AI_KEYWORDS = [
    "ai", "llm", "gpt", "agent", "rag", "embedding", "transformer",
    "diffusion", "inference", "fine-tun", "finetun", "chatbot", "copilot",
    "mcp", "deep learning", "machine learning", "generative",
]

# ---------- watch 白名单(官方不打 topic 的仓 + 曾误杀保险) ----------
WATCH = [
    "hiyouga/LLaMA-Factory",                    # 个人号爆款(topic 通道可能覆盖,双保险)
    "AUTOMATIC1111/Stable-Diffusion-WebUI",
    "lllyasviel/Fooocus",
    "danny-avila/LibreChat",
    "binary-husky/gpt_academic",
]

# ---------- 黑名单 ----------
# 用户级(优先):该用户所有仓不采。适合搬运号/刷星号/课程作业号。
EXCLUDE_USERS = []
# 仓库级:"owner/repo"。双保险:拼进搜索查询 + 合并时过滤。
EXCLUDE_REPOS = []
