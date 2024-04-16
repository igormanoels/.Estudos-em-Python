import os

os.system('cls')
# Criar um algoritmo que calcule e imprima a área de um losango.

diagMaior = int(input("Favor informar o valor da \"Maior Diagonal\": "))
diagMenor = int(input("Favor informar o valor da \"Menor Diagonal\": "))

areaLos = ((diagMenor * diagMaior) / 2)
print("O valor da área do losango é ", areaLos)

input("\n\nPressione o \"enter\" para encerrar...")
