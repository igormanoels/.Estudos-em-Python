import os
os.system('cls')

'''
Receba o valor de um depósito em poupança. 
Calcule e mostre o valor após 1 mês de aplicação sabendo que rende 1,3% a. m.
'''

deposito = float(input("Informe o valor do deposito: "))

res = deposito * 1.013

print(f"Rendimento após um mês: R${res:.2f}")
