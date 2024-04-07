import os

os.system('cls')
'''
    a primeira e a última letra se a palavra for par, caso contrário a letra central
'''

palavra = input("Informe a palavra desejada: ")
quant = len(palavra)

if quant % 2 == 0:
    print(palavra[0],palavra[quant-1])
else: 
    print(palavra[int(quant/2)])
    
input("\n\nPressione o \"enter\" para encerrar...")
