import os

os.system('cls')
# Construir um algoritmo que leia dois valores numéricos inteiros e efetue a adição; 
# caso o resultado seja maior que 10, apresentá-lo.

num1 = input("Informe o primeiro número: ")
num2 = input("Informe o segundo número: ")

res = num1+num2

if (res >= 10):
    print(f"A soma dos números {num1} e {num2} é {res}.")
else:
    print("A soma é menor que 10.")

input("\n\nPressione o \"enter\" para encerrar...")
