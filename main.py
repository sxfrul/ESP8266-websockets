import asyncio
import websockets

async def send_command(uri, command):
    async with websockets.connect(uri) as websocket:
        await websocket.send(command)

async def main():
    uri = "ws://172.20.10.7:80"  # Replace <nodeMCU_IP_address> with NodeMCU's IP address
    while True:
        command = input("Enter command (e.g., 'led1:on', 'led1:off', etc.): ")
        await send_command(uri, command)

asyncio.run(main())