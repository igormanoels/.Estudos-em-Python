import os

os.system('cls')
'''
    Entrar com dez números (positivos ou negativos) e imprimir o 
    maior e o menor número da lista.
'''

lista = []

for i in range(10):
    num = int(input(f"Informe o {i+1}º número: "))
    lista.append(num)

maior = max(lista)
menor = min(lista)

print(f"Maior número: {maior} | Menor número: {menor}")

input("\n\nPressione o \"enter\" para encerrar...")
