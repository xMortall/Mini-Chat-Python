from bibliotecas import asyncio

ip = '127.0.0.1'
port = 8888

async def receber_mensagens(reader):
    """
    Recebe mensagens do servidor.
    """
    
    while True:
        dados = await reader.read(100)
        if not dados:
            break
        print(f"Mensagem recebida: {dados.decode()}")

async def enviar_mensagens(writer):
    while True:
        mensagem = await asyncio.to_thread(input, "Digite uma mensagem: ")
        writer.write(mensagem.encode())
        await writer.drain()

async def main():
    reader, writer = await asyncio.open_connection(ip, port)
    
    await asyncio.gather(
        receber_mensagens(reader),
        enviar_mensagens(writer)
    )

asyncio.run(main())