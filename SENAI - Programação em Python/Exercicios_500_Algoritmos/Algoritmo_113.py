import os

os.system('cls')
# Entrar com dois números e imprimi-los em ordem crescente (suponha números diferentes).

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

if num1 == num2: 
    print("Os números são iguais.")
else:
    if (num1 < num2):
        print(f"\nEm ordem crescente: {num1}, {num2}.")
    else: 
        print(f"\nEm ordem crescente: {num2}, {num1}.")

input("\n\nPressione o \"enter\" para encerrar...")
