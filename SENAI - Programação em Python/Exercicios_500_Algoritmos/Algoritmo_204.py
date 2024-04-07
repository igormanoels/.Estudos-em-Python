import os
import math

os.system('cls')
'''
    Criar um algoritmo que leia um número da entrada (num), leia n números inteiros 
    da entrada e imprima o maior deles. Suponha que todos os números lidos serão 
    positivos. Exemplo:
'''

quant = int(input("Informe a quantidade de números desejadas: "))
maior = 0

for i in range(quant):
    while True:
        num = int(input(f"Informe o {i+1} número: "))
        if num >= 0: 
            maior = max(num, maior)
            break
        else: 
            print("Número inválido! Informe número positivos.")

print(f"\nO maior número é {maior}")

input("\n\nPressione o \"enter\" para encerrar...")
