'''
5. Crie um programa que solicite à pessoa usuária digitar dois números inteiros e calcular a potência do 1º número elevado ao 2º.

Dica: use a função pow() da biblioteca math
'''

from math import pow

base = int(input('Informe o valor da base: '))
expoente = int(input('Informe o valor do expoente: '))

res = pow(base, expoente)
print(f'O resultado é {res:.2f}')

