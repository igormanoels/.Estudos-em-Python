import os

os.system('cls')
# Fazer um algoritmo que possa entrar com o saldo de uma aplicação e imprima o novo saldo, considerando o reajuste de 1%.

saldo = float(input("Favor informar o saldo que será reajustado: "))
saldo = saldo * 1.01
saldoFormatado = "{:.2f}".format(saldo)

print("Saldo Reajustado: R$", saldoFormatado)
