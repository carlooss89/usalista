from pydantic import BaseModel # BaseModel do Pydantic para validação de dados
from typing import List, Optional # Listas e tipos opcionais
from datetime import datetime  # Para manipulação de datas
from app.schemas.item_lista import ItemListaOut  # Representação de um item na lista, para resposta detalhada

class ShoppingListBase(BaseModel): # Base para a lista de compras
    nome: str  # Nome da lista de compras (ex: "Compra da Semana")

class ShoppingListCreate(ShoppingListBase): # Modelo para criação de uma nova lista de compras
    pass  # Por enquanto, ao criar uma lista, só exigimos o nome.

class ShoppingListUpdate(BaseModel): # Modelo para atualização de uma lista de compras
    nome: Optional[str] = None  # Permite atualizar o nome da lista (opcional)

class ShoppingListOut(BaseModel): # Modelo de saída para a lista de compras
    id: int 
    nome: str 
    data_criacao: datetime 
    owner_id: int 
    items: List[ItemListaOut] = []  # Lista de itens dentro dessa lista de compras (retorna já os itens também)

    class Config: # Configuração para o Pydantic
        orm_mode = True  # Permite conversão direta dos objetos SQLAlchemy para os schemas Pydantic

