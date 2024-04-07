import os

os.system('cls')
'''
    Entrar com um nome e imprimi-lo tantas vezes quantos forem seus caracteres.
'''

nome = input("Informe o nome desejado: ")
quant = len(nome)

for i in range(quant):
    print(f"{i+1}º <--- {nome}.")
    
input("\n\nPressione o \"enter\" para encerrar...")
