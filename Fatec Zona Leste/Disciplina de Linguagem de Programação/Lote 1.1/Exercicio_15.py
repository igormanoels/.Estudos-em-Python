import os
import math
os.system('cls')

# Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre a hipotenusa.

valorA = float(input("Informe o valor do primeiro cateto: "))
valorB = float(input("Informe o valor do segundo cateto: "))

hipotenusa = math.sqrt((math.pow(valorA, 2) + (math.pow(valorB, 2))))

print(f"O valor da hipotenuso é {hipotenusa:.2f}")
