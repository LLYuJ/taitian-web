"""媒体文件管理API"""
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from typing import List, Optional
import os
import uuid
import shutil
from pathlib import Path

from app.core.database import get_db
from app.core.security import get_current_active_user
from app.core.config import settings
from app.models.user import User
from app.models.media import MediaFile, MediaType
from app.schemas.media import MediaFileResponse

router = APIRouter()

# 确保上传目录存在
UPLOAD_DIR = Path(settings.UPLOAD_DIR)
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def get_media_type(mime_type: str) -> MediaType:
    """根据MIME类型判断媒体类型"""
    if mime_type.startswith("image/"):
        return MediaType.IMAGE
    elif mime_type.startswith("video/"):
        return MediaType.VIDEO
    elif mime_type in ["application/pdf", "application/msword", 
                       "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                       "application/vnd.ms-excel",
                       "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"]:
        return MediaType.DOCUMENT
    else:
        return MediaType.OTHER


@router.post("/upload", response_model=MediaFileResponse)
async def upload_file(
    file: UploadFile = File(...),
    category: Optional[str] = None,
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db)
):
    """上传文件"""
    # 检查文件扩展名
    file_ext = os.path.splitext(file.filename)[1].lower()
    if file_ext not in settings.ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"不支持的文件类型。允许的类型：{', '.join(settings.ALLOWED_EXTENSIONS)}"
        )
    
    # 生成唯一文件名
    unique_filename = f"{uuid.uuid4()}{file_ext}"
    file_path = UPLOAD_DIR / unique_filename
    
    # 保存文件
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # 获取文件大小
        file_size = os.path.getsize(file_path)
        
        # 检查文件大小
        if file_size > settings.MAX_UPLOAD_SIZE:
            os.remove(file_path)
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"文件大小超过限制（最大{settings.MAX_UPLOAD_SIZE / 1024 / 1024}MB）"
            )
        
        # 保存到数据库
        media_type = get_media_type(file.content_type or "")
        media_file = MediaFile(
            filename=unique_filename,
            original_filename=file.filename,
            file_path=str(file_path),
            file_size=file_size,
            mime_type=file.content_type,
            media_type=media_type,
            uploaded_by=current_user.id,
            category=category
        )
        
        db.add(media_file)
        await db.commit()
        await db.refresh(media_file)
        
        return MediaFileResponse(
            id=media_file.id,
            filename=media_file.filename,
            original_filename=media_file.original_filename,
            file_url=f"/uploads/{media_file.filename}",
            file_size=media_file.file_size,
            mime_type=media_file.mime_type,
            media_type=media_file.media_type,
            category=media_file.category,
            created_at=media_file.created_at
        )
    
    except Exception as e:
        if os.path.exists(file_path):
            os.remove(file_path)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"文件上传失败：{str(e)}"
        )


@router.get("/list", response_model=List[MediaFileResponse])
async def list_files(
    category: Optional[str] = None,
    media_type: Optional[MediaType] = None,
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db)
):
    """获取文件列表"""
    query = select(MediaFile)
    
    if category:
        query = query.where(MediaFile.category == category)
    if media_type:
        query = query.where(MediaFile.media_type == media_type)
    
    query = query.order_by(MediaFile.created_at.desc())
    result = await db.execute(query)
    media_files = result.scalars().all()
    
    return [
        MediaFileResponse(
            id=mf.id,
            filename=mf.filename,
            original_filename=mf.original_filename,
            file_url=f"/uploads/{mf.filename}",
            file_size=mf.file_size,
            mime_type=mf.mime_type,
            media_type=mf.media_type,
            category=mf.category,
            created_at=mf.created_at
        )
        for mf in media_files
    ]


@router.delete("/{file_id}")
async def delete_file(
    file_id: int,
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db)
):
    """删除文件"""
    result = await db.execute(select(MediaFile).where(MediaFile.id == file_id))
    media_file = result.scalar_one_or_none()
    
    if not media_file:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="文件不存在"
        )
    
    # 删除物理文件
    file_path = Path(media_file.file_path)
    if file_path.exists():
        os.remove(file_path)
    
    # 从数据库删除
    await db.execute(delete(MediaFile).where(MediaFile.id == file_id))
    await db.commit()
    
    return {"message": "文件删除成功"}

