import os

os.system('cls')
'''
    Criar um algoritmo que entre com uma palavra e imprima conforme
    o exemplo a seguir:
        palavra:    TERRA
        Saída:      TERRA
                    ERRA
                    RRA
                    RA
                    A
'''

palavra = input("Informe a palavra desejada: ")
quant = len(palavra)

for i in range(quant):
    print(palavra[i:])
    
input("\n\nPressione o \"enter\" para encerrar...")
