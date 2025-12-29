"""媒体文件模型"""
from sqlalchemy import Column, Integer, String, DateTime, Enum as SQLEnum
from datetime import datetime
import enum
from app.core.database import Base


class MediaType(str, enum.Enum):
    """媒体类型"""
    IMAGE = "image"
    DOCUMENT = "document"
    VIDEO = "video"
    OTHER = "other"


class MediaFile(Base):
    """媒体文件表"""
    __tablename__ = "media_files"
    
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    original_filename = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    file_size = Column(Integer)
    mime_type = Column(String)
    media_type = Column(SQLEnum(MediaType), default=MediaType.OTHER)
    uploaded_by = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    category = Column(String)  # 分类：如产品图片、新闻图片等

