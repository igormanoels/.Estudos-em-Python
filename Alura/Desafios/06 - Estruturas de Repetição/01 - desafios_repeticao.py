# 1) Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num1 +=1
for cont in range(num1, num2):
    print(cont, end=' ')



