"""
Real-time WebSocket Manager for Multi-Tenant ERP System
Handles connection lifecycle, message routing, and synchronization
"""
import asyncio
import json
import logging
from datetime import datetime
from typing import Dict, Set, Optional, Any
from fastapi import WebSocket, WebSocketDisconnect
from pydantic import BaseModel

logger = logging.getLogger(__name__)


class ConnectionManager:
    """Manages WebSocket connections with multi-tenant isolation"""
    
    def __init__(self):
        # Tenant ID -> Set of WebSocket connections
        self.active_connections: Dict[str, Set[WebSocket]] = {}
        # Connection ID -> WebSocket mapping
        self.connection_map: Dict[str, WebSocket] = {}
        # User ID -> Set of Connection IDs
        self.user_connections: Dict[str, Set[str]] = {}
        # Sequence counters per tenant
        self.sequence_counters: Dict[str, int] = {}
        # Lock for thread-safe operations
        self.lock = asyncio.Lock()
        
    async def connect(self, websocket: WebSocket, tenant_id: str, user_id: str, connection_type: str = "client") -> str:
        """Accept connection and register it"""
        await websocket.accept()
        connection_id = f"{tenant_id}_{user_id}_{datetime.utcnow().timestamp()}"
        
        async with self.lock:
            if tenant_id not in self.active_connections:
                self.active_connections[tenant_id] = set()
                self.sequence_counters[tenant_id] = 0
            
            self.active_connections[tenant_id].add(websocket)
            self.connection_map[connection_id] = websocket
            
            if user_id not in self.user_connections:
                self.user_connections[user_id] = set()
            self.user_connections[user_id].add(connection_id)
            
        logger.info(f"WebSocket connected: {connection_id} (Tenant: {tenant_id}, User: {user_id}, Type: {connection_type})")
        return connection_id
    
    async def disconnect(self, connection_id: str):
        """Remove connection and clean up resources"""
        async with self.lock:
            if connection_id not in self.connection_map:
                return
                
            websocket = self.connection_map[connection_id]
            
            # Find tenant and remove from active connections
            for tenant_id, connections in self.active_connections.items():
                if websocket in connections:
                    connections.discard(websocket)
                    if not connections:
                        del self.active_connections[tenant_id]
                    break
            
            # Remove from connection map
            del self.connection_map[connection_id]
            
            # Remove from user connections
            for user_id, conn_ids in self.user_connections.items():
                if connection_id in conn_ids:
                    conn_ids.discard(connection_id)
                    if not conn_ids:
                        del self.user_connections[user_id]
                    break
        
        logger.info(f"WebSocket disconnected: {connection_id}")
    
    async def send_personal_message(self, message: dict, connection_id: str):
        """Send message to specific connection"""
        if connection_id not in self.connection_map:
            return
            
        try:
            websocket = self.connection_map[connection_id]
            await websocket.send_json(message)
        except Exception as e:
            logger.error(f"Error sending message to {connection_id}: {e}")
            await self.disconnect(connection_id)
    
    async def broadcast_to_tenant(self, message: dict, tenant_id: str, priority: str = "normal"):
        """Broadcast message to all connections in a tenant"""
        if tenant_id not in self.active_connections:
            return
            
        # Add sequence number and timestamp
        async with self.lock:
            self.sequence_counters[tenant_id] += 1
            message["seq"] = self.sequence_counters[tenant_id]
            message["timestamp"] = datetime.utcnow().isoformat()
            message["priority"] = priority
        
        dead_connections = []
        for websocket in self.active_connections[tenant_id]:
            try:
                await websocket.send_json(message)
            except Exception as e:
                logger.error(f"Broadcast error: {e}")
                dead_connections.append(websocket)
        
        # Clean up dead connections
        for websocket in dead_connections:
            for conn_id, ws in list(self.connection_map.items()):
                if ws == websocket:
                    await self.disconnect(conn_id)
    
    async def broadcast_to_user(self, message: dict, user_id: str):
        """Send message to all connections of a specific user"""
        if user_id not in self.user_connections:
            return
            
        for connection_id in self.user_connections[user_id]:
            await self.send_personal_message(message, connection_id)
    
    async def heartbeat_check(self):
        """Periodically check connection health"""
        while True:
            await asyncio.sleep(30)  # Check every 30 seconds
            dead_connections = []
            
            for conn_id, websocket in list(self.connection_map.items()):
                try:
                    # Send ping
                    await websocket.send_json({"type": "ping"})
                except:
                    dead_connections.append(conn_id)
            
            for conn_id in dead_connections:
                logger.warning(f"Removing dead connection: {conn_id}")
                await self.disconnect(conn_id)
    
    def get_stats(self) -> dict:
        """Get connection statistics"""
        return {
            "total_connections": len(self.connection_map),
            "active_tenants": len(self.active_connections),
            "connections_per_tenant": {
                tid: len(conns) for tid, conns in self.active_connections.items()
            }
        }


# Global instance
manager = ConnectionManager()
