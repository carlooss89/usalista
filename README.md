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
│   ├── schemas/ <br> # Schemas para entrada e saída de dados (Pydantic)
│   │   └── init.py <br>
│   │   └── user.py <br>
│   ├── services/ <br>
│   │   └── user_service.py <br>
│   ├── models/ <br> # Modelos das tabelas (ORM)
│   │   └── user.py <br>
│   ├── shopping_list.py <br>   
│   │── item_lista.py <br>
│   ├── services/ <br>
│   ├── dependencies.py <br>
│   ├── utils/ # Funções auxiliares (ex: segurança)
│   │   └── seguranca.py <br>
│   ├── routers/ <br> # Arquivos de rotas da API
│   │   └── user_router.py <br>
│   ├── db/ 
│   │   └── database.py <br> # Conexão com o banco de dados
│   └── main.py <br> # Ponto de entrada da aplicação FastAPI
├── .env <br> # Variáveis de ambiente (ex: DATABASE_URL)
├── .gitgnore <br> # Arquivos e diretórios que o Git deve ignorar ao rastrear alterações em um repositório
├── requirements.txt <br> # Pacotes e dependências do projeto
├── README.md <br> # Documentação do projeto
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

## 📌 Rotas de Usuário e Autenticação (até agora)
✅ Cadastro de Usuário
Endpoint:
```POST /users/```

Descrição:
Cria um novo usuário no sistema.

Exemplo de JSON para cadastro:

json
```{```
  ```"username": "Cadu89",```
  ```"email": "cadu89@example.com",```
  ```"password": "123456"```
```}```

Resposta de sucesso:
json
```{```
  ```"id": 1,```
  ```"username": "Cadu89",```
  ```"email": "cadu89@example.com"```
```}```

## ✅ Login e Geração de Token JWT
Endpoint:
```POST /auth/login```

Descrição:
Realiza a autenticação de usuário via e-mail e senha.
Se for bem-sucedido, retorna um token JWT que será usado nas rotas protegidas.

Formato de envio:
👉 O login usa o formato ```application/x-www-form-urlencoded```, como pede o padrão OAuth2.

Exemplo de corpo da requisição (form-data ou x-www-form-urlencoded):

Campo	Valor
username	```cadu89@example.com```
password	123456

Resposta de sucesso:
json
```{```
  ```"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",```
  ```"token_type": "bearer"```
```}```

## ✅ Observações importantes:
Login é feito pelo campo ```email```, mas o FastAPI espera um campo ```username``` no formulário OAuth2 (por isso usamos o email dentro do campo username no login).

As senhas são armazenadas de forma segura no banco, usando hash com ```bcrypt```.

Estamos usando JWT para autenticação nas próximas rotas protegidas.

## ✅ Rotas protegidas por Token JWT
A partir desta etapa, algumas rotas da API Usalista só podem ser acessadas com um token de autenticação válido.

🔒 Exemplo de rota protegida:
✔️ Obter dados do usuário logado
Endpoint:

```GET /users/me```

Descrição:
Retorna os dados do usuário atualmente autenticado.

Requer:
✅ Token JWT válido no cabeçalho da requisição.

## 📌 Endpoints - Itens da Lista
Esses endpoints permitem que o usuário autenticado faça o CRUD (Create, Read, Update, Delete) dos itens dentro de suas listas de compras.

Importante: Todos os endpoints abaixo exigem autenticação via Token JWT.

## 🔸 Criar um novo Item
POST /items/

Requer Token JWT

Body JSON Exemplo:
json
```{```
  ```"nome": "Arroz",```
  ```"quantidade": 2,```
  ```"comprado": false,```
  ```"shopping_list_id": 1```
```}```

. Resposta Exemplo (201 Created):
json
```{```
  ```"id": 5,```
  ```"nome": "Arroz",```
  ```"quantidade": 2,```
  ```"comprado": false,```
  ```"data_criacao": "2025-06-15T15:30:00.000Z",```
  ```"dono_id": 1,```
  ```"shopping_list_id": 1```
```}```

## 🔸 Listar Itens do Usuário
GET /items/

Requer Token JWT

Resposta Exemplo:

json
```[```
  ```{```
    ```"id": 1,```
    ```"nome": "Arroz",```
    ```"quantidade": 2,```
    ```"comprado": false,```
    ```"data_criacao": "2025-06-15T15:30:00.000Z",```
    ```"dono_id": 1,```
    ```"shopping_list_id": 1```
  ```},```
 ``` ...```
```]```

## 🔸 Obter detalhes de um Item específico
GET /items/{item_id}

Requer Token JWT

Exemplo: /items/1

Resposta Exemplo:

json
```{```
  ```"id": 1,```
  ```"nome": "Arroz",```
  ```"quantidade": 2,```
  ```"comprado": false,```
  ```"data_criacao": "2025-06-15T15:30:00.000Z",```
  ```"dono_id": 1,```
  ```"shopping_list_id": 1```
```}```

## 🔸 Atualizar um Item
PUT /items/{item_id}

Requer Token JWT

Body JSON Exemplo:

json
```{```
  ```"nome": "Arroz Integral",```
  ```"quantidade": 3,```
  ```"comprado": true,```
  ```"shopping_list_id": 1```
```}```

. Resposta Exemplo:

json
```{```
  ```"id": 1,```
  ```"nome": "Arroz Integral",```
  ```"quantidade": 3,```
  ```"comprado": true,```
  ```"data_criacao": "2025-06-15T15:30:00.000Z",```
  ```"dono_id": 1,```
  ```"shopping_list_id": 1```
```}```

## 🔸 Deletar um Item
DELETE ```/items/{item_id}```

Requer Token JWT

Exemplo: ```/items/1```

Resposta (204 No Content):

Nenhum conteúdo (status 204).

---
## 📋 Endpoints - Shopping Lists (Listas de Compras)
Estes endpoints são responsáveis por criar, listar, atualizar e excluir listas de compras associadas a cada usuário.

🔐 Autenticação
✅ Todos os endpoints desta seção exigem Token JWT de autenticação.
✅ O usuário só pode gerenciar suas próprias listas.

## 📥 Exemplo de JSON para criar uma lista (POST /shopping_lists/):
json
```{```
  ```"nome": "Compra da semana"```
```}```

## 📤 Exemplo de resposta (GET de uma lista):
json 
```{```
  ```"id": 1,```
  ```"nome": "Compra da semana",```
  ```"data_criacao": "2025-06-15T12:34:56.789Z",```
  ```"owner_id": 1,```
  ```"items": []```
```}```

---
## ✅ Regras de acesso para Shopping Lists:
▫️ O usuário só pode visualizar, editar ou excluir listas que ele mesmo criou.

▫️ No futuro: Quando for implementar o recurso de listas compartilhadas, o comportamento será:

▫️ Visualizar: Usuário poderá ver listas que foram compartilhadas com ele.

▫️ Editar/Deletar: Apenas o dono da lista ou pessoas com permissão explícita.

▫️ Adicionar itens: Poderá ser liberado para usuários convidados (configurável por permissão).

🏁

▶️ Como testar no Swagger:
1. Faça login com um usuário válido:
bash 
```POST /auth/token```

Envie um JSON com:
json
```{```
  ```"username": "seu_email@example.com",```
  ```"password": "suas_senha"```
```}```

Exemplo de retorno:
json
```{```
  ```"access_token": "eyJ0eXAiOiJKV1QiLCJhbGci...",```
  ```"token_type": "bearer"```
```}```

2. Copie o token (access_token retornado).

3. No Swagger, clique no botão "Authorize", cole o token assim:

```Bearer``` SEU_TOKEN_AQUI
Exemplo:
```Bearer``` Bearer eyJ0eXAiOiJKV1QiLCJhbGci...

4. Agora, acesse a rota:
```GET /users/me```

✅ Se o token for válido, você verá a resposta com os dados do usuário:
json
```{```
  ```"id": 1,```
  ```"nome": "Carlos",```
  ```"email": "carlos@example.com"```
```}```

❌ Se o token estiver ausente ou inválido, a API retornará:

json
```{```
  ```"detail": "Não autenticado"```
```}```

---

## 📌 Status do Projeto

🚧 Em desenvolvimento — funcionalidades de autenticação e CRUD de listas já implementadas.

### 🧪 Funcionalidades (em desenvolvimento)

● ✅Cadastro de usuários

● ✅ Login/autenticação

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
