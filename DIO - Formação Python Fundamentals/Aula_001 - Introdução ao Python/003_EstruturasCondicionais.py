# Aula 01 - Conhecendo a Linguagem de Programação Python

import os
os.system('cls')

print("ESTRUTURA CONDICIONAL")
saldo = 1000
saque = float(input("Digite o valor do Saque: R$ "))

if saque < saldo:
    saldo -= saque
    print("Saque realizado com sucesso! Agora o saldo é R$", saldo )
else:
    print("Não há saldo suficiente! Saldo disponível R$", saldo)

# Opererador ternário
status = "Sucesso" if saldo >= saque else "Falha"
print(status)

limite = 500
print("\n\nESTRUTURA CONDICIONAL")
if saque <= saldo:
    if limite >= saque:
        saldo -= saque
        print("Saque realizado com sucesso! Agora o saldo é R$", saldo )
    else:
        print("Não há limite disponível para saque!")
else:
    print("Não há saldo suficiente! Saldo disponível R$", saldo)

