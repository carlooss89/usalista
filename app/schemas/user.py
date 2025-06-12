# app/schemas/user.py

from pydantic import BaseModel, EmailStr # Importando BaseModel e EmailStr do Pydantic para validação de dados

# Schema usado para criar um novo usuário (entrada de dados)
class UserCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str

# Schema de resposta (opcional para rotas de retorno)
class UserOut(BaseModel):
    id: int
    nome: str
    email: EmailStr

    class Config:
        orm_mode = True  # Permite que o Pydantic leia objetos do SQLAlchemy
