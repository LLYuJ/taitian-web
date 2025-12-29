#!/bin/bash

echo "==================================="
echo "启动泰田集团官网后端服务"
echo "==================================="

cd backend

# 检查是否安装了uv
if ! command -v uv &> /dev/null
then
    echo "错误: 未找到uv包管理器"
    echo "请先安装uv: curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# 同步依赖
echo "正在同步依赖..."
uv sync

# 创建.env文件（如果不存在）
if [ ! -f .env ] && [ -f .env.example ]; then
    echo "创建.env配置文件..."
    cp .env.example .env
elif [ ! -f .env ]; then
    echo "提示: 使用默认配置（所有配置项都有默认值）"
fi

# 启动服务
echo "启动FastAPI服务器..."
echo "访问地址: http://localhost:8000"
echo "API文档: http://localhost:8000/docs"
echo "==================================="

uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

