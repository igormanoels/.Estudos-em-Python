import os

os.system('cls')
# Entrarcom dois números e imprimir o maiornúmero (suponha números diferentes).

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

if num1 == num2: 
    print("Os números são iguais.")
else:
    if (num1 > num2):
        print(f"\nO número {num1} é o maior.")
    else: 
        print(f"\nO número {num2} é o maior.")

input("\n\nPressione o \"enter\" para encerrar...")
