import os
os.system('cls')

'''
Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessariamente em ordem. 
Mostre os 4 números em ordem crescente.
'''

valorA = float(input("Informe o primeiro valor: "))
valorB = float(input("Informe o segundo valor: "))
valorC = float(input("Informe o terceiro valor: "))
valorD = float(input("Informe o quarto valor: "))

if valorD < valorA and valorD < valorB and valorD < valorC:
    print(valorD, ", ", valorA, ", ", valorB, ", ", valorC)
elif valorC < valorA and valorC < valorB and valorC < valorD:
    print(valorC, ", ", valorA, ", ", valorB, ", ", valorD)
elif valorB < valorA and valorB < valorC and valorB < valorD:
    print(valorB, ", ", valorA, ", ", valorC, ", ", valorD)
else:
    print(valorA, ", ", valorB, ", ", valorC, ", ", valorD)
