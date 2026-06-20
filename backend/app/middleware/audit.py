""""Audit logging middleware for all data mutations."""
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import AuditLog
import json
import structlog

logger = structlog.get_logger()

async def log_audit_event(db, tenant_id, user_id, action, entity_type, entity_id, old_vals, new_vals, ip=None, ua=None):
    log = AuditLog(tenant_id=tenant_id, user_id=user_id, action=action, entity_type=entity_type,
                   entity_id=entity_id, old_values=old_vals, new_values=new_vals,
                   ip_address=ip, user_agent=ua)
    db.add(log)
    await db.commit()

class AuditMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        return response
