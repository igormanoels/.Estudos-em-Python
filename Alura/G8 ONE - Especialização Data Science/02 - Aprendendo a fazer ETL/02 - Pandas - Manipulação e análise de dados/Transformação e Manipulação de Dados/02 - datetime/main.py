import pandas as pd
import numpy as np


# Tratando os dados com datetime
moveis = pd.read_json('Alura/G8 ONE - Especialização Data Science/02 - Aprendendo a fazer ETL/02 - Pandas - Manipulação e análise de dados/Transformação e Manipulação de Dados/02 - datetime/dados/moveis_disponiveis.json')
print('\n', moveis.head())

# Verificando o que precisa ser feito
print('\n\n', moveis.info())



# Tratando os dados para datetime
moveis['data'] = pd.to_datetime(moveis['data'])
print('\n\n', moveis)

print('\n\n', moveis.info()) # verificando se deu certo


# Analisando a situação atual
print('\n', moveis.head(10))


# Formatando o tempo da data
print('\n', moveis['data'].dt.strftime('%Y-%m'))

# Agrupando as datas por mes
vagas_disponiveis = moveis.groupby(moveis['data'].dt.strftime('%Y-%m'))['vaga_disponivel'].sum()
print('\n', vagas_disponiveis)



# utilizamos o método fillna para preencher os elementos vazios por '0.0'
# definimos o parâmetro de inplace para True para substituir no DataFrame
moveis['preco'] = moveis['preco'].fillna('0.0', inplace = True)

moveis['preco'] = moveis['preco'].apply(lambda x: x.replace('$', '').replace(',','')) # apagamos o $ e as vírgulas com apply lambda

moveis['preco'] = moveis['preco'].astype(np.float64) # transformamos os tipos de dados para float64

print('\n', moveis.head(10)) # observamos o resultado final