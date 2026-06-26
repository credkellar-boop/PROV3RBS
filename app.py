from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from src.socket_manager import ConnectionManager
from src.engine import get_proverb
from src.video_manager import generate_video_token
from src.localization import load_locale

app = FastAPI()
manager = ConnectionManager()

# Mount static files and templates
app.mount("/static", StaticFiles(directory="client"), name="static")
templates = Jinja2Templates(directory="client")

class TokenRequest(BaseModel):
    room_name: str
    identity: str

@app.get("/", response_class=HTMLResponse)
async def get_ui(request: Request, lang: str = "en"):
    """Serves the main frontend UI with localized text."""
    locale_data = load_locale(lang)
    return templates.TemplateResponse("index.html", {"request": request, "locale": locale_data})

@app.get("/api/proverb")
async def read_proverb():
    """REST endpoint to fetch a random proverb."""
    return {"data": get_proverb()}

@app.post("/api/video/token")
async def get_video_token(req: TokenRequest):
    """Generates a LiveKit token for joining a video study room."""
    token = generate_video_token(req.room_name, req.identity)
    return {"token": token}

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    """Handles real-time chat communication."""
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Scholar {client_id}: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Scholar {client_id} disconnected.")
