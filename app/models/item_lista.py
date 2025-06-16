from app.db.database import Base # É a classe-mãe vinda do database.py; qualquer classe que estenda Base vira tabela.
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey # Importa os tipos de coluna que vamos usar: inteiros, strings, booleanos e chaves estrangeiras.

from sqlalchemy.orm import relationship # Função que cria um vínculo ORM entre tabelas.

class ItemLista(Base): # Define o modelo / tabela ItemLista.
    __tablename__ = "itens_lista" # ← Define o nome da tabela no banco de dados.

    id = Column(Integer, primary_key=True, index=True) # ← id é a chave primária da tabela, que identifica unicamente cada item.
    nome = Column(String, nullable=False) # Ex: "Arroz"
    quantidade = Column(Integer, default=1) # Ex: 2 (quantidade de arroz)
    comprado = Column(Boolean, default=False) # Ex: False (se o item foi comprado ou não)

    shopping_list_id = Column(Integer, ForeignKey("shopping_lists.id")) # ← item pertence a uma lista / shopping_list_id é a chave estrangeira que conecta este item à lista de compras
    
    shopping_list = relationship("ShoppingList", back_populates="items") # ← vínculo de volta 
    # shopping_list é o nome do atributo na classe ShoppingList que referencia os itens da lista
