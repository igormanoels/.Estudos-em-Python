import os
import math

os.system('cls')
#   Criar o algoritmo que deixe entrar com dois números e imprimir o quadrado do menor número 
#   e a raiz quadrada do maior número, se for possível.


num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

if num1 == num2: 
    print("Os números são iguais.")
else:
    if (num1 < num2):
        menor = math.pow(num1, 2)
        maior = math.sqrt(num2)
        print(f"\nQuadrado do menor número: {menor}\nRaiz Quadrada do maior número: {maior}.")
    else: 
        menor = math.pow(num2, 2)
        maior = math.sqrt(num1)
        print(f"\nQuadrado do menor número: {menor}\nRaiz Quadrada do maior número: {maior}.")

input("\n\nPressione o \"enter\" para encerrar...")
