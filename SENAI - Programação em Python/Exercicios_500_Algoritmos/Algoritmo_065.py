import os
import math

os.system('cls')
# Cálcular e apresentar o valor do volume de uma lata de óleo, utilizando a fórmula: volume = 3.14159 * R^2 * altura.

raio = float(input("Favor informar o valor do raio: "))
altura = float(input("Favor informar o valor do volume: "))

volume = round((math.pi * math.pow(raio,2) * altura), 2)

print("Volume = ", volume)

input("\n\nPressione o \"enter\" para encerrar...")
