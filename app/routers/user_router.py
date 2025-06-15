# app/routers/user_router.py

from fastapi import APIRouter, Depends, HTTPException # Importando as dependências necessárias
from sqlalchemy.orm import Session # Importando o Session do SQLAlchemy

from app.db.database import get_db # Importando a função get_db para obter a sessão do banco de dados
from app.schemas.user import UserCreate, UserOut # Importando os schemas de entrada e saída do usuário
from app.services import user_service # Importando o serviço de usuário para manipulação de dados
from app.utils.seguranca import get_password_hash # Importando a função de hash de senha para segurança

router = APIRouter(tags=["Usuários"]) # Prefixo de rota e tag do Swagger para organização das rotas # Cria uma instância do APIRouter com a tag "Usuários" # prefix="/users", foi retirado o prefixo de rota, pois não é necessário aqui, por conta do prefixo já estar definido no main.py


@router.post("/", response_model=UserOut,status_code=201 ) # Rota para criar um novo usuário / adicionei o status_code=201 para indicar que o recurso foi criado com sucesso
def create_user(user: UserCreate, db: Session = Depends(get_db)): # Função para criar um usuário
    existing_user = user_service.get_user_by_email(db, user.email) # Verifica se o usuário já existe pelo email
    if existing_user: # Se o usuário já existir, lança uma exceção HTTP 400
        raise HTTPException(status_code=400, detail="Email já cadastrado") # Lança uma exceção HTTP 400 se o email já estiver cadastrado
    
    return user_service.create_user(db, user) # Cria o usuário e retorna o objeto criado


@router.get("/{user_id}", response_model=UserOut) # Rota para buscar usuário por ID
def get_user(user_id: int, db: Session = Depends(get_db)): # Função para obter um usuário pelo ID
    user = user_service.get_user_by_id(db, user_id) # Obtém o usuário pelo ID fornecido
    if not user: # Se o usuário não for encontrado, lança uma exceção HTTP 404
        raise HTTPException(status_code=404, detail="Usuário não encontrado") # Lança uma exceção HTTP 404 se o usuário não for encontrado
    
    return user # Retorna o usuário encontrado

@router.get("/all", response_model=list[UserOut]) # (Opcional) Rota para listar todos os usuários
def list_users(db: Session = Depends(get_db)): # Função para listar todos os usuários
    return user_service.get_all_users(db) # Retorna a lista de todos os usuários encontrados
