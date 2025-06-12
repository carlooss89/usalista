from sqlalchemy import Column, Integer, String, ForeignKey #Importa os tipos de coluna que vamos usar: inteiros, strings e chaves estrangeiras.

from sqlalchemy.orm import relationship #Função que cria um vínculo ORM entre tabelas.

from app.db.base import Base # É a classe-mãe vinda do base.py; qualquer classe que estenda Base vira tabela.

from app.db.database import Base #É a classe-mãe vinda do database.py; qualquer classe que estenda Base vira tabela.

class ShoppingList(Base): #Nome da tabela shopping_lists. Define o modelo / tabela ShoppingList.
    __tablename__ = "shopping_lists" #Define o nome da tabela no banco de dados.

    id = Column(Integer, primary_key=True, index=True) #Define a coluna id como chave primária e índice. Coluna inteira, chave primária, com índice para buscas rápidas.
    
    title = Column(String, index=True, nullable=False) #title – rótulo da lista (“Compra da semana”). Índice melhora busca por título. Coluna de título da lista, com índice para buscas rápidas e não pode ser nula.
    
    owner_id = Column(Integer, ForeignKey("users.id")) # owner_id – chave estrangeira que referencia o id do usuário na tabela users. Coluna inteira, chave estrangeira que referencia a tabela de usuários. owner_id conecta cada lista a um usuário; ForeignKey("users.id") garante integridade referencial.

    owner = relationship("User", back_populates="lists") # Cria um relacionamento com a tabela User, onde "lists" é o nome do atributo na classe User que referencia as listas de compras do usuário. owner é a volta do relacionamento: cada lista “sabe” quem é seu usuário.
    
    items = relationship("ItemLista", back_populates="shopping_list", cascade="all, delete-orphan") # Cria um relacionamento com a tabela ItemLista, onde "shopping_list" é o nome do atributo na classe ItemLista que referencia a lista de compras. items é a volta do relacionamento: cada lista “sabe” quais itens ela contém.
