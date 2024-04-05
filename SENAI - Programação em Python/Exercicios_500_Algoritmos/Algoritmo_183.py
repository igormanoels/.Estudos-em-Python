import os 
import math

os.system('cls')
'''
    Entrar com 10 números e imprimir o quadrado de cada número.
'''

for i in range(10):
    num = int(input("Informe o número desejado: "))
    quad = math.pow(num, 2)
    print(f"O quadrado de {num} é --> {quad}.\n")

input("\n\nPressione o \"enter\" para encerrar...")
