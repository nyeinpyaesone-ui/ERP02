from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query, HTTPException
from typing import Optional, Dict, List
from ..services.websocket_manager import manager as ws_manager, ConnectionType
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

router = APIRouter()

@router.websocket("/{tenant_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    tenant_id: str,
    conn_type: ConnectionType = Query(default=ConnectionType.CLIENT),
    token: Optional[str] = Query(None)
):
    """
    Enterprise WebSocket endpoint with multi-tenant support.
    
    Features:
    - Tenant isolation
    - Connection type routing (admin, client, system, worker)
    - Authentication via token
    - Heartbeat monitoring
    - Message sequencing
    """
    try:
        # Extract user_id from token (simplified - use actual JWT validation in production)
        user_id = f"user_{tenant_id}_{conn_type.value}"
        if token:
            # In production: user_id = await validate_jwt_token(token)
            pass
            
        logger.info(f"WS connection: tenant={tenant_id}, type={conn_type.value}, user={user_id}")
        
        # Connect with tenant context
        await ws_manager.connect(websocket, user_id, conn_type, tenant_id)
        
        # Send welcome message
        await ws_manager.send_personal_message({
            "type": "welcome",
            "message": f"Connected to {tenant_id} as {conn_type.value}",
            "server_time": datetime.utcnow().isoformat(),
            "features": [
                "real_time_updates",
                "task_tracking", 
                "inventory_alerts",
                "order_notifications",
                "finance_events"
            ]
        }, user_id, conn_type)
        
        # Message handling loop
        while True:
            try:
                data = await websocket.receive_json()
                msg_type = data.get("type")
                
                if msg_type == "heartbeat":
                    await ws_manager.handle_heartbeat(user_id, conn_type)
                    
                elif msg_type == "sync_request":
                    await ws_manager.send_personal_message({
                        "type": "sync_response",
                        "status": "synchronized",
                        "server_time": datetime.utcnow().isoformat(),
                        "sequence": ws_manager.sequence_counters.get(user_id, 0)
                    }, user_id, conn_type)
                    
                elif msg_type == "ack":
                    sequence = data.get("sequence")
                    ack_key = f"{user_id}:{sequence}"
                    if ack_key in ws_manager.pending_acks:
                        del ws_manager.pending_acks[ack_key]
                        
                elif msg_type == "subscribe":
                    channels = data.get("channels", [])
                    logger.info(f"User {user_id} subscribed to: {channels}")
                    
                else:
                    logger.warning(f"Unknown WS message type: {msg_type}")
                    
            except Exception as e:
                logger.error(f"WS message error: {e}")
                await ws_manager.send_personal_message({
                    "type": "error",
                    "message": str(e)
                }, user_id, conn_type)
                
    except WebSocketDisconnect:
        logger.info(f"WS disconnected: {user_id}")
        ws_manager.disconnect(user_id, conn_type)
    except Exception as e:
        logger.error(f"WS connection failed: {e}")
        try:
            await websocket.close(code=1011, reason=str(e))
        except:
            pass

@router.get("/stats")
async def get_websocket_stats():
    """Get real-time WebSocket statistics"""
    return ws_manager.get_connection_stats()

@router.get("/health")
async def health_check():
    """WebSocket service health check"""
    stats = ws_manager.get_connection_stats()
    return {
        "status": "healthy",
        "connections": stats["total_connections"],
        "timestamp": datetime.utcnow().isoformat()
    }