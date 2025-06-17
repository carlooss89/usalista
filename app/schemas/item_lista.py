from pydantic import BaseModel # Para validação de dados
from datetime import datetime # Para manipular datas e horas
from typing import Optional # Para tipos opcionais

class ItemListaBase(BaseModel): # Base para os modelos de item de lista
    nome: str 
    quantidade: Optional[int] = 1 # Quantidade do item, padrão é 1
    comprado: Optional[bool] = False # Indica se o item foi comprado ou não

class ItemListaCreate(ItemListaBase): # Modelo para criação de um novo item de lista
    shopping_list_id: Optional[int] = None  # Por enquanto opcional, caso futuramente queira implementar múltiplas listas

class ItemListaOut(ItemListaBase): # Modelo de saída para exibir os itens da lista
    id: int 
    data_criacao: datetime # Data e hora de criação do item
    dono_id: int 

    class Config: # Configurações adicionais para o modelo
        orm_mode = True # Permite que o Pydantic converta modelos ORM para dicionários
