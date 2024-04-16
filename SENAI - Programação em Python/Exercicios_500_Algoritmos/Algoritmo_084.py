import os

os.system('cls')
# Ler um número e imprimir se ele é par ou ímpar.

num = int(input("Informe um número: "))

if num % 2 == 0:
    print(f"\nO número {num} é par")
else:
    print(f"\nO número {num} é impar")

input("\n\nPressione o \"enter\" para encerrar...")
