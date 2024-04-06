import os

os.system('cls')
'''
    Criar um algoritmo que leia um número (num) e imprima a soma dos números múltiplos 
    de 5 no intervalo aberto entre 1 e num. Suponha que num será maior que zero. 
        Limite superior: 15             Saída: 15 
        (5 10) - múltiplos de 5
'''

limSup = int(input("Informe o limite superior: "))
c = 0
soma = 0

while c <= limSup:
    if c % 5 == 0:
        soma += c
    c += 1
    
print(f"Somatória: {soma}")

input("\n\nPressione o \"enter\" para encerrar...")
