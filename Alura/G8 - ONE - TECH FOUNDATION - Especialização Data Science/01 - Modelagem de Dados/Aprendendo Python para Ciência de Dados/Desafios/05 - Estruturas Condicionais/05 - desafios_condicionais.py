# 5) Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.
produto1 = float(input('Informe o primeiro valor do produto: '))
produto2 = float(input('Informe o segundo valor do produto: '))
produto3 = float(input('Informe o terceiro valor do produto: '))

lista = produto1, produto2, produto3

print(f'O menor valor é {min(lista)}')

