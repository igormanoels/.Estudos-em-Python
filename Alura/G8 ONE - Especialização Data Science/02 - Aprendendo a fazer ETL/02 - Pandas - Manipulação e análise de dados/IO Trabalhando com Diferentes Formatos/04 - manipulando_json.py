import pandas as pd

# Manipulando um arquivo JSON (JavaScript Object Notation)

arquivo = 'D:/GitHub/.Estudos-em-Python/Alura/G8 - ONE - TECH FOUNDATION - Especialização Data Science/02 - Aprendendo a fazer ETL/02 - Pandas - Manipulação e análise de dados/IO Trabalhando com Diferentes Formatos de Arquivos/dados/pacientes.json'
dados = pd.read_json(arquivo)
print('\n',dados)


# Json com dados aninhados
arquivo2 = 'D:/GitHub/.Estudos-em-Python/Alura/G8 - ONE - TECH FOUNDATION - Especialização Data Science/02 - Aprendendo a fazer ETL/02 - Pandas - Manipulação e análise de dados/IO Trabalhando com Diferentes Formatos de Arquivos/dados/pacientes_2.json'
dados2 = pd.read_json(arquivo2)
print('\n',dados2)


# Normalizando os dados aninhados
df_normalizado = pd.json_normalize(dados2['Pacientes'])
print('\n',df_normalizado)


# Salvando o arquivo
df_normalizado.to_json('historico_normalizado.json')

