import pandas as pd


arquivo = 'D:/GitHub/.Estudos-em-Python/Alura/G8 - ONE - TECH FOUNDATION - Especialização Data Science/02 - Aprendendo a fazer ETL/02 - Pandas - Manipulação e análise de dados/IO Trabalhando com Diferentes Formatos de Arquivos/dados/filmes_wikipedia.html'
html = pd.read_html(arquivo)
print(html)


# Verificando o tipo
print('\n', type(html))


# Verificando o tamanho
print('\n', len(html))


# Colocando uma tabela em outro variavel para separar o conteúdo
top_filmes = html[1]
print('\n', top_filmes)


# Salvando em html
top_filmes.to_html('top_filmes.html')
