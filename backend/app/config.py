from functools import lru_cache
from typing import List, Optional
from pydantic import Field, PostgresDsn, RedisDsn, AmqpDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )


    APP_NAME: str = "Enterprise Resource Planning System"
    APP_VERSION: str = "2.0.0-final"
    DEBUG: bool = Field(default=False)
    ENVIRONMENT: str = "production"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    UVICORN_WORKERS: int = 4


    SECRET_KEY: str = Field(..., description="256-bit secret for JWT signing")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    PASSWORD_MIN_LENGTH: int = 12
    MAX_LOGIN_ATTEMPTS: int = 5
    LOCKOUT_DURATION_MINUTES: int = 30


    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:3001",
        "https://*.vercel.app",
    ]


    DATABASE_URL: PostgresDsn = Field(...)
    DATABASE_POOL_SIZE: int = 20
    DATABASE_MAX_OVERFLOW: int = 10
    DATABASE_POOL_RECYCLE: int = 3600


    REDIS_URL: RedisDsn = Field(...)
    REDIS_DB: int = 0
    REDIS_CACHE_TTL: int = 300


    RABBITMQ_URL: AmqpDsn = Field(...)
    RABBITMQ_EXCHANGE: str = "erp_events"


    UPLOAD_DIR: str = "/app/uploads"
    MAX_UPLOAD_SIZE_MB: int = 50
    ALLOWED_EXTENSIONS: List[str] = ["pdf", "docx", "xlsx", "csv", "png", "jpg", "json"]


    SMTP_HOST: Optional[str] = None
    SMTP_PORT: int = 587
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAIL_FROM: str = "erp@company.com"
    EMAIL_ENABLED: bool = False


    SENTRY_DSN: Optional[str] = None
    PROMETHEUS_PORT: int = 9090
    METRICS_ENABLED: bool = True


    ENABLE_REALTIME_SYNC: bool = True
    ENABLE_AUDIT_LOG: bool = True
    ENABLE_RATE_LIMITING: bool = True
    ENABLE_WEBSOCKET: bool = True
    ENABLE_BACKGROUND_JOBS: bool = True


    DEFAULT_TENANT_ID: str = "default"
    TENANT_ISOLATION_LEVEL: str = "schema"
    MAX_TENANTS_PER_INSTANCE: int = 1000


    CACHE_ENABLED: bool = True
    CACHE_DEFAULT_TTL: int = 300
    BULK_INSERT_BATCH_SIZE: int = 1000
    API_MAX_PAGE_SIZE: int = 100

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()