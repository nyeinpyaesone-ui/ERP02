"""Manufacturing API Module"""
from fastapi import APIRouter, Depends
from app.api.v1.auth import get_current_user

router = APIRouter()

@router.get("/")
async def manufacturing_root(current_user = Depends(get_current_user)):
    return {"module": "manufacturing", "status": "active"}

@router.get("/dashboard")
async def manufacturing_dashboard(current_user = Depends(get_current_user)):
    return {"module": "manufacturing", "ai_insight": "AI-powered insights available for manufacturing module."}
