import os
import math

os.system('cls')
'''
Ler três números, os possíveis lados de um triângulo, e imprimira classificação segundo os lados. 
    Para ser um triângulo - a<b+c && b<a+c&& c<a+b
    Triangulo equilatero - a == b && a == c
    Triangulo isosceles  - a == b || a==c || b==c
    Triangulo escaleno
'''

ladoA = int(input("Informe o primeiro lado do triângulo: "))
ladoB = int(input("Informe o segundo lado do triângulo: "))
ladoC = int(input("Informe o terceiro lado do triângulo: "))

if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoA+ladoB:
    if ladoA == ladoB and ladoA == ladoC:
        print("\nEsse é um Triângulo Equilatero.")
    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        print("\nEsse é um Triângulo Isosceles.")
    else:
        print("\nEsse é um Triângulo Escaleno.")
else:
    print("\nNão podem ser lados de um triângulo.")
    

input("\n\nPressione o \"enter\" para encerrar...") 
