import os

os.system('cls')
'''
    Criar um algoritmo que leia um número e imprima todos os números de 1 até o 
    número lido e o seu produto. Exemplo: 
        número: 3       Saída: 1 2 3 
                        6 
'''

num = int(input("Informe até onde contar: "))
c = 1
soma = 0

while c <= num: 
    soma += c
    c += 1

print(f"Somatória: {soma}")

input("\n\nPressione o \"enter\" para encerrar...")
