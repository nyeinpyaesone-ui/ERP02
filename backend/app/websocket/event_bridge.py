"""
Event Bridge - Connects RabbitMQ events to WebSocket notifications
Translates business events into real-time messages for dashboards
"""
import asyncio
import json
import logging
from typing import Dict, Any
from aio_pika import Message, IncomingMessage
from ..services.event_bus import EventBus
from ..websocket.manager import manager

logger = logging.getLogger(__name__)


class EventBridge:
    """Bridges asynchronous events from RabbitMQ to WebSocket clients"""
    
    def __init__(self):
        self.event_handlers: Dict[str, callable] = {}
        self.setup_handlers()
    
    def setup_handlers(self):
        """Register event handlers for different event types"""
        
        # Task completion/failure events
        self.event_handlers["task.completed"] = self.handle_task_completed
        self.event_handlers["task.failed"] = self.handle_task_failed
        
        # Inventory events
        self.event_handlers["inventory.low_stock"] = self.handle_low_stock
        self.event_handlers["inventory.restocked"] = self.handle_restocked
        self.event_handlers["inventory.order_shipped"] = self.handle_order_shipped
        
        # Order events
        self.event_handlers["order.created"] = self.handle_order_created
        self.event_handlers["order.updated"] = self.handle_order_updated
        self.event_handlers["order.cancelled"] = self.handle_order_cancelled
        
        # Finance events
        self.event_handlers["invoice.overdue"] = self.handle_invoice_overdue
        self.event_handlers["payment.received"] = self.handle_payment_received
        self.event_handlers["budget.exceeded"] = self.handle_budget_exceeded
        
        # HR events
        self.event_handlers["timesheet.submitted"] = self.handle_timesheet_submitted
        self.event_handlers["leave.approved"] = self.handle_leave_approved
        self.event_handlers["payroll.processed"] = self.handle_payroll_processed
        
        # System events
        self.event_handlers["system.alert"] = self.handle_system_alert
        self.event_handlers["system.maintenance"] = self.handle_maintenance
    
    async def handle_event(self, event_type: str, data: Dict[str, Any]):
        """Route event to appropriate handler"""
        handler = self.event_handlers.get(event_type)
        if handler:
            try:
                await handler(data)
            except Exception as e:
                logger.error(f"Error handling event {event_type}: {e}")
        else:
            logger.warning(f"No handler for event type: {event_type}")
    
    # Task handlers
    async def handle_task_completed(self, data: Dict[str, Any]):
        """Handle task completion notification"""
        tenant_id = data.get("tenant_id")
        message = {
            "type": "notification",
            "category": "task",
            "priority": "normal",
            "event": "task.completed",
            "data": {
                "task_id": data.get("task_id"),
                "task_type": data.get("task_type"),
                "status": "completed",
                "message": f"Task {data.get('task_type')} completed successfully",
                "result_url": data.get("result_url")
            }
        }
        await manager.broadcast_to_tenant(message, tenant_id)
    
    async def handle_task_failed(self, data: Dict[str, Any]):
        """Handle task failure notification"""
        tenant_id = data.get("tenant_id")
        message = {
            "type": "notification",
            "category": "task",
            "priority": "high",
            "event": "task.failed",
            "data": {
                "task_id": data.get("task_id"),
                "task_type": data.get("task_type"),
                "status": "failed",
                "error": data.get("error"),
                "message": f"Task {data.get('task_type')} failed"
            }
        }
        await manager.broadcast_to_tenant(message, tenant_id)
    
    # Inventory handlers
    async def handle_low_stock(self, data: Dict[str, Any]):
        """Handle low stock alert"""
        tenant_id = data.get("tenant_id")
        message = {
            "type": "alert",
            "category": "inventory",
            "priority": "high",
            "event": "inventory.low_stock",
            "data": {
                "item_id": data.get("item_id"),
                "item_name": data.get("item_name"),
                "current_stock": data.get("current_stock"),
                "threshold": data.get("threshold"),
                "message": f"Low stock alert: {data.get('item_name')} ({data.get('current_stock')} units)"
            }
        }
        await manager.broadcast_to_tenant(message, tenant_id)
    
    async def handle_restocked(self, data: Dict[str, Any]):
        """Handle restock notification"""
        tenant_id = data.get("tenant_id")
        message = {
            "type": "notification",
            "category": "inventory",
            "priority": "normal",
            "event": "inventory.restocked",
            "data": {
                "item_id": data.get("item_id"),
                "item_name": data.get("item_name"),
                "quantity": data.get("quantity"),
                "message": f"Restocked: {data.get('item_name')} ({data.get('quantity')} units)"
            }
        }
        await manager.broadcast_to_tenant(message, tenant_id)
    
    async def handle_order_shipped(self, data: Dict[str, Any]):
        """Handle order shipment notification"""
        tenant_id = data.get("tenant_id")
        message = {
            "type": "notification",
            "category": "orders",
            "priority": "normal",
            "event": "inventory.order_shipped",
            "data": {
                "order_id": data.get("order_id"),
                "tracking_number": data.get("tracking_number"),
                "message": f"Order {data.get('order_id')} has been shipped"
            }
        }
        # Send to specific customer if available
        if data.get("customer_id"):
            await manager.broadcast_to_user(message, data.get("customer_id"))
        else:
            await manager.broadcast_to_tenant(message, tenant_id)
    
    # Order handlers
    async def handle_order_created(self, data: Dict[str, Any]):
        """Handle new order notification"""
        tenant_id = data.get("tenant_id")
        message = {
            "type": "notification",
            "category": "orders",
            "priority": "normal",
            "event": "order.created",
            "data": {
                "order_id": data.get("order_id"),
                "customer_id": data.get("customer_id"),
                "total_amount": data.get("total_amount"),
                "message": f"New order created: {data.get('order_id')}"
            }
        }
        await manager.broadcast_to_tenant(message, tenant_id)
    
    async def handle_order_updated(self, data: Dict[str, Any]):
        """Handle order update notification"""
        tenant_id = data.get("tenant_id")
        message = {
            "type": "notification",
            "category": "orders",
            "priority": "normal",
            "event": "order.updated",
            "data": {
                "order_id": data.get("order_id"),
                "status": data.get("status"),
                "message": f"Order {data.get('order_id')} status updated to {data.get('status')}"
            }
        }
        await manager.broadcast_to_tenant(message, tenant_id)
    
    async def handle_order_cancelled(self, data: Dict[str, Any]):
        """Handle order cancellation"""
        tenant_id = data.get("tenant_id")
        message = {
            "type": "notification",
            "category": "orders",
            "priority": "high",
            "event": "order.cancelled",
            "data": {
                "order_id": data.get("order_id"),
                "reason": data.get("reason"),
                "message": f"Order {data.get('order_id')} cancelled"
            }
        }
        await manager.broadcast_to_tenant(message, tenant_id)
    
    # Finance handlers
    async def handle_invoice_overdue(self, data: Dict[str, Any]):
        """Handle overdue invoice alert"""
        tenant_id = data.get("tenant_id")
        message = {
            "type": "alert",
            "category": "finance",
            "priority": "high",
            "event": "invoice.overdue",
            "data": {
                "invoice_id": data.get("invoice_id"),
                "amount": data.get("amount"),
                "days_overdue": data.get("days_overdue"),
                "customer_id": data.get("customer_id"),
                "message": f"Invoice {data.get('invoice_id')} is {data.get('days_overdue')} days overdue"
            }
        }
        await manager.broadcast_to_tenant(message, tenant_id)
    
    async def handle_payment_received(self, data: Dict[str, Any]):
        """Handle payment received notification"""
        tenant_id = data.get("tenant_id")
        message = {
            "type": "notification",
            "category": "finance",
            "priority": "normal",
            "event": "payment.received",
            "data": {
                "payment_id": data.get("payment_id"),
                "invoice_id": data.get("invoice_id"),
                "amount": data.get("amount"),
                "message": f"Payment received: ${data.get('amount')}"
            }
        }
        await manager.broadcast_to_tenant(message, tenant_id)
    
    async def handle_budget_exceeded(self, data: Dict[str, Any]):
        """Handle budget exceeded alert"""
        tenant_id = data.get("tenant_id")
        message = {
            "type": "alert",
            "category": "finance",
            "priority": "critical",
            "event": "budget.exceeded",
            "data": {
                "department": data.get("department"),
                "budget_limit": data.get("budget_limit"),
                "actual_spend": data.get("actual_spend"),
                "message": f"Budget exceeded for {data.get('department')}"
            }
        }
        await manager.broadcast_to_tenant(message, tenant_id)
    
    # HR handlers
    async def handle_timesheet_submitted(self, data: Dict[str, Any]):
        """Handle timesheet submission"""
        tenant_id = data.get("tenant_id")
        message = {
            "type": "notification",
            "category": "hr",
            "priority": "normal",
            "event": "timesheet.submitted",
            "data": {
                "timesheet_id": data.get("timesheet_id"),
                "employee_id": data.get("employee_id"),
                "period": data.get("period"),
                "message": f"Timesheet submitted for period {data.get('period')}"
            }
        }
        await manager.broadcast_to_tenant(message, tenant_id)
    
    async def handle_leave_approved(self, data: Dict[str, Any]):
        """Handle leave approval notification"""
        tenant_id = data.get("tenant_id")
        message = {
            "type": "notification",
            "category": "hr",
            "priority": "normal",
            "event": "leave.approved",
            "data": {
                "leave_id": data.get("leave_id"),
                "employee_id": data.get("employee_id"),
                "start_date": data.get("start_date"),
                "end_date": data.get("end_date"),
                "message": f"Leave request approved"
            }
        }
        await manager.broadcast_to_user(message, data.get("employee_id"))
    
    async def handle_payroll_processed(self, data: Dict[str, Any]):
        """Handle payroll processing completion"""
        tenant_id = data.get("tenant_id")
        message = {
            "type": "notification",
            "category": "hr",
            "priority": "normal",
            "event": "payroll.processed",
            "data": {
                "payroll_id": data.get("payroll_id"),
                "period": data.get("period"),
                "employee_count": data.get("employee_count"),
                "message": f"Payroll processed for {data.get('period')}"
            }
        }
        await manager.broadcast_to_tenant(message, tenant_id)
    
    # System handlers
    async def handle_system_alert(self, data: Dict[str, Any]):
        """Handle system-wide alert"""
        tenant_id = data.get("tenant_id")
        message = {
            "type": "alert",
            "category": "system",
            "priority": data.get("priority", "high"),
            "event": "system.alert",
            "data": {
                "alert_id": data.get("alert_id"),
                "severity": data.get("severity"),
                "message": data.get("message"),
                "affected_services": data.get("affected_services", [])
            }
        }
        await manager.broadcast_to_tenant(message, tenant_id)
    
    async def handle_maintenance(self, data: Dict[str, Any]):
        """Handle scheduled maintenance notification"""
        tenant_id = data.get("tenant_id")
        message = {
            "type": "notification",
            "category": "system",
            "priority": "normal",
            "event": "system.maintenance",
            "data": {
                "maintenance_id": data.get("maintenance_id"),
                "scheduled_time": data.get("scheduled_time"),
                "duration": data.get("duration"),
                "affected_services": data.get("affected_services", []),
                "message": f"Scheduled maintenance: {data.get('message')}"
            }
        }
        await manager.broadcast_to_tenant(message, tenant_id)


# Global instance
event_bridge = EventBridge()
