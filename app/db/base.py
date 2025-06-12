from sqlalchemy.orm import declarative_base # Importa a função declarative_base do SQLAlchemy, que é usada para criar a classe base para os modelos do banco de dados.

Base = declarative_base() # Cria a classe base para todos os modelos do banco de dados. Todos os modelos (tabelas) do projeto vão herdar dessa classe Base para se tornarem tabelas no banco.
