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

        texto = dados.decode()
        # Se houver ": " na string, pega só a parte depois do segundo ":"
        partes = texto.split(": ", 2)
        if len(partes) == 3:
            # partes = [endereço, nome, mensagem]
            remetente = partes[1]
            mensagem = partes[2]
            print(f"{remetente}: {mensagem}")
        else:
            print(texto)

async def enviar_mensagens(writer, nome):
    while True:
        mensagem = await asyncio.to_thread(input, "Digite uma mensagem: ")
        mensagem_com_nome = f"{nome}: {mensagem}"
        writer.write(mensagem_com_nome.encode())
        await writer.drain()

async def main():
    reader, writer = await asyncio.open_connection(ip, port)

    nome = await asyncio.to_thread(input, "Escolha seu nome: ")
    
    await asyncio.gather(
        receber_mensagens(reader),
        enviar_mensagens(writer, nome)
    )

asyncio.run(main())