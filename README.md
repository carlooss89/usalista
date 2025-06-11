#  🛒 usalista

**usalista** é uma API para controle de listas de compras entre usuários, com autenticação, permissões e registro de ações.

---

## 🚀 Objetivo do Projeto

O **Usalista** tem como objetivo permitir que usuários criem, editem e acompanhem listas de compras de forma simples e eficiente. Esse projeto também serve como estudo prático de desenvolvimento back-end com Python e FastAPI.

---

## 🧱 Tecnologias Utilizadas

- 🐍 Python 3.12
- ⚡ FastAPI
- 🐘 PostgreSQL
- 🔐 Pydantic (validações e schemas)
- 🛠️ SQLAlchemy (ORM)
- 🐳 Docker (planejado para etapas futuras)
- 📦 dotenv (variáveis de ambiente)
- ✅ Uvicorn (servidor ASGI)
- 📁 Git e GitHub

---

## 📁 Estrutura de Pastas

usalista/ <br>
│
├── app/ <br>
│ ├── models/ <br>
│ │ ├── user.py <br>
│ │ └── item_lista.py # (a ser criado) <br>
│ ├── services/ <br>
│ ├── routers/ <br>
│ ├── database.py <br>
│ └── main.py <br>
│
├── .env <br>
├── requirements.txt <br>
├── README.md <br>
└── ... <br>

---

## ⚙️ Como Rodar o Projeto Localmente

## 1. **Clone o repositório**

*bash*

```git clone https://github.com/seu-usuario/usalista.git```
```cd usalista```

## 2. Crie o ambiente virtual

*bash*

```python -m venv venv```
```source venv/bin/activate```  # Linux/macOS
```venv\Scripts\activate```     # Windows

# 3. Instale as dependências

*bash*

```pip install -r requirements.txt```

# 4. Configure o arquivo .env

*env*

```DATABASE_URL=postgresql://usuario:senha@localhost:5432/usalista```

Execute o projeto

*bash*

```uvicorn app.main:app --reload```

🧪 Funcionalidades (em desenvolvimento)

● ✅Cadastro de usuários

● ⬜ Login/autenticação

● ⬜ CRUD de itens da lista

● ⬜ Compartilhamento de listas

● ⬜ Filtros e categorias

---
🛠️ Contribuindo
Caso queira contribuir, abra uma issue ou envie um pull request! Todo feedback é bem-vindo. 😄
---

📌 Autor
Projeto em construção por **carlooss89** 🚀🌎

📃 Licença (em desenvolvimento)
Este projeto está sob a licença MIT. Veja o arquivo *LICENSE* para mais detalhes.
