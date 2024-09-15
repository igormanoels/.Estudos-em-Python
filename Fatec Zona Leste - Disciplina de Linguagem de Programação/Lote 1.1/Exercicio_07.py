import os
os.system('cls')

# Receba os valores do comprimento, largura e altura de um paralelepípedo. Calcule e mostre seu volume.

valorA = int(input("Informe o valor do comprimento"))
valorB = int(input("Informe o valor da largura"))
valorC = int(input("Informe o valor da altura"))

res = 2 * (valorA * valorB + valorB * valorC + valorA * valorC)
print("Área do paralelepipedo: ", res)