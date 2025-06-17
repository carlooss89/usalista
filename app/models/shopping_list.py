from app.db.database import Base #É a classe-mãe vinda do database.py; qualquer classe que estenda Base vira tabela.
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime #Importa os tipos de coluna que vamos usar: inteiros, strings e chaves estrangeiras.
from sqlalchemy.orm import relationship #Função que cria um vínculo ORM entre tabelas.
from datetime import datetime #Importa a classe datetime para manipular datas e horas.
from app.models.item_lista import ItemLista # Relacionamento com os itens da lista / Importa o modelo ItemLista, que representa a tabela de itens de lista no banco de dados

class ShoppingList(Base): #Nome da tabela shopping_lists. Define o modelo / tabela ShoppingList.
    __tablename__ = "shopping_lists" #Define o nome da tabela no banco de dados.

    id = Column(Integer, primary_key=True, index=True) #Define a coluna id como chave primária e índice. Coluna inteira, chave primária, com índice para buscas rápidas.
    
    nome = Column(String, index=True, nullable=False) #nome – rótulo da lista (“Compra da semana”). Índice melhora busca por nome. Coluna de nome da lista, com índice para buscas rápidas e não pode ser nula.

    data_criacao = Column(DateTime, default=datetime.utcnow) # data_criacao – data e hora de criação da lista. Coluna de data e hora, padrão é a data atual (UTC). 
    owner_id = Column(Integer, ForeignKey("users.id")) # Relacionamento com o dono da lista (User) / Um usuário pode ter várias listas
    owner = relationship("User", back_populates="lists") # Um usuário pode ter várias listas de compras
    items = relationship("ItemLista", back_populates="shopping_list", cascade="all, delete-orphan") # Uma lista pode ter vários items
    
    items = relationship("ItemLista", back_populates="shopping_list", cascade="all, delete-orphan") # Cria um relacionamento com a tabela ItemLista, onde "shopping_list" é o nome do atributo na classe ItemLista que referencia a lista de compras, "items" é a volta do relacionamento: cada lista “sabe” quais itens ela contém.
