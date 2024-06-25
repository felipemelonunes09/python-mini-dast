import websockets

from flask import json
from models.Scan import Scan

from config import WEB_SOCKET_HOST, WEB_SOCKET_PORT

async def notify_scan_created(scan: Scan):
    uri = f"ws://{WEB_SOCKET_HOST}:{WEB_SOCKET_PORT}"  # WebSocket server address
    async with websockets.connect(uri) as websocket:

        urls = []
        for application_url in scan.Urls:
            urls.append({
                "url": application_url.Url,
                "name": application_url.Name
            })

        data = {
            "id":               scan.Id,
            "urls":             urls,
            "application_name": scan.ApplicationName
        }

        await websocket.send(json.dumps(data))

