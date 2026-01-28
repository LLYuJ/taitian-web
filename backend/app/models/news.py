"""新闻资讯模型"""
from sqlalchemy import Column, Integer, String, Text, DateTime, Enum as SQLEnum
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from datetime import datetime
import enum
import uuid
from app.core.database import Base


class NewsCategory(str, enum.Enum):
    """新闻分类"""
    COMPANY = "company"      # 公司新闻
    EXHIBITION = "exhibition"  # 展会现场


class NewsStatus(str, enum.Enum):
    """新闻状态"""
    DRAFT = "draft"          # 草稿（编辑中/预览中）
    PUBLISHED = "published"  # 已发布


class News(Base):
    """新闻资讯表"""
    __tablename__ = "news"
    
    # UUID 主键
    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    title = Column(String(255), nullable=False)
    summary = Column(String(500))  # 摘要
    content = Column(Text)  # 正文内容
    image_url = Column(String(500))  # 封面图URL
    category = Column(SQLEnum(NewsCategory), default=NewsCategory.COMPANY)
    
    # 发布状态（枚举）
    status = Column(SQLEnum(NewsStatus), default=NewsStatus.DRAFT)
    published_at = Column(DateTime, nullable=True)
    
    # 预览令牌（永久有效）
    preview_token = Column(String(64), nullable=True, index=True)
    
    # 时间戳
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 创建者（User.id 是整数类型）
    created_by = Column(Integer, nullable=True)
