from typing import List, Optional
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import select, func, or_
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.db.models import Customer, SalesOrder, SalesOrderLine, CustomerInteraction, OrderStatus
from app.api.v1.auth import get_current_user, require_role
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
             "credit_balance": float(c.credit_balance), "risk_score": c.risk_score, "is_active": c.is_active} for c in customers]

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
    # Simple sentiment analysis without AI
    content = (interaction.content or interaction.subject).lower()
    positive_words = ['good', 'great', 'excellent', 'happy', 'satisfied', 'positive', 'thank']
    negative_words = ['bad', 'poor', 'terrible', 'angry', 'unsatisfied', 'negative', 'complaint', 'issue']
    
    positive_count = sum(1 for word in positive_words if word in content)
    negative_count = sum(1 for word in negative_words if word in content)
    
    if positive_count > negative_count:
        sentiment = "positive"
    elif negative_count > positive_count:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    ci = CustomerInteraction(customer_id=UUID(customer_id), interaction_type=interaction.interaction_type,
                             subject=interaction.subject, content=interaction.content,
                             sentiment=sentiment,
                             performed_by=current_user.id)
    db.add(ci)
    await db.commit()
    return {"success": True, "interaction_id": str(ci.id), "sentiment": ci.sentiment}

@router.post("/lead-scoring")
async def lead_scoring(req: LeadScoreRequest, db: AsyncSession = Depends(get_db),
                       current_user = Depends(require_role(["admin", "manager"]))):
    # Simple rule-based lead scoring without AI
    scored_leads = []
    for lead in req.leads:
        score = 0
        # Company size scoring
        if lead.get('company_size', 0) > 100:
            score += 30
        elif lead.get('company_size', 0) > 50:
            score += 20
        elif lead.get('company_size', 0) > 10:
            score += 10
        
        # Engagement scoring
        if lead.get('email_opened', False):
            score += 15
        if lead.get('demo_requested', False):
            score += 25
        if lead.get('website_visits', 0) > 5:
            score += 20
        
        # Budget scoring
        budget = lead.get('estimated_budget', 0)
        if budget > 50000:
            score += 30
        elif budget > 10000:
            score += 15
        
        lead_score = min(100, score)
        priority = "high" if lead_score >= 70 else "medium" if lead_score >= 40 else "low"
        
        scored_leads.append({
            "lead_id": lead.get('id'),
            "score": lead_score,
            "priority": priority
        })
    
    return scored_leads

@router.post("/churn-prediction")
async def churn_prediction(db: AsyncSession = Depends(get_db), current_user = Depends(require_role(["admin", "manager"]))):
    # Simple rule-based churn prediction without AI
    result = await db.execute(select(Customer).where(Customer.tenant_id == current_user.tenant_id, Customer.is_active == True))
    customers = result.scalars().all()
    
    churn_predictions = []
    for c in customers[:50]:  # Limit to 50 for performance
        risk_score = 0
        
        # Days since last purchase (simulated)
        days_since_purchase = 45
        if days_since_purchase > 90:
            risk_score += 40
        elif days_since_purchase > 60:
            risk_score += 25
        elif days_since_purchase > 30:
            risk_score += 10
        
        # Support tickets (simulated)
        support_tickets = 3
        if support_tickets > 5:
            risk_score += 30
        elif support_tickets > 2:
            risk_score += 15
        
        # Payment delays (simulated)
        payment_delays = 1
        if payment_delays > 3:
            risk_score += 30
        elif payment_delays > 0:
            risk_score += 15
        
        churn_risk = min(100, risk_score)
        risk_level = "high" if churn_risk >= 60 else "medium" if churn_risk >= 30 else "low"
        
        churn_predictions.append({
            "customer_id": str(c.id),
            "customer_name": f"{c.first_name} {c.last_name}",
            "churn_risk_score": churn_risk,
            "risk_level": risk_level,
            "recommended_action": "Contact immediately" if risk_level == "high" else "Schedule check-in" if risk_level == "medium" else "Monitor"
        })
    
    return churn_predictions

@router.get("/dashboard")
async def crm_dashboard(db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    total_customers = await db.execute(select(func.count(Customer.id)).where(Customer.tenant_id == current_user.tenant_id))
    total_orders = await db.execute(select(func.count(SalesOrder.id)).where(SalesOrder.tenant_id == current_user.tenant_id))
    revenue = await db.execute(select(func.sum(SalesOrder.total_amount)).where(
        SalesOrder.tenant_id == current_user.tenant_id, SalesOrder.status == OrderStatus.DELIVERED))
    return {"total_customers": total_customers.scalar() or 0, "total_orders": total_orders.scalar() or 0,
            "total_revenue": float(revenue.scalar() or 0), "insight": "Customer retention analysis based on order history."}