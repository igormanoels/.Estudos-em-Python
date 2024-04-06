import os

os.system('cls')
'''
    Criar um algoritmo que leia um número que servirá para controlar os primeiros números
    ímpares. Deverá ser impressa a soma desses números. Suponha que num será maior que zero. 
        Quantos: 5      Saída: 25 
        ( 1 3 5 7 9) - primeiros ímpares
'''

quant = int(input("Informe a quantidade de números impares deseja ver: "))
c = 0
num = 0
soma = 0

print("Sequência:", end=" ")
while c != quant:
    if num % 2 != 0:
        soma += num
        c += 1
        print(f"{num}", end=" ")
    num += 1

print(f"\nSomatória: {soma}")

input("\n\nPressione o \"enter\" para encerrar...")
