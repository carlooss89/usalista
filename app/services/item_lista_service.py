from sqlalchemy.orm import Session # Importa a sessão do SQLAlchemy para interagir com o banco de dados
from app.models.item_lista import ItemLista # Importa o modelo ItemLista, que representa a tabela de itens de lista no banco de dados
from app.schemas.item_lista import ItemListaCreate # Importa o esquema ItemListaCreate, que define os dados necessários para criar um novo item de lista
from datetime import datetime # Importa a classe datetime para manipular datas e horas

def criar_item(db: Session, item_data: ItemListaCreate, dono_id: int): # Função para criar um novo item de lista
    novo_item = ItemLista( # Cria uma nova instância de ItemLista com os dados fornecidos   
        nome=item_data.nome, 
        quantidade=item_data.quantidade, 
        comprado=item_data.comprado,
        data_criacao=datetime.utcnow(),
        dono_id=dono_id,
        shopping_list_id=item_data.shopping_list_id # shopping_list_id é opcional, pode ser None se não for especificado
    )
    db.add(novo_item) 
    db.commit() 
    db.refresh(novo_item) 
    return novo_item 

def listar_itens_do_usuario(db: Session, user_id: int): # Função para listar todos os itens de lista pertencentes a um usuário específico
    return db.query(ItemLista).filter(ItemLista.dono_id == user_id).all() # Função que retorna todos os itens de lista do usuário com o ID especificado

def obter_item_por_id(db: Session, item_id: int, user_id: int): # Função para obter um item de lista específico pelo ID, garantindo que pertence ao usuário
    return db.query(ItemLista).filter(ItemLista.id == item_id, ItemLista.dono_id == user_id).first() # Retorna o primeiro item que corresponde ao ID e ao dono especificados, ou None se não encontrar
# Isso garante que o usuário só possa acessar seus próprios itens de lista.

def atualizar_item(db: Session, item: ItemLista, item_data: ItemListaCreate): # Função para atualizar um item de lista existente
    item.nome = item_data.nome 
    item.quantidade = item_data.quantidade 
    item.comprado = item_data.comprado 
    db.commit()
    db.refresh(item)
    return item

def deletar_item(db: Session, item: ItemLista): # Função para deletar um item de lista existente
    db.delete(item)
    db.commit() # Retorna None após deletar o item
