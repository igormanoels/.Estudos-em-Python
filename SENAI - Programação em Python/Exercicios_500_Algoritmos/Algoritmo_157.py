import os

os.system('cls')
'''
    Criar um algoritmo que leia uma data (no formato ddmmaaaa) e 
    imprimir se a data e valida ou não
'''

data = input("Informe a data desejada: ")

lista = data.split('/')

ano = int(lista[2])
mes = int(lista[1])
dia = int(lista[0])

if ano > 1900 and ano <= 2024:
    if mes >= 1 and mes <= 12:
        if mes == 2:
            if dia < 30:
                print(f"Data válida: {dia}/{mes}/{ano}.")
            else:
                print("Data inválida.")
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia < 31:
                print(f"Data válida: {dia}/{mes}/{ano}.")
            else:
                print("Data inválida.")
        elif dia <= 31:
            if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 31:
                print(f"Data válida: {dia}/{mes}/{ano}.")
            else:
                print("Data inválida.")
    else:
        print("Data inválida.")
        
'''
    1 = 31      4 = 30      7 = 31      10 = 31
    2 = 28      5 = 31      8 = 31      11 = 30
    3 = 31      6 = 30      9 = 30      12 = 31
'''    

input("\n\nPressione o \"enter\" para encerrar...")
