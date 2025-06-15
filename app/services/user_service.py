# app/services/user_service.py

from sqlalchemy.orm import Session # Importando Session do SQLAlchemy
from app.models.user import User # Importando o modelo User
from app.schemas.user import UserCreate # Supondo que você tenha esse schema / Importando o schema UserCreate 
from app.utils.seguranca import get_password_hash  # Usando a função centralizada para hash de senhas 
# from passlib.context import CryptContext / Importando CryptContext para hash de senhas

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") / Configurando o contexto de hash de senha

# def get_password_hash(password: str) -> str: / Retorna a senha criptografada 
    # return pwd_context.hash(password) # Removido, pois agora usamos a função centralizada get_password_hash

def create_user(db: Session, user: UserCreate) -> User: # Função para criar um novo usuário no banco de dados / db: Session: o banco de dados é injetado via dependência do FastAPI.
    
    existing_user = get_user_by_email(db, user.email) # Verifica se o usuário já existe pelo e-mail
    if existing_user:
        raise ValueError("Email já cadastrado!") # Lança uma exceção se o e-mail já estiver cadastrado
    
    db_user = User(  # Cria uma instância do modelo User com os dados do schema UserCreate
        username=user.username,  
        email=user.email,
        hashed_password=get_password_hash(user.password) # Em produção, você deve hash a senha! Cria um novo usuário com os dados do schema UserCreate
    )
    db.add(db_user) # Adiciona o usuário à sessão do banco de dados
    db.commit() # Comita as mudanças no banco de dados
    db.refresh(db_user) # Atualiza o objeto db_user com os dados do banco de dados
    return db_user # Retorna o usuário criado

# Função para buscar usuário por ID
def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()

# Função para buscar usuário por e-mail
def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

# Função para retornar todos os usuários (opcional)
def get_all_users(db: Session) -> list[User]:
    return db.query(User).all()
