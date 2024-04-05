import os

os.system('cls')
'''
    Imprimir os 100 primeiros pares. 
'''

c = 0
numPar = 0

while numPar <= 100:
    if c % 2 == 0:
        print(c)
        numPar += 1
    c += 1
        
input("\n\nPressione o \"enter\" para encerrar...")
