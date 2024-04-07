import os

os.system('cls')
'''
    Entrar com 12 números e imprimir a média desses números.
'''
soma = 0

for i in range(12):
    num = int(input(f"Informe o {i+1}º número: "))
    soma += num

med = soma / 12

print(f"\nMédia: {med}")

input("\n\nPressione o \"enter\" para encerrar...")
