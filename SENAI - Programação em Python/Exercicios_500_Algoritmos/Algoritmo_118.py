import os

os.system('cls')
# Entrar com três números e imprimi-los em ordem crescente (suponha números diferentes). 

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))

if num1 <= num2 and num2 <= num3:
    print(f"\nSequência: {num1}, {num2} e {num3}.")
elif num1 <= num3 and num3 <= num2:
    print(f"\nSequência: {num1}, {num3} e {num2}.")
elif num2 <= num1 and num1 <= num3:
    print(f"\nSequência: {num2}, {num1} e {num3}.")
elif num2 <= num3 and num3 <= num1:
    print(f"\nSequência: {num2}, {num3} e {num1}.")
elif num3 <= num1 and num1 <= num2:
    print(f"\nSequência: {num3}, {num1} e {num2}.")
else:
    print(f"\nSequência: {num3}, {num2} e {num1}.")

input("\n\nPressione o \"enter\" para encerrar...")
