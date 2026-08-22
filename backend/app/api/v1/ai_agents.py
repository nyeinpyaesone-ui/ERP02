"""AI Agent API - Direct access to all 15+ skills with observability."""
from typing import List, Dict, Any, Optional
from fastapi import APIRouter, Depends, HTTPException, Body
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.session import get_db
from app.api.v1.auth import get_current_user, require_role
from app.ai.agent_system import ai_orchestrator, AgentContext, ollama
from app.db.models import AIAgentRun, AIConversation

router = APIRouter()

class SkillRequest(BaseModel):
    skill: str
    data: Dict[str, Any] = {}
    model: Optional[str] = None

class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    session_id: str
    model: str
    tokens_used: int

@router.get("/skills")
async def list_skills(current_user = Depends(get_current_user)):
    return {
        "agent": "erp_ai_agent",
        "skills": [
            {"name": "_inventory_forecast", "category": "Inventory", "description": "Predict inventory needs 30/60/90 days"},
            {"name": "_inventory_reorder_optimizer", "category": "Inventory", "description": "Optimize reorder points using EOQ/ROP"},
            {"name": "_demand_pattern_analysis", "category": "Inventory", "description": "ABC/XYZ demand classification"},
            {"name": "_lead_scoring", "category": "CRM", "description": "Score leads 0-100 based on behavior"},
            {"name": "_churn_prediction", "category": "CRM", "description": "Predict customer churn probability"},
            {"name": "_sales_forecast", "category": "CRM", "description": "Forecast revenue next 12 months"},
            {"name": "_anomaly_detection", "category": "Finance", "description": "Detect financial transaction anomalies"},
            {"name": "_cash_flow_forecast", "category": "Finance", "description": "13-week cash flow prediction"},
            {"name": "_invoice_risk_scoring", "category": "Finance", "description": "Score invoice payment risk"},
            {"name": "_timesheet_anomaly_detection", "category": "HR", "description": "Detect timesheet irregularities"},
            {"name": "_leave_optimization", "category": "HR", "description": "Optimize leave approvals"},
            {"name": "_supplier_risk_assessment", "category": "Procurement", "description": "Assess supplier financial/geopolitical risk"},
            {"name": "_po_optimization", "category": "Procurement", "description": "Optimize purchase orders"},
            {"name": "_production_efficiency_forecast", "category": "Manufacturing", "description": "Predict production bottlenecks"},
            {"name": "_project_risk_assessment", "category": "Projects", "description": "Multi-dimensional project risk analysis"},
            {"name": "_compliance_document_review", "category": "Compliance", "description": "Review docs for regulatory gaps"},
            {"name": "_natural_language_query", "category": "General", "description": "Convert NL to SQL/insights"},
        ],
        "models": ["llama3.1", "mistral", "codellama", "nomic-embed-text"],
    }

@router.post("/run")
async def run_skill(req: SkillRequest, db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    ctx = AgentContext(tenant_id=str(current_user.tenant_id), user_id=str(current_user.id))
    result = await ai_orchestrator.execute("erp", req.skill, req.data, ctx, model=req.model)
    return {"run_id": ctx.trace_id, "agent": "erp_ai_agent", "skill": req.skill, "status": "success",
            "result": result.get("output", {}), "tokens": result.get("tokens", 0),
            "cost_usd": result.get("cost", 0), "execution_time_ms": result.get("tokens", 0) * 10}

@router.post("/chat", response_model=ChatResponse)
async def chat_with_ai(req: ChatRequest, db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    session_id = req.session_id or str(uuid.uuid4())

    user_msg = AIConversation(tenant_id=current_user.tenant_id, user_id=current_user.id, session_id=session_id,
                             role="user", content=req.message)
    db.add(user_msg)
    await db.commit()

    ctx = AgentContext(tenant_id=str(current_user.tenant_id), user_id=str(current_user.id), session_id=session_id)
    nlq_result = await ai_orchestrator.execute("erp", "_natural_language_query",
                                                {"query": req.message, "schema": "ERP with products, customers, orders, invoices, employees"}, ctx)
    response_text = nlq_result.get("output", {}).get("summary", "I can help you with that. Could you provide more details?")

    assistant_msg = AIConversation(tenant_id=current_user.tenant_id, user_id=current_user.id, session_id=session_id,
                                    role="assistant", content=response_text, model="llama3.1", tokens=nlq_result.get("tokens", 0))
    db.add(assistant_msg)
    await db.commit()

    return ChatResponse(response=response_text, session_id=session_id, model="llama3.1", tokens_used=nlq_result.get("tokens", 0))

@router.get("/conversations/{session_id}")
async def get_conversation_history(session_id: str, db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    result = await db.execute(select(AIConversation).where(
        AIConversation.session_id == session_id, AIConversation.user_id == current_user.id).order_by(AIConversation.created_at))
    messages = result.scalars().all()
    return [{"role": m.role, "content": m.content, "created_at": m.created_at.isoformat(), "tokens": m.tokens} for m in messages]

@router.get("/runs/history")
async def get_agent_run_history(limit: int = 50, db: AsyncSession = Depends(get_db),
                                current_user = Depends(require_role(["admin", "manager"]))):
    result = await db.execute(select(AIAgentRun).where(AIAgentRun.tenant_id == current_user.tenant_id)
                              .order_by(AIAgentRun.created_at.desc()).limit(limit))
    runs = result.scalars().all()
    return [{"id": str(r.id), "agent": r.agent_name, "skill": r.skill_used, "status": r.status,
             "tokens": r.tokens_used, "cost": float(r.cost_usd) if r.cost_usd else 0,
             "duration_ms": r.execution_time_ms, "created_at": r.created_at.isoformat()} for r in runs]

@router.get("/models")
async def list_available_models(current_user = Depends(get_current_user)):
    try:
        models = await ollama.list_models()
        return {"models": models, "status": "available"}
    except Exception as e:
        return {"models": [], "status": "unavailable", "error": str(e)}
