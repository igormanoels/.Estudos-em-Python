import os

os.system('cls')
'''
    Criar um algoritmo que leia um número que servirá para controlar os números 
    pares que serão impressos a partir de 2. Exemplo: 
    Quantos: 4      Saída: 2 4 6 8
'''
quant = int(input("Informe a quantidade de número pares que deseja saber a partir de zero: "))
c = 0
num = 0

print("Sequência:", end="  ")
while c != quant:
    if num % 2 == 0:
        print(f" {num}", end="  ")
        c += 1
    num += 1

input("\n\nPressione o \"enter\" para encerrar...")
