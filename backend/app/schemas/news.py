"""新闻资讯相关模式"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID
from app.models.news import NewsCategory, NewsStatus


class NewsBase(BaseModel):
    """新闻基础模式"""
    title: str
    summary: Optional[str] = None
    content: Optional[str] = None
    image_url: Optional[str] = None
    category: NewsCategory = NewsCategory.COMPANY


class NewsCreate(NewsBase):
    """新闻创建模式"""
    pass


class NewsUpdate(BaseModel):
    """新闻更新模式"""
    title: Optional[str] = None
    summary: Optional[str] = None
    content: Optional[str] = None
    image_url: Optional[str] = None
    category: Optional[NewsCategory] = None
    status: Optional[NewsStatus] = None


class NewsResponse(NewsBase):
    """新闻响应模式"""
    id: UUID
    status: NewsStatus
    published_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class NewsAdminResponse(NewsResponse):
    """管理端新闻响应模式（包含预览信息）"""
    preview_token: Optional[str] = None
    created_by: Optional[int] = None


class NewsListResponse(BaseModel):
    """新闻列表响应"""
    id: UUID
    title: str
    summary: Optional[str] = None
    image_url: Optional[str] = None
    category: NewsCategory
    status: NewsStatus
    published_at: Optional[datetime] = None
    created_at: datetime
    
    class Config:
        from_attributes = True


class PreviewTokenResponse(BaseModel):
    """预览令牌响应"""
    preview_url: str
    token: str
