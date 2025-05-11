import pandas as pd 

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



