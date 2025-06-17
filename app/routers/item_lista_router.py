from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session # 

from app.db.database import get_db # Importa a sessão do SQLAlchemy para interagir com o banco de dados
from app.schemas.item_lista import ItemListaCreate, ItemListaOut # Importa os esquemas ItemListaCreate e ItemListaOut, que definem os dados necessários para criar e retornar itens de lista
from app.services import item_lista_service # Importa o serviço de itens de lista, que contém a lógica de negócios para manipular itens de lista
from app.dependencies import get_current_user # Importa a função para obter o usuário atual, que valida o token JWT e retorna o usuário autenticado
from app.models import User, ItemLista # Importa os modelos User e ItemLista, que representam as tabelas de usuários e itens de lista no banco de dados

router = APIRouter(tags=["Itens da Lista"]) # Cria um roteador FastAPI para agrupar as rotas relacionadas aos itens da lista

@router.post("/items/", response_model=ItemListaOut, status_code=status.HTTP_201_CREATED) # Define a rota para criar um novo item de lista 

def criar_item_lista( # Função para criar um novo item de lista
    item_data: ItemListaCreate, # Dados do item a ser criado, conforme definido no esquema ItemListaCreate
    db: Session = Depends(get_db), # Dependência para obter a sessão do banco de dados
    current_user: User = Depends(get_current_user) # Dependência para obter o usuário atual, que valida o token JWT
):
    """
    Cria um novo item na lista do usuário logado.
    Requer token JWT.
    """
    return item_lista_service.criar_item(db, item_data, current_user.id) # Chama o serviço para criar o item de lista, passando a sessão do banco de dados, os dados do item e o ID do usuário atual

@router.get("/items/", response_model=list[ItemListaOut]) # Define a rota para listar todos os itens do usuário
def listar_itens_usuario( # Função para listar todos os itens de lista do usuário autenticado
    db: Session = Depends(get_db), # Dependência para obter a sessão do banco de dados
    current_user: User = Depends(get_current_user) # Dependência para obter o usuário atual, que valida o token JWT
):
    """
    Lista todos os itens do usuário autenticado.
    Requer token JWT.
    """
    return item_lista_service.listar_itens_do_usuario(db, current_user.id) # Chama o serviço para listar os itens do usuário, passando a sessão do banco de dados e o ID do usuário atual

@router.get("/items/{item_id}", response_model=ItemListaOut) # Define a rota para obter os detalhes de um item específico do usuário
def obter_item( # Função para obter os detalhes de um item de lista específico do usuário
    item_id: int, # ID do item a ser obtido
    db: Session = Depends(get_db), # Dependência para obter a sessão do banco de dados
    current_user: User = Depends(get_current_user) # Dependência para obter o usuário atual, que valida o token JWT
):
    """
    Retorna os detalhes de um item específico do usuário.
    Requer token JWT.
    """
    item = item_lista_service.obter_item_por_id(db, item_id, current_user.id) # Chama o serviço para obter o item de lista pelo ID, garantindo que pertence ao usuário atual
    if not item: 
        raise HTTPException(status_code=404, detail="Item não encontrado") # Se o item não for encontrado, lança uma exceção HTTP 404
    return item

@router.put("/items/{item_id}", response_model=ItemListaOut) # Define a rota para atualizar um item específico do usuário
def atualizar_item( # Função para atualizar um item de lista específico do usuário
    item_id: int, 
    item_data: ItemListaCreate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user) 
):
    """
    Atualiza os dados de um item específico do usuário.
    Requer token JWT.
    """
    item = item_lista_service.obter_item_por_id(db, item_id, current_user.id) 
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado") 
    return item_lista_service.atualizar_item(db, item, item_data) # Chama o serviço para atualizar o item de lista, passando a sessão do banco de dados, o item existente e os novos dados do item

@router.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT) # Define a rota para deletar um item específico do usuário
def deletar_item( # Função para deletar um item de lista específico do usuário
    item_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Deleta um item específico da lista do usuário.
    Requer token JWT.
    """
    item = item_lista_service.obter_item_por_id(db, item_id, current_user.id) # Obtém o item de lista pelo ID, garantindo que pertence ao usuário atual
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado") # Se o item não for encontrado, lança uma exceção HTTP 404
    item_lista_service.deletar_item(db, item) # Chama o serviço para deletar o item de lista, passando a sessão do banco de dados e o item a ser deletado
    return {"detail": "Item deletado com sucesso"} # Retorna uma resposta de sucesso, indicando que o item foi deletado 
