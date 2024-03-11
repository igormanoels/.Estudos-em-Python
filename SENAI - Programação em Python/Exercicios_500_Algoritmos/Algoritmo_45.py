import os
import math

os.system('cls')
# Entrar com um número e imprimir a seguinte saída: numero, quadrado. raiz quadrada.

num = int(input("Informe um número para os cálculos: "))
raizQd = math.sqrt(num)
potencia = math.pow(num, 2)

print("Raiz Quadrada: ", raizQd, "\tPotência²: ", potencia)
