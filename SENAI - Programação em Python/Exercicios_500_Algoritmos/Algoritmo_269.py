import os
import math
os.system('cls')
'''
    Entrar com números e imprimir o quadrado de cada número até entrar um número 
    múltiplo de 6 que deverá ter seu quadrado também impresso. 
'''

while True:
    num = int(input("Informe um número para descobrir o seu quadrado: "))
    print(f"O quadrado de {num} é {math.pow(num, 2)}\n")
    if num % 6 == 0: break

input("\n\nPressione o \"enter\" para encerrar...")
