import os

os.system('cls')
# Entrar com dois números e imprimir o menor numero (suponha números diferentes).

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

if num1 == num2: 
    print("Os números são iguais.")
else:
    if (num1 < num2):
        print(f"\nO número {num1} é o menor.")
    else: 
        print(f"\nO número {num2} é o menor.")

input("\n\nPressione o \"enter\" para encerrar...")
