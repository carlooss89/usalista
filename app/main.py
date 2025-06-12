from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from app.routers import user_router # importa o router

app = FastAPI(
    title="Usalista",
    description="Uma aplicação para gerenciar listas de compras com autenticação de usuários.",
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
