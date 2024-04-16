import os
import math

os.system('cls')
# Entrar com os lados a, b, c de um paralelepípedo. Calcular e imprimir a diagonal.

ladoA = float(input("Informe o valor do lado A: "))
ladoB = float(input("Informe o valor do lado B: "))
ladoC = float(input("Informe o valor do lado C: "))

diagonal = math.sqrt((math.pow(ladoA, 2) + math.pow(ladoB, 2) + math.pow(ladoC, 2)))

print("O valor da Diagonal do paralelepípedo é ", diagonal)

input("\n\nPressione o enter para encerrar...")
