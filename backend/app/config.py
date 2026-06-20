"""Production Configuration with Pydantic Settings v2"""
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

    # Application
    APP_NAME: str = "AI ERP System"
    APP_VERSION: str = "2.0.0-final"
    DEBUG: bool = Field(default=False)
    ENVIRONMENT: str = "production"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    UVICORN_WORKERS: int = 4

    # Security
    SECRET_KEY: str = Field(..., description="256-bit secret for JWT signing")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    PASSWORD_MIN_LENGTH: int = 12
    MAX_LOGIN_ATTEMPTS: int = 5
    LOCKOUT_DURATION_MINUTES: int = 30

    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:3001",
        "https://*.vercel.app",
    ]

    # Database
    DATABASE_URL: PostgresDsn = Field(...)
    DATABASE_POOL_SIZE: int = 20
    DATABASE_MAX_OVERFLOW: int = 10
    DATABASE_POOL_RECYCLE: int = 3600

    # Redis
    REDIS_URL: RedisDsn = Field(...)
    REDIS_DB: int = 0
    REDIS_CACHE_TTL: int = 300

    # RabbitMQ
    RABBITMQ_URL: AmqpDsn = Field(...)
    RABBITMQ_EXCHANGE: str = "erp_events"

    # AI / Ollama
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_TIMEOUT: int = 120
    OLLAMA_MODELS: List[str] = [
        "llama3.1",
        "mistral",
        "codellama",
        "nomic-embed-text",
        "llama3.1:8b",
    ]
    AI_MAX_TOKENS: int = 4096
    AI_TEMPERATURE: float = 0.7
    AI_TOP_P: float = 0.9
    AI_REQUEST_TIMEOUT: int = 60
    AI_MAX_CONCURRENT: int = 10

    # File Storage
    UPLOAD_DIR: str = "/app/uploads"
    MAX_UPLOAD_SIZE_MB: int = 50
    ALLOWED_EXTENSIONS: List[str] = ["pdf", "docx", "xlsx", "csv", "png", "jpg", "json"]

    # Email
    SMTP_HOST: Optional[str] = None
    SMTP_PORT: int = 587
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAIL_FROM: str = "erp@company.com"
    EMAIL_ENABLED: bool = False

    # Monitoring
    SENTRY_DSN: Optional[str] = None
    PROMETHEUS_PORT: int = 9090
    METRICS_ENABLED: bool = True

    # Feature Flags
    ENABLE_AI_AGENTS: bool = True
    ENABLE_REALTIME_SYNC: bool = True
    ENABLE_AUDIT_LOG: bool = True
    ENABLE_RATE_LIMITING: bool = True
    ENABLE_WEBSOCKET: bool = True
    ENABLE_BACKGROUND_JOBS: bool = True

    # Multi-tenant
    DEFAULT_TENANT_ID: str = "default"
    TENANT_ISOLATION_LEVEL: str = "schema"
    MAX_TENANTS_PER_INSTANCE: int = 1000

    # Performance
    CACHE_ENABLED: bool = True
    CACHE_DEFAULT_TTL: int = 300
    BULK_INSERT_BATCH_SIZE: int = 1000
    API_MAX_PAGE_SIZE: int = 100

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
