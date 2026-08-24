from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import structlog
import traceback

logger = structlog.get_logger()

class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except Exception as e:
            trace_id = getattr(request.state, 'trace_id', 'unknown')
            logger.error("unhandled_exception", path=request.url.path, method=request.method,
                         error=str(e), trace=traceback.format_exc()[:500], trace_id=trace_id)
            return JSONResponse(status_code=500, content={
                "detail": "Internal server error",
                "trace_id": trace_id,
                "type": "internal_error"
            })