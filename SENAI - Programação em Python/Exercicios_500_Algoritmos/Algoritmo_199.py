import os

os.system('cls')
'''
    Criar um algoritmo que leia os limites inferior e superior de um intervalo e imprima
    todos os números múltiplos de 6 no intervalo fechado. Suponha que os dados digitados 
    são para um intervalo crescente. Exemplo: 
        Limite inferior: 5          Saída: 6 12 
        Limite superior: 13
'''

limInf = int(input("Informe o limite inferior: "))
limSup = int(input("Informe o limite superior: "))

print("Sequência: ", end="")
while limInf <= limSup:
    if limInf % 6 == 0:
        print(f"{limInf}", end=" ")
    limInf += 1

input("\n\nPressione o \"enter\" para encerrar...")
