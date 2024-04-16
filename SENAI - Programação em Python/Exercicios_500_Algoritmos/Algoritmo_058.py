import math
import os

os.system('cls')
# rar com valores para xnum 1, xnum2 e xnum3 e imprimir o valor de x segundo a função:

n1 = int(input("Favor informar o primeiro termo: "))
n2 = int(input("Favor informar o segundo termo: "))
n3 = int(input("Favor informar o terceiro termo: "))

resFunc = n1 + (n2 / (n1 + n3)) + (2 * (n1 - n2)) + (math.log(64, 2))
print("Resultado da Função: ", resFunc)

input("\n\nPressione o \"enter\" para encerrar...")
