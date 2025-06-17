from sqlalchemy.orm import Session # Importa a sessão do SQLAlchemy para interagir com o banco de dados
from typing import List, Optional # Importa tipos de lista e opcional
from app import models, schemas # Importa os modelos e schemas necessários

# Função para criar uma nova lista de compras
def create_shopping_list(db: Session, shopping_list: schemas.shopping_list.ShoppingListCreate, user_id: int) -> models.ShoppingList: # Recebe a sessão do banco, o schema da lista de compras e o ID do usuário
    db_list = models.ShoppingList( # Cria uma nova instância do modelo ShoppingList
        nome=shopping_list.nome, 
        owner_id=user_id  # A lista fica associada ao usuário logado
    )
    db.add(db_list) 
    db.commit() 
    db.refresh(db_list) 
    return db_list 

# Função para buscar todas as listas de um usuário
def get_user_shopping_lists(db: Session, user_id: int) -> List[models.ShoppingList]:
    return db.query(models.ShoppingList).filter(models.ShoppingList.owner_id == user_id).all() 


# Função para buscar uma lista específica pelo id
def get_shopping_list(db: Session, shopping_list_id: int) -> Optional[models.ShoppingList]:
    return db.query(models.ShoppingList).filter(models.ShoppingList.id == shopping_list_id).first()

# Função para atualizar uma lista de compras
def update_shopping_list(db: Session, shopping_list: models.ShoppingList, update_data: schemas.shopping_list.ShoppingListUpdate) -> models.ShoppingList: 
    if update_data.nome is not None: 
        shopping_list.nome = update_data.nome 
    db.commit() 
    db.refresh(shopping_list)
    return shopping_list

# Função para deletar uma lista de compras
def delete_shopping_list(db: Session, shopping_list: models.ShoppingList): 
    db.delete(shopping_list) 
    db.commit() 

