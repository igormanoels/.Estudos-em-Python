import os
os.system('cls')

valorA = float(input("Informe o primeiro valor: "))
valorB = float(input("Informe o segundo valor: "))

if valorA > valorB:
    print(valorA,", ",valorB)
else:
    print(valorB,", ",valorA)
