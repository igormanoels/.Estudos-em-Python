import os

os.system('cls')
'''
    imprima as letras de uma palavra de trás para frete
'''

palavra = input("Informe a palavra desejada: ")
quant = len(palavra)-1

while quant >= 0:
    print(palavra[quant], end="\t")
    quant -= 1

input("\n\nPressione o \"enter\" para encerrar...")
