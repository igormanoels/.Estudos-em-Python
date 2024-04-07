import os

os.system('cls')
'''
    Criar um algoritmo que entre com uma palavra e se a palavra 
    tiver número ímpar de caracteres, imprima conforme o exemplo 
    a seguir; caso contrário, imprima: NÃO FACO
        palavra:    SONHO
                    N
                    ONH
                    SONHO
'''

palavra = input("Informe a palavra desejada: ")
quant = len(palavra)

if quant % 2 == 1:  # Verifica se a palavra tem um número ímpar de caracteres
    meio = quant // 2
    for i in range(meio + 1):
        print(" " * i + palavra[meio - i: meio + i + 1])
else:
    print("Não Faço!")

input("\n\nPressione o \"enter\" para encerrar...")
