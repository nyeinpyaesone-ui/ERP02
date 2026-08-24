"""
Enterprise Manufacturing (MRP) Module
Production Scheduling, Bill of Materials, Work Orders, Quality Control
"""
from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from pydantic import BaseModel, Field, validator
from typing import List, Optional
from datetime import date, datetime
from decimal import Decimal
import uuid

from app.db.session import get_db
from app.db.models import (
    Product, Warehouse, BOM, BOMLine, 
    ManufacturingOrder, StockMovement, Tenant, User
)
from app.middleware.auth import get_current_user
from app.services.event_bus import publish_event

router = APIRouter(prefix="/manufacturing", tags=["Manufacturing"])

# --- Pydantic Schemas ---

class BOMLineSchema(BaseModel):
    component_product_id: uuid.UUID
    quantity_required: Decimal
    scrap_percentage: Decimal = Decimal('0.00')

class BOMCreateSchema(BaseModel):
    product_id: uuid.UUID
    version: int = 1
    lines: List[BOMLineSchema]

class ManufacturingOrderCreateSchema(BaseModel):
    product_id: uuid.UUID
    bom_id: Optional[uuid.UUID] = None
    quantity_to_produce: Decimal
    scheduled_start: date
    scheduled_end: date

class ManufacturingOrderResponse(BaseModel):
    id: uuid.UUID
    order_number: str
    product_id: uuid.UUID
    quantity_to_produce: Decimal
    status: str
    scheduled_start: Optional[date]
    scheduled_end: Optional[date]
    
    class Config:
        from_attributes = True

# --- Endpoints ---

@router.post("/bom", status_code=status.HTTP_201_CREATED)
async def create_bill_of_materials(
    bom_data: BOMCreateSchema,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Create a Bill of Materials (BOM) for a product.
    Defines components required for manufacturing.
    """
    tenant_id = current_user.tenant_id
    
    async with db.begin():
        # Verify parent product exists
        product_stmt = select(Product).where(
            Product.id == bom_data.product_id,
            Product.tenant_id == tenant_id
        )
        result = await db.execute(product_stmt)
        product = result.scalar_one_or_none()
        
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        
        # Create BOM
        new_bom = BOM(
            tenant_id=tenant_id,
            product_id=bom_data.product_id,
            version=bom_data.version,
            is_active=True
        )
        db.add(new_bom)
        await db.flush()
        
        # Add BOM Lines
        for line in bom_data.lines:
            # Verify component exists
            comp_stmt = select(Product).where(
                Product.id == line.component_product_id,
                Product.tenant_id == tenant_id
            )
            comp_result = await db.execute(comp_stmt)
            component = comp_result.scalar_one_or_none()
            
            if not component:
                raise HTTPException(
                    status_code=404, 
                    detail=f"Component product {line.component_product_id} not found"
                )
            
            bom_line = BOMLine(
                bom_id=new_bom.id,
                component_id=line.component_product_id,
                quantity_required=line.quantity_required,
                unit_of_measure='UNIT',
                scrap_percentage=line.scrap_percentage
            )
            db.add(bom_line)
    
    background_tasks.add_task(
        publish_event,
        tenant_id=str(tenant_id),
        event_type="MANUFACTURING.BOM.CREATED",
        payload={"bom_id": str(new_bom.id), "product_id": str(bom_data.product_id)}
    )
    
    return {"bom_id": str(new_bom.id), "version": new_bom.version}

@router.post("/orders", response_model=ManufacturingOrderResponse, status_code=status.HTTP_201_CREATED)
async def create_manufacturing_order(
    mo_data: ManufacturingOrderCreateSchema,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Create a Manufacturing Order (MO).
    Reserves raw materials from inventory based on BOM.
    """
    tenant_id = current_user.tenant_id
    
    async with db.begin():
        # Generate Order Number
        count_stmt = select(func.count(ManufacturingOrder.id)).where(
            ManufacturingOrder.tenant_id == tenant_id
        )
        count_result = await db.execute(count_stmt)
        order_num = f"MO-{datetime.utcnow().strftime('%Y%m%d')}-{count_result.scalar() + 1:05d}"
        
        # If no BOM specified, fetch latest active BOM for product
        bom_id = mo_data.bom_id
        if not bom_id:
            bom_stmt = select(BOM.id).where(
                BOM.product_id == mo_data.product_id,
                BOM.is_active == True
            ).order_by(BOM.version.desc()).limit(1)
            bom_result = await db.execute(bom_stmt)
            bom_id = bom_result.scalar_one_or_none()
            
            if not bom_id:
                raise HTTPException(status_code=400, detail="No active BOM found for this product")
        
        # Create MO
        new_mo = ManufacturingOrder(
            tenant_id=tenant_id,
            order_number=order_num,
            product_id=mo_data.product_id,
            bom_id=bom_id,
            quantity_to_produce=mo_data.quantity_to_produce,
            status='draft',
            scheduled_start=mo_data.scheduled_start,
            scheduled_end=mo_data.scheduled_end,
            created_by=current_user.id
        )
        db.add(new_mo)
        await db.flush()
        
        # Material Reservation Logic (Optional - Advanced MRP)
        # Fetch BOM lines and calculate total component requirements
        bom_lines_stmt = select(BOMLine).where(BOMLine.bom_id == bom_id)
        bom_lines_result = await db.execute(bom_lines_stmt)
        bom_lines = bom_lines_result.scalars().all()
        
        for bom_line in bom_lines:
            required_qty = bom_line.quantity_required * mo_data.quantity_to_produce
            scrap_adj = required_qty * (Decimal('1') + (bom_line.scrap_percentage / Decimal('100')))
            
            # Create reservation stock movement (direction=0 for reservation)
            reservation = StockMovement(
                product_id=bom_line.component_id,
                movement_type='adjustment',  # Using existing enum
                quantity=int(scrap_adj),
                reference=f"MO-RESERVE-{new_mo.id}",
                reason=f"Material reservation for MO {order_num}",
                performed_by=current_user.id
            )
            db.add(reservation)
    
    background_tasks.add_task(
        publish_event,
        tenant_id=str(tenant_id),
        event_type="MANUFACTURING.ORDER.CREATED",
        payload={"mo_id": str(new_mo.id), "order_number": order_num}
    )
    
    return new_mo

@router.post("/orders/{mo_id}/start")
async def start_manufacturing_order(
    mo_id: uuid.UUID,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Start a manufacturing order.
    Changes status to 'in_progress' and records actual start time.
    """
    async with db.begin():
        stmt = select(ManufacturingOrder).where(
            ManufacturingOrder.id == mo_id,
            ManufacturingOrder.tenant_id == current_user.tenant_id
        )
        result = await db.execute(stmt)
        mo = result.scalar_one_or_none()
        
        if not mo:
            raise HTTPException(status_code=404, detail="Manufacturing order not found")
        
        if mo.status != 'draft':
            raise HTTPException(status_code=400, detail="Only draft orders can be started")
        
        mo.status = 'in_progress'
        mo.actual_start = datetime.utcnow()
    
    background_tasks.add_task(
        publish_event,
        tenant_id=str(current_user.tenant_id),
        event_type="MANUFACTURING.ORDER.STARTED",
        payload={"mo_id": str(mo_id)}
    )
    
    return {"message": "Manufacturing order started", "status": mo.status}

@router.post("/orders/{mo_id}/complete")
async def complete_manufacturing_order(
    mo_id: uuid.UUID,
    produced_quantity: Decimal,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Complete a manufacturing order.
    Produces finished goods into inventory.
    """
    tenant_id = current_user.tenant_id
    
    async with db.begin():
        stmt = select(ManufacturingOrder).where(
            ManufacturingOrder.id == mo_id,
            ManufacturingOrder.tenant_id == tenant_id
        )
        result = await db.execute(stmt)
        mo = result.scalar_one_or_none()
        
        if not mo:
            raise HTTPException(status_code=404, detail="Manufacturing order not found")
        
        if mo.status != 'in_progress':
            raise HTTPException(status_code=400, detail="Only in-progress orders can be completed")
        
        mo.status = 'completed'
        mo.actual_end = datetime.utcnow()
        
        # Find default warehouse (simplified - should use routing)
        wh_stmt = select(Warehouse.id).where(Warehouse.tenant_id == tenant_id).limit(1)
        wh_result = await db.execute(wh_stmt)
        warehouse_id = wh_result.scalar_one_or_none()
        
        if not warehouse_id:
            raise HTTPException(status_code=400, detail="No warehouse configured")
        
        # Create inbound stock move for finished product
        finished_move = StockMove(
            tenant_id=tenant_id,
            product_id=mo.product_id,
            warehouse_id=warehouse_id,
            move_type='INBOUND',
            reference_doc_type='MO',
            reference_doc_id=mo.id,
            quantity=produced_quantity,
            direction=1,  # Inbound
            performed_by=current_user.id
        )
        db.add(finished_move)
        
        # Consume reserved materials (create outbound moves)
        # Simplified: In production, would track actual consumption vs BOM
    
    background_tasks.add_task(
        publish_event,
        tenant_id=str(tenant_id),
        event_type="MANUFACTURING.ORDER.COMPLETED",
        payload={"mo_id": str(mo_id), "produced_quantity": str(produced_quantity)}
    )
    
    return {"message": "Manufacturing order completed", "produced_quantity": produced_quantity}

@router.get("/orders")
async def list_manufacturing_orders(
    status_filter: Optional[str] = None,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    List manufacturing orders with optional status filter.
    """
    stmt = select(ManufacturingOrder).where(
        ManufacturingOrder.tenant_id == current_user.tenant_id
    )
    
    if status_filter:
        stmt = stmt.where(ManufacturingOrder.status == status_filter)
    
    stmt = stmt.order_by(ManufacturingOrder.created_at.desc())
    
    result = await db.execute(stmt)
    orders = result.scalars().all()
    
    return [
        {
            "id": str(o.id),
            "order_number": o.order_number,
            "product_id": str(o.product_id),
            "quantity": float(o.quantity_to_produce),
            "status": o.status,
            "scheduled_start": o.scheduled_start.isoformat() if o.scheduled_start else None,
            "scheduled_end": o.scheduled_end.isoformat() if o.scheduled_end else None
        }
        for o in orders
    ]
