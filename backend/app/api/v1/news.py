"""新闻资讯管理API"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from typing import List, Optional
from datetime import datetime
from uuid import UUID
import uuid as uuid_module

from app.core.database import get_db
from app.core.security import get_current_active_user
from app.models.user import User
from app.models.news import News, NewsCategory, NewsStatus
from app.schemas.news import (
    NewsCreate, NewsUpdate, NewsResponse, NewsAdminResponse,
    NewsListResponse, PreviewTokenResponse
)

router = APIRouter()


# ============ 公开接口 ============

@router.get("/list", response_model=List[NewsListResponse])
async def list_published_news(
    category: Optional[NewsCategory] = None,
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db)
):
    """获取已发布的新闻列表（公开接口）"""
    query = select(News).where(News.status == NewsStatus.PUBLISHED)
    
    if category:
        query = query.where(News.category == category)
    
    query = query.order_by(News.published_at.desc()).offset(skip).limit(limit)
    result = await db.execute(query)
    news_list = result.scalars().all()
    
    return news_list


@router.get("/detail/{news_id}", response_model=NewsResponse)
async def get_published_news(
    news_id: UUID,
    db: AsyncSession = Depends(get_db)
):
    """获取已发布的新闻详情（公开接口）"""
    result = await db.execute(
        select(News).where(News.id == news_id, News.status == NewsStatus.PUBLISHED)
    )
    news = result.scalar_one_or_none()
    
    if not news:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="新闻不存在或未发布"
        )
    
    return news


@router.get("/preview/{token}", response_model=NewsResponse)
async def get_news_by_preview_token(
    token: str,
    db: AsyncSession = Depends(get_db)
):
    """通过预览令牌获取新闻（用于整页预览，公开接口）"""
    result = await db.execute(
        select(News).where(News.preview_token == token)
    )
    news = result.scalar_one_or_none()
    
    if not news:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="预览链接无效"
        )
    
    # 预览令牌永久有效，不检查过期时间
    return news


# ============ 管理接口（需认证） ============

@router.get("/admin/list", response_model=List[NewsAdminResponse])
async def list_all_news(
    category: Optional[NewsCategory] = None,
    status_filter: Optional[NewsStatus] = Query(None, alias="status"),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db)
):
    """获取所有新闻列表，包含草稿（管理接口）"""
    query = select(News)
    
    if category:
        query = query.where(News.category == category)
    if status_filter:
        query = query.where(News.status == status_filter)
    
    query = query.order_by(News.updated_at.desc()).offset(skip).limit(limit)
    result = await db.execute(query)
    news_list = result.scalars().all()
    
    return news_list


@router.get("/admin/{news_id}", response_model=NewsAdminResponse)
async def get_news_admin(
    news_id: UUID,
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db)
):
    """获取新闻详情（管理接口）"""
    result = await db.execute(select(News).where(News.id == news_id))
    news = result.scalar_one_or_none()
    
    if not news:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="新闻不存在"
        )
    
    return news


@router.post("", response_model=NewsAdminResponse)
async def create_news(
    news_data: NewsCreate,
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db)
):
    """创建新闻（默认为草稿状态）"""
    news = News(
        title=news_data.title,
        summary=news_data.summary,
        content=news_data.content,
        image_url=news_data.image_url,
        category=news_data.category,
        status=NewsStatus.DRAFT,  # 默认草稿状态
        created_by=current_user.id
    )
    
    db.add(news)
    await db.commit()
    await db.refresh(news)
    
    return news


@router.put("/{news_id}", response_model=NewsAdminResponse)
async def update_news(
    news_id: UUID,
    news_data: NewsUpdate,
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db)
):
    """更新新闻"""
    result = await db.execute(select(News).where(News.id == news_id))
    news = result.scalar_one_or_none()
    
    if not news:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="新闻不存在"
        )
    
    # 更新字段
    update_data = news_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(news, field, value)
    
    # 如果状态改为已发布且之前未发布过，设置发布时间
    if news_data.status == NewsStatus.PUBLISHED and not news.published_at:
        news.published_at = datetime.utcnow()
    
    news.updated_at = datetime.utcnow()
    await db.commit()
    await db.refresh(news)
    
    return news


@router.delete("/{news_id}")
async def delete_news(
    news_id: UUID,
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db)
):
    """删除新闻"""
    result = await db.execute(select(News).where(News.id == news_id))
    news = result.scalar_one_or_none()
    
    if not news:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="新闻不存在"
        )
    
    await db.execute(delete(News).where(News.id == news_id))
    await db.commit()
    
    return {"message": "新闻删除成功"}


@router.post("/{news_id}/publish", response_model=NewsAdminResponse)
async def publish_news(
    news_id: UUID,
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db)
):
    """发布新闻"""
    result = await db.execute(select(News).where(News.id == news_id))
    news = result.scalar_one_or_none()
    
    if not news:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="新闻不存在"
        )
    
    news.status = NewsStatus.PUBLISHED
    if not news.published_at:
        news.published_at = datetime.utcnow()
    news.updated_at = datetime.utcnow()
    
    await db.commit()
    await db.refresh(news)
    
    return news


@router.post("/{news_id}/unpublish", response_model=NewsAdminResponse)
async def unpublish_news(
    news_id: UUID,
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db)
):
    """撤回发布（变为草稿状态）"""
    result = await db.execute(select(News).where(News.id == news_id))
    news = result.scalar_one_or_none()
    
    if not news:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="新闻不存在"
        )
    
    news.status = NewsStatus.DRAFT
    news.updated_at = datetime.utcnow()
    
    await db.commit()
    await db.refresh(news)
    
    return news


@router.post("/{news_id}/preview", response_model=PreviewTokenResponse)
async def generate_preview_token(
    news_id: UUID,
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db)
):
    """生成预览令牌（用于整页预览草稿内容，永久有效）"""
    result = await db.execute(select(News).where(News.id == news_id))
    news = result.scalar_one_or_none()
    
    if not news:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="新闻不存在"
        )
    
    # 如果已有预览令牌，直接返回；否则生成新的
    if not news.preview_token:
        news.preview_token = uuid_module.uuid4().hex
        news.updated_at = datetime.utcnow()
        await db.commit()
    
    # 构建预览 URL（指向详情页面）
    preview_url = f"/zh/news/detail/{news.id}?token={news.preview_token}"
    
    return PreviewTokenResponse(
        preview_url=preview_url,
        token=news.preview_token
    )
