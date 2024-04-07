import os

os.system('cls')
'''
    Entrar com 12 nomes e imprimir o primeiro caractere de cada nome.
'''

for i in range(8):
    nome = input(f"Informe o {i+1}º nome: ")
    letra = nome[0].upper()
    print(f"a primeira letra de {nome} é ---> {letra}. \n")

input("\n\nPressione o \"enter\" para encerrar...")
