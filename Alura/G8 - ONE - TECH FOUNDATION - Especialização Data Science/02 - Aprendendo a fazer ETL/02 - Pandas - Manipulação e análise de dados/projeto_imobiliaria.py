import pandas as pd
import matplotlib.pyplot as plt


arquivo = 'Alura/G8 - ONE - TECH FOUNDATION - Especialização Data Science/02 - Aprendendo a fazer ETL/02 - Pandas - Manipulação e análise de dados/base-dados/aluguel.csv'

dados = pd.read_csv(arquivo, sep=';')

print(dados)


# Ler algumas linhas
print('\n',dados.head())    # Retorna as 5 primeiras linhas, por default
print('\n',dados.head(10))  # Retorna as linhas conforme o parametro
print('\n',dados.tail())    # Retorna as 5 últimas linhas
print('\n', type(dados))    # Retorna o tipo de dado a ser tratado


print('\n', dados.shape)    # Retorna a quantidade de linhas x colunas

print('\n', dados.columns)  # Retorna os indices das colunas

print('\n', dados.info())   # Retorna as informações dos dados de cada coluna, se ele é int, float, string, object e até a quantidade de dados não nulos



'''
    A Series é uma estrutura de dados unidimensional que pode armazenar qualquer tipo de dados, rotulados com índices.
   
    O DataFrame é uma tabela de dados bidimensional, semelhante a uma planilha do Excel, com colunas rotuladas e linhas numeradas.
'''
print('\n', dados['Tipo'])  # Retorna uma 'series', com indice e o dado da coluna. Nesse caso o object informado são Strings

print('\n', dados[['Quartos', 'Valor']])  # Retorna um 'dataframe', com indice e os dados das colunas. Nesse caso podemos ver que são valores inteiros e float



# Quais os valores médios de aluguel por tipo de imóvel?
print(f"Média global: {(dados['Valor'].mean()):.2f}") # Retora a média global
print('\n',dados.groupby('Tipo').mean(numeric_only=True))    # Retorna a média por agrupamento por meio de um dataframe
print('\n',dados.groupby('Tipo')['Valor'].mean(numeric_only=True))    # Retorna a média por agrupamento por meio de um series, podendo ou não usar o numeric_only
print('\n',dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor'))    # Retorna a média por agrupamento por meio de um series, podendo ou não usar o numeric_only

df_preco_tipo = dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')

df_preco_tipo.plot(kind='barh', figsize=(14, 10), color='purple')
plt.show()

print('\n',dados.Tipo.unique)
imoveis_comerciais = ['Conjunto Comercial/Sala', 
                      'Prédio Inteiro', 'Loja/Salão', 
                      'Galpão/Depósito/Armazém', 
                      'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial',
                      'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio', 'Sítio',
                      'Pousada/Chalé', 'Hotel', 'Indústria']

df_dentro_conjunto = dados.query('@imoveis_comerciais in Tipo')   #Seleciona linhas com base em uma condição, o @ é uma notação usada para passar uma variavel no parametro da query

df_fora_conjunto = dados.query('@imoveis_comerciais not in Tipo')   # nega a condição e busca oq não faz parte da busca
print('\n', df_dentro_conjunto.head(100))       
print('\n', df_dentro_conjunto.Tipo.unique())

df = df_fora_conjunto.groupby('Tipo')[['Valor']].mean().sort_values('Valor')
df.plot(kind='barh', figsize=(14, 10), color='blue')
plt.show()

# Buscando por imóveis com suites
df_com_suites = dados.query('Suites >= 1')
df = df_com_suites.groupby('Tipo')[['Suites']].count().sort_values('Suites')
df.plot(kind='barh', figsize=(14, 10), color='blue')
plt.show()



# Qual o percentual de cada tipo de imóvel na nossa base de dados?
tipos_unicos = dados.Tipo.unique()
print('\nTipo de dados: ',tipos_unicos)

num_ocorrencias_tipo = dados.Tipo.value_counts()
print('\nQuantidade de dados por tipo: ', num_ocorrencias_tipo)

# Atribui a variavel sobre dados na coluna Tipo uma contagem do percentual, convertendo em dataframe e ordenando o coluna Tipo
percentual_ocorrencias_tipo = dados.Tipo.value_counts(normalize=True).to_frame().sort_values('Tipo')
percentual_ocorrencias_tipo = (dados.Tipo.value_counts(normalize=True)*100).to_frame().sort_values('Tipo') # para trazer o percentual cheio
print('\nPercentual de ocorrencias',percentual_ocorrencias_tipo)

percentual_ocorrencias_tipo.plot(kind='bar', figsize=(14, 10), color='green', xlabel='Tipo', ylabel='Percentual')
plt.show()


df_apartamento = dados.query('Tipo == "Apartamento"')
print('\nData Frame com os dados de apartamentos',df_apartamento.head())





# Verificando e Tratando valores núlos
print('\nDataframe com boolean',dados.isnull()) # Retorna um dataframe com True se houver um valor null, caso contrário False
print('\nSoma dos valores núlos', dados.isnull().sum())

df_tratado = dados.fillna(0)
print('\nSubstituição dos valores nulos', df_tratado ) # Retorna um dataframe com 0 onde houver valores nulos
print('\n',df_tratado.isnull().sum()) # confirmando se deu certo





# Removendo valores apartamentos que possuem valor de aluguel igual a 0
# Removendo valores apartamentos com o valor do condomínio igual a 0.
indices_remover = df_tratado.query('Valor == 0 or Condominio == 0').index
print('\nQuantidade de indices para remover', indices_remover)

# O parametro 0 serve para indicar a remoção das linhas, e 1 para colunas. inplace efetiva a alteração sem necessidade de uma nova atribuição para outra variavel
df_tratado.drop(indices_remover, axis=0, inplace=True) 
indices_remover = df_tratado.query('Valor == 0 or Condominio == 0').index
print('\nQuantidade de indices que restaram: ',indices_remover)

print('\n', df_tratado.drop('Vagas', axis=1)) # Removendo uma coluna sem efitivar a alteração





# Aplicando filtros - Apartamentos que possuem 1 quarto e aluguel menor que R$ 1200;
# Fazendo de outra forma sem o Query
selecao1 = df_tratado['Quartos'] == 1
print('\n',df_tratado[selecao1]) # O pandas retorna apenas os valores true

selecao2 = df_tratado['Valor'] < 1200
print('\n', df_tratado[selecao2])

selecao_final = (selecao1) & (selecao2) # Junta as duas seleções & -> and
print('\n', df_tratado[selecao_final])


# Aplicando filtros - Apartamentos que possuem pelo menos 2 quartos, aluguel menor que R$ 3000 e área maior que 70 m².
selecao = (df_tratado['Quartos'] >= 2) & (df_tratado['Valor'] < 3000) & (df_tratado['Area'] > 70)
print('\n', df_tratado[selecao])
