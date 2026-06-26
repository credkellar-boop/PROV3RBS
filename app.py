from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from src.socket_manager import ConnectionManager
from src.engine import get_proverb

app = FastAPI()
manager = ConnectionManager()

@app.get("/proverb")
async def read_proverb():
    return {"data": get_proverb()}

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Client #{client_id}: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left")
      
