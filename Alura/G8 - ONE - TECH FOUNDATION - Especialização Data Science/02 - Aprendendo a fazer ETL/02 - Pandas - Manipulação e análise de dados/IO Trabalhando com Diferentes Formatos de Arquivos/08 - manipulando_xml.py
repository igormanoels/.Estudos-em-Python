import pandas as pd

# Manipulando XML (Extensible Markup Language)

arquivo = 'D:/GitHub/.Estudos-em-Python/Alura/G8 - ONE - TECH FOUNDATION - Especialização Data Science/02 - Aprendendo a fazer ETL/02 - Pandas - Manipulação e análise de dados/IO Trabalhando com Diferentes Formatos de Arquivos/dados/imdb_top_1000.xml'
df = pd.read_xml(arquivo)
print('\n', df)


# Lendo 10 linhas
print('\n', df.head(10))


# Escrevendo em xlm
df.to_xml('filmes_imdb.xml')