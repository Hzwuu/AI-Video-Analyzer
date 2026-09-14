# AI-Video-Analyzer

AI 短视频爆款分析与生产辅助系统。目标是一个可运行、可演示的前后端 MVP，用真实项目记录从零到上线的完整过程。

## 当前进度

- 已完成：Git 与项目结构、用户管理模块、示例数据读取、视频评分分析、SQLite 连接与建表、单元测试、整合演示脚本
- 进行中：第 1 周收尾（环境、Git 与 Python 工程写法）
- 计划中：FastAPI 后端服务、MySQL 与 SQLAlchemy、Vue3 前端、LLM/RAG/Agent 能力、Docker 部署

## 技术栈

Python 3.12 / SQLite（第 3 周迁移到 MySQL）/ pytest

后续加入：FastAPI、SQLAlchemy、Vue3、Docker

## 目录结构

```
AI-Video-Analyzer/
├── data/
│   └── videos.json              # 示例视频数据
├── tests/
│   └── test_user_manager.py     # 用户模块单元测试
├── database.py                  # 数据库连接、建表与增查函数
├── demo.py                      # 整合演示：读取 → 分析 → 入库 → 查询
├── fetch.py                     # 读取 data/videos.json
├── user_manager.py              # 用户管理模块
├── video_analyzer.py            # 视频评分与分级
├── requirements.txt
└── README.md
```

## 运行步骤

```powershell
# 1. 创建并激活虚拟环境
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. 安装依赖
pip install -r requirements.txt

# 3. 运行整合演示
python demo.py

# 4. 运行单元测试
python -m pytest -q
```

## 示例输出

```
用户已入库： 2 人
读取到视频： 3 条
数据库里的视频报告：
AI短视频测试三 48000 11.48 爆款
AI短视频测试一 12000 7.54 一般
AI短视频测试二 3500 3.66 一般
```

## 评分规则

得分 = (点赞数 / 播放量 + 评论数 / 播放量) × 100，保留两位小数。10 分以上为爆款，3 分以上为一般，其余为待优化。

## 后续计划

- 第 2 周：FastAPI 基础服务（GET /videos、POST /analyze、GET /report/{id}）
- 第 3 周：MySQL 与 SQLAlchemy，接口接入真实数据库
- 10 月：Vue3 前端 MVP、LLM 统一接口、RAG 知识库、基础 Agent
- 11 月：Docker 部署上线与演示视频