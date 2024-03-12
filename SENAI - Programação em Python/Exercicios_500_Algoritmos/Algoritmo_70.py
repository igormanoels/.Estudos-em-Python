import os

os.system('cls')
'''
    Todo restaurante embora por lei não possa obrigar o cliente a pagar, cobra 10% para o garçom. 
    Fazer um algoritmo que leia o valor gasto com despesas realizadas em um restaurante e imprima o valor total com a gorjeta.
'''
consumo = float(input("Informe o valor da conta: R$ "))
gorjeta = round((consumo * 0.1) , 2)
pgmt = round((consumo + gorjeta), 2)

print(f"\n \t   Nota de Pagamento"
      f"\nConsumo..................R$ {consumo}"
      f"\nGorjeta..................R$ {gorjeta}"
      f"\nValor Final..............R$ {pgmt}")
input("\n\nPressione o \"enter\" para encerrar...")
