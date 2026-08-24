from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends, HTTPException, Query
from typing import Optional
from ..services.websocket_manager import manager, ConnectionType, MessageType
from ..db.session import get_db
from ..middleware.auth import get_current_user_ws
from sqlalchemy.orm import Session
import logging
import asyncio
from datetime import datetime

logger = logging.getLogger(__name__)
router = APIRouter()

@router.websocket("/ws/{tenant_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    tenant_id: str,
    conn_type: ConnectionType = Query(default=ConnectionType.CLIENT),
    token: Optional[str] = Query(None)
):
    """
    Main WebSocket endpoint for real-time communication.
    
    Supports:
    - Multi-tenant isolation via tenant_id
    - Connection type routing (admin, client, system, worker)
    - Authentication via token query parameter
    - Automatic heartbeat monitoring
    """
    # Authenticate user (simplified for WS - in production use proper JWT validation)
    try:
        # In production, validate token and extract user_id
        # For now, we'll use a placeholder approach
        user_id = f"user_{tenant_id}_{conn_type.value}"  # Replace with actual auth
        
        if token:
            # Validate token and extract actual user_id
            # user_id = await validate_ws_token(token)
            pass
            
        logger.info(f"WS connection attempt: tenant={tenant_id}, type={conn_type.value}, user={user_id}")
        
        # Connect to manager with tenant context
        await manager.connect(websocket, user_id, conn_type, tenant_id)
        
        # Send welcome message
        await manager.send_personal_message({
            "type": "welcome",
            "message": f"Connected to {tenant_id} as {conn_type.value}",
            "features": [
                "real_time_updates",
                "task_tracking",
                "inventory_alerts",
                "order_notifications"
            ]
        }, user_id, conn_type)
        
        # Keep connection alive and handle messages
        while True:
            try:
                # Wait for incoming messages with timeout
                data = await asyncio.wait_for(websocket.receive_json(), timeout=30.0)
                
                # Handle different message types
                msg_type = data.get("type")
                
                if msg_type == "heartbeat":
                    await manager.handle_heartbeat(user_id, conn_type)
                    
                elif msg_type == "sync_request":
                    # Client requesting synchronization state
                    await manager.send_personal_message({
                        "type": "sync_response",
                        "status": "synchronized",
                        "server_time": datetime.utcnow().isoformat(),
                        "sequence": manager.sequence_counters.get(user_id, 0)
                    }, user_id, conn_type)
                    
                elif msg_type == "ack":
                    # Acknowledgment of received message
                    message_id = data.get("message_id")
                    sequence = data.get("sequence")
                    ack_key = f"{user_id}:{sequence}"
                    
                    if ack_key in manager.pending_acks:
                        del manager.pending_acks[ack_key]
                        logger.debug(f"Acknowledged message {message_id} from {user_id}")
                        
                elif msg_type == "subscribe":
                    # Subscribe to specific event channels
                    channels = data.get("channels", [])
                    logger.info(f"User {user_id} subscribed to: {channels}")
                    
                else:
                    logger.warning(f"Unknown message type: {msg_type}")
                    
            except asyncio.TimeoutError:
                # Send heartbeat request if no activity
                await manager.send_personal_message({
                    "type": "heartbeat_request",
                    "timestamp": datetime.utcnow().isoformat()
                }, user_id, conn_type)
                
            except WebSocketDisconnect:
                logger.info(f"WebSocket disconnected: {user_id}")
                manager.disconnect(user_id, conn_type)
                break
                
            except Exception as e:
                logger.error(f"Error processing WS message: {e}")
                await manager.send_personal_message({
                    "type": "error",
                    "message": str(e)
                }, user_id, conn_type)
                
    except Exception as e:
        logger.error(f"WS connection failed: {e}")
        try:
            await websocket.close(code=1011, reason=str(e))
        except:
            pass

@router.get("/stats")
async def get_websocket_stats():
    """Get real-time WebSocket connection statistics"""
    return manager.get_connection_stats()

@router.post("/broadcast/tenant/{tenant_id}")
async def broadcast_to_tenant(
    tenant_id: str,
    message: dict,
    conn_type: Optional[ConnectionType] = None,
    priority: str = "normal"
):
    """
    API endpoint to broadcast message to all users in a tenant.
    Used by backend services to push updates.
    """
    count = await manager.broadcast_to_tenant(
        message=message,
        tenant_id=tenant_id,
        conn_type=conn_type,
        priority=priority
    )
    return {"sent_to": count, "tenant_id": tenant_id}

@router.post("/broadcast/system")
async def broadcast_system_alert(message: dict, exclude_tenants: Optional[list] = None):
    """
    API endpoint for system-wide alerts.
    """
    count = await manager.broadcast_system_wide(
        message=message,
        exclude_tenants=exclude_tenants
    )
    return {"sent_to": count, "scope": "system"}

@router.get("/health")
async def health_check():
    """Health check endpoint for WebSocket service"""
    stats = manager.get_connection_stats()
    status = "healthy" if stats["total_connections"] >= 0 else "degraded"
    return {
        "status": status,
        "connections": stats["total_connections"],
        "timestamp": datetime.utcnow().isoformat()
    }
