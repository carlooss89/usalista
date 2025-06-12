from sqlalchemy import create_engine # Importa o create_engine do SQLAlchemy, que é responsável por criar a conexão com o banco de dados. É como ligar os cabos entre o seu app e o PostgreSQL. 

from sqlalchemy.ext.declarative import declarative_base
#Aqui importamos uma ferramenta para criar a base dos modelos (tabelas).Todos os arquivos dentro de models/ vão herdar essa base para funcionar como tabelas no banco.


from sqlalchemy.orm import sessionmaker, Session
#Importa o sessionmaker do SQLAlchemy, que é usado para criar sessões de banco de dados.
#sessionmaker é o fábricante de sessões — ou seja, com ele você cria sessões para ler e gravar dados no banco.

from dotenv import load_dotenv
#Importa o load_dotenv que lê o conteúdo do .env, onde está guardada a DATABASE_URL e outras variáveis secretas.

import os # Usamos a biblioteca padrão os para acessar variáveis de ambiente que foram carregadas do .env.

from app.db.base import Base # Importa a classe Base que foi criada no arquivo base.py. Essa classe é a base para todos os modelos do banco de dados, como User, ShoppingList e ItemLista.
import app.models # Importa os modelos do banco de dados, como User, ShoppingList e ItemLista. Isso é necessário para que o SQLAlchemy reconheça essas tabelas quando criarmos o banco de dados.


load_dotenv() # Carrega variáveis do .env

DATABASE_URL = os.getenv("DATABASE_URL") #URL do banco de dados vinda do .env

engine = create_engine(DATABASE_URL) # Cria o engine com SQLAlchemy

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # Cria uma fábrica de sessões

Base = declarative_base() # Cria a classe base para todos os seus modelos (ex: usuários, itens, listas, etc.). Todos os modelos do projeto vão herdar de Base para se tornarem tabelas no banco.


def get_db(): # Função para obter a sessão do banco de dados
    db: Session = SessionLocal() # Cria uma nova sessão do banco de dados
    try: # Tenta executar o bloco de código
        yield db # Retorna a sessão para ser usada nas rotas
    finally:    # Garante que a sessão será fechada após o uso
        db.close() # Fecha a sessão do banco de dados
# Isso é importante para liberar recursos e evitar vazamentos de memória.