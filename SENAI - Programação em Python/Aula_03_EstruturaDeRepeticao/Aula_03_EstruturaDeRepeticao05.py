import os
os.system('cls')

saldo = 1000

while (True):
    operacao = input("Digite a operação (Saque/Depósito/sair): ").lower()
    if (operacao == "sair"):
        print("Obrigado por realizar o nosso sistema.")
        break # O break retorna a condição para o while como false, e faz com que o programa encerre.
    elif (operacao == "saque"):
        valor = int(input("Digite o valor para saque: "))
        if (valor > saldo):
            print("Saldo insuficiente para saque.")
        else: 
            saldo = saldo - valor
            print(f"Saque realizado com sucesso! Saldo atual {saldo}")
    elif (operacao == "deposito"):
        deposito = float(input("Digite um valor para depósito: "))
        saldo = saldo + deposito
        print(f"Depósito realizado com sucesso! Saldo atual {saldo}")
    else:
        print("Operação inválida!")
