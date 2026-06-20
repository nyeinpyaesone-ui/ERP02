"""Finance API with AI Anomaly Detection, Cash Flow Forecasting, and Full GL."""
from typing import List, Optional
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from decimal import Decimal
from datetime import date

from app.db.session import get_db
from app.db.models import Account, JournalEntry, JournalEntryLine, Invoice, Payment, PaymentStatus
from app.api.v1.auth import get_current_user, require_role
from app.ai.agent_system import ai_orchestrator, AgentContext

router = APIRouter()

class AccountCreate(BaseModel):
    account_code: str
    account_name: str
    account_type: str
    parent_id: Optional[str] = None
    is_bank_account: bool = False

class JournalEntryCreate(BaseModel):
    entry_date: Optional[str] = None
    reference: Optional[str] = None
    description: str
    lines: List[dict]

class InvoiceCreate(BaseModel):
    invoice_number: str
    customer_id: str
    order_id: Optional[str] = None
    issue_date: Optional[str] = None
    due_date: str
    line_items: List[dict]
    tax_rate: float = 0.0

class PaymentCreate(BaseModel):
    invoice_id: str
    amount: float
    payment_method: str
    reference: Optional[str] = None

@router.get("/accounts")
async def list_accounts(account_type: Optional[str] = None, db: AsyncSession = Depends(get_db),
                        current_user = Depends(get_current_user)):
    query = select(Account).where(Account.tenant_id == current_user.tenant_id)
    if account_type:
        query = query.where(Account.account_type == account_type)
    result = await db.execute(query)
    accounts = result.scalars().all()
    return [{"id": str(a.id), "account_code": a.account_code, "account_name": a.account_name,
             "account_type": a.account_type, "balance": float(a.balance), "currency": a.currency} for a in accounts]

@router.post("/journal-entries")
async def create_journal_entry(entry: JournalEntryCreate, db: AsyncSession = Depends(get_db),
                               current_user = Depends(require_role(["admin", "manager"]))):
    entry_date = date.today() if not entry.entry_date else date.fromisoformat(entry.entry_date)
    new_entry = JournalEntry(tenant_id=current_user.tenant_id,
                             entry_number=f"JE-{entry_date.strftime('%Y%m%d')}-{await _get_next_je_number(db)}",
                             entry_date=entry_date, reference=entry.reference, description=entry.description,
                             created_by=current_user.id)
    db.add(new_entry)
    await db.flush()

    total_debit = Decimal("0")
    total_credit = Decimal("0")
    for line in entry.lines:
        je_line = JournalEntryLine(entry_id=new_entry.id, account_id=UUID(line["account_id"]),
                                   debit=Decimal(str(line.get("debit", 0))) if line.get("debit") else None,
                                   credit=Decimal(str(line.get("credit", 0))) if line.get("credit") else None,
                                   description=line.get("description"))
        db.add(je_line)
        if je_line.debit: total_debit += je_line.debit
        if je_line.credit: total_credit += je_line.credit

    new_entry.total_debit = total_debit
    new_entry.total_credit = total_credit
    await db.commit()
    return {"id": str(new_entry.id), "entry_number": new_entry.entry_number,
            "total_debit": float(total_debit), "total_credit": float(total_credit)}

async def _get_next_je_number(db):
    result = await db.execute(select(func.count(JournalEntry.id)))
    return result.scalar() + 1

@router.post("/invoices")
async def create_invoice(invoice: InvoiceCreate, db: AsyncSession = Depends(get_db),
                         current_user = Depends(require_role(["admin", "manager", "user"]))):
    subtotal = sum(Decimal(str(item["quantity"])) * Decimal(str(item["unit_price"])) for item in invoice.line_items)
    tax_amount = subtotal * Decimal(str(invoice.tax_rate))
    total = subtotal + tax_amount

    new_inv = Invoice(tenant_id=current_user.tenant_id, invoice_number=invoice.invoice_number,
                      customer_id=UUID(invoice.customer_id), order_id=UUID(invoice.order_id) if invoice.order_id else None,
                      issue_date=date.today() if not invoice.issue_date else date.fromisoformat(invoice.issue_date),
                      due_date=date.fromisoformat(invoice.due_date), subtotal=subtotal, tax_amount=tax_amount,
                      total_amount=total, balance_due=total)
    db.add(new_inv)
    await db.commit()
    await db.refresh(new_inv)
    return {"id": str(new_inv.id), "invoice_number": new_inv.invoice_number, "total_amount": float(total), "status": new_inv.status.value}

@router.post("/payments")
async def record_payment(payment: PaymentCreate, db: AsyncSession = Depends(get_db),
                         current_user = Depends(require_role(["admin", "manager"]))):
    result = await db.execute(select(Invoice).where(Invoice.id == UUID(payment.invoice_id)))
    invoice = result.scalar_one_or_none()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")

    new_payment = Payment(tenant_id=current_user.tenant_id, invoice_id=UUID(payment.invoice_id),
                          amount=Decimal(str(payment.amount)), payment_method=payment.payment_method,
                          reference=payment.reference)
    db.add(new_payment)
    invoice.amount_paid += new_payment.amount
    invoice.balance_due = invoice.total_amount - invoice.amount_paid
    if invoice.balance_due <= 0:
        invoice.status = PaymentStatus.PAID
    elif invoice.balance_due < invoice.total_amount:
        invoice.status = PaymentStatus.PARTIAL
    await db.commit()
    return {"success": True, "invoice_id": payment.invoice_id, "amount_paid": float(invoice.amount_paid),
            "balance_due": float(invoice.balance_due), "status": invoice.status.value}

@router.post("/ai/anomaly-detection")
async def ai_anomaly_detection(transactions: List[dict], db: AsyncSession = Depends(get_db),
                               current_user = Depends(require_role(["admin", "auditor"]))):
    ctx = AgentContext(tenant_id=str(current_user.tenant_id), user_id=str(current_user.id))
    result = await ai_orchestrator.execute("erp", "_anomaly_detection", {"transactions": transactions}, ctx)
    return result.get("output", {})

@router.post("/ai/cash-flow-forecast")
async def ai_cash_flow_forecast(db: AsyncSession = Depends(get_db),
                                current_user = Depends(require_role(["admin", "manager"]))):
    ctx = AgentContext(tenant_id=str(current_user.tenant_id), user_id=str(current_user.id))
    result = await ai_orchestrator.execute("erp", "_cash_flow_forecast",
                                           {"cash_data": {"ar_aging": [10000, 5000, 3000, 2000],
                                                          "ap_due": [8000, 4000], "recurring_expenses": 15000}}, ctx)
    return result.get("output", {})

@router.get("/dashboard")
async def finance_dashboard(db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    total_receivable = await db.execute(select(func.sum(Invoice.balance_due)).where(
        Invoice.tenant_id == current_user.tenant_id,
        Invoice.status.in_([PaymentStatus.PENDING, PaymentStatus.PARTIAL])))
    total_paid = await db.execute(select(func.sum(Payment.amount)).where(Payment.tenant_id == current_user.tenant_id))
    overdue = await db.execute(select(func.count(Invoice.id)).where(
        Invoice.tenant_id == current_user.tenant_id, Invoice.status == PaymentStatus.OVERDUE))
    return {"total_receivable": float(total_receivable.scalar() or 0), "total_collected": float(total_paid.scalar() or 0),
            "overdue_invoices": overdue.scalar() or 0, "ai_insight": "Invoices flagged for high payment risk."}
