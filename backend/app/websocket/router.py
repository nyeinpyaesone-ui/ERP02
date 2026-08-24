"""
WebSocket Router - Handles WebSocket endpoints and lifecycle
"""
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query, Header
from typing import Optional
import logging
from .manager import manager

logger = logging.getLogger(__name__)

router = APIRouter()


@router.websocket("/ws/{tenant_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    tenant_id: str,
    user_id: str = Query(..., description="User ID"),
    connection_type: str = Query("client", description="Connection type: client, admin, worker")
):
    """
    Main WebSocket endpoint for real-time communication
    Supports multi-tenant isolation with user-specific routing
    """
    # Validate authentication header (simplified - in production verify JWT)
    auth_header: Optional[str] = websocket.headers.get("authorization")
    if not auth_header:
        await websocket.close(code=4001, reason="Missing authorization")
        return
    
    try:
        # Connect and register
        connection_id = await manager.connect(websocket, tenant_id, user_id, connection_type)
        
        # Send welcome message
        await manager.send_personal_message(
            {
                "type": "connected",
                "connection_id": connection_id,
                "tenant_id": tenant_id,
                "user_id": user_id,
                "message": "WebSocket connection established"
            },
            connection_id
        )
        
        # Keep connection alive and handle messages
        while True:
            try:
                data = await websocket.receive_json()
                
                # Handle different message types
                msg_type = data.get("type")
                
                if msg_type == "ping":
                    await manager.send_personal_message({"type": "pong"}, connection_id)
                
                elif msg_type == "ack":
                    # Acknowledge receipt of a message
                    seq = data.get("seq")
                    logger.debug(f"Ack received for sequence {seq} from {connection_id}")
                
                elif msg_type == "subscribe":
                    # Subscribe to specific event channels
                    channels = data.get("channels", [])
                    logger.info(f"Connection {connection_id} subscribed to: {channels}")
                
                else:
                    logger.warning(f"Unknown message type: {msg_type}")
                    
            except WebSocketDisconnect:
                break
            except Exception as e:
                logger.error(f"Error receiving message: {e}")
                break
    
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
        try:
            await websocket.close(code=4000, reason=str(e))
        except:
            pass
    finally:
        # Clean up on disconnect
        if 'connection_id' in locals():
            await manager.disconnect(connection_id)


@router.get("/ws/stats")
async def get_websocket_stats():
    """Get WebSocket connection statistics"""
    return manager.get_stats()


@router.get("/ws/health")
async def websocket_health():
    """Health check endpoint"""
    stats = manager.get_stats()
    return {
        "status": "healthy",
        "connections": stats["total_connections"],
        "tenants": stats["active_tenants"]
    }
