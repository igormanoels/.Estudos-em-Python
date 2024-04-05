import os

os.system('cls')
'''
    Imprimir os múltiplos de 5, no intervalo de 1 até 500. 
'''
c = 1

while c <= 500:
    if c % 5 == 0:
        print(c)
    c += 1

input("\n\nPressione o \"enter\" para encerrar...")
