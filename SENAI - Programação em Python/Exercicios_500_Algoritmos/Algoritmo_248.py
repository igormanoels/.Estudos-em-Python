import os

os.system('cls')
'''
    Criar um algoritmo que entre com uma palavra e imprima 
    conforme exemplo a seguir: 
    palavra: SONHO 
    SONHO 
    SONHO SONHO 
    SONHO SONHO SONHO 
    SONHO SONHO SONHO SONHO 
    SONHO SONHO SONHO SONHO SONHO
'''

palavra = input("Informe a palavra desejada: ")
quant = len(palavra)

print("\n")
for i in range(quant):
    c = i + 1
    while c > 0:
        print(palavra, end=" ")
        c -= 1
    print("\n")

input("\n\nPressione o \"enter\" para encerrar...")