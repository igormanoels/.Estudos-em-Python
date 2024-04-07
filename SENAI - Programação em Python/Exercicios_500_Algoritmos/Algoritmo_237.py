import os

os.system('cls')
'''
    Ler o número de termos da série (n) e imprimir o valor de H, sendo:
'''

num = int(input("Informe o número desejado: "))
res = 0

for i in range(num):
    if i % 2 == 0:
        res -= (1 / (i+1))
    else:
        res += (1 / (i+1))
        
print("Resultado da série: ", res)

input("\n\nPressione o \"enter\" para encerrar...")
