import os
import math

os.system('cls')
'''
    Imprimir o quadrado dos numeros de 1 ate 20 
'''

c = 1

while( c <= 20):
    quad = math.pow(c, 2)
    print(f"{c} ao quadrado é ---> {quad}")
    c += 1
    
input("\n\nPressione o \"enter\" para encerrar...")
