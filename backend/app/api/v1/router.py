"""API路由聚合"""
from fastapi import APIRouter
from app.api.v1 import auth, media, news

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["认证"])
api_router.include_router(media.router, prefix="/media", tags=["媒体文件"])
api_router.include_router(news.router, prefix="/news", tags=["新闻资讯"])

