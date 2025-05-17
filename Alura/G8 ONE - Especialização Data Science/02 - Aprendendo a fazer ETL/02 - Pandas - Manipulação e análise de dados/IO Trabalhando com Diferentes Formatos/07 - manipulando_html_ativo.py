import pandas

# Todas as tabelas
link = pandas.read_html('https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_popula%C3%A7%C3%A3o')
print('\n', link)


# Apenas a primeira tabela
link2 = pandas.read_html('https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_popula%C3%A7%C3%A3o')[0]
print('\n', link2)
