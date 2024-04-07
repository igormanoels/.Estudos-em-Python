import os

os.system('cls')
'''
    Ler o numero de termos da serie (N) e imprimir o valor de 5 sendo
'''

num = int(input("Informe o número desejado: "))
res = 0
c = 0

while c < num:
    res += ((c + 1) / (num - c))
    c += 1

print("Resultado:", res)

input("\n\nPressione o \"enter\" para encerrar...")

