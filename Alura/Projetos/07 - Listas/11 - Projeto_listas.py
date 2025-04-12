'''
11) Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos. 
Os dados das vendas foram armazenados em um dicionário:

Escreva um código que calcule o total de vendas e o produto mais vendido.
'''

produtos = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60, 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}

mais_vendido = 0
nome_produto = ''
total_vendas = 0

for chave, valor in produtos.items():
    total_vendas += valor

    if valor > mais_vendido:
        mais_vendido = valor
        nome_produto = chave


print(f'Produto mais vendito: {nome_produto}, quantidade de vendas: {mais_vendido}\nTotal de vendas: {total_vendas}')

