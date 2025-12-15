from bibliotecas import asyncio

client_connections = set() # Quant de clientes
ip = '127.0.0.1' # Endereço IP do servidor
port = 8888 # Porta do servidor


async def client_msg(reader, writer):
    """
    Define uma conexão com o cliente
    e gerencia o envio e recebimento de mensagens.
    """

    add_client = writer.get_extra_info('peername') # Pega o Ip e porta
    print(f"Connection from {add_client}")
    client_connections.add(writer)

    try:
        while True:
            data = await reader.read(100) # Recebe a mensagem até 100 bytes
            if not data:
                break
            msg = data.decode()
            print(f"{add_client} disse: {msg}")

            for client in client_connections:
                if client != writer:
                    client.write(f"{add_client}: {msg}".encode())
                    await client.drain()
    finally:
        print(f"O {add_client} desconectou-se")
        client_connections.remove(writer)
        writer.close()

async def main():
    """
    Cria server e aguarda conexões de clientes.
    """
    
    server = await asyncio.start_server(client_msg, ip, port)
    print(f"Servidor rodando em {ip}:{port}")
    async with server:
        await server.serve_forever()


asyncio.run(main())