import math
import os

os.system('cls')
''' Entrar com o lado de um quadrado e imprimir: 
        - Perimetro: 
        - Area: 
        - Diagonal: 
'''

lado = int(input("Favor informar o valor do lado do quadrado: "))

perimetro = lado * 4
area = math.pow(lado, 2)
diagonal = lado * math.sqrt(2)

print("\nPerimetro: ", perimetro,
      "\nArea: ", area,
      "\nDiagonal: ", diagonal)

input("\n\nPressione o enter para encerrar...")
