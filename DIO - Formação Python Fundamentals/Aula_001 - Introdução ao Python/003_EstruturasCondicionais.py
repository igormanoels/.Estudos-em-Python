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

# Escolha...caso
op = int(input("Menu de investimento \n1-Poupança \n2-Renda fixa \nDigite a opção desejada: "))
investimento = float(input("Informe agora o valor a ser investido: R$"))
match op:
    case 1:
        print(f"Montante após investimento R${(investimento*1.03):.2f}")
    case 2:
        print(f"Montante após investimento R${(investimento * 1.05):.2f}")
    case _:
        print("Opção inválida!")
# Outra forma
def classificar_numero(numero):
    match numero:
        case 1 | 2 | 3:
            return "Número pequeno"
        case 4 | 5 | 6:
            return "Número médio"
        case _:
            return "Número fora do intervalo"

numero = int(input("Digite um número entre 1 e 6: "))
print(classificar_numero(numero))
