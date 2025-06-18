# dashboard_ui/routes.py

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from typing import List
import json
from loguru import logger

router = APIRouter()
clients: List[WebSocket] = []

@router.get("/")
async def dashboard():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Firewall Dashboard</title>
    </head>
    <body>
        <h2>Firewall Events</h2>
        <ul id="events"></ul>
        <script>
            const ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = (event) => {
                const msg = JSON.parse(event.data);
                const li = document.createElement("li");
                li.textContent = `[${msg.timestamp}] ${msg.type} - ${msg.detail}`;
                document.getElementById("events").appendChild(li);
            };
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    logger.info("WebSocket client connected.")

    try:
        while True:
            await websocket.receive_text()  # Optionally process incoming messages
    except WebSocketDisconnect:
        clients.remove(websocket)
        logger.warning("WebSocket client disconnected.")

async def broadcast_event(event: dict):
    for client in clients:
        try:
            await client.send_text(json.dumps(event))
        except Exception as e:
            logger.error(f"WebSocket broadcast error: {e}")

# dashboard_ui/__init__.py

from .routes import router, broadcast_event
