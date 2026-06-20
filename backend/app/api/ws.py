"""WebSocket for real-time ERP updates with tenant isolation."""
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import Dict, List

router = APIRouter()

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, tenant_id: str):
        await websocket.accept()
        self.active_connections.setdefault(tenant_id, []).append(websocket)

    def disconnect(self, websocket: WebSocket, tenant_id: str):
        if tenant_id in self.active_connections:
            self.active_connections[tenant_id].remove(websocket)

    async def broadcast(self, tenant_id: str, message: dict):
        for ws in self.active_connections.get(tenant_id, []):
            await ws.send_json(message)

    async def send_to_user(self, tenant_id: str, user_id: str, message: dict):
        # In production, track user_id per websocket
        for ws in self.active_connections.get(tenant_id, []):
            await ws.send_json({"target_user": user_id, **message})

manager = ConnectionManager()

@router.websocket("/{tenant_id}")
async def websocket_endpoint(websocket: WebSocket, tenant_id: str):
    await manager.connect(websocket, tenant_id)
    try:
        while True:
            data = await websocket.receive_json()
            await websocket.send_json({"type": "echo", "data": data, "timestamp": "now"})
    except WebSocketDisconnect:
        manager.disconnect(websocket, tenant_id)
