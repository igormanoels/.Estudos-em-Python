import pandas as pd
from sqlalchemy import create_engine, inspect, text # Para criar o motor, não foi usado -->'MetaData, Table'


# Manipulando SQL (Structured Query Language)

# Criando o bando em memoria
engine = create_engine('sqlite:///:memory:')


dados = pd.read_csv('D:/GitHub/.Estudos-em-Python/Alura/G8 - ONE - TECH FOUNDATION - Especialização Data Science/02 - Aprendendo a fazer ETL/02 - Pandas - Manipulação e análise de dados/IO Trabalhando com Diferentes Formatos de Arquivos/dados/clientes_banco.csv')

print('\n',dados.head(5))

# Criando o banco de dados a partir do csv
dados.to_sql('Clientes', engine, index=False)


# Verificando o bando de dados
inspector = inspect(engine)
print('\n', inspector.get_table_names()) # Retorna as tabelas do banco de dados


# Criando uma consulta
query = 'SELECT * FROM Clientes WHERE Categoria_de_renda = "Empregado"'
empregados = pd.read_sql(query, engine) # Faz a leitura de uma consulta
print('\n', empregados)


empregados.to_sql('Empregados', con=engine, index=False) # Criando uma nova tabela
print('\n', pd.read_sql_table('Empregados', engine)) # Faz a leitura da tabela completa

print('\n', pd.read_sql_table('Empregados', engine, columns=['ID_Cliente','Grau_escolaridade', 'Rendimento_anual'])) # consulta personalizada


# Crinado QUERY
query_todos = 'SELECT * FROM Clientes'
clientes = pd.read_sql(query_todos, engine) # Faz a leitura de uma consulta


# Deletando Dados
query_deletando = 'DELETE FROM Clientes WHERE ID_Cliente=5008804'
# Cria um método que estabelece uma conexão com o banco de dados e ao final encerra a transação
with engine.connect() as conn:
    resposta = conn.execute(text(query_deletando))
    print('\n','Retorno ao deletar: ', resposta.rowcount)

clientes = pd.read_sql_table('Clientes', engine) # Consultando para verificar se deu certo


# Atualizando Dados
query_atualizando = ''' UPDATE Clientes 
                        SET Grau_escolaridade="Ensino superior" 
                        WHERE ID_Cliente=5008808'''
with engine.connect() as conn:
    resposta = conn.execute(text(query_atualizando))
    print('\n','Retorno ao atualizar: ', resposta.rowcount)

clientes = pd.read_sql_table('Clientes', engine) # Consultando para verificar se deu certo


'''
Query       	Retorno útil em CursorResult
SELECT	        .fetchall(), .fetchone()
INSERT	        .lastrowid, .rowcount
UPDATE/DELETE	.rowcount
'''