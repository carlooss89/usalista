from passlib.context import CryptContext # Importa o contexto de criptografia do Passlib
from jose import JWTError, jwt # Importa o JWTError e jwt do JOSE para manipulação de tokens JWT
from datetime import datetime, timedelta # Importa datetime e timedelta para manipulação de datas e horas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # Cria um contexto de criptografia usando o algoritmo bcrypt, que é seguro para armazenar senhas.

SECRET_KEY = "sua_chave_secreta_super_segura" # Chave secreta usada para assinar os tokens JWT. Deve ser mantida em segredo e não deve ser compartilhada publicamente.
ALGORITHM = "HS256" # Algoritmo de assinatura usado para os tokens JWT. HS256 é um algoritmo de hash seguro.
TEMPO_EXPIRACAO_MIN = 30 # Tempo de expiração do token em minutos. Aqui está definido como 30 minutos, mas pode ser ajustado conforme necessário.

def get_password_hash(password: str) -> str: # Função para gerar o hash da senha
    return pwd_context.hash(password) # Recebe uma senha em texto simples e retorna o hash criptografado dela usando bcrypt.

def verify_password(plain_password: str, hashed_password: str) -> bool: # Função para verificar se a senha em texto simples corresponde ao hash armazenado
    
    return pwd_context.verify(plain_password, hashed_password) # Função para verificar se a senha em texto simples corresponde ao hash armazenado

def criar_token_acesso(dados: dict) -> str:
    dados_a_codificar = dados.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=TEMPO_EXPIRACAO_MIN)
    dados_a_codificar.update({"exp": expiracao})
    token_jwt = jwt.encode(dados_a_codificar, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt

def verificar_token(token: str) -> dict | None: # Função para verificar e decodificar um token JWT
    try: # Tenta decodificar o token usando a chave secreta e o algoritmo especificado
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]) # Decodifica o token e retorna o payload (dados contidos no token)
        return payload # Retorna o payload do token se a decodificação for bem-sucedida
    except JWTError: # Se ocorrer um erro durante a decodificação do token, como token expirado ou inválido
        return None # Retorna None se o token for inválido ou expirado
