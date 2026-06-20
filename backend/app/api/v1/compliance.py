"""Compliance API Module"""
from fastapi import APIRouter, Depends
from app.api.v1.auth import get_current_user

router = APIRouter()

@router.get("/")
async def compliance_root(current_user = Depends(get_current_user)):
    return {"module": "compliance", "status": "active"}

@router.get("/dashboard")
async def compliance_dashboard(current_user = Depends(get_current_user)):
    return {"module": "compliance", "ai_insight": "AI-powered insights available for compliance module."}
