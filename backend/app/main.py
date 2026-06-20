"""AI ERP System - Production Application Entry Point"""
import asyncio
import time
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse, ORJSONResponse
from fastapi.exceptions import RequestValidationError
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import uvicorn
import structlog
import orjson

from app.config import settings
from app.db.session import engine, init_db, close_db
from app.api.v1 import (
    inventory, crm, finance, hr, ai_agents, analytics,
    procurement, manufacturing, projects, compliance, auth
)
from app.api.ws import websocket_router
from app.services.event_bus import event_bus
from app.services.ai_orchestrator import ai_orchestrator
from app.services.cache_manager import cache_manager
from app.services.scheduler import scheduler_service
from app.services.monitoring import metrics_collector
from app.middleware.tenant import TenantMiddleware
from app.middleware.audit import AuditMiddleware
from app.middleware.error_handler import ErrorHandlerMiddleware
from app.middleware.request_timing import RequestTimingMiddleware

logger = structlog.get_logger()
limiter = Limiter(key_func=get_remote_address)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan with graceful startup/shutdown."""
    start_time = time.time()
    logger.info("erp_startup_initiated", version=settings.APP_VERSION)

    # Initialize database
    await init_db()

    # Connect infrastructure services
    await cache_manager.connect()
    await event_bus.connect()
    await scheduler_service.start()

    # Initialize AI orchestrator
    await ai_orchestrator.initialize()

    # Start metrics collection
    metrics_collector.start()

    startup_duration = time.time() - start_time
    logger.info("erp_startup_complete", duration_seconds=round(startup_duration, 2))

    yield

    # Graceful shutdown
    logger.info("erp_shutdown_initiated")
    await scheduler_service.stop()
    await cache_manager.disconnect()
    await event_bus.disconnect()
    await ai_orchestrator.shutdown()
    await close_db()
    metrics_collector.stop()
    logger.info("erp_shutdown_complete")

app = FastAPI(
    title="AI ERP System",
    description="AI-Native Enterprise Resource Planning with Agentic Intelligence",
    version=settings.APP_VERSION,
    docs_url="/docs" if settings.DEBUG else None,
    redoc_url="/redoc" if settings.DEBUG else None,
    openapi_url="/openapi.json" if settings.DEBUG else None,
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Middleware stack (order matters: outermost first)
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    allow_headers=["*"],
    expose_headers=["X-Request-ID", "X-Tenant-ID"],
)
app.add_middleware(RequestTimingMiddleware)
app.add_middleware(ErrorHandlerMiddleware)
app.add_middleware(AuditMiddleware)
app.add_middleware(TenantMiddleware)

# API Routes
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(inventory.router, prefix="/api/v1/inventory", tags=["Inventory"])
app.include_router(crm.router, prefix="/api/v1/crm", tags=["CRM"])
app.include_router(finance.router, prefix="/api/v1/finance", tags=["Finance"])
app.include_router(hr.router, prefix="/api/v1/hr", tags=["HR"])
app.include_router(ai_agents.router, prefix="/api/v1/ai", tags=["AI Agents"])
app.include_router(analytics.router, prefix="/api/v1/analytics", tags=["Analytics"])
app.include_router(procurement.router, prefix="/api/v1/procurement", tags=["Procurement"])
app.include_router(manufacturing.router, prefix="/api/v1/manufacturing", tags=["Manufacturing"])
app.include_router(projects.router, prefix="/api/v1/projects", tags=["Projects"])
app.include_router(compliance.router, prefix="/api/v1/compliance", tags=["Compliance"])
app.include_router(websocket_router, prefix="/ws", tags=["WebSocket"])

@app.get("/health", tags=["System"])
@limiter.limit("120/minute")
async def health_check(request: Request):
    """Comprehensive health check with dependency status."""
    return {
        "status": "healthy",
        "version": settings.APP_VERSION,
        "timestamp": time.time(),
        "services": {
            "database": await check_db(),
            "cache": await cache_manager.health(),
            "ai_engine": await ai_orchestrator.health(),
            "message_queue": await event_bus.health(),
            "scheduler": scheduler_service.is_running(),
        }
    }

async def check_db():
    try:
        from sqlalchemy import text
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        return {"status": "connected", "latency_ms": 0}
    except Exception as e:
        return {"status": "disconnected", "error": str(e)}

@app.get("/api/v1/system/metrics", tags=["System"])
async def system_metrics():
    """Prometheus-compatible system metrics."""
    return await metrics_collector.get_metrics()

@app.get("/api/v1/system/info", tags=["System"])
async def system_info():
    """System information and capabilities."""
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": "production" if not settings.DEBUG else "development",
        "features": {
            "ai_agents": settings.ENABLE_AI_AGENTS,
            "realtime_sync": settings.ENABLE_REALTIME_SYNC,
            "audit_logging": settings.ENABLE_AUDIT_LOG,
            "rate_limiting": settings.ENABLE_RATE_LIMITING,
        },
        "modules": [
            "inventory", "crm", "finance", "hr", "procurement",
            "manufacturing", "projects", "compliance", "analytics", "ai"
        ],
        "ai_models": settings.OLLAMA_MODELS,
    }

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        workers=1 if settings.DEBUG else settings.UVICORN_WORKERS,
        access_log=settings.DEBUG,
        log_level="info" if settings.DEBUG else "warning",
    )
