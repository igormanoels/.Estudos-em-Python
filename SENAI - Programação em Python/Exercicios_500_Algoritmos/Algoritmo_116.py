import os

os.system('cls')
# Entrar com três números e imprimir o maior número (suponha números diferentes).

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))

if num1 == num2 and num1 == num3 and num2 == num3:
    print("Os informados são iguais.")
else: 
    maior = max(num1, num2, num3)
    print(f"\n{maior} é o maior número.")
    
input("\n\nPressione o \"enter\" para encerrar...")
