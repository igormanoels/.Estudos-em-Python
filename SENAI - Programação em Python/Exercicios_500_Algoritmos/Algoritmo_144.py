import os

os.system('cls')
'''
    O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de acordo 
    com o saldo médio no último ano. Fazer um algoritmo que leia o saldo médio de um cliente 
    e calcule o valor do crédito de acordo com a tabela a seguir. 
        - Imprimir uma mensagem informando o saldo médio e o valor do crédito. 
            SALDO MÉDIO PERCENTUAL 
            de O a 500  ------------->   nenhum crédito 
            de 501 a 1000   --------->   30% do valor do saldo médio 
            de 1001 a 3000  --------->   40% do valor do saldo médio 
            acima de 3001   --------->   50% do valor do saldo médio 
'''

saldoMedio = float(input("Informe o saldo médio do cliente: "))

if saldoMedio <= 500:
    print("Não há crédito disponível para este cliente.")
elif saldoMedio <= 1000:
    credito = saldoMedio * 0.3
    print(f"Crédito disponível: {credito}")
elif saldoMedio <= 3000:
    credito = saldoMedio * 0.4
    print(f"Crédito disponível: {credito}")
else:
    credito = saldoMedio * 0.5
    print(f"Crédito disponível: {credito}")
    
input("\n\nPressione o \"enter\" para encerrar...")
