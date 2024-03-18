import os

os.system('cls')
# Ler três números e imprimir se eles podem ou não ser lados de um triângulo. 
# Regra: a<b+c && b<a+c && c<a+b

ladoA = int(input("Informe o primeiro lado do triângulo: "))
ladoB = int(input("Informe o segundo lado do triângulo: "))
ladoC = int(input("Informe o terceiro lado do triângulo: "))

if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoA+ladoB:
    print("\nPodem ser lados de um triângulo.")
else:
    print("\nNão podem ser lados de um triângulo.")

input("\n\nPressione o \"enter\" para encerrar...")
