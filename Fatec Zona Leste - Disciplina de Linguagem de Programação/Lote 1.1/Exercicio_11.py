import os
import math
os.system('cls')

# Receba o raio de uma circunferência. Calcule e mostre o comprimento da circunferência.

raio = float(input("Informe o valor do raio: "))

circ = 2 * math.pi * raio

print(f"O valor da circunferência é {circ:.2f}")
