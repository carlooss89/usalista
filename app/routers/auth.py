# app/routers/auth.py

from fastapi import APIRouter, Depends, HTTPException, status # Importando as dependências necessárias
from sqlalchemy.orm import Session # Importando o Session do SQLAlchemy
from fastapi.security import OAuth2PasswordRequestForm # Importando o OAuth2PasswordRequestForm para autenticação via formulário de login

from app.db.database import get_db # Importando a função get_db para obter a sessão do banco de dados
# from app.models import models / Importando os modelos do banco de dados
from app.models import User, ItemLista # Importando os modelos de usuário e item (se necessário)
from app.utils.seguranca import verify_password, criar_token_acesso # Importando funções de segurança para verificação de senha e criação de token JWT



router = APIRouter() # Criando um roteador FastAPI para agrupar as rotas de autenticação

@router.post("/auth/login") # Rota para autenticação de usuário via e-mail e senha
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)): # Função de login que recebe os dados do formulário e a sessão do banco de dados
    """
    Autenticação do usuário via e-mail e senha.
    Retorna um token JWT se for bem-sucedido.
    """
    usuario = db.query(User).filter(User.email == form_data.username).first() # Busca o usuário pelo e-mail fornecido no formulário

    if not usuario: # Se o usuário não for encontrado, lança uma exceção HTTP 401
        raise HTTPException( # Lança uma exceção HTTP 401 se o usuário não for encontrado
            status_code=status.HTTP_401_UNAUTHORIZED, # 
            detail="Usuário não encontrado", # Detalhe da exceção
            headers={"WWW-Authenticate": "Bearer"}, # Cabeçalho para indicar que a autenticação é do tipo Bearer
        )

    if not verificar_password(form_data.password, usuario.senha): # Verifica se a senha fornecida corresponde à senha armazenada no banco de dados
        raise HTTPException( # Se a senha estiver incorreta, lança uma exceção HTTP 401
            status_code=status.HTTP_401_UNAUTHORIZED, # Código de status HTTP 401 (Não autorizado)
            detail="Senha incorreta", # Detalhe da exceção
            headers={"WWW-Authenticate": "Bearer"}, # Cabeçalho para indicar que a autenticação é do tipo Bearer
        )

    # Gera o token com o ID e e-mail do usuário
    token = criar_token_acesso({"sub": str(usuario.id)}) # Cria o token de acesso usando a função de segurança, passando o ID do usuário como 'sub' (subject)

    return {"access_token": token, "token_type": "bearer"} # Retorna o token de acesso e o tipo de token (Bearer) em formato JSON
