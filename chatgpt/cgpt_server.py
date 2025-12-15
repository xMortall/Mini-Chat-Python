from bibliotecas import asyncio
from cgpt_protocol import pack, unpack

clientes = {}

async def handle_client(reader, writer):
    nome = (await reader.read(1024)).decode()
    clientes[writer] = nome

    print(f"{nome} conectado")
    await broadcast(pack("status", f"{nome} entrou no chat"))

    try:
        while True:
            msg = await reader.read(1024)
            if not msg:
                break

            data = unpack(msg)

            if data["type"] == "msg":
                await broadcast(pack("msg", f"{nome}: {data['data']}"))

            elif data["type"] == "cmd" and data["data"] == "/online":
                writer.write(pack("info", f"Online: {len(clientes)}"))
                await writer.drain()

    finally:
        del clientes[writer]
        await broadcast(pack("status", f"{nome} saiu"))
        writer.close()

async def broadcast(msg):
    for w in clientes:
        w.write(msg)
    await asyncio.gather(*(w.drain() for w in clientes))

async def main():
    server = await asyncio.start_server(handle_client, "0.0.0.0", 5000)
    print("Servidor online")
    async with server:
        await server.serve_forever()

asyncio.run(main())
