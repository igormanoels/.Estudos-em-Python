import os

os.system('cls')
'''
    A polícia rodoviária resolveu fazer cumprir a lei e cobrar dos motoristas o DUT. Sabendo-se que o mês em que 
    o emplacamento do carro deve ser renovado é determinado pelo último número da placa do mesmo, criar um 
    algoritmo que, a partir da leitura da placa do carro, informe o mês em que o emplacamento deve ser renovado.
'''

placa = input("Digite a placa do carro: ")

tmn = len(placa)
ultimoDgt = int(placa[tmn-1])

match ultimoDgt:
    case 1:
        print("\nO DUT precisa ser renovado em Janeiro.")
    case 2:
        print("\nO DUT precisa ser renovado em Fevereiro.")
    case 3:
        print("\nO DUT precisa ser renovado em Março.")
    case 4:
        print("\nO DUT precisa ser renovado em Abril.")
    case 5:
        print("\nO DUT precisa ser renovado em Maio.")
    case 6:
        print("\nO DUT precisa ser renovado em Junho.")
    case 7:
        print("\nO DUT precisa ser renovado em Julho.")
    case 8:
        print("\nO DUT precisa ser renovado em Agosto.")
    case 9:
        print("\nO DUT precisa ser renovado em Setembro.")
    case 0:
        print("\nO DUT precisa ser renovado em Outubro.")
    case _:
        print("\nA placa informada é inválida.")

input("\n\nPressione o \"enter\" para encerrar...")
