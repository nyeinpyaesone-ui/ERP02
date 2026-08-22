from fastapi import APIRouter, Depends
from app.api.v1.auth import get_current_user

router = APIRouter()

@router.get("/")
async def analytics_root(current_user = Depends(get_current_user)):
    return {"module": "analytics", "status": "active"}

@router.get("/dashboard")
async def analytics_dashboard(current_user = Depends(get_current_user)):
    return {"module": "analytics", "insight": "Statistical insights available for analytics module."}