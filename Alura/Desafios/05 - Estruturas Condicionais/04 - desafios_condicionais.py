'''
4) Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba
o valor mais alto e mais baixo entre esses três anos.
'''
preco1 = float(input('Informe o primeiro valor do carro: '))
preco2 = float(input('Informe o segundo valor do carro: '))
preco3 = float(input('Informe o terceiro valor do carro: '))

lista = preco1, preco2, preco3
menor_valor = min(lista)
maior_valor = max(lista)

print(f'O menor valor é {menor_valor} e o maior valor é {maior_valor}')

