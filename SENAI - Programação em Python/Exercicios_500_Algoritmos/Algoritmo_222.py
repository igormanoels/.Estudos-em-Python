import os

os.system('cls')
'''
    Criar um algoritmo que entre com uma palavra e imprima 
    conforme o exemplo a seguir:
        palavra: PAZ
        Saída: ZAP
'''

palavra = input("Informe a palavra desejada: ")
quant = len(palavra)-1

while quant >= 0:
    print(palavra[quant])
    quant -= 1
    
input("\n\nPressione o \"enter\" para encerrar...")
