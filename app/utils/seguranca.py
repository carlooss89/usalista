from passlib.context import CryptContext # Importa o contexto de criptografia do Passlib


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # Cria um contexto de criptografia usando o algoritmo bcrypt, que é seguro para armazenar senhas.

def get_password_hash(password: str) -> str: # Função para gerar o hash da senha
    return pwd_context.hash(password) # Recebe uma senha em texto simples e retorna o hash criptografado dela usando bcrypt.

def verify_password(plain_password: str, hashed_password: str) -> bool: # Função para verificar se a senha em texto simples corresponde ao hash armazenado
    
    return pwd_context.verify(plain_password, hashed_password) # Função para verificar se a senha em texto simples corresponde ao hash armazenado
