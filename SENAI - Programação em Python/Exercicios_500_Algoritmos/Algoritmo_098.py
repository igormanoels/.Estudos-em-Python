import os

os.system('cls')
'''
    A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários estatutários. O valor máximo
    da prestação não poderá ultrapassar 30% do salário bruto Fazer um algoritmo que permita entrar com o salário
    bruto e o valor da prestação e informar se o empréstimo pode ou não ser concedido.
'''
sal = float(input("Informe o salário do funcionário: "))
emprest = float(input("Informe o valor do empréstimo: "))
parc = int(input("Informe a quantidade de parcelas: "))

prest = emprest / parc
prestMax = sal * 0.3

if (prest <= prestMax):
    print("\nEmpréstimo Aprovado!")
else:
    print("\nEmpréstimo Negado!")

input("\n\nPressione o \"enter\" para encerrar...")
