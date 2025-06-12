from fastapi import FastAPI # Importando o FastAPI para criar a aplicação
from fastapi.middleware.cors import CORSMiddleware # Importando o middleware CORS para permitir requisições de diferentes origens
from app.routers import user_router # importa o router

app = FastAPI(  # Cria uma instância do FastAPI, que é a aplicação principal 
    title="Usalista", # Título da API, que será exibido na documentação Swagger
    description="Uma aplicação para gerenciar listas de compras com autenticação de usuários.", # Descrição da API, que será exibida na documentação Swagger
    version="1.0.0"
)

app.include_router(user_router.router) # Inclui no app / Inclui o router de usuários

app.add_middleware( # Adiciona o middleware CORS para permitir requisições de diferentes origens
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/") # Rota raiz da API
def read_root(): # Função que retorna uma mensagem de boas-vindas
    return {"message": "Bem-vindo à API Usalista!"} # Rota de boas-vindas da API
