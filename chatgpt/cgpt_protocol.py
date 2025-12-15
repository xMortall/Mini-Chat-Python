from bibliotecas import js

def pack(tipo, dados):
    return js.dumps({
        "type": tipo,
        "data": dados
    }).encode()

def unpack(msg):
    return js.loads(msg.decode())
