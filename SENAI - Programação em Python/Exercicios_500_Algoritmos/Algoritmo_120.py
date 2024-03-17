import os

os.system('cls')
# Entrar com três números e armazená-los em três variáveis com os seguintes nomes maior, intermediário e menor (suponha numeros diferentes) 

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))

maior = max(num1, num2, num3)
menor = min(num1, num2, num3)

if num1 != maior and num1 != menor:
    media = num1
elif num2 != maior and num2 != menor:
    media = num2
elif num3 != maior and num3 != menor:
    media = num3
    
print(f"\nMaior: {maior}\nMenor:{menor}\nIntermediário: {media}")

input("\n\nPressione o \"enter\" para encerrar...")
