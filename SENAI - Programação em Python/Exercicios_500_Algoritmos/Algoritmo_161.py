import os
import math

os.system('cls')
'''
    Criar um algoritmo que entre com cinco números e imprimir 
    o quadrado de cada número. 
'''
c = 0

while (c < 5):
    num = int(input(f"Informe o {c+1} número para saber o seu quadrado: "))
    quad = math.pow(num, 2)
    print(f"O quadrado de {num} é ---> {quad}")
    c += 1


input("\n\nPressione o \"enter\" para encerrar...")
