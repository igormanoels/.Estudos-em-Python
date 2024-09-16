import os
os.system('cls')

# Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor

valorA = float(input("Informe o primeiro valor: "))
valorB = float(input("Informe o segundo valor: "))

if valorA > valorB:
    res = "É múltiplo." if valorA % valorB == 0 else "Não é múltiplo"
else:
    res = "É múltiplo." if valorB % valorA == 0 else "Não é múltiplo"

print(res)
