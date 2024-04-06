import os

os.system('cls')
'''
    Criar um algoritmo que leia um número que será o limite superior de um intervalo 
    e imprimir todos os números ímpares menores do que esse número. Exemplo: 
        Limite superior: 15 
        Saída: 1 3 5 7 9 11 13 
'''

limSup = int(input("Informe o limite superior: "))
num = 0


print("Sequência: ", end="")
while num <= limSup:
    if num % 2 != 0:
        print(f"{num}", end="\t")
    num += 1    


input("\n\nPressione o \"enter\" para encerrar...")
