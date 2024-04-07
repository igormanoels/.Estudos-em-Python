import os

os.system('cls')
'''
    Entrar com oito nomes e imprimir quantas letras tem cada nome.
'''

for i in range(8):
    nome = input(f"Informe o {i+1}º nome: ")
    quant = len(nome)
    print(f"{nome} tem {quant} letras.\n")
    
input("\n\nPressione o \"enter\" para encerrar...")
