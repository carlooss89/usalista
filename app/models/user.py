from sqlalchemy import Column, Integer, String #Importa os tipos de coluna que vamos usar: inteiros e strings.
from sqlalchemy.orm import relationship #Função que cria um vínculo ORM entre tabelas.
from app.database import Base #É a classe-mãe vinda do database.py; qualquer classe que estenda Base vira tabela.

class User(Base): #Define o modelo / tabela User.
    __tablename__ = "users" #Define o nome da tabela no banco de dados.

    id = Column(Integer, primary_key=True, index=True) #Define a coluna id como chave primária e índice. Coluna inteira, chave primária, com índice para buscas rápidas.
    
    username = Column(String, unique=True, index=True, nullable=False) #Coluna de nome de usuário, única, com índice para buscas rápidas e não pode ser nula.
    
    email = Column(String, unique=True, index=True, nullable=False) #Coluna de email, única, com índice para buscas rápidas e não pode ser nula.
    
    hashed_password = Column(String, nullable=False) #Coluna de senha criptografada, não pode ser nula.

    lists = relationship("ShoppingList", back_populates="owner") #Cria um relacionamento com a tabela ShoppingList, onde "owner" é o nome do atributo na classe ShoppingList que referencia o usuário.
    # Isso permite acessar as listas de compras de um usuário diretamente através do objeto User.
    
    
