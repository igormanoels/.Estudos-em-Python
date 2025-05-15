import pandas as pd

# Realizando a leitura de arquivos com separadores diferentes para arquivos CSV(Comma Separated Values)
arquivo = 'D:/GitHub/.Estudos-em-Python/Alura/G8 - ONE - TECH FOUNDATION - Especialização Data Science/02 - Aprendendo a fazer ETL/02 - Pandas - Manipulação e análise de dados/IO Trabalhando com Diferentes Formatos de Arquivos/dados/emissoes_CO2.xlsx'
dados = pd.read_excel(arquivo)
print(dados.head(10))


# Buscando as abas do arquivo
print('\nNome das páginas do arquivo: ', pd.ExcelFile(arquivo).sheet_names)


# Realizando a leitura especificando a busca por página desejada
percapita = pd.read_excel(arquivo, sheet_name='emissoes_percapita')
print('\nBuscando pela página percapita\n',percapita.head(10))

fontes = pd.read_excel(arquivo, sheet_name='fontes')
print('\nBuscando pela página fontes\n',fontes.head(10))

intervalo = pd.read_excel(arquivo, sheet_name='emissoes_C02', usecols='A:D')
print('\nIntervalo de colunas\n',intervalo.head(10))

intervalo2 = pd.read_excel(arquivo, sheet_name='emissoes_C02', usecols='A:D', nrows=10)
print('\nIntervalo de colunas e linhas\n',intervalo2)


# Salvando o dataframe em XLSX (planilhas)
percapita.to_excel('Alura/G8 - ONE - TECH FOUNDATION - Especialização Data Science/02 - Aprendendo a fazer ETL/02 - Pandas - Manipulação e análise de dados/IO Trabalhando com Diferentes Formatos de Arquivos/CO2_percapita.xlsx', index=False)






