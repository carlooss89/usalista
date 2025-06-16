# app/dependencies.py

from fastapi import Depends, HTTPException, status # Importa as dependências necessárias do FastAPI 
from fastapi.security import OAuth2PasswordBearer # Importa o esquema de segurança OAuth2 para autenticação via token
from jose import JWTError, jwt # Importa as bibliotecas para manipulação de JWT (JSON Web Tokens)
from sqlalchemy.orm import Session # Importa a sessão do SQLAlchemy para interagir com o banco de dados

from app.db.database import get_db # Importa a função para obter a sessão do banco de dados
from app.models import User # Importa o modelo User, que representa a tabela de usuários no banco de dados
from app.utils.seguranca import SECRET_KEY, ALGORITHM  # Importa os dados usados no token

# Configuração do esquema de segurança para OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")  # Rota de login que gera o token

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """Função para validar o token JWT e retornar o usuário atual"""

    try:
        # Decodifica o token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub") # Obtém o ID do usuário do payload do token

        if user_id is None: # Verifica se o ID do usuário está presente no payload
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Token inválido - ID de usuário não encontrado",
                headers={"WWW-Authenticate": "Bearer"},
            )

    except JWTError: # Captura erros de decodificação do token
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Busca o usuário no banco de dados
    user = db.query(User).filter(User.id == int(user_id)).first()

    if user is None:    # Verifica se o usuário existe no banco de dados
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não encontrado",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user # Retorna o usuário atual se tudo estiver correto
