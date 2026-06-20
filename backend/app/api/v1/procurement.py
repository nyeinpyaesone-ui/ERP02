"""Procurement API Module"""
from fastapi import APIRouter, Depends
from app.api.v1.auth import get_current_user

router = APIRouter()

@router.get("/")
async def procurement_root(current_user = Depends(get_current_user)):
    return {"module": "procurement", "status": "active"}

@router.get("/dashboard")
async def procurement_dashboard(current_user = Depends(get_current_user)):
    return {"module": "procurement", "ai_insight": "AI-powered insights available for procurement module."}
