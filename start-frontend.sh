#!/bin/bash

echo "==================================="
echo "启动泰田集团官网前端服务"
echo "==================================="

cd frontend

# 检查是否安装了Node.js
if ! command -v node &> /dev/null
then
    echo "错误: 未找到Node.js"
    echo "请先安装Node.js: https://nodejs.org/"
    exit 1
fi

# 安装依赖
if [ ! -d "node_modules" ]; then
    echo "正在安装依赖..."
    npm install
fi

# 启动服务
echo "启动Vite开发服务器..."
echo "访问地址: http://localhost:5173"
echo "==================================="

npm run dev

