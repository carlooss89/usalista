from fastapi import APIRouter, Depends, HTTPException, status  # Importa as dependências do FastAPI para criar rotas e gerenciar erros
from sqlalchemy.orm import Session # Importa a sessão do SQLAlchemy para interagir com o banco de dados
from typing import List # Importa tipos de lista para as respostas

from app import models, schemas, services # Importa os modelos, schemas e serviços necessários
from app.dependencies import get_db, get_current_user 

router = APIRouter( # Cria um roteador para organizar as rotas relacionadas às listas de compras
    prefix="/shopping-lists", # Define o prefixo para as rotas deste roteador
    tags=["Shopping Lists"] # Adiciona tags para categorizar as rotas na documentação automática do FastAPI
)

@router.post("/", response_model=schemas.shopping_list.ShoppingList) # Define a rota para criar uma nova lista de compras
def create_shopping_list( # Função para criar uma nova lista de compras
    shopping_list: schemas.shopping_list.ShoppingListCreate, 
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_user) 
):
    """
    Cria uma nova lista de compras para o usuário autenticado.
    """
    return services.shopping_list_service.create_shopping_list(db, shopping_list, current_user.id)

@router.get("/", response_model=List[schemas.shopping_list.ShoppingList]) # Define a rota para listar todas as listas de compras do usuário
def read_user_shopping_lists( 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user) # Obtém o usuário autenticado através de uma dependência
):
    """
    Lista todas as listas de compras do usuário autenticado.
    """
    return services.shopping_list_service.get_user_shopping_lists(db, current_user.id)

@router.get("/{shopping_list_id}", response_model=schemas.shopping_list.ShoppingList) # Define a rota para buscar uma lista de compras específica pelo ID
def read_shopping_list( 
    shopping_list_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user) # Obtém o usuário autenticado através de uma dependência
):
    """
    Busca uma lista de compras específica por ID, apenas se pertencer ao usuário.
    """
    db_list = services.shopping_list_service.get_shopping_list(db, shopping_list_id) # Busca a lista de compras pelo ID
    if db_list is None or db_list.owner_id != current_user.id: # Verifica se a lista existe e se pertence ao usuário autenticado
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lista não encontrada ou acesso negado.")
    return db_list

@router.put("/{shopping_list_id}", response_model=schemas.shopping_list.ShoppingList) # Define a rota para atualizar uma lista de compras específica pelo ID
def update_shopping_list( 
    shopping_list_id: int,
    update_data: schemas.shopping_list.ShoppingListUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """
    Atualiza o nome de uma lista de compras, apenas se ela pertencer ao usuário.
    """
    db_list = services.shopping_list_service.get_shopping_list(db, shopping_list_id)
    if db_list is None or db_list.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lista não encontrada ou acesso negado.")
    return services.shopping_list_service.update_shopping_list(db, db_list, update_data)

@router.delete("/{shopping_list_id}", status_code=status.HTTP_204_NO_CONTENT) # Define a rota para deletar uma lista de compras específica pelo ID
def delete_shopping_list( 
    shopping_list_id: int,
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_user) 
):
    """
    Exclui uma lista de compras, apenas se ela pertencer ao usuário.
    """
    db_list = services.shopping_list_service.get_shopping_list(db, shopping_list_id) # Busca a lista de compras pelo ID
    if db_list is None or db_list.owner_id != current_user.id: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lista não encontrada ou acesso negado.")
    services.shopping_list_service.delete_shopping_list(db, db_list) # Chama o serviço para deletar a lista de compras
