import os

os.system('cls')
# Ler um número inteiro de 3 casas decimais e imprimir se o algarismo da casa das centenas é par ou ímpar.

num = int(input("Informe um número a partir de 100: "))

cent = num // 100

if cent % 2 == 0:
    print("\nA Centena do número informado é \"Par\".")
else: 
    print("\nA Centena do número informado é \"Impar\".")


input("\n\nPressione o \"enter\" para encerrar...")

