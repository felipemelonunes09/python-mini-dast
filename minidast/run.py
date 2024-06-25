import asyncio
import websockets
from flask import json
from config import application_scanner
from task import scan_task

class Server:
    """
    class representing a WebSocket server for handling scan tasks.

    Attributes:
        - host (str): The host address for the server.
        - port (int): The port number for the server.

    Methods:
        - handle_client: A coroutine method for handling incoming WebSocket messages.
        - run_server: A coroutine method for running the WebSocket server.

    Usage:
        - server = Server("localhost", 8765)
        - asyncio.get_event_loop().run_until_complete(server.run_server())
        - asyncio.get_event_loop().run_forever()
    """

    def __init__(self, host, port):
        """Initialize the Server with a host and port."""
        self.host = host
        self.port = port

    async def handle_client(self, websocket, path):
        """Handle incoming WebSocket messages.

        Args:
            - websocket: The WebSocket connection object.
            - path: The path of the WebSocket request.
        """
        message = await websocket.recv()
        data = json.loads(message)
        scan_id = data.get("id", None)
        urls = data.get("urls", [])
        scan_task.apply_async(args=[scan_id, urls], kwargs={})

    async def run_server(self):
        """Run the WebSocket server."""
        start_server = websockets.serve(self.handle_client, self.host, self.port)
        await start_server

if __name__ == "__main__":

    from config import SERVER_HOST, SERVER_PORT

    server = Server(SERVER_HOST, SERVER_PORT)
    asyncio.get_event_loop().run_until_complete(server.run_server())
    asyncio.get_event_loop().run_forever()