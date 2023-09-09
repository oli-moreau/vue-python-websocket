import asyncio
import websockets

connected = set()

async def handler(websocket, path):
    # Register websocket connection
    connected.add(websocket)
    try:
        async for message in websocket:
            # Broadcast message to all connected clients
            for client in connected:
                if client != websocket:
                    await client.send(message)
    finally:
        # Unregister websocket connection
        connected.remove(websocket)

start_server = websockets.serve(handler, 'localhost', 12345)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
