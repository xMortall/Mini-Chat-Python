from bibliotecas import asyncio
from cgpt_protocol import pack, unpack

async def main():
    nome = input("Nome: ")

    reader, writer = await asyncio.open_connection("127.0.0.1", 5000)
    writer.write(nome.encode())
    await writer.drain()

    async def receber():
        while True:
            msg = await reader.read(1024)
            if not msg:
                break
            data = unpack(msg)
            print(data["data"])

    async def enviar():
        while True:
            texto = await asyncio.to_thread(input)
            if texto.startswith("/"):
                writer.write(pack("cmd", texto))
            else:
                writer.write(pack("msg", texto))
            await writer.drain()

    await asyncio.gather(receber(), enviar())

asyncio.run(main())
