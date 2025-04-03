import os
import math
os.system('cls')

# Receba os 2 números inteiros. Calcule e mostre a soma dos quadrados.

valorA = int(input("Informe o primeiro valor: "))
valorB = int(input("Informe o segundo valor: "))

res = (math.pow(valorA, 2)) + (math.pow(valorB, 2))
print("A soma dos quadrados é ", res)
