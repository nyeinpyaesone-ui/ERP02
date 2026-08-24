"""
Real-Time Event Integration Service

This service bridges the asynchronous event bus with real-time WebSocket notifications,
ensuring that background task completions and system events are immediately pushed
to connected clients.

Features:
- Listens to RabbitMQ events
- Routes events to appropriate WebSocket channels
- Supports tenant-specific broadcasting
- Handles critical alerts with priority routing
"""

import asyncio
import logging
from typing import Dict, Any
from datetime import datetime

from .event_bus import event_bus
from .websocket_manager import manager as ws_manager, ConnectionType, MessageType

logger = logging.getLogger(__name__)

class RealTimeEventBridge:
    """Bridges async events from RabbitMQ to WebSocket real-time notifications"""
    
    def __init__(self):
        self.event_handlers: Dict[str, callable] = {
            "task.completed": self.handle_task_completed,
            "task.failed": self.handle_task_failed,
            "inventory.low_stock": self.handle_inventory_alert,
            "order.status_changed": self.handle_order_update,
            "finance.payment_received": self.handle_finance_event,
            "finance.invoice_overdue": self.handle_finance_event,
            "hr.payroll_processed": self.handle_hr_event,
            "system.alert": self.handle_system_alert,
        }
        self.running = False
        
    async def start(self):
        """Start listening to events and bridging to WebSocket"""
        self.running = True
        logger.info("RealTimeEventBridge started")
        
        # Subscribe to relevant events
        for event_type in self.event_handlers.keys():
            await event_bus.subscribe(event_type, self.process_event)
            
    async def stop(self):
        """Stop the bridge"""
        self.running = False
        logger.info("RealTimeEventBridge stopped")
        
    async def process_event(self, event_data: dict):
        """Process incoming event and route to WebSocket"""
        if not self.running:
            return
            
        event_type = event_data.get("type")
        tenant_id = event_data.get("tenant_id")
        
        logger.debug(f"Processing event: {event_type} for tenant: {tenant_id}")
        
        # Route to appropriate handler
        if event_type in self.event_handlers:
            await self.event_handlers[event_type](event_data)
        else:
            # Generic event handling
            await self.handle_generic_event(event_data)
            
    async def handle_task_completed(self, event_data: dict):
        """Handle task completion events"""
        tenant_id = event_data.get("tenant_id")
        task_info = event_data.get("data", {})
        user_id = task_info.get("user_id")
        
        message = {
            "type": MessageType.TASK_UPDATE.value,
            "status": "completed",
            "task_id": task_info.get("task_id"),
            "task_type": task_info.get("task_type"),
            "result": task_info.get("result"),
            "completed_at": datetime.utcnow().isoformat()
        }
        
        if user_id:
            # Send to specific user
            await ws_manager.send_personal_message(
                message=message,
                user_id=user_id,
                conn_type=ConnectionType.CLIENT
            )
        elif tenant_id:
            # Broadcast to tenant
            await ws_manager.broadcast_to_tenant(
                message=message,
                tenant_id=tenant_id,
                priority="normal"
            )
            
        logger.info(f"Task completed notification sent: {task_info.get('task_id')}")
        
    async def handle_task_failed(self, event_data: dict):
        """Handle task failure events"""
        tenant_id = event_data.get("tenant_id")
        task_info = event_data.get("data", {})
        
        message = {
            "type": MessageType.TASK_UPDATE.value,
            "status": "failed",
            "task_id": task_info.get("task_id"),
            "task_type": task_info.get("task_type"),
            "error": task_info.get("error"),
            "failed_at": datetime.utcnow().isoformat()
        }
        
        if tenant_id:
            await ws_manager.broadcast_to_tenant(
                message=message,
                tenant_id=tenant_id,
                priority="critical"
            )
            
        logger.warning(f"Task failed notification sent: {task_info.get('task_id')}")
        
    async def handle_inventory_alert(self, event_data: dict):
        """Handle low stock inventory alerts"""
        tenant_id = event_data.get("tenant_id")
        alert_data = event_data.get("data", {})
        
        message = {
            "type": MessageType.INVENTORY_ALERT.value,
            "priority": "high",
            "item_id": alert_data.get("item_id"),
            "item_name": alert_data.get("item_name"),
            "current_stock": alert_data.get("current_stock"),
            "threshold": alert_data.get("threshold"),
            "warehouse": alert_data.get("warehouse"),
            "alert_time": datetime.utcnow().isoformat()
        }
        
        if tenant_id:
            await ws_manager.broadcast_to_tenant(
                message=message,
                tenant_id=tenant_id,
                conn_type=ConnectionType.ADMIN,
                priority="high"
            )
            
        logger.info(f"Inventory alert broadcast: {alert_data.get('item_name')}")
        
    async def handle_order_update(self, event_data: dict):
        """Handle order status changes"""
        tenant_id = event_data.get("tenant_id")
        order_data = event_data.get("data", {})
        
        message = {
            "type": MessageType.ORDER_STATUS.value,
            "order_id": order_data.get("order_id"),
            "old_status": order_data.get("old_status"),
            "new_status": order_data.get("new_status"),
            "updated_at": datetime.utcnow().isoformat(),
            "details": order_data.get("details")
        }
        
        # Send to specific customer if available
        customer_id = order_data.get("customer_id")
        if customer_id:
            await ws_manager.send_personal_message(
                message=message,
                user_id=customer_id,
                conn_type=ConnectionType.CLIENT
            )
            
        # Also notify admin team
        if tenant_id:
            await ws_manager.broadcast_to_tenant(
                message=message,
                tenant_id=tenant_id,
                conn_type=ConnectionType.ADMIN,
                priority="normal"
            )
            
        logger.info(f"Order status update: {order_data.get('order_id')}")
        
    async def handle_finance_event(self, event_data: dict):
        """Handle finance-related events (payments, invoices)"""
        tenant_id = event_data.get("tenant_id")
        finance_data = event_data.get("data", {})
        event_type = event_data.get("type")
        
        message = {
            "type": MessageType.FINANCE_NOTIFICATION.value,
            "event_subtype": event_type,
            "invoice_id": finance_data.get("invoice_id"),
            "amount": finance_data.get("amount"),
            "currency": finance_data.get("currency"),
            "status": finance_data.get("status"),
            "timestamp": datetime.utcnow().isoformat()
        }
        
        if tenant_id:
            await ws_manager.broadcast_to_tenant(
                message=message,
                tenant_id=tenant_id,
                conn_type=ConnectionType.ADMIN,
                priority="normal"
            )
            
        logger.info(f"Finance event notification: {event_type}")
        
    async def handle_hr_event(self, event_data: dict):
        """Handle HR events (payroll, timesheets)"""
        tenant_id = event_data.get("tenant_id")
        hr_data = event_data.get("data", {})
        
        message = {
            "type": "hr_notification",
            "event_type": event_data.get("type"),
            "employee_id": hr_data.get("employee_id"),
            "details": hr_data,
            "processed_at": datetime.utcnow().isoformat()
        }
        
        if tenant_id:
            await ws_manager.broadcast_to_tenant(
                message=message,
                tenant_id=tenant_id,
                conn_type=ConnectionType.ADMIN,
                priority="normal"
            )
            
    async def handle_system_alert(self, event_data: dict):
        """Handle critical system-wide alerts"""
        alert_data = event_data.get("data", {})
        
        message = {
            "type": MessageType.SYSTEM_ALERT.value,
            "severity": alert_data.get("severity", "warning"),
            "title": alert_data.get("title"),
            "message": alert_data.get("message"),
            "affected_services": alert_data.get("affected_services"),
            "timestamp": datetime.utcnow().isoformat(),
            "action_required": alert_data.get("action_required", False)
        }
        
        # Broadcast system-wide
        await ws_manager.broadcast_system_wide(
            message=message,
            exclude_tenants=alert_data.get("exclude_tenants")
        )
        
        logger.critical(f"System alert broadcast: {alert_data.get('title')}")
        
    async def handle_generic_event(self, event_data: dict):
        """Handle generic/unrecognized events"""
        tenant_id = event_data.get("tenant_id")
        
        message = {
            "type": "generic_event",
            "event_type": event_data.get("type"),
            "data": event_data.get("data"),
            "timestamp": datetime.utcnow().isoformat()
        }
        
        if tenant_id:
            await ws_manager.broadcast_to_tenant(
                message=message,
                tenant_id=tenant_id,
                priority="low"
            )

# Singleton instance
realtime_bridge = RealTimeEventBridge()
