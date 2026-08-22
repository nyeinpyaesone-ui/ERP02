from fastapi import APIRouter, Depends
from app.api.v1.auth import get_current_user

router = APIRouter()

@router.get("/")
async def projects_root(current_user = Depends(get_current_user)):
    return {"module": "projects", "status": "active"}

@router.get("/dashboard")
async def projects_dashboard(current_user = Depends(get_current_user)):
    return {"module": "projects", "insight": "Project timeline and resource metrics available for projects module."}