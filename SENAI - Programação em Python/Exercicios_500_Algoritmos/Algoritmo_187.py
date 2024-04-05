import os
import math

os.system('cls')
'''
    Criar um algoritmo que calcule e imprima o valor de b elevado a n. 
    O valor de n deverá ser maior do que 1 e inteiro e o valor de b maior
    ou igual a 2 e inteiro.
'''

while True:
    base = int(input("Informe a base de para cálculo: "))
    if base >= 2:
        break
    else:
        print("Número inválido, ele precisa ser maior/ igual a 2.\n")

while True:
    n = int(input("Agora informe o valor do expoente: "))
    if n > 1:
        break
    else:
        print("Número inválido, ele precisa ser maior que 1.\n")

quad = math.pow(base, n)
print(f"\n{base} elevado a {n} é ---> {quad}.")

input("\n\nPressione o \"enter\" para encerrar...")
