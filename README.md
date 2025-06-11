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
    ├── services/ <br>
    │   └── user_service.py <br>
│   ├── models/ <br>
│   ├── user.py <br>
│   ├── shopping_list.py <br>  
│   ├── shopping_list.py <br> 
│   └── item_lista.py <br>
│   ├── services/ <br>
│   ├── routers/ <br>
│   ├── database.py <br>
│   └── main.py <br>
│
├── .env <br>
├── requirements.txt <br>
├── README.md <br>
└──  <br>

---

## 🧩 Modelos de Dados: Listas de Compras e Itens

O projeto `usalista` possui dois modelos principais que representam a lógica de uma lista de compras real:

### 📋 `ShoppingList`

Representa uma lista de compras criada por um usuário.

| Campo         | Tipo     | Descrição                                |
|---------------|----------|------------------------------------------|
| `id`          | Integer  | Identificador único da lista             |
| `title`       | String   | Título da lista (ex: "Compra do mês")    |
| `owner_id`    | Integer  | Referência ao usuário dono da lista      |
| `items`       | Relacionamento | Lista de itens associados a esta lista |

### 🛒 `ItemLista`

Representa um item individual que pertence a uma lista de compras.

| Campo             | Tipo     | Descrição                                  |
|-------------------|----------|--------------------------------------------|
| `id`              | Integer  | Identificador único do item                |
| `nome`            | String   | Nome do item (ex: "Arroz")                 |
| `quantidade`      | Integer  | Quantidade desejada (ex: 2)                |
| `unidade`         | String   | Unidade de medida (ex: "kg", "unidade")    |
| `shopping_list_id`| Integer  | Referência à lista de compras (chave estrangeira) |

🔁 **Relacionamento entre eles:**
- Uma `ShoppingList` pode conter vários `ItemLista` (relação 1:N).
- O relacionamento é bidirecional com SQLAlchemy, permitindo navegar entre os modelos facilmente.
- Ao apagar uma `ShoppingList`, todos os seus `ItemLista` são removidos automaticamente (`cascade="all, delete-orphan"`).

---

## ✅ Exemplo de Uso

Imagine que o usuário João criou uma lista chamada **"Compra da semana"** e adicionou os itens:

- 2 kg de Arroz
- 1 pacote de Café
- 3 unidades de Maçã

Essa estrutura permite armazenar tudo isso de forma organizada e relacional no banco de dados.

---

## 📌 Status do Projeto

🚧 Em desenvolvimento — funcionalidades de autenticação e CRUD de listas já implementadas.

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
