import os

os.system('cls')
'''
    Ler o numero de termos da serie (n) e imprimir o valor de H sendo
'''

num = int(input("Informe a série: "))
res = 0
for i in range(num):
    res += (1 / (i+1))
    
print(f"Resultado da série: {res}")

input("\n\nPressione o \"enter\" para encerrar...")
    