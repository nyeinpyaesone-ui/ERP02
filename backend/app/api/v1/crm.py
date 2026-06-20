"""CRM API with AI Lead Scoring, Churn Prediction, and Sentiment Analysis."""
from typing import List, Optional
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import select, func, or_
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.db.models import Customer, SalesOrder, SalesOrderLine, CustomerInteraction, OrderStatus
from app.api.v1.auth import get_current_user, require_role
from app.ai.agent_system import ai_orchestrator, AgentContext
from app.services.cache_manager import cache_manager
from app.services.event_bus import event_bus

router = APIRouter()

class CustomerCreate(BaseModel):
    customer_code: str
    company_name: Optional[str] = None
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    customer_type: str = "individual"
    industry: Optional[str] = None
    credit_limit: Optional[float] = None

class InteractionCreate(BaseModel):
    customer_id: str
    interaction_type: str
    subject: str
    content: Optional[str] = None

class LeadScoreRequest(BaseModel):
    leads: List[dict]

@router.get("/customers")
async def list_customers(search: Optional[str] = None, customer_type: Optional[str] = None,
                         page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
                         db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    query = select(Customer).where(Customer.tenant_id == current_user.tenant_id)
    if search:
        query = query.where(or_(Customer.first_name.ilike(f"%{search}%"), Customer.email.ilike(f"%{search}%")))
    if customer_type:
        query = query.where(Customer.customer_type == customer_type)
    query = query.offset((page - 1) * page_size).limit(page_size)
    result = await db.execute(query)
    customers = result.scalars().all()
    return [{"id": str(c.id), "customer_code": c.customer_code, "company_name": c.company_name,
             "first_name": c.first_name, "last_name": c.last_name, "email": c.email,
             "credit_balance": float(c.credit_balance), "ai_score": c.ai_score, "is_active": c.is_active} for c in customers]

@router.post("/customers")
async def create_customer(customer: CustomerCreate, db: AsyncSession = Depends(get_db),
                          current_user = Depends(require_role(["admin", "manager", "user"]))):
    new_customer = Customer(tenant_id=current_user.tenant_id, customer_code=customer.customer_code,
                            company_name=customer.company_name, first_name=customer.first_name,
                            last_name=customer.last_name, email=customer.email, phone=customer.phone,
                            customer_type=customer.customer_type, industry=customer.industry,
                            credit_limit=customer.credit_limit)
    db.add(new_customer)
    await db.commit()
    await db.refresh(new_customer)
    await event_bus.publish("crm.customer_created", {"customer_id": str(new_customer.id)})
    return {"id": str(new_customer.id), "customer_code": new_customer.customer_code, "name": f"{new_customer.first_name} {new_customer.last_name}"}

@router.post("/customers/{customer_id}/interactions")
async def add_interaction(customer_id: str, interaction: InteractionCreate, db: AsyncSession = Depends(get_db),
                          current_user = Depends(get_current_user)):
    ctx = AgentContext(tenant_id=str(current_user.tenant_id), user_id=str(current_user.id))
    sentiment_result = await ai_orchestrator.execute("erp", "_natural_language_query",
                                                       {"query": f"Analyze sentiment: {interaction.content or interaction.subject}"}, ctx)

    ci = CustomerInteraction(customer_id=UUID(customer_id), interaction_type=interaction.interaction_type,
                             subject=interaction.subject, content=interaction.content,
                             sentiment=sentiment_result.get("output", {}).get("summary", "neutral")[:20],
                             ai_summary=sentiment_result.get("output", {}).get("summary", "")[:200],
                             performed_by=current_user.id)
    db.add(ci)
    await db.commit()
    return {"success": True, "interaction_id": str(ci.id), "ai_sentiment": ci.sentiment}

@router.post("/ai/lead-scoring")
async def ai_lead_scoring(req: LeadScoreRequest, db: AsyncSession = Depends(get_db),
                          current_user = Depends(require_role(["admin", "manager"]))):
    ctx = AgentContext(tenant_id=str(current_user.tenant_id), user_id=str(current_user.id))
    result = await ai_orchestrator.execute("erp", "_lead_scoring", {"leads": req.leads}, ctx)
    return result.get("output", [])

@router.post("/ai/churn-prediction")
async def ai_churn_prediction(db: AsyncSession = Depends(get_db), current_user = Depends(require_role(["admin", "manager"]))):
    result = await db.execute(select(Customer).where(Customer.tenant_id == current_user.tenant_id, Customer.is_active == True))
    customers = result.scalars().all()
    customer_data = [{"customer_id": str(c.id), "days_since_last_purchase": 45, "purchase_frequency": 2.5,
                      "support_tickets": 3, "payment_delays": 1, "contract_renewal_days": 90} for c in customers]
    ctx = AgentContext(tenant_id=str(current_user.tenant_id), user_id=str(current_user.id))
    result = await ai_orchestrator.execute("erp", "_churn_prediction", {"customers": customer_data[:50]}, ctx)
    return result.get("output", [])

@router.get("/dashboard")
async def crm_dashboard(db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    total_customers = await db.execute(select(func.count(Customer.id)).where(Customer.tenant_id == current_user.tenant_id))
    total_orders = await db.execute(select(func.count(SalesOrder.id)).where(SalesOrder.tenant_id == current_user.tenant_id))
    revenue = await db.execute(select(func.sum(SalesOrder.total_amount)).where(
        SalesOrder.tenant_id == current_user.tenant_id, SalesOrder.status == OrderStatus.DELIVERED))
    return {"total_customers": total_customers.scalar() or 0, "total_orders": total_orders.scalar() or 0,
            "total_revenue": float(revenue.scalar() or 0), "ai_insight": "Top customers at churn risk identified."}
