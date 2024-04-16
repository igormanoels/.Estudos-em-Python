import os
import math

os.system('cls')
'''
    Entrar com um número e imprimir a raiz quadrada do número caso ele seja positivo 
    e o quadrado do número caso ele seja negativo.
'''

num = int(input("Digite um número: "))

if (num == 0):
    print("\nNúmero informado inválido. ")
elif (num > 0):
    res = round(math.sqrt(num), 2)
    print(f"\nA raiz quadrada de {num} é {res}.")
else:
    res = math.pow(num, 2)
    print(f"\nO quadrado de {num} é {res}.")

input("\n\nPressione o \"enter\" para encerrar...")
