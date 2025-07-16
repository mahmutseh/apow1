from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import json

app = FastAPI()

# Allow any origin for simplicity
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BINANCE_WS = "wss://fstream.binance.com/stream?streams=btcusdt@trade"

# Placeholder in-memory storage
connected_clients = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        connected_clients.remove(websocket)

async def binance_listener():
    import websockets
    async for conn in websockets.connect(BINANCE_WS):
        try:
            async for msg in conn:
                data = json.loads(msg)
                for ws in connected_clients:
                    await ws.send_json(data)
        except Exception:
            await asyncio.sleep(5)
            continue

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(binance_listener())
