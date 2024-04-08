import os

os.system('cls')
'''
    Criar um algoritmo que entre com uma palavra e se ,a palavra tiver número ímpar de caracteres, 
    imprima conforme exemplo a seguir, caso contrário, imprima : NAO FACO: 
    palavra: SONHO 
    SONHO 
    SONHO SONHO SONHO 
    SONHO SONHO SONHO SONHO SONHO
'''

palavra = input("informe a palavra desejada: ")
quant = len(palavra)

if quant % 2 == 0:
    print("\nNão faço!")
else:
    print("\n")
    for i in range(quant):
        c = i + 1
        if c % 2 != 0:
            while c > 0:
                print(palavra, end=" ")
                c -= 1
            print("\n")
        
input("\n\nPressione o \"enter\" para encerrar...")
