import os
import math

os.system('cls')

ladoA = int(input("Informe o primeiro lado do triângulo: "))
ladoB = int(input("Informe o segundo lado do triângulo: "))
ladoC = int(input("Informe o terceiro lado do triângulo: "))

if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoA + ladoB:
    if ladoA > ladoB and ladoA > ladoC:
        maior = math.pow(ladoA, 2)
        lados = math.pow(ladoB, 2) + math.pow(ladoC, 2)
    elif ladoB > ladoC:
        maior = math.pow(ladoB, 2)
        lados = math.pow(ladoA, 2) + math.pow(ladoC, 2)
    else:
        maior = math.pow(ladoC, 2)
        lados = math.pow(ladoA, 2) + math.pow(ladoB, 2)
        
    if maior == lados:
        print("\nTriângulo Retângulo") 
    elif maior > lados: 
        print("\nTriângulo Obtusângulo") 
    else:
        print("\nTriângulo Acutângulo")    
else:
    print("\nNão podem ser lados de um triângulo.")

input("\n\nPressione o \"enter\" para encerrar...")
