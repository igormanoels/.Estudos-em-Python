import os
import math

os.system('cls')
'''
    Entrar com 15 números e imprimir a raiz quadrada de cada número. 
'''

for i in range(15):
    num = int(input("Informe o número desejado: "))
    raiz = math.sqrt(num)
    print(f"A raiz quadrada de {num} é ---> {raiz}\n")

input("\n\nPressione o \"enter\" para encerrar...")
    