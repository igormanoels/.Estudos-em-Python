import os

os.system('cls')

# Entrar com quatro números e imprimir a média ponderada, sabendo-se que os
# pesos são respectivamente: 1, 2, 3 e 4.

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
n3 = int(input("Informe o terceiro número: "))
n4 = int(input("Informe o quarto número: "))

media = ((n1 + n2 + n3 + n4)/4)
print("Média: ", media)
