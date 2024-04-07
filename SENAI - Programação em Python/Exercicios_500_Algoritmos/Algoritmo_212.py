import os
import math

os.system('cls')
'''
    Entrar com 20 números e imprimir a soma dos números cujos quadrados
    são menores do que 225.
'''
res = 0

for i in range(20):
    num = int(input(f"Informe o {i+1}º número: "))
    quad = math.pow(num, 2)
    if quad < 225:
        res += num

print(f"\nSomatória é ---> {res}")

input("\n\nPressione o \"enter\" para encerrar...")
