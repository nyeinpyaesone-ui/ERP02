import asyncio
import logging
from typing import Dict, Set, Optional
from fastapi import WebSocket, WebSocketDisconnect
from enum import Enum
from datetime import datetime
import json

logger = logging.getLogger(__name__)

class ConnectionType(str, Enum):
    ADMIN = "admin"
    CLIENT = "client"
    SYSTEM = "system"
    WORKER = "worker"

class MessageType(str, Enum):
    TASK_UPDATE = "task_update"
    INVENTORY_ALERT = "inventory_alert"
    ORDER_STATUS = "order_status"
    FINANCE_NOTIFICATION = "finance_notification"
    SYSTEM_ALERT = "system_alert"
    HEARTBEAT = "heartbeat"
    SYNC_REQUEST = "sync_request"
    SYNC_RESPONSE = "sync_response"

class ConnectionManager:
    def __init__(self):
        # Active connections: {connection_type: {user_id: websocket}}
        self.active_connections: Dict[str, Dict[str, WebSocket]] = {
            ConnectionType.ADMIN: {},
            ConnectionType.CLIENT: {},
            ConnectionType.SYSTEM: {},
            ConnectionType.WORKER: {}
        }
        
        # Multi-tenant grouping: {tenant_id: set of user_ids}
        self.tenant_groups: Dict[str, Set[str]] = {}
        self.user_tenant_map: Dict[str, str] = {}
        
        # Connection metadata for health monitoring
        self.connection_metadata: Dict[str, dict] = {}
        
        # Sequence numbers for message ordering guarantee
        self.sequence_counters: Dict[str, int] = {}
        
        # Pending acknowledgments for reliability
        self.pending_acks: Dict[str, dict] = {}

    async def connect(self, websocket: WebSocket, user_id: str, conn_type: ConnectionType, tenant_id: Optional[str] = None):
        """Establish WebSocket connection with synchronization handshake"""
        await websocket.accept()
        
        # Store connection
        self.active_connections[conn_type][user_id] = websocket
        
        # Initialize sequence counter
        if user_id not in self.sequence_counters:
            self.sequence_counters[user_id] = 0
            
        # Handle tenant grouping for multi-tenancy
        if tenant_id:
            self.user_tenant_map[user_id] = tenant_id
            if tenant_id not in self.tenant_groups:
                self.tenant_groups[tenant_id] = set()
            self.tenant_groups[tenant_id].add(user_id)
            
        # Store metadata
        self.connection_metadata[user_id] = {
            "type": conn_type,
            "tenant_id": tenant_id,
            "connected_at": datetime.utcnow().isoformat(),
            "last_heartbeat": datetime.utcnow().timestamp(),
            "message_count": 0
        }
        
        logger.info(f"New {conn_type.value} connection: User={user_id}, Tenant={tenant_id}")
        
        # Send synchronization handshake response
        sync_payload = {
            "type": MessageType.SYNC_RESPONSE.value,
            "status": "connected",
            "user_id": user_id,
            "connection_type": conn_type.value,
            "tenant_id": tenant_id,
            "server_time": datetime.utcnow().isoformat(),
            "sequence_start": self.sequence_counters[user_id],
            "protocol_version": "2.0"
        }
        
        await websocket.send_json(sync_payload)
        logger.debug(f"Sync handshake completed for {user_id}")

    def disconnect(self, user_id: str, conn_type: ConnectionType):
        """Gracefully disconnect and cleanup resources"""
        if user_id in self.active_connections[conn_type]:
            del self.active_connections[conn_type][user_id]
            
        # Cleanup tenant mapping
        if user_id in self.user_tenant_map:
            tenant_id = self.user_tenant_map[user_id]
            if tenant_id in self.tenant_groups:
                self.tenant_groups[tenant_id].discard(user_id)
                if not self.tenant_groups[tenant_id]:
                    del self.tenant_groups[tenant_id]
            del self.user_tenant_map[user_id]
            
        # Cleanup metadata
        if user_id in self.connection_metadata:
            del self.connection_metadata[user_id]
            
        # Cleanup pending acks
        keys_to_remove = [k for k in self.pending_acks if k.startswith(f"{user_id}:")]
        for key in keys_to_remove:
            del self.pending_acks[key]
            
        logger.info(f"Connection closed: User={user_id}, Type={conn_type.value}")

    async def send_personal_message(self, message: dict, user_id: str, conn_type: ConnectionType, require_ack: bool = False):
        """Send message to specific user with optional acknowledgment requirement"""
        if user_id not in self.active_connections[conn_type]:
            logger.warning(f"User {user_id} not connected as {conn_type.value}")
            return False
            
        websocket = self.active_connections[conn_type][user_id]
        
        # Increment sequence number
        self.sequence_counters[user_id] = self.sequence_counters.get(user_id, 0) + 1
        message["sequence"] = self.sequence_counters[user_id]
        message["timestamp"] = datetime.utcnow().isoformat()
        
        try:
            await websocket.send_json(message)
            
            # Track pending acknowledgment if required
            if require_ack:
                ack_key = f"{user_id}:{self.sequence_counters[user_id]}"
                self.pending_acks[ack_key] = {
                    "message": message,
                    "sent_at": datetime.utcnow().timestamp(),
                    "retries": 0
                }
                
            # Update metadata
            if user_id in self.connection_metadata:
                self.connection_metadata[user_id]["message_count"] += 1
                self.connection_metadata[user_id]["last_heartbeat"] = datetime.utcnow().timestamp()
                
            return True
            
        except WebSocketDisconnect:
            logger.error(f"WebSocket disconnected while sending to {user_id}")
            self.disconnect(user_id, conn_type)
            return False
        except Exception as e:
            logger.error(f"Failed to send message to {user_id}: {e}")
            return False

    async def broadcast_to_tenant(self, message: dict, tenant_id: str, conn_type: Optional[ConnectionType] = None, priority: str = "normal"):
        """Broadcast message to all users in a tenant with optional type filtering"""
        if tenant_id not in self.tenant_groups:
            logger.debug(f"No active connections for tenant {tenant_id}")
            return 0
            
        success_count = 0
        message["priority"] = priority
        message["broadcast_scope"] = "tenant"
        message["target_tenant"] = tenant_id
        
        # High priority messages bypass some checks
        if priority == "critical":
            message["critical"] = True
            
        disconnected_users = []
        
        for user_id in self.tenant_groups[tenant_id]:
            # Determine which connection types to target
            target_types = [conn_type] if conn_type else list(ConnectionType)
            
            for ctype in target_types:
                if user_id in self.active_connections[ctype]:
                    try:
                        # Add user-specific sequence
                        self.sequence_counters[user_id] = self.sequence_counters.get(user_id, 0) + 1
                        msg_copy = message.copy()
                        msg_copy["sequence"] = self.sequence_counters[user_id]
                        msg_copy["recipient"] = user_id
                        
                        await self.active_connections[ctype][user_id].send_json(msg_copy)
                        success_count += 1
                        
                        if user_id in self.connection_metadata:
                            self.connection_metadata[user_id]["message_count"] += 1
                            
                        break  # Sent successfully to one connection type
                        
                    except WebSocketDisconnect:
                        disconnected_users.append((user_id, ctype))
                    except Exception as e:
                        logger.error(f"Broadcast error to {user_id}: {e}")
                        
        # Cleanup disconnected users
        for uid, ctype in disconnected_users:
            self.disconnect(uid, ctype)
            
        logger.info(f"Broadcast to tenant {tenant_id}: {success_count} successful")
        return success_count

    async def broadcast_system_wide(self, message: dict, exclude_tenants: Optional[list] = None):
        """Broadcast system-wide alert to all connected clients"""
        message["scope"] = "system"
        message["type"] = MessageType.SYSTEM_ALERT.value
        message["timestamp"] = datetime.utcnow().isoformat()
        
        total_sent = 0
        exclude_tenants = exclude_tenants or []
        
        for tenant_id, user_ids in self.tenant_groups.items():
            if tenant_id in exclude_tenants:
                continue
            sent = await self.broadcast_to_tenant(message, tenant_id)
            total_sent += sent
            
        # Also send to system monitors
        if "SYSTEM" in self.active_connections:
            for user_id in self.active_connections[ConnectionType.SYSTEM]:
                try:
                    await self.send_personal_message(message, user_id, ConnectionType.SYSTEM)
                    total_sent += 1
                except:
                    pass
                    
        logger.info(f"System-wide broadcast: {total_sent} recipients")
        return total_sent

    async def handle_heartbeat(self, user_id: str, conn_type: ConnectionType):
        """Process heartbeat and update connection health"""
        if user_id in self.connection_metadata:
            self.connection_metadata[user_id]["last_heartbeat"] = datetime.utcnow().timestamp()
            
        # Respond with heartbeat acknowledgment
        await self.send_personal_message({
            "type": MessageType.HEARTBEAT.value,
            "status": "alive",
            "server_time": datetime.utcnow().isoformat()
        }, user_id, conn_type)

    async def request_acknowledgment(self, user_id: str, conn_type: ConnectionType, message_id: str):
        """Request explicit acknowledgment for critical messages"""
        await self.send_personal_message({
            "type": "ack_request",
            "message_id": message_id,
            "requested_at": datetime.utcnow().isoformat()
        }, user_id, conn_type, require_ack=True)

    def get_connection_stats(self) -> dict:
        """Get real-time connection statistics"""
        stats = {
            "total_connections": sum(len(conns) for conns in self.active_connections.values()),
            "by_type": {ctype.value: len(conns) for ctype, conns in self.active_connections.items()},
            "active_tenants": len(self.tenant_groups),
            "pending_acks": len(self.pending_acks),
            "timestamp": datetime.utcnow().isoformat()
        }
        return stats

    async def cleanup_stale_connections(self, timeout_seconds: int = 300):
        """Periodic cleanup of stale connections based on heartbeat timeout"""
        current_time = datetime.utcnow().timestamp()
        stale_users = []
        
        for user_id, metadata in self.connection_metadata.items():
            last_heartbeat = metadata.get("last_heartbeat", 0)
            if current_time - last_heartbeat > timeout_seconds:
                stale_users.append((user_id, metadata["type"]))
                
        for user_id, conn_type in stale_users:
            logger.warning(f"Cleaning up stale connection: {user_id}")
            self.disconnect(user_id, conn_type)
            
        return len(stale_users)

# Singleton instance
manager = ConnectionManager()
