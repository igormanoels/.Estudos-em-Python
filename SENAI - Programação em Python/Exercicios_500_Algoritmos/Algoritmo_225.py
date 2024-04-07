import os

os.system('cls')
'''
    Cirar um algoritmo que entre com as palavras e imprima
    conforme o exemplo a seguir:
    Palavra:    Terra
    Saída:      a
                ra
                rra
                erra
                Terra
'''     

palavra = input("Informe a palavra desejada: ")
quant = len(palavra)

for i in range(quant):
    print(palavra[quant-1-i:])
    
input("\n\nPressione o \"enter\" para encerrar...")
