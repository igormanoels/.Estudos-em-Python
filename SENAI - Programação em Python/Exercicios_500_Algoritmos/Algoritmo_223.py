import os

os.system('cls')
'''
    Criar um algoritmo que entre com uma palavra e imprima conforme
    o exemplo a seguir:
        palavra: AMOR
        Saída:  A
                AM
                AMO
                AMOR
'''

palavra = input("Informe a palavra desejada: ")
quant = len(palavra)

for i in range(quant+1):
    print(palavra[:i])
    
input("\n\nPressione o \"enter\" para encerrar...")
