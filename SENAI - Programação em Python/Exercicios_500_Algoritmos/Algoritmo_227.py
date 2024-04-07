import os

os.system('cls')
'''
    Criar um algoritmo que entre com uma palavra e se a palavra tiver
    número ímpar de caracteres, imprima conforme o exemplo a seguir; 
    caso contrário, imprima:
        NÃO FACO
        palavra:    SONHO
                    SONHO
                    ONH
                    N
'''
palavra = input("Informe a palavra desejada: ")
quant = len(palavra)

for i in range(quant):      
    if quant % 2 == 0:
        print("Não Faço!")
        break
    else: 
        print(palavra[0+i:quant-i])

input("\n\nPressione o \"enter\" para encerrar...")
