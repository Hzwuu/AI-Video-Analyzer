# AI-Video-Analyzer

[![CI](https://github.com/Hzwuu/AI-Video-Analyzer/actions/workflows/ci.yml/badge.svg)](https://github.com/Hzwuu/AI-Video-Analyzer/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.12-3776AB)
![Lint](https://img.shields.io/badge/lint-ruff-261230)
![Tests](https://img.shields.io/badge/tests-pytest-0A9EDC)

AI 短视频爆款分析与生产辅助系统。一个从零开始、按版本迭代的学习项目：目标是在 2026 年 11 月前，做成可公开演示的「后端服务 + 前端页面 + AI 能力」完整作品，并记录每一步工程决策。

## 当前进度

- ✅ 第 1 周：项目结构、用户管理模块、示例数据读取、评分分析、SQLite 建表与增删查、单元测试、整合演示脚本
- 🚧 第 2 周：FastAPI 后端服务（`GET /videos` → 分类筛选 → `POST /analyze` → `GET /report/{id}`）
- ⏳ 之后：MySQL + SQLAlchemy、Vue3 前端、LLM/RAG/Agent 能力、异步任务、Docker 部署

## 技术栈

| 层面 | 当前 | 计划 |
| --- | --- | --- |
| 语言 | Python 3.12 | — |
| 数据 | SQLite（内存） | MySQL + SQLAlchemy |
| 服务 | — | FastAPI + uvicorn |
| 前端 | — | Vue3 |
| 质量 | pytest、ruff、pre-commit、GitHub Actions | 覆盖率报告 |

## 快速开始

```powershell
# 1. 创建并激活虚拟环境
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. 安装依赖（开发依赖含 pytest / ruff / pre-commit）
pip install -r requirements-dev.txt

# 3. 运行整合演示（读取 → 分析 → 入库 → 查询）
python demo.py

# 4. 运行测试与代码检查
python -m pytest
ruff check .
```

### 常用命令（Makefile）

| 命令 | 作用 |
| --- | --- |
| `make install` | 安装运行依赖 |
| `make dev` | 安装开发依赖（含测试与检查工具） |
| `make run` | 运行整合演示 |
| `make test` | 运行单元测试 |
| `make lint` | ruff 代码检查 |
| `make fmt` | ruff 代码格式化 |
| `make check` | 检查 + 测试（提交前用） |
| `make hooks` | 安装 pre-commit 钩子 |

> Windows 上没有 `make` 时，可用 `mingw32-make` 代替。

## 目录结构

```
AI-Video-Analyzer/
├── .github/workflows/ci.yml   # CI：推送后自动跑 ruff + pytest
├── data/
│   └── videos.json            # 示例视频数据
├── tests/
│   └── test_user_manager.py   # 用户模块单元测试
├── database.py                # SQLite 连接、建表与增删查
├── demo.py                    # 整合演示：读取 → 分析 → 入库 → 查询
├── fetch.py                   # 读取 data/videos.json
├── user_manager.py            # 用户管理模块（纯逻辑）
├── video_analyzer.py          # 视频评分与分级
├── .pre-commit-config.yaml    # 提交前自动检查
├── pyproject.toml             # 项目元数据 + ruff / pytest 配置
├── requirements.txt           # 运行依赖
├── requirements-dev.txt       # 开发依赖
└── Makefile                   # 常用命令封装
```

## 工程规范

- **提交信息**：Conventional Commits，如 `feat: 新增分析接口`、`fix: 修复除零问题`、`docs: 补充运行说明`
- **分支**：`feat/xxx`、`fix/xxx`、`docs/xxx`、`chore/xxx`，完成后合并进 `main`
- **提交前**：pre-commit 自动跑 ruff；CI 在每次推送后跑代码检查与全部测试
- **不提交**：密钥（`.env`）、虚拟环境、缓存与数据库文件

## 路线图

| 版本 | 内容 |
| --- | --- |
| v0.1 | 脚本层：数据读取、评分、SQLite、单元测试 ✅ |
| v0.2 | FastAPI 服务：`GET /videos`、分类筛选、`POST /analyze`、`GET /report/{id}` 🚧 |
| v0.3 | MySQL + SQLAlchemy、注册登录最小接口 |
| v0.4 | Vue3 前端 MVP |
| v0.5 | LLM 统一接口 + RAG 最小闭环、异步任务改造 |
| v1.0 | Docker 化、公网部署、缓存限流、演示视频 |

---

个人学习项目，用于记录从脚本到服务的完整工程过程。
