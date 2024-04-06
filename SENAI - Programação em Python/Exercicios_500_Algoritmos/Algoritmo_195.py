import os

os.system('cls')
''' 
    Criar um algoritmo que imprima a soma dos números pares entre 25 e 200. 
'''
soma = 0
c = 25

while c <= 200:
    if c % 2 == 0:
        soma += c
    c += 1

print(f"Somatória: {soma}")

input("\n\nPressione o \"enter\" para encerrar...")
