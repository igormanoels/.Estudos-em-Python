# Aula 01 - Conhecendo a Linguagem de Programação Python

import os
os.system('cls')

print("OPERADORES ARITIMÉTICOS")
print(5 + 4," ---> Adição")
print(5 - 4," ---> Subtração")
print(5 * 4," ---> Multiplicação")
print(5 ** 2," ---> Potenciação")
print(5 / 4," ---> Divisão")
print(5 // 4," ---> Parte inteira da divisão")
print(5 % 4," ---> Resto da divisão")


print("\n\nOPERADORES DE COMPARAÇÃO")
saldo = 500
saque = 200
print(saldo > saque, " ---> É maior")
print(saldo >= saque, " ---> É maior ou igual ")
print(saldo < saque, " ---> É menor")
print(saldo <= saque, " ---> É menor ou igual")
print(saldo == saque, " ---> É igual")
print(saldo != saque, " ---> É diferente")


print("\n\nOPERADORES DE ATRIBUIÇÃO")
saldo = 500
print(saldo, " ---> Saldo recebe valor")
saldo += 200
print(saldo, " ---> Recebe a soma de 200 ao valor presente")
saldo -= 450
print(saldo, " ---> Recebe a subtração de 200 ao valor presente")
# Pode ser utilizado com qualquer operador da mesma forma


print("\n\nOPERADORES DE LÓGICOS")
saldo = 500
saque = 200
LIMITE = 1000
contatos_emergencia = [] # Lista sem elementos


print(saldo > saque and saque <= LIMITE, " ---> É maior 'E' menor ou igual")
print(saldo > saque or saque == LIMITE, " ---> É maior 'OU' é igual")
print( not saldo > saque, " ---> Inverte, É maior")
print( not "Texto", " ---> Inverte, há texto")
print( not "", " ---> Inverte, não há texto")
print(not contatos_emergencia, " ---> Inverte, lista vázia")  


print("\n\nOPERADORES DE IDENTIDADE")
saldo = 500
saque = 200
print( saldo is saque, " ---> Verifica se ocupa a mesma posição de memória")
print( saldo is not saque, " ---> Verifica se não ocupa a mesma posição de memória")


print("\n\nOPERADORES DE ASSOCIAÇÃO")
cursos = ["Java", "Python", "C#", "C++", "Ruby", "Node"]
nome = "Igor Manoel de Santana"
print("Python" not in cursos, " ---> Verifica se não está")
print("Igor" in nome, " ---> Verifica se está")

