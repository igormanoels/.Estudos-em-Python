import os
os.system('cls')

# Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menos valor.

valorA = float(input("Informe o primeiro valor: "))
valorB = float(input("Informe o segundo valor: "))

if valorA > valorB:
    res = valorA - valorB
else:
    res = valorB - valorA

print(f"A diferença é de {res:.2f}")
