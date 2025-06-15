# app/schemas/user.py

from pydantic import BaseModel, EmailStr # Importando BaseModel e EmailStr do Pydantic para validação de dados

# Schema usado para criar um novo usuário (entrada de dados)
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel): # Schema usado para retornar os dados do usuário
    id: int
    username: str
    email: EmailStr

    model_config = { # Configuração do modelo Pydantic
        "from_attributes": True # Permite que o Pydantic crie o modelo a partir de atributos do SQLAlchemy
    }