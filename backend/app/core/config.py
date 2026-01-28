"""应用配置"""
from pydantic_settings import BaseSettings
from typing import List, Optional


class Settings(BaseSettings):
    """应用配置类"""
    
    # 应用信息
    APP_NAME: str = "泰田集团官网"
    API_VERSION: str = "v1"
    DEBUG: bool = True
    
    # 数据库配置 - PostgreSQL
    # 通过环境变量或 .env 文件配置
    # 开发环境(macOS): postgresql+asyncpg://用户名@localhost:5432/taitian
    # 生产环境(Linux): postgresql+asyncpg://postgres:password@localhost:5432/taitian
    DATABASE_URL: str = "postgresql+asyncpg://postgres:password@localhost:5432/taitian"
    
    # JWT配置
    SECRET_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440  # 24小时
    
    # CORS配置
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
    ]
    
    # 文件上传配置
    UPLOAD_DIR: str = "uploads"
    MAX_UPLOAD_SIZE: int = 10 * 1024 * 1024  # 10MB
    ALLOWED_EXTENSIONS: List[str] = [
        ".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg",
        ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".zip"
    ]
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

