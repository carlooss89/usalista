from fastapi import FastAPI # Importando o FastAPI para criar a aplicação
from fastapi.middleware.cors import CORSMiddleware # Importando o middleware CORS para permitir requisições de diferentes origens
from fastapi.openapi.utils import get_openapi # Importando a função get_openapi para customizar o esquema OpenAPI
from app.routers import user_router # importa o router
from app.routers import auth # Estava "routes" mudei para "routers" / Importa o módulo de autenticação, que contém as rotas de login e autenticação
from app.db.database import Base, engine # Importa a classe Base e o engine do banco de dados para inicialização
from app.models.user import User # Importa o modelo User, que define a estrutura da tabela de usuários 

Base.metadata.create_all(bind=engine) # Cria todas as tabelas definidas nos modelos que herdam de Base, como User, ShoppingList e ItemLista. Isso é necessário para garantir que o banco de dados esteja atualizado com a estrutura definida nos modelos.

app = FastAPI(  # Cria uma instância do FastAPI, que é a aplicação principal 
    title="Usalista", # Título da API, que será exibido na documentação Swagger
    description="Uma aplicação para gerenciar listas de compras com autenticação de usuários.", # Descrição da API, que será exibida na documentação Swagger
    version="1.0.0"
)

app.include_router(user_router.router, prefix="/users", tags=["Usuários"]) # Inclui o roteador de usuários, com prefixo "/users" e tag "Usuários" para organização na documentação Swagger
app.include_router(auth.router, prefix="/auth", tags=["Autenticação"]) # Inclui o roteador de autenticação, com prefixo "/auth" e tag "Autenticação" para organização na documentação Swagger

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

# Função para customizar o OpenAPI e ativar o botão "Authorize" no Swagger
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi( # Importa a função get_openapi do FastAPI para gerar o esquema OpenAPI
        title="Usalista",
        version="1.0.0", 
        description="Uma aplicação para gerenciar listas de compras com autenticação de usuários.", 
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": { # Nome do esquema de segurança
            "type": "http", # Tipo HTTP
            "scheme": "bearer", # Tipo de autenticação Bearer
            "bearerFormat": "JWT", # Formato JWT
        }
    }
    # Faz com que todas as rotas exijam por padrão o esquema de segurança
    for path in openapi_schema["paths"]:
        for method in openapi_schema["paths"][path]:
            if "security" not in openapi_schema["paths"][path][method]:
                openapi_schema["paths"][path][method]["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

# Aponta o OpenAPI da aplicação para a nova função customizada
app.openapi = custom_openapi

