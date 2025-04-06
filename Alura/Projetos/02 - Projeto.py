'''
11) Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo. 
O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, 
se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:

Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes.
'''

lado1 = float(input('Informe o valor do primeiro lado do triangulo: '))
lado2 = float(input('Informe o valor do segundo lado do triangulo: '))
lado3 = float(input('Informe o valor do terceiro lado do triangulo: '))


if lado1 == lado2 and lado2 == lado3:
    print('O triangulo é equilátero')
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print('O triangulo é isóceles')
else:
    print('O triangulo é escaleno')

