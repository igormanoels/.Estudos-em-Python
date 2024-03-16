import os

os.system('cls')
# Ler um número e imprimir se ele é positivo, negativo ou nulo.

num = int(input("Informe um número: "))

if num == 0:
    print("\nNULO!")
else:
    if num > 0:
        print("\nPOSITIVO!")
    else:
        print("\nNEGATIVO")

input("\n\nPressione o \"enter\" para encerrar...")
