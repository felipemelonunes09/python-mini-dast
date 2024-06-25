import asyncio
import websockets
import task

from flask import json

from config import application_scanner

async def server(websocket, path):

    message = await websocket.recv()
    data = json.loads(message)

    scan_id = data.get("id", None)
    urls = data.get("urls", [])

    task.scan_task.apply_async(args=[scan_id, urls], kwargs={})


if __name__ == "__main__":

    start_server = websockets.serve(server, "0.0.0.0", 8765)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()