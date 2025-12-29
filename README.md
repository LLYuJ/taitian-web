# 泰田集团企业官网

现代工业风格的企业官网，包含前端展示和后台管理系统。

## 技术栈

### 前端
- Vue 3 + Vite
- Element Plus (UI组件库)
- Vue Router (路由管理)
- Pinia (状态管理)
- Axios (HTTP客户端)
- 配色方案：白色 + #2CB5BE (青色)

### 后端
- FastAPI
- SQLAlchemy (ORM)
- SQLite (数据库)
- uv (包管理)
- JWT (身份认证)

## 项目结构

```
taitian/
├── backend/          # FastAPI后端
│   ├── app/
│   │   ├── api/      # API路由
│   │   ├── core/     # 核心配置
│   │   ├── models/   # 数据模型
│   │   ├── schemas/  # Pydantic模式
│   │   └── main.py   # 应用入口
│   ├── uploads/      # 静态文件上传目录
│   └── pyproject.toml
└── frontend/         # Vue前端
    ├── src/
    │   ├── views/    # 页面组件
    │   ├── components/ # 可复用组件
    │   ├── router/   # 路由配置
    │   ├── stores/   # 状态管理
    │   └── assets/   # 静态资源
    └── package.json
```

## 功能特性

### 前台展示
- 首页（企业介绍、产品展示）
- 关于泰田（企业信息、装备、理念等）
- 产品中心（各类产品分类展示）
- 行业应用
- 公司动态
- 客户服务

### 后台管理
- 管理员登录
- 静态文件管理（上传/删除图片、文档）
- 内容管理（新闻、产品等）

## 快速开始

### 后端启动

```bash
cd backend
uv pip install -e .
uv run uvicorn app.main:app --reload
```

### 前端启动

```bash
cd frontend
npm install
npm run dev
```

## 默认管理员账号

- 用户名: admin
- 密码: admin123

**请在生产环境中修改默认密码！**

