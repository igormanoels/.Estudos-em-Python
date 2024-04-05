import os

os.system('cls')
'''
    Criar um algoritmo que imprima todos os numeros de 1 ate 100 e a soma deles 
'''

soma = 0
c = 1

while c <= 100:
    print(c)
    soma += c
    c += 1

print(f"\n\nSomatória dos números de 1 a 100 = {soma}")

input("\n\nPressione o \"enter\" para encerrar...")
