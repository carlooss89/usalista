# init_db.py

from app.db.database import Base, engine # Importa a classe Base e o engine do banco de dados para inicialização
from app.models import user, shopping_list, item_lista # Importa os modelos do banco de dados, como User, ShoppingList e ItemLista. Isso é necessário para que o SQLAlchemy reconheça essas tabelas quando criarmos o banco de dados.


print("🔄 Criando tabelas no banco...") 
Base.metadata.create_all(bind=engine) # Cria todas as tabelas definidas nos modelos que herdam de Base, como User, ShoppingList e ItemLista.
print("✅ Tabelas criadas com sucesso.")
