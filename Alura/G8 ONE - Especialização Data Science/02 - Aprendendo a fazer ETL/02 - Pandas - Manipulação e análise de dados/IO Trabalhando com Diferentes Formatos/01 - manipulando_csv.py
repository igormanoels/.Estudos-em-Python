import pandas as pd

# Realizando a leitura de arquivos com separadores diferentes para arquivos CSV(Comma Separated Values)
arquivo = 'D:/GitHub/.Estudos-em-Python/Alura/G8 - ONE - TECH FOUNDATION - Especialização Data Science/02 - Aprendendo a fazer ETL/02 - Pandas - Manipulação e análise de dados/IO Trabalhando com Diferentes Formatos de Arquivos/dados/superstore_data.csv'
dados_mercado = pd.read_csv(arquivo) # lendo sep default
print('\n',dados_mercado.head(5))

arquivo_ponto_virgula = 'D:/GitHub/.Estudos-em-Python/Alura/G8 - ONE - TECH FOUNDATION - Especialização Data Science/02 - Aprendendo a fazer ETL/02 - Pandas - Manipulação e análise de dados/IO Trabalhando com Diferentes Formatos de Arquivos/dados/superstore_data_ponto_virgula.csv'
dados_mercado_ponto_virgula = pd.read_csv(arquivo_ponto_virgula, sep=';') # lendo sep ';'
print(dados_mercado_ponto_virgula.head(5))


# Lendo do arquivo apenas N linhas desejadas
linhas_desejadas = pd.read_csv(arquivo, nrows=10)
print(linhas_desejadas)


# Lendo do arquivo apenas colunas desejadas
dados_selecao = pd.read_csv(arquivo, usecols=['Id', 'Year_Birth', 'Income'])
print('\nSeleção de dados:',dados_selecao)

dados_selecao = pd.read_csv(arquivo, usecols=[0,1,4])
print('\nSeleção de dados:',dados_selecao)


# Salvando um arquivo em CSV
dados_selecao.to_csv('Alura/G8 - ONE - TECH FOUNDATION - Especialização Data Science/02 - Aprendendo a fazer ETL/02 - Pandas - Manipulação e análise de dados/IO Trabalhando com Diferentes Formatos de Arquivos/clientes_mercado.csv', sep=',', index=False)
