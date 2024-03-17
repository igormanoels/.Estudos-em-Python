import os

os.system('cls')
# Entrar com três nu" meros e armazenar o maior numero na variavel de nome maior(suponha números diferentes) 

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))

if num1 > num2:
    if num1 > num3:
        max = num1
    else: 
        max = num3
else:
    if num2 > num3:
        max = num2
    else:
        max = num3

print(f"\n{max} é o maior número.")

input("\n\nPressione o \"enter\" para encerrar...")
