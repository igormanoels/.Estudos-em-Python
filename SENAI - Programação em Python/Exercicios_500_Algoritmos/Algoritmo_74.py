import os

os.system('cls')
'''
    Para vários tributos, a base de cálculo é o salário mínimo. Fazer um algoritmo que leia o valor do salário mínimo 
    e o valor do salário de uma pessoa. Calcular e imprimir quantos salários mínimos ela ganha.
'''

salMin = float(input("Favor informar o valor do salário mínimo vigente: ")) # Em 2024 o valor é de R$ 1412,00
salFunc = float(input("Favor informar o salário do trabalhador: "))

qSalMin = round((salFunc / salMin) , 2)

print("\nA quantidade de \"Salários Mínimos\" recebida é de ", qSalMin)
input("\n\nPressione o \"enter\" para encerrar...")
