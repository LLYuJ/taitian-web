"""媒体文件相关模式"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.media import MediaType


class MediaFileBase(BaseModel):
    """媒体文件基础模式"""
    filename: str
    original_filename: str
    category: Optional[str] = None


class MediaFileCreate(MediaFileBase):
    """媒体文件创建模式"""
    file_path: str
    file_size: int
    mime_type: str
    media_type: MediaType
    uploaded_by: Optional[int] = None


class MediaFileInDB(MediaFileBase):
    """数据库中的媒体文件"""
    id: int
    file_path: str
    file_size: int
    mime_type: str
    media_type: MediaType
    uploaded_by: Optional[int]
    created_at: datetime
    
    class Config:
        from_attributes = True


class MediaFileResponse(BaseModel):
    """媒体文件响应"""
    id: int
    filename: str
    original_filename: str
    file_url: str
    file_size: int
    mime_type: str
    media_type: MediaType
    category: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True

