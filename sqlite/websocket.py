import asyncio
import websockets
import sqlite3
import json

connected = set()

conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()

async def handler(websocket, path):
    connected.add(websocket)
    try:
        cursor.execute('SELECT * FROM bookshelf')
        initial_data = cursor.fetchall()
        await websocket.send(json.dumps(initial_data))
        
        async for message in websocket:
            for client in connected:
                if client != websocket:
                    await client.send(message)
    finally:
        connected.remove(websocket)

start_server = websockets.serve(handler, 'localhost', 12345)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
