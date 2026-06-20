""""Request timing middleware for performance monitoring."""
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import time
import structlog

logger = structlog.get_logger()

class RequestTimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.time()
        response = await call_next(request)
        duration = time.time() - start
        response.headers["X-Response-Time"] = f"{duration:.3f}s"
        if duration > 1.0:
            logger.warning("slow_request", path=request.url.path, method=request.method, duration_ms=round(duration * 1000, 2))
        return response
