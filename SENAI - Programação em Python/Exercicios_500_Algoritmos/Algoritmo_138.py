import os

os.system('cls')
'''
    Ler um número inteiro entre 1 e 12 e escrever o mês correspondente. Caso o usuário digite um número fora desse 
    intervalo, deverá aparecer uma mensagem informando que não existe mês com este número. 
'''

mes = int(input("Informe o número para saber a qual mês ele corresponde: "))

match mes:
    case 1:
        print("Janeiro")
    case 2:
        print("Feveiro")
    case 3:
        print("Março")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case 6:
        print("Junho")
    case 7:
        print("Julho")
    case 8:
        print("Agosto")
    case 9:
        print("Setembro")
    case 10:
        print("Outubro")
    case 11:
        print("Novembro")
    case 12:
        print("Dezembro")

input("\n\nPressione o \"enter\" para encerrar...")