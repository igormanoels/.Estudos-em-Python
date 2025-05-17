from sqlalchemy import text
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:')

query = 'DELETE FROM clientes WHERE ID_Cliente=5008804'
with engine.connect() as conn:
    result = conn.execute(text(query))
    conn.commit()  

'''
Vamos quebrar o código em partes para entender melhor cada etapa:

1. Definição da consulta SQL: Primeiro, definimos o que queremos fazer com o banco de dados em uma string de consulta SQL, armazenada 
na variável query. Aqui, o comando DELETE é usado para remover o registro de um cliente específico, identificado pelo ID_Cliente=5008804.

2. Estabelecendo conexão com o banco de dados: Usamos with engine.connect() as conn para abrir uma conexão com o banco. O with é muito 
útil porque gerencia automaticamente a abertura e o fechamento da conexão. Isso significa que, após o bloco de código ser executado, a 
conexão será fechada automaticamente, evitando que recursos sejam desperdiçados ou bloqueios no banco de dados se prolonguem.

3. Executando a consulta: Dentro do bloco with, executamos a consulta com conn.execute(text(query)). A função text() é usada aqui para 
garantir que a string de consulta seja interpretada como SQL puro.

4. Confirmar a transação: Por fim, chamamos conn.commit() para confirmar a transação. Isso é crucial porque, em muitos bancos de dados, 
as alterações feitas (como deletar um registro) não são salvas permanentemente até que sejam confirmadas explicitamente.

'''

query = 'UPDATE clientes SET Grau_escolaridade="Ensino superior" WHERE ID_Cliente=5008808'
with engine.connect() as conn:
    result = conn.execute(text(query))
    conn.commit()  