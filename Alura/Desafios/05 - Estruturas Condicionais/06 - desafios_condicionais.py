# 6) Escreva um programa que leia três números e os exiba em ordem decrescente.
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))

lista = num1, num2, num3

print(f'Lista ordenada: {sorted(lista)}')

