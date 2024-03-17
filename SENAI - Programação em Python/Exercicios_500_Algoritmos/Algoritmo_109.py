import os

os.system('cls')
# Criar um algoritmo que entre com dois nomes e imprimi-los em ordem alfabética.

nome1 = input("Informe o primeiro número: ")
nome2 = input("Informe o segundo número: ")

if nome1[0] < nome2[0]:
    print(f"{nome1}, {nome2}.")
else:
    print(f"{nome2}, {nome1}.")
    
input("\n\nPressione o \"enter\" para encerrar...")
