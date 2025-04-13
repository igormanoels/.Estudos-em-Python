'''
10. Faça um programa para uma loja que vende grama para jardins. 

Essa loja trabalha com jardins circulares e o preço do metro quadrado da grama é de R$ 25,00. 

Peça à pessoa usuária o raio da área circular e devolva o valor em reais do quanto precisará pagar.
'''
from math import pi, pow

valor_metro = 25.00

raio_circular = float(input('Informe o raio da área circular: '))

area = round((pi * pow(raio_circular, 2)), 2)


print(f'Orçamento final R${area*valor_metro}')


