import os

os.system('cls')
'''
    Criar um algoritmo que entre com uma palavra e imprime conforme 
    o exemplo a seguir:
        Palavra: Amor
        Saída: Amor
               Amo
               Am
               A
'''

palavra = input("Informe a palavra desejada: ")
quant = len(palavra)

for i in range(quant):
    print(palavra[0:quant-i])
    
input("\n\nPressione o \"enter\" para encerrar...")
    