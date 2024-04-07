import os

os.system('cls')
'''
    Criar um algoritmo que entre com uma palavra e imprima conforme 
    o exemplo a seguir:
'''

nome = input("Informe o nome desejado: ")
quant = len(nome)

for i in range(quant):
    print(nome[i])
    
input("\n\nPressione o \"enter\" para encerrar...")
