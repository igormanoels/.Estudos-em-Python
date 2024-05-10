import os
os.system('cls')
'''
    Entrar com nomes enquanto forem diferentes de FIM e imprimir o primeiro caractere de cada nome.
'''

print("Algoritmo que imprime a primeira letra de cada nome")

while True:
    nome = input("Informe um nome, ou \"fim\" para encerrar: ").upper()
    if nome.__contains__("FIM"):
        print("Programa encerrado")
        break
    else:
        print(f"Primeira letra de {nome[0]}\n")

input("\n\nPressione o \"enter\" para encerrar...")
