# Mini Chat em Python (Asyncio)

Este é um **mini chat cliente-servidor** desenvolvido em Python, usando a biblioteca `asyncio` para comunicação **assíncrona**.  
O projeto permite múltiplos clientes conectados ao mesmo tempo, com envio e recebimento de mensagens **simultâneos**, sem travamentos.

---

## 📌 Funcionalidades

- Servidor TCP que aceita múltiplos clientes
- Comunicação **assíncrona** (asyncio)  
- Broadcast de mensagens para todos os clientes conectados  
- Cliente que envia e recebe mensagens ao mesmo tempo  
- Estrutura simples, fácil de evoluir para:
  - Nomes de usuários
  - Comandos (`/online`, `/sair`)  
  - Salas de chat

---

## 🛠️ Tecnologias utilizadas

- Tudo no requirements.txt

---

## 📂 Estrutura do projeto

mini_chat/
│
├── server.py # Código do servidor
├── client.py # Código do cliente
├── bibliotecas.py # Onde está todas as bibliotecas
└── README.md # Este arquivo


---

## 🚀 Como rodar

### 1️⃣ Servidor

```bash
No terminal, execute:

c
python3 server.py
```

```bash
#Em outro terminal, execute:

python client.py


#O cliente conectará ao servidor e permitirá enviar mensagens.
#Você pode abrir vários clientes simultaneamente para testar o chat.
